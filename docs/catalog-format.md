# Catalogue format

[中文](catalog-format.zh.md) | English

The catalogue uses YAML schema version 1 and Python 3.10 or later. Install `requirements.txt` before invoking the scripts. Paths are relative to this repository unless a field explicitly refers to upstream source.

## Taxonomy and sources

`catalog/categories.yaml` contains ordered categories with stable `id`, bilingual `title`, and bilingual `description`. Empty categories remain available for contributions; generated README sections include populated categories only.

`catalog/sources.yaml` maps a source identifier to `repository`, `revision`, `license`, and `maintainer`. A revision is a full 40-character upstream Git commit. The resolver supports GitHub and GitCode HTTPS URLs and their respective raw-content endpoints. The license describes the source project; it does not change when the catalogue is licensed.

## Skill entries

See [a complete example](../catalog/skills/vllm-ascend-serving.yaml).

| Field | Meaning |
|---|---|
| `id` | Unique lowercase hyphenated identifier; matches the YAML filename. |
| `category` | Exactly one ID from the taxonomy. |
| `summary.zh`, `summary.en` | Short task-and-output descriptions. |
| `tags` | Frameworks and components; use consistent existing spellings where applicable. |
| `execution` | `offline`, `host`, `npu`, or `depends-on-checks`; see the usage guide for their meanings. |
| `role` | `task` or `workflow`; the latter coordinates multiple stages. |
| `source.project` | Key in `sources.yaml`. |
| `source.path` | Upstream relative path ending in `SKILL.md`. |
| `source.sha256` | SHA-256 of that file's exact bytes. |
| `review.status` | `definition-reviewed`, required for inclusion. |
| `review.date` | Quoted ISO date, e.g. `"2026-10-15"`. |
| `review.evidence` | Local source-inspection record. |
| `validation.status` | `not-recorded` or `reproduced`. |
| `validation.cases` | Empty for `not-recorded`; otherwise scoped reproductions. |

Validation case fields are documented in the [validation policy](validation-policy.md). Duplicate YAML keys and unknown entry fields are rejected.

## Commands

```bash
python3 scripts/render_catalog.py
python3 scripts/render_catalog.py --check
python3 scripts/validate_catalog.py
python3 scripts/validate_catalog.py --source-root vllm-ascend-skills=../vllm-ascend-skills
python3 scripts/validate_catalog.py --source-root cannbot-skills=../cannbot-skills
python3 scripts/validate_catalog.py --check-remote
```

Scripts resolve their default root from their own location. `--root /absolute/catalogue/path` selects another catalogue, including a disposable validation copy. Repeat `--source-root PROJECT=PATH` to inspect multiple upstream checkouts. Each checkout must be at the recorded upstream revision; an independently imported local Git snapshot has a different commit identity. Use a separate checkout at the pinned revision or run the remote hash check.

The renderer updates only the marked README blocks. Its check mode detects drift without writing. The validator checks metadata, evidence paths, local Markdown links and anchors, HTML image references, and SVG XML. Local source checks compare HEAD and definition hashes. Remote checks download pinned SKILL.md files and compare hashes; general external documentation URLs are outside that check.

The [CI workflow](../.github/workflows/validate.yml) runs catalogue validation and renderer drift checks. Execution validation is recorded through case evidence.
