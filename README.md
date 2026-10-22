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

## Triton 与 AscendC 算子专题

已按规格建模、设计流水、编码迁移、测试精度、Review 交付、性能优化和横向知识支持整理专题。当前专题含 **264 份不同定义、271 个目录条目**，其中 58 份为知识、示例或案例。不同来源的同名变体保留固定版本和完整目录。

[专题分类与使用说明](docs/operator-skills.md) · [机器可读统计](catalog/topics/operator-skills-2026-10-22.json) · [条目表 CSV](catalog/topics/operator-skills-2026-10-22.csv)

## 技能目录

目录按主要任务分类，条目展示技术栈、执行条件与元数据入口。定义审阅核对固定版本的技能说明与声明用途；运行复现按具体环境和用例记录，覆盖数量见下方统计。

执行条件标签含义如下：

- `执行需 NPU`：完整工作流需在昇腾 NPU 设备上运行（阅读分析与方案设计可在本地进行）；
- `离线分析`：基于已有 Profiling 或诊断产物进行离线分析，需安装对应主机脚本依赖；
- `主机工具`：运行代码检查、设计规划或 CANN Simulator 模拟等主机侧工具；
- `设备取决于检查项`：所需运行环境取决于用户选择的验证用例。

审阅范围、复现案例及其证据见各条目记录。字段与判定规则见[条目格式](docs/catalog-format.zh.md)和[验证规则](docs/validation-policy.zh.md)。

<!-- CATALOG:START -->

305 个技能 · 10 个分类

定义已审阅：305 · 已有运行复现记录：0。具体范围见各条目记录。

| 来源项目 | 已收录 | 维护者 | 许可证 |
|---|---|---|---|
| [vllm-ascend-skills](https://github.com/pisceskkk/vllm-ascend-skills) | 17 | pisceskkk | MIT |
| [cannbot-skills](https://gitcode.com/cann/cannbot-skills) | 78 | CANNBot SIG (cann) | CANN Open Software License v2.0 |
| [cannbot](https://gitcode.com/cann/cannbot) | 53 | CANNBot SIG (cann) | CANN Open Software License v2.0; CAKE plugin also includes Apache-2.0 |
| [cannbot-knowledge](https://gitcode.com/cann/cannbot-knowledge) | 7 | CANNBot SIG (cann) | CANN Open Software License v2.0 |
| [ascendc-skills](https://gitcode.com/ascendc-agent/ascendc-skills) | 31 | ascendc-agent | Not declared in the pinned repository root |
| [ascend-agent-skills](https://gitcode.com/Ascend/agent-skills) | 23 | Ascend community | Apache-2.0 (code/configuration) AND CC-BY-SA-4.0 (documentation); incorporated sources retain their terms |
| [akg](https://github.com/mindspore-ai/akg) | 49 | MindSpore AKG maintainers | Apache-2.0 |
| [hive](https://github.com/KernelHive/ascendc-skill) | 4 | KernelHive | Not declared in the pinned repository root; bundled references retain their terms |
| [model-agent](https://gitcode.com/Ascend/model-agent) | 22 | Ascend community | BSD-3-Clause; incorporated skills retain their upstream terms |
| [opgen](https://github.com/Just-it/AscendOpGenAgent) | 11 | Just-it | Apache-2.0 |
| [awesome](https://github.com/ascend-ai-coding/awesome-ascend-skills) | 4 | ascend-ai-coding | Not declared in the pinned repository root; synchronized sources retain their terms |
| [mindiesd](https://github.com/Ascend/MindIE-SD) | 2 | Ascend MindIE-SD maintainers | MulanPSL-2.0 |
| [asc-devkit](https://gitcode.com/cann/asc-devkit) | 4 | CANN AscendC maintainers | CANN Open Software License v2.0 |

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

- [ascendc-env-check](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-env-check/SKILL.md) — 检查 NPU 设备、CANN 配置、工具链依赖和实际架构。
  `CANNBot` `Ascend C` `Implementation and migration` `执行需 NPU` · [条目](catalog/skills/ascendc-env-check.yaml)
- [cann-env-setup](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/cann-env-setup/SKILL.md) — 准备昇腾算子开发所需的 CANN 安装和环境配置。
  `CANNBot` `Operator support` `Implementation and migration` `执行需 NPU` · [条目](catalog/skills/cann-env-setup.yaml)
- [repo-env-check](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-env-check/SKILL.md) — 检查选定 Python/CANN 环境并记录对应环境证据。
  `CANNBot` `Ascend C` `Implementation and migration` `执行需 NPU` · [条目](catalog/skills/repo-env-check.yaml)
- [triton-operator-env-config](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-env-config/SKILL.md) — 验证 CANN、Python、PyTorch、torch_npu 和 Triton-Ascend 开发环境。
  `Model Agent` `Triton` `Implementation and migration` `执行需 NPU` · [条目](catalog/skills/triton-operator-env-config.yaml)

<a id="model-integration"></a>

### 模型接入与转换

接入模型、转换权重，并核对配置与输入输出。

- [model-infer-migrator](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-migrator/SKILL.md) — 将 HF 模型或本地代码适配到 cann-recipes-infer 或独立 Runner，建立 eager 推理基线。
  `CANNBot` `PyTorch` `cann-recipes-infer` `执行需 NPU` · [条目](catalog/skills/model-infer-migrator.yaml)

<a id="serving"></a>

### 服务部署与扩展

部署共置或 PD 分离服务，验证拓扑、端点与请求。

- [model-infer-parallel-analysis](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-parallel-analysis/SKILL.md) — 根据模型结构与 Atlas A2/A3 规格分析并行策略，输出 parallel_config 候选和定量依据。
  `CANNBot` `PyTorch` `Parallelism` `主机工具` · [条目](catalog/skills/model-infer-parallel-analysis.yaml)
- [model-infer-parallel-impl](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-parallel-impl/SKILL.md) — 按确认的 TP/EP 配置改造并行层、通信组、权重和启动配置，并验证模型运行。
  `CANNBot` `PyTorch` `HCCL` `执行需 NPU` · [条目](catalog/skills/model-infer-parallel-impl.yaml)
- [vllm-ascend-pd-serving](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-pd-serving/SKILL.md) — 部署 Prefill/Decode 分离服务，验证连接器、角色启动顺序与 KV 传输。
  `vLLM Ascend` `PD` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-pd-serving.yaml)
- [vllm-ascend-serving](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-serving/SKILL.md) — 完成共置服务的版本配对、设备选择、启动、健康检查与清理。
  `vLLM Ascend` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-serving.yaml)

<a id="correctness"></a>

### 正确性与精度

固定参考与用例矩阵，比较输出、误差和任务质量。

- [aog-input-gen-builder](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-input-gen-builder/SKILL.md) — 从 AscendC 源包或可微标杆生成常规与边界输入数据。
  `CANNBot` `Ascend C` `Testing and numerical validation` `Community` `执行需 NPU` · [条目](catalog/skills/aog-input-gen-builder.yaml)
- [api-perf-test](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/docs/skill_3510_api_perf_test/SKILL.md) — 构建运行 DAV_3510 API 性能用例并分析采集结果。
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/api-perf-test.yaml)
- [api-ut](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/api-ut/SKILL.md) — 生成 AscendC API 单测并依据覆盖率报告补齐用例。
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `设备取决于检查项` · [条目](catalog/skills/api-ut.yaml)
- [asc-api-test](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/docs/asc-api-test/SKILL.md) — 生成 AscendC API 测试样例及数据、校验资产。
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/asc-api-test.yaml)
- [asc-api-ut-gen](https://gitcode.com/cann/asc-devkit/blob/cd10a15efc6d2221814f6167e5055c7e640ccc7c/.agent/skills/asc-api-ut-gen/SKILL.md) — 依据结构化架构约束生成 DevKit API gtest，并按覆盖率补齐用例。
  `Ascend DevKit` `Ascend C` `Testing and numerical validation` `设备取决于检查项` · [条目](catalog/skills/asc-api-ut-gen.yaml)
- [ascendc-evaluation](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/ascendc-evaluation/SKILL.md) — 验证 AscendC 多用例数值正确性并采集性能证据。
  `CANNBot` `Ascend C` `Testing and numerical validation` `Community` `执行需 NPU` · [条目](catalog/skills/ascendc-evaluation.yaml)
- [ascendc-operator-precision-eval](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-precision-eval/SKILL.md) — 生成 Shape、dtype 和边界精度用例并输出数值对比报告。
  `Ascend Agent Skills` `Ascend C` `Testing and numerical validation` `Community` `执行需 NPU` · [条目](catalog/skills/ascendc-operator-precision-eval.yaml)
- [ascendc-operator-st-gen](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-st-gen/SKILL.md) — 创建修复 CANN 算子的 ATK ST 双标杆精度验证工程。
  `Ascend Agent Skills` `Ascend C` `Testing and numerical validation` `Community` `执行需 NPU` · [条目](catalog/skills/ascendc-operator-st-gen.yaml)
- [ascendc-operator-testcase-gen](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-testcase-gen/SKILL.md) — 生成供精度和性能评估复用的算子用例规格及 Golden 契约。
  `Ascend Agent Skills` `Ascend C` `Testing and numerical validation` `Community` `执行需 NPU` · [条目](catalog/skills/ascendc-operator-testcase-gen.yaml)
- [ascendc-ops-evaluation](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/ascendc-ops-evaluation/SKILL.md) — 构建部署 CANN 算子仓实现，对比基线与进化版本的精度和性能。
  `CANNBot` `Ascend C` `Testing and numerical validation` `Community` `执行需 NPU` · [条目](catalog/skills/ascendc-ops-evaluation.yaml)
- [ascendc-whitebox-design](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-whitebox-design/SKILL.md) — 提取 Tiling/Kernel 路径并生成带覆盖检查的可执行白盒用例矩阵。
  `CANNBot` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/ascendc-whitebox-design.yaml)
- [blackbox-tester](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/blackbox-tester/SKILL.md) — 针对已部署候选全量执行 TTK ACLNN 黑盒套件并核对结果数量。
  `CANNBot` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/blackbox-tester.yaml)
- [kernel-verifier](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/triton/kernel-verifier/SKILL.md) — 检查 Triton 实现结构、执行 Golden 比对并测量通过候选。
  `AscendOpGenAgent` `Triton` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/kernel-verifier.yaml)
- [model-agent-ascendc-operator-precision-eval](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-precision-eval/SKILL.md) — 生成 Shape、dtype 和边界精度用例并输出数值对比报告。
  `Model Agent` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/model-agent-ascendc-operator-precision-eval.yaml)
- [model-agent-ascendc-operator-testcase-gen](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-testcase-gen/SKILL.md) — 生成供精度和性能评估复用的算子用例规格及 Golden 契约。
  `Model Agent` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/model-agent-ascendc-operator-testcase-gen.yaml)
- [operator-test](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/ut-gen/SKILL.md) — 以 optest 计划描述 AscendC 用例，执行数据生成、调用与校验。
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/operator-test.yaml)
- [remote-npu-test](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/remote-npu-test/SKILL.md) — 通过仓内远程执行器运行独立测试并回收结构化证据。
  `AscendC Agent` `Operator support` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/remote-npu-test.yaml)
- [repo-test-develop](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-test-develop/SKILL.md) — 组织 proto、Golden、用例资产，以 CANN Bench 执行黑盒、白盒和回归评测。
  `CANNBot` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/repo-test-develop.yaml)
- [simt-stc-doc](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/simt-stc-doc/SKILL.md) — 依据已确认需求创建 SIMT 测试用例和缺陷记录模板。
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/simt-stc-doc.yaml)
- [single-api-test](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/docs/skill_3510_single_api_test/SKILL.md) — 生成执行单个 DAV_3510 API 验证用例。
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/single-api-test.yaml)
- [st-verifier](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/st-verifier/SKILL.md) — 独立检查 ST 覆盖、设计一致性、框架集成和执行证据。
  `CANNBot` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/st-verifier.yaml)
