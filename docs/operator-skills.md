# Triton-Ascend and AscendC operator skills

This topic indexes fixed public skill packages for operator specification, design, implementation, tests, review, performance work, and selected shared support. It preserves each upstream directory and repository context through pinned links. It does not install skills or redistribute upstream implementations.

The [JSON manifest](../catalog/topics/operator-skills-2026-10-22.json) contains every retained entry, lifecycle assignment, source revision, definition hash, complete directory link, duplicate association, and scope exclusion. The [CSV table](../catalog/topics/operator-skills-2026-10-22.csv) is convenient for filtering. The catalogue-wide taxonomy remains unchanged.

## Counts and counting units

- Source review date: 2026-10-22.
- Selected definitions from 12 newly surveyed source projects: **269** physical `SKILL.md` paths.
- Four identical complete directory trees are represented through source associations rather than duplicate catalogue entries.
- Retained packages from these sources: **265**. Add six already-listed vLLM operator tasks for **271 operator-topic package entries** across 13 projects.
- **264 unique definition byte sequences** appear in these 271 packages. Seven packages share definition bytes with another entry but have different scripts, references, or other directory resources; these remain separate catalogue records.
- Definition-level split: **187 task definitions + 19 workflow definitions + 58 knowledge/case/example definitions**.
- The full catalogue now contains **342 entries**, including unrelated pre-existing inference skills. This update adds 252 entries to the previous 90.

These are counts of fixed definitions and packages, not counts of independent capabilities or hardware-qualified workflows. Different definitions can overlap. A name match is not a deduplication rule.

### Presentation classification

The following eight groups are mutually exclusive under the unique-definition counting unit. They sum to 264. The first six describe lifecycle tasks; the seventh contains active retrieval/intake/trace tasks; the last contains reference resources.

| Group | Definitions |
|---|---:|
| Specification and modeling | 10 |
| Design and pipelines | 18 |
| Implementation and migration | 72 |
| Testing and numerical validation | 38 |
| Review and delivery | 25 |
| Profiling and optimization | 29 |
| Knowledge retrieval and experience tasks | 14 |
| Knowledge references, examples, and cases | 58 |
| **Total** | **264** |

The 58 resources comprise 30 knowledge references, six implementation examples, and 22 optimization cases. **43** are the Triton-Ascend-specific AKG resources. Their scoped example measurements are source observations, not new measurements by this catalogue. The original seven-stage classification has 72 in its knowledge stage because that stage combines these 58 resources with the 14 active support tasks.

| Scope | Task/workflow definitions | Reference resources | All definitions |
|---|---:|---:|---:|
| Triton directly | 31 | 43 | 74 |
| AscendC directly | 147 | 12 | 159 |
| Shared operator support | 28 | 3 | 31 |
| **Total** | **206** | **58** | **264** |

Scope and lifecycle are different axes. An AscendC API lookup task is direct AscendC support, while its lifecycle role is knowledge retrieval. End-to-end workflow entrypoints receive one primary lifecycle classification for counting; their own instructions can cover every stage.

## Source coverage

| Source | Package entries | Unique definitions attributed to source | Pinned revision |
|---|---:|---:|---|
| cannbot-skills | 55 | 55 | `5891c39619a56716b6f73a335ed7709560bb2da8` |
| cannbot | 53 | 53 | `88637debe061dccc41cd6808f871f446f9c46c7a` |
| cannbot-knowledge | 7 | 7 | `fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e` |
| ascendc-skills | 31 | 31 | `0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236` |
| ascend-gitcode-agent-skills | 23 | 23 | `a4011846f6d79fcee3e7b90fafe588d8a51fbc91` |
| akg | 49 | 49 | `5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff` |
| hive | 4 | 4 | `c78f267d0423d59a51a02070e5bb845fde2dbd69` |
| model-agent | 22 | 15 | `b355135ad6e4e67861a83305ba115af8928cfb83` |
| opgen | 11 | 11 | `595ce700122e1fea46d5bdc0949578b130ba404f` |
| awesome | 4 | 4 | `75ec89ce9d401be8ac95980e1c3f42f8d4315057` |
| mindiesd | 2 | 2 | `d6f5ca90a882c73b25ace504ae9da254976f53c6` |
| asc-devkit | 4 | 4 | `cd10a15efc6d2221814f6167e5055c7e640ccc7c` |
| vllm-ascend-skills | 6 | 6 | `4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3` |

Attribution of identical definitions follows the first canonical declaration in the manifest, not an authorship claim. In particular, the Ascend/agent-skills aggregation source includes the separately identified MindStudio snapshot. Model-Agent resource variants remain linked to Model-Agent even when their definition text matches another source.

## End-to-end application entrypoints

Some applications define an orchestrator in `AGENTS.md`, not `SKILL.md`. They are useful workflow entrypoints but are excluded from the skill-definition count:

- [CANNBot Triton generator](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/triton-op-generator/AGENTS.md) coordinates task construction, sketch design, coding, verification, optimization, and reporting.
- [CANNBot registered-operator workflow](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/workflows/op-develop.yaml) provides the ACLNN design, implementation, independent checks, and test-execution graph.
- [AscendC operator Agent](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/agents/agent_op_gen/AGENTS.md) describes the six-stage AscendC development sequence.

