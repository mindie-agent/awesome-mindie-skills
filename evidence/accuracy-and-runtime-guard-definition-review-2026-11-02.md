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

Preserve the complete `vllm-ascend-accuracy/` directory (`SKILL.md`, `references/`, `scripts/collect_env.py`, and `LICENSE`) and the complete `06_agent_skills/` plus `01_enable_and_start/`, `02_problem_localization/`, `03_detectors/`, and `04_case_studies/` directories in `runtime-guard-docs` so relative references and helper scripts (`locate_first_divergence.py`, `verify_request_kv.py`, `check_weight_md5.py`, `compare_env.py`, `summarize_guard_dir.py`, `trigger_manual_dump.py`) remain intact.

## Reviewed workflows and boundaries

### `vllm-ascend-accuracy`

Inspected `vllm-ascend-accuracy/SKILL.md`, `references/diagnosis-matrix.md`, `references/issue-patterns.md`, `references/tool-configs.md`, and `scripts/collect_env.py`.

The workflow classifies vLLM-Ascend accuracy regressions into four symptom families (benchmark metric drop, greedy token divergence, repetition/gibberish degeneration, and `NaN`/`Inf` collapse), audits the live serving process environment (`/proc/<PID>/environ` and `/proc/<PID>/maps`), walks an 11-dimension single-variable ablation matrix (graph mode, fusion, MTP speculative decoding, quantization scheme, attention backend, prefix caching, chunked prefill, concurrency, TP/DP/EP/CP topology, context length, and sampling), and runs layerwise `msprobe` comparisons under `--enforce-eager` before reporting closure under a four-state honesty classification (`候选修复`, `已规避`, `已解决`, `受阻`).

### `runtime-guard-config-recommender`, `runtime-guard-investigation`, `runtime-guard-ref-kv-dump`, and `runtime-guard-kv-analysis`

Inspected `06_agent_skills/README.md`, `06_agent_skills/SKILLS_METADATA.md`, all nine `06_agent_skills/*/SKILL.md` definitions, the six helper scripts in `06_agent_skills/scripts/`, and chapters `01` through `05`.

- `runtime-guard-config-recommender` generates valid `additional_config.runtime_guard` payloads restricted to the three shipped detectors (`token_repeat`, `logits_finite`, `spec_acceptance`), enforcing startup-only `runtime_config_hot_reload=true` and cumulative `dump_kv.manual_dump` watermark rules (`auto_max_times: 0`).
- `runtime-guard-investigation` orchestrates end-to-end online KV delimitation across single-instance (`force-feed`) and dual-instance deployments, separating `trigger_rate`, `precision`, and `detect_rate` (including `detector_gap` manual captures).
- `runtime-guard-ref-kv-dump` constructs a clean reference KV dump on the exact same execution mode (`ACLGraph` vs Eager) and TP/PP topology by feeding `prompt_token_ids + output_token_ids[:-1]` (`n_prompt + n_output - 1` tokens) with `max_tokens=1, temperature=0`.
- `runtime-guard-kv-analysis` stitches multi-TP KV head shards (`dim=-2`), classifies `unused_slots` into three hygiene levels (`clean_zero`, `finite_dirty`, `nonfinite_pollution`), gates `used_slots` on `numeric_issue` (`NaN`, `Inf`, `zero_norm`) before computing cosine similarity, builds the dual-view token-by-layer and single-token layer-chain tables, and walks the `Q1-Q10` decision tree to separate KV write corruption from downstream post-KV faults.

## Deduplication and scope control

`runtime-guard-docs/06_agent_skills` contains nine skill folders. To prevent catalogue bloat while retaining the complete upstream checkout:

- The four primary entries above (`runtime-guard-config-recommender`, `runtime-guard-investigation`, `runtime-guard-ref-kv-dump`, and `runtime-guard-kv-analysis`) are indexed as standalone catalogue entries.
- `detector-sweep` and `msprobe-dump` are sub-stages already orchestrated by `runtime-guard-investigation` and covered by `vllm-ascend-accuracy`.
- `build-anomaly-env` (synthetic fault injection for test environments) and the branch-specific backport patch appliers (`apply-mrv1-patch`, `apply-v030-mrv2-patch`) remain available inside the pinned `runtime-guard-docs` checkout without separate top-level catalogue entries.

## Validation status

All five entries are recorded with `review.status: definition-reviewed` and `validation.status: not-recorded` (`cases: []`). Pinned Git revisions and `SKILL.md` SHA-256 digests were verified via `python3 scripts/validate_catalog.py` and `python3 scripts/render_catalog.py --check`.