- [tilelang2ascend-precision-tuning](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/tilelang2ascend-precision-tuning/SKILL.md) — 通过 DumpTensor 和分段对比定位修复 AscendC 精度问题。
  `CANNBot` `Ascend C` `Testing and numerical validation` `Community` `执行需 NPU` · [条目](catalog/skills/tilelang2ascend-precision-tuning.yaml)
- [tiling-exception-coverage](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/tiling-exception-coverage/SKILL.md) — 为 Tiling UT 设计带明确失败或降级断言的负向用例。
  `CANNBot` `Ascend C` `Testing and numerical validation` `主机工具` · [条目](catalog/skills/tiling-exception-coverage.yaml)
- [tiling-ut-harness](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/tiling-ut-harness/SKILL.md) — 使用指定平台 Mock 和已安装 Host 库构建运行 TilingFunc gtest。
  `CANNBot` `Ascend C` `Testing and numerical validation` `主机工具` · [条目](catalog/skills/tiling-ut-harness.yaml)
- [triton-op-verifier](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-op-verifier/SKILL.md) — 检查 Triton 实现真实性、执行 Golden 比对并采集性能结果。
  `CANNBot` `Triton` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/triton-op-verifier.yaml)
- [triton-operator-precision-eval](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-precision-eval/SKILL.md) — 对比 Triton 与 PyTorch 实现并生成数值误差报告。
  `Model Agent` `Triton` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/triton-operator-precision-eval.yaml)
- [vllm-ascend-correctness-validation](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-correctness-validation/SKILL.md) — 设计确定性用例，比较代码版本、执行模式与 API 路径的输出。
  `vLLM Ascend` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-correctness-validation.yaml)

<a id="benchmarking"></a>

### 性能评测与回归

通过预热、重复测量和受控对比评估吞吐与延迟。

- [aog-perf-eval](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-perf-eval/SKILL.md) — 以 Profiler 和墙钟两种方式评估生成的 AscendC 算子。
  `CANNBot` `Ascend C` `Profiling and optimization` `Community` `执行需 NPU` · [条目](catalog/skills/aog-perf-eval.yaml)
- [ascendc-operator-performance-eval](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-performance-eval/SKILL.md) — 使用 Profiler 用例和对比报告评估 AscendC 实现与标杆性能。
  `Ascend Agent Skills` `Ascend C` `Profiling and optimization` `Community` `执行需 NPU` · [条目](catalog/skills/ascendc-operator-performance-eval.yaml)
- [model-agent-ascendc-operator-performance-eval](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-performance-eval/SKILL.md) — 使用 Profiler 用例和对比报告评估 AscendC 实现与标杆性能。
  `Model Agent` `Ascend C` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/model-agent-ascendc-operator-performance-eval.yaml)
- [triton-operator-performance-eval](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-performance-eval/SKILL.md) — 使用 msprof 测量 Triton-Ascend 时延和利用率并报告瓶颈。
  `Model Agent` `Triton` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/triton-operator-performance-eval.yaml)
- [vllm-ascend-benchmark](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-benchmark/SKILL.md) — 对一个代码状态进行预热与重复测量，输出归一化吞吐和延迟指标。
  `vLLM Ascend` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-benchmark.yaml)
- [vllm-ascend-performance-regression](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-performance-regression/SKILL.md) — 交替运行基线与候选版本，在相同负载下比较性能变化与波动。
  `vLLM Ascend` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-performance-regression.yaml)

<a id="profiling"></a>

### Profiling 与瓶颈分析

采集或分析 trace、逐 rank 行为与 HBM 占用，保留证据。

- [ascend-profiling-analysis](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-profiling-analysis/SKILL.md) — 分析 rank、step、layer、block、算子及跨 rank 行为，输出可追溯的瓶颈证据。
  `Ascend` `Profiling` `离线分析` · [条目](catalog/skills/ascend-profiling-analysis.yaml)
- [ge-memory-analysis](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/graph/ge-memory-analysis/SKILL.md) — 分诊 GE Device 显存、Host 泄漏及算子地址问题，结合日志和报告进行内存归因。
  `CANNBot` `GE` `HBM` `设备取决于检查项` · [条目](catalog/skills/ge-memory-analysis.yaml)
- [model-infer-perf-breakdown](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-perf-breakdown/SKILL.md) — 将 kernel_details.csv 与 trace 按模型组件拆解，生成耗时、空隙和异常层 HTML 报告。
  `CANNBot` `Ascend` `Profiling` `离线分析` · [条目](catalog/skills/model-infer-perf-breakdown.yaml)
- [model-infer-profiling](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-profiling/SKILL.md) — 通过框架内置或注入式 torch_npu.profiler 采集模型性能数据，并检查输出完整性。
  `CANNBot` `PyTorch` `torch_npu` `执行需 NPU` · [条目](catalog/skills/model-infer-profiling.yaml)
- [msot-msopprof-operator-profiler](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/official/MindStudio/skills/msot-msopprof-operator-profiler/SKILL.md) — 选择上板或仿真采集方式，解释 msOpProf 指标、时间线和瓶颈。
  `Ascend Agent Skills` `Operator support` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/msot-msopprof-operator-profiler.yaml)
- [op-mfu-calculator](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/official/MindStudio/skills/op-mfu-calculator/SKILL.md) — 依据 Shape、耗时、dtype 和硬件峰值计算算子利用率。
  `Ascend Agent Skills` `Operator support` `Profiling and optimization` `离线分析` · [条目](catalog/skills/op-mfu-calculator.yaml)
- [ops-profiling](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ops-profiling/SKILL.md) — 采集可比较的算子时延和硬件指标，输出逐 Kernel 瓶颈分析。
  `CANNBot` `Operator support` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/ops-profiling.yaml)
- [performance-analyzer](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/ascendc/performance-analyzer/SKILL.md) — 采集对比 AscendC Kernel 性能并定位优化方向。
  `AscendOpGenAgent` `Ascend C` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/performance-analyzer.yaml)
- [performance-summary](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/performance-summary/SKILL.md) — 汇总不同用例的 Kernel 评测结果和优化观察。
  `AKG` `Operator support` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/performance-summary.yaml)
- [triton-mfu-analyzer](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-mfu-analyzer/SKILL.md) — 按 dtype 校准峰值，测量算子利用率并拆解逐 Kernel 时延。
  `CANNBot` `Triton` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/triton-mfu-analyzer.yaml)
- [triton-simulator-optimizer](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-simulator-optimizer/SKILL.md) — 采集仿真指令和流水证据，将瓶颈映射到优化动作。
  `CANNBot` `Triton` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/triton-simulator-optimizer.yaml)
- [vllm-ascend-memory-profiling](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-memory-profiling/SKILL.md) — 将服务 HBM 占用归因到权重、KV cache、HCCL、激活与运行时，并说明残差。
  `vLLM Ascend` `HBM` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-memory-profiling.yaml)
- [vllm-ascend-profiling-collection](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-profiling-collection/SKILL.md) — 采集指定负载窗口的 torch-profiler 数据，检查请求成功与逐 rank 输出完整性。
  `vLLM Ascend` `torch-profiler` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-profiling-collection.yaml)

<a id="optimization"></a>

### 推理优化

优化执行、调度和资源重叠，并配对验证正确性与收益。

- [ascend-model-multistream-overlap-skill](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-model-multistream-overlap-skill/SKILL.md) — 从源码与 trace 构建资源约束 DAG，设计多流重叠并配对验证收益。
  `Ascend` `Multistream` `执行需 NPU` · [条目](catalog/skills/ascend-model-multistream-overlap-skill.yaml)
- [ge-fusion-pass-skill](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/graph/ge-fusion-pass-skill/SKILL.md) — 串联 GE 自定义融合 pass 的需求分析、实现与功能验证，交付阶段证据。
  `CANNBot` `GE` `CANN` `设备取决于检查项` `流程编排` · [条目](catalog/skills/ge-fusion-pass-skill.yaml)
- [model-infer-fusion](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-fusion/SKILL.md) — 匹配 PyTorch 模型中的计算模式与 torch_npu 融合算子，实施替换并验证。
  `CANNBot` `PyTorch` `torch_npu` `执行需 NPU` · [条目](catalog/skills/model-infer-fusion.yaml)
- [model-infer-graph-mode](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-graph-mode/SKILL.md) — 适配模型 Decode 路径的 npugraph_ex 或 GE 图模式，处理图中断并验证结果。
  `CANNBot` `PyTorch` `Graph` `执行需 NPU` · [条目](catalog/skills/model-infer-graph-mode.yaml)
- [model-infer-kvcache](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-kvcache/SKILL.md) — 选择并改造连续缓存、Paged Attention、MLA 或滑窗 KV cache，衔接 FA 算子并验证。
  `CANNBot` `PyTorch` `KV cache` `执行需 NPU` · [条目](catalog/skills/model-infer-kvcache.yaml)
- [model-infer-multi-stream](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-multi-stream/SKILL.md) — 提供模型 DAG 拆解、多流 API 选择、同步与控核规则，用于方案设计和重叠验证。
  `CANNBot` `PyTorch` `Multistream` `设备取决于检查项` · [条目](catalog/skills/model-infer-multi-stream.yaml)
- [model-infer-prefetch](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-prefetch/SKILL.md) — 针对已确认的 memory-bound 热点设计权重预取窗口，接入 npu_prefetch 并测量收益。
  `CANNBot` `torch_npu` `Prefetch` `执行需 NPU` · [条目](catalog/skills/model-infer-prefetch.yaml)
- [model-infer-quantization](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-quantization/SKILL.md) — 接入已有 compressed-tensors 量化权重，检查产物契约、运行时映射、真实生效与收益。
  `CANNBot` `PyTorch` `compressed-tensors` `执行需 NPU` · [条目](catalog/skills/model-infer-quantization.yaml)

<a id="operators"></a>

### 算子开发与迁移

串联算子实现、用例验证和逐 shape 性能优化。

- [aiss-tiling-solver](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/aiss-tiling-solver/SKILL.md) — 构造 AISS-TilingSolver 输入、求解 Tiling 参数并解释结果。
  `CANNBot` `Ascend C` `Design and pipelines` `主机工具` · [条目](catalog/skills/aiss-tiling-solver.yaml)
