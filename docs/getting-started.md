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
