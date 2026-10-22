# Deployment guide

Follow common setup, choose the A3 or A5 path, add SSD only for three-tier pooling, then validate the selected route.

- [Common setup and launch](#common-setup-and-launch)
- [A3: HCCS / SDMA](#a3-hccs--sdma)
- [A5: choose UB or UBoE explicitly](#a5-choose-ub-or-uboe-explicitly)
- [Add SSD to an established DRAM pool](#add-ssd-to-an-established-dram-pool)
- [Validate the selected route](#validate-the-selected-route)

## Common setup and launch

Sources: the pinned MemCache config/install/compatibility docs and MemFabric installation docs in [sources](sources.md).

### Inspect before installing

Use the intended runtime interpreter:

```bash
python3 -m pip show memcache-hybrid memfabric-hybrid vllm vllm-ascend
python3 -m pip check
npu-smi info
uname -r
getconf PAGESIZE
free -h
```

Record package paths, package versions, repository commits and local patches. MemCache's dependency metadata selects its MemFabric range; resolve that range before pinning both versions. Prefer a compatible existing image. If installing, use explicitly selected compatible wheel versions for the target architecture/Python, then verify imports in that interpreter. Do not upgrade a running environment just because the Wiki says latest. The historical SSD introduction uses 1.2.0; it does not establish that every later UBSIO setting exists in that wheel.

Current MemFabric installation docs require a HYBM AICPU operator for A5 (and A2 device_rdma via hcomm). For versions exposing `mfcli`, inspect `mfcli kernel info`, then use `mfcli kernel install` when installation is needed and within scope; the current standalone kernel build requires CANN >=9.1.0. Older packages have different delivery flows: use their documentation. Do not replace that procedure universally with an import side effect.

Containers must see their allocated NPU devices, required driver/CANN libraries, transport devices and shared memory; SSD owners additionally need the selected raw block devices. Reuse a site-approved container definition. No generic requirement to launch every container privileged or mount the entire host filesystem.

### Configuration

Locate installed templates instead of assuming a Python path:

```bash
python3 -c 'from pathlib import Path; import memcache_hybrid; print(Path(memcache_hybrid.__file__).resolve().parent / "config")'
```

Copy `mmc-meta.conf` and `mmc-local.conf` into the deployment directory. Preserve release-specific settings. These are substitutions, not literal runnable values:

```ini
## meta.conf: one reachable control-plane endpoint per deployment
ock.mmc.meta_service_url = tcp://<META_HOST>:5000
ock.mmc.meta_service.config_store_url = tcp://<CONFIG_HOST>:6000
ock.mmc.meta_service.metrics_url = http://<METRICS_BIND_HOST>:8000
```

```ini
## local.conf: all participants agree on Meta / ConfigStore
ock.mmc.meta_service_url = tcp://<META_HOST>:5000
ock.mmc.local_service.config_store_url = tcp://<CONFIG_HOST>:6000
ock.mmc.local_service.world_size = 256
ock.mmc.local_service.protocol = <SELECTED_PROTOCOL>
ock.mmc.local_service.dram.size = <PER_OWNER_CAPACITY>
ock.mmc.local_service.max.dram.size = <RELEASE_SUPPORTED_RESERVATION>
ock.mmc.local_service.storage.enabled = false
```

`world_size` is the maximum rank count in the inspected template, not the model TP/DP count; count standalone and inference participants and keep it stable after registration. Inspect the selected release's reservation constraints before choosing `max.dram.size`. For device protocols, current templates describe 1GB capacity alignment. Actual DRAM capacity is the sum of aligned per-owner allocations. Separate MemCache DRAM from UBSIO buffers, model/runtime host memory and OS reserves; `max.dram.size` is not proof of registered physical capacity.

A minimal `run_meta.sh` contains:

```bash
export MMC_META_CONFIG_PATH=/absolute/deployment/meta.conf
python3 -c 'from memcache_hybrid import MetaService; MetaService.main()'
```

### Inference integration

Set `MMC_LOCAL_CONFIG_PATH` in each inference launcher. Retain the working model/parallel arguments; for a colocated vLLM Ascend service, the official integration example adds:

```bash
--enable-prefix-caching --kv-transfer-config '{"kv_connector":"AscendStoreConnector","kv_role":"kv_both","kv_connector_extra_config":{"backend":"memcache"}}'
```

This fragment is not a complete model launch command. Confirm connector registration and accepted extra fields in the installed vllm-ascend. Do not blindly add `use_layerwise`, a module path or a connector from another release. Hybrid models and layerwise transfer require matching layout support in that release.

For PD, preserve the working P-to-D connector and role topology. Compose pooling through the framework's supported multi-connector mechanism; replacing the transfer connector with the store connector breaks PD. Do not assume that `kv_both` from the colocated example is the correct role for every PD child connector. Generate P/D/proxy scripts only when PD was requested.

## A3: HCCS / SDMA

Sources: MemCache A3 standalone case, compatibility table, and MemFabric connectivity guide in [sources](sources.md).

1. Check the installed-release compatibility matrix. The inspected A3 SDMA table specifies HDK >=25.5.1, LingQu L1 >=1.5.0 (prefers 1.5.1), kernel >=5.10, and SDMA scope within the supernode. Its firmware troubleshooting entry names >=7.8.0.6.201. Do not substitute an Ethernet-connected pair for an HCCS-connected supernode.
2. Query the allocated devices with `hccn_tool -i <ID> -vnic -g`; check peer HCCS paths using `hccn_tool -i <ID> -hccs_ping -g address <PEER_VNIC_IP>`. Validate all intended edges, including direction. Check TLS consistency without automatically disabling it. Use a small MemFabric transfer to confirm the actual data path.
3. SDMA addressability, not just `free -h`, limits pool capacity. The Wiki's roughly 680GB on a 2TB host is an example. Use the matching MemFabric `mem_scan.py` before loading model weights and budget from measured addressable space. Cache dropping, memory compaction, BIOS changes and reboots are conditional host operations, not routine launcher steps.
4. Prepare two local configs per node. In both, set `device_sdma` and the same Meta/ConfigStore endpoints. The owner config uses the measured DRAM budget; inference config uses `dram.size = 0GB`. The Wiki example reserves `max.dram.size = 1024GB` in both; verify the installed release accepts this consumer/owner arrangement. Do not apply the general template's nonzero-capacity comment to reject the documented standalone consumer without checking code.
5. Start one storage owner per node before model loading. A minimal `memcache_standalone.py`, adapted from the official case:

```python
import time
from memcache_hybrid import DistributedObjectStore

store = DistributedObjectStore()
result = store.init(0)  # select the intended visible device for this owner
if result != 0:
    raise SystemExit(f"MemCache init failed: {result}")
print("MemCache storage owner ready", flush=True)
while True:
    time.sleep(1)
```

Run with its storage config:

```bash
export MMC_LOCAL_CONFIG_PATH=/absolute/deployment/mmc-local-standalone.conf
python3 memcache_standalone.py
```

Wait for every owner to initialize and register, then launch inference with the zero-DRAM client config. Keep owners alive for the service lifetime. Two-tier owners have storage disabled. Three-tier owners apply [SSD settings](#add-ssd-to-an-established-dram-pool); zero-DRAM inference clients keep SSD disabled. One owner sharing a node's disk means `ubsio.standalone.device_count = 1`, regardless of inference TP/DP.

## A5: choose UB or UBoE explicitly

Sources: MemCache 950DT/950PR protocol guide, MemFabric connectivity, operator installation and hugepage guides in [sources](sources.md).

| Topology | MemCache protocol | Network evidence |
| --- | --- | --- |
| Device UB | `device_urma` | actual UB EIDs and small successful transfer |
| Device UBoE | `device_uboe` | device bond IP/gateway, UBoE link and small successful transfer |

The protocol guide describes 950 Pod UB using six external ports, and 950 Server UB using die0 external ports versus UBoE using a die1 parameter-plane port. Treat that as the documented hardware scope, not a port-count rule for all A5 products. The guide does not establish UBoE support for every Pod variant.

Check `urma_admin show` for UB EIDs. For UBoE, inspect each allocated device:

```bash
hccn_tool -g -dev_info -i <ID>
hccn_tool -g -ip -i <ID> -d <BOND_NAME>
hccn_tool -g -gateway -i <ID> -d <BOND_NAME>
hccn_tool -t -ping -i <ID> -src_address <LOCAL_BOND_IP> -dst_address <PEER_BOND_IP> -pkt 1024
```

Use the actual bond name/tool syntax from the installed driver. Management NIC IP, Meta TCP address, NPU bond IP and UB EID are different identifiers. A successful Meta connection cannot establish device transport health. For UB, use the official connectivity guide's `urma_perftest` recipe with discovered local/peer EIDs, then a MemFabric transfer in the deployment environment.

Start from the working CANN/driver environment and verify HYBM operator installation as described in [common setup](#common-setup-and-launch). A separate HIXL/Mooncake P-to-D engine may need its own endpoint/protocol settings; MemCache's `protocol` does not configure that engine. Preserve a working endpoint configuration rather than synthesizing HIXL variables from this MemCache guide.

For a fused deployment, set per-worker DRAM in local.conf and start Meta then inference. Example: four actual storage workers at 25GB each contribute about 100GB before accounting for allocation alignment. Count actual storage workers; do not assume every API server, DP rank or TP rank contributes storage. All participants in one intended pool use compatible endpoints and transport.

For two tiers set `storage.enabled = false`. For three tiers, apply [SSD settings](#add-ssd-to-an-established-dram-pool) to contributing workers and set the UBSIO process count to actual disk-sharing owners on each host.

Hugepage requirements depend on MemFabric allocator/version. Inspect the selected page size and per-NUMA `nr_hugepages` and `free_hugepages`; configured targets are not available capacity. The A5 1GB tutorial includes platform-specific boot/register changes, which are not universal prerequisites. Do not copy register writes, disable signature verification or change boot configuration as an implicit deployment step. If required by the exact platform/release, state the concrete change and obtain the host owner's authorization if not already granted.

For `device_urma` error 507018, only apply the Wiki's legacy `import memfabric_hybrid` workaround when plog also identifies `libcann_hybm_kernel.so` / `HybmBatchWrite`. Newer operator packaging uses `mfcli`; arbitrary UBoE or stream failures are not this diagnosis.

## Add SSD to an established DRAM pool

Sources: MemCache SSD introduction and detailed UBSIO guide in [sources](sources.md). The transport choice remains A3 SDMA, A5 UB or A5 UBoE; SSD is an additional storage backend, not a network protocol.

### Device ownership and memory

Check on the SSD host:

```bash
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
findmnt --source /dev/<TARGET>
```

Also check child partitions, swap, holders and existing consumers before assigning a device. Use only an explicitly allocated exclusive cache device with no mounted filesystem or data to preserve. A partition or loop device is supported by the detailed guide, but is not automatically equivalent in performance to a dedicated NVMe. Expose it to the owner container. Never run partitioning, formatting, `wipefs` or force initialization just to make a launch succeed.

Apply to storage owners, not A3 zero-DRAM clients:

```ini
ock.mmc.local_service.storage.enabled = true
ubsio.disk.path = /dev/<EXCLUSIVE_CACHE_DEVICE>
ubsio.mem.size_in_gb = 10
ubsio.standalone.device_count = <OWNERS_SHARING_DISKS_ON_THIS_HOST>
ubsio.standalone.force_new_disk = false
ubsio.wcache.evict_water_level = 0
```

These are template values requiring release validation. Multiple disk paths use colons. `device_count` is not the disk count or cluster-wide NPU count. For one A3 standalone owner use 1. Every owner must agree on the disk-sharing layout.

UBSIO memory is additional to MemCache DRAM. The detailed guide requires at least 5GB per process for SSD, suggests 10GB for fused deployment and 50GB for standalone, bounded by remaining host memory divided by owner count. The introduction also mentions 80GB for A3: that is not a universal minimum. Use an explicit budget; do not allocate all reported free memory or silently shrink to an unsupported size.

### Resolve documentation conflicts before launch

- The introduction says its release lacks recovery and requires `force_new_disk=true`; the detailed guide says `false` loads compatible disk metadata. The template above preserves existing layout only if supported. Check the installed UBSIO release and disk metadata. If initialization is required, stop and obtain explicit authorization for that identified cache device; do not retry with true automatically. False is not a promise of recovery after a crash.
- The detailed guide spells the scratch setting as both `ubsio.batch_read.standalone.use_scratch_pool` (table) and `ubsio.bdm.batch_read.standalone.use_scratch_pool` (body). It requires scratch buffering on A3 and suggests disabling it elsewhere to avoid a copy. Verify the accepted key in the installed UBSIO parser/defaults and effective startup configuration; do not set both spellings and assume it worked. Keep A3 scratch enabled; if it cannot be verified, do not claim that three-tier deployment is ready.
- An old wheel may not expose newer L2.5, scratch or BDM options. Omit unsupported optimizations rather than treating ignored keys as enabled features.

### Eviction and readback

For a version supporting these Meta settings, a tuning example is:

```ini
ock.mmc.evict_threshold_high = 70
ock.mmc.evict_threshold_low = 60
```

This is not a required replacement for defaults (the introduction lists 90/80). Keep low below high and leave room for a batch allocation plus concurrent requests. The introduction's allocation-size warning is release-specific; verify actual allocator behavior when a large Put fails rather than assuming a disk can compensate for arbitrarily small DRAM.

UBSIO L2.5 is a separate host-memory write cache. With a disk configured, `ubsio.wcache.evict_water_level=0` is the documented way to push writes toward L3 promptly. A high value can keep data in L2.5; an external hit or UBSIO hit then does not prove disk readback. Do not conflate L2.5 usage with MemCache DRAM registration.

Validate store -> DRAM pressure/eviction -> physical SSD write -> repeat request -> SSD readback -> successful request. Increase distinct prefixes to displace HBM before reducing DRAM. Stop on unsupported configuration, disk ownership ambiguity or repeated allocation/read errors; preserve the first failure evidence instead of changing topology or initializing the disk.

## Validate the selected route

1. Record Meta registration and actual owner count/capacity. Confirm inference health and complete one request. In PD, verify P-to-D transfer and proxy routing as well.
2. Warm distinct shared prefixes, then query them again with new suffixes. Control the request route and DP coverage. If everything stays in HBM, enlarge the prefix working set or use a supported targeted cache-reset operation; restarting the whole pool invalidates this check.
3. Capture before/after deltas for all participating inference engines and Meta during the same window. Exclude warmup from formal performance. Verify external reuse independently from service readiness.
4. For SSD, require actual write/eviction/readback evidence and a successful consuming request. Native metrics, logs and a controlled workload are the first choice. `iostat -dxm -y <DEVICE> 2` shows interval device bandwidth but includes unrelated traffic and cannot prove useful KV hits. Kernel-bypass I/O may not be represented. Do not add custom statistics code unless requested.
5. Keep the user's performance metric and baseline. For a no-history-reuse baseline, disable HBM and external history reuse while retaining PD KV transfer. A two-tier versus three-tier comparison is a different experiment. Do not promise 4x, 90% hits or an SSD share from an unrelated historical model/run.

For matching token counters, combined reuse = (HBM hit + external hit) / HBM query. Equivalently H + (1-H)*E only when external query equals HBM query minus HBM hit. Never add conditional percentages or mix periods. SSD key-hit share is an object-count metric, not automatically a token/byte share for hybrid/layerwise layouts. Label the user's chosen SSD denominator and method; omit an unsupported exact attribution claim.

When a benchmark is requested, use an existing supported tool such as AISBench and preserve its native output and success/failure counts. Deliver commands, resolved configurations, source/package versions, data parameters/hash, warmup boundaries, logs and metrics. This skill includes no fixed benchmark wrapper or SSD tracing library.