- [aog-a3-author](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-a3-author/SKILL.md) — 为跨代迁移生成源架构标杆运行器和输入清单。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/aog-a3-author.yaml)
- [aog-knowledge-maintain](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-knowledge-maintain/SKILL.md) — 将运行发现与知识库去重并准备带来源的知识摄入。
  `CANNBot` `Ascend C` `Knowledge and cases` `Community` `主机工具` · [条目](catalog/skills/aog-knowledge-maintain.yaml)
- [aog-op-classify](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-op-classify/SKILL.md) — 分类源算子，输出结构化结果和相关知识建议。
  `CANNBot` `Ascend C` `Specification and modeling` `Community` `主机工具` · [条目](catalog/skills/aog-op-classify.yaml)
- [aog-prior-art-verify](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-prior-art-verify/SKILL.md) — 查找已有目标架构迁移候选，核对来源并构建测量。
  `CANNBot` `Ascend C` `Design and pipelines` `Community` `主机工具` · [条目](catalog/skills/aog-prior-art-verify.yaml)
- [api-example](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/api-example/SKILL.md) — 创建包含 Host/Kernel、构建配置和运行脚本的 AscendC API 示例。
  `AscendC Agent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/api-example.yaml)
- [api-gen](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/api-gen/SKILL.md) — 依据设计文档实现 AscendC API 并验证代码变更。
  `AscendC Agent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/api-gen.yaml)
- [asc-ar-dev](https://gitcode.com/cann/asc-devkit/blob/cd10a15efc6d2221814f6167e5055c7e640ccc7c/.agent/skills/asc-ar-dev/SKILL.md) — 分析 AscendC 需求、核对 API、实现评审代码并规划构建、仿真与上板验证。
  `Ascend DevKit` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/asc-ar-dev.yaml)
- [asc-npu-arch](https://gitcode.com/cann/asc-devkit/blob/cd10a15efc6d2221814f6167e5055c7e640ccc7c/.agent/skills/asc-npu-arch/SKILL.md) — 确认 DevKit 芯片名、架构宏、SocVersion、dtype 和 API 支持事实。
  `Ascend DevKit` `Ascend C` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/asc-npu-arch.yaml)
- [asc-perf-tuning](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/asc-perf-tuning/SKILL.md) — 在支持架构上完成 AscendC 采集、诊断、优化、精度验证和性能对比。
  `AscendC Agent` `Ascend C` `Profiling and optimization` `执行需 NPU` `流程编排` · [条目](catalog/skills/asc-perf-tuning.yaml)
- [asc-search](https://gitcode.com/cann/asc-devkit/blob/cd10a15efc6d2221814f6167e5055c7e640ccc7c/.agent/skills/asc-search/SKILL.md) — 建立查询 AscendC C API 文档索引，按需求定位资料。
  `Ascend DevKit` `Ascend C` `Knowledge and cases` `主机工具` · [条目](catalog/skills/asc-search.yaml)
- [ascend-agent-skills-ascendc-operator-performance-optim](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/official/MindStudio/skills/ascendc-operator-performance-optim/SKILL.md) — 使用 msprof op 构建采集 AscendC 算子，修改代码并重新采集对比。
  `Ascend Agent Skills` `Ascend C` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/ascend-agent-skills-ascendc-operator-performance-optim.yaml)
- [ascend-call-generation](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/ascend-call-generation/SKILL.md) — 从函数式 PyTorch 生成 AscendC 工程、Host、pybind 和 Kernel 骨架。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/ascend-call-generation.yaml)
- [ascend-doc-auto-updater](https://github.com/KernelHive/ascendc-skill/blob/c78f267d0423d59a51a02070e5bb845fde2dbd69/skills/ascend-doc-update/SKILL.md) — 依据源码和接口变更更新昇腾算子技术文档。
  `KernelHive` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascend-doc-auto-updater.yaml)
- [ascend-kernel-generator](https://github.com/KernelHive/ascendc-skill/blob/c78f267d0423d59a51a02070e5bb845fde2dbd69/skills/ascend-kernel-generator/SKILL.md) — 生成 AscendC Kernel，验证编译、精度、性能并归档通过实现。
  `KernelHive` `Ascend C` `Implementation and migration` `执行需 NPU` `流程编排` · [条目](catalog/skills/ascend-kernel-generator.yaml)
- [ascend-operator-guide](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/usability/op-gen/ascend-operator-guide/SKILL.md) — 按 AscendC 算子类别导航到所需概念、文档和优化方法。
  `AscendC Agent` `Ascend C` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/ascend-operator-guide.yaml)
- [ascend-opplugin](https://github.com/ascend-ai-coding/awesome-ascend-skills/blob/75ec89ce9d401be8ac95980e1c3f42f8d4315057/skills/ops/ascend-opplugin/SKILL.md) — 按分发和算子契约实现测试昇腾 PyTorch op-plugin 绑定。
  `Awesome Ascend Skills` `Operator support` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascend-opplugin.yaml)
- [ascend-triton-kernel-optimization](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-kernel-optimization/SKILL.md) — 对正确性通过的内核进行逐 shape 测量，结合 profiler 迭代优化。
  `Ascend` `Triton` `执行需 NPU` · [条目](catalog/skills/ascend-triton-kernel-optimization.yaml)
- [ascend-triton-kernel-validation](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-kernel-validation/SKILL.md) — 按 shape、dtype、layout 和 stride 矩阵验证候选与参考，检查执行路径和 fallback。
  `Ascend` `Triton` `执行需 NPU` · [条目](catalog/skills/ascend-triton-kernel-validation.yaml)
- [ascend-triton-operator-development](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-operator-development/SKILL.md) — 从 PyTorch 参考或 GPU Triton 实现开发首个 Ascend Triton 算子候选。
  `Ascend` `Triton` `执行需 NPU` · [条目](catalog/skills/ascend-triton-operator-development.yaml)
- [ascend-triton-workflow](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-triton-workflow/SKILL.md) — 协调 Triton 算子开发、正确性验证与性能优化，衔接各阶段证据。
  `Ascend` `Triton` `执行需 NPU` `流程编排` · [条目](catalog/skills/ascend-triton-workflow.yaml)
- [ascendc-api-best-practices](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-api-best-practices/SKILL.md) — 查询 AscendC 计算、归约、搬运、Buffer、转换和通信 API 的正确用法。
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/ascendc-api-best-practices.yaml)
- [ascendc-api-knowledge-query](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/ascendc-api-knowledge-query/SKILL.md) — 检索匹配平台的 AscendC API 知识卡并追溯源码和头文件。
  `CANNBot Knowledge` `Ascend C` `Knowledge and cases` `主机工具` · [条目](catalog/skills/ascendc-api-knowledge-query.yaml)
- [ascendc-ar-develop](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/ascendc-ar-develop/SKILL.md) — 分析 AscendC 需求、实现评审 Host/Device 代码并规划验证。
  `AscendC Agent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascendc-ar-develop.yaml)
- [ascendc-backward-gen](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/ascendc-backward-gen/SKILL.md) — 从可微 PyTorch 正向标杆生成 AscendC 反向算子并上板验证。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `执行需 NPU` `流程编排` · [条目](catalog/skills/ascendc-backward-gen.yaml)
- [ascendc-blaze-best-practice](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-blaze-best-practice/SKILL.md) — 为 Ascend950 DAV_3510 选择 Blaze/Tensor API 模板并实现 MatMul 系列算子。
  `CANNBot` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascendc-blaze-best-practice.yaml)
- [ascendc-blaze-migration](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-blaze-migration/SKILL.md) — 按固定契约将 Ascend950 Kernel 分支迁移到 Blaze/Tensor API，并配对验证。
  `CANNBot` `Ascend C` `Implementation and migration` `执行需 NPU` `流程编排` · [条目](catalog/skills/ascendc-blaze-migration.yaml)
- [ascendc-build-system](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/ascendc-build-system/SKILL.md) — 检查修复 AscendC Host/Kernel 构建及代码生成链路。
  `CANNBot` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascendc-build-system.yaml)
- [ascendc-cross-gen-migration](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-cross-gen-migration/SKILL.md) — 完成 AscendC 算子 A2/A3 到 A5 的架构改造及精度、性能验证。
  `CANNBot` `Ascend C` `Implementation and migration` `执行需 NPU` `流程编排` · [条目](catalog/skills/ascendc-cross-gen-migration.yaml)
- [ascendc-cross-gen-port](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/ascendc-cross-gen-port/SKILL.md) — 按明确源、目标架构迁移 AscendC 算子并对照标杆验证。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `执行需 NPU` `流程编排` · [条目](catalog/skills/ascendc-cross-gen-port.yaml)
- [ascendc-design-doc](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/ascendc-design-doc/SKILL.md) — 结合源码和 API 约束编写 AscendC 详设及测试计划。
  `AscendC Agent` `Ascend C` `Design and pipelines` `主机工具` · [条目](catalog/skills/ascendc-design-doc.yaml)
- [ascendc-direct-invoke-template](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-direct-invoke-template/SKILL.md) — 选择完整的 Vector、Blaze MatMul 或 Kirin 核函数直调工程模板。
  `CANNBot` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascendc-direct-invoke-template.yaml)
- [ascendc-direct-invoke-to-registry-invoke](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-direct-invoke-to-registry-invoke/SKILL.md) — 将现有核函数直调工程转换为 ACLNN/GEIR 注册调用算子。
  `CANNBot` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascendc-direct-invoke-to-registry-invoke.yaml)
- [ascendc-docs-search](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-docs-search/SKILL.md) — 通过本地索引和在线来源查找 AscendC API、样例及兼容性资料。
  `CANNBot` `Ascend C` `Knowledge and cases` `主机工具` · [条目](catalog/skills/ascendc-docs-search.yaml)
- [ascendc-evolution-knowledge](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/ascendc-evolution-knowledge/SKILL.md) — 检索 AscendC 架构、API 陷阱、优化模式和已验证的进化经验。
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `Community` `主机工具` · [条目](catalog/skills/ascendc-evolution-knowledge.yaml)
- [ascendc-evolution-strategies](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/ascendc-evolution-strategies/SKILL.md) — 按瓶颈和算子族检索 AscendC 优化策略并检查组合兼容性。
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `Community` `主机工具` · [条目](catalog/skills/ascendc-evolution-strategies.yaml)
- [ascendc-evolution-world-model](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/ascendc-evolution-world-model/SKILL.md) — 维护基于证据的决策树，选择和验证 AscendC 优化实验。
  `CANNBot` `Ascend C` `Profiling and optimization` `Community` `执行需 NPU` · [条目](catalog/skills/ascendc-evolution-world-model.yaml)
- [ascendc-mc2-best-practice](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-mc2-best-practice/SKILL.md) — 设计调试多卡 AscendC 通算融合及其内存、同步契约。
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/ascendc-mc2-best-practice.yaml)
- [ascendc-operator-a5-migration](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/official/Common/ascendc-operator-A5-migration/SKILL.md) — 分基础适配、RegBase 和 SIMT 阶段将 AscendC 算子迁移到 A5。
  `Ascend Agent Skills` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascendc-operator-a5-migration.yaml)
- [ascendc-operator-code-gen](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-code-gen/SKILL.md) — 生成 AscendC Host/Kernel 代码、注册 PyTorch 并衔接构建测试。
  `Ascend Agent Skills` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/ascendc-operator-code-gen.yaml)
- [ascendc-operator-design](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-design/SKILL.md) — 设计算子接口、两级 Tiling、UB 分配和 Kernel 计算逻辑。
  `Ascend Agent Skills` `Ascend C` `Design and pipelines` `Community` `主机工具` · [条目](catalog/skills/ascendc-operator-design.yaml)
- [ascendc-operator-dev](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-dev/SKILL.md) — 组织 AscendC 自定义算子的工程初始化、设计、用例、实现和评估。
  `Ascend Agent Skills` `Ascend C` `Implementation and migration` `Community` `执行需 NPU` `流程编排` · [条目](catalog/skills/ascendc-operator-dev.yaml)
- [ascendc-operator-develop-workflow](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/usability/op-gen/ascendc-operator-develop-workflow/SKILL.md) — 组织 AscendC 设计、实现、构建测试、问题修复、总结和文档。
  `AscendC Agent` `Ascend C` `Implementation and migration` `执行需 NPU` `流程编排` · [条目](catalog/skills/ascendc-operator-develop-workflow.yaml)
- [ascendc-operator-performance-optim](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-performance-optim/SKILL.md) — 依据实测瓶颈修改 AscendC 代码，并复核精度及相对基线性能。
  `Ascend Agent Skills` `Ascend C` `Profiling and optimization` `Community` `执行需 NPU` · [条目](catalog/skills/ascendc-operator-performance-optim.yaml)
- [ascendc-operator-project-init](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-project-init/SKILL.md) — 创建可构建的 AscendC 自定义算子工程并列出注册检查点。
  `Ascend Agent Skills` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/ascendc-operator-project-init.yaml)
- [ascendc-perf-optimize](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-perf-optimize/SKILL.md) — 结合 Tiling 模型和 Profiling 配平卡间、核间及核内流水。
  `CANNBot` `Ascend C` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/ascendc-perf-optimize.yaml)
- [ascendc-performance-best-practices](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-performance-best-practices/SKILL.md) — 按算子族检索优化方法、参考代码和平台流水约束。
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/ascendc-performance-best-practices.yaml)
- [ascendc-performance-optimization](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/usability/op-gen/ascendc-performance-optimization/SKILL.md) — 依据实测瓶颈选择 Tiling、双缓冲、内存和计算优化方案。
  `AscendC Agent` `Ascend C` `Profiling and optimization` `执行需 NPU` `流程编排` · [条目](catalog/skills/ascendc-performance-optimization.yaml)
- [ascendc-planning](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/design-gen/SKILL.md) — 规划 AscendC 语义、精度、Tiling、Buffer 和流水实现方案。
  `AscendC Agent` `Ascend C` `Design and pipelines` `主机工具` · [条目](catalog/skills/ascendc-planning.yaml)
- [ascendc-regbase-best-practice](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-regbase-best-practice/SKILL.md) — 查询 DAV_3510 RegBase API 约束、实现结构和参考算子。
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/ascendc-regbase-best-practice.yaml)
- [ascendc-regbase-sample-gen](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/ascendc-regbase-sample-gen/SKILL.md) — 按 DevKit 样例结构生成面向指定平台的 AscendC RegBase 工程。
  `AscendC Agent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascendc-regbase-sample-gen.yaml)
