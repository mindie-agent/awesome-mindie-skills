# blue-server-toolkit initial catalogue review

- Review date: 2026-10-20.
- Source: [xuchi-0808/blue-server-toolkit](https://github.com/xuchi-0808/blue-server-toolkit).
- Upstream revision: `b9f5529774c67482696c830b91af25a39c82c949`, resolved from GitHub `main`.
- Maintainer: xuchi-0808.
- License: MIT; the pinned revision's LICENSE names the copyright holder `xuchi-0808`.
- Scope: one entrypoint (repository-root `SKILL.md`) selected for Ascend engineering environment support.

## Inspection method

The upstream repository was cloned locally and inspected at the pinned revision. Inspection covered the `SKILL.md` frontmatter and declared scope, the README, the CHANGELOG, the configuration template, 7 helper scripts, and all 15 advanced documents under `docs/`. The catalogue entry stores the SHA-256 of the pinned `SKILL.md` bytes; remote verification is performed by `python3 scripts/validate_catalog.py --check-remote`.

## Entry coverage

| Upstream area | Coverage |
|---|---|
| `SKILL.md` | Connection checks and SSH stability (ControlMaster multiplexing), code sync, UT execution, model download, log viewing, container management, file transfer, pip/image mirror strategy, and an experience memo. |
| `docs/` (15) | SSH connection stability, NPU process cleanup, chip numbering (A3), 950DT fabric identity and RoCE connectivity, vLLM-ascend build and service guide, vLLM service profiling and profiling analysis, PD-disaggregated bring-up, docker bind-mount traps, image mirrors, HDK installation, gzone download, and graph debugging. |
| `scripts/` (7) | NPU status checks, per-generation docker container bring-up (Atlas A2/A3/A5), torch FLOPs measurement, first-run configuration initialization. |

## Scope and dependencies

- The skill runs on a host-side client over SSH (`ssh`/`scp`/`rsync`/`docker`/`curl`) and needs no local NPU hardware, hence `execution: host`; operations that inspect or change NPU state (for example `npu-smi`) act on the remote server's devices.
- vLLM-related documents assume vllm-ascend deployments; the container bring-up scripts target Atlas A2/A3/A5 server generations.
- Content is operational know-how for remote development servers; it does not by itself run inference workloads. Runtime correctness and performance remain out of scope, so the entry uses `validation.status: not-recorded`.
- Disclosure note: the pinned content mentions one intranet container-registry hostname (`cr.rnd.huawei.com`), which also appears in Huawei's public Ascend/MindIE-Motor documentation, and RFC1918 example addressing only. No credentials, real hostnames, or account identifiers are present.
