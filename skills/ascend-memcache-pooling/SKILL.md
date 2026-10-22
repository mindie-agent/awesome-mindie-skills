---
name: ascend-memcache-pooling
description: Deploy MemCache and MemFabric KV pools on Ascend A3 or A5 (UB/UBoE), selecting HBM+DRAM or HBM+DRAM+SSD, configuring storage owners and inference clients, and verifying external reuse and SSD readback.
---

# Ascend MemCache pooling

Use for two-tier (inference HBM + MemCache DRAM) or three-tier (+ UBSIO SSD) deployment. Preserve the user's inference framework, model, parallel layout and existing working launch commands. vLLM Ascend is the concrete integration example here; another framework needs its own supported connector. PD disaggregation is optional and is not synonymous with pooling. This skill is self-contained and does not require a workspace-specific SSH coordinator.

## Select the deployment

| Hardware / transport | Two-tier route | Three-tier route |
| --- | --- | --- |
| A3 HCCS, `device_sdma` | Meta, then per-node standalone storage, then inference clients contributing 0GB | Same ordering; enable SSD on storage owners only |
| A5 UB, `device_urma` | Meta, then inference workers contributing DRAM | Enable SSD on those storage owners |
| A5 UBoE, `device_uboe` | Same ownership pattern with verified UBoE links | Same SSD extension, retaining UBoE transport |

A3 standalone is the documented remedy for SDMA address-window pressure, not a claim that fused deployment is impossible. A5 fused workers are a recipe, not a hardware requirement. Do not infer UBoE support for every A5 Pod from the Server example. These are documentation-derived deployment routes, not a six-case hardware certification.

1. Discover the actual hosts/containers, NPU IDs, network topology, installed packages, inference source revision, model and working command. Ask only for missing decisions such as storage budget or a disk that may be initialized. Read [common setup](references/deployment.md#common-setup-and-launch).
2. Follow the hardware-specific section in the [deployment guide](references/deployment.md), including its SSD section for three tiers. Follow the installed release's configuration, not an unrelated current Wiki example.
3. Prepare explicit per-role configurations and minimal launch scripts. Keep Meta, storage owner (A3), inference, and optional PD proxy separate. Put inference environment and command in one script, with `set -o pipefail` and `2>&1 | tee server.log`. Do not add restart loops or benchmark orchestration unless requested.
4. Start Meta, all standalone owners if used, inference, then a PD proxy after both roles are ready. Check each stage once from outside the launchers. Reuse an existing healthy matching deployment when authorized; do not start competing owners over the same disk.
5. Verify a real request and external reuse using [validation](references/deployment.md#validate-the-selected-route). Three-tier success additionally needs SSD write/evict/readback evidence; registered capacity alone is insufficient. Keep SSD attribution aligned with the user's chosen method; do not inject custom tracing by default.
6. Deliver launch commands, effective configuration, versions, actual owner counts/capacities and evidence paths. Report separately: service ready, external reuse verified, SSD readback verified, performance tested. Stop only owned failed processes; restore prior configuration when a change fails, retaining logs.

## Sources and version boundaries

Read [source ledger](references/sources.md) when checking provenance or resolving conflicting instructions. It pins both official Wiki repositories and implementation documentation as inspected on 2026-10-19. Designs marked WIP are not deployment guarantees. Never import private machine addresses, credentials, historical benchmark thresholds or custom patches into a generic recipe without stating their scope.
