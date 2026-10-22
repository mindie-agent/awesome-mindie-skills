<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img src="assets/banner-light.svg" alt="Awesome MindIE Skills — Curated Agent Skills for Ascend Inference" width="960">
  </picture>
</p>

# Awesome MindIE Skills

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-0F766E.svg)](LICENSE)

[中文](README.md) | English

A shared catalogue of Agent Skills for **Ascend inference engineering**, helping developers find, use, and contribute reusable engineering workflows by task.

The catalogue covers environment setup, model integration, serving, correctness, performance analysis, and operator development. Each entry links to its original source and records execution requirements, a source revision, and validation information. Skills typically use a `SKILL.md` file to organize task instructions, workflows, and references for a coding assistant to load as needed.

Share useful skills, improve entry descriptions, and contribute reproducible results from using them.

## Start with a task

Navigate directly to the category matching your engineering goal:

| Task | Category |
|---|---|
| Inspect NPU environment or configure CANN software stack | [Environment and dependencies](#environment) |
| Adapt a model to Ascend and establish an execution baseline | [Model integration and conversion](#model-integration) |
| Deploy inference services or configure PD disaggregation | [Serving and scaling](#serving) |
| Verify output correctness and accuracy alignment | [Correctness and accuracy](#correctness) |
| Measure throughput and latency, or detect regressions | [Benchmarking and regressions](#benchmarking) |
| Collect and analyze traces, cross-rank behavior, or memory usage | [Profiling and bottleneck analysis](#profiling) |
| Apply quantization, KV caches, graph mode, or multistream optimization | [Inference optimization](#optimization) |
| Develop operators with Ascend C, CATLASS, PyPTO, TileLang, or Triton | [Operator development and migration](#operators) |
| Diagnose runtime crashes, hangs, or graph compiler errors | [Debugging](#debugging) |
| Plan validation for code changes and delivery | [Delivery and operations](#delivery) |

## How to use a skill

Applying a skill to your project follows four basic steps:

1. **Choose a skill**: Select the entry matching your task from the [Skill catalogue](#skill-catalogue);
2. **Review scope and dependencies**: Check the declared scope, software prerequisites, and execution conditions (such as offline analysis, host tools, or NPU requirements);
3. **Obtain the source**: Clone the upstream repository at its pinned commit revision (see the [usage guide](docs/getting-started.md) for concrete clone and setup commands);
4. **Load and execute**: Point your AI assistant or agent environment to the skill's `SKILL.md`, providing the target project path and task inputs.

**Generic prompt example**:

> Read `<skill-path>/SKILL.md` and follow its defined workflow to perform `<task-name>` on my project at `/path/to/project` with inputs `<inputs>`, reporting the findings and supporting evidence paths.

## Triton and AscendC operator topic

The topic covers specification, pipeline design, implementation/migration, numerical tests, review/delivery, performance work, and knowledge support. It contains **264 distinct definitions in 271 package entries**, including 58 knowledge resources, examples, and cases. Same-name variants retain their pinned versions and complete directory context.

[Classification and usage](docs/operator-skills.md) · [Machine-readable statistics](catalog/topics/operator-skills-2026-10-22.json) · [Entry table CSV](catalog/topics/operator-skills-2026-10-22.csv)


## Skill catalogue

Entries are grouped by their primary task and show technology tags, execution requirements, and metadata links. Definition reviews inspect pinned skill instructions and their declared purpose. Execution reproductions record specific environments and cases; coverage counts appear below.

Execution tags describe the following conditions:

- `NPU execution`: The complete workflow requires Ascend NPU hardware (planning and code inspection can be done locally);
- `Offline analysis`: Operates on existing profiling traces or diagnostic artifacts with the required host dependencies;
- `Host tools`: Runs host-side inspection, tiling design, or tools such as CANN Simulator;
- `Hardware depends on checks`: Required hardware depends on the specific validation test cases chosen.

Each entry's metadata links to its review scope, reproduction cases, and evidence. See the [catalogue format](docs/catalog-format.md) and [validation policy](docs/validation-policy.md) for fields and criteria.

<!-- CATALOG:START -->

342 skills · 10 categories

Definitions reviewed: 342 · Entries with execution reproductions: 1. See each entry's metadata for scope.

| Upstream Source | Listed | Maintainer | License |
|---|---|---|---|
| [vllm-ascend-skills](https://github.com/pisceskkk/vllm-ascend-skills) | 17 | pisceskkk | MIT |
| [cannbot-skills](https://gitcode.com/cann/cannbot-skills) | 78 | CANNBot SIG (cann) | CANN Open Software License v2.0 |
| [ascend-pooling-workflows](https://github.com/Yuli-yx/awesome-mindie-skills) | 1 | zouyida2052 and Yuli-yx | CC0-1.0 AND MIT (see package NOTICE) |
| [awesome-va-skills](https://github.com/Yuli-yx/awesome-va-skills) | 3 | Yuli-yx (adapted collection); wangxiaoteng888 (AISBench origin) | MIT (the three listed packages only) |
| [va-workflows](https://github.com/Yuli-yx/awesome-va-skills) | 10 | Yuli-yx collection; original authors credited in ATTRIBUTION.md | MIT |
| [va-hixl-workflows](https://github.com/Yuli-yx/awesome-va-skills) | 5 | Yuli-yx collection; original authors credited in ATTRIBUTION.md | CANN-2.0 |
| [va-apache-workflows](https://github.com/Yuli-yx/awesome-va-skills) | 4 | Yuli-yx collection; original authors credited in ATTRIBUTION.md | Apache-2.0 |
| [blue-server-toolkit](https://github.com/xuchi-0808/blue-server-toolkit) | 7 | xuchi-0808 | MIT |
| [ascend-agent-skills](https://github.com/Henry-Avery/ascend-agent-skills) | 2 | Henry-Avery | MIT |
| [vllm-mrv2-kernel-tools](https://github.com/Liamup777/vllm-mrv2-kernel-tools) | 1 | Liamup777 | Apache-2.0 |
| [upstream-downstream-analysis](https://github.com/SOMEONEUNSEEN/awesome-mindie-skills) | 1 | SOMEONEUNSEEN | CC0-1.0 |
| [vllm-ascend-pd-disaggregation-skills](https://github.com/nwpu-zxr/vllm-ascend-pd-disaggregation-skills) | 3 | nwpu-zxr | MIT |
| [cannbot](https://gitcode.com/cann/cannbot) | 53 | CANNBot SIG (cann) | CANN Open Software License v2.0; CAKE plugin also includes Apache-2.0 |
| [cannbot-knowledge](https://gitcode.com/cann/cannbot-knowledge) | 7 | CANNBot SIG (cann) | CANN Open Software License v2.0 |
| [ascendc-skills](https://gitcode.com/ascendc-agent/ascendc-skills) | 31 | ascendc-agent | Not declared in the pinned repository root |
| [akg](https://github.com/mindspore-ai/akg) | 49 | MindSpore AKG maintainers | Apache-2.0 |
| [hive](https://github.com/KernelHive/ascendc-skill) | 4 | KernelHive | Not declared in the pinned repository root; bundled references retain their terms |
| [model-agent](https://gitcode.com/Ascend/model-agent) | 22 | Ascend community | BSD-3-Clause; incorporated skills retain their upstream terms |
| [opgen](https://github.com/Just-it/AscendOpGenAgent) | 11 | Just-it | Apache-2.0 |
| [awesome](https://github.com/ascend-ai-coding/awesome-ascend-skills) | 4 | ascend-ai-coding | Not declared in the pinned repository root; synchronized sources retain their terms |
| [mindiesd](https://github.com/Ascend/MindIE-SD) | 2 | Ascend MindIE-SD maintainers | MulanPSL-2.0 |
| [asc-devkit](https://gitcode.com/cann/asc-devkit) | 4 | CANN AscendC maintainers | CANN Open Software License v2.0 |
| [ascend-gitcode-agent-skills](https://gitcode.com/Ascend/agent-skills) | 23 | Ascend community | Apache-2.0 (code/configuration) AND CC-BY-SA-4.0 (documentation); incorporated sources retain their terms |

- [Environment and dependencies](#environment)
- [Model integration and conversion](#model-integration)
- [Serving and scaling](#serving)
- [Correctness and accuracy](#correctness)
- [Benchmarking and regressions](#benchmarking)
- [Profiling and bottleneck analysis](#profiling)
- [Inference optimization](#optimization)
- [Operator development and migration](#operators)
- [Debugging](#debugging)
- [Delivery and operations](#delivery)

<a id="environment"></a>

### Environment and dependencies

Check drivers, CANN, framework compatibility, containers, and devices.

- [ascendc-env-check](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-env-check/SKILL.md) — Inspect NPU devices, CANN configuration, toolchain dependencies, and the detected architecture.
  `CANNBot` `Ascend C` `Implementation and migration` `NPU execution` · [Metadata](catalog/skills/ascendc-env-check.yaml)
- [blue-server-provisioning](https://github.com/xuchi-0808/blue-server-toolkit/blob/5707a86922713f830f1f5fea2bedbb0a0a1cdc3a/skills/blue-server-provisioning/SKILL.md) — Bring up fresh Ascend servers and containers — bare-metal HDK driver and firmware installation (HwHiAiUser, driver before firmware), container creation with start-docker-A2/A3/A5.sh, and image-ID discipline.
  `Ascend` `CANN` `Docker` `NPU execution` · [Metadata](catalog/skills/blue-server-provisioning.yaml)
- [blue-vllm-ascend-build](https://github.com/xuchi-0808/blue-server-toolkit/blob/5707a86922713f830f1f5fea2bedbb0a0a1cdc3a/skills/blue-vllm-ascend-build/SKILL.md) — Build or upgrade vllm-ascend from source — editable two-step install, version pairing via vllm-main-verified.commit, setuptools 77 or newer, pip mirror setup, rsync-then-chown sync, and an error-keyword FAQ; pure CPU.
  `vLLM Ascend` `CANN` `Host tools` · [Metadata](catalog/skills/blue-vllm-ascend-build.yaml)
- [cann-env-setup](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/cann-env-setup/SKILL.md) — Prepare CANN installation and environment configuration for Ascend operator development.
  `CANNBot` `Operator support` `Implementation and migration` `NPU execution` · [Metadata](catalog/skills/cann-env-setup.yaml)
- [machine-management](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/machine-management/SKILL.md) — Add, verify, repair, or remove a managed remote NPU host for this workspace.
  `Ascend` `vLLM Ascend` `Hardware depends on checks` `Workflow` · [Metadata](catalog/skills/machine-management.yaml)
- [remote-code-parity](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/remote-code-parity/SKILL.md) — Ensure a ready remote runtime runs the exact current local workspace state before any remote smoke, service launch, or benchmark.
  `Ascend` `vLLM Ascend` `Host tools` `Workflow` · [Metadata](catalog/skills/remote-code-parity.yaml)
- [remote-toolbox](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/remote-toolbox/SKILL.md) — Resolve, probe, execute, observe jobs, sync, manage service lifecycle, transfer artifacts, and clean VAWS remote Ascend session containers through structured agent-facing CLI entrypoints..
  `Ascend` `vLLM Ascend` `Host tools` `Workflow` · [Metadata](catalog/skills/remote-toolbox.yaml)
- [repo-env-check](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-env-check/SKILL.md) — Inspect selected Python/CANN environment candidates and record scoped environment evidence.
  `CANNBot` `Ascend C` `Implementation and migration` `NPU execution` · [Metadata](catalog/skills/repo-env-check.yaml)
- [repo-init](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/repo-init/SKILL.md) — Initialize this workspace after clone.
  `Ascend` `vLLM Ascend` `Host tools` `Workflow` · [Metadata](catalog/skills/repo-init.yaml)
- [session-management](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/session-management/SKILL.md) — Create, list, inspect, remove, and garbage-collect isolated VAWS agent sessions.
  `Ascend` `vLLM Ascend` `Host tools` `Workflow` · [Metadata](catalog/skills/session-management.yaml)
- [triton-operator-env-config](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-env-config/SKILL.md) — Verify the CANN, Python, PyTorch, torch_npu, and Triton-Ascend development environment.
  `Model Agent` `Triton` `Implementation and migration` `NPU execution` · [Metadata](catalog/skills/triton-operator-env-config.yaml)
- [vllm-ascend-build](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/vllm-ascend-build/SKILL.md) — Compile and verify vLLM-Ascend from a pinned workspace or PR revision inside a ready Ascend container.
  `Ascend` `vLLM Ascend` `Host tools` `Workflow` · [Metadata](catalog/skills/vllm-ascend-build.yaml)

<a id="model-integration"></a>

### Model integration and conversion

Integrate models, convert weights, and verify configuration and input/output contracts.

- [main2main](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/main2main/SKILL.md) — Adapt vLLM-Ascend to upstream vLLM main changes.
  `Ascend` `vLLM Ascend` `Offline analysis` `Workflow` · [Metadata](catalog/skills/main2main.yaml)
- [model-infer-migrator](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-migrator/SKILL.md) — Adapt HF models or local code to cann-recipes-infer or a standalone runner and establish an eager inference baseline.
  `CANNBot` `PyTorch` `cann-recipes-infer` `NPU execution` · [Metadata](catalog/skills/model-infer-migrator.yaml)
- [modelscope](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/modelscope/SKILL.md) — Download, resume, status-check, and SHA256-verify ModelScope model weights.
  `Ascend` `vLLM Ascend` `Host tools` `Workflow` · [Metadata](catalog/skills/modelscope.yaml)
- [pd-disaggregation-design](https://github.com/nwpu-zxr/vllm-ascend-pd-disaggregation-skills/blob/2852c18ac977783f336f8c8864ca84dfee3f5cc6/skills/pd-disaggregation-design/SKILL.md) — Design and review PD connectors; assess new cache layouts against specs, shapes, strides and storage semantics to identify compatibility gaps.
  `vLLM` `vLLM Ascend` `PD` `KV Cache` `Hardware depends on checks` · [Metadata](catalog/skills/pd-disaggregation-design.yaml)
- [vllm-ascend-model-adapter](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/vllm-ascend-model-adapter/SKILL.md) — Adapt and debug existing or new models for vLLM on Ascend NPU.
  `Ascend` `vLLM Ascend` `NPU execution` `Workflow` · [Metadata](catalog/skills/vllm-ascend-model-adapter.yaml)

<a id="serving"></a>

### Serving and scaling

Deploy colocated or disaggregated services and verify topology, endpoints, and requests.

- [ascend-memcache-pooling](https://github.com/Yuli-yx/awesome-mindie-skills/blob/2844c25cd3f63cd0cd817cce866de827653babf2/skills/ascend-memcache-pooling/SKILL.md) — Deploy A3/A5 DRAM/SSD pools, preserve P/D transport, inspect Host RoCE and monitor multi-DP HBM, external reuse and SSD readback evidence.
  `MemCache` `MemFabric` `vLLM Ascend` `SSD` `Host RoCE` `Monitoring` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascend-memcache-pooling.yaml)
- [blue-vllm-service](https://github.com/xuchi-0808/blue-server-toolkit/blob/5707a86922713f830f1f5fea2bedbb0a0a1cdc3a/skills/blue-vllm-service/SKILL.md) — Manage the vLLM-on-Ascend service lifecycle — start and stop vllm serve in containers, health checks, multi-service layout, P/D disaggregated bring-up (mooncake, load-balance proxy), TP and parallelism planning, and graph-mode debugging.
  `vLLM Ascend` `NPU execution` · [Metadata](catalog/skills/blue-vllm-service.yaml)
- [model-infer-parallel-analysis](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-parallel-analysis/SKILL.md) — Analyze model structure and Atlas A2/A3 specifications to propose parallel_config candidates with quantitative rationale.
  `CANNBot` `PyTorch` `Parallelism` `Host tools` · [Metadata](catalog/skills/model-infer-parallel-analysis.yaml)
- [model-infer-parallel-impl](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-parallel-impl/SKILL.md) — Implement approved TP/EP configurations across parallel layers, communication groups, weights, and launch settings, then validate execution.
  `CANNBot` `PyTorch` `HCCL` `NPU execution` · [Metadata](catalog/skills/model-infer-parallel-impl.yaml)
- [pd-disaggregation-serving](https://github.com/nwpu-zxr/vllm-ascend-pd-disaggregation-skills/blob/2852c18ac977783f336f8c8864ca84dfee3f5cc6/skills/pd-disaggregation-serving/SKILL.md) — Prepare or deploy P/D/proxy services using existing lifecycle controllers when available; verify routing, actual KV transfer and cleanup.
  `vLLM` `vLLM Ascend` `PD` `KV Cache` `Hardware depends on checks` `Workflow` · [Metadata](catalog/skills/pd-disaggregation-serving.yaml)
- [platform-agent-launch-config](https://github.com/Henry-Avery/ascend-agent-skills/blob/c95957444543f136fa30ba054d1afd5cf3900622/skills/platform-agent-launch-config/SKILL.md) — Trace an inference platform launch path and reuse existing configuration to prepare field guidance, agent scripts, differences, and gaps for a human or agent handoff.
  `vLLM Ascend` `AiClusterHub` `PD` `Host tools` · [Metadata](catalog/skills/platform-agent-launch-config.yaml)
- [vllm-ascend-pd-serving](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-pd-serving/SKILL.md) — Plan and review prefill/decode vLLM Ascend serving with explicit roles, connectors, ordering and KV transfer evidence.
  `vLLM Ascend` `PD` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-pd-serving.yaml)
- [vllm-ascend-serving](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-serving/SKILL.md) — Plan and review one colocated vLLM Ascend service lifecycle, including source pairing, device selection, launch, health, and cleanup.
  `vLLM Ascend` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-serving.yaml)

<a id="correctness"></a>

### Correctness and accuracy

Fix references and case matrices to compare outputs, numerical error, and task quality.

- [aisbench-accuracy](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/aisbench-accuracy/SKILL.md) — Run AISBench dataset accuracy evaluation against a running vLLM service, aligning sampling, prompts and answer postprocessing with the baseline.
  `Ascend` `vLLM Ascend` `NPU execution` `Workflow` · [Metadata](catalog/skills/aisbench-accuracy.yaml)
- [aog-input-gen-builder](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-input-gen-builder/SKILL.md) — Generate normal and edge-case input datasets from an AscendC source package or differentiable reference.
  `CANNBot` `Ascend C` `Testing and numerical validation` `Community` `NPU execution` · [Metadata](catalog/skills/aog-input-gen-builder.yaml)
- [api-perf-test](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/docs/skill_3510_api_perf_test/SKILL.md) — Build and run DAV_3510 API performance cases and inspect profiling results.
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/api-perf-test.yaml)
- [api-ut](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/api-ut/SKILL.md) — Generate AscendC API unit tests and use coverage reports to fill missing cases.
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `Hardware depends on checks` · [Metadata](catalog/skills/api-ut.yaml)
- [asc-api-test](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/docs/asc-api-test/SKILL.md) — Generate AscendC API test examples and their data/checking assets.
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/asc-api-test.yaml)
- [asc-api-ut-gen](https://gitcode.com/cann/asc-devkit/blob/cd10a15efc6d2221814f6167e5055c7e640ccc7c/.agent/skills/asc-api-ut-gen/SKILL.md) — Generate DevKit API gtests with structured architecture constraints and coverage-driven case backfill.
  `Ascend DevKit` `Ascend C` `Testing and numerical validation` `Hardware depends on checks` · [Metadata](catalog/skills/asc-api-ut-gen.yaml)
- [ascendc-evaluation](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/ascendc-evaluation/SKILL.md) — Evaluate multi-case AscendC numerical correctness and collect operator performance evidence.
  `CANNBot` `Ascend C` `Testing and numerical validation` `Community` `NPU execution` · [Metadata](catalog/skills/ascendc-evaluation.yaml)
- [ascendc-operator-precision-eval](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-precision-eval/SKILL.md) — Generate a shape/dtype/boundary precision suite and produce numerical comparison reports.
  `Ascend Agent Skills` `Ascend C` `Testing and numerical validation` `Community` `NPU execution` · [Metadata](catalog/skills/ascendc-operator-precision-eval.yaml)
- [ascendc-operator-st-gen](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-st-gen/SKILL.md) — Create or repair ATK ST dual-reference numerical validation for CANN operators.
  `Ascend Agent Skills` `Ascend C` `Testing and numerical validation` `Community` `NPU execution` · [Metadata](catalog/skills/ascendc-operator-st-gen.yaml)
- [ascendc-operator-testcase-gen](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-testcase-gen/SKILL.md) — Generate a shared operator case specification and golden contract for precision and performance evaluation.
  `Ascend Agent Skills` `Ascend C` `Testing and numerical validation` `Community` `NPU execution` · [Metadata](catalog/skills/ascendc-operator-testcase-gen.yaml)
- [ascendc-ops-evaluation](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/ascendc-ops-evaluation/SKILL.md) — Build and deploy operators from CANN operator repositories and compare baseline and evolved implementations.
  `CANNBot` `Ascend C` `Testing and numerical validation` `Community` `NPU execution` · [Metadata](catalog/skills/ascendc-ops-evaluation.yaml)
- [ascendc-whitebox-design](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-whitebox-design/SKILL.md) — Extract tiling/kernel paths and generate executable whitebox case matrices with coverage checks.
  `CANNBot` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/ascendc-whitebox-design.yaml)
- [blackbox-tester](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/blackbox-tester/SKILL.md) — Run full TTK ACLNN blackbox suites against the deployed candidate and validate result counts.
  `CANNBot` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/blackbox-tester.yaml)
- [kernel-verifier](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/triton/kernel-verifier/SKILL.md) — Check Triton implementation structure, run golden comparisons, and benchmark valid candidates.
  `AscendOpGenAgent` `Triton` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/kernel-verifier.yaml)
- [model-agent-ascendc-operator-precision-eval](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-precision-eval/SKILL.md) — Generate a shape/dtype/boundary precision suite and produce numerical comparison reports.
  `Model Agent` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/model-agent-ascendc-operator-precision-eval.yaml)
- [model-agent-ascendc-operator-testcase-gen](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-testcase-gen/SKILL.md) — Generate a shared operator case specification and golden contract for precision and performance evaluation.
  `Model Agent` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/model-agent-ascendc-operator-testcase-gen.yaml)
- [operator-test](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/ut-gen/SKILL.md) — Describe AscendC cases in an optest plan and execute data generation, invocation, and validation.
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/operator-test.yaml)
- [remote-npu-test](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/remote-npu-test/SKILL.md) — Run standalone tests through the repository remote runner and collect structured execution evidence.
  `AscendC Agent` `Operator support` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/remote-npu-test.yaml)
- [repo-test-develop](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-test-develop/SKILL.md) — Create proto/golden/cases assets and run blackbox, whitebox, and regression evaluation with CANN Bench.
  `CANNBot` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/repo-test-develop.yaml)
- [simt-stc-doc](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/simt-stc-doc/SKILL.md) — Create a SIMT test-case and defect-record template from a confirmed requirement.
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/simt-stc-doc.yaml)
- [single-api-test](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/docs/skill_3510_single_api_test/SKILL.md) — Generate and execute a single DAV_3510 API validation case.
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/single-api-test.yaml)
- [st-verifier](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/st-verifier/SKILL.md) — Independently check ST coverage, design consistency, framework integration, and execution evidence.
  `CANNBot` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/st-verifier.yaml)
- [tilelang2ascend-precision-tuning](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/tilelang2ascend-precision-tuning/SKILL.md) — Use DumpTensor and staged comparisons to locate and repair AscendC precision failures.
  `CANNBot` `Ascend C` `Testing and numerical validation` `Community` `NPU execution` · [Metadata](catalog/skills/tilelang2ascend-precision-tuning.yaml)
- [tiling-exception-coverage](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/tiling-exception-coverage/SKILL.md) — Design negative Tiling UTs with explicit failure/degradation assertions.
  `CANNBot` `Ascend C` `Testing and numerical validation` `Host tools` · [Metadata](catalog/skills/tiling-exception-coverage.yaml)
- [tiling-ut-harness](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/tiling-ut-harness/SKILL.md) — Build and run host-side TilingFunc gtests with the declared platform mocks and installed host library.
  `CANNBot` `Ascend C` `Testing and numerical validation` `Host tools` · [Metadata](catalog/skills/tiling-ut-harness.yaml)
- [triton-op-verifier](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-op-verifier/SKILL.md) — Check Triton implementation authenticity, execute golden comparisons, and collect benchmark results.
  `CANNBot` `Triton` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/triton-op-verifier.yaml)
- [triton-operator-precision-eval](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-precision-eval/SKILL.md) — Compare a Triton implementation with PyTorch and generate numerical error reports.
  `Model Agent` `Triton` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/triton-operator-precision-eval.yaml)
- [vllm-ascend-correctness-validation](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-correctness-validation/SKILL.md) — Design and compare deterministic vLLM Ascend correctness cases across code states, execution modes and API paths.
  `vLLM Ascend` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-correctness-validation.yaml)

<a id="benchmarking"></a>

### Benchmarking and regressions

Evaluate throughput and latency using warmup, repeated measurements, and controlled comparisons.

- [aisbench-pd-benchmark](https://github.com/Yuli-yx/awesome-va-skills/blob/8d9f7ee56d088f15a398181590c4512bfc725d6f/.agents/skills/aisbench-pd-benchmark/SKILL.md) — Prepare proxy-routed AISBench cases with tokenizer-based datasets, separate warmup and formal runs, and captured configuration and results.
  `vLLM Ascend` `AISBench` `PD` `NPU execution` · [Metadata](catalog/skills/aisbench-pd-benchmark.yaml)
- [aog-perf-eval](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-perf-eval/SKILL.md) — Evaluate generated AscendC operators with profiler and wall-clock measurements.
  `CANNBot` `Ascend C` `Profiling and optimization` `Community` `NPU execution` · [Metadata](catalog/skills/aog-perf-eval.yaml)
- [ascendc-operator-performance-eval](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-performance-eval/SKILL.md) — Benchmark an AscendC implementation against its reference using profiler cases and comparison reports.
  `Ascend Agent Skills` `Ascend C` `Profiling and optimization` `Community` `NPU execution` · [Metadata](catalog/skills/ascendc-operator-performance-eval.yaml)
- [model-agent-ascendc-operator-performance-eval](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-performance-eval/SKILL.md) — Benchmark an AscendC implementation against its reference using profiler cases and comparison reports.
  `Model Agent` `Ascend C` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/model-agent-ascendc-operator-performance-eval.yaml)
- [pd-pure-role-benchmark](https://github.com/Yuli-yx/awesome-va-skills/blob/8d9f7ee56d088f15a398181590c4512bfc725d6f/.agents/skills/pd-pure-role-benchmark/SKILL.md) — Validate pure Prefill and Decode capacity and end-to-end steady QPS with TTFT, TPOT, cache-hit, role-bottleneck and MTP controls.
  `vLLM Ascend` `AISBench` `PD` `MTP` `NPU execution` `Workflow` · [Metadata](catalog/skills/pd-pure-role-benchmark.yaml)
- [triton-operator-performance-eval](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-performance-eval/SKILL.md) — Measure Triton-Ascend latency and hardware utilization with msprof and report bottlenecks.
  `Model Agent` `Triton` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/triton-operator-performance-eval.yaml)
- [vllm-ascend-benchmark](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-benchmark/SKILL.md) — Measure one vLLM Ascend online-serving code state with warmup, repeated runs and normalized metrics.
  `vLLM Ascend` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-benchmark.yaml)
- [vllm-ascend-performance-regression](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-performance-regression/SKILL.md) — Compare baseline and candidate vLLM Ascend serving performance using controlled alternating runs.
  `vLLM Ascend` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-performance-regression.yaml)

<a id="profiling"></a>

### Profiling and bottleneck analysis

Collect or analyze traces, per-rank behavior, and HBM use with traceable evidence.

- [ascend-memory-profiling](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/ascend-memory-profiling/SKILL.md) — Profile and attribute HBM memory usage on Ascend NPU for vLLM serving scenarios.
  `Ascend` `vLLM Ascend` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascend-memory-profiling.yaml)
- [ascend-profiling-analysis](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-profiling-analysis/SKILL.md) — Analyze Ascend profiler roots into rank, step, layer, block, operator and cross-rank findings with traceable evidence.
  `Ascend` `Profiling` `Offline analysis` · [Metadata](catalog/skills/ascend-profiling-analysis.yaml)
- [ascend-profiling-collection](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/ascend-profiling-collection/SKILL.md) — Collect one Ascend torch-profiler case end-to-end on a workspace-managed remote NPU container.
  `Ascend` `vLLM Ascend` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascend-profiling-collection.yaml)
- [blue-vllm-profiling](https://github.com/xuchi-0808/blue-server-toolkit/blob/5707a86922713f830f1f5fea2bedbb0a0a1cdc3a/skills/blue-vllm-profiling/SKILL.md) — Capture and interpret profiling for vLLM on Ascend — launch flags, /start_profile and /stop_profile, steady-state windows, per-rank analyse() parsing, step_trace_time buckets, operator attribution, and bottleneck triage.
  `vLLM Ascend` `Profiling` `torch_npu` `NPU execution` · [Metadata](catalog/skills/blue-vllm-profiling.yaml)
- [ge-memory-analysis](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/graph/ge-memory-analysis/SKILL.md) — Triage GE device memory, host leaks, and operator addresses, and attribute memory use from logs and reports.
  `CANNBot` `GE` `HBM` `Hardware depends on checks` · [Metadata](catalog/skills/ge-memory-analysis.yaml)
- [model-infer-perf-breakdown](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-perf-breakdown/SKILL.md) — Break down kernel_details.csv and traces by model component and generate an HTML report of timing, gaps, and anomalous layers.
  `CANNBot` `Ascend` `Profiling` `Offline analysis` · [Metadata](catalog/skills/model-infer-perf-breakdown.yaml)
- [model-infer-profiling](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-profiling/SKILL.md) — Collect model profiling data through built-in or injected torch_npu.profiler instrumentation and verify output completeness.
  `CANNBot` `PyTorch` `torch_npu` `NPU execution` · [Metadata](catalog/skills/model-infer-profiling.yaml)
- [msot-msopprof-operator-profiler](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/official/MindStudio/skills/msot-msopprof-operator-profiler/SKILL.md) — Select device/simulator profiling modes and interpret msOpProf metrics, timelines, and bottlenecks.
  `Ascend Agent Skills` `Operator support` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/msot-msopprof-operator-profiler.yaml)
- [op-mfu-calculator](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/official/MindStudio/skills/op-mfu-calculator/SKILL.md) — Calculate operator FLOPs utilization from shape, duration, dtype, and the declared hardware peak.
  `Ascend Agent Skills` `Operator support` `Profiling and optimization` `Offline analysis` · [Metadata](catalog/skills/op-mfu-calculator.yaml)
- [ops-profiling](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ops-profiling/SKILL.md) — Collect comparable operator latency and hardware metrics and report per-kernel bottlenecks.
  `CANNBot` `Operator support` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/ops-profiling.yaml)
- [performance-analyzer](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/ascendc/performance-analyzer/SKILL.md) — Collect and compare AscendC kernel performance and identify optimization directions.
  `AscendOpGenAgent` `Ascend C` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/performance-analyzer.yaml)
- [performance-summary](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/performance-summary/SKILL.md) — Summarize kernel benchmark results and optimization observations across cases.
  `AKG` `Operator support` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/performance-summary.yaml)
- [triton-mfu-analyzer](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-mfu-analyzer/SKILL.md) — Measure operator utilization and decompose per-kernel latency with dtype-aware peak accounting.
  `CANNBot` `Triton` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/triton-mfu-analyzer.yaml)
- [triton-simulator-optimizer](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-simulator-optimizer/SKILL.md) — Collect simulator instruction/pipe evidence and map bottlenecks to optimization actions.
  `CANNBot` `Triton` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/triton-simulator-optimizer.yaml)
- [vllm-ascend-memory-profiling](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-memory-profiling/SKILL.md) — Attribute Ascend HBM use during vLLM serving to weights, KV cache, HCCL, activations and runtime components.
  `vLLM Ascend` `HBM` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-memory-profiling.yaml)
- [vllm-ascend-profiling-collection](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-profiling-collection/SKILL.md) — Collect one vLLM Ascend serving torch-profiler case with a verified workload window and complete rank outputs.
  `vLLM Ascend` `torch-profiler` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-profiling-collection.yaml)

<a id="optimization"></a>

### Inference optimization

Optimize execution, scheduling, and resource overlap with paired correctness and performance validation.

- [ascend-model-multistream-overlap-skill](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-model-multistream-overlap-skill/SKILL.md) — Design Ascend model multistream overlap from verified source mapping, resource-aware DAGs and paired validation.
  `Ascend` `Multistream` `NPU execution` · [Metadata](catalog/skills/ascend-model-multistream-overlap-skill.yaml)
- [ge-fusion-pass-skill](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/graph/ge-fusion-pass-skill/SKILL.md) — Coordinate requirements, implementation, and functional validation for GE custom fusion passes with stage evidence.
  `CANNBot` `GE` `CANN` `Hardware depends on checks` `Workflow` · [Metadata](catalog/skills/ge-fusion-pass-skill.yaml)
- [model-infer-fusion](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-fusion/SKILL.md) — Match PyTorch model computation patterns to torch_npu fused operators, implement replacements, and validate them.
  `CANNBot` `PyTorch` `torch_npu` `NPU execution` · [Metadata](catalog/skills/model-infer-fusion.yaml)
- [model-infer-graph-mode](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-graph-mode/SKILL.md) — Adapt model decode paths to npugraph_ex or GE graph mode, address graph breaks, and validate results.
  `CANNBot` `PyTorch` `Graph` `NPU execution` · [Metadata](catalog/skills/model-infer-graph-mode.yaml)
- [model-infer-kvcache](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-kvcache/SKILL.md) — Select and implement contiguous, paged, MLA, or sliding-window KV caches, integrate attention operators, and validate behavior.
  `CANNBot` `PyTorch` `KV cache` `NPU execution` · [Metadata](catalog/skills/model-infer-kvcache.yaml)
- [model-infer-multi-stream](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-multi-stream/SKILL.md) — Provide model DAG analysis, multistream API selection, synchronization, and core-allocation guidance for planning and overlap validation.
  `CANNBot` `PyTorch` `Multistream` `Hardware depends on checks` · [Metadata](catalog/skills/model-infer-multi-stream.yaml)
- [model-infer-prefetch](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-prefetch/SKILL.md) — Design weight-prefetch windows for confirmed memory-bound hotspots, integrate npu_prefetch, and measure gains.
  `CANNBot` `torch_npu` `Prefetch` `NPU execution` · [Metadata](catalog/skills/model-infer-prefetch.yaml)
- [model-infer-quantization](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-quantization/SKILL.md) — Integrate existing compressed-tensors quantized weights and verify artifact contracts, runtime mapping, activation, and gains.
  `CANNBot` `PyTorch` `compressed-tensors` `NPU execution` · [Metadata](catalog/skills/model-infer-quantization.yaml)

<a id="operators"></a>

### Operator development and migration

Connect kernel implementation, case validation, and per-shape optimization.

- [aiss-tiling-solver](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/aiss-tiling-solver/SKILL.md) — Prepare inputs for AISS-TilingSolver, solve tiling parameters, and interpret the result.
  `CANNBot` `Ascend C` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/aiss-tiling-solver.yaml)
- [aog-a3-author](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-a3-author/SKILL.md) — Generate source-architecture reference runners and input manifests for cross-generation migration.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/aog-a3-author.yaml)
- [aog-knowledge-maintain](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-knowledge-maintain/SKILL.md) — Deduplicate runtime findings against the knowledge base and stage sourced knowledge intake.
  `CANNBot` `Ascend C` `Knowledge and cases` `Community` `Host tools` · [Metadata](catalog/skills/aog-knowledge-maintain.yaml)
- [aog-op-classify](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-op-classify/SKILL.md) — Classify source operators and emit a structured classification with relevant knowledge recommendations.
  `CANNBot` `Ascend C` `Specification and modeling` `Community` `Host tools` · [Metadata](catalog/skills/aog-op-classify.yaml)
- [aog-prior-art-verify](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-prior-art-verify/SKILL.md) — Find, provenance-stage, build, and measure existing target-architecture migration candidates.
  `CANNBot` `Ascend C` `Design and pipelines` `Community` `Host tools` · [Metadata](catalog/skills/aog-prior-art-verify.yaml)
- [api-example](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/api-example/SKILL.md) — Create a complete AscendC API example with host/kernel code, build settings, and run scripts.
  `AscendC Agent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/api-example.yaml)
- [api-gen](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/api-gen/SKILL.md) — Implement AscendC APIs from a supplied design document and verify repository changes.
  `AscendC Agent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/api-gen.yaml)
- [asc-ar-dev](https://gitcode.com/cann/asc-devkit/blob/cd10a15efc6d2221814f6167e5055c7e640ccc7c/.agent/skills/asc-ar-dev/SKILL.md) — Analyze AscendC requirements, verify API facts, implement/review code, and plan build/simulation/device validation.
  `Ascend DevKit` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/asc-ar-dev.yaml)
- [asc-npu-arch](https://gitcode.com/cann/asc-devkit/blob/cd10a15efc6d2221814f6167e5055c7e640ccc7c/.agent/skills/asc-npu-arch/SKILL.md) — Resolve DevKit chip names, architecture macros, SocVersion, dtype, and API support facts.
  `Ascend DevKit` `Ascend C` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/asc-npu-arch.yaml)
- [asc-perf-tuning](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/asc-perf-tuning/SKILL.md) — Profile, diagnose, optimize, precision-check, and compare AscendC kernels on supported architectures.
  `AscendC Agent` `Ascend C` `Profiling and optimization` `NPU execution` `Workflow` · [Metadata](catalog/skills/asc-perf-tuning.yaml)
- [asc-search](https://gitcode.com/cann/asc-devkit/blob/cd10a15efc6d2221814f6167e5055c7e640ccc7c/.agent/skills/asc-search/SKILL.md) — Build and query an index of AscendC C API documentation for requirement-driven lookup.
  `Ascend DevKit` `Ascend C` `Knowledge and cases` `Host tools` · [Metadata](catalog/skills/asc-search.yaml)
- [ascend-agent-skills-ascendc-operator-performance-optim](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/official/MindStudio/skills/ascendc-operator-performance-optim/SKILL.md) — Build and profile an AscendC operator with msprof op, change the code, and compare recollected results.
  `Ascend Agent Skills` `Ascend C` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/ascend-agent-skills-ascendc-operator-performance-optim.yaml)
- [ascend-call-generation](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/ascend-call-generation/SKILL.md) — Generate an AscendC project, host code, pybind wrapper, and kernel scaffold from functional PyTorch.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/ascend-call-generation.yaml)
- [ascend-doc-auto-updater](https://github.com/KernelHive/ascendc-skill/blob/c78f267d0423d59a51a02070e5bb845fde2dbd69/skills/ascend-doc-update/SKILL.md) — Update Ascend operator technical documents to match source and interface changes.
  `KernelHive` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascend-doc-auto-updater.yaml)
- [ascend-kernel-generator](https://github.com/KernelHive/ascendc-skill/blob/c78f267d0423d59a51a02070e5bb845fde2dbd69/skills/ascend-kernel-generator/SKILL.md) — Generate AscendC kernels, verify compilation/accuracy/performance, and save passing implementations.
  `KernelHive` `Ascend C` `Implementation and migration` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascend-kernel-generator.yaml)
- [ascend-operator-guide](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/usability/op-gen/ascend-operator-guide/SKILL.md) — Route AscendC operator families to required concepts, documentation, and optimization methods.
  `AscendC Agent` `Ascend C` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/ascend-operator-guide.yaml)
- [ascend-opplugin](https://github.com/ascend-ai-coding/awesome-ascend-skills/blob/75ec89ce9d401be8ac95980e1c3f42f8d4315057/skills/ops/ascend-opplugin/SKILL.md) — Implement and test Ascend PyTorch op-plugin bindings with matched dispatch and operator contracts.
  `Awesome Ascend Skills` `Operator support` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascend-opplugin.yaml)
- [ascend-triton-kernel-optimization](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-kernel-optimization/SKILL.md) — Optimize a correctness-passed Ascend Triton kernel with per-shape measurements and profiler evidence.
  `Ascend` `Triton` `NPU execution` · [Metadata](catalog/skills/ascend-triton-kernel-optimization.yaml)
- [ascend-triton-kernel-validation](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-kernel-validation/SKILL.md) — Validate an Ascend Triton candidate against a trusted reference with a declared case matrix and fallback gate.
  `Ascend` `Triton` `NPU execution` · [Metadata](catalog/skills/ascend-triton-kernel-validation.yaml)
- [ascend-triton-operator-development](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-operator-development/SKILL.md) — Develop the first correct Ascend Triton kernel from a PyTorch reference or a GPU Triton implementation.
  `Ascend` `Triton` `NPU execution` · [Metadata](catalog/skills/ascend-triton-operator-development.yaml)
- [ascend-triton-workflow](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-workflow/SKILL.md) — Coordinate complete Ascend Triton operator development, correctness validation and optimization with linked evidence.
  `Ascend` `Triton` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascend-triton-workflow.yaml)
- [ascendc-api-best-practices](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-api-best-practices/SKILL.md) — Look up correct AscendC arithmetic, reduction, data-copy, buffer, conversion, and communication API usage.
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/ascendc-api-best-practices.yaml)
- [ascendc-api-knowledge-query](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/ascendc-api-knowledge-query/SKILL.md) — Retrieve platform-matched AscendC API cards and follow verified source/header references.
  `CANNBot Knowledge` `Ascend C` `Knowledge and cases` `Host tools` · [Metadata](catalog/skills/ascendc-api-knowledge-query.yaml)
- [ascendc-ar-develop](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/ascendc-ar-develop/SKILL.md) — Analyze AscendC requirements, implement/review host-device code, and plan validation.
  `AscendC Agent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-ar-develop.yaml)
- [ascendc-backward-gen](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/ascendc-backward-gen/SKILL.md) — Generate an AscendC backward operator from a differentiable PyTorch forward reference and verify it on NPU.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascendc-backward-gen.yaml)
- [ascendc-blaze-best-practice](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-blaze-best-practice/SKILL.md) — Select Blaze/Tensor API templates and implement MatMul-family kernels for Ascend950 DAV_3510.
  `CANNBot` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-blaze-best-practice.yaml)
- [ascendc-blaze-migration](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-blaze-migration/SKILL.md) — Migrate an Ascend950 kernel branch to Blaze/Tensor API with frozen contracts and paired validation.
  `CANNBot` `Ascend C` `Implementation and migration` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascendc-blaze-migration.yaml)
- [ascendc-build-system](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/ascendc-build-system/SKILL.md) — Inspect and repair the AscendC host/kernel build and code-generation pipeline.
  `CANNBot` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-build-system.yaml)
- [ascendc-cross-gen-migration](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-cross-gen-migration/SKILL.md) — Migrate AscendC operators from A2/A3 to A5 with architecture adaptation and precision/performance checks.
  `CANNBot` `Ascend C` `Implementation and migration` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascendc-cross-gen-migration.yaml)
- [ascendc-cross-gen-port](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/ascendc-cross-gen-port/SKILL.md) — Port AscendC operators between declared source and target architectures with reference validation.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascendc-cross-gen-port.yaml)
- [ascendc-design-doc](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/ascendc-design-doc/SKILL.md) — Write detailed AscendC design and test plans grounded in source and API constraints.
  `AscendC Agent` `Ascend C` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/ascendc-design-doc.yaml)
- [ascendc-direct-invoke-template](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-direct-invoke-template/SKILL.md) — Select a complete Vector, Blaze MatMul, or Kirin direct-invocation project template.
  `CANNBot` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-direct-invoke-template.yaml)
- [ascendc-direct-invoke-to-registry-invoke](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-direct-invoke-to-registry-invoke/SKILL.md) — Convert an existing direct-invocation kernel into an ACLNN/GEIR registered custom operator.
  `CANNBot` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-direct-invoke-to-registry-invoke.yaml)
- [ascendc-docs-search](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-docs-search/SKILL.md) — Find AscendC API documentation, examples, and compatibility references using local indexes and online sources.
  `CANNBot` `Ascend C` `Knowledge and cases` `Host tools` · [Metadata](catalog/skills/ascendc-docs-search.yaml)
- [ascendc-evolution-knowledge](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/ascendc-evolution-knowledge/SKILL.md) — Retrieve AscendC architecture, API pitfalls, optimization patterns, and proven evolution knowledge.
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `Community` `Host tools` · [Metadata](catalog/skills/ascendc-evolution-knowledge.yaml)
- [ascendc-evolution-strategies](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/ascendc-evolution-strategies/SKILL.md) — Retrieve AscendC optimization strategies by bottleneck and operator family and check their compatibility.
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `Community` `Host tools` · [Metadata](catalog/skills/ascendc-evolution-strategies.yaml)
- [ascendc-evolution-world-model](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/ascendc-evolution-world-model/SKILL.md) — Manage an evidence-driven decision tree for selecting and validating AscendC optimization experiments.
  `CANNBot` `Ascend C` `Profiling and optimization` `Community` `NPU execution` · [Metadata](catalog/skills/ascendc-evolution-world-model.yaml)
- [ascendc-mc2-best-practice](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-mc2-best-practice/SKILL.md) — Design and debug multidevice AscendC communication-computation fusion and its memory/synchronization contracts.
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/ascendc-mc2-best-practice.yaml)
- [ascendc-operator-a5-migration](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/official/Common/ascendc-operator-A5-migration/SKILL.md) — Adapt an AscendC operator from A2/A3 to A5 through baseline, RegBase, and SIMT stages.
  `Ascend Agent Skills` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-operator-a5-migration.yaml)
- [ascendc-operator-code-gen](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-code-gen/SKILL.md) — Generate AscendC host/kernel code, register it in PyTorch, and invoke build/test steps.
  `Ascend Agent Skills` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-operator-code-gen.yaml)
- [ascendc-operator-design](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-design/SKILL.md) — Design operator interfaces, two-level tiling, UB allocation, and kernel computation.
  `Ascend Agent Skills` `Ascend C` `Design and pipelines` `Community` `Host tools` · [Metadata](catalog/skills/ascendc-operator-design.yaml)
- [ascendc-operator-dev](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-dev/SKILL.md) — Coordinate an AscendC custom operator from project setup through design, cases, code, and evaluation.
  `Ascend Agent Skills` `Ascend C` `Implementation and migration` `Community` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascendc-operator-dev.yaml)
- [ascendc-operator-develop-workflow](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/usability/op-gen/ascendc-operator-develop-workflow/SKILL.md) — Coordinate AscendC design, implementation, build/test, repair, results, and documentation.
  `AscendC Agent` `Ascend C` `Implementation and migration` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascendc-operator-develop-workflow.yaml)
- [ascendc-operator-performance-optim](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-performance-optim/SKILL.md) — Modify AscendC code from measured bottlenecks and recheck precision and baseline-relative performance.
  `Ascend Agent Skills` `Ascend C` `Profiling and optimization` `Community` `NPU execution` · [Metadata](catalog/skills/ascendc-operator-performance-optim.yaml)
- [ascendc-operator-project-init](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-project-init/SKILL.md) — Create an AscendC custom-op project with buildable scaffolds and registration checkpoints.
  `Ascend Agent Skills` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-operator-project-init.yaml)
- [ascendc-perf-optimize](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-perf-optimize/SKILL.md) — Use tiling models and profiling to balance interdevice, intercore, and intracore pipelines.
  `CANNBot` `Ascend C` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/ascendc-perf-optimize.yaml)
- [ascendc-performance-best-practices](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-performance-best-practices/SKILL.md) — Retrieve operator-family optimization methods, reference code, and platform-specific pipeline constraints.
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/ascendc-performance-best-practices.yaml)
- [ascendc-performance-optimization](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/usability/op-gen/ascendc-performance-optimization/SKILL.md) — Select tiling, double-buffering, memory, and compute optimizations from measured bottlenecks.
  `AscendC Agent` `Ascend C` `Profiling and optimization` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascendc-performance-optimization.yaml)
- [ascendc-planning](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/design-gen/SKILL.md) — Plan AscendC semantics, numerical requirements, tiling, buffering, and pipeline implementation.
  `AscendC Agent` `Ascend C` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/ascendc-planning.yaml)
- [ascendc-regbase-best-practice](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-regbase-best-practice/SKILL.md) — Look up DAV_3510 RegBase API constraints, implementation structures, and reference operators.
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/ascendc-regbase-best-practice.yaml)
- [ascendc-regbase-sample-gen](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/ascendc-regbase-sample-gen/SKILL.md) — Generate a platform-specific AscendC RegBase sample in the DevKit example structure.
  `AscendC Agent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-regbase-sample-gen.yaml)
- [ascendc-registry-invoke-template](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-registry-invoke-template/SKILL.md) — Create a registered AscendC operator project with host/kernel code and UT/ST examples.
  `CANNBot` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-registry-invoke-template.yaml)
- [ascendc-registry-invoke-to-direct-invoke](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-registry-invoke-to-direct-invoke/SKILL.md) — Extract a registered operator kernel and adapt it to direct kernel invocation.
  `CANNBot` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-registry-invoke-to-direct-invoke.yaml)
- [ascendc-simt-best-practices](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-simt-best-practices/SKILL.md) — Look up AscendC SIMT thread layouts, indexing, data movement, synchronization, and debugging APIs.
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/ascendc-simt-best-practices.yaml)
- [ascendc-simt-tiling-design](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-simt-tiling-design/SKILL.md) — Design SIMT core/thread partitioning, memory allocation, tiling keys, and workspace contracts.
  `CANNBot` `Ascend C` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/ascendc-simt-tiling-design.yaml)
- [ascendc-st-design](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-st-design/SKILL.md) — Derive constraints and generate L0/L1/L2 system-test cases from ACLNN interface specifications.
  `CANNBot` `Ascend C` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/ascendc-st-design.yaml)
- [ascendc-tiling-design](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-tiling-design/SKILL.md) — Design multicore and UB tiling, buffer allocation, and branch coverage by operator family.
  `CANNBot` `Ascend C` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/ascendc-tiling-design.yaml)
- [ascendc-translator](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/ascendc/ascendc-translator/SKILL.md) — Translate a TileLang design into an AscendC kernel and Python binding, then verify the AscendC result.
  `AscendOpGenAgent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-translator.yaml)
- [ascendc-ut-develop](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-ut-develop/SKILL.md) — Generate or extend op_host, op_api, and op_kernel unit tests and close coverage gaps.
  `CANNBot` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-ut-develop.yaml)
- [ascendc](https://github.com/ascend-ai-coding/awesome-ascend-skills/blob/75ec89ce9d401be8ac95980e1c3f42f8d4315057/skills/ops/ascendc/SKILL.md) — Coordinate design, generation, build, numerical evaluation, profiling, and optimization in an ascend-kernel project.
  `Awesome Ascend Skills` `Ascend C` `Implementation and migration` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascendc.yaml)
- [ascendkerneloptimization](https://github.com/KernelHive/ascendc-skill/blob/c78f267d0423d59a51a02070e5bb845fde2dbd69/skills/ascend-kernel-optimization/SKILL.md) — Analyze and iteratively optimize an AscendC kernel with benchmark feedback.
  `KernelHive` `Ascend C` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/ascendkerneloptimization.yaml)
- [benchmark-dev](https://github.com/Ascend/MindIE-SD/blob/d6f5ca90a882c73b25ace504ae9da254976f53c6/.agents/skills/benchmark-dev/SKILL.md) — Develop and use MindIE-SD microbenchmarks to compare real operator implementations and detect drift.
  `MindIE-SD` `Operator support` `Implementation and migration` `NPU execution` · [Metadata](catalog/skills/benchmark-dev.yaml)
- [cake-docs-search](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/cake-docs-search/SKILL.md) — Find AscendC API, example, and compatibility resources for the CAKE generation pipeline.
  `CANNBot` `Ascend C` `Knowledge and cases` `Community` `Host tools` · [Metadata](catalog/skills/cake-docs-search.yaml)
- [cake-evo](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/cake-evo/SKILL.md) — Generate isolated AscendC variants with different optimization strategies and select measured winners.
  `CANNBot` `Ascend C` `Profiling and optimization` `Community` `NPU execution` `Workflow` · [Metadata](catalog/skills/cake-evo.yaml)
- [case-simplifier](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/ascendc/case-simplifier/SKILL.md) — Select a smaller test-case set while retaining the declared operator coverage dimensions.
  `AscendOpGenAgent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/case-simplifier.yaml)
- [catlass-op-develop](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/catlass-op-develop/SKILL.md) — Generate CATLASS kernels, device invocation, parameters, and epilogues from a design and reference project.
  `CANNBot` `CATLASS` `Hardware depends on checks` · [Metadata](catalog/skills/catlass-op-develop.yaml)
- [code-performance-advisor](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/code-performance-advisor/SKILL.md) — Diagnose AscendC profiling bottlenecks using expert rules and source context.
  `CANNBot` `Ascend C` `Profiling and optimization` `Community` `Offline analysis` · [Metadata](catalog/skills/code-performance-advisor.yaml)
- [design-template](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/design-template/SKILL.md) — Render a selected ACLNN design template with the caller's verified operator facts.
  `CANNBot` `Ascend C` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/design-template.yaml)
- [dsl-baseline-generation-easyasc](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/dsl-baseline-generation-easyasc/SKILL.md) — Generate an initial easyasc DSL implementation from functional PyTorch for AscendC code generation.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/dsl-baseline-generation-easyasc.yaml)
- [dsl-baseline-generation](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/dsl-baseline-generation/SKILL.md) — Generate AscendDSL compute and tiling structures from a functional PyTorch reference.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/dsl-baseline-generation.yaml)
- [dsl-easyasc-codegen](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/dsl-easyasc-codegen/SKILL.md) — Author and simulate an easyasc operator before generating native AscendC code.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/dsl-easyasc-codegen.yaml)
- [dsl-easyasc-post](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/dsl-easyasc-post/SKILL.md) — Adapt native easyasc code-generation output to the CAKE operator project layout.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/dsl-easyasc-post.yaml)
- [dsl-lowering](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/dsl-lowering/SKILL.md) — Lower operator DSL code to AscendC through multiple passes and diagnose compilation failures.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/dsl-lowering.yaml)
- [dsl-optimization](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/dsl-optimization/SKILL.md) — Tune DSL tiling, vectorization, and pipeline structure using verified performance feedback.
  `CANNBot` `Ascend C` `Profiling and optimization` `Community` `NPU execution` · [Metadata](catalog/skills/dsl-optimization.yaml)
- [easyasc-codegen](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/easyasc-codegen/SKILL.md) — Generate and build AscendC from easyasc DSL and expose the compiled operator artifact.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/easyasc-codegen.yaml)
- [easyasc-dsl-bridge](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/easyasc-dsl-bridge/SKILL.md) — Generate torch_npu bindings and ModelNew wrappers for easyasc-generated AscendC kernels.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/easyasc-dsl-bridge.yaml)
- [example-sim-support](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/example-sim-support/SKILL.md) — Adapt an AscendC example to selectable NPU, CPU-debug, and simulator build modes.
  `AscendC Agent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/example-sim-support.yaml)
- [functional-conversion](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/functional-conversion/SKILL.md) — Convert an nn.Module reference to a stateless functional API with explicit inputs.
  `CANNBot` `Ascend C` `Specification and modeling` `Community` `Host tools` · [Metadata](catalog/skills/functional-conversion.yaml)
- [generate-case](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/generate-case/SKILL.md) — Generate executable AscendC validation assets from the testing section of a supplied design.
  `AscendC Agent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/generate-case.yaml)
