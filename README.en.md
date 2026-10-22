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

## Skill catalogue

Entries are grouped by their primary task and show technology tags, execution requirements, and metadata links. Definition reviews inspect pinned skill instructions and their declared purpose. Execution reproductions record specific environments and cases; coverage counts appear below.

Execution tags describe the following conditions:

- `NPU execution`: The complete workflow requires Ascend NPU hardware (planning and code inspection can be done locally);
- `Offline analysis`: Operates on existing profiling traces or diagnostic artifacts with the required host dependencies;
- `Host tools`: Runs host-side inspection, tiling design, or tools such as CANN Simulator;
- `Hardware depends on checks`: Required hardware depends on the specific validation test cases chosen.

Each entry's metadata links to its review scope, reproduction cases, and evidence. See the [catalogue format](docs/catalog-format.md) and [validation policy](docs/validation-policy.md) for fields and criteria.

<!-- CATALOG:START -->

83 skills · 10 categories

Definitions reviewed: 83 · Entries with execution reproductions: 0. See each entry's metadata for scope.

| Upstream Source | Listed | Maintainer | License |
|---|---|---|---|
| [vllm-ascend-skills](https://github.com/pisceskkk/vllm-ascend-skills) | 17 | pisceskkk | MIT |
| [cannbot-skills](https://gitcode.com/cann/cannbot-skills) | 36 | CANNBot SIG (cann) | CANN Open Software License v2.0 |
| [ascend-pooling-workflows](https://github.com/Yuli-yx/awesome-mindie-skills) | 1 | zouyida2052 and Yuli-yx | CC0-1.0 AND MIT (see package NOTICE) |
| [awesome-va-skills](https://github.com/Yuli-yx/awesome-va-skills) | 3 | Yuli-yx (adapted collection); wangxiaoteng888 (AISBench origin) | MIT (the three listed packages only) |
| [va-workflows](https://github.com/Yuli-yx/awesome-va-skills) | 10 | Yuli-yx collection; original authors credited in ATTRIBUTION.md | MIT |
| [va-hixl-workflows](https://github.com/Yuli-yx/awesome-va-skills) | 5 | Yuli-yx collection; original authors credited in ATTRIBUTION.md | CANN-2.0 |
| [va-apache-workflows](https://github.com/Yuli-yx/awesome-va-skills) | 4 | Yuli-yx collection; original authors credited in ATTRIBUTION.md | Apache-2.0 |
| [blue-server-toolkit](https://github.com/xuchi-0808/blue-server-toolkit) | 7 | xuchi-0808 | MIT |

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

- [ascendc-env-check](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-env-check/SKILL.md) — Check NPU status, CANN configuration, and development dependencies, and report device architecture and environment findings.
  `CANNBot` `CANN` `NPU execution` · [Metadata](catalog/skills/ascendc-env-check.yaml)
- [blue-server-provisioning](https://github.com/xuchi-0808/blue-server-toolkit/blob/5707a86922713f830f1f5fea2bedbb0a0a1cdc3a/skills/blue-server-provisioning/SKILL.md) — Bring up fresh Ascend servers and containers — bare-metal HDK driver and firmware installation (HwHiAiUser, driver before firmware), container creation with start-docker-A2/A3/A5.sh, and image-ID discipline.
  `Ascend` `CANN` `Docker` `NPU execution` · [Metadata](catalog/skills/blue-server-provisioning.yaml)
- [blue-vllm-ascend-build](https://github.com/xuchi-0808/blue-server-toolkit/blob/5707a86922713f830f1f5fea2bedbb0a0a1cdc3a/skills/blue-vllm-ascend-build/SKILL.md) — Build or upgrade vllm-ascend from source — editable two-step install, version pairing via vllm-main-verified.commit, setuptools 77 or newer, pip mirror setup, rsync-then-chown sync, and an error-keyword FAQ; pure CPU.
  `vLLM Ascend` `CANN` `Host tools` · [Metadata](catalog/skills/blue-vllm-ascend-build.yaml)
- [cann-env-setup](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/cann-env-setup/SKILL.md) — Guide CANN installation, environment configuration, and driver and Python interface checks.
  `CANNBot` `CANN` `NPU execution` · [Metadata](catalog/skills/cann-env-setup.yaml)
- [machine-management](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/machine-management/SKILL.md) — Add, verify, repair, or remove a managed remote NPU host for this workspace.
  `Ascend` `vLLM Ascend` `Hardware depends on checks` `Workflow` · [Metadata](catalog/skills/machine-management.yaml)
- [remote-code-parity](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/remote-code-parity/SKILL.md) — Ensure a ready remote runtime runs the exact current local workspace state before any remote smoke, service launch, or benchmark.
  `Ascend` `vLLM Ascend` `Host tools` `Workflow` · [Metadata](catalog/skills/remote-code-parity.yaml)
- [remote-toolbox](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/remote-toolbox/SKILL.md) — Resolve, probe, execute, observe jobs, sync, manage service lifecycle, transfer artifacts, and clean VAWS remote Ascend session containers through structured agent-facing CLI entrypoints..
  `Ascend` `vLLM Ascend` `Host tools` `Workflow` · [Metadata](catalog/skills/remote-toolbox.yaml)
- [repo-init](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/repo-init/SKILL.md) — Initialize this workspace after clone.
  `Ascend` `vLLM Ascend` `Host tools` `Workflow` · [Metadata](catalog/skills/repo-init.yaml)
- [session-management](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/session-management/SKILL.md) — Create, list, inspect, remove, and garbage-collect isolated VAWS agent sessions.
  `Ascend` `vLLM Ascend` `Host tools` `Workflow` · [Metadata](catalog/skills/session-management.yaml)
- [vllm-ascend-build](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/vllm-ascend-build/SKILL.md) — Compile and verify vLLM-Ascend from a pinned workspace or PR revision inside a ready Ascend container.
  `Ascend` `vLLM Ascend` `Host tools` `Workflow` · [Metadata](catalog/skills/vllm-ascend-build.yaml)

<a id="model-integration"></a>

### Model integration and conversion

Integrate models, convert weights, and verify configuration and input/output contracts.

- [main2main](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/main2main/SKILL.md) — Adapt vLLM-Ascend to upstream vLLM main changes.
  `Ascend` `vLLM Ascend` `Offline analysis` `Workflow` · [Metadata](catalog/skills/main2main.yaml)
- [model-infer-migrator](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-migrator/SKILL.md) — Adapt HF models or local code to cann-recipes-infer or a standalone runner and establish an eager inference baseline.
  `CANNBot` `PyTorch` `cann-recipes-infer` `NPU execution` · [Metadata](catalog/skills/model-infer-migrator.yaml)
- [modelscope](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/modelscope/SKILL.md) — Download, resume, status-check, and SHA256-verify ModelScope model weights.
  `Ascend` `vLLM Ascend` `Host tools` `Workflow` · [Metadata](catalog/skills/modelscope.yaml)
- [vllm-ascend-model-adapter](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/vllm-ascend-model-adapter/SKILL.md) — Adapt and debug existing or new models for vLLM on Ascend NPU.
  `Ascend` `vLLM Ascend` `NPU execution` `Workflow` · [Metadata](catalog/skills/vllm-ascend-model-adapter.yaml)

<a id="serving"></a>

### Serving and scaling

Deploy colocated or disaggregated services and verify topology, endpoints, and requests.

- [ascend-memcache-pooling](https://github.com/Yuli-yx/awesome-mindie-skills/blob/2844c25cd3f63cd0cd817cce866de827653babf2/skills/ascend-memcache-pooling/SKILL.md) — Deploy A3/A5 DRAM/SSD pools, preserve P/D transport, inspect Host RoCE and monitor multi-DP HBM, external reuse and SSD readback evidence.
  `MemCache` `MemFabric` `vLLM Ascend` `SSD` `Host RoCE` `Monitoring` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascend-memcache-pooling.yaml)
- [blue-vllm-service](https://github.com/xuchi-0808/blue-server-toolkit/blob/5707a86922713f830f1f5fea2bedbb0a0a1cdc3a/skills/blue-vllm-service/SKILL.md) — Manage the vLLM-on-Ascend service lifecycle — start and stop vllm serve in containers, health checks, multi-service layout, P/D disaggregated bring-up (mooncake, load-balance proxy), TP and parallelism planning, and graph-mode debugging.
  `vLLM Ascend` `NPU execution` · [Metadata](catalog/skills/blue-vllm-service.yaml)
- [model-infer-parallel-analysis](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-parallel-analysis/SKILL.md) — Analyze model structure and Atlas A2/A3 specifications to propose parallel_config candidates with quantitative rationale.
  `CANNBot` `PyTorch` `Parallelism` `Host tools` · [Metadata](catalog/skills/model-infer-parallel-analysis.yaml)
- [model-infer-parallel-impl](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-parallel-impl/SKILL.md) — Implement approved TP/EP configurations across parallel layers, communication groups, weights, and launch settings, then validate execution.
  `CANNBot` `PyTorch` `HCCL` `NPU execution` · [Metadata](catalog/skills/model-infer-parallel-impl.yaml)
- [vllm-ascend-pd-serving](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-pd-serving/SKILL.md) — Plan and review prefill/decode vLLM Ascend serving with explicit roles, connectors, ordering and KV transfer evidence.
  `vLLM Ascend` `PD` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-pd-serving.yaml)
- [vllm-ascend-serving](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-serving/SKILL.md) — Plan and review one colocated vLLM Ascend service lifecycle, including source pairing, device selection, launch, health, and cleanup.
  `vLLM Ascend` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-serving.yaml)

<a id="correctness"></a>

### Correctness and accuracy

Fix references and case matrices to compare outputs, numerical error, and task quality.

- [aisbench-accuracy](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/aisbench-accuracy/SKILL.md) — Run AISBench dataset accuracy evaluation against a running vLLM service, aligning sampling, prompts and answer postprocessing with the baseline.
  `Ascend` `vLLM Ascend` `NPU execution` `Workflow` · [Metadata](catalog/skills/aisbench-accuracy.yaml)
- [ops-precision-standard](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ops-precision-standard/SKILL.md) — Select accuracy comparison rules by operator semantics and dtype to define acceptance criteria and reference results.
  `CANNBot` `Ascend C` `Host tools` · [Metadata](catalog/skills/ops-precision-standard.yaml)
- [ops-simulator](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ops-simulator/SKILL.md) — Use CANN Simulator on the host for operator correctness and performance simulation and pipeline report analysis.
  `CANNBot` `CANN Simulator` `Host tools` · [Metadata](catalog/skills/ops-simulator.yaml)
- [vllm-ascend-correctness-validation](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-correctness-validation/SKILL.md) — Design and compare deterministic vLLM Ascend correctness cases across code states, execution modes and API paths.
  `vLLM Ascend` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-correctness-validation.yaml)

<a id="benchmarking"></a>

### Benchmarking and regressions

Evaluate throughput and latency using warmup, repeated measurements, and controlled comparisons.

- [aisbench-pd-benchmark](https://github.com/Yuli-yx/awesome-va-skills/blob/8d9f7ee56d088f15a398181590c4512bfc725d6f/.agents/skills/aisbench-pd-benchmark/SKILL.md) — Prepare proxy-routed AISBench cases with tokenizer-based datasets, separate warmup and formal runs, and captured configuration and results.
  `vLLM Ascend` `AISBench` `PD` `NPU execution` · [Metadata](catalog/skills/aisbench-pd-benchmark.yaml)
- [pd-pure-role-benchmark](https://github.com/Yuli-yx/awesome-va-skills/blob/8d9f7ee56d088f15a398181590c4512bfc725d6f/.agents/skills/pd-pure-role-benchmark/SKILL.md) — Validate pure Prefill and Decode capacity and end-to-end steady QPS with TTFT, TPOT, cache-hit, role-bottleneck and MTP controls.
  `vLLM Ascend` `AISBench` `PD` `MTP` `NPU execution` `Workflow` · [Metadata](catalog/skills/pd-pure-role-benchmark.yaml)
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
- [ge-memory-analysis](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/graph/ge-memory-analysis/SKILL.md) — Triage GE device memory, host leaks, and operator addresses, and attribute memory use from logs and reports.
  `CANNBot` `GE` `HBM` `Hardware depends on checks` · [Metadata](catalog/skills/ge-memory-analysis.yaml)
- [model-infer-perf-breakdown](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-perf-breakdown/SKILL.md) — Break down kernel_details.csv and traces by model component and generate an HTML report of timing, gaps, and anomalous layers.
  `CANNBot` `Ascend` `Profiling` `Offline analysis` · [Metadata](catalog/skills/model-infer-perf-breakdown.yaml)
- [model-infer-profiling](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-profiling/SKILL.md) — Collect model profiling data through built-in or injected torch_npu.profiler instrumentation and verify output completeness.
  `CANNBot` `PyTorch` `torch_npu` `NPU execution` · [Metadata](catalog/skills/model-infer-profiling.yaml)
- [ops-profiling](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ops-profiling/SKILL.md) — Collect operator performance with msprof, compare candidates against references, and report bottlenecks and measurements.
  `CANNBot` `CANN` `msprof` `NPU execution` · [Metadata](catalog/skills/ops-profiling.yaml)
- [vllm-ascend-memory-profiling](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-memory-profiling/SKILL.md) — Attribute Ascend HBM use during vLLM serving to weights, KV cache, HCCL, activations and runtime components.
  `vLLM Ascend` `HBM` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-memory-profiling.yaml)
- [vllm-ascend-profiling-collection](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-profiling-collection/SKILL.md) — Collect one vLLM Ascend serving torch-profiler case with a verified workload window and complete rank outputs.
  `vLLM Ascend` `torch-profiler` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-profiling-collection.yaml)

<a id="optimization"></a>

### Inference optimization

Optimize execution, scheduling, and resource overlap with paired correctness and performance validation.

- [ascend-model-multistream-overlap-skill](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-model-multistream-overlap-skill/SKILL.md) — Design Ascend model multistream overlap from verified source mapping, resource-aware DAGs and paired validation.
  `Ascend` `Multistream` `NPU execution` · [Metadata](catalog/skills/ascend-model-multistream-overlap-skill.yaml)
- [ge-fusion-pass-skill](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/graph/ge-fusion-pass-skill/SKILL.md) — Coordinate requirements, implementation, and functional validation for GE custom fusion passes with stage evidence.
  `CANNBot` `GE` `CANN` `Hardware depends on checks` `Workflow` · [Metadata](catalog/skills/ge-fusion-pass-skill.yaml)
- [model-infer-fusion](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-fusion/SKILL.md) — Match PyTorch model computation patterns to torch_npu fused operators, implement replacements, and validate them.
  `CANNBot` `PyTorch` `torch_npu` `NPU execution` · [Metadata](catalog/skills/model-infer-fusion.yaml)
- [model-infer-graph-mode](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-graph-mode/SKILL.md) — Adapt model decode paths to npugraph_ex or GE graph mode, address graph breaks, and validate results.
  `CANNBot` `PyTorch` `Graph` `NPU execution` · [Metadata](catalog/skills/model-infer-graph-mode.yaml)
- [model-infer-kvcache](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-kvcache/SKILL.md) — Select and implement contiguous, paged, MLA, or sliding-window KV caches, integrate attention operators, and validate behavior.
  `CANNBot` `PyTorch` `KV cache` `NPU execution` · [Metadata](catalog/skills/model-infer-kvcache.yaml)
- [model-infer-multi-stream](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-multi-stream/SKILL.md) — Provide model DAG analysis, multistream API selection, synchronization, and core-allocation guidance for planning and overlap validation.
  `CANNBot` `PyTorch` `Multistream` `Hardware depends on checks` · [Metadata](catalog/skills/model-infer-multi-stream.yaml)
- [model-infer-prefetch](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-prefetch/SKILL.md) — Design weight-prefetch windows for confirmed memory-bound hotspots, integrate npu_prefetch, and measure gains.
  `CANNBot` `torch_npu` `Prefetch` `NPU execution` · [Metadata](catalog/skills/model-infer-prefetch.yaml)
- [model-infer-quantization](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-quantization/SKILL.md) — Integrate existing compressed-tensors quantized weights and verify artifact contracts, runtime mapping, activation, and gains.
  `CANNBot` `PyTorch` `compressed-tensors` `NPU execution` · [Metadata](catalog/skills/model-infer-quantization.yaml)

<a id="operators"></a>

### Operator development and migration

Connect kernel implementation, case validation, and per-shape optimization.

- [ascend-triton-kernel-optimization](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-kernel-optimization/SKILL.md) — Optimize a correctness-passed Ascend Triton kernel with per-shape measurements and profiler evidence.
  `Ascend` `Triton` `NPU execution` · [Metadata](catalog/skills/ascend-triton-kernel-optimization.yaml)
- [ascend-triton-kernel-validation](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-kernel-validation/SKILL.md) — Validate an Ascend Triton candidate against a trusted reference with a declared case matrix and fallback gate.
  `Ascend` `Triton` `NPU execution` · [Metadata](catalog/skills/ascend-triton-kernel-validation.yaml)
- [ascend-triton-operator-development](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-operator-development/SKILL.md) — Develop the first correct Ascend Triton kernel from a PyTorch reference or a GPU Triton implementation.
  `Ascend` `Triton` `NPU execution` · [Metadata](catalog/skills/ascend-triton-operator-development.yaml)
- [ascend-triton-workflow](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-workflow/SKILL.md) — Coordinate complete Ascend Triton operator development, correctness validation and optimization with linked evidence.
  `Ascend` `Triton` `NPU execution` `Workflow` · [Metadata](catalog/skills/ascend-triton-workflow.yaml)
- [ascendc-direct-invoke-template](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-direct-invoke-template/SKILL.md) — Select an Ascend C direct-invocation template for Vector, Blaze Matmul, or Kirin and scaffold the operator project.
  `CANNBot` `Ascend C` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-direct-invoke-template.yaml)
- [ascendc-perf-optimize](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-perf-optimize/SKILL.md) — Combine tiling models, simulation, and profiling to plan inter-device, inter-core, and intra-core pipeline optimizations.
  `CANNBot` `Ascend C` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-perf-optimize.yaml)
- [ascendc-registry-invoke-template](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-registry-invoke-template/SKILL.md) — Build Ascend C registered-operator projects from templates with multi-architecture implementations and UT/ST examples.
  `CANNBot` `Ascend C` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-registry-invoke-template.yaml)
- [ascendc-tiling-design](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-tiling-design/SKILL.md) — Design multicore and UB tiling, buffer allocation, and branch coverage by operator family.
  `CANNBot` `Ascend C` `Host tools` · [Metadata](catalog/skills/ascendc-tiling-design.yaml)
- [catlass-op-develop](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/catlass-op-develop/SKILL.md) — Generate CATLASS kernels, device invocation, parameters, and epilogues from a design and reference project.
  `CANNBot` `CATLASS` `Hardware depends on checks` · [Metadata](catalog/skills/catlass-op-develop.yaml)
- [pypto-op-develop](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/pypto-op-develop/SKILL.md) — Build PyPTO implementation modules in phases from design contracts, then consolidate the final kernel and documentation.
  `CANNBot` `PyPTO` `Hardware depends on checks` · [Metadata](catalog/skills/pypto-op-develop.yaml)
- [tilelang-op-develop](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/tilelang-op-develop/SKILL.md) — Use device evidence to route TileLang implementation and accuracy validation to the Ascend910 or Ascend950 workflow.
  `CANNBot` `TileLang` `NPU execution` · [Metadata](catalog/skills/tilelang-op-develop.yaml)
- [torch-custom-ops-guide](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/graph/torch-custom-ops-guide/SKILL.md) — Design registration, Meta inference, and npugraph_ex graph integration for Python custom operators.
  `CANNBot` `PyTorch` `npugraph_ex` `Hardware depends on checks` · [Metadata](catalog/skills/torch-custom-ops-guide.yaml)
- [triton-op-coding](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/triton-op-coding/SKILL.md) — Generate Triton Ascend kernels from task descriptions and iterate on code using error feedback.
  `CANNBot` `Triton` `Hardware depends on checks` · [Metadata](catalog/skills/triton-op-coding.yaml)

<a id="debugging"></a>

### Debugging

Reduce startup, communication, graph, and operator failures and verify fixes.

- [ascend-operator-debug](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-operator-debug/SKILL.md) — Reduce an Ascend model symptom to one operator call and validate its dtype, shape, layout and execution modes.
  `Ascend` `NPU execution` · [Metadata](catalog/skills/ascend-operator-debug.yaml)
- [ascendc-precision-debug](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-precision-debug/SKILL.md) — Reduce Ascend C accuracy failures to minimal reproducers and inspect numerical stability, synchronization, and data movement.
  `CANNBot` `Ascend C` `Hardware depends on checks` · [Metadata](catalog/skills/ascendc-precision-debug.yaml)
- [asys-toolkit](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/tools/asys-toolkit/SKILL.md) — Use asys in Ascend EP environments to collect failure information, inspect device health, and parse diagnostic artifacts.
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
- [ge-dynamic-shape-diagnose](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/graph/ge-dynamic-shape-diagnose/SKILL.md) — Identify unknown-graph and dynamic-shape scheduling triggers from GE compiler logs.
  `CANNBot` `GE` `Offline analysis` · [Metadata](catalog/skills/ge-dynamic-shape-diagnose.yaml)
- [hixl-troubleshoot](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/hixl-troubleshoot/SKILL.md) — 在 Ascend 上定位 HIXL/ADXL/HIXL_CS 建链、传输问题。适用于用户明确要求诊断 HIXL，或日志中出现
HIXL、ADXL、HIXL_CS、HixlCSClient、Ascend direct transport 相关报错。
.
  `Ascend` `HIXL` `NPU execution` `Workflow` · [Metadata](catalog/skills/hixl-troubleshoot.yaml)
- [model-infer-precision-debug](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-precision-debug/SKILL.md) — Diagnose KVCache and FlashAttention prefill/decode accuracy differences, cache updates, and mapping errors.
  `CANNBot` `PyTorch` `KV cache` `NPU execution` · [Metadata](catalog/skills/model-infer-precision-debug.yaml)
- [model-infer-runtime-debug](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-runtime-debug/SKILL.md) — Narrow model loading and inference failures to diagnose HCCL errors, OOM, timeouts, and hangs, then verify fixes.
  `CANNBot` `PyTorch` `HCCL` `NPU execution` · [Metadata](catalog/skills/model-infer-runtime-debug.yaml)
- [msaicerr-toolkit](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/tools/msaicerr-toolkit/SKILL.md) — Use msaicerr in the originating runtime environment to analyze AI Core errors, parse dumps, and check environment constraints.
  `CANNBot` `CANN` `msaicerr` `Hardware depends on checks` · [Metadata](catalog/skills/msaicerr-toolkit.yaml)
- [msnpureport-toolkit](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/tools/msnpureport-toolkit/SKILL.md) — Export device logs and query or set diagnostic configuration with the required permissions in supported Ascend EP environments.
  `CANNBot` `CANN` `msnpureport` `NPU execution` · [Metadata](catalog/skills/msnpureport-toolkit.yaml)
- [torch-npugraph-ex-dfx-triage](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/graph/torch-npugraph-ex-dfx-triage/SKILL.md) — Collect layered logs and route npugraph_ex issues to compilation, runtime, accuracy, or performance diagnosis.
  `CANNBot` `PyTorch` `npugraph_ex` `Hardware depends on checks` `Workflow` · [Metadata](catalog/skills/torch-npugraph-ex-dfx-triage.yaml)
- [vllm-ascend-distributed-debug](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-distributed-debug/SKILL.md) — Diagnose Ascend multi-rank startup, collective, endpoint and hang failures using explicit topology and per-rank evidence.
  `vLLM Ascend` `HCCL` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-distributed-debug.yaml)
- [vllm-ascend-graph-debug](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-graph-debug/SKILL.md) — Localize Ascend graph capture, replay or eager/graph divergence with controlled experiments and intermediate snapshots.
  `vLLM Ascend` `Graph` `NPU execution` · [Metadata](catalog/skills/vllm-ascend-graph-debug.yaml)

<a id="delivery"></a>

### Delivery and operations

Map changes to build, correctness, and performance checks and record coverage.

- [ascendc-code-review](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-code-review/SKILL.md) — Route Ascend C reviews by file, PR, or targeted question to check coding rules and design consistency.
  `CANNBot` `Ascend C` `Host tools` · [Metadata](catalog/skills/ascendc-code-review.yaml)
- [blue-npu-ops](https://github.com/xuchi-0808/blue-server-toolkit/blob/5707a86922713f830f1f5fea2bedbb0a0a1cdc3a/skills/blue-npu-ops/SKILL.md) — Operate a single NPU server — npu-smi status reading, HBM usage and orphan release, precise-PID cleanup of leftover processes, idle checks, A3 chip numbering and device visibility mapping, and torch-based FLOPS measurement.
  `Ascend` `HBM` `NPU execution` · [Metadata](catalog/skills/blue-npu-ops.yaml)
- [blue-server-toolkit](https://github.com/xuchi-0808/blue-server-toolkit/blob/5707a86922713f830f1f5fea2bedbb0a0a1cdc3a/skills/blue-server-toolkit/SKILL.md) — Perform high-frequency daily operations on remote Ascend NPU development servers — SSH connection checks and stability (persistent ControlMaster multiplexing), code sync, UT execution, model and image download, log viewing, container management, and file transfer; also the routing hub when unsure which sibling skill fits.
  `Ascend` `Docker` `SSH` `Host tools` · [Metadata](catalog/skills/blue-server-toolkit.yaml)
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
- [vllm-ascend-change-validation](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-change-validation/SKILL.md) — Map a vLLM or vllm-ascend diff to sufficient correctness, build and performance evidence and summarize coverage.
  `vLLM Ascend` `Hardware depends on checks` · [Metadata](catalog/skills/vllm-ascend-change-validation.yaml)
- [vllm-ascend-release-note-writer](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/vllm-ascend-release-note-writer/SKILL.md) — You are a release note writer for vLLM Ascend project (vllm-project/vllm-ascend).
  `Ascend` `vLLM Ascend` `Offline analysis` `Workflow` · [Metadata](catalog/skills/vllm-ascend-release-note-writer.yaml)
- [vllm-ascend-release](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/.agents/skills/vllm-ascend-release/SKILL.md) — End-to-end release management skill for vLLM Ascend.
  `Ascend` `vLLM Ascend` `Offline analysis` `Workflow` · [Metadata](catalog/skills/vllm-ascend-release.yaml)

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