- [ascendc-registry-invoke-template](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-registry-invoke-template/SKILL.md) — 创建包含 Host/Kernel 代码和 UT/ST 样例的注册调用工程。
  `CANNBot` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascendc-registry-invoke-template.yaml)
- [ascendc-registry-invoke-to-direct-invoke](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-registry-invoke-to-direct-invoke/SKILL.md) — 抽取注册算子中的 Kernel 并转换为核函数直调形式。
  `CANNBot` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascendc-registry-invoke-to-direct-invoke.yaml)
- [ascendc-simt-best-practices](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-simt-best-practices/SKILL.md) — 查询 AscendC SIMT 线程排布、索引、搬运、同步和调试 API。
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/ascendc-simt-best-practices.yaml)
- [ascendc-simt-tiling-design](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-simt-tiling-design/SKILL.md) — 设计 SIMT 核与线程切分、内存分配、TilingKey 和 Workspace 契约。
  `CANNBot` `Ascend C` `Design and pipelines` `主机工具` · [条目](catalog/skills/ascendc-simt-tiling-design.yaml)
- [ascendc-st-design](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-st-design/SKILL.md) — 从 ACLNN 接口规格提取约束并生成 L0/L1/L2 系统测试用例。
  `CANNBot` `Ascend C` `Design and pipelines` `主机工具` · [条目](catalog/skills/ascendc-st-design.yaml)
- [ascendc-tiling-design](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-tiling-design/SKILL.md) — 按算子族设计多核与 UB 切分、Buffer 分配和分支覆盖。
  `CANNBot` `Ascend C` `Design and pipelines` `主机工具` · [条目](catalog/skills/ascendc-tiling-design.yaml)
- [ascendc-translator](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/ascendc/ascendc-translator/SKILL.md) — 将 TileLang 设计转为 AscendC Kernel 和 Python 绑定，并验证结果。
  `AscendOpGenAgent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascendc-translator.yaml)
- [ascendc-ut-develop](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-ut-develop/SKILL.md) — 生成补充 op_host、op_api、op_kernel 单测并补齐覆盖缺口。
  `CANNBot` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/ascendc-ut-develop.yaml)
- [ascendc](https://github.com/ascend-ai-coding/awesome-ascend-skills/blob/75ec89ce9d401be8ac95980e1c3f42f8d4315057/skills/ops/ascendc/SKILL.md) — 在 ascend-kernel 工程中组织设计、生成、构建、精度评估、采集与优化。
  `Awesome Ascend Skills` `Ascend C` `Implementation and migration` `执行需 NPU` `流程编排` · [条目](catalog/skills/ascendc.yaml)
- [ascendkerneloptimization](https://github.com/KernelHive/ascendc-skill/blob/c78f267d0423d59a51a02070e5bb845fde2dbd69/skills/ascend-kernel-optimization/SKILL.md) — 结合评测反馈分析并迭代优化 AscendC Kernel。
  `KernelHive` `Ascend C` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/ascendkerneloptimization.yaml)
- [benchmark-dev](https://github.com/Ascend/MindIE-SD/blob/d6f5ca90a882c73b25ace504ae9da254976f53c6/.agents/skills/benchmark-dev/SKILL.md) — 开发使用 MindIE-SD 微基准，对比真实算子实现并检测性能漂移。
  `MindIE-SD` `Operator support` `Implementation and migration` `执行需 NPU` · [条目](catalog/skills/benchmark-dev.yaml)
- [cake-docs-search](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/cake-docs-search/SKILL.md) — 为 CAKE 生成流程查找 AscendC API、样例和兼容性资料。
  `CANNBot` `Ascend C` `Knowledge and cases` `Community` `主机工具` · [条目](catalog/skills/cake-docs-search.yaml)
- [cake-evo](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/cake-evo/SKILL.md) — 以不同策略生成隔离的 AscendC 变体，依据实测选择候选。
  `CANNBot` `Ascend C` `Profiling and optimization` `Community` `执行需 NPU` `流程编排` · [条目](catalog/skills/cake-evo.yaml)
- [case-simplifier](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/ascendc/case-simplifier/SKILL.md) — 在保留声明覆盖维度的前提下选取更小的算子用例集。
  `AscendOpGenAgent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/case-simplifier.yaml)
- [catlass-op-develop](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/catlass-op-develop/SKILL.md) — 依据设计和 CATLASS 参考工程生成 Kernel、Device 调用、Params 与 Epilogue 实现。
  `CANNBot` `CATLASS` `设备取决于检查项` · [条目](catalog/skills/catlass-op-develop.yaml)
- [code-performance-advisor](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/code-performance-advisor/SKILL.md) — 结合专家规则和源码上下文诊断 AscendC 性能瓶颈。
  `CANNBot` `Ascend C` `Profiling and optimization` `Community` `离线分析` · [条目](catalog/skills/code-performance-advisor.yaml)
- [design-template](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/design-template/SKILL.md) — 将已核对算子事实填入指定 ACLNN 设计模板。
  `CANNBot` `Ascend C` `Design and pipelines` `主机工具` · [条目](catalog/skills/design-template.yaml)
- [dsl-baseline-generation-easyasc](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/dsl-baseline-generation-easyasc/SKILL.md) — 从函数式 PyTorch 生成 easyasc DSL 初版，供 AscendC 代码生成。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/dsl-baseline-generation-easyasc.yaml)
- [dsl-baseline-generation](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/dsl-baseline-generation/SKILL.md) — 从函数式 PyTorch 标杆生成 AscendDSL 计算和切分结构。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/dsl-baseline-generation.yaml)
- [dsl-easyasc-codegen](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/dsl-easyasc-codegen/SKILL.md) — 编写仿真 easyasc 算子，再生成原生 AscendC 代码。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/dsl-easyasc-codegen.yaml)
- [dsl-easyasc-post](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/dsl-easyasc-post/SKILL.md) — 将 easyasc 原生生成结果适配到 CAKE 算子工程布局。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/dsl-easyasc-post.yaml)
- [dsl-lowering](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/dsl-lowering/SKILL.md) — 通过多级 Pass 将算子 DSL 降为 AscendC，并定位编译失败。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/dsl-lowering.yaml)
- [dsl-optimization](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/dsl-optimization/SKILL.md) — 依据验证过的性能反馈调优 DSL 切分、向量化和流水结构。
  `CANNBot` `Ascend C` `Profiling and optimization` `Community` `执行需 NPU` · [条目](catalog/skills/dsl-optimization.yaml)
- [easyasc-codegen](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/easyasc-codegen/SKILL.md) — 从 easyasc DSL 生成构建 AscendC，并提供编译算子产物。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/easyasc-codegen.yaml)
- [easyasc-dsl-bridge](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/easyasc-dsl-bridge/SKILL.md) — 为 easyasc 生成的 AscendC Kernel 构建 torch_npu 绑定和 ModelNew 封装。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/easyasc-dsl-bridge.yaml)
- [example-sim-support](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/example-sim-support/SKILL.md) — 使 AscendC 样例支持 NPU、CPU 调试和仿真三种构建模式。
  `AscendC Agent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/example-sim-support.yaml)
- [functional-conversion](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/functional-conversion/SKILL.md) — 将 nn.Module 标杆转为输入显式的无状态函数式 API。
  `CANNBot` `Ascend C` `Specification and modeling` `Community` `主机工具` · [条目](catalog/skills/functional-conversion.yaml)
- [generate-case](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/generate-case/SKILL.md) — 从设计中的测试章节生成可执行 AscendC 验证资产。
  `AscendC Agent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/generate-case.yaml)
