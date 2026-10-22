# Operator skill definition review, 2026-10-22

## Scope and method

This source review adds the operator topic described in [the topic guide](../docs/operator-skills.md). Definitions were read at pinned commits using `git show` for local Git objects or the public GitHub/GitCode raw-content interfaces. Discovery covered each selected entry's frontmatter, declared purpose, headings, workflow text, prerequisites, outputs, and referenced resource structure. Operator tasks were selected by source directory and declared output, not by repository name alone. No source skill instructions were executed during inspection.

The [manifest](../catalog/topics/operator-skills-2026-10-22.json) is the complete file-inspection inventory. Each retained catalogue record stores the SHA-256 of the original UTF-8 source definition. Local Git objects were used so Windows checkout line-ending conversion would not redefine upstream hashes. Full commit revisions, project licenses, and maintainers appear in [source metadata](../catalog/sources.yaml).

The review selected 269 definitions from 12 source projects. Identical definition text alone initially identified 11 associations. Comparing complete directory trees found seven resource variants, retained as distinct package entries, and four exact directory associations retained in the manifest. Six pre-existing vLLM operator entries keep their 2026-10-15 review and unchanged source revision. Result: 271 topic packages and 264 unique definition byte sequences. This count is not a claim of 264 independent capabilities.

## Inspected source boundaries

| Source | Selected packages after directory associations | Revision |
|---|---:|---|
| cannbot-skills | 55 | `5891c39619a56716b6f73a335ed7709560bb2da8` |
| cannbot | 53 | `88637debe061dccc41cd6808f871f446f9c46c7a` |
| cannbot-knowledge | 7 | `fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e` |
| ascendc-skills | 31 | `0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236` |
| ascend-agent-skills | 23 | `a4011846f6d79fcee3e7b90fafe588d8a51fbc91` |
| akg | 49 | `5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff` |
| hive | 4 | `c78f267d0423d59a51a02070e5bb845fde2dbd69` |
| model-agent | 22 | `b355135ad6e4e67861a83305ba115af8928cfb83` |
| opgen | 11 | `595ce700122e1fea46d5bdc0949578b130ba404f` |
| awesome | 4 | `75ec89ce9d401be8ac95980e1c3f42f8d4315057` |
| mindiesd | 2 | `d6f5ca90a882c73b25ace504ae9da254976f53c6` |
| asc-devkit | 4 | `cd10a15efc6d2221814f6167e5055c7e640ccc7c` |
| vllm-ascend-skills | 6 | `4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3` |

- CANNBot skill inspection covers AscendC/Triton `ops/`, selected shared operator support, and community AscendC-output paths. Application inspection covers direct/registered invocation, CAKE, cross-generation/backward generation, and Triton evolution packages.
- AscendC Skills inspection covers operator planning, implementation/debugging, performance methods, relevant API UT/test generation, and sample engineering. Generic publishing and unrelated document tools are excluded.
- Ascend/agent-skills inspection covers applicable community operator packages, the A5 migration package, and the explicitly identified MindStudio profiling/optimization snapshot. Its CANNBot submodule is not duplicated.
- AKG inspection covers 43 Triton-Ascend reference/case/example definitions and six task/designer/workflow resources. All 43 are resource definitions in topic statistics.
- OpGen inspection covers all 11 Triton/AscendC packages. KernelHive inspection covers its four Ascend operator generation/optimization/migration/document packages.
- Awesome Ascend inspection covers its four local operator packages. Its external synchronized trees are omitted as mirrors.
- Model-Agent inspection includes the retained Triton/AscendC operator families and fusion-planning entry. Exact directory associations and resource variants are recorded explicitly.
- DevKit inspection covers four repository-local API development, UT, architecture, and search packages. MindIE-SD inspection covers the operator-development router and benchmark-development entry.

The existing 36 CANNBot records were moved to the reviewed CANNBot source revision consistently. Existing non-topic source paths remain unchanged, and their definition hashes were refreshed; the manifest lists those paths. No disappeared source path was silently redirected to another implementation.

## Known definition-format defects

Four source definitions were inspectable as documents but contain malformed YAML frontmatter or line-number prefixes. They remain links to the original source and are not claimed to pass an Agent Skills packaging validator:

- `cannbot`: `plugins-official/ops-registry-invoke/skills/tiling-exception-coverage/SKILL.md` (unquoted description containing a colon).
- `ascendc-skills`: `skills/common/code-review/asc-devkit-review/SKILL.md` (line-number prefixes in the source text).
- `model-agent`: `skills/optimization/ascendc-operator-code-gen/SKILL.md` and `skills/optimization/ascendc-operator-compile-debug/SKILL.md` (unquoted colon-bearing descriptions).

These metadata defects do not alter the recorded source bytes. Consumers must inspect the pinned package and upstream installation behavior before relying on automatic discovery.

## Execution conditions and limits

Planning, static review, knowledge lookup, and resource examples receive host-side reading/inspection labels. This label does not mean an embedded kernel example can execute without NPU. Complete generation/evaluation/optimization workflows usually require matched NPU tools and hardware. Simulator and Tiling-UT host workflows have their own toolchain requirements. Hardware-dependent API test paths are labeled accordingly.

No operator was compiled, no NPU job was started, and no hardware accuracy or performance qualification was performed for this import. All newly reviewed entries use `validation.status: not-recorded` and empty cases. Prior source observations and benchmark claims are not imported as new validation evidence.

The catalogue and topic files are original metadata and links. Original source licenses apply to referenced implementations, knowledge, and bundled dependencies. AscendC Skills, KernelHive, and Awesome Ascend have no root license file at the inspected revision; the catalogue records that fact without assigning its own CC0 terms to them.

## Catalogue validation

- `python scripts/validate_catalog.py`: passed for 305 skills, 10 taxonomy categories, 13 source projects, and 740 local links.
- `python scripts/render_catalog.py --check`: passed for both generated README blocks.
- A disposable catalogue copy with an unknown entry field was rejected as expected.
- Source-level checks matched 244 retained definitions to the original Git-object bytes at their pinned revisions. Seventeen connector-fetched GitHub definitions matched the blob object IDs returned by their pinned source trees. The four DevKit definitions were fetched at the recorded full commit through GitCode's raw endpoint.
- Windows checkout CRLF conversion was observed in the knowledge repository. Hash checks use original Git-object bytes rather than normalized checkout text.
- `git diff --check`: passed. These checks validate catalogue structure and source identity, not NPU behavior.