- [hint-mode](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/designer/hint-mode/SKILL.md) — Define a constrained parameter/search space to guide algorithm-sketch optimization.
  `AKG` `Operator support` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/hint-mode.yaml)
- [kernel-agent-overview](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/kernel-agent/kernel-agent-overview/SKILL.md) — Explain AKG kernel-agent roles, tools, and generation/verification interaction.
  `AKG` `Operator support` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/kernel-agent-overview.yaml)
- [kernel-designer](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/triton/kernel-designer/SKILL.md) — Design an algorithm sketch and execution strategy for a Triton-Ascend task.
  `AscendOpGenAgent` `Triton` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/kernel-designer.yaml)
- [kernel-generator](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/triton/kernel-generator/SKILL.md) — Generate Triton-Ascend code from a task, sketch, architecture, and previous verification feedback.
  `AscendOpGenAgent` `Triton` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/kernel-generator.yaml)
- [kernel-splitter](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/triton/kernel-splitter/SKILL.md) — Split an operator into suitable Triton kernels with intermediate-data and execution contracts.
  `AscendOpGenAgent` `Triton` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/kernel-splitter.yaml)
- [kernel-workflow](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/kernel-workflow/SKILL.md) — Coordinate AKG task construction, sketch design, generation, verification, and iterative optimization.
  `AKG` `Operator support` `Implementation and migration` `NPU execution` `Workflow` · [Metadata](catalog/skills/kernel-workflow.yaml)