- [hint-mode](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/designer/hint-mode/SKILL.md) — 定义约束参数和搜索空间，指导算法草图优化。
  `AKG` `Operator support` `Design and pipelines` `主机工具` · [条目](catalog/skills/hint-mode.yaml)
- [kernel-agent-overview](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/kernel-agent/kernel-agent-overview/SKILL.md) — 说明 AKG 算子 Agent 角色、工具及生成与验证交互。
  `AKG` `Operator support` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/kernel-agent-overview.yaml)
- [kernel-designer](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/triton/kernel-designer/SKILL.md) — 为 Triton-Ascend 任务设计算法草图和执行策略。
  `AscendOpGenAgent` `Triton` `Design and pipelines` `主机工具` · [条目](catalog/skills/kernel-designer.yaml)
- [kernel-generator](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/triton/kernel-generator/SKILL.md) — 结合任务、草图、架构和验证反馈生成 Triton-Ascend 代码。
  `AscendOpGenAgent` `Triton` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/kernel-generator.yaml)
- [kernel-splitter](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/triton/kernel-splitter/SKILL.md) — 按中间数据和执行契约将算子拆分为合适的 Triton Kernel。
  `AscendOpGenAgent` `Triton` `Design and pipelines` `主机工具` · [条目](catalog/skills/kernel-splitter.yaml)
- [kernel-workflow](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/kernel-workflow/SKILL.md) — 组织 AKG 任务构建、草图设计、生成、验证和迭代优化。
  `AKG` `Operator support` `Implementation and migration` `执行需 NPU` `流程编排` · [条目](catalog/skills/kernel-workflow.yaml)
- [knowledge-ingest](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/knowledge-ingest/SKILL.md) — 将登记文档或固定版本源码转为受治理、可追溯的候选知识。
  `CANNBot Knowledge` `Operator support` `Knowledge and cases` `主机工具` · [条目](catalog/skills/knowledge-ingest.yaml)
- [knowledge-lint](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/knowledge-lint/SKILL.md) — 校验知识结构、来源、导航和生命周期元数据。
  `CANNBot Knowledge` `Operator support` `Knowledge and cases` `主机工具` · [条目](catalog/skills/knowledge-lint.yaml)
- [knowledge-query](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/knowledge-query/SKILL.md) — 在算子设计、实现、测试和优化决策前检索匹配平台的知识卡。
  `CANNBot Knowledge` `Operator support` `Knowledge and cases` `主机工具` · [条目](catalog/skills/knowledge-query.yaml)
- [latency-optimizer](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/triton/latency-optimizer/SKILL.md) — 依据测量反馈迭代优化 Triton-Ascend 时延，并回归精度。
  `AscendOpGenAgent` `Triton` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/latency-optimizer.yaml)
- [merge-incompatible-samples](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/merge-incompatible-samples/SKILL.md) — 通过明确的编译期分支合并跨架构不兼容 AscendC 样例。
  `AscendC Agent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/merge-incompatible-samples.yaml)
- [model-agent-ascendc-operator-code-gen](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-code-gen/SKILL.md) — 生成 AscendC Host/Kernel 代码、注册 PyTorch 并衔接构建测试。
  `Model Agent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/model-agent-ascendc-operator-code-gen.yaml)
- [model-agent-ascendc-operator-design](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-design/SKILL.md) — 设计算子接口、两级 Tiling、UB 分配和 Kernel 计算逻辑。
  `Model Agent` `Ascend C` `Design and pipelines` `主机工具` · [条目](catalog/skills/model-agent-ascendc-operator-design.yaml)
- [model-agent-ascendc-operator-dev](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-dev/SKILL.md) — 组织 AscendC 自定义算子的工程初始化、设计、用例、实现和评估。
  `Model Agent` `Ascend C` `Implementation and migration` `执行需 NPU` `流程编排` · [条目](catalog/skills/model-agent-ascendc-operator-dev.yaml)
- [model-agent-ascendc-operator-performance-optim](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-performance-optim/SKILL.md) — 依据实测瓶颈修改 AscendC 代码，并复核精度及相对基线性能。
  `Model Agent` `Ascend C` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/model-agent-ascendc-operator-performance-optim.yaml)
- [model-agent-ascendc-operator-project-init](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-project-init/SKILL.md) — 创建可构建的 AscendC 自定义算子工程并列出注册检查点。
  `Model Agent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/model-agent-ascendc-operator-project-init.yaml)
- [model-agent-simple-vector-triton-gpu-to-npu](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/simple-vector-triton-gpu-to-npu/SKILL.md) — 将简单 Vector Triton Kernel 从 GPU 迁移到昇腾并验证。
  `Model Agent` `Triton` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/model-agent-simple-vector-triton-gpu-to-npu.yaml)
- [multi-scenario-sample-pattern](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/multi-scenario-sample-pattern/SKILL.md) — 将相似 AscendC 样例合并为可选场景的统一工程。
  `AscendC Agent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/multi-scenario-sample-pattern.yaml)
- [npu-arch](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/npu-arch/SKILL.md) — 确认芯片、架构、SocVersion、特性支持与条件编译边界。
  `CANNBot` `Operator support` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/npu-arch.yaml)
- [npu-migration-ascend](https://github.com/KernelHive/ascendc-skill/blob/c78f267d0423d59a51a02070e5bb845fde2dbd69/skills/ascend-npu-migration/SKILL.md) — 保持语义一致，将源算子迁移到 AscendC 并完成集成验证。
  `KernelHive` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/npu-migration-ascend.yaml)
- [npu-op-benchmark](https://github.com/ascend-ai-coding/awesome-ascend-skills/blob/75ec89ce9d401be8ac95980e1c3f42f8d4315057/skills/ops/npu-op-benchmark/SKILL.md) — 检查已有 NPU 环境，按明确 Shape 和计时条件评测算子。
  `Awesome Ascend Skills` `Operator support` `Implementation and migration` `执行需 NPU` · [条目](catalog/skills/npu-op-benchmark.yaml)
- [op-desc-generation](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/op-desc-generation/SKILL.md) — 生成包含 Shape、dtype 和属性的结构化算子描述。
  `CANNBot` `Ascend C` `Specification and modeling` `Community` `主机工具` · [条目](catalog/skills/op-desc-generation.yaml)
- [op-task-extractor](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/triton/op-task-extractor/SKILL.md) — 从需求或源码提取独立可评测的算子任务。
  `AscendOpGenAgent` `Triton` `Specification and modeling` `主机工具` · [条目](catalog/skills/op-task-extractor.yaml)
- [operator-dev](https://github.com/Ascend/MindIE-SD/blob/d6f5ca90a882c73b25ace504ae9da254976f53c6/.agents/skills/operator-dev/SKILL.md) — 路由到 CANNBot 算子技能，并叠加 MindIE-SD 集成、部署和模型验证约束。
  `MindIE-SD` `Operator support` `Implementation and migration` `执行需 NPU` `流程编排` · [条目](catalog/skills/operator-dev.yaml)
- [ops-design-paradigms](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ops-design-paradigms/SKILL.md) — 选择广播、归约和收缩范式，核对资源与实现约束。
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/ops-design-paradigms.yaml)
- [ops-direct-invoke](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/ops-direct-invoke/SKILL.md) — 组织直调算子的需求、环境、分工执行、验收和交付。
  `CANNBot` `Ascend C` `Implementation and migration` `执行需 NPU` `流程编排` · [条目](catalog/skills/ops-direct-invoke.yaml)
- [ops-knowledge-cv-ingest](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/ops-knowledge-cv-ingest/SKILL.md) — 提取完整 Cube/MIX_CV 算子路径及数据流、资源和同步契约。
  `CANNBot Knowledge` `Operator support` `Knowledge and cases` `主机工具` · [条目](catalog/skills/ops-knowledge-cv-ingest.yaml)
- [ops-knowledge-trace-ingest](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/ops-knowledge-trace-ingest/SKILL.md) — 将算子开发轨迹提炼为带来源的诊断 Runbook 和修复模式。
  `CANNBot Knowledge` `Operator support` `Knowledge and cases` `主机工具` · [条目](catalog/skills/ops-knowledge-trace-ingest.yaml)
- [ops-knowledge-vv-ingest](https://gitcode.com/cann/cannbot-knowledge/blob/fd3dd23d19d4bab3da27951cd9f8d6b1a3b8644e/.agents/skills/ops-knowledge-vv-ingest/SKILL.md) — 提取非 Cube 算子路径及内存、Workspace、同步和生命周期契约。
  `CANNBot Knowledge` `Operator support` `Knowledge and cases` `主机工具` · [条目](catalog/skills/ops-knowledge-vv-ingest.yaml)
- [ops-precision-standard](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ops-precision-standard/SKILL.md) — 按语义和输入输出 dtype 选择精度判据及 Golden 构造方式。
  `CANNBot` `Operator support` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/ops-precision-standard.yaml)
- [ops-registry-invoke](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/ops-registry-invoke/SKILL.md) — 启动 ACLNN 注册调用算子开发工作流。
  `CANNBot` `Ascend C` `Implementation and migration` `执行需 NPU` `流程编排` · [条目](catalog/skills/ops-registry-invoke.yaml)
- [ops-requirement-analysis](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/ops-requirement-analysis/SKILL.md) — 调研模型场景、参考框架和 CANN 能力，编写算子需求。
  `CANNBot` `Ascend C` `Specification and modeling` `主机工具` · [条目](catalog/skills/ops-requirement-analysis.yaml)
- [ops-simulator](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ops-simulator/SKILL.md) — 运行主机侧 CANN 精度、性能仿真并解释流水报告。
  `CANNBot` `Operator support` `Implementation and migration` `主机工具` · [条目](catalog/skills/ops-simulator.yaml)
- [ops-theoretical-performance-estimation](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ops-theoretical-performance-estimation/SKILL.md) — 估算 Ascend950 RegBase 纯 Vector 算子的设计期时延下界。
  `CANNBot` `Ascend C` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/ops-theoretical-performance-estimation.yaml)
- [pypto-op-develop](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/pypto-op-develop/SKILL.md) — 根据设计契约逐阶段构建 PyPTO impl 模块，整理最终内核实现和说明。
  `CANNBot` `PyPTO` `设备取决于检查项` · [条目](catalog/skills/pypto-op-develop.yaml)
- [reference-generation](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/reference-generation/SKILL.md) — 生成保持语义的 PyTorch Golden 及可复现输入构造器。
  `CANNBot` `Ascend C` `Specification and modeling` `Community` `主机工具` · [条目](catalog/skills/reference-generation.yaml)
- [remote-cann-development](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/remote-cann-development/SKILL.md) — 在指定远程 NPU 后端同步、执行和测试算子工程。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/remote-cann-development.yaml)
- [repo-build-guide](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-build-guide/SKILL.md) — 构建直调算子和 CANN Bench 包，核对实际加载的产物。
  `CANNBot` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/repo-build-guide.yaml)
