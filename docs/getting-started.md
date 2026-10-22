# Find and use a skill

[中文](getting-started.zh.md) | English

## Select the workflow

Start from the task navigation in the [Chinese](../README.md) or [English](../README.en.md) README. Choose an entry whose expected output matches your task, then open its linked `SKILL.md`. Read the scope, inputs, workflow, and referenced files. Check the execution tag and the entry's metadata for source revision and validation evidence.

The catalogue brings together skills maintained in their original repositories. Each source defines its installation requirements and complete directory layout. Preserve that layout so referenced files and related skills can be found.

## Obtain a source collection

Use the repository URL and revision in the selected entry's [source record](../catalog/sources.yaml). The following commands obtain the collections currently represented in the catalogue. Run the commands for your chosen source in a directory where you want to keep it.

### vLLM Ascend Skills

```bash
git clone https://github.com/pisceskkk/vllm-ascend-skills.git
git -C vllm-ascend-skills checkout --detach 4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3
```

Read the source README for dependencies. Its entrypoints are under `skills/<name>/SKILL.md`, with references, scripts, and shared libraries in the same repository.

### CANNBot Skills

```bash
git clone https://gitcode.com/cann/cannbot-skills.git
git -C cannbot-skills checkout --detach 393564ae43f304426db2c206e361cd43b2811413
```

CANNBot entrypoints use paths such as `model/<name>/SKILL.md`, `ops/<name>/SKILL.md`, `graph/<name>/SKILL.md`, and `tools/<name>/SKILL.md`. Entrypoints can route to sibling skills, platform-specific instructions, or plugin agents. The upstream installation guide describes plugin discovery and setup.

### Additional PD workflows

```bash
git clone https://github.com/Yuli-yx/awesome-va-skills.git
git -C awesome-va-skills checkout --detach 8d9f7ee56d088f15a398181590c4512bfc725d6f
```

The three listed entrypoints are under `.agents/skills/`. Preserve each entire
package, including scripts, references, examples, agent metadata and LICENSE.
Pure-role capacity acceptance also uses the AISBench PD benchmark package at
the same revision. The AISBench skill originates from wangxiaoteng888; see the
source collection's `ATTRIBUTION.md` for the original revision and adaptations.
MIT applies to these three packages; other packages retain their own licenses.

Install the selected skill's Python/tool dependencies and obtain the external
AISBench/prefix-wrapper checkout where needed. Registration does not start
services or download models. Inventories and case files are runtime inputs.
The collection also contains legacy `.agents/lib/`, `.agents/scripts/` and
`.remote-dev/` tooling: preserve those paths if choosing its managed-tool
integration, or use configured MindIE remote companions. The legacy layout
does not claim compatibility with current MindIE component interfaces.

### Additional VA collection workflows

The new `va-workflows`, `va-apache-workflows` and `va-hixl-workflows` sources
share the complete collection snapshot below, with separate license groups:

```bash
git clone https://github.com/Yuli-yx/awesome-va-skills.git awesome-va-collection
git -C awesome-va-collection checkout --detach 7d3aa5f3b55049a2f917b4ca682c1e9963033c18
```

Keep the complete selected package and required `.agents/lib/`, `.agents/scripts/`
and `.remote-dev/` paths. Legacy execution helpers have not been ported to a new
MindIE coordinator API. Inspect differences before integrating with an existing
workspace; do not overwrite its runtime state. Original package attribution and
MIT/Apache/CANN license distinctions remain in the collection's ATTRIBUTION.md.
The earlier three PD entries intentionally retain their separate reviewed source.

## Load the selected instructions

Give your coding assistant the actual entrypoint path from `source.path` in the selected catalogue entry, the target repository, and the task inputs. If your client supports discovering skill directories, configure discovery using that client's documented settings and verify that the selected skill was loaded.

A task prompt can follow this structure:

> Read the selected SKILL.md and its relevant references. Use the project and input paths I provide to complete the task. State the expected output, execute the applicable workflow, and return the result with its evidence and remaining gaps.

For offline profiling analysis, provide the profiler output root and the question to investigate. For service execution, provide the model path, source revisions, devices, topology, workload, and desired result. Triton development additionally needs a trusted reference and a declared shape/dtype/layout case matrix.

## Understand execution conditions

| Value | Meaning |
|---|---|
| `offline` | The declared analysis workflow can operate on existing artifacts; install script dependencies from upstream. |
| `host` | Code inspection, planning, or host tools such as CANN Simulator; toolchains or network access may still be required. |
| `npu` | Completing the workflow includes Ascend execution, collection, or timing. Planning and reading can happen locally. |
| `depends-on-checks` | The required hardware depends on the selected validation cases. |

Use the target project's matched software versions. Consult upstream instructions for CANN, PyTorch, `torch_npu`, vLLM Ascend, Triton, profilers, and benchmarking tools as applicable.

For example, CANNBot model adaptation targets PyTorch and, where selected, `cann-recipes-infer`. Quantization entries cover existing `compressed-tensors` artifacts. CATLASS, PyPTO, TileLang, and Triton entrypoints require their respective source trees or toolchains. `ops-simulator` needs CANN Simulator. Diagnostic tools carry product-form and permission requirements in their entrypoints: asys targets Ascend EP, and msaicerr analysis uses the originating runtime environment. Check the [validation policy](validation-policy.md) to interpret recorded compatibility and reproduction evidence.

## Preserve results

Retain source revisions, the execution environment, case configuration, logs, and output artifact paths. Share a reproduction or a useful correction through the [contribution guide](../CONTRIBUTING.md), with the fields described in the [validation policy](validation-policy.md).
