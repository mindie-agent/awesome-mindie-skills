---
name: analyze-upstream-downstream
description: Compare a module in an upstream framework with its downstream plugin, fork, or platform adaptation. Trace actual calls and replacement boundaries to distinguish inherited behavior, synchronized changes, migration gaps, and platform limits, then produce an evidence-based migration plan. Use for feature alignment, bugfix synchronization, and optimization assessments, not ordinary single-repository code review.
---

# Upstream and downstream module analysis

Determine which relevant capabilities upstream provides, which downstream actually uses, which updates follow the dependency automatically, and which need manual adaptation. Classify behavior and execution branches separately rather than assigning one label to an entire module or commit.

## Inputs and scope

Resolve these inputs from the request and workspace. Continue independent investigation when information is missing; ask only for details that change the comparison.

| Input | Purpose |
| --- | --- |
| `UPSTREAM_ROOT` / `DOWNSTREAM_ROOT` | Source roots, or two versions of the same repository. |
| `UPSTREAM_ENTRY` / `DOWNSTREAM_ENTRY` | Module or feature entrypoints; locate them through callers or registries when unknown. |
| `SCOPE` | Relevant capabilities, fixes, performance concerns, configurations, and platforms. |
| `BASELINE` | Requested version, downstream dependency pin, or current local snapshot. |
| `OUTPUT` | Conversation report or requested local record; use sanitized identifiers by default. |

An analysis request is read-only with respect to code and history and produces findings and a plan. Implementation, commits, and publication follow the user's actual authorization. Include existing workspace changes in the baseline; do not reset, switch, or overwrite them to manufacture a clean snapshot.

## Privacy and reusable material

- Keep the skill, templates, and examples generic. Do not store task-specific paths, usernames, accounts, private repositories, internal hosts, source excerpts, or revision identifiers in reusable resources.
- Use actual roots for local navigation. In reports, default to `UPSTREAM/relative/path:line` and `DOWNSTREAM/relative/path:line`; do not export the absolute-root mapping. For external sharing, also replace sensitive relative paths, symbols, branches, and private revisions with stable evidence identifiers.
- Retain only the versions, symbols, and minimal code context needed as local evidence. Avoid full environment dumps, remote URLs, author identities, and unrelated logs. Inspect Markdown link targets, image metadata, attachments, and configuration fields as well as visible text.
- Use confirmed public projects and documentation for external research. Do not send private paths, symbols, logs, code, or internal URLs to public search, including searches intended to test whether they are public. Reformulate the technical question without private details.
- Sanitization does not authorize uploading, publishing, or sending a report. Honor requests for more specific local evidence within their stated scope; do not collect credentials.

## Establish a reproducible baseline

Read applicable repository rules and verify both entrypoints. Record each revision, relevant working-tree differences, dependency pins, and platform or build switches. For non-Git sources, record a version and source identifier.

Distinguish the local source snapshot, the upstream version declared compatible by downstream, and the packages or binaries actually loaded at runtime. Report pin/source mismatches separately. Current files do not prove production behavior, and version dates do not prove that a snapshot matches the remote tip. Verify public upstream state when the user requests the latest version; do not silently update repositories or replace the comparison baseline.

## Trace actual calls and bindings

Follow entrypoints through the smallest boundary that explains the target behavior:

- Construction, initialization, configuration, callers, state updates, and output processing.
- Inheritance, delegation, direct imports, copied implementations, patches, registries, factories, and backend selection.
- Relevant linking, code generation, compile conditions, and runtime loading mechanisms.

For each operation, record **call site -> actual implementation -> activation conditions**. Prefer symbol searches within relevant directories. When useful, inspect upstream history, downstream bindings, and test coverage as separate lines of investigation, then reconcile evidence against the same baseline.

Pay particular attention to these boundaries:

1. **Inherited orchestration with overridden primitives.** Inheriting a scheduler or orchestration class does not imply inheriting every lower-level fix. Separate shared helper references from copied functions.
2. **Captured symbols and renamed entrypoints.** A defining module and a caller that imported a symbol earlier may hold different bindings. Assigning an old name does not prove that current calls change. Check exports, registration order, and later overrides.
3. **Entrypoint contracts.** Compare production-call positional arguments, keywords, defaults, returns, layouts, and state ownership. An adapted operator or a test calling an old helper directly does not establish full-path compatibility.
4. **Configuration branches.** Defaults, optional features, fallback paths, and platforms can have different conclusions. Mark unresolved dynamic bindings as unknown and propose the smallest runtime check needed to resolve them.

## Compare behavior and inspect history

List upstream capabilities and required contracts before comparing them with actual downstream paths. As relevant, examine inputs and outputs, shapes and types, numerical semantics, randomness, state lifetime, edge inputs, errors, synchronization, and allocation. Avoid applying irrelevant checklist items.

Inspect history, renames, and important fix diffs within the relevant paths. Commit titles and PR descriptions help locate changes; actual diffs and current source determine conclusions:

- A missing commit identity does not imply a missing fix: downstream may cherry-pick, squash, rewrite, or implement an equivalent algorithm.
- A commit can span a shared helper, an overridden function, and callers. Classify them separately and inspect prerequisites and follow-up fixes.
- Missing same-name files or symbols do not prove a missing capability; same-name configuration does not guarantee equal semantics.
- Local optimizations, boundary guards, and platform workarounds may be intentional. Establish their constraints before recommending replacement.

## Build the difference matrix

Attach applicable configuration, evidence from both sides, and a validation level to each conclusion. Split an item when its execution branches differ.

| Classification | Required basis |
| --- | --- |
| Directly inherited | Current calls still reach upstream implementation with compatible contracts; state dependency-version and configuration conditions. |
| Manually synchronized | An independent downstream implementation covers the behavior; explain equivalence evidence and validation gaps. |
| Manual synchronization needed | Relevant upstream behavior or fixes apply to the scope but are overridden or disconnected; identify the concrete omission. |
| Downstream-specific / intentional difference | A local extension, optimization, or workaround; establish constraints and reasons to preserve it. |
| Platform limitation / explicitly unsupported | Code, configuration, or platform documentation supports the limitation; platform difference alone is insufficient. |
| Unresolved / not applicable | Evidence is insufficient, or the target configuration does not enter the path. Distinguish those reasons and explain what would resolve uncertainty. |

Direct inheritance does not mean enabled by default, deployed, or tested on the target platform. Report statically demonstrable interface incompatibilities or missing guards explicitly without claiming a reproduced runtime failure.

Separate source inspection, reference/unit tests, target-environment execution, end-to-end checks, and performance evidence. Algorithm differences are not automatically bugs. For randomized algorithms, compare distributions and invariants; require per-element equality under the same seed only when the contract demands it. Performance claims require matched environments and workloads, not upstream measurements from other hardware.

## Report and propose a minimal migration plan

Include baselines, actual bindings, existing capabilities, the difference matrix, recommended actions, and validation gaps. For structured delivery or a saved record, adapt the [report template](references/report-template.md) to the task; omit irrelevant sections.

Prioritize clear correctness and interface gaps, then memory and measurable performance improvements, then independent features and platform capabilities. Each action should identify its trigger, smallest modification boundary, prerequisites, and acceptance criteria. **Already inherited; no code change needed** is a complete outcome.

Reuse existing extension points and tests. Regression checks should exercise production calls or registration boundaries, not only isolated helpers. Identify caller issues outside the module separately and explain their impact without describing the entire module as broken.

Before finishing, check for baseline drift, mixed source/runtime claims, synchronized changes incorrectly labeled missing, citations to uninspected versions, and leaked environment details. Revise classifications when new test evidence contradicts them.