- [knowledge-ingest](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/knowledge-ingest/SKILL.md) — Convert registered documents or fixed source revisions into governed, traceable knowledge candidates.
  `CANNBot Knowledge` `Operator support` `Knowledge and cases` `Host tools` · [Metadata](catalog/skills/knowledge-ingest.yaml)
- [knowledge-lint](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/knowledge-lint/SKILL.md) — Validate knowledge structure, provenance, navigation, and lifecycle metadata.
  `CANNBot Knowledge` `Operator support` `Knowledge and cases` `Host tools` · [Metadata](catalog/skills/knowledge-lint.yaml)
- [knowledge-query](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/knowledge-query/SKILL.md) — Retrieve platform-aware knowledge cards before operator design, implementation, testing, or optimization decisions.
  `CANNBot Knowledge` `Operator support` `Knowledge and cases` `Host tools` · [Metadata](catalog/skills/knowledge-query.yaml)
- [latency-optimizer](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/triton/latency-optimizer/SKILL.md) — Iteratively optimize Triton-Ascend latency with measured feedback and numerical regression checks.
  `AscendOpGenAgent` `Triton` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/latency-optimizer.yaml)
- [merge-incompatible-samples](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/merge-incompatible-samples/SKILL.md) — Combine incompatible architecture-specific AscendC samples with explicit compile-time branches.
  `AscendC Agent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/merge-incompatible-samples.yaml)
- [model-agent-ascendc-operator-code-gen](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-code-gen/SKILL.md) — Generate AscendC host/kernel code, register it in PyTorch, and invoke build/test steps.
  `Model Agent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/model-agent-ascendc-operator-code-gen.yaml)
