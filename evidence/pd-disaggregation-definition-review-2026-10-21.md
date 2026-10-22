# PD disaggregation source definition review

- Review date: 2026-10-21.
- Method: maintainer-side source inspection for this catalogue submission.
- Source: [nwpu-zxr/vllm-ascend-pd-disaggregation-skills](https://github.com/nwpu-zxr/vllm-ascend-pd-disaggregation-skills).
- Revision: `2852c18ac977783f336f8c8864ca84dfee3f5cc6`.
- Maintainer: `nwpu-zxr`.
- License: MIT; the source retains the original Qi Mao copyright notice.
- Inputs: upstream bilingual README, LICENSE, catalogue-integration guide and all three `skills/pd-disaggregation-*/SKILL.md` entrypoints. Supporting review covered the shared skill-reuse contract, serving workflow coordination, design layout assessment and accuracy bottom-up validation references.

The [source record](../catalog/sources.yaml) pins the complete collection. Each [skill entry](../catalog/skills/) records the SHA-256 of the exact entrypoint bytes. Installing a skill requires its complete upstream directory, including references, scripts when present, and license, rather than only its `SKILL.md`.

## Tasks, inputs and outputs

| Skill | Inputs and workflow | Expected output and category |
|---|---|---|
| `pd-disaggregation-design` | Concrete model/cache specs, all component shapes/strides/sizes, storage semantics and named connector revisions; trace allocation, registration, mapping, transfer and lifetime | Per-component compatibility verdict, adaptation gaps and validation plan; `model-integration` |
| `pd-disaggregation-serving` | Model/platform/connector configuration, endpoints, role topology and existing service ownership; prepare or launch through selected lifecycle controllers and verify actual transfer | P/D/proxy configuration, service state, request/transfer evidence and scoped cleanup; `serving` |
| `pd-disaggregation-accuracy-debug` | Preserved failing request, runtime/configuration identity and source/tensor/log evidence; select feature isolation or producer-to-consumer validation | First divergent boundary, scoped causal classification and remedy validation or next discriminating experiment; `debugging` |

All three use `execution: depends-on-checks`: source/layout review, script preparation and analysis of existing artifacts can run on a host. Live Ascend serving, tensor capture, feature-isolation experiments and device validation require an authorized matching NPU environment and its actual software/transport dependencies. This label does not claim that the complete runtime workflow runs without devices.

The definitions require model- and revision-specific official vLLM Ascend documentation and HIXL documentation when that backend is involved. They do not declare a universal launch command, hardware support matrix, fixed cache layout or universally applicable N-1 handoff. Source/runtime contracts and each component's first consumption determine the comparison boundary.

## Specialization and coexistence

The collection supplies PD methodology with optional specialist execution. It complements existing entries as follows:

- `model-infer-kvcache` can inform cache implementation analysis; the new design entry specifically assesses a named PD connector end to end, including peer specs, registration bounds, placement and storage lifetime.
- `vllm-ascend-pd-serving` already covers PD deployment. The new serving entry adds a standalone methodology and explicit coordination with available host workflows. It preserves one deployment plan and one lifecycle controller per service, reuses existing state and acceptance evidence, reconciles uncertain launches, and prevents recursive routing or duplicate startup/rollback.
- Correctness, graph, operator, distributed and `model-infer-precision-debug` skills can supply bounded diagnostic steps. The new accuracy entry retains responsibility for cross-node KV/state content and destination placement before consumption, feature interactions, dirty-block reuse and PD causal attribution. A specialist's local pass is not end-to-end PD proof.

The `auto`, `prefer-integrated` and `standalone` choices are natural-language preferences, not new executable APIs. Optional skill absence permits bundled methods; explicit user requirements and mandatory host rules remain binding. Catalogue inclusion does not imply that a referenced skill is installed or compatible. The coordination instructions do not themselves implement locks or demonstrate live interoperability.

## Validation scope

This record supports definition-level inclusion only. All three entries use `validation.status: not-recorded` and empty cases. Package checks, catalogue validation and pinned source hashes do not establish a device reproduction, transport correctness, model accuracy or performance. No live MindIE deployment or NPU experiment is claimed by this submission.
