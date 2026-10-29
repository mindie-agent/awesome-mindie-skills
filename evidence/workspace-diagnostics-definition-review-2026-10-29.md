# Workspace diagnostics: definition review

- Review date: 2026-10-29.
- Source: [wangxiaoteng888/vllm-ascend-workspace](https://github.com/wangxiaoteng888/vllm-ascend-workspace/tree/bb4b39c4c1989a63ab7a6860e8c42c8756b2773b).
- Source revision: `bb4b39c4c1989a63ab7a6860e8c42c8756b2773b`.
- Contributor and maintainer of these workflows: wangxiaoteng / wangxiaoteng888.
- Scope: source definition, supporting workflow and helper inspection; offline helper checks. No live service or NPU execution.

## Provenance and complete packages

The source workspace retains its [MIT license](https://github.com/wangxiaoteng888/vllm-ascend-workspace/blob/bb4b39c4c1989a63ab7a6860e8c42c8756b2773b/LICENSE), including Qi Mao's copyright notice. The PD package was already published in source commit `5fba343c1c2b3d896f1273e0ecb9b0581f8128d4`; its supplied local text matches that package after accounting for Windows checkout line endings. The reviewed revision adds the contributor's host-memory package, package notices and offline regression cases.

The host-memory package bundles a user-supplied variant of smem. Its Matt Mackall copyright header declares GPL-2.0-or-later, and `scripts/smem/COPYING` retains the GPL v2 text. The exact prior upstream revision of that variant is not recorded; this source commit pins its distributed content. Only line endings were normalized. The package [NOTICE](https://github.com/wangxiaoteng888/vllm-ascend-workspace/blob/bb4b39c4c1989a63ab7a6860e8c42c8756b2773b/.agents/skills/vllm-host-memory-leak/NOTICE) separates these terms from the workspace MIT license. BCC is an external dependency, not bundled source.

Obtain the pinned source without copying only an entrypoint:

```bash
git clone https://github.com/wangxiaoteng888/vllm-ascend-workspace.git
git -C vllm-ascend-workspace fetch origin bb4b39c4c1989a63ab7a6860e8c42c8756b2773b
git -C vllm-ascend-workspace checkout --detach bb4b39c4c1989a63ab7a6860e8c42c8756b2773b
```

Preserve the chosen `.agents/skills/<name>/` directory, references, scripts, agent metadata and license notices. Retain `.remote-dev/` and the workspace support layout when using its remote companion tools; endpoint configuration is user-supplied runtime state. Reading or installing these packages does not initialize submodules, launch services, download models, or attach tracing tools.

## Reviewed workflows and boundaries

### PD decode profiling

Inspected `SKILL.md`, `agents/openai.yaml`, `references/pd-decode-workflow.md`, and all four scripts: `capture_decode_window.sh`, `metrics_delta.py`, `analyse_trace_views.py`, and `package_trace_views.sh`.

The workflow accepts explicit P/D roles, proxy routing, model and parallel configuration, independent P/D cache settings, recompute/MTP/task-queue/stack settings, a capture duration, an expected rank count, and an output filesystem. It waits for increasing D-node generation-token counters before starting the profiler and records another counter delta across the capture window. It processes each expected D rank and produces trace views, a parser manifest, control responses, metric snapshots, and `D_trace_views_only.tar.gz` with a SHA-256 sidecar.

This specializes the existing `ascend-profiling-collection` workflow: evidence that D actually decoded and a D-only trace handoff are its primary outputs. It is distinct from AISBench performance measurement, general trace interpretation, and PD service lifecycle management.

Completing collection requires a supported two-node Ascend deployment, matching vLLM/Ascend and `torch_npu` runtime, reachable metrics and profile-control endpoints, a supported PD proxy, Python, Bash, curl and standard archive tools. Metric attribution expects labeled `vllm:generation_tokens_total` samples with an `engine` label and a stable process lifetime. The trace helpers check nonempty files and counts; these checks do not establish trace semantic validity or model correctness. No version-independent profiler flag or hardware compatibility claim is made.

### Host-memory growth diagnosis

Inspected `SKILL.md`, agent metadata, `NOTICE`, `LICENSE`, all five references, the diagnostic Python helpers, smem launch wrappers and license header, and `tests/test_offline.py`. This is not a full audit of the bundled smem implementation.

The workflow starts with process identity and fresh USS/PSS/RSS samples. It distinguishes Python/native allocation growth, mapped memory, allocator retention and possible notification backlog before selecting a diagnostic branch. Its BCC branch first verifies malloc/free observation on an isolated worker and bounds the subsequent capture. Optional SpinCondition instrumentation defaults to preview and requires a matching source hash to apply. Passive notification reporting does not add ZMQ poll/recv/EVENTS calls from its reporting thread.

Inputs include the exact PID namespace and process lifetime, workload and service configuration, code/library versions, and a new evidence directory. Outputs include identity and mapped-library hashes, memory samples and plots, BCC manifests and reports, notification summaries, and source-backed findings with unproven hypotheses separated. USS growth, printed outstanding allocations, and send/recv differences are not presented as proof of a leak or absolute queue depth.

This complements `ascend-memory-profiling`, which attributes NPU HBM. The selected execution condition is `depends-on-checks`: offline parsing uses a host Python environment, live sampling requires Linux `/proc` access, BCC needs matching kernel/tooling and tracing permissions, and an Ascend inference reproduction or fix validation needs its actual service/NPU environment. Plotting additionally needs matplotlib; the optional smem wrapper needs Bash, flock and timeout. No new service restart or runtime instrumentation was performed for this review.

## Deduplication

The supplied workspace contained 14 principal domain/workspace skill packages. Twelve names or equivalent workflows are already represented: `repo-init`, `machine-management`, `session-management`, `remote-toolbox`, `remote-code-parity`, `modelscope`, `vllm-ascend-serving`, `vllm-ascend-benchmark`, `aisbench-pd-benchmark`, `ascend-memory-profiling`, `ascend-profiling-collection`, and `ascend-profiling-analysis`.

Their current catalogue entries and independently maintained adaptations are preserved. In particular, the existing AISBench entry retains its reviewed Yuli-yx adaptation and the original wangxiaoteng888 attribution. This contribution adds only the two distinct workflows above. The contributor-specific signed-commit helper is not an Ascend task entry.

## Offline checks and limits

Checks used Python 3.12.10 on Windows, PyYAML 6.0.3, and Git for Windows Bash for shell syntax checks:

- Both skill entrypoints pass the skill frontmatter validator; referenced local Markdown links resolve.
- Python syntax parsing succeeds for the 15 `.py` files in the two packages, including the new regression test module. This does not execute Linux-only helpers or the bundled extensionless smem program.
- Seven host-memory regression cases pass: mapping-aware BCC file offsets, PID reuse rejection and lifetime selection, stale-data refusal, notification interval deltas, counter reset rejection, mixed-process rejection, and refusal to patch mismatched source bytes.
- Five synthetic PD helper cases pass: positive per-engine decode delta, refusal of zero delta, refusal of missing generation metrics, reuse of existing nonempty trace files, and rejection of an incorrect expected rank count. The trace-reuse cases do not import `torch_npu` or invoke analysis on raw device data.
- Bash syntax checks pass for both PD shell helpers and `smem/mem_monitor.sh`. Archive creation and live profile control were not executed.

The committed memory helper cases are reproducible from the pinned workspace:

```bash
python3 -m unittest discover -s .agents/skills/vllm-host-memory-leak/tests -v
```

The source's 2026-10-22 validation note is retained as author-provided history. Its external runtime artifacts were not re-executed or imported in this contribution and are not used to claim reproduction at the current revision. Both entries use `validation.status: not-recorded` and `cases: []`.

Catalogue checks cover schema, local links, generated bilingual README content, pinned source revisions and definition hashes. Remote hash retrieval is source integrity verification, not inference or hardware validation.

## Catalogue validation results

The following checks passed for this contribution:

```bash
python3 scripts/validate_catalog.py
python3 scripts/render_catalog.py --check
python3 scripts/validate_catalog.py --source-root vllm-ascend-workspace=<pinned-local-checkout>
python3 -m unittest discover -s skills/ascend-memcache-pooling/tests -v
```

The catalogue contains 344 skills, 10 categories and 24 source records; its 833 local links resolve. The existing 17 repository regression tests pass. A disposable catalogue copy also rejected duplicate YAML keys, an unknown category, an invalid hash and stale README rendering. Windows source-checkout line endings were restored to exact Git blob bytes before comparing hashes.

The full `python3 scripts/validate_catalog.py --check-remote` run matched 336 of 344 definitions, including both new entries. Eight unchanged entries from `ascendc-agent/ascendc-skills` on GitCode returned HTTP 403: `api-gen`, `asc-testcase-doc-gen`, `cmake-race-auditor`, `examples-docs-validator`, `generate-case`, `multi-scenario-sample-pattern`, `tpipe-to-static-tensor`, and `ub-boundary-check`. These are remote access failures, not reported hash mismatches. Both newly added definitions were additionally retrieved and hash-checked successfully on their own. The full remote check is therefore recorded as incomplete, not passed.