- [model-agent-ascendc-operator-design](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-design/SKILL.md) — Design operator interfaces, two-level tiling, UB allocation, and kernel computation.
  `Model Agent` `Ascend C` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/model-agent-ascendc-operator-design.yaml)
- [model-agent-ascendc-operator-dev](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-dev/SKILL.md) — Coordinate an AscendC custom operator from project setup through design, cases, code, and evaluation.
  `Model Agent` `Ascend C` `Implementation and migration` `NPU execution` `Workflow` · [Metadata](catalog/skills/model-agent-ascendc-operator-dev.yaml)
- [model-agent-ascendc-operator-performance-optim](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-performance-optim/SKILL.md) — Modify AscendC code from measured bottlenecks and recheck precision and baseline-relative performance.
  `Model Agent` `Ascend C` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/model-agent-ascendc-operator-performance-optim.yaml)
- [model-agent-ascendc-operator-project-init](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-project-init/SKILL.md) — Create an AscendC custom-op project with buildable scaffolds and registration checkpoints.
  `Model Agent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/model-agent-ascendc-operator-project-init.yaml)
- [model-agent-simple-vector-triton-gpu-to-npu](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/simple-vector-triton-gpu-to-npu/SKILL.md) — Port simple Vector Triton kernels from GPU to Ascend and verify the adapted implementation.
  `Model Agent` `Triton` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/model-agent-simple-vector-triton-gpu-to-npu.yaml)
- [multi-scenario-sample-pattern](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/multi-scenario-sample-pattern/SKILL.md) — Combine similar AscendC examples into a selectable multi-scenario sample.
  `AscendC Agent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/multi-scenario-sample-pattern.yaml)
