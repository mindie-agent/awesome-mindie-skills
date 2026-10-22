---
name: ascend-memcache-pooling
description: Deploy and inspect Ascend A3/A5 MemCache KV pools over SDMA, UB, UBoE or supported Host RoCE; plan DRAM/SSD owners, preserve P/D transfer, and monitor multi-DP HBM, external reuse and SSD readback evidence.
---

# Ascend MemCache pooling

Use for two-tier (inference HBM + MemCache DRAM) or three-tier (+ UBSIO SSD) deployment, cache-hit diagnosis and read-only periodic monitoring. Preserve the user's model, inference framework, parallel topology, IP family, runner, quantization, MTP and working launch commands. P/D disaggregation is optional; its KV transport is separate from the pool data plane. No workspace-specific remote coordinator is required.

## Select the route

| Hardware / pool transport | Storage ownership | Three-tier extension |
| --- | --- | --- |
| A3 HCCS, `device_sdma` | Meta, per-node standalone owners, then zero-DRAM inference clients | SSD on owners only |
| A5 UB, `device_urma` | Meta, then contributing inference workers | SSD on actual owners |
| A5 UBoE, `device_uboe` | Same ownership recipe with verified device UBoE links | Preserve UBoE while adding SSD |
| A5 Host RoCE, `device_rdma` | Release-supported owners with physical NPU/NIC mapping | Preserve Host RoCE while adding SSD |

These are deployment recipes with release-specific support, not a hardware certification matrix. A3 standalone addresses SDMA window pressure; A5 fused workers are not a hardware requirement. Do not infer UBoE support for all Pod variants from a Server example.

- For deployment, read [deployment](references/deployment.md); for Host RoCE or P/D composition, also read [transports and integration](references/transports.md).
- For cumulative refresh, interval deltas or independent DP API ports, read [monitoring](references/monitoring.md) and use [cache_metrics.py](scripts/cache_metrics.py). Monitoring only sends GET requests; it does not send inference, reset caches or restart services.
- For a requested hit-rate/performance target, read [controlled validation](references/validation.md). The monitor alone cannot establish SSD physical readback, correctness, TTFT/TPOT or throughput acceptance.
- For provenance, release conflicts or contribution licensing, read [sources](references/sources.md) and [NOTICE](NOTICE).

## Workflow

1. Discover the intended hosts/containers, devices, process ownership, disk allocation, endpoints, installed package paths/versions, source revisions and existing model commands. Record pool transport and P-to-D transport separately. Inspect first; ask only for decisions that block the requested work.
2. Prepare explicit per-role configurations and minimal launch scripts from the installed release's templates. Record actual owner counts, per-owner DRAM, total DRAM, transport staging, UBSIO buffers, disk capacity, high/low eviction watermarks and layerwise choice. `world_size` is a member limit, not actual pool capacity. Explain proposed changes and their basis; apply within existing user authorization without asking for it again. Template/default values do not imply authorization to initialize a disk or change global host/network settings.
3. If deployment was requested, start Meta, standalone owners if selected, inference, then an optional P/D proxy after both roles are ready. Reuse a healthy matching owned deployment when appropriate. Keep logs and process identities, use `set -o pipefail` with `2>&1 | tee server.log`, and avoid restart loops. A preparation-only task stops at reviewable scripts/configs.
4. Validate a cold write and successful request, then request-correlated external reuse with HBM history accounted for. For P/D, verify P-to-D transfer separately. For SSD, validate write/evict/readback and device evidence; capacity, exist hits and flush bytes are insufficient.
5. If benchmarking was requested, freeze the workload and compare matched OFF/ON cases. Tune only within the authorized resource/load range and preserve each attempt. Report unmet targets rather than converting low-load latency into a capacity claim.
6. Deliver commands, effective configs, versions, source/data hashes, capacities, evidence and unresolved boundaries. Distinguish service ready, external reuse verified, SSD readback verified and performance accepted. Clean up only resources belonging to this task.

No fixed model, host, device mask, disk size or benchmark threshold is built into this skill. Layerwise, hybrid KV and unequal TP require explicit support in the selected framework/release. A pool reset is not an HBM-only reset; inspect the installed API's scope before proposing destructive cache operations.
