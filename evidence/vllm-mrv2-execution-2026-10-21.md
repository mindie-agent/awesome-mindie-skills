# vLLM MRV2 case preparation and NPU execution record

## Identity and acceptance

- Date: 2026-10-21; submitted by Liamup777.
- Skill/controller revision: `ed71b1b56994e419998e4cd85f5ace013f92447d` of [vllm-mrv2-kernel-tools](https://github.com/Liamup777/vllm-mrv2-kernel-tools/tree/ed71b1b56994e419998e4cd85f5ace013f92447d).
- vLLM base: `9ed533eb4adfe48aef7e569a08daeccd2a773fed` (`v0.30.0`).
- vLLM target: `db9527a46873454610df6dbedf79a36d6bf1a7f6` (`v0.31.0`).
- Ascend source: [`5d0665fbaf1270745d04d94907c6e81784dc8584`](https://github.com/Liamup777/vllm-ascend/commit/5d0665fbaf1270745d04d94907c6e81784dc8584).
- No model weights, tokenizer, dataset, distributed model service or collective communication were needed: cases directly launch JIT kernels.

Acceptance for the recorded execution subset: verify the actual imported vLLM/Ascend commit identities; validate all eight case structures; execute one smoke case, then all eight cases in isolated sequential worker processes; each full case must exit successfully and produce 50 finite, nonnegative timing samples after 10 warmups. Numerical correctness is explicitly outside this acceptance and remains `not_checked`.

## Installation and preparation

Keep the complete tool checkout. Example paths below are portable replacements for private paths; adapt them to the local installation. Source Git objects must already exist locally; the tool does not automatically fetch or change source checkouts.

```bash
git clone https://github.com/Liamup777/vllm-mrv2-kernel-tools.git
cd vllm-mrv2-kernel-tools
git checkout --detach ed71b1b56994e419998e4cd85f5ace013f92447d
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e . --no-deps
```

Load `skills/vllm-mrv2-kernel-workflow/SKILL.md` from that checkout in the agent. Supply the installed Python path and source locations. The agent follows the same controller command:

```bash
python3 -m kernel_tools pipeline \
  --repo /path/to/vllm --source /path/to/vllm-ascend \
  --base v0.30.0 --target v0.31.0 \
  --model gpt-6-sol --reason medium \
  --prepare-only --output /path/to/results/prepared
```

The recorded preparation reviewed two additions and generated three cases for `spec_decode.draft_model.speculator._prepare_prefill_inputs_kernel` and five for `spec_decode.rejection_sampler._gather_draft_sampled_kernel`. The first short name also exists in other modules: use the exact retained targets.

Both generation states were `ready`; `cases validate` returned `PASS: 8 cases (structure only; semantic/NPU checks not performed)`. Preparation itself exited 1 with `needs_review`: the AI put the absence of runtime, binding and correctness validation into `review.unresolved`. That original state is retained; the later device run is separate evidence, not a retroactive claim that a single pipeline invocation completed successfully. AI regeneration can produce different cases; replay the retained inputs below for this specific result.

Preparation read a dirty local Ascend tree with five modified capture/MoE files. Device execution instead used clean detached worktrees at the locked commits; these local modifications were not transferred. No replacement of these two kernel symbols was found in the supplied Ascend sources. Each runtime result resolved to the upstream vLLM target and recorded the defining file hash.

## Environment and private target configuration

Controller: macOS with Python 3.12.2 and authenticated Codex CLI; AI stages used `gpt-6-sol`, medium reasoning. Remote: Docker, Python 3.12.13, one selected logical `npu:0` (`Ascend910_9362`) from 16 visible logical devices. Each kernel launches on one device; no interconnect topology is exercised. Other devices had unrelated jobs, and device isolation was a cooperative tool lock rather than exclusive host isolation.

Software observed by doctor: torch `2.10.0+cpu`, torch-npu `2.10.0.post7.dev20260918`, Triton module/package `3.6.0`, triton-ascend `3.6.0+dev20260920`, CANN `9.0.1`, npu-smi `26.0.rc1`. Installed vLLM distribution metadata was stale relative to the worktrees; source identity was established from actual import paths and Git HEADs instead. These versions describe one observed environment, not a general compatibility matrix.

Initialize a private config with `python3 -m kernel_tools init --output /private/kernel-tools.json`, then edit its target using the upstream [setup reference](https://github.com/Liamup777/vllm-mrv2-kernel-tools/blob/ed71b1b56994e419998e4cd85f5ace013f92447d/skills/vllm-mrv2-kernel-workflow/references/setup.md). A portable configuration shape is:

```json
{
  "targets": {
    "my-npu": {
      "host": "npu-lab",
      "container": "vllm-container",
      "python": "python3",
      "cwd": "/workspace/vllm-ascend",
      "pythonpath": ["/workspace/vllm", "/workspace/vllm-ascend"],
      "setup": "/usr/local/Ascend/ascend-toolkit/set_env.sh",
      "device": "npu:0",
      "result_root": "/workspace/kernel-results"
    }
  }
}
```

`npu-lab` is the user's existing OpenSSH alias; configure key authentication and verify the host fingerprint separately. Container paths and logical device mapping must reflect the actual environment. Inspect occupancy before selecting a device. Use clean isolated worktrees when active source checkouts contain unrelated work. The tool uploads its runner and cases, not production source or dependencies.

## Retained artifacts and replay

The following artifacts are committed alongside this record, rather than linked to private local or NPU paths:

- [Input-preparation cases](vllm-mrv2-2026-10-21/cases/prepare-prefill.json): three original generated cases.
- [Draft-gather cases](vllm-mrv2-2026-10-21/cases/gather-draft-sampled.json): five original generated cases.
- [Source lock](vllm-mrv2-2026-10-21/source-lock.json): original commit-only lock, fingerprint `dc1e53e673a6beaac310c1683ee5f9ae2e7e7471ae27209d7f6890d63998546f`.
- [Results](vllm-mrv2-2026-10-21/results.json): per-case statuses, timing summaries and binding hashes extracted from the successful full run. Private hostnames and filesystem roots are omitted; numeric summaries are unchanged. This is an evidence summary, not a replacement for raw worker logs or a kernel-tools resume directory.

From the tool checkout, set `EVIDENCE` to the absolute path of this catalogue's `evidence/vllm-mrv2-2026-10-21` directory. `RESULTS` below must point to a new output parent. Populate remote imports at the two exact locked commits before verifying:

```bash
EVIDENCE=/path/to/awesome-mindie-skills/evidence/vllm-mrv2-2026-10-21
RESULTS=/path/to/new-results
python3 -m kernel_tools cases validate "$EVIDENCE/cases"
python3 -m kernel_tools doctor --config /private/kernel-tools.json --npu my-npu --device npu:0
python3 -m kernel_tools verify "$EVIDENCE" --config /private/kernel-tools.json --npu my-npu
python3 -m kernel_tools run "$EVIDENCE/cases" \
  --kernel _prepare_prefill_inputs_kernel --case-name smoke_one_request \
  --config /private/kernel-tools.json --npu my-npu --device npu:0 \
  --warmup 3 --rounds 10 --timeout 180 --output "$RESULTS/smoke"
python3 -m kernel_tools run "$EVIDENCE/cases" \
  --config /private/kernel-tools.json --npu my-npu --device npu:0 \
  --warmup 10 --rounds 50 --timeout 180 --output "$RESULTS/full"
```

Only proceed after doctor, source verification and smoke succeed. Standalone `run` does not check the source lock automatically. Keep source state unchanged between verification and execution.

## Observations

Source verification returned `verified` for both clean imported worktrees. Smoke and full execution returned exit code 0. Every full case had `status=success` and `correctness=not_checked`:

| Kernel | Case | Execution | Mean microseconds |
|---|---|---|---:|
| `_prepare_prefill_inputs_kernel` | smoke_one_request | success | 82.314 |
| `_prepare_prefill_inputs_kernel` | typical_mixed_rejection_padding | success | 92.084 |
| `_prepare_prefill_inputs_kernel` | boundary_512_two_iterations | success | 90.749 |
| `_gather_draft_sampled_kernel` | smoke_two_logits | success | 83.324 |
| `_gather_draft_sampled_kernel` | mixed_placeholder_state_mapping | success | 83.328 |
| `_gather_draft_sampled_kernel` | tile_minus_one_1023 | success | 107.846 |
| `_gather_draft_sampled_kernel` | tile_exact_1024 | success | 113.286 |
| `_gather_draft_sampled_kernel` | tile_plus_one_1025 | success | 115.283 |

The separate smoke mean was 14.130 microseconds (3 warmups, 10 samples). The difference from the full run and the full-run outliers show that these timings are observations, not a stable performance baseline. No speedup, service throughput or regression threshold is claimed.

Initial connection attempts timed out before SSH authentication; later key login succeeded. The first source verification correctly rejected mismatched active checkouts; clean detached worktrees resolved that prerequisite. Original working trees and unrelated processes were preserved. Warnings included deprecated Triton CANN math aliases, driver/CANN allocation padding, and tar timestamps about 105 seconds ahead of the remote clock; none prevented the successful run.

## Remaining limits

No numerical reference, accuracy test, model E2E coverage, throughput benchmark or performance improvement was checked. The three 1023/1024/1025 draft-gather cases are synthetic single-request long-draft tile boundaries, not established production request layouts. Noncontiguous views, aliases and correlated random layouts are not covered. Commit-only locks do not capture dirty-file content. The record establishes the stated direct-JIT execution subset on this one device/software environment; it does not establish that every branch or mode of the skill works.