- [repo-coding-rules](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-coding-rules/SKILL.md) — 应用 CANN Bench 实现真实性、包装、接口和 AscendC 代码规范。
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/repo-coding-rules.yaml)
- [repo-knowledge](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-knowledge/SKILL.md) — 查询 CANN Bench 提交、任务、精度和评分契约。
  `CANNBot` `Ascend C` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/repo-knowledge.yaml)
- [repo-op-templates](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-op-templates/SKILL.md) — 从 CANN Bench 参考工程和模板创建直调代码。
  `CANNBot` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/repo-op-templates.yaml)
- [repo-requirement](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/repo-requirement/SKILL.md) — 记录跨重试复用的算子需求、环境选择和修改范围。
  `CANNBot` `Ascend C` `Specification and modeling` `主机工具` · [条目](catalog/skills/repo-requirement.yaml)
- [simple-vector-triton-gpu-to-npu](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/simple-vector-triton-gpu-to-npu/SKILL.md) — 将简单 Vector Triton Kernel 从 GPU 迁移到昇腾并验证。
  `Ascend Agent Skills` `Triton` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/simple-vector-triton-gpu-to-npu.yaml)
- [simt-requirement-doc](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/simt-requirement-doc/SKILL.md) — 澄清 SIMT 需求并编写实现与验收规格。
  `AscendC Agent` `Ascend C` `Specification and modeling` `主机工具` · [条目](catalog/skills/simt-requirement-doc.yaml)
- [sketch-design](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/designer/sketch-design/SKILL.md) — 描述感知硬件的算法草图和代码生成所需优化决策。
  `AKG` `Operator support` `Design and pipelines` `主机工具` · [条目](catalog/skills/sketch-design.yaml)
- [skill-trace](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/skill-trace/SKILL.md) — 记录算子生成中技能的输入、耗时和结果。
  `CANNBot` `Ascend C` `Knowledge and cases` `Community` `主机工具` · [条目](catalog/skills/skill-trace.yaml)
- [task-constructor](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/task-constructor/SKILL.md) — 构建包含标杆和可复现输入函数的独立 Kernel 生成任务。
  `AKG` `Operator support` `Specification and modeling` `主机工具` · [条目](catalog/skills/task-constructor.yaml)
- [tilelang-designer](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/ascendc/tilelang-designer/SKILL.md) — 以块级和 Tile 级表达算子，为 AscendC 生成提供设计输入。
  `AscendOpGenAgent` `Ascend C` `Design and pipelines` `主机工具` · [条目](catalog/skills/tilelang-designer.yaml)
- [tilelang-op-develop](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/tilelang-op-develop/SKILL.md) — 根据设备探测结果路由到 Ascend910 或 Ascend950 的 TileLang 实现与精度验证流程。
  `CANNBot` `TileLang` `执行需 NPU` · [条目](catalog/skills/tilelang-op-develop.yaml)
- [tilelang2ascend-case-simplifier](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/tilelang2ascend-case-simplifier/SKILL.md) — 在保留声明覆盖维度的前提下精简算子用例集。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/tilelang2ascend-case-simplifier.yaml)
- [tilelang2ascend-operator-project-init](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/tilelang2ascend-operator-project-init/SKILL.md) — 创建 AscendC 算子骨架、可构建文件和后续开发清单。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/tilelang2ascend-operator-project-init.yaml)
- [tilelang2ascend-tilelang-designer](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/tilelang2ascend-tilelang-designer/SKILL.md) — 组织块级和 Tile 级设计，为 AscendC 转译准备 TileLang 设计表达。
  `CANNBot` `Ascend C` `Design and pipelines` `Community` `主机工具` · [条目](catalog/skills/tilelang2ascend-tilelang-designer.yaml)
- [tilelang2ascend-trace-recorder](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/tilelang2ascend-trace-recorder/SKILL.md) — 记录算子开发轨迹并提炼带来源的 Runbook，供后续检索复用。
  `CANNBot` `Ascend C` `Knowledge and cases` `Community` `主机工具` · [条目](catalog/skills/tilelang2ascend-trace-recorder.yaml)
- [tilelang2ascend-translator](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/tilelang2ascend-translator/SKILL.md) — 将 TileLang 设计转译为 AscendC Kernel 及 Python 调用封装。
  `CANNBot` `Ascend C` `Implementation and migration` `Community` `设备取决于检查项` · [条目](catalog/skills/tilelang2ascend-translator.yaml)
- [torch-ascendc-op-extension](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/torch-ascendc-op-extension/SKILL.md) — 将已有 AscendC 算子通过自定义接口接入 PyTorch。
  `CANNBot` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/torch-ascendc-op-extension.yaml)
- [torch-custom-ops-guide](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/graph/torch-custom-ops-guide/SKILL.md) — 注册 Python 自定义算子、补齐 Meta 行为并适配 npugraph_ex。
  `CANNBot` `Operator support` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/torch-custom-ops-guide.yaml)
- [tpipe-to-static-tensor](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/tpipe-to-static-tensor/SKILL.md) — 将 TPipe/TQue AscendC 样例迁移为静态 Tensor 编程。
  `AscendC Agent` `Ascend C` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/tpipe-to-static-tensor.yaml)
- [trace-recorder](https://github.com/Just-it/AscendOpGenAgent/blob/595ce700122e1fea46d5bdc0949578b130ba404f/skills/ascendc/trace-recorder/SKILL.md) — 记录算子实现、验证和优化决策，形成执行轨迹。
  `AscendOpGenAgent` `Ascend C` `Knowledge and cases` `主机工具` · [条目](catalog/skills/trace-recorder.yaml)
- [triton-agent-loop](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/triton-auto-evolve/skills/triton-agent-loop/SKILL.md) — 组织独立 Triton 优化轮次，保留逐轮产物与评测结果。
  `CANNBot` `Triton` `Profiling and optimization` `Community` `执行需 NPU` `流程编排` · [条目](catalog/skills/triton-agent-loop.yaml)
- [triton-ascend-api-rules](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-api-rules/SKILL.md) — 查询 Triton-Ascend 后端 API 和语法限制指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-api-rules.yaml)
- [triton-ascend-ascend-hardware-constraints](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-ascend-hardware-constraints/SKILL.md) — 查询 Triton-Ascend 片上内存预算和编译器约束指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-ascend-hardware-constraints.yaml)
- [triton-ascend-attention](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/guides/triton-ascend-attention/SKILL.md) — 查询 Triton-Ascend Attention 切分、在线 Softmax 和掩码指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-attention.yaml)
- [triton-ascend-basics](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-basics/SKILL.md) — 查询 Triton-Ascend Program ID、Grid、Kernel 结构和启动语法指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-basics.yaml)
- [triton-ascend-case-elemwise-broadcast-2d](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-elemwise-broadcast-2d/SKILL.md) — 参考 Triton-Ascend 二维广播优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-elemwise-broadcast-2d.yaml)
- [triton-ascend-case-elemwise-broadcast-3d](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-elemwise-broadcast-3d/SKILL.md) — 参考 Triton-Ascend 三维广播优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-elemwise-broadcast-3d.yaml)
- [triton-ascend-case-elemwise-cast](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-elemwise-cast/SKILL.md) — 参考 Triton-Ascend 数据类型转换优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-elemwise-cast.yaml)
- [triton-ascend-case-elemwise-concat](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-elemwise-concat/SKILL.md) — 参考 Triton-Ascend 拼接优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-elemwise-concat.yaml)
- [triton-ascend-case-elemwise-zeros](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-elemwise-zeros/SKILL.md) — 参考 Triton-Ascend 零初始化优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-elemwise-zeros.yaml)
- [triton-ascend-case-index-histogram](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-index-histogram/SKILL.md) — 参考 Triton-Ascend 直方图索引优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-index-histogram.yaml)
- [triton-ascend-case-index-put](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-index-put/SKILL.md) — 参考 Triton-Ascend 索引更新优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-index-put.yaml)
- [triton-ascend-case-matmul-large-k](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-matmul-large-k/SKILL.md) — 参考 Triton-Ascend 大 K 矩阵乘优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-matmul-large-k.yaml)
- [triton-ascend-case-matmul-swizzle2d](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-matmul-swizzle2d/SKILL.md) — 参考 Triton-Ascend 矩阵乘 Swizzle优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-matmul-swizzle2d.yaml)
- [triton-ascend-case-reduction-amax-large](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amax-large/SKILL.md) — 参考 Triton-Ascend 大规模 amax 归约优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-amax-large.yaml)
- [triton-ascend-case-reduction-amax-medium](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amax-medium/SKILL.md) — 参考 Triton-Ascend 中等规模 amax 归约优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-amax-medium.yaml)
- [triton-ascend-case-reduction-amax-small](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amax-small/SKILL.md) — 参考 Triton-Ascend 小规模 amax 归约优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-amax-small.yaml)
- [triton-ascend-case-reduction-amin-atomic](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amin-atomic/SKILL.md) — 参考 Triton-Ascend 原子 amin 归约优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-amin-atomic.yaml)
- [triton-ascend-case-reduction-amin-large](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amin-large/SKILL.md) — 参考 Triton-Ascend 大规模 amin 归约优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-amin-large.yaml)
- [triton-ascend-case-reduction-amin-medium](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amin-medium/SKILL.md) — 参考 Triton-Ascend 中等规模 amin 归约优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-amin-medium.yaml)
- [triton-ascend-case-reduction-amin-small](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-amin-small/SKILL.md) — 参考 Triton-Ascend 小规模 amin 归约优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-amin-small.yaml)
- [triton-ascend-case-reduction-mean-large](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-mean-large/SKILL.md) — 参考 Triton-Ascend 大规模 mean 归约优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-mean-large.yaml)
- [triton-ascend-case-reduction-mean-medium](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-mean-medium/SKILL.md) — 参考 Triton-Ascend 中等规模 mean 归约优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-mean-medium.yaml)
- [triton-ascend-case-reduction-prod-small](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-prod-small/SKILL.md) — 参考 Triton-Ascend 小规模乘积归约优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-prod-small.yaml)
- [triton-ascend-case-reduction-sum-fused](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-sum-fused/SKILL.md) — 参考 Triton-Ascend 逐元素与 sum 融合优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-sum-fused.yaml)
- [triton-ascend-case-reduction-sum-large](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-sum-large/SKILL.md) — 参考 Triton-Ascend 大规模 sum 归约优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-sum-large.yaml)
- [triton-ascend-case-reduction-weighted-swiglu](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/cases/triton-ascend-case-reduction-weighted-swiglu/SKILL.md) — 参考 Triton-Ascend 带权 SwiGLU 反向优化案例及其限定场景下的设计、测量观察。
  `AKG` `Triton` `Knowledge and cases` `Optimization case` `主机工具` · [条目](catalog/skills/triton-ascend-case-reduction-weighted-swiglu.yaml)
