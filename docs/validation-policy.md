# Review and execution validation

[中文](validation-policy.zh.md) | English

## Definition review

Every listed skill has a dated inspection of its definition at a fixed source revision. Check its declared task, core workflow, expected outputs, source ownership, license, and execution conditions. Record the files inspected and the scope of the review under `evidence/`.

The initial reviews cover [17 vLLM Ascend entrypoints](../evidence/definition-review-2026-10-15.md) and [36 CANNBot entrypoints](../evidence/cannbot-definition-review-2026-10-15.md). They record definition-level inspection and source hashes. Execution reproductions are recorded separately below.

## Execution reproduction

Use `validation.status: not-recorded` and `cases: []` until evidence is available. To mark a skill `reproduced`, provide at least one case with all of these fields:

| Field | Required information |
|---|---|
| `date` | Quoted ISO execution date. |
| `source_revision` | Full commit, matching the entry's current source revision. |
| `environment.hardware` | Device model, count, and topology; for offline analysis, state the host and absence of NPU execution. |
| `environment.software` | Applicable framework, runtime, compiler, and tool versions. |
| `scope` | Task, workload, and exact acceptance criteria exercised. |
| `evidence` | Local Markdown record linking configuration, observations, and accessible artifacts. |

The evidence record should identify model and weight revision where relevant, code revision, commands, inputs, raw outputs, expected and observed results, and limitations. Only record a passing reproduction after its declared acceptance criteria pass. Failed or incomplete attempts can be retained in evidence records without marking the entry reproduced.

A reproduced case supports its recorded environment and scope. Broader hardware or software compatibility needs additional cases. A successful offline analysis case does not establish the behavior of a device execution workflow.

## Updating sources

When the source revision changes, review the definition again and update its hash. Reproduce cases against that revision before retaining a `reproduced` label. Preserve historical evidence with its original revision and date.
