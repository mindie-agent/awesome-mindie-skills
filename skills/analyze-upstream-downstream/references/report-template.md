# Upstream and downstream analysis report

Use this structure for a requested record or structured delivery. These are filling instructions, not findings; merge or omit sections that do not apply.

## Baseline and scope

- Target: feature/module boundary, configuration, and platform.
- Upstream and downstream: inspected revisions or snapshots and relevant working-tree differences.
- Dependencies: whether downstream pins match the upstream snapshot; whether loaded package provenance is confirmed.
- Evidence locations: `UPSTREAM/relative/path:line` and `DOWNSTREAM/relative/path:line`. For a shared version, replace sensitive paths, symbols, and revisions with role aliases and evidence identifiers; exclude the actual root mapping.
- Limits: unavailable versions, dependencies, dynamic bindings, or target-environment evidence.

## Actual bindings and existing capabilities

| Operation / activation conditions | Call site | Current implementation source | Entrypoint contract | Evidence ID |
| --- | --- | --- | --- | --- |

Add a diagram only when the call relationships are difficult to express in a short table. List existing capabilities so that already adapted behavior does not reappear as migration work.

## Difference and inheritance matrix

| Capability / fix / optimization | Upstream behavior and history | Current downstream behavior | Classification | Applicable conditions | Evidence and validation level | Minimal action |
| --- | --- | --- | --- | --- | --- | --- |

Split commits spanning multiple binding boundaries into separate rows. Link confirmed public sources; use local evidence identifiers for private material. Distinguish unknown behavior from missing behavior, and existing code from passing tests.

## Evidence for important differences

Expand only items affecting conclusions or development order:

- Trigger conditions and expected behavior.
- Actual calls, interfaces, or algorithm differences on both sides.
- Alternative implementations, compatibility branches, or prior synchronization already ruled out.
- Conclusions established statically and hypotheses still requiring validation.
- Minimal modification boundary, prerequisites, and local adaptations to preserve.

## Development and validation plan

| Priority / impact | Action and modification boundary | Prerequisites | Smallest effective validation | Acceptance criteria |
| --- | --- | --- | --- | --- |

Choose validation levels according to the actual issue:

- Interfaces/bindings: production entrypoint arguments, registration results, and optional branches; do not only call an old helper.
- Correctness: regression inputs reproducing the difference, reference outputs, and edge conditions.
- Numerical/randomized behavior: errors, distributions, invariants, and acceptable statistical criteria.
- Performance: timing, memory, compilation, and synchronization evidence under identical software, hardware, and workloads.

## Current status

Separate confirmed facts, executed checks and results, failed or unrun checks and reasons, and hypotheses awaiting validation. Report only commands actually executed and their results; a test file's existence does not establish a passing test.

Before sharing, inspect prose, link targets, citations, attachments, and metadata for real paths, accounts, private identifiers, credentials, or unrelated code. Keep evidence traceable without exporting identity mappings or extra environment information.