- [npu-arch](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/npu-arch/SKILL.md) — Resolve chip, architecture, SocVersion, feature support, and conditional-compilation boundaries.
  `CANNBot` `Operator support` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/npu-arch.yaml)
- [npu-migration-ascend](https://github.com/KernelHive/ascendc-skill/blob/c78f267d0423d59a51a02070e5bb845fde2dbd69/skills/ascend-npu-migration/SKILL.md) — Port a source operator to AscendC with matched semantics, engineering integration, and verification.
  `KernelHive` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/npu-migration-ascend.yaml)
- [npu-op-benchmark](https://github.com/ascend-ai-coding/awesome-ascend-skills/blob/75ec89ce9d401be8ac95980e1c3f42f8d4315057/skills/ops/npu-op-benchmark/SKILL.md) — Check an existing NPU environment and benchmark an operator with declared shapes and timing conditions.
  `Awesome Ascend Skills` `Operator support` `Implementation and migration` `NPU execution` · [Metadata](catalog/skills/npu-op-benchmark.yaml)
- [op-desc-generation](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/op-desc-generation/SKILL.md) — Generate a structured operator description with shapes, dtypes, and attributes.
  `CANNBot` `Ascend C` `Specification and modeling` `Community` `Host tools` · [Metadata](catalog/skills/op-desc-generation.yaml)
- [op-task-extractor](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/triton/op-task-extractor/SKILL.md) — Extract a self-contained operator benchmark task from user requirements or source.
  `AscendOpGenAgent` `Triton` `Specification and modeling` `Host tools` · [Metadata](catalog/skills/op-task-extractor.yaml)
- [operator-dev](https://github.com/Ascend/MindIE-SD/blob/d6f5ca90a882c73b25ace504ae9da254976f53c6/.agents/skills/operator-dev/SKILL.md) — Route operator work to CANNBot and apply MindIE-SD integration, deployment, and model-validation constraints.
  `MindIE-SD` `Operator support` `Implementation and migration` `NPU execution` `Workflow` · [Metadata](catalog/skills/operator-dev.yaml)
- [ops-design-paradigms](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ops-design-paradigms/SKILL.md) — Choose broadcast, reduction, and contraction design paradigms and their resource/implementation constraints.
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/ops-design-paradigms.yaml)
- [ops-direct-invoke](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/ops-direct-invoke/SKILL.md) — Coordinate direct-invocation requirements, environment, delegated work, acceptance, and delivery.
  `CANNBot` `Ascend C` `Implementation and migration` `NPU execution` `Workflow` · [Metadata](catalog/skills/ops-direct-invoke.yaml)
- [ops-knowledge-cv-ingest](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/ops-knowledge-cv-ingest/SKILL.md) — Extract complete Cube/MIX_CV operator paths and their dataflow, resource, and synchronization contracts.
  `CANNBot Knowledge` `Operator support` `Knowledge and cases` `Host tools` · [Metadata](catalog/skills/ops-knowledge-cv-ingest.yaml)
- [ops-knowledge-trace-ingest](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/ops-knowledge-trace-ingest/SKILL.md) — Distill operator-development traces into sourced diagnostic runbooks and reusable repair patterns.
  `CANNBot Knowledge` `Operator support` `Knowledge and cases` `Host tools` · [Metadata](catalog/skills/ops-knowledge-trace-ingest.yaml)
- [ops-knowledge-vv-ingest](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/ops-knowledge-vv-ingest/SKILL.md) — Extract non-Cube operator routes and their memory, workspace, synchronization, and lifecycle contracts.
  `CANNBot Knowledge` `Operator support` `Knowledge and cases` `Host tools` · [Metadata](catalog/skills/ops-knowledge-vv-ingest.yaml)
- [ops-precision-standard](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ops-precision-standard/SKILL.md) — Choose numerical acceptance criteria and golden construction by semantics and input/output dtype.
  `CANNBot` `Operator support` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/ops-precision-standard.yaml)
- [ops-registry-invoke](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/ops-registry-invoke/SKILL.md) — Start the ACLNN registered-operator development workflow.
  `CANNBot` `Ascend C` `Implementation and migration` `NPU execution` `Workflow` · [Metadata](catalog/skills/ops-registry-invoke.yaml)
- [ops-requirement-analysis](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/ops-requirement-analysis/SKILL.md) — Research model usage, reference frameworks, and CANN capabilities to write operator requirements.
  `CANNBot` `Ascend C` `Specification and modeling` `Host tools` · [Metadata](catalog/skills/ops-requirement-analysis.yaml)
- [ops-simulator](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ops-simulator/SKILL.md) — Run host-side CANN precision/performance simulation and interpret pipeline reports.
  `CANNBot` `Operator support` `Implementation and migration` `Host tools` · [Metadata](catalog/skills/ops-simulator.yaml)
- [ops-theoretical-performance-estimation](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ops-theoretical-performance-estimation/SKILL.md) — Estimate design-time latency bounds for Ascend950 RegBase pure-Vector operators.
  `CANNBot` `Ascend C` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/ops-theoretical-performance-estimation.yaml)
- [pypto-op-develop](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/pypto-op-develop/SKILL.md) — Build PyPTO implementation modules in phases from design contracts, then consolidate the final kernel and documentation.
  `CANNBot` `PyPTO` `Hardware depends on checks` · [Metadata](catalog/skills/pypto-op-develop.yaml)
- [reference-generation](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/reference-generation/SKILL.md) — Generate a faithful PyTorch golden implementation and reproducible input constructors.
  `CANNBot` `Ascend C` `Specification and modeling` `Community` `Host tools` · [Metadata](catalog/skills/reference-generation.yaml)
- [remote-cann-development](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/remote-cann-development/SKILL.md) — Synchronize, execute, and test an operator project on declared remote NPU backends.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/remote-cann-development.yaml)
- [repo-build-guide](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-build-guide/SKILL.md) — Build direct-invocation operators and CANN Bench packages and verify loaded artifact identity.
  `CANNBot` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/repo-build-guide.yaml)
- [repo-coding-rules](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-coding-rules/SKILL.md) — Apply CANN Bench authenticity, wrapper, interface, and AscendC code-quality rules.
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/repo-coding-rules.yaml)
- [repo-knowledge](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-knowledge/SKILL.md) — Look up CANN Bench submission, task, numerical, and scoring contracts.
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/repo-knowledge.yaml)
- [repo-op-templates](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-op-templates/SKILL.md) — Create direct-invocation code from the CANN Bench reference project and operator templates.
  `CANNBot` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/repo-op-templates.yaml)
