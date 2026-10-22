# Transport and inference integration

Use the [deployment guide](deployment.md) for A3 SDMA and A5 UB/UBoE. This supplement captures A5 Host RoCE and P/D distinctions from the workspace-authored pooling guide; it is not a claim that every release/topology supports every combination. Pin package versions, loaded paths, configuration and physical mappings before reuse.

## Independent data planes

| Pool configuration | Meaning | Separate P/D choice, if requested |
| --- | --- | --- |
| `device_urma` | A5 UB pool | Preserve working UB/UBG or other supported P/D transport |
| `device_rdma` | Supported Host RoCE pool | Explicit `roce:host` endpoints when P/D also uses Host RoCE |
| `device_uboe` | Device UBoE pool | Explicit `uboe:device` when selected for P/D |

Meta TCP, configuration-store TCP, metrics HTTP and pool transport addresses serve different purposes. Selecting `ub_rtp:device` for a P/D engine does not prove that the pool uses UBG. Do not inject HIXL P/D variables into every pool route.

## A5 Host RoCE

Verify `device_rdma` support in the selected MemCache/MemFabric build. Record NPU physical IDs, container-visible IDs, NIC/GID/IP, source policy routes, MTU, driver and NUMA placement. A site topology name such as 1825 is not a protocol enum. Preserve IPv4/IPv6 and existing networking; do not copy another host's route or HCCN files.

The workspace recipe used the following MemFabric environment; validate each variable against the installed release and include staging in the host-memory budget:

```bash
export MF_HYBM_RDMA_SWAP_SPACE_SIZE=2048
export MF_HYBM_RDMA_FORCE_UNREGISTERED=1
export MF_HYBM_RDMA_USE_HCOMM=1
```

When P/D also selects Host RoCE, its HIXL configuration can use:

```bash
export ASCEND_GLOBAL_RESOURCE_CONFIG='{"comm_resource_config.protocol_desc":["roce:host"]}'
```

The working resource-loader entrypoint determines whether the endpoint directory is configured on the outer multi-connector, its P/D child, or both. Inspect that implementation; retain matching paths. One physical-card endpoint template is:

```json
{
  "version": "1.3",
  "net_instance_id": "<actual-network-instance>",
  "endpoint_list": [
    {"protocol": "roce", "comm_id": "<physical-card-host-roce-ip>", "placement": "host"}
  ]
}
```

Use the supported filename such as `ub_endpoint_npu_<physical_id>.json`. Verify MemFabric's HCCN address and the HIXL endpoint refer to the intended physical card/NIC. A container-private `hccn.conf` must retain all release-required keys. The control socket NIC need not be the RoCE NIC. Do not derive physical mapping from logical rank numbers or infer RDMA success from TCP/HTTP health.

Inspect allocated transport devices, driver libraries, shared memory and per-NUMA free hugepages without changing them. Device exposure must follow the site's supported container policy; where that policy exposes all physical NPU nodes, express the authorized runtime subset with `ASCEND_RT_VISIBLE_DEVICES`. Never remap a live service's devices.

## Preserve P-to-D KV transfer

For colocated serving, use the supported `AscendStoreConnector` integration in deployment.md. For P/D, retain the existing transfer connector (for example a supported Mooncake standard or hybrid connector) and compose the store connector through the installed framework's multi-connector implementation. Preserve role, KV port, DP/TP, block size, scheduler and model flags; `kv_both` from a colocated example is not universally correct for a P/D child.

Inspect `backend=memcache`, `use_layerwise`, lookup RPC allocation and endpoint-loading keys in the exact deployed code. P-side layerwise is optional and model/runner dependent; keep D-side layerwise disabled where required by that implementation. Independently validate all involved KV groups and asynchronous completion. Do not silently substitute a pooled P-to-Pool-to-D handoff design for an existing direct P-to-D connector.

Use the same supported hash configuration (including `PYTHONHASHSEED`) for compatible participants. Incompatible KV layouts, model revisions or TP slices need a supported namespace or separate pool. A changed salt is not an acceptable way to preserve identical OFF/ON prefix data in a controlled comparison.
