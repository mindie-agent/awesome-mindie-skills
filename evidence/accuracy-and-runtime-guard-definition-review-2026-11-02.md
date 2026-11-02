# vLLM-Ascend accuracy and Runtime Guard: definition review

- Review date: 2026-11-02.
- Sources:
  - [zhaochuang001/awesome-agent-skills](https://github.com/zhaochuang001/awesome-agent-skills/tree/836e239f80cb76c45a5dd667839e40f336789472) at revision `836e239f80cb76c45a5dd667839e40f336789472` (MIT license; maintainer: `zhaochuang` / `zhaochuang001`).
  - [djh95/runtime-guard-docs](https://github.com/djh95/runtime-guard-docs/tree/45bc2603f48f883a448ed7c2bbeed38f9a2398e1) at revision `45bc2603f48f883a448ed7c2bbeed38f9a2398e1` (license not declared in the pinned repository root; maintainer: `djh95`).
- Scope: source definition, reference documentation, and companion Python script inspection. No live service or NPU hardware execution was performed in this review.

## Provenance and complete packages

Obtain the pinned `awesome-agent-skills` source:

```bash
git clone https://github.com/zhaochuang001/awesome-agent-skills.git
git -C awesome-agent-skills fetch origin 836e239f80cb76c45a5dd667839e40f336789472
git -C awesome-agent-skills checkout --detach 836e239f80cb76c45a5dd667839e40f336789472
```

Obtain the pinned `runtime-guard-docs` source:

```bash
git clone https://github.com/djh95/runtime-guard-docs.git
git -C runtime-guard-docs fetch origin 45bc2603f48f883a448ed7c2bbeed38f9a2398e1
git -C runtime-guard-docs checkout --detach 45bc2603f48f883a448ed7c2bbeed38f9a2398e1
```

Preserve the complete `vllm-ascend-accuracy/` directory (`SKILL.md`, `references/diagnostic-playbook.md`, `references/remediation-playbook.md`, `scripts/env_snapshot.py`, and repository root `LICENSE`) and the complete `06_agent_skills/` plus `01_enable_and_start/`, `02_problem_localization/`, `03_detectors/`, `04_case_studies/`, `05_mrv1_backport/`, `05_v030_backport/`, and `07_architecture/` directories in `runtime-guard-docs` so relative references and helper scripts (`summarize_reports.py`, `score_completion_samples.py`, `correlate_incident.py`, `verify_request_kv.py`, `inspect_kv_dump.py`, `prepare_ref_inputs.py`, `request_from_report.py`, `stitch_kv.py`, `compare_kv_similarity.py`, `compare_per_layer.py`, `locate_first_divergence.py`, and `_lib.py`) remain intact.

## Reviewed workflows and boundaries

### `vllm-ascend-accuracy`

Inspected `vllm-ascend-accuracy/SKILL.md`, `references/diagnostic-playbook.md`, `references/remediation-playbook.md`, `scripts/env_snapshot.py`, and the repository root `LICENSE`.

The workflow classifies vLLM-Ascend accuracy regressions into four symptom families (benchmark metric drop, greedy token divergence, repetition/gibberish degeneration, and `NaN`/`Inf` collapse), captures a live serving environment snapshot via `scripts/env_snapshot.py` (including `/proc/<PID>/environ` and `/proc/<PID>/maps`), walks an 11-dimension single-variable ablation matrix (graph mode, fusion, MTP speculative decoding, quantization scheme, attention backend, prefix caching, chunked prefill, concurrency, TP/DP/EP/CP topology, context length, and sampling), and reports closure under a four-state remediation playbook (`候选修复`, `已规避`, `已解决`, `受阻`).

### `runtime-guard-config-recommender`, `runtime-guard-investigation`, `runtime-guard-ref-kv-dump`, and `runtime-guard-kv-analysis`

Inspected `06_agent_skills/README.md`, `06_agent_skills/SKILLS_METADATA.md`, all nine `06_agent_skills/*/SKILL.md` definitions, the helper scripts in `06_agent_skills/scripts/` (`summarize_reports.py`, `score_completion_samples.py`, `correlate_incident.py`, `verify_request_kv.py`, `inspect_kv_dump.py`, `prepare_ref_inputs.py`, `request_from_report.py`, `stitch_kv.py`, `compare_kv_similarity.py`, `compare_per_layer.py`, `locate_first_divergence.py`, and `_lib.py`), and chapters `01` through `07`.

- `runtime-guard-config-recommender` generates valid `additional_config.runtime_guard` payloads restricted to the three shipped detectors (`token_repeat`, `logits_finite`, `spec_acceptance`), enforcing startup-only `runtime_config_hot_reload=true`, `report.max_per_req >= 1`, and cumulative `dump_kv.manual_dump` watermark rules (`auto_max_times: 0` required by `validate_dump_mutual_exclusive`).
- `runtime-guard-investigation` orchestrates end-to-end online KV delimitation across single-instance (`force-feed`) and dual-instance deployments, separating `trigger`, `precision`, and `detect` rates (including `detector_gap` manual captures) and walking the `Q1-Q10` decision tree across stitched multi-TP dumps (`stitch_kv.py`, `compare_kv_similarity.py`, `compare_per_layer.py`, `locate_first_divergence.py`).
- `runtime-guard-ref-kv-dump` constructs a clean reference KV dump on the exact same execution mode (`ACLGraph` vs Eager) and TP/PP topology by feeding `prompt_token_ids + output_token_ids[:-1]` (`n_prompt + n_output - 1` tokens) with `max_tokens=1, temperature=0`, and runs the 3-step numeric-first comparison (`unused_slots` hygiene, `used_slots` numeric issue gating before cosine similarity, and dual-view token/layer tables).
- `runtime-guard-kv-analysis` performs offline-only analysis of `runtime_guard` report JSON files, completion samples, and single-side `.pt` KV dumps (`summarize_reports.py`, `score_completion_samples.py`, `correlate_incident.py`, `verify_request_kv.py`, `inspect_kv_dump.py`), emitting the `verify_request_kv` `PASS`/`FAIL` gate before handing off to `runtime-guard-ref-kv-dump` and `runtime-guard-investigation`.

## Deduplication and scope control

`runtime-guard-docs/06_agent_skills` contains nine skill folders. To prevent catalogue bloat while retaining the complete upstream checkout:

- The four primary entries above (`runtime-guard-config-recommender`, `runtime-guard-investigation`, `runtime-guard-ref-kv-dump`, and `runtime-guard-kv-analysis`) are indexed as standalone catalogue entries.
- `detector-sweep` and `msprobe-dump` are sub-stages already orchestrated by `runtime-guard-investigation` and covered by `vllm-ascend-accuracy`.
- `build-anomaly-env` (synthetic fault injection for test environments) and the branch-specific backport patch appliers (`apply-mrv1-patch`, `apply-v030-mrv2-patch`) remain available inside the pinned `runtime-guard-docs` checkout without separate top-level catalogue entries.

## Validation status

All five entries are recorded with `review.status: definition-reviewed` and `validation.status: not-recorded` (`cases: []`). Pinned Git revisions and `SKILL.md` SHA-256 digests were verified via `python3 scripts/validate_catalog.py` and `python3 scripts/render_catalog.py --check`.