- [repo-requirement](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-requirement/SKILL.md) — Record confirmed operator requirements, environment choices, and modification scope across retries.
  `CANNBot` `Ascend C` `Specification and modeling` `Host tools` · [Metadata](catalog/skills/repo-requirement.yaml)
- [simple-vector-triton-gpu-to-npu](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/simple-vector-triton-gpu-to-npu/SKILL.md) — Port simple Vector Triton kernels from GPU to Ascend and verify the adapted implementation.
  `Ascend Agent Skills` `Triton` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/simple-vector-triton-gpu-to-npu.yaml)
- [simt-requirement-doc](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/simt-requirement-doc/SKILL.md) — Clarify a SIMT requirement and draft its implementation and acceptance specification.
  `AscendC Agent` `Ascend C` `Specification and modeling` `Host tools` · [Metadata](catalog/skills/simt-requirement-doc.yaml)
- [sketch-design](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/designer/sketch-design/SKILL.md) — Describe hardware-aware algorithm sketches and optimization decisions for kernel generation.
  `AKG` `Operator support` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/sketch-design.yaml)
- [skill-trace](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/skill-trace/SKILL.md) — Record skill inputs, durations, and outcomes during operator generation.
  `CANNBot` `Ascend C` `Knowledge and cases` `Community` `Host tools` · [Metadata](catalog/skills/skill-trace.yaml)
- [task-constructor](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/task-constructor/SKILL.md) — Build a self-contained kernel-generation task with a reference and reproducible input functions.
  `AKG` `Operator support` `Specification and modeling` `Host tools` · [Metadata](catalog/skills/task-constructor.yaml)
- [tilelang-designer](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/ascendc/tilelang-designer/SKILL.md) — Express an operator at block and tile levels as the design input for AscendC generation.
  `AscendOpGenAgent` `Ascend C` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/tilelang-designer.yaml)
- [tilelang-op-develop](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/tilelang-op-develop/SKILL.md) — Use device evidence to route TileLang implementation and accuracy validation to the Ascend910 or Ascend950 workflow.
  `CANNBot` `TileLang` `NPU execution` · [Metadata](catalog/skills/tilelang-op-develop.yaml)
- [tilelang2ascend-case-simplifier](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/tilelang2ascend-case-simplifier/SKILL.md) — Reduce an operator case set while preserving its declared coverage dimensions.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/tilelang2ascend-case-simplifier.yaml)
- [tilelang2ascend-operator-project-init](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/tilelang2ascend-operator-project-init/SKILL.md) — Create an AscendC operator scaffold with buildable files and a development checklist.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/tilelang2ascend-operator-project-init.yaml)
- [tilelang2ascend-tilelang-designer](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/tilelang2ascend-tilelang-designer/SKILL.md) — Coordinate block- and tile-level design to prepare a TileLang description for AscendC translation.
  `CANNBot` `Ascend C` `Design and pipelines` `Community` `Host tools` · [Metadata](catalog/skills/tilelang2ascend-tilelang-designer.yaml)
- [tilelang2ascend-trace-recorder](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/tilelang2ascend-trace-recorder/SKILL.md) — Record an operator-development trace and extract sourced runbooks for later retrieval.
  `CANNBot` `Ascend C` `Knowledge and cases` `Community` `Host tools` · [Metadata](catalog/skills/tilelang2ascend-trace-recorder.yaml)
- [tilelang2ascend-translator](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/tilelang2ascend-translator/SKILL.md) — Translate a TileLang design into an AscendC kernel and its Python invocation wrapper.
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `Hardware depends on checks` · [Metadata](catalog/skills/tilelang2ascend-translator.yaml)
- [torch-ascendc-op-extension](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/torch-ascendc-op-extension/SKILL.md) — Wrap an existing AscendC operator for PyTorch using registered custom-op interfaces.
  `CANNBot` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/torch-ascendc-op-extension.yaml)
- [torch-custom-ops-guide](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/graph/torch-custom-ops-guide/SKILL.md) — Register Python custom operators, supply Meta behavior, and adapt them to npugraph_ex.
  `CANNBot` `Operator support` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/torch-custom-ops-guide.yaml)
- [tpipe-to-static-tensor](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/tpipe-to-static-tensor/SKILL.md) — Migrate TPipe/TQue-based AscendC examples to static Tensor programming.
  `AscendC Agent` `Ascend C` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/tpipe-to-static-tensor.yaml)
- [trace-recorder](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/ascendc/trace-recorder/SKILL.md) — Record implementation, verification, and optimization decisions in an operator execution trace.
  `AscendOpGenAgent` `Ascend C` `Knowledge and cases` `Host tools` · [Metadata](catalog/skills/trace-recorder.yaml)
- [triton-agent-loop](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/triton-auto-evolve/skills/triton-agent-loop/SKILL.md) — Coordinate independent Triton optimization rounds and retain per-round artifacts and evaluation results.
  `CANNBot` `Triton` `Profiling and optimization` `Community` `NPU execution` `Workflow` · [Metadata](catalog/skills/triton-agent-loop.yaml)
- [triton-ascend-api-rules](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-api-rules/SKILL.md) — Look up Triton-Ascend guidance on backend API and syntax restrictions for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-api-rules.yaml)
- [triton-ascend-ascend-hardware-constraints](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-ascend-hardware-constraints/SKILL.md) — Look up Triton-Ascend guidance on on-chip memory budgets and compiler constraints for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-ascend-hardware-constraints.yaml)
- [triton-ascend-attention](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/guides/triton-ascend-attention/SKILL.md) — Look up Triton-Ascend guidance on attention tiling, online softmax, and masking for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-attention.yaml)
- [triton-ascend-basics](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-basics/SKILL.md) — Look up Triton-Ascend guidance on program IDs, grids, kernel structure, and launch syntax for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-basics.yaml)
- [triton-ascend-case-elemwise-broadcast-2d](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-elemwise-broadcast-2d/SKILL.md) — Consult a Triton-Ascend optimization case for 2D broadcast, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-elemwise-broadcast-2d.yaml)
- [triton-ascend-case-elemwise-broadcast-3d](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-elemwise-broadcast-3d/SKILL.md) — Consult a Triton-Ascend optimization case for 3D broadcast, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-elemwise-broadcast-3d.yaml)
- [triton-ascend-case-elemwise-cast](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-elemwise-cast/SKILL.md) — Consult a Triton-Ascend optimization case for dtype conversion, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-elemwise-cast.yaml)
- [triton-ascend-case-elemwise-concat](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-elemwise-concat/SKILL.md) — Consult a Triton-Ascend optimization case for concatenation, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-elemwise-concat.yaml)
- [triton-ascend-case-elemwise-zeros](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-elemwise-zeros/SKILL.md) — Consult a Triton-Ascend optimization case for zero initialization, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-elemwise-zeros.yaml)
- [triton-ascend-case-index-histogram](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-index-histogram/SKILL.md) — Consult a Triton-Ascend optimization case for histogram indexing, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-index-histogram.yaml)
- [triton-ascend-case-index-put](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-index-put/SKILL.md) — Consult a Triton-Ascend optimization case for indexed updates, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-index-put.yaml)
- [triton-ascend-case-matmul-large-k](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-matmul-large-k/SKILL.md) — Consult a Triton-Ascend optimization case for large-K matrix multiplication, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-matmul-large-k.yaml)
- [triton-ascend-case-matmul-swizzle2d](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-matmul-swizzle2d/SKILL.md) — Consult a Triton-Ascend optimization case for matrix-multiplication swizzling, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-matmul-swizzle2d.yaml)
- [triton-ascend-case-reduction-amax-large](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amax-large/SKILL.md) — Consult a Triton-Ascend optimization case for large amax reductions, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-amax-large.yaml)
- [triton-ascend-case-reduction-amax-medium](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amax-medium/SKILL.md) — Consult a Triton-Ascend optimization case for medium amax reductions, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-amax-medium.yaml)
- [triton-ascend-case-reduction-amax-small](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amax-small/SKILL.md) — Consult a Triton-Ascend optimization case for small amax reductions, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-amax-small.yaml)
- [triton-ascend-case-reduction-amin-atomic](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amin-atomic/SKILL.md) — Consult a Triton-Ascend optimization case for atomic amin reductions, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-amin-atomic.yaml)
- [triton-ascend-case-reduction-amin-large](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amin-large/SKILL.md) — Consult a Triton-Ascend optimization case for large amin reductions, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-amin-large.yaml)
- [triton-ascend-case-reduction-amin-medium](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amin-medium/SKILL.md) — Consult a Triton-Ascend optimization case for medium amin reductions, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-amin-medium.yaml)
- [triton-ascend-case-reduction-amin-small](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amin-small/SKILL.md) — Consult a Triton-Ascend optimization case for small amin reductions, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-amin-small.yaml)
- [triton-ascend-case-reduction-mean-large](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-mean-large/SKILL.md) — Consult a Triton-Ascend optimization case for large mean reductions, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-mean-large.yaml)
- [triton-ascend-case-reduction-mean-medium](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-mean-medium/SKILL.md) — Consult a Triton-Ascend optimization case for medium mean reductions, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-mean-medium.yaml)
- [triton-ascend-case-reduction-prod-small](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-prod-small/SKILL.md) — Consult a Triton-Ascend optimization case for small product reductions, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-prod-small.yaml)
- [triton-ascend-case-reduction-sum-fused](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-sum-fused/SKILL.md) — Consult a Triton-Ascend optimization case for fused elementwise/sum, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-sum-fused.yaml)
- [triton-ascend-case-reduction-sum-large](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-sum-large/SKILL.md) — Consult a Triton-Ascend optimization case for large sum reductions, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-sum-large.yaml)
- [triton-ascend-case-reduction-weighted-swiglu](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-weighted-swiglu/SKILL.md) — Consult a Triton-Ascend optimization case for weighted SwiGLU backward, including its scoped design and measurement observations.
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `Host tools` · [Metadata](catalog/skills/triton-ascend-case-reduction-weighted-swiglu.yaml)
- [triton-ascend-debugging](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-debugging/SKILL.md) — Look up Triton-Ascend guidance on compile, runtime, numerical, and performance diagnosis for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-debugging.yaml)
- [triton-ascend-elementwise-reduce-fused](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/guides/triton-ascend-elementwise-reduce-fused/SKILL.md) — Look up Triton-Ascend guidance on elementwise-plus-global-reduction kernels for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-elementwise-reduce-fused.yaml)
- [triton-ascend-elementwise](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/guides/triton-ascend-elementwise/SKILL.md) — Look up Triton-Ascend guidance on elementwise kernels for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-elementwise.yaml)
- [triton-ascend-error-fix](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/evolved-fix/triton-ascend-error-fix/SKILL.md) — Look up Triton-Ascend guidance on compiler, indexing, memory, and numerical failures for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-error-fix.yaml)
- [triton-ascend-example-double-kernel](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/examples/triton-ascend-example-double-kernel/SKILL.md) — Use the Triton-Ascend implementation example for staged two-kernel execution as a code-structure reference.
  `AKG` `Triton` `Knowledge and cases` `Implementation example` `Host tools` · [Metadata](catalog/skills/triton-ascend-example-double-kernel.yaml)
- [triton-ascend-example-layernorm](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/examples/triton-ascend-example-layernorm/SKILL.md) — Use the Triton-Ascend implementation example for LayerNorm as a code-structure reference.
  `AKG` `Triton` `Knowledge and cases` `Implementation example` `Host tools` · [Metadata](catalog/skills/triton-ascend-example-layernorm.yaml)
- [triton-ascend-example-matmul](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/examples/triton-ascend-example-matmul/SKILL.md) — Use the Triton-Ascend implementation example for matrix multiplication as a code-structure reference.
  `AKG` `Triton` `Knowledge and cases` `Implementation example` `Host tools` · [Metadata](catalog/skills/triton-ascend-example-matmul.yaml)
- [triton-ascend-example-relu](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/examples/triton-ascend-example-relu/SKILL.md) — Use the Triton-Ascend implementation example for ReLU as a code-structure reference.
  `AKG` `Triton` `Knowledge and cases` `Implementation example` `Host tools` · [Metadata](catalog/skills/triton-ascend-example-relu.yaml)
- [triton-ascend-example-softmax](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/examples/triton-ascend-example-softmax/SKILL.md) — Use the Triton-Ascend implementation example for Softmax as a code-structure reference.
  `AKG` `Triton` `Knowledge and cases` `Implementation example` `Host tools` · [Metadata](catalog/skills/triton-ascend-example-softmax.yaml)
- [triton-ascend-examples-mindspore](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/examples/triton-ascend-examples-mindspore/SKILL.md) — Use the Triton-Ascend implementation example for MindSpore integration as a code-structure reference.
  `AKG` `Triton` `Knowledge and cases` `Implementation example` `Host tools` · [Metadata](catalog/skills/triton-ascend-examples-mindspore.yaml)
