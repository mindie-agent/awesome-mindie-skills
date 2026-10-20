# blue-server-toolkit initial catalogue review

- Review date: 2026-10-20.
- Source: [xuchi-0808/blue-server-toolkit](https://github.com/xuchi-0808/blue-server-toolkit).
- Upstream revision: `5707a86922713f830f1f5fea2bedbb0a0a1cdc3a`, resolved from GitHub `main`.
- Maintainer: xuchi-0808.
- License: MIT; the pinned revision's LICENSE names the copyright holder `xuchi-0808`.
- Scope: seven entrypoints under `skills/` selected for Ascend engineering environment support. This review supersedes the single-entry draft previously pinned at revision `b9f5529774c67482696c830b91af25a39c82c949`; upstream restructured its monolithic `SKILL.md` into a seven-skill plugin at version 3.0.0.

## Inspection method

The upstream repository was cloned locally and inspected at the pinned revision. Inspection covered the plugin manifest (`.claude-plugin/plugin.json`), the README, the CHANGELOG, the shared skill-contract template, the configuration template, helper scripts, and all seven `SKILL.md` definitions. Each catalogue entry stores the SHA-256 of its pinned upstream `SKILL.md` bytes; remote verification is performed by `python3 scripts/validate_catalog.py --check-remote`, and local verification by `--source-root` against a clone held at the recorded revision.

## Entry coverage

| Catalogue entry | Category | Coverage |
|---|---|---|
| `blue-server-toolkit` | delivery | Daily-operations hub: SSH connection checks and stability (ControlMaster multiplexing), code sync, UT execution, model download, log viewing, container management, file transfer, image mirrors, configuration management; routes to the sibling skills. |
| `blue-npu-ops` | delivery | Single-server NPU operations: npu-smi reading, HBM usage and orphan release, precise-PID leftover-process cleanup, idle checks, A3 chip numbering, torch FLOPS measurement. |
| `blue-npu-fabric` | debugging | Cross-machine NPU data-plane and fabric identity: hccs_ping RoCE checks and false positives, firewalld host-TCP blocking, 950DT (A5) rootinfo/ub_endpoint/urma_admin, EID drift; routed by EI error codes. |
| `blue-server-provisioning` | environment | Fresh-server and container bring-up: bare-metal HDK driver and firmware installation (driver before firmware, HwHiAiUser), start-docker-A2/A3/A5.sh container creation, image-ID discipline. |
| `blue-vllm-ascend-build` | environment | Source build and upgrade of vllm-ascend: editable two-step install, version pairing via vllm-main-verified.commit, setuptools 77+, pip mirror setup, rsync-then-chown; pure CPU. |
| `blue-vllm-profiling` | profiling | vLLM-on-Ascend profiling capture and interpretation: launch flags, /start_profile and /stop_profile, steady-state windows, per-rank analyse(), step_trace_time buckets, operator attribution, bottleneck triage. |
| `blue-vllm-service` | serving | vLLM-on-Ascend service lifecycle: start/stop vllm serve in containers, health checks, multi-service layout, P/D disaggregated bring-up (mooncake, load-balance proxy), TP and parallelism planning, graph-mode debugging. |

## Scope and dependencies

- The hub entry runs on a host-side client over SSH and needs no local NPU hardware, and `blue-vllm-ascend-build` is a pure-CPU build workflow; both use `execution: host`. The remaining five entries inspect or change NPU devices and containers running on NPU servers, so they use `execution: npu`.
- vLLM entries assume vllm-ascend deployments; provisioning targets Atlas A2/A3/A5 server generations; fabric checks require multi-machine RoCE connectivity.
- Content is operational know-how for remote development servers; it does not by itself run inference workloads. Runtime correctness and performance remain out of scope, so all seven entries use `validation.status: not-recorded`.
- Disclosure note: the pinned content mentions one intranet container-registry hostname (`cr.rnd.huawei.com`), which also appears in Huawei's public Ascend/MindIE-Motor documentation, and RFC1918 example addressing only. No credentials, real hostnames, or account identifiers are present.