- [triton-ascend-debugging](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-debugging/SKILL.md) — 查询 Triton-Ascend 编译、运行、数值和性能诊断指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-debugging.yaml)
- [triton-ascend-elementwise-reduce-fused](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/guides/triton-ascend-elementwise-reduce-fused/SKILL.md) — 查询 Triton-Ascend 逐元素与全局归约复合算子指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-elementwise-reduce-fused.yaml)
- [triton-ascend-elementwise](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/guides/triton-ascend-elementwise/SKILL.md) — 查询 Triton-Ascend 逐元素算子指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-elementwise.yaml)
- [triton-ascend-error-fix](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/evolved-fix/triton-ascend-error-fix/SKILL.md) — 查询 Triton-Ascend 编译、索引、内存和数值问题指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-error-fix.yaml)
- [triton-ascend-example-double-kernel](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/examples/triton-ascend-example-double-kernel/SKILL.md) — 参考 Triton-Ascend 分阶段双 Kernel 执行实现示例及代码结构。
  `AKG` `Triton` `Knowledge and cases` `Implementation example` `主机工具` · [条目](catalog/skills/triton-ascend-example-double-kernel.yaml)
- [triton-ascend-example-layernorm](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/examples/triton-ascend-example-layernorm/SKILL.md) — 参考 Triton-Ascend LayerNorm实现示例及代码结构。
  `AKG` `Triton` `Knowledge and cases` `Implementation example` `主机工具` · [条目](catalog/skills/triton-ascend-example-layernorm.yaml)
- [triton-ascend-example-matmul](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/examples/triton-ascend-example-matmul/SKILL.md) — 参考 Triton-Ascend 矩阵乘实现示例及代码结构。
  `AKG` `Triton` `Knowledge and cases` `Implementation example` `主机工具` · [条目](catalog/skills/triton-ascend-example-matmul.yaml)
- [triton-ascend-example-relu](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/examples/triton-ascend-example-relu/SKILL.md) — 参考 Triton-Ascend ReLU实现示例及代码结构。
  `AKG` `Triton` `Knowledge and cases` `Implementation example` `主机工具` · [条目](catalog/skills/triton-ascend-example-relu.yaml)
- [triton-ascend-example-softmax](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/examples/triton-ascend-example-softmax/SKILL.md) — 参考 Triton-Ascend Softmax实现示例及代码结构。
  `AKG` `Triton` `Knowledge and cases` `Implementation example` `主机工具` · [条目](catalog/skills/triton-ascend-example-softmax.yaml)
- [triton-ascend-examples-mindspore](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/examples/triton-ascend-examples-mindspore/SKILL.md) — 参考 Triton-Ascend MindSpore 集成实现示例及代码结构。
  `AKG` `Triton` `Knowledge and cases` `Implementation example` `主机工具` · [条目](catalog/skills/triton-ascend-examples-mindspore.yaml)
- [triton-ascend-fused-operator-optimization](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/evolved-improvement/triton-ascend-fused-operator-optimization/SKILL.md) — 查询 Triton-Ascend 融合性能上限、Pass 合并和访存重构指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-fused-operator-optimization.yaml)
- [triton-ascend-grid-config](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-grid-config/SKILL.md) — 查询 Triton-Ascend 分核、Grid/Block 选择和二次切分指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-grid-config.yaml)
- [triton-ascend-matmul](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/guides/triton-ascend-matmul/SKILL.md) — 查询 Triton-Ascend 矩阵乘算子指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-matmul.yaml)
- [triton-ascend-memory](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-memory/SKILL.md) — 查询 Triton-Ascend UB 使用、布局、连续访存和预取指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-memory.yaml)
- [triton-ascend-migration](https://github.com/ascend-ai-coding/awesome-ascend-skills/blob/75ec89ce9d401be8ac95980e1c3f42f8d4315057/skills/ops/triton-ascend-migration/SKILL.md) — 将 GPU Triton 或 PyTorch 语义迁移到 Triton-Ascend，生成最小上板验证脚本。
  `Awesome Ascend Skills` `Triton` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/triton-ascend-migration.yaml)
- [triton-ascend-optimization](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/fundamentals/triton-ascend-optimization/SKILL.md) — 查询 Triton-Ascend Tiling、Grid 选择、对齐和后端优化指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-optimization.yaml)
- [triton-ascend-performance-improvement](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/evolved-improvement/triton-ascend-performance-improvement/SKILL.md) — 查询 Triton-Ascend 实测 Tile、加载、归约和 Pass 优化模式指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-performance-improvement.yaml)
- [triton-ascend-reduce](https://github.com/mindspore-ai/akg/blob/5aa15f3fe4d856eb60cd3b27447e04f5f1fb4dff/akg_agents/python/akg_agents/op/resources/skills/triton-ascend/guides/triton-ascend-reduce/SKILL.md) — 查询 Triton-Ascend 归约和归一化算子指南，使用时核对所述平台和编译器范围。
  `AKG` `Triton` `Knowledge and cases` `Knowledge reference` `主机工具` · [条目](catalog/skills/triton-ascend-reduce.yaml)
- [triton-ascendc-fused-op-generator](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/training-optimization/operator-fusion/triton-ascendc-fused-op-generator/SKILL.md) — 识别融合候选、估算 GM 流量收益并生成 Triton/AscendC 实现方案。
  `Model Agent` `Operator support` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/triton-ascendc-fused-op-generator.yaml)
- [triton-latency-optimizer](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-latency-optimizer/SKILL.md) — 每轮修改一个优化点，配对验证 Triton-Ascend 正确性与时延。
  `CANNBot` `Triton` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/triton-latency-optimizer.yaml)
- [triton-op-coding](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-op-coding/SKILL.md) — 依据任务和草图生成纯 Triton-Ascend Kernel，并按验证反馈修复。
  `CANNBot` `Triton` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/triton-op-coding.yaml)
- [triton-op-designer](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-op-designer/SKILL.md) — 依据算子规格和历史反馈设计感知架构的算法草图。
  `CANNBot` `Triton` `Design and pipelines` `主机工具` · [条目](catalog/skills/triton-op-designer.yaml)
- [triton-operator-code-gen](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-code-gen/SKILL.md) — 从设计或功能需求生成昇腾 Triton Kernel 和冒烟测试。
  `Model Agent` `Triton` `Implementation and migration` `设备取决于检查项` · [条目](catalog/skills/triton-operator-code-gen.yaml)
- [triton-operator-design](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-design/SKILL.md) — 定义 Triton 算子语义、接口、Tiling 和 Kernel 实现策略。
  `Model Agent` `Triton` `Design and pipelines` `主机工具` · [条目](catalog/skills/triton-operator-design.yaml)
- [triton-operator-dev](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-dev/SKILL.md) — 组织 Triton 环境、设计、编码、检视、精度验证和性能迭代。
  `Model Agent` `Triton` `Implementation and migration` `执行需 NPU` `流程编排` · [条目](catalog/skills/triton-operator-dev.yaml)
- [triton-operator-performance-optim](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-performance-optim/SKILL.md) — 调优 Triton-Ascend Tiling 和内存使用，并复核精度与性能。
  `Model Agent` `Triton` `Profiling and optimization` `执行需 NPU` · [条目](catalog/skills/triton-operator-performance-optim.yaml)
- [triton-task-extractor](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-task-extractor/SKILL.md) — 从用户代码或需求构建独立算子任务和输入用例。
  `CANNBot` `Triton` `Specification and modeling` `主机工具` · [条目](catalog/skills/triton-task-extractor.yaml)
- [vector-triton-ascend-ops-optimizer](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/vector-triton-ascend-ops-optimizer/SKILL.md) — 通过 UB 预算、批处理和流水优化 Vector Triton，并进行实测对比。
  `Ascend Agent Skills` `Triton` `Profiling and optimization` `Community` `执行需 NPU` · [条目](catalog/skills/vector-triton-ascend-ops-optimizer.yaml)
- [workflow-bootstrap](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-registry-invoke/skills/workflow-bootstrap/SKILL.md) — 检测目标架构并选择对应注册算子工作流。
  `CANNBot` `Ascend C` `Implementation and migration` `执行需 NPU` `流程编排` · [条目](catalog/skills/workflow-bootstrap.yaml)

<a id="debugging"></a>

### 故障诊断

缩小启动、通信、图执行和算子异常的复现范围并验证修复。

- [ascend-operator-debug](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/ascend-operator-debug/SKILL.md) — 将模型异常缩小到单算子调用，检查 dtype、shape、layout 与执行模式。
  `Ascend` `执行需 NPU` · [条目](catalog/skills/ascend-operator-debug.yaml)
- [ascendc-crash-debug](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-crash-debug/SKILL.md) — 诊断 AscendC 卡死、崩溃、内存和 Buffer/同步问题。
  `CANNBot` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/ascendc-crash-debug.yaml)
- [ascendc-debugging](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/usability/op-gen/ascendc-debugging/SKILL.md) — 诊断编译、运行和数值问题，验证小规模、典型及边界用例。
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/ascendc-debugging.yaml)
- [ascendc-mssanitizer](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-mssanitizer/SKILL.md) — 运行解释 mssanitizer，检测非法访问、泄漏和 UB 越界。
  `Ascend Agent Skills` `Ascend C` `Testing and numerical validation` `Community` `执行需 NPU` · [条目](catalog/skills/ascendc-mssanitizer.yaml)
- [ascendc-op-debug](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/ascendc-op-debug/SKILL.md) — 基于假设检验诊断精度、崩溃、卡死和多核不一致。
  `CANNBot` `Ascend C` `Testing and numerical validation` `Community` `执行需 NPU` · [条目](catalog/skills/ascendc-op-debug.yaml)
- [ascendc-operator-compile-debug](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-compile-debug/SKILL.md) — 构建安装 AscendC 扩展，运行精度测试并修复失败。
  `Ascend Agent Skills` `Ascend C` `Testing and numerical validation` `Community` `执行需 NPU` · [条目](catalog/skills/ascendc-operator-compile-debug.yaml)
- [ascendc-operator-precision-debug](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-precision-debug/SKILL.md) — 分析数值误差形态、隔离异常计算并验证 AscendC 修复。
  `Ascend Agent Skills` `Ascend C` `Testing and numerical validation` `Community` `执行需 NPU` · [条目](catalog/skills/ascendc-operator-precision-debug.yaml)
- [ascendc-precision-debug](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-precision-debug/SKILL.md) — 将数值异常收敛为可复现单算子用例，定位根因并验证修复。
  `CANNBot` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/ascendc-precision-debug.yaml)
- [ascendc-runtime-debug](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-runtime-debug/SKILL.md) — 结合错误码和 plog 定位 AscendC 调用、Tiling 和运行时故障。
  `CANNBot` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/ascendc-runtime-debug.yaml)
- [asys-toolkit](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/tools/asys-toolkit/SKILL.md) — 在 Ascend EP 环境使用 asys 收集故障信息、检查设备健康并解析诊断产物。
  `CANNBot` `CANN` `asys` `设备取决于检查项` · [条目](catalog/skills/asys-toolkit.yaml)
