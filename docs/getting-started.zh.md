# 查找与使用技能

中文 | [English](getting-started.md)

## 选择适用工作流

从[中文主页](../README.md)或[英文主页](../README.en.md)的“从任务开始”导航出发，根据目标工程产出选择匹配的技能条目，并打开其链接的 `SKILL.md`。阅读适用范围、输入要求、执行步骤与关联参考文件，同时核对执行条件标签以及条目元数据中记录的源码版本和验证证据。

本目录聚合各上游仓库维护的技能定义。每个来源仓库各自规定了安装要求与完整目录结构；克隆时请保留原始目录层次，以便技能内部的参考资料、脚本和相邻技能能够被正确引用。

## 获取上游技能集

根据所选条目在[来源记录](../catalog/sources.yaml)中声明的仓库地址与固定 commit 获取源码。以下命令可用于拉取当前目录收录的两套上游技能集合，请在本地工作目录中按需执行：

### vLLM Ascend Skills

```bash
git clone https://github.com/pisceskkk/vllm-ascend-skills.git
git -C vllm-ascend-skills checkout --detach 4e7417c3d88847a17ba6d61d6a9b748ad8e0bbc3
```

依赖项说明见上游仓库 `README.md`。其技能入口位于 `skills/<name>/SKILL.md`，同一仓库内包含配套参考文档、脚本与共享辅助库。

### CANNBot Skills

```bash
git clone https://gitcode.com/cann/cannbot-skills.git
git -C cannbot-skills checkout --detach 393564ae43f304426db2c206e361cd43b2811413
```

CANNBot 的技能入口分布在 `model/<name>/SKILL.md`、`ops/<name>/SKILL.md`、`graph/<name>/SKILL.md` 和 `tools/<name>/SKILL.md` 等路径下。入口可根据任务进一步路由至同级子技能、芯片架构专用说明或插件代理。插件发现与配置方式见上游安装指南。

## 加载技能说明

向 AI 编程助手或智能体提供所选条目 `source.path` 对应的本地 `SKILL.md` 路径、目标工程仓库路径及任务输入参数。若客户端支持自动发现技能目录，可按客户端文档配置技能搜索路径，并在会话开始时确认目标技能已加载。

通用调用提示词结构示例：

> 请阅读所选的 SKILL.md 及其相关参考文件，基于我提供的工程路径与输入数据完成任务。请先说明预期产出，执行适用的工作流步骤，并返回执行结果、关键证据路径以及尚未覆盖的边界。

- **离线 Profiling 分析**：提供 profiler 输出根目录及待排查的性能问题；
- **服务部署与执行**：提供模型权重路径、源码版本、NPU 设备列表、并行拓扑、负载参数及期望验证目标；
- **Triton 算子开发**：额外提供可信参考实现以及声明的 `shape`/`dtype`/`layout` 测试矩阵。

## 理解执行条件

| 取值 | 含义 |
|---|---|
| `offline` | 声明的分析工作流可直接基于已有 Profiling 或诊断产物离线运行；需按上游说明安装主机侧脚本依赖。 |
| `host` | 主机侧代码检视、Tiling 规划或 CANN Simulator 仿真等工具；可能需安装相应工具链或访问网络。 |
| `npu` | 完整工作流包含昇腾 NPU 实机运行、数据采集或性能计时；方案设计与代码阅读可在本地完成。 |
| `depends-on-checks` | 所需硬件环境取决于用户所选的具体验证检查项。 |

执行时请使用目标工程配套的软件栈版本，按需参考上游关于 CANN、PyTorch、`torch_npu`、vLLM Ascend、Triton、性能分析器及基准测试工具的说明。

例如，CANNBot 模型适配面向 PyTorch 及（按需选用的）`cann-recipes-infer`；量化条目面向已有的 `compressed-tensors` 权重产物；CATLASS、PyPTO、TileLang 与 Triton 入口需要各自的源码树或工具链；`ops-simulator` 依赖 CANN Simulator。维测工具在入口中声明了产品形态与权限前提：如 `asys` 面向 Ascend EP 环境，`msaicerr` 需在产生日志的原始运行环境中分析。如何解读已记录的兼容性与复现证据，请参阅[验证规则](validation-policy.zh.md)。

## 留存与分享结果

执行过程中请保留源码 commit、软硬件运行环境、用例配置、原始日志与产物路径。若希望分享可复现案例或提交条目修正，请按照[贡献指南](../CONTRIBUTING.zh.md)及[验证规则](validation-policy.zh.md)中定义的字段提交。
