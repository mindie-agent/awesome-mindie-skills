<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img src="assets/banner-light.svg" alt="Awesome MindIE Skills — Curated Agent Skills for Ascend Inference" width="960">
  </picture>
</p>

# Awesome MindIE Skills

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-0F766E.svg)](LICENSE)

中文 | [English](README.en.md)

面向 **Ascend（昇腾）推理工程**的 Agent Skills 共享清单，帮助开发者按任务查找、使用和贡献可复用的工程工作流。

目录覆盖环境配置、模型接入、服务部署、正确性验证、性能分析与算子开发。每项技能链接到原始维护位置，并记录执行条件、源码版本和验证信息。技能通常以 `SKILL.md` 组织任务说明、执行流程与参考资料，供编程助手按需加载。

欢迎分享实用技能、修正条目说明，以及贡献可复现的使用结果。

## 从任务开始

根据当前工程目标，快速定位对应的分类入口：

| 研发任务 | 分类入口 |
|---|---|
| 检查 NPU 环境或配置 CANN 软件栈 | [环境与依赖](#environment) |
| 将模型适配到 Ascend 并建立运行基线 | [模型接入与转换](#model-integration) |
| 部署推理服务，或配置 PD 分离架构 | [服务部署与扩展](#serving) |
| 验证推理结果数值正确性与精度对齐 | [正确性与精度](#correctness) |
| 测量吞吐与时延，排查性能劣化 | [性能评测与回归](#benchmarking) |
| 采集与分析 Trace、跨卡行为或显存占用 | [Profiling 与瓶颈分析](#profiling) |
| 适配量化、KV 缓存、图模式或多流并发 | [推理优化](#optimization) |
| 使用 Ascend C、CATLASS、PyPTO、TileLang 或 Triton 开发算子 | [算子开发与迁移](#operators) |
| 定位运行时崩溃、卡死或图编译器异常 | [故障诊断](#debugging) |
| 为代码变更制定验证计划 | [工程交付与运行维护](#delivery) |

## 通用使用流程

选择技能后，按以下步骤在项目中使用：

1. **选择技能**：根据工程任务在[技能目录](#技能目录)中选择适用的技能条目；
2. **查阅范围与依赖**：阅读条目声明的用途、软硬件前提及执行条件（如离线分析、主机工具或需 NPU 硬件）；
3. **获取源码**：将对应的上游仓库克隆至本地并检出记录的固定 commit（具体安装与依赖命令见[使用指南](docs/getting-started.zh.md)）；
4. **加载并提供输入**：在 AI 编程助手或智能体环境中加载技能的 `SKILL.md` 文件，指定目标项目路径与任务参数。

**通用调用示例**：

> 请阅读 `<skill-path>/SKILL.md`，按照其定义的工作流程对我的项目路径 `/path/to/project` 执行 `<task-name>`，任务输入参数为 `<inputs>`，并输出执行结论与关键证据路径。

## 技能目录

目录按主要任务分类，条目展示技术栈、执行条件与元数据入口。定义审阅核对固定版本的技能说明与声明用途；运行复现按具体环境和用例记录，覆盖数量见下方统计。

执行条件标签含义如下：

- `执行需 NPU`：完整工作流需在昇腾 NPU 设备上运行（阅读分析与方案设计可在本地进行）；
- `离线分析`：基于已有 Profiling 或诊断产物进行离线分析，需安装对应主机脚本依赖；
- `主机工具`：运行代码检查、设计规划或 CANN Simulator 模拟等主机侧工具；
- `设备取决于检查项`：所需运行环境取决于用户选择的验证用例。

审阅范围、复现案例及其证据见各条目记录。字段与判定规则见[条目格式](docs/catalog-format.zh.md)和[验证规则](docs/validation-policy.zh.md)。

<!-- CATALOG:START -->

53 个技能 · 10 个分类

定义已审阅：53 · 已有运行复现记录：0。具体范围见各条目记录。

| 来源项目 | 已收录 | 维护者 | 许可证 |
|---|---|---|---|
| [vllm-ascend-skills](https://github.com/pisceskkk/vllm-ascend-skills) | 17 | pisceskkk | MIT |
| [cannbot-skills](https://gitcode.com/cann/cannbot-skills) | 36 | CANNBot SIG (cann) | CANN Open Software License v2.0 |

- [环境与依赖](#environment)
- [模型接入与转换](#model-integration)
- [服务部署与扩展](#serving)
- [正确性与精度](#correctness)
- [性能评测与回归](#benchmarking)
- [Profiling 与瓶颈分析](#profiling)
- [推理优化](#optimization)
- [算子开发与迁移](#operators)
- [故障诊断](#debugging)
- [工程交付与运行维护](#delivery)

<a id="environment"></a>

### 环境与依赖

检查驱动、CANN、框架配套、容器和设备环境。

- [ascendc-env-check](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-env-check/SKILL.md) — 查询 NPU 状态、CANN 配置和开发依赖，输出设备架构与环境检查结果。
  `CANNBot` `CANN` `执行需 NPU` · [条目](catalog/skills/ascendc-env-check.yaml)
- [cann-env-setup](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/cann-env-setup/SKILL.md) — 指导 CANN 安装、环境变量配置及驱动和 Python 接口验证。
  `CANNBot` `CANN` `执行需 NPU` · [条目](catalog/skills/cann-env-setup.yaml)

<a id="model-integration"></a>

### 模型接入与转换

接入模型、转换权重，并核对配置与输入输出。

- [model-infer-migrator](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-migrator/SKILL.md) — 将 HF 模型或本地代码适配到 cann-recipes-infer 或独立 Runner，建立 eager 推理基线。
  `CANNBot` `PyTorch` `cann-recipes-infer` `执行需 NPU` · [条目](catalog/skills/model-infer-migrator.yaml)

<a id="serving"></a>

### 服务部署与扩展

部署共置或 PD 分离服务，验证拓扑、端点与请求。

- [model-infer-parallel-analysis](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-parallel-analysis/SKILL.md) — 根据模型结构与 Atlas A2/A3 规格分析并行策略，输出 parallel_config 候选和定量依据。
  `CANNBot` `PyTorch` `Parallelism` `主机工具` · [条目](catalog/skills/model-infer-parallel-analysis.yaml)
- [model-infer-parallel-impl](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-parallel-impl/SKILL.md) — 按确认的 TP/EP 配置改造并行层、通信组、权重和启动配置，并验证模型运行。
  `CANNBot` `PyTorch` `HCCL` `执行需 NPU` · [条目](catalog/skills/model-infer-parallel-impl.yaml)
- [vllm-ascend-pd-serving](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-pd-serving/SKILL.md) — 部署 Prefill/Decode 分离服务，验证连接器、角色启动顺序与 KV 传输。
  `vLLM Ascend` `PD` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-pd-serving.yaml)
- [vllm-ascend-serving](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-serving/SKILL.md) — 完成共置服务的版本配对、设备选择、启动、健康检查与清理。
  `vLLM Ascend` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-serving.yaml)

<a id="correctness"></a>

### 正确性与精度

固定参考与用例矩阵，比较输出、误差和任务质量。

- [ops-precision-standard](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ops-precision-standard/SKILL.md) — 按算子语义和 dtype 选择精度比对规则，辅助构造验收标准与参考结果。
  `CANNBot` `Ascend C` `主机工具` · [条目](catalog/skills/ops-precision-standard.yaml)
- [ops-simulator](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ops-simulator/SKILL.md) — 使用 CANN Simulator 在主机执行算子精度和性能仿真，并分析流水线报告。
  `CANNBot` `CANN Simulator` `主机工具` · [条目](catalog/skills/ops-simulator.yaml)
- [vllm-ascend-correctness-validation](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-correctness-validation/SKILL.md) — 设计确定性用例，比较代码版本、执行模式与 API 路径的输出。
  `vLLM Ascend` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-correctness-validation.yaml)

<a id="benchmarking"></a>

### 性能评测与回归

通过预热、重复测量和受控对比评估吞吐与延迟。

- [vllm-ascend-benchmark](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-benchmark/SKILL.md) — 对一个代码状态进行预热与重复测量，输出归一化吞吐和延迟指标。
  `vLLM Ascend` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-benchmark.yaml)
- [vllm-ascend-performance-regression](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-performance-regression/SKILL.md) — 交替运行基线与候选版本，在相同负载下比较性能变化与波动。
  `vLLM Ascend` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-performance-regression.yaml)

<a id="profiling"></a>

### Profiling 与瓶颈分析

采集或分析 trace、逐 rank 行为与 HBM 占用，保留证据。

- [ascend-profiling-analysis](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-profiling-analysis/SKILL.md) — 分析 rank、step、layer、block、算子及跨 rank 行为，输出可追溯的瓶颈证据。
  `Ascend` `Profiling` `离线分析` · [条目](catalog/skills/ascend-profiling-analysis.yaml)
- [ge-memory-analysis](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/graph/ge-memory-analysis/SKILL.md) — 分诊 GE Device 显存、Host 泄漏及算子地址问题，结合日志和报告进行内存归因。
  `CANNBot` `GE` `HBM` `设备取决于检查项` · [条目](catalog/skills/ge-memory-analysis.yaml)
- [model-infer-perf-breakdown](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-perf-breakdown/SKILL.md) — 将 kernel_details.csv 与 trace 按模型组件拆解，生成耗时、空隙和异常层 HTML 报告。
  `CANNBot` `Ascend` `Profiling` `离线分析` · [条目](catalog/skills/model-infer-perf-breakdown.yaml)
- [model-infer-profiling](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-profiling/SKILL.md) — 通过框架内置或注入式 torch_npu.profiler 采集模型性能数据，并检查输出完整性。
  `CANNBot` `PyTorch` `torch_npu` `执行需 NPU` · [条目](catalog/skills/model-infer-profiling.yaml)
- [ops-profiling](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ops-profiling/SKILL.md) — 用 msprof 采集算子性能，对比候选与标杆并生成瓶颈分析和测量报告。
  `CANNBot` `CANN` `msprof` `执行需 NPU` · [条目](catalog/skills/ops-profiling.yaml)
- [vllm-ascend-memory-profiling](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-memory-profiling/SKILL.md) — 将服务 HBM 占用归因到权重、KV cache、HCCL、激活与运行时，并说明残差。
  `vLLM Ascend` `HBM` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-memory-profiling.yaml)
- [vllm-ascend-profiling-collection](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-profiling-collection/SKILL.md) — 采集指定负载窗口的 torch-profiler 数据，检查请求成功与逐 rank 输出完整性。
  `vLLM Ascend` `torch-profiler` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-profiling-collection.yaml)

<a id="optimization"></a>

### 推理优化

优化执行、调度和资源重叠，并配对验证正确性与收益。

- [ascend-model-multistream-overlap-skill](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-model-multistream-overlap-skill/SKILL.md) — 从源码与 trace 构建资源约束 DAG，设计多流重叠并配对验证收益。
  `Ascend` `Multistream` `执行需 NPU` · [条目](catalog/skills/ascend-model-multistream-overlap-skill.yaml)
- [ge-fusion-pass-skill](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/graph/ge-fusion-pass-skill/SKILL.md) — 串联 GE 自定义融合 pass 的需求分析、实现与功能验证，交付阶段证据。
  `CANNBot` `GE` `CANN` `设备取决于检查项` `流程编排` · [条目](catalog/skills/ge-fusion-pass-skill.yaml)
- [model-infer-fusion](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-fusion/SKILL.md) — 匹配 PyTorch 模型中的计算模式与 torch_npu 融合算子，实施替换并验证。
  `CANNBot` `PyTorch` `torch_npu` `执行需 NPU` · [条目](catalog/skills/model-infer-fusion.yaml)
- [model-infer-graph-mode](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-graph-mode/SKILL.md) — 适配模型 Decode 路径的 npugraph_ex 或 GE 图模式，处理图中断并验证结果。
  `CANNBot` `PyTorch` `Graph` `执行需 NPU` · [条目](catalog/skills/model-infer-graph-mode.yaml)
- [model-infer-kvcache](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-kvcache/SKILL.md) — 选择并改造连续缓存、Paged Attention、MLA 或滑窗 KV cache，衔接 FA 算子并验证。
  `CANNBot` `PyTorch` `KV cache` `执行需 NPU` · [条目](catalog/skills/model-infer-kvcache.yaml)
- [model-infer-multi-stream](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-multi-stream/SKILL.md) — 提供模型 DAG 拆解、多流 API 选择、同步与控核规则，用于方案设计和重叠验证。
  `CANNBot` `PyTorch` `Multistream` `设备取决于检查项` · [条目](catalog/skills/model-infer-multi-stream.yaml)
- [model-infer-prefetch](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-prefetch/SKILL.md) — 针对已确认的 memory-bound 热点设计权重预取窗口，接入 npu_prefetch 并测量收益。
  `CANNBot` `torch_npu` `Prefetch` `执行需 NPU` · [条目](catalog/skills/model-infer-prefetch.yaml)
- [model-infer-quantization](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-quantization/SKILL.md) — 接入已有 compressed-tensors 量化权重，检查产物契约、运行时映射、真实生效与收益。
  `CANNBot` `PyTorch` `compressed-tensors` `执行需 NPU` · [条目](catalog/skills/model-infer-quantization.yaml)

<a id="operators"></a>

### 算子开发与迁移

串联算子实现、用例验证和逐 shape 性能优化。

- [ascend-triton-kernel-optimization](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-kernel-optimization/SKILL.md) — 对正确性通过的内核进行逐 shape 测量，结合 profiler 迭代优化。
  `Ascend` `Triton` `执行需 NPU` · [条目](catalog/skills/ascend-triton-kernel-optimization.yaml)
- [ascend-triton-kernel-validation](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-kernel-validation/SKILL.md) — 按 shape、dtype、layout 和 stride 矩阵验证候选与参考，检查执行路径和 fallback。
  `Ascend` `Triton` `执行需 NPU` · [条目](catalog/skills/ascend-triton-kernel-validation.yaml)
- [ascend-triton-operator-development](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-operator-development/SKILL.md) — 从 PyTorch 参考或 GPU Triton 实现开发首个 Ascend Triton 算子候选。
  `Ascend` `Triton` `执行需 NPU` · [条目](catalog/skills/ascend-triton-operator-development.yaml)
- [ascend-triton-workflow](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-workflow/SKILL.md) — 协调 Triton 算子开发、正确性验证与性能优化，衔接各阶段证据。
  `Ascend` `Triton` `执行需 NPU` `流程编排` · [条目](catalog/skills/ascend-triton-workflow.yaml)
- [ascendc-direct-invoke-template](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-direct-invoke-template/SKILL.md) — 按 Vector、Blaze Matmul 或 Kirin 路径选择 Ascend C Kernel 直调模板并搭建工程。
  `CANNBot` `Ascend C` `设备取决于检查项` · [条目](catalog/skills/ascendc-direct-invoke-template.yaml)
- [ascendc-perf-optimize](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-perf-optimize/SKILL.md) — 结合 Tiling 模型、仿真与 profiling，制定卡间、核间和核内流水优化策略。
  `CANNBot` `Ascend C` `设备取决于检查项` · [条目](catalog/skills/ascendc-perf-optimize.yaml)
- [ascendc-registry-invoke-template](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-registry-invoke-template/SKILL.md) — 基于模板搭建 Ascend C 注册调用工程，参考多架构实现和 UT/ST 样例。
  `CANNBot` `Ascend C` `设备取决于检查项` · [条目](catalog/skills/ascendc-registry-invoke-template.yaml)
- [ascendc-tiling-design](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-tiling-design/SKILL.md) — 按算子类别设计多核和 UB 切分、Buffer 规划与分支覆盖。
  `CANNBot` `Ascend C` `主机工具` · [条目](catalog/skills/ascendc-tiling-design.yaml)
- [catlass-op-develop](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/catlass-op-develop/SKILL.md) — 依据设计和 CATLASS 参考工程生成 Kernel、Device 调用、Params 与 Epilogue 实现。
  `CANNBot` `CATLASS` `设备取决于检查项` · [条目](catalog/skills/catlass-op-develop.yaml)
- [pypto-op-develop](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/pypto-op-develop/SKILL.md) — 根据设计契约逐阶段构建 PyPTO impl 模块，整理最终内核实现和说明。
  `CANNBot` `PyPTO` `设备取决于检查项` · [条目](catalog/skills/pypto-op-develop.yaml)
- [tilelang-op-develop](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/tilelang-op-develop/SKILL.md) — 根据设备探测结果路由到 Ascend910 或 Ascend950 的 TileLang 实现与精度验证流程。
  `CANNBot` `TileLang` `执行需 NPU` · [条目](catalog/skills/tilelang-op-develop.yaml)
- [torch-custom-ops-guide](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/graph/torch-custom-ops-guide/SKILL.md) — 为纯 Python 自定义算子设计注册、Meta 推导和 npugraph_ex 入图适配。
  `CANNBot` `PyTorch` `npugraph_ex` `设备取决于检查项` · [条目](catalog/skills/torch-custom-ops-guide.yaml)
- [triton-op-coding](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/triton-op-coding/SKILL.md) — 根据任务描述生成 Triton Ascend 内核，并结合错误反馈迭代代码。
  `CANNBot` `Triton` `设备取决于检查项` · [条目](catalog/skills/triton-op-coding.yaml)

<a id="debugging"></a>

### 故障诊断

缩小启动、通信、图执行和算子异常的复现范围并验证修复。

- [ascend-operator-debug](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-operator-debug/SKILL.md) — 将模型异常缩小到单算子调用，检查 dtype、shape、layout 与执行模式。
  `Ascend` `执行需 NPU` · [条目](catalog/skills/ascend-operator-debug.yaml)
- [ascendc-precision-debug](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-precision-debug/SKILL.md) — 从最小复现定位 Ascend C 精度异常，检查数值稳定性、同步和数据搬运。
  `CANNBot` `Ascend C` `设备取决于检查项` · [条目](catalog/skills/ascendc-precision-debug.yaml)
- [asys-toolkit](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/tools/asys-toolkit/SKILL.md) — 在 Ascend EP 环境使用 asys 收集故障信息、检查设备健康并解析诊断产物。
  `CANNBot` `CANN` `asys` `设备取决于检查项` · [条目](catalog/skills/asys-toolkit.yaml)
- [ge-dynamic-shape-diagnose](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/graph/ge-dynamic-shape-diagnose/SKILL.md) — 根据 GE 编译日志定位 unknown graph 与动态 shape 调度的触发原因。
  `CANNBot` `GE` `离线分析` · [条目](catalog/skills/ge-dynamic-shape-diagnose.yaml)
- [model-infer-precision-debug](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-precision-debug/SKILL.md) — 定位 KVCache 与 FlashAttention 相关的 Prefill/Decode 精度差异、缓存更新和映射问题。
  `CANNBot` `PyTorch` `KV cache` `执行需 NPU` · [条目](catalog/skills/model-infer-precision-debug.yaml)
- [model-infer-runtime-debug](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/model/model-infer-runtime-debug/SKILL.md) — 逐阶段缩小模型加载和推理运行异常，诊断 HCCL、OOM、超时与卡死并验证修复。
  `CANNBot` `PyTorch` `HCCL` `执行需 NPU` · [条目](catalog/skills/model-infer-runtime-debug.yaml)
- [msaicerr-toolkit](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/tools/msaicerr-toolkit/SKILL.md) — 在日志产生环境使用 msaicerr 分析 AI Core Error、解析 Dump 并检查环境约束。
  `CANNBot` `CANN` `msaicerr` `设备取决于检查项` · [条目](catalog/skills/msaicerr-toolkit.yaml)
- [msnpureport-toolkit](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/tools/msnpureport-toolkit/SKILL.md) — 在受支持的 Ascend EP 环境导出 Device 日志，并按权限查询或设置维测配置。
  `CANNBot` `CANN` `msnpureport` `执行需 NPU` · [条目](catalog/skills/msnpureport-toolkit.yaml)
- [torch-npugraph-ex-dfx-triage](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/graph/torch-npugraph-ex-dfx-triage/SKILL.md) — 收集分层日志并将 npugraph_ex 问题路由到编译、运行时、精度或性能诊断。
  `CANNBot` `PyTorch` `npugraph_ex` `设备取决于检查项` `流程编排` · [条目](catalog/skills/torch-npugraph-ex-dfx-triage.yaml)
- [vllm-ascend-distributed-debug](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-distributed-debug/SKILL.md) — 根据拓扑和逐 rank 证据定位启动、collective、端点与卡死问题。
  `vLLM Ascend` `HCCL` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-distributed-debug.yaml)
- [vllm-ascend-graph-debug](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-graph-debug/SKILL.md) — 通过受控实验和中间快照定位图捕获、回放及 eager/graph 分歧。
  `vLLM Ascend` `Graph` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-graph-debug.yaml)

<a id="delivery"></a>

### 工程交付与运行维护

将变更映射到构建、正确性和性能验证，记录覆盖范围。

- [ascendc-code-review](https://gitcode.com/cann/cannbot-skills/blob/393564ae43f304426db2c206e361cd43b2811413/ops/ascendc-code-review/SKILL.md) — 按文件、PR 或定向问题路由 Ascend C 代码检视，检查规范与设计一致性。
  `CANNBot` `Ascend C` `主机工具` · [条目](catalog/skills/ascendc-code-review.yaml)
- [vllm-ascend-change-validation](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-change-validation/SKILL.md) — 根据 baseline/candidate 差异确定构建、正确性与性能检查，报告通过项及覆盖缺口。
  `vLLM Ascend` `设备取决于检查项` · [条目](catalog/skills/vllm-ascend-change-validation.yaml)

<!-- CATALOG:END -->

## 社区贡献

你可以通过以下方式完善这份共享清单：

- **建议新技能**：分享你或团队在 Ascend 推理工程中使用的技能，说明其用途、输入与产出；
- **修正与反馈**：若发现条目元数据有误、依赖变更或链接失效，欢迎提交 Issue 或修正 PR；
- **引入新来源项目**：推荐公开可访问、许可清晰的技能仓库与工作流集合；
- **补充运行复现记录**：按技能的执行条件运行用例，分享软件与设备环境、输入、结果和日志。

各来源的条目采用统一的收录标准。提交方式、元数据要求及维护命令见[贡献指南](CONTRIBUTING.zh.md)。

## 相关资源

- [vLLM Ascend Skills](https://github.com/pisceskkk/vllm-ascend-skills) — 上游技能源（vLLM Ascend 服务化部署、性能评测与 Triton 优化）。
- [CANNBot Skills](https://gitcode.com/cann/cannbot-skills) — 上游技能源（CANN 环境配置、模型适配优化与多路线算子开发）。
- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) — 社区通用智能体技能索引参考。
- [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md) — 社区精选清单指导原则。
- [品牌资产说明](assets/brand.zh.md) — 标识素材与展示规范。

## 许可证

本清单内容、维护脚本与原创视觉素材采用 [CC0-1.0](LICENSE)。所链接技能保留各自许可证，详见[来源记录](catalog/sources.yaml)。
