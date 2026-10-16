# 品牌与视觉资产说明

中文 | [English](brand.md)

README 顶部横幅（Banner）将带有 Awesome 墨镜元素的 `mindie-agent` 吉祥物图标与目录标题、Ascend 推理工程定位及社区受众信息结合展示。白色吉祥物佩戴黑色墨镜，背景为紫色圆角方砖。浅色与深色两版 SVG 横幅均内嵌了同一张 PNG 图标，以确保在各类渲染环境中可作为独立自包含图像正常显示。

组织原始图标于 2026-10-15 获取自 [mindie-agent GitHub 组织主页](https://github.com/mindie-agent)（[头像源文件](https://avatars.githubusercontent.com/u/322608234?v=4&s=256)），其原始权利归所有者所有；本目录原创的视觉排版与素材采用仓库的 CC0-1.0 许可证。

| 资源文件 | 用途说明 |
|---|---|
| [mindie-agent-avatar.png](mindie-agent-avatar.png) | 组织原始图标快照，256 × 256 PNG。 |
| [mindie-agent-awesome.png](mindie-agent-awesome.png) | Awesome 墨镜风格改编版图标，内嵌于浅色与深色两版 README 横幅中。 |
| [logo.svg](logo.svg) | 目录辅助标识，128 × 128 viewBox。 |
| [logo-mono.svg](logo-mono.svg) | 单色目录标识，适用于浅色背景与印刷场景。 |
| [banner-light.svg](banner-light.svg) | 浅色主题 README 横幅，1200 × 320 viewBox。 |
| [banner-dark.svg](banner-dark.svg) | 深色主题 README 横幅，1200 × 320 viewBox。 |

README 通过 HTML `<picture>` 元素在支持深色模式的客户端自动切换深色横幅，并以浅色横幅作为默认回退。横幅下方的 Markdown 标题与导语完整保留了项目名称与用途说明，确保纯文本与无障碍阅读体验。

## 配色规范

- **组织图标**：保持原有的紫色底块与白色图形配色；
- **青绿色（Teal）**：浅色横幅强调色使用 `#0F766E`，深色背景强调色使用 `#5EEAD4`；
- **深灰蓝（Slate）**：正文或深色背景使用 `#0F172A`；
- **浅色文字**：`#F8FAFC`。

使用时请保持图标纵横比与透明通道。若后续更新 Awesome 墨镜改编图标，请同步更新两版 SVG 横幅中的内嵌 PNG 并预览浅色/深色主题效果。如需制作社交平台预览图（Social Preview），建议使用相同的 Awesome 图标、主标题与副标题，按 1280 × 640 画布独立排版。