- [triton-ascend-fused-operator-optimization](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/evolved-improvement/triton-ascend-fused-operator-optimization/SKILL.md) — Look up Triton-Ascend guidance on fusion ceilings, pass merging, and data-access reconstruction for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-fused-operator-optimization.yaml)
- [triton-ascend-grid-config](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-grid-config/SKILL.md) — Look up Triton-Ascend guidance on core allocation, grid/block choices, and secondary tiling for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-grid-config.yaml)
- [triton-ascend-matmul](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/guides/triton-ascend-matmul/SKILL.md) — Look up Triton-Ascend guidance on matrix-multiplication kernels for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-matmul.yaml)
- [triton-ascend-memory](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-memory/SKILL.md) — Look up Triton-Ascend guidance on UB use, layouts, coalesced access, and prefetch for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-memory.yaml)
- [triton-ascend-migration](https://github.com/ascend-ai-coding/awesome-ascend-skills/blob/75ec89ce9d401be8ac95980e1c3f42f8d4315057/skills/ops/triton-ascend-migration/SKILL.md) — Port GPU Triton or PyTorch semantics to Triton-Ascend and produce a minimal device validation script.
  `Awesome Ascend Skills` `Triton` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/triton-ascend-migration.yaml)
- [triton-ascend-optimization](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-optimization/SKILL.md) — Look up Triton-Ascend guidance on tiling, grid selection, alignment, and backend optimization for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-optimization.yaml)
- [triton-ascend-performance-improvement](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/evolved-improvement/triton-ascend-performance-improvement/SKILL.md) — Look up Triton-Ascend guidance on measured tile, load, reduction, and pass optimization patterns for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-performance-improvement.yaml)
- [triton-ascend-reduce](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/guides/triton-ascend-reduce/SKILL.md) — Look up Triton-Ascend guidance on reduction and normalization kernels for the documented platform and compiler scope.
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `Host tools` · [Metadata](catalog/skills/triton-ascend-reduce.yaml)
- [triton-ascendc-fused-op-generator](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/training-optimization/operator-fusion/triton-ascendc-fused-op-generator/SKILL.md) — Identify fusion candidates, estimate GM traffic savings, and generate a Triton/AscendC implementation plan.
  `Model Agent` `Operator support` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/triton-ascendc-fused-op-generator.yaml)
- [triton-latency-optimizer](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-latency-optimizer/SKILL.md) — Optimize Triton-Ascend kernels one change at a time with paired correctness and latency checks.
  `CANNBot` `Triton` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/triton-latency-optimizer.yaml)
- [triton-op-coding](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-op-coding/SKILL.md) — Generate pure Triton-Ascend kernels from a task and sketch and repair them using verifier feedback.
  `CANNBot` `Triton` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/triton-op-coding.yaml)
- [triton-op-designer](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-op-designer/SKILL.md) — Design an architecture-aware algorithm sketch from an operator specification and historical feedback.
  `CANNBot` `Triton` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/triton-op-designer.yaml)
- [triton-operator-code-gen](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-code-gen/SKILL.md) — Generate an Ascend Triton kernel and smoke test from a design or functional requirement.
  `Model Agent` `Triton` `Implementation and migration` `Hardware depends on checks` · [Metadata](catalog/skills/triton-operator-code-gen.yaml)
- [triton-operator-design](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-design/SKILL.md) — Specify Triton operator semantics, interface, tiling, and kernel implementation strategy.
  `Model Agent` `Triton` `Design and pipelines` `Host tools` · [Metadata](catalog/skills/triton-operator-design.yaml)
- [triton-operator-dev](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-dev/SKILL.md) — Coordinate Triton environment, design, coding, review, numerical validation, and performance iteration.
  `Model Agent` `Triton` `Implementation and migration` `NPU execution` `Workflow` · [Metadata](catalog/skills/triton-operator-dev.yaml)
- [triton-operator-performance-optim](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-performance-optim/SKILL.md) — Tune Triton-Ascend tiling and memory use while rechecking correctness and performance.
  `Model Agent` `Triton` `Profiling and optimization` `NPU execution` · [Metadata](catalog/skills/triton-operator-performance-optim.yaml)
- [triton-task-extractor](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-task-extractor/SKILL.md) — Construct a self-contained operator task and case inputs from user code or requirements.
  `CANNBot` `Triton` `Specification and modeling` `Host tools` · [Metadata](catalog/skills/triton-task-extractor.yaml)
- [vector-triton-ascend-ops-optimizer](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/vector-triton-ascend-ops-optimizer/SKILL.md) — Optimize Vector Triton kernels using UB budgeting, batching, pipelines, and measured comparisons.
  `Ascend Agent Skills` `Triton` `Profiling and optimization` `Community` `NPU execution` · [Metadata](catalog/skills/vector-triton-ascend-ops-optimizer.yaml)
- [vllm-mrv2-kernel-workflow](https://github.com/Liamup777/vllm-mrv2-kernel-tools/blob/ed71b1b56994e419998e4cd85f5ace013f92447d/skills/vllm-mrv2-kernel-workflow/SKILL.md) — Review new MRV2 Triton kernels between vLLM tags or commits, generate source-grounded cases, and optionally verify sources and execute and measure them on Ascend.
  `vLLM Ascend` `Triton` `MRV2` `Hardware depends on checks` `Workflow` `Reproduction recorded` · [Metadata](catalog/skills/vllm-mrv2-kernel-workflow.yaml) · [Validation record](evidence/vllm-mrv2-execution-2026-10-21.md)
- [workflow-bootstrap](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/workflow-bootstrap/SKILL.md) — Detect the target architecture and select the matching registered-operator workflow.
  `CANNBot` `Ascend C` `Implementation and migration` `NPU execution` `Workflow` · [Metadata](catalog/skills/workflow-bootstrap.yaml)

<a id="debugging"></a>

### Debugging

Reduce startup, communication, graph, and operator failures and verify fixes.

- [ascend-operator-debug](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-operator-debug/SKILL.md) — Reduce an Ascend model symptom to one operator call and validate its dtype, shape, layout and execution modes.
  `Ascend` `NPU execution` · [Metadata](catalog/skills/ascend-operator-debug.yaml)
- [ascendc-crash-debug](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-crash-debug/SKILL.md) — Diagnose AscendC hangs, crashes, memory errors, and buffer or synchronization failures.
  `CANNBot` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/ascendc-crash-debug.yaml)
- [ascendc-debugging](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/usability/op-gen/ascendc-debugging/SKILL.md) — Diagnose compile/runtime/numerical failures and verify small, typical, and boundary cases.
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/ascendc-debugging.yaml)
- [ascendc-mssanitizer](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-mssanitizer/SKILL.md) — Run and interpret mssanitizer checks for illegal memory accesses, leaks, and UB bounds.
  `Ascend Agent Skills` `Ascend C` `Testing and numerical validation` `Community` `NPU execution` · [Metadata](catalog/skills/ascendc-mssanitizer.yaml)
- [ascendc-op-debug](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/ascendc-op-debug/SKILL.md) — Use a hypothesis-driven procedure to diagnose numerical errors, crashes, hangs, and multicore inconsistency.
  `CANNBot` `Ascend C` `Testing and numerical validation` `Community` `NPU execution` · [Metadata](catalog/skills/ascendc-op-debug.yaml)
- [ascendc-operator-compile-debug](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-compile-debug/SKILL.md) — Build an AscendC extension, install its package, run precision tests, and repair failures.
  `Ascend Agent Skills` `Ascend C` `Testing and numerical validation` `Community` `NPU execution` · [Metadata](catalog/skills/ascendc-operator-compile-debug.yaml)
- [ascendc-operator-precision-debug](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-precision-debug/SKILL.md) — Analyze numerical error patterns, isolate the faulty computation, and validate targeted AscendC repairs.
  `Ascend Agent Skills` `Ascend C` `Testing and numerical validation` `Community` `NPU execution` · [Metadata](catalog/skills/ascendc-operator-precision-debug.yaml)
- [ascendc-precision-debug](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-precision-debug/SKILL.md) — Reduce numerical failures to a reproducible operator case, locate the cause, and verify the repair.
  `CANNBot` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/ascendc-precision-debug.yaml)
- [ascendc-runtime-debug](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-runtime-debug/SKILL.md) — Interpret AscendC runtime error codes and plog evidence to locate invocation and tiling failures.
  `CANNBot` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/ascendc-runtime-debug.yaml)
- [asys-toolkit](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/tools/asys-toolkit/SKILL.md) — Use asys in Ascend EP environments to collect failure information, inspect device health, and parse diagnostic artifacts.
  `CANNBot` `CANN` `asys` `Hardware depends on checks` · [Metadata](catalog/skills/asys-toolkit.yaml)
- [blue-npu-fabric](https://github.com/xuchi-0808/blue-server-toolkit/blob/5707a86922713f830f1f5fea2bedbb0a0a1cdc3a/skills/blue-npu-fabric/SKILL.md) — Diagnose cross-machine NPU data-plane and fabric identity — hccs_ping RoCE checks and false positives, firewalld host-TCP blocking, 950DT (A5) rootinfo, ub_endpoint, and urma_admin, plus EID drift; routed by EI error codes.
  `Ascend` `RoCE` `NPU execution` · [Metadata](catalog/skills/blue-npu-fabric.yaml)
- [debugging-vllm-ascend-pd-accuracy](https://github.com/Yuli-yx/awesome-va-skills/blob/8d9f7ee56d088f15a398181590c4512bfc725d6f/.agents/skills/debugging-vllm-ascend-pd-accuracy/SKILL.md) — Diagnose PD repetition and accuracy divergence using P/D/proxy comparisons, single-variable experiments, KV fingerprints and first-divergence evidence.
  `vLLM Ascend` `PD` `KV transfer` `Accuracy` `NPU execution` `Workflow` · [Metadata](catalog/skills/debugging-vllm-ascend-pd-accuracy.yaml)
- [driver-peermem-check](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/driver-peermem-check/SKILL.md) — 分析 Ascend 驱动 .run 包中是否包含 npu_peermem.ko 及相关源码。适用于：
- 判断某个驱动版本是否支持 d2d/d2rd RDMA 传输
- 对比不同平台的驱动包内容差异
- 检查 npu_peermem 模块的构建依赖是否就绪
- 用户提到驱动包、npu_peermem、d2d RDMA 失败、peer memory 等问题时
.
  `Ascend` `HIXL` `Offline analysis` `Workflow` · [Metadata](catalog/skills/driver-peermem-check.yaml)
- [ge-dynamic-shape-diagnose](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/graph/ge-dynamic-shape-diagnose/SKILL.md) — Identify unknown-graph and dynamic-shape scheduling triggers from GE compiler logs.
  `CANNBot` `GE` `Offline analysis` · [Metadata](catalog/skills/ge-dynamic-shape-diagnose.yaml)
- [gm-align-debug](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/gm-align-debug/SKILL.md) — Reproduce GM/UB copy alignment and byte-reinterpretation failures using memory dumps.
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/gm-align-debug.yaml)
- [hixl-troubleshoot](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/hixl-troubleshoot/SKILL.md) — 在 Ascend 上定位 HIXL/ADXL/HIXL_CS 建链、传输问题。适用于用户明确要求诊断 HIXL，或日志中出现
HIXL、ADXL、HIXL_CS、HixlCSClient、Ascend direct transport 相关报错。
.
  `Ascend` `HIXL` `NPU execution` `Workflow` · [Metadata](catalog/skills/hixl-troubleshoot.yaml)
- [model-agent-ascendc-operator-compile-debug](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-compile-debug/SKILL.md) — Build an AscendC extension, install its package, run precision tests, and repair failures.
  `Model Agent` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/model-agent-ascendc-operator-compile-debug.yaml)
- [model-agent-ascendc-operator-precision-debug](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-precision-debug/SKILL.md) — Analyze numerical error patterns, isolate the faulty computation, and validate targeted AscendC repairs.
  `Model Agent` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/model-agent-ascendc-operator-precision-debug.yaml)
- [model-infer-precision-debug](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-precision-debug/SKILL.md) — Diagnose KVCache and FlashAttention prefill/decode accuracy differences, cache updates, and mapping errors.
  `CANNBot` `PyTorch` `KV cache` `NPU execution` · [Metadata](catalog/skills/model-infer-precision-debug.yaml)
- [model-infer-runtime-debug](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-runtime-debug/SKILL.md) — Narrow model loading and inference failures to diagnose HCCL errors, OOM, timeouts, and hangs, then verify fixes.
  `CANNBot` `PyTorch` `HCCL` `NPU execution` · [Metadata](catalog/skills/model-infer-runtime-debug.yaml)
- [msaicerr-toolkit](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/tools/msaicerr-toolkit/SKILL.md) — Use msaicerr in the originating runtime environment to analyze AI Core errors, parse dumps, and check environment constraints.
  `CANNBot` `CANN` `msaicerr` `Hardware depends on checks` · [Metadata](catalog/skills/msaicerr-toolkit.yaml)
- [msnpureport-toolkit](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/tools/msnpureport-toolkit/SKILL.md) — Export device logs and query or set diagnostic configuration with the required permissions in supported Ascend EP environments.
  `CANNBot` `CANN` `msnpureport` `NPU execution` · [Metadata](catalog/skills/msnpureport-toolkit.yaml)
- [pd-disaggregation-accuracy-debug](https://github.com/nwpu-zxr/vllm-ascend-pd-disaggregation-skills/blob/2852c18ac977783f336f8c8864ca84dfee3f5cc6/skills/pd-disaggregation-accuracy-debug/SKILL.md) — Diagnose PD accuracy top-down or bottom-up, aligning completed P KV/state with D contents and placement before first consumption to establish the cause.
  `vLLM` `vLLM Ascend` `PD` `KV Cache` `Hardware depends on checks` `Workflow` · [Metadata](catalog/skills/pd-disaggregation-accuracy-debug.yaml)
- [torch-npugraph-ex-dfx-triage](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/graph/torch-npugraph-ex-dfx-triage/SKILL.md) — Collect layered logs and route npugraph_ex issues to compilation, runtime, accuracy, or performance diagnosis.
  `CANNBot` `PyTorch` `npugraph_ex` `Hardware depends on checks` `Workflow` · [Metadata](catalog/skills/torch-npugraph-ex-dfx-triage.yaml)
- [triton-precision-debug](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-precision-debug/SKILL.md) — Diagnose Triton-Ascend numerical failures and validate a targeted repair.
  `CANNBot` `Triton` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/triton-precision-debug.yaml)
