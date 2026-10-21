# vLLM MRV2 kernel workflow definition review

- Date: 2026-10-21.
- Maintainer: Liamup777.
- Project: [vllm-mrv2-kernel-tools](https://github.com/Liamup777/vllm-mrv2-kernel-tools).
- Reviewed revision: `ed71b1b56994e419998e4cd85f5ace013f92447d`.
- Upstream license: [Apache-2.0](https://github.com/Liamup777/vllm-mrv2-kernel-tools/blob/ed71b1b56994e419998e4cd85f5ace013f92447d/LICENSE).
- Entry: [skills/vllm-mrv2-kernel-workflow/SKILL.md](https://github.com/Liamup777/vllm-mrv2-kernel-tools/blob/ed71b1b56994e419998e4cd85f5ace013f92447d/skills/vllm-mrv2-kernel-workflow/SKILL.md).
- Entry SHA-256: `8404e5c1a994411e17e039d79df5995f36b3e666715bfdfeb22581366d313b00`.
- Method: inspect the pinned entry, its setup/workflow/acceptance/troubleshooting references, the three stage skills, README installation and invocation instructions, case protocol, source verification, and remote execution paths.

## Task and boundary

The workflow compares two locally available vLLM tags or commit SHAs, reviews additions under `vllm/v1/worker/gpu`, derives direct-launch JSON inputs from upstream and optional local Ascend sources, and can execute them through a configured SSH/Docker target. It records resolved commits, generation states, per-case results and failed logs.

Only locally defined kernels with direct launches, or explicitly imported external Triton symbols directly launched in that GPU directory, qualify. JIT-only helpers, imported Python wrappers, moves/renames and transitive object-method reachability do not become additions. Static candidates require AI review. This CLI is a release/commit delta workflow, not a single-version complete XLSX inventory.

This differs from general Triton development/optimization entries: it starts from vLLM MRV2 source changes and produces source-locked executable input cases. It does not implement or optimize kernels and supplies no operator-specific numerical reference.

## Dependencies and installation

Keep the complete upstream repository or installed wheel resources. Copying only the entry directory loses the Python controller, sibling stage skills and documentation. Python CLI installation and agent skill discovery are separate steps. The [upstream README](https://github.com/Liamup777/vllm-mrv2-kernel-tools/blob/ed71b1b56994e419998e4cd85f5ace013f92447d/README.md) documents direct entry-path loading and non-overwriting symlink registration.

The controller requires Python 3.11+, Git, and a separately installed/authenticated Codex CLI for AI review and generation. Its Python control plane has no third-party runtime dependencies. Build installation may download setuptools. Model availability depends on the user's account; `--model` and `--reason` are per-run choices.

`pipeline --prepare-only` needs no remote target and makes no NPU connection. Remote execution additionally requires compatible Torch, torch_npu, Triton-Ascend and CANN, matching actual vLLM/Ascend imports, an accessible device, and an existing SSH key configuration. Passwords and private keys do not belong in JSON. Docker targets require a running container and suitable Docker permissions; bare-metal targets omit `container`.

The execution condition is `depends-on-checks`: preparation is host-side; actual kernel execution requires an NPU. The role is `workflow`; only this user-facing entry is registered. Internal stages depend on controller-provided snapshots and response schemas.

## Evidence limits

Source locks compare actual imported repository commits, not dirty-file content. Source identity checks, JSON structure validation, compilation, execution, timing and numerical correctness are distinct observations. Execution success retains `correctness=not_checked` and establishes neither model-level reachability nor service throughput.

The dated [execution record](vllm-mrv2-execution-2026-10-21.md) covers eight retained cases on one software/device configuration. Its acceptance and remaining limitations are scoped separately from this definition review.
