# 定义审阅与运行验证规则

中文 | [English](validation-policy.md)

## 定义审阅（Definition Review）

本目录收录的每项技能均在固定上游源码版本（commit）下完成了带日期的定义审阅。定义审阅核对该技能声明的任务目标、核心工作流、预期产出、来源归属、许可证及执行条件，并将所检视的文件范围与结论记录在 `evidence/` 目录下。

首批定义审阅覆盖了 [17 个 vLLM Ascend 技能入口](../evidence/definition-review-2026-10-15.md)与 [36 个 CANNBot 技能入口](../evidence/cannbot-definition-review-2026-10-15.md)，记录了定义级检视结论与源码文件 SHA-256 摘要。实机或工具运行复现按下方规则单独记录。

## 运行复现（Execution Reproduction）

在尚未补充可复现的运行证据前，条目保持 `validation.status: not-recorded` 且 `cases: []`。若要将条目标记为 `reproduced`，需在 `validation.cases` 中提供至少一个包含以下全部字段的复现案例：

| 字段 | 必填内容 |
|---|---|
| `date` | 带引号的 ISO 执行日期字符串。 |
| `source_revision` | 完整的 40 位 commit SHA，需与条目当前记录的上游源码版本一致。 |
| `environment.hardware` | 设备型号、卡数与互联拓扑；若为离线分析，需注明主机环境并说明未执行 NPU 实机运行。 |
| `environment.software` | 相关的框架、运行时、编译器与工具版本。 |
| `scope` | 实际验证的任务、负载参数及精确验收判据。 |
| `evidence` | 仓库内 `evidence/` 下的 Markdown 证据记录路径，需包含配置、观测结果与可访问的产物说明。 |

证据文档应根据任务类型记录模型与权重版本、代码 commit、执行命令、输入参数、原始输出摘要、预期与实测结果对比以及已知限制。仅当声明的验收判据全部通过时，才可将条目标记为 `reproduced`；失败或未完成的尝试可保留在证据记录中供参考，但不将条目标为已复现。

每条复现案例仅证明其在所记录的软硬件环境与测试范围内成立；更广泛的硬件或软件版本兼容性需通过补充新案例来覆盖。离线分析案例的通过不能替代设备端执行工作流的实机验证结论。

## 上游版本更新

当上游技能仓库的固定 commit 更新时，需重新审阅变更后的技能定义并更新其 `sha256` 与审阅记录。在针对新版本完成复现验证之前，不得直接沿用旧版本的 `reproduced` 状态；历史复现证据文件可保留其原始 commit 与日期以备追溯。