- [ge-dynamic-shape-diagnose](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/graph/ge-dynamic-shape-diagnose/SKILL.md) — 根据 GE 编译日志定位 unknown graph 与动态 shape 调度的触发原因。
  `CANNBot` `GE` `离线分析` · [条目](catalog/skills/ge-dynamic-shape-diagnose.yaml)
- [gm-align-debug](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/gm-align-debug/SKILL.md) — 通过内存 Dump 复现 GM/UB 搬运对齐及字节重解释问题。
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/gm-align-debug.yaml)
- [model-agent-ascendc-operator-compile-debug](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-compile-debug/SKILL.md) — 构建安装 AscendC 扩展，运行精度测试并修复失败。
  `Model Agent` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/model-agent-ascendc-operator-compile-debug.yaml)
- [model-agent-ascendc-operator-precision-debug](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-precision-debug/SKILL.md) — 分析数值误差形态、隔离异常计算并验证 AscendC 修复。
  `Model Agent` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/model-agent-ascendc-operator-precision-debug.yaml)
- [model-infer-precision-debug](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-precision-debug/SKILL.md) — 定位 KVCache 与 FlashAttention 相关的 Prefill/Decode 精度差异、缓存更新和映射问题。
  `CANNBot` `PyTorch` `KV cache` `执行需 NPU` · [条目](catalog/skills/model-infer-precision-debug.yaml)
- [model-infer-runtime-debug](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/model/model-infer-runtime-debug/SKILL.md) — 逐阶段缩小模型加载和推理运行异常，诊断 HCCL、OOM、超时与卡死并验证修复。
  `CANNBot` `PyTorch` `HCCL` `执行需 NPU` · [条目](catalog/skills/model-infer-runtime-debug.yaml)
- [msaicerr-toolkit](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/tools/msaicerr-toolkit/SKILL.md) — 在日志产生环境使用 msaicerr 分析 AI Core Error、解析 Dump 并检查环境约束。
  `CANNBot` `CANN` `msaicerr` `设备取决于检查项` · [条目](catalog/skills/msaicerr-toolkit.yaml)
- [msnpureport-toolkit](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/tools/msnpureport-toolkit/SKILL.md) — 在受支持的 Ascend EP 环境导出 Device 日志，并按权限查询或设置维测配置。
  `CANNBot` `CANN` `msnpureport` `执行需 NPU` · [条目](catalog/skills/msnpureport-toolkit.yaml)
- [torch-npugraph-ex-dfx-triage](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/graph/torch-npugraph-ex-dfx-triage/SKILL.md) — 收集分层日志并将 npugraph_ex 问题路由到编译、运行时、精度或性能诊断。
  `CANNBot` `PyTorch` `npugraph_ex` `设备取决于检查项` `流程编排` · [条目](catalog/skills/torch-npugraph-ex-dfx-triage.yaml)
- [triton-precision-debug](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/triton-precision-debug/SKILL.md) — 定位 Triton-Ascend 数值异常并验证针对性修复。
  `CANNBot` `Triton` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/triton-precision-debug.yaml)
- [ub-boundary-check](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/ub-boundary-check/SKILL.md) — 复现 UB 边界、向量读写、Mask 和搬运内存问题。
  `AscendC Agent` `Ascend C` `Testing and numerical validation` `执行需 NPU` · [条目](catalog/skills/ub-boundary-check.yaml)
- [vllm-ascend-distributed-debug](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-distributed-debug/SKILL.md) — 根据拓扑和逐 rank 证据定位启动、collective、端点与卡死问题。
  `vLLM Ascend` `HCCL` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-distributed-debug.yaml)
- [vllm-ascend-graph-debug](https://github.com/pisceskkk/vllm-ascend-skills/blob/4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3/skills/vllm-ascend-graph-debug/SKILL.md) — 通过受控实验和中间快照定位图捕获、回放及 eager/graph 分歧。
  `vLLM Ascend` `Graph` `执行需 NPU` · [条目](catalog/skills/vllm-ascend-graph-debug.yaml)

<a id="delivery"></a>

### 工程交付与运行维护

将变更映射到构建、正确性和性能验证，记录覆盖范围。

- [aog-report-gen](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-report-gen/SKILL.md) — 为跨代迁移或反向算子生成输出项目报告。
  `CANNBot` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/aog-report-gen.yaml)
- [aog-self-critic](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/ascendc-port-orchestrator/skills/aog-self-critic/SKILL.md) — 检查当前算子开发会话的重复流程问题并提出修正。
  `CANNBot` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/aog-self-critic.yaml)
- [asc-devkit-review](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/code-review/asc-devkit-review/SKILL.md) — 审查 Ascend DevKit PR 并形成基于源码的检视意见。
  `AscendC Agent` `Ascend C` `Review and delivery` `主机工具` · [条目](catalog/skills/asc-devkit-review.yaml)
- [asc-testcase-doc-gen](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/asc-testcase-doc-gen/SKILL.md) — 将需求文档转为结构化测试用例文档。
  `AscendC Agent` `Operator support` `Review and delivery` `主机工具` · [条目](catalog/skills/asc-testcase-doc-gen.yaml)
- [ascendc-code-review](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-code-review/SKILL.md) — 基于可检验假设审查 AscendC 源码或 PR 的规范和设计一致性。
  `CANNBot` `Ascend C` `Review and delivery` `主机工具` · [条目](catalog/skills/ascendc-code-review.yaml)
- [ascendc-docs-gen](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-docs-gen/SKILL.md) — 基于标准模板编写算子需求、详设、API 文档和 README。
  `CANNBot` `Ascend C` `Review and delivery` `主机工具` · [条目](catalog/skills/ascendc-docs-gen.yaml)
- [ascendc-evolution-report](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/community/ops/ascendc-evolution-report/SKILL.md) — 生成并检查进化变体、性能对比、决策过程和资源消耗的 HTML 报告。
  `CANNBot` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/ascendc-evolution-report.yaml)
- [ascendc-op-doc-generator](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-op-doc-generator/SKILL.md) — 提取源码契约并生成 ACLNN API 文档和算子 README。
  `Ascend Agent Skills` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/ascendc-op-doc-generator.yaml)
- [ascendc-op-doc-incremental](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-op-doc-incremental/SKILL.md) — 对比源码变更与算子文档并生成增量更新。
  `Ascend Agent Skills` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/ascendc-op-doc-incremental.yaml)
- [ascendc-operator-code-review](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-code-review/SKILL.md) — 检查 AscendC 代码正确性和工程规范问题。
  `Ascend Agent Skills` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/ascendc-operator-code-review.yaml)
- [ascendc-operator-doc-gen](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-doc-gen/SKILL.md) — 依据实现源码生成 PyTorch 风格算子接口文档。
  `Ascend Agent Skills` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/ascendc-operator-doc-gen.yaml)
- [ascendc-operator-doc-writer](https://gitcode.com/Ascend/agent-skills/blob/a4011846f6d79fcee3e7b90fafe588d8a51fbc91/community/Op/ascendc-operator-doc-writer/SKILL.md) — 结合本地源码和已有模板编写算子技术文档。
  `Ascend Agent Skills` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/ascendc-operator-doc-writer.yaml)
- [ascendc-sync-audit](https://gitcode.com/cann/cannbot-skills/blob/5891c39619a56716b6f73a335ed7709560bb2da8/ops/ascendc-sync-audit/SKILL.md) — 检查流水、核间信号和生产消费 Buffer 一致性，并提出修复。
  `CANNBot` `Ascend C` `Review and delivery` `主机工具` · [条目](catalog/skills/ascendc-sync-audit.yaml)
- [cake-code-review](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/cake-code-review/SKILL.md) — 在评测前检查生成 AscendC 的结构和算法正确性。
  `CANNBot` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/cake-code-review.yaml)
- [cake-review](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/cake-review/SKILL.md) — 检视完整 Kernel 生成轨迹并记录流程和实现改进。
  `CANNBot` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/cake-review.yaml)
- [cann-review](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/code-review/cann-review/SKILL.md) — 按精确版本检查 GitCode PR 和跨仓契约，并进行反证检验。
  `AscendC Agent` `Operator support` `Review and delivery` `主机工具` · [条目](catalog/skills/cann-review.yaml)
- [cmake-race-auditor](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/common/cmake_auditor/SKILL.md) — 检查 CMake 生成文件依赖缺口和并行构建竞态。
  `AscendC Agent` `Operator support` `Review and delivery` `主机工具` · [条目](catalog/skills/cmake-race-auditor.yaml)
- [examples-docs-validator](https://gitcode.com/ascendc-agent/ascendc-skills/blob/0a46bf1d4fd373c3a8cc136aa6a4a958e9f4f236/skills/sample/examples-docs-validator/SKILL.md) — 检查样例 README、注释规范及文档与代码的一致性。
  `AscendC Agent` `Ascend C` `Review and delivery` `主机工具` · [条目](catalog/skills/examples-docs-validator.yaml)
- [git-version-management](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/git-version-management/SKILL.md) — 通过 Git worktree 隔离算子变体并记录阶段提交和来源。
  `CANNBot` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/git-version-management.yaml)
- [model-agent-ascendc-operator-code-review](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/ascendc-operator-code-review/SKILL.md) — 检查 AscendC 代码正确性和工程规范问题。
  `Model Agent` `Ascend C` `Review and delivery` `主机工具` · [条目](catalog/skills/model-agent-ascendc-operator-code-review.yaml)
- [op-dashboard](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/op-dashboard/SKILL.md) — 生成展示算法流、UB 切分、精度和性能的算子交互面板。
  `CANNBot` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/op-dashboard.yaml)
- [ops-direct-invoke-maintain](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-official/ops-direct-invoke/skills/ops-direct-invoke-maintain/SKILL.md) — 维护直调工作流契约、角色定义和回归检查。
  `CANNBot` `Ascend C` `Review and delivery` `主机工具` · [条目](catalog/skills/ops-direct-invoke-maintain.yaml)
- [task-progress](https://gitcode.com/cann/cannbot/blob/88637debe061dccc41cd6808f871f446f9c46c7a/plugins-community/collaborative-agent-kernel-evolution/skills/task-progress/SKILL.md) — 维护算子工作流进度、状态变化和待办任务。
  `CANNBot` `Ascend C` `Review and delivery` `Community` `主机工具` · [条目](catalog/skills/task-progress.yaml)
- [triton-operator-code-review](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/optimization/triton-operator-code-review/SKILL.md) — 静态检查 Triton Host/Device 正确性、API 误用和性能隐患。
  `Model Agent` `Triton` `Review and delivery` `主机工具` · [条目](catalog/skills/triton-operator-code-review.yaml)
- [triton-operator-doc-gen](https://gitcode.com/Ascend/model-agent/blob/b355135ad6e4e67861a83305ba115af8928cfb83/skills/documentation/triton-operator-doc-gen/SKILL.md) — 生成包含参数、约束和调用样例的 Triton 算子接口文档。
  `Model Agent` `Triton` `Review and delivery` `主机工具` · [条目](catalog/skills/triton-operator-doc-gen.yaml)
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