The CANNBot direct-invocation and registry-invocation `SKILL.md` entrypoints are already counted. AKG kernel verification is implemented in runtime code in addition to its skill resources.

## Preserve complete packages and dependencies

1. Select an entry's `source.project`, `source.path`, and full revision in [source metadata](../catalog/sources.yaml).
2. Clone the upstream repository and check out that exact revision. Use the pinned `directory_url` in the JSON manifest to inspect the complete package.
3. Keep sibling skills, references, scripts, templates, and declared submodules available. A copied `SKILL.md` alone is insufficient for workflows that call sibling skills or repository tools.
4. Follow that source's installation instructions for the chosen Agent client. Keep namespaced variants separate; identical names from different sources must not overwrite one another.
5. Use the target platform's matched CANN, PyTorch/torch_npu, Triton-Ascend, compiler, profiler, simulator, and test-tool versions. The catalogue's fixed links do not establish cross-repository version compatibility.

CANNBot's application, skill, and knowledge repositories have separate ownership boundaries. AscendC remote tests use the repository's runner. AKG resources are loaded by its skill system, while KernelHive expects its benchmark service/runtime. MindIE-SD adds business integration constraints on top of CANNBot routing. Sources without a root license declaration are identified as such in source metadata; upstream references and bundled third-party code retain their original terms.

## Duplicate and variant policy

Four exact directory associations were collapsed in the catalogue while retaining both source paths:

| Associated source path | Canonical source path | Identical directory tree |
|---|---|---|
| `ascendc-skills/skills/usability/op-gen/ascendc-planning/SKILL.md` | `ascendc-skills/skills/common/design-gen/SKILL.md` | `b660dcc164fc0b74df156a47857e88b15d236d11` |
| `model-agent/skills/optimization/ascendc-operator-doc-gen/SKILL.md` | `ascend-gitcode-agent-skills/community/Op/ascendc-operator-doc-gen/SKILL.md` | `b4c3e7aa0b831b15e305f937c89ed2e8c17773b4` |
| `model-agent/skills/optimization/ascendc-operator-mssanitizer/SKILL.md` | `ascend-gitcode-agent-skills/community/Op/ascendc-operator-mssanitizer/SKILL.md` | `3e083459ed77117b28aaea6b950e31b06ccbbdac` |
| `model-agent/skills/optimization/vector-triton-ascend-ops-optimizer/SKILL.md` | `ascend-gitcode-agent-skills/community/Op/vector-triton-ascend-ops-optimizer/SKILL.md` | `d8120fdbadd0cead06cd9e1aea26e4cf8cb80128` |

Seven same-definition packages have different directory trees and remain separate records. Other same-name packages may have both definition and resource differences. The following same-name groups are kept distinct:

| Declared skill name | Catalogue IDs |
|---|---|
| `ascendc-operator-code-gen` | `ascendc-operator-code-gen`, `model-agent-ascendc-operator-code-gen` |
| `ascendc-operator-code-review` | `ascendc-operator-code-review`, `model-agent-ascendc-operator-code-review` |
| `ascendc-operator-compile-debug` | `ascendc-operator-compile-debug`, `model-agent-ascendc-operator-compile-debug` |
| `ascendc-operator-design` | `ascendc-operator-design`, `model-agent-ascendc-operator-design` |
| `ascendc-operator-dev` | `ascendc-operator-dev`, `model-agent-ascendc-operator-dev` |
| `ascendc-operator-performance-eval` | `ascendc-operator-performance-eval`, `model-agent-ascendc-operator-performance-eval` |
| `ascendc-operator-performance-optim` | `ascendc-operator-performance-optim`, `ascend-agent-skills-ascendc-operator-performance-optim`, `model-agent-ascendc-operator-performance-optim` |
| `ascendc-operator-precision-debug` | `ascendc-operator-precision-debug`, `model-agent-ascendc-operator-precision-debug` |
| `ascendc-operator-precision-eval` | `ascendc-operator-precision-eval`, `model-agent-ascendc-operator-precision-eval` |
| `ascendc-operator-project-init` | `ascendc-operator-project-init`, `model-agent-ascendc-operator-project-init` |
| `ascendc-operator-testcase-gen` | `ascendc-operator-testcase-gen`, `model-agent-ascendc-operator-testcase-gen` |
| `simple-vector-triton-gpu-to-npu` | `simple-vector-triton-gpu-to-npu`, `model-agent-simple-vector-triton-gpu-to-npu` |

The aggregation repository's `official/CANNBot` submodule, `awesome-ascend-skills/external/` snapshots, and frozen application-plugin copies in `cannbot-skills` are not recounted as new sources of the same application. Standalone knowledge cards in `cannbot-knowledge/knowledge/` are not `SKILL.md` packages and are excluded.

## Review scope

The [review record](../evidence/operator-definition-review-2026-10-22.md) records source inspection, hashes, known metadata defects, and execution boundaries. Every newly listed package retains `validation.status: not-recorded`. No NPU execution, benchmark result, or upstream test pass is asserted by this import.