- [ub-boundary-check](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/ub-boundary-check/SKILL.md) — Reproduce UB boundary, vector-load/store, mask, and data-copy memory failures.
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `NPU execution` · [Metadata](catalog/skills/ub-boundary-check.yaml)
- [vllm-ascend-distributed-debug](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-distributed-debug/SKILL.md) — Diagnose Ascend multi-rank startup, collective, endpoint and hang failures using explicit topology and per-rank evidence.
  `vLLM Ascend` `HCCL` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-distributed-debug.yaml)
- [vllm-ascend-graph-debug](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-graph-debug/SKILL.md) — Localize Ascend graph capture, replay or eager/graph divergence with controlled experiments and intermediate snapshots.
  `vLLM Ascend` `Graph` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-graph-debug.yaml)

<a id="delivery"></a>

### Delivery and operations

Map changes to build, correctness, and performance checks and record coverage.

- [analyze-upstream-downstream](https://github.com/SOMEONEUNSEEN/awesome-mindie-skills/blob/614d7c22c05f147d96e09044aa1b8e62cc9ec89e/skills/analyze-upstream-downstream/SKILL.md) — Trace actual calls and replacement boundaries between an upstream framework and its downstream adaptation, distinguish inherited behavior, synchronized changes and migration gaps, and produce sanitized evidence with a minimal migration plan.
  `Framework plugins` `Platform adaptations` `Host tools` `Workflow` · [Metadata](catalog/skills/analyze-upstream-downstream.yaml)
- [aog-report-gen](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-report-gen/SKILL.md) — Generate a project report for cross-generation migration or backward-operator generation.
  `CANNBot` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/aog-report-gen.yaml)
- [aog-self-critic](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-self-critic/SKILL.md) — Audit the current operator-development session for recurring process failures and corrective actions.
  `CANNBot` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/aog-self-critic.yaml)
- [asc-devkit-review](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/code-review/asc-devkit-review/SKILL.md) — Review Ascend DevKit pull requests and produce source-grounded findings.
  `AscendC Agent` `Ascend C` `Review and delivery` `Host tools` · [Metadata](catalog/skills/asc-devkit-review.yaml)
- [asc-testcase-doc-gen](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/asc-testcase-doc-gen/SKILL.md) — Turn a supplied requirement document into a structured test-case document.
  `AscendC Agent` `Operator support` `Review and delivery` `Host tools` · [Metadata](catalog/skills/asc-testcase-doc-gen.yaml)
- [ascendc-code-review](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-code-review/SKILL.md) — Review AscendC source or PRs for applicable rules and design consistency using testable hypotheses.
  `CANNBot` `Ascend C` `Review and delivery` `Host tools` · [Metadata](catalog/skills/ascendc-code-review.yaml)
- [ascendc-docs-gen](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-docs-gen/SKILL.md) — Write operator requirements, detailed design, API documentation, and README files from standard templates.
  `CANNBot` `Ascend C` `Review and delivery` `Host tools` · [Metadata](catalog/skills/ascendc-docs-gen.yaml)
- [ascendc-evolution-report](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/ascendc-evolution-report/SKILL.md) — Generate and self-check an HTML report of evolution variants, performance, decisions, and resource use.
  `CANNBot` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/ascendc-evolution-report.yaml)
- [ascendc-op-doc-generator](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-op-doc-generator/SKILL.md) — Extract source contracts to generate ACLNN API documentation and an operator README.
  `Ascend Agent Skills` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/ascendc-op-doc-generator.yaml)
- [ascendc-op-doc-incremental](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-op-doc-incremental/SKILL.md) — Compare source changes with operator documents and produce incremental updates.
  `Ascend Agent Skills` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/ascendc-op-doc-incremental.yaml)
- [ascendc-operator-code-review](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-code-review/SKILL.md) — Review AscendC source for correctness and engineering-rule violations.
  `Ascend Agent Skills` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/ascendc-operator-code-review.yaml)
- [ascendc-operator-doc-gen](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-doc-gen/SKILL.md) — Generate PyTorch-style operator interface documentation from implemented source.
  `Ascend Agent Skills` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/ascendc-operator-doc-gen.yaml)
- [ascendc-operator-doc-writer](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-doc-writer/SKILL.md) — Write operator technical documentation from local source and an existing template.
  `Ascend Agent Skills` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/ascendc-operator-doc-writer.yaml)
- [ascendc-sync-audit](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-sync-audit/SKILL.md) — Audit pipeline and intercore signals and producer/consumer buffer consistency, then propose repairs.
  `CANNBot` `Ascend C` `Review and delivery` `Host tools` · [Metadata](catalog/skills/ascendc-sync-audit.yaml)
- [blue-npu-ops](https://github.com/xuchi-0808/blue-server-toolkit/blob/5707a86922713f830f1f5fea2bedbb0a0a1cdc3a/skills/blue-npu-ops/SKILL.md) — Operate a single NPU server — npu-smi status reading, HBM usage and orphan release, precise-PID cleanup of leftover processes, idle checks, A3 chip numbering and device visibility mapping, and torch-based FLOPS measurement.
  `Ascend` `HBM` `NPU execution` · [Metadata](catalog/skills/blue-npu-ops.yaml)
- [blue-server-toolkit](https://github.com/xuchi-0808/blue-server-toolkit/blob/5707a86922713f830f1f5fea2bedbb0a0a1cdc3a/skills/blue-server-toolkit/SKILL.md) — Perform high-frequency daily operations on remote Ascend NPU development servers — SSH connection checks and stability (persistent ControlMaster multiplexing), code sync, UT execution, model and image download, log viewing, container management, and file transfer; also the routing hub when unsure which sibling skill fits.
  `Ascend` `Docker` `SSH` `Host tools` · [Metadata](catalog/skills/blue-server-toolkit.yaml)
- [cake-code-review](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/cake-code-review/SKILL.md) — Review generated AscendC structure and algorithm correctness before evaluation.
  `CANNBot` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/cake-code-review.yaml)
- [cake-review](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/cake-review/SKILL.md) — Review the complete kernel-generation trace and record process and implementation improvements.
  `CANNBot` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/cake-review.yaml)
- [cann-review](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/code-review/cann-review/SKILL.md) — Review exact GitCode PR revisions and cross-repository contracts with counterexample checks.
  `AscendC Agent` `Operator support` `Review and delivery` `Host tools` · [Metadata](catalog/skills/cann-review.yaml)
- [cmake-race-auditor](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/cmake_auditor/SKILL.md) — Find generated-file dependency gaps and parallel build races in CMake projects.
  `AscendC Agent` `Operator support` `Review and delivery` `Host tools` · [Metadata](catalog/skills/cmake-race-auditor.yaml)
- [examples-docs-validator](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/examples-docs-validator/SKILL.md) — Check example README/comment rules and consistency between documentation and source.
  `AscendC Agent` `Ascend C` `Review and delivery` `Host tools` · [Metadata](catalog/skills/examples-docs-validator.yaml)
- [git-version-management](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/git-version-management/SKILL.md) — Isolate operator variants with Git worktrees and record stage commits and provenance.
  `CANNBot` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/git-version-management.yaml)
- [hixl-pr-review](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/hixl-pr-review/SKILL.md) — HIXL 代码检视技能。用于检视 GitCode 上的 HIXL 项目 PR，当用户要求检视PR，审查PR时调用此skill。
自动分析代码变更，检查内存泄漏、安全漏洞和可读性，生成结构化报告并发布评论。
.
  `Ascend` `HIXL` `Offline analysis` `Workflow` · [Metadata](catalog/skills/hixl-pr-review.yaml)
- [hixl-srs-doc-generator](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/hixl-srs-doc-generator/SKILL.md) — 当用户要求为 HIXL 或 ADXL 功能生成、扩展或评审 SRS/需求设计文档时使用，特别涉及 src/hixl 或 src/llm_datadist/adxl 目录下的变更。
触发关键词包括 SRS、设计文档、需求描述、功能要点、技术方案、相关文档、测试方案，或将简短需求转化为完整设计文档的请求。
.
  `Ascend` `HIXL` `Offline analysis` `Workflow` · [Metadata](catalog/skills/hixl-srs-doc-generator.yaml)
- [hixl-ut-generator](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/hixl-ut-generator/SKILL.md) — 为 HIXL 仓库中的 C++ 改动生成单元测试（UT）方案与代码草稿。
支持三种输入源：
1.
  `Ascend` `HIXL` `Offline analysis` `Workflow` · [Metadata](catalog/skills/hixl-ut-generator.yaml)
- [model-agent-ascendc-operator-code-review](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-code-review/SKILL.md) — Review AscendC source for correctness and engineering-rule violations.
  `Model Agent` `Ascend C` `Review and delivery` `Host tools` · [Metadata](catalog/skills/model-agent-ascendc-operator-code-review.yaml)
- [op-dashboard](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/op-dashboard/SKILL.md) — Generate an interactive operator dashboard for algorithm flow, UB tiling, precision, and performance.
  `CANNBot` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/op-dashboard.yaml)
- [ops-direct-invoke-maintain](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/ops-direct-invoke-maintain/SKILL.md) — Maintain direct-invocation workflow contracts, role definitions, and regression checks.
  `CANNBot` `Ascend C` `Review and delivery` `Host tools` · [Metadata](catalog/skills/ops-direct-invoke-maintain.yaml)
- [task-progress](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/task-progress/SKILL.md) — Maintain operator-workflow progress, state transitions, and unresolved tasks.
  `CANNBot` `Ascend C` `Review and delivery` `Community` `Host tools` · [Metadata](catalog/skills/task-progress.yaml)
- [triton-operator-code-review](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-code-review/SKILL.md) — Statically inspect Triton host/device code for correctness, API misuse, and performance hazards.
  `Model Agent` `Triton` `Review and delivery` `Host tools` · [Metadata](catalog/skills/triton-operator-code-review.yaml)
- [triton-operator-doc-gen](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/documentation/triton-operator-doc-gen/SKILL.md) — Generate Triton operator interface documentation with parameter, constraint, and usage examples.
  `Model Agent` `Triton` `Review and delivery` `Host tools` · [Metadata](catalog/skills/triton-operator-doc-gen.yaml)
- [vllm-ascend-change-validation](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-change-validation/SKILL.md) — Map a vLLM or vllm-ascend diff to sufficient correctness, build and performance evidence and summarize coverage.
  `vLLM Ascend` `Hardware depends on checks` · [Metadata](catalog/skills/vllm-ascend-change-validation.yaml)
- [vllm-ascend-release-note-writer](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/vllm-ascend-release-note-writer/SKILL.md) — You are a release note writer for vLLM Ascend project (vllm-project/vllm-ascend).
  `Ascend` `vLLM Ascend` `Offline analysis` `Workflow` · [Metadata](catalog/skills/vllm-ascend-release-note-writer.yaml)
- [vllm-ascend-release](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/vllm-ascend-release/SKILL.md) — End-to-end release management skill for vLLM Ascend.
  `Ascend` `vLLM Ascend` `Offline analysis` `Workflow` · [Metadata](catalog/skills/vllm-ascend-release.yaml)
- [vllm-dev-chat-organization](https://github.com/Henry-Avery/ascend-agent-skills/blob/c95957444543f136fa30ba054d1afd5cf3900622/skills/vllm-dev-chat-organization/SKILL.md) — Name vLLM development chats by their actual goal, organize a specified scope, and prepare or perform authorized archival.
  `vLLM` `vLLM Ascend` `Host tools` · [Metadata](catalog/skills/vllm-dev-chat-organization.yaml)

<!-- CATALOG:END -->

## Contributing

You can help improve this shared catalogue in several ways:

- **Suggest new skills**: Share skills you or your team use for Ascend inference engineering, describing their purpose, inputs, and outputs;
- **Report fixes or stale entries**: Submit issues or PRs if you encounter outdated metadata, broken links, or changed dependencies;
- **Propose new upstream collections**: Recommend publicly accessible skill repositories and workflow collections with clear licenses;
- **Submit execution reproductions**: Run cases under the skill's execution requirements and share the software and device environment, inputs, results, and logs.

Entries from every source follow the same inclusion standards. See the [contribution guide](CONTRIBUTING.md) for submission steps, metadata requirements, and maintenance commands.

## Related resources

- [vLLM Ascend Skills](https://github.com/pisceskkk/vllm-ascend-skills) — Upstream source collection for vLLM Ascend serving, benchmarking, and Triton workflows.
- [CANNBot Skills](https://gitcode.com/cann/cannbot-skills) — Upstream source collection for CANN environments, model integration, and operator engineering.
- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) — Reference for general agent skill discovery.
- [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md) — Community awesome list guidelines.
- [Brand assets](assets/brand.md) — SVG marks and design standards.

## License

This catalogue, maintenance scripts, and original graphics are dedicated to the public domain under [CC0-1.0](LICENSE). Linked upstream skills retain their respective project licenses; see [catalog/sources.yaml](catalog/sources.yaml).
