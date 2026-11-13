"""Render bilingual README catalogue blocks from YAML.

[Role]
CLI renderer (`scripts/render_catalog.py`) generating the deterministic Markdown
blocks between `CATALOG:START` and `CATALOG:END` in `README.md` and `README.en.md`.

[Invariants]
- Surrounding editorial sections outside the ordered marker pair are preserved.
- `--check` fails with exit code 1 on stale blocks without mutating files.
- Writes explicitly use Unix LF (`newline="\\n"`).

[Timeouts & Locks]
- Pure local file rendering (`< 2s`), lock-free, zero subprocesses or network calls.

[Side-Effect Policy]
- Read-only when `--check` is set; updates `README.md` and `README.en.md` otherwise.
"""

import argparse
from pathlib import Path
import sys

import yaml

from catalog import ROOT, load_catalog, source_url

START = "<!-- CATALOG:START -->"
END = "<!-- CATALOG:END -->"
LABELS = {
    "zh": {
        "execution": {"npu": "执行需 NPU", "offline": "离线分析", "host": "主机工具", "depends-on-checks": "设备取决于检查项"},
        "review": "定义已审阅", "not-recorded": "运行验证未记录", "reproduced": "已有复现记录",
        "workflow": "流程编排", "record": "条目", "proof": "验证记录",
    },
    "en": {
        "execution": {"npu": "NPU execution", "offline": "Offline analysis", "host": "Host tools", "depends-on-checks": "Hardware depends on checks"},
        "review": "Definition reviewed", "not-recorded": "Execution validation not recorded", "reproduced": "Reproduction recorded",
        "workflow": "Workflow", "record": "Metadata", "proof": "Validation record",
    },
}


def render(categories, sources, skills, lang):
    labels = LABELS[lang]
    used = [category for category in categories.values() if any(s["category"] == category["id"] for s in skills)]
    count = f"{len(skills)} 个技能 · {len(used)} 个分类" if lang == "zh" else f"{len(skills)} skills · {len(used)} categories"
    lines = [START, "", count, ""]
    reviewed = sum(item["review"]["status"] == "definition-reviewed" for item in skills)
    reproduced = sum(item["validation"]["status"] == "reproduced" for item in skills)
    coverage = (
        f"定义已审阅：{reviewed} · 已有运行复现记录：{reproduced}。具体范围见各条目记录。"
        if lang == "zh"
        else f"Definitions reviewed: {reviewed} · Entries with execution reproductions: {reproduced}. See each entry's metadata for scope."
    )
    lines += [coverage, ""]
    table_header = (
        "| 来源项目 | 已收录 | 维护者 | 许可证 |"
        if lang == "zh"
        else "| Upstream Source | Listed | Maintainer | License |"
    )
    lines += [table_header, "|---|---|---|---|"]
    for ident, project in sources.items():
        total = sum(item["source"]["project"] == ident for item in skills)
        if total:
            lines.append(
                f"| [{ident}]({project['repository']}) | {total} | {project['maintainer']} | {project['license']} |"
            )
    lines.append("")
    for category in used:
        lines.append(f"- [{category['title'][lang]}](#{category['id']})")
    for category in used:
        lines.extend(["", f'<a id="{category["id"]}"></a>', "", f"### {category['title'][lang]}", "", category["description"][lang], ""])
        for item in skills:
            if item["category"] != category["id"]:
                continue
            tags = item["tags"] + [labels["execution"][item["execution"]]]
            if item["role"] == "workflow":
                tags.append(labels["workflow"])
            if item["validation"]["status"] == "reproduced":
                tags.append(labels["reproduced"])
            metadata = f"[{labels['record']}](catalog/skills/{item['id']}.yaml)"
            proofs = "".join(f" · [{labels['proof']}]({case['evidence']})" for case in item["validation"]["cases"])
            lines.extend([
                f"- [{item['id']}]({source_url(item, sources)}) — {item['summary'][lang]}",
                "  " + " ".join(f"`{tag}`" for tag in tags) + f" · {metadata}{proofs}",
            ])
    lines.extend(["", END])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail when generated content is stale")
    parser.add_argument("--root", type=Path, default=ROOT, help="Catalogue root (also supports disposable copies)")
    args = parser.parse_args()
    try:
        categories, sources, skills = load_catalog(args.root)
        stale = []
        for name, lang in (("README.md", "zh"), ("README.en.md", "en")):
            path = args.root / name
            original = path.read_text(encoding="utf-8")
            if original.count(START) != 1 or original.count(END) != 1 or original.index(START) >= original.index(END):
                raise ValueError(f"{name}: expected exactly one ordered catalogue marker pair")
            before, rest = original.split(START)
            _, after = rest.split(END)
            updated = before + render(categories, sources, skills, lang) + after
            if updated != original:
                stale.append(name)
                if not args.check:
                    path.write_text(updated, encoding="utf-8", newline="\n")
        if stale and args.check:
            raise ValueError("Stale generated content: " + ", ".join(stale))
        print("README catalogue blocks are current." if args.check else "Rendered both README catalogues.")
    except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
