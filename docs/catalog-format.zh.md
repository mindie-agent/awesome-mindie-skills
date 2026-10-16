# 目录条目格式

中文 | [English](catalog-format.md)

本目录采用 YAML schema 版本 1，维护脚本需要 Python 3.10 及以上版本。运行脚本前请先安装 `requirements.txt`。除非字段明确指向外部上游源码，所有路径均相对于本仓库根目录。

## 分类体系与上游来源

`catalog/categories.yaml` 定义有序的任务分类，包含稳定的 `id`、中英文双语 `title` 与双语 `description`。尚无条目的分类仍保留在分类体系中供后续贡献使用；自动生成的 README 目录区块仅展示包含条目的分类。

`catalog/sources.yaml` 将来源标识符映射到 `repository`、`revision`、`license` 和 `maintainer`。其中 `revision` 为完整的 40 位上游 Git commit SHA。URL 解析器支持 GitHub 与 GitCode 的 HTTPS 仓库链接及其对应的原始内容（raw）端点。`license` 记录上游源码项目自身的许可证，不因本目录仓库采用 CC0-1.0 而改变。

## 技能条目字段

完整示例可参考 [`catalog/skills/vllm-ascend-serving.yaml`](../catalog/skills/vllm-ascend-serving.yaml)。

| 字段 | 含义 |
|---|---|
| `id` | 唯一的小写连字符标识符，需与 YAML 文件名一致。 |
| `category` | 分类体系（`categories.yaml`）中的唯一分类 ID。 |
| `summary.zh`、`summary.en` | 简短的中英文任务与产出概述。 |
| `tags` | 涉及的框架与组件标签；请尽量沿用已有的规范拼写。 |
| `execution` | `offline`、`host`、`npu` 或 `depends-on-checks`；具体含义见[使用指南](getting-started.zh.md)。 |
| `role` | `task`（单项任务）或 `workflow`（协调多个阶段的工作流编排）。 |
| `source.project` | `sources.yaml` 中登记的来源项目键名。 |
| `source.path` | 上游仓库内以 `SKILL.md` 结尾的相对路径。 |
| `source.sha256` | 该 `SKILL.md` 文件原始字节的 SHA-256 摘要。 |
| `review.status` | `definition-reviewed`（收录必备状态，表示已完成定义审阅）。 |
| `review.date` | 带引号的 ISO 日期字符串，例如 `"2026-10-15"`。 |
| `review.evidence` | 仓库内 `evidence/` 下的源码定义审阅记录路径。 |
| `validation.status` | `not-recorded`（尚未记录运行复现）或 `reproduced`（已有复现记录）。 |
| `validation.cases` | 当状态为 `not-recorded` 时为空列表 `[]`；否则为指明环境与范围的复现案例列表。 |

复现案例（`validation.cases`）的详细字段要求见[验证规则](validation-policy.zh.md)。校验器会拒绝重复的 YAML 键或未定义的额外字段。

## 维护与校验命令

```bash
python3 scripts/render_catalog.py
python3 scripts/render_catalog.py --check
python3 scripts/validate_catalog.py
python3 scripts/validate_catalog.py --source-root vllm-ascend-skills=../vllm-ascend-skills
python3 scripts/validate_catalog.py --source-root cannbot-skills=../cannbot-skills
python3 scripts/validate_catalog.py --check-remote
```

脚本默认根据自身所在路径定位仓库根目录；可通过 `--root /absolute/catalogue/path` 指定其他目录（包括临时校验副本）。`--source-root PROJECT=PATH` 可重复传入以同时核对多个本地上游仓库检出。每个本地检出必须处于 `sources.yaml` 记录的精确 commit；若本地为独立导入的 Git 快照（commit SHA 不同），请使用检出在固定 commit 的独立副本或直接运行 `--check-remote`。

渲染脚本（`render_catalog.py`）仅更新中英文 README 中位于标记注释之间的目录区块；`--check` 模式仅检测内容是否过期而不改写文件。校验脚本（`validate_catalog.py`）检查 YAML 元数据、证据文件路径、仓库内 Markdown 链接与标题锚点、HTML 图片引用以及 SVG XML 合法性。本地源码检查会比对上游 `HEAD` 与各 `SKILL.md` 的 SHA-256；远程检查会下载固定版本的 `SKILL.md` 并核对哈希（普通外部文档链接不在远程哈希检查范围内）。

[CI 工作流](../.github/workflows/validate.yml)会自动运行目录元数据校验与 README 渲染一致性检查。运行复现结果通过案例证据文件独立记录。
