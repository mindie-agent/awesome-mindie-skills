# 参与贡献

中文 | [English](CONTRIBUTING.md)

欢迎共同完善面向 Ascend（昇腾）推理工程的 Agent Skills 共享目录。贡献可以来自个人开发者、工程团队或社区技能集合。所有收录条目遵循统一标准：任务边界清晰、上游来源可追溯、执行条件明确记录。

## 贡献方式

- **推荐新技能或技能集合**：使用[技能推荐 Issue 模板](.github/ISSUE_TEMPLATE/suggest-skill.md)，说明该技能解决的工程任务与预期产出；
- **修正条目信息**：若发现中英文摘要、链接、前置依赖或元数据有误，可使用[条目问题反馈模板](.github/ISSUE_TEMPLATE/broken-entry.md)提交 Issue，或直接提交修正 PR；
- **补充运行复现案例**：按照[验证规则](docs/validation-policy.zh.md)记录软硬件环境、验证范围与结果证据；
- **改进任务导航与分类**：结合具体技能条目优化分类说明或提出新分类建议。

编写条目说明时，请站在使用者的角度帮助你快速判断是否适用，并保留原作者署名与上游许可证信息。

## 本地环境准备

在仓库根目录下创建虚拟环境并安装依赖：

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## 新增技能条目

1. 在固定的完整 Git commit 下审阅上游 `SKILL.md`，记录维护者、许可证、仓库内相对路径以及该文件的 SHA-256 摘要；
2. 如需引入新的上游仓库，先在 `catalog/sources.yaml` 中登记。当前支持 GitHub 与 GitCode 仓库；若引入其他代码托管平台，需同步扩展 URL 解析与校验脚本；
3. 创建 `catalog/skills/<skill-id>.yaml`，字段遵循[条目格式](docs/catalog-format.zh.md)，并从[分类体系](catalog/categories.yaml)中选择唯一分类；
4. 编写简明的中英文双语摘要（`summary.zh` 与 `summary.en`），准确描述任务目标与产出，使用 `tags` 标注框架/组件，使用 `execution` 标注执行环境要求；
5. 在 `evidence/` 目录下新增带日期的定义审阅记录；若有运行复现结果，按[验证规则](docs/validation-policy.zh.md)单独记录；
6. 重新生成中英文 README 的目录区块并运行本地校验：

```bash
python3 scripts/render_catalog.py
python3 scripts/validate_catalog.py
python3 scripts/render_catalog.py --check
python3 scripts/validate_catalog.py --check-remote
```

前三条命令在本地离线运行；最后一条命令会拉取固定的上游 `SKILL.md` 原文并校验其 SHA-256 哈希（网络异常应与目录格式错误区分报告）。

若希望针对本地克隆的上游仓库核对版本与哈希，可传入已注册的来源标识与本地路径：

```bash
python3 scripts/validate_catalog.py --source-root vllm-ascend-skills=../vllm-ascend-skills
python3 scripts/validate_catalog.py --source-root cannbot-skills=../cannbot-skills
```

本地上游检出必须处于 `catalog/sources.yaml` 记录的 commit；若本地工作区在其他分支或提交上，请使用检出在固定 commit 的独立副本或运行 `--check-remote`。脚本参数与字段细则见[条目格式](docs/catalog-format.zh.md)。

## 更新已有条目

升级某个来源项目在 `catalog/sources.yaml` 中的固定 commit 会影响该项目下的全部技能条目。请逐一核对变更后的 `SKILL.md` 定义，更新文件哈希与定义审阅记录；仅当新版本已有对应复现证据时才保留 `reproduced` 状态，历史证据文件可继续保留以供追溯。

若某项技能的核心产出发生变化，请重新评估其所属分类，并在 PR 中说明删除或替换的原因。请保持中英文导览说明、调用示例与生成目录的一致性。

## 审阅要求

- 上游源码公开可访问，且具备明确的维护者与许可证；
- 任务目标、输入参数、预期产出与软硬件依赖清晰易懂；
- 与已有条目边界区分明确，或说明了具体的专有适用场景；
- 关于设备或框架兼容性的声明具备明确范围与证据支撑；
- 本地链接、标题锚点与生成的 README 区块全部通过脚本校验。

推荐新技能请使用技能推荐模板，反馈失效链接或元数据错误请使用条目问题模板。向本目录仓库提交的内容采用 [CC0-1.0 许可证](LICENSE)，所链接的上游技能仍保留其各自项目的许可证。
