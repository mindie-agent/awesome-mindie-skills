# Contributing

[中文](CONTRIBUTING.zh.md) | English

Help developers discover and share useful skills for Ascend inference engineering. Contributions can come from individual authors, engineering teams, or community collections. Each entry follows the same requirements for a clear task, traceable source, and documented execution conditions.

## Ways to contribute

- Suggest a skill or source collection using the [skill suggestion template](.github/ISSUE_TEMPLATE/suggest-skill.md). Explain the task it addresses and the expected result.
- Correct descriptions, translations, links, or prerequisites using the [entry issue template](.github/ISSUE_TEMPLATE/broken-entry.md), or submit a focused pull request.
- Share a reproducible execution case with the environment, scope, and evidence described in the [validation policy](docs/validation-policy.md).
- Improve task navigation and propose categories supported by concrete entries.

Keep descriptions useful to a reader choosing a skill. Credit its original maintainers and retain the source license information.

## Prepare a contribution

Run these commands from the catalogue repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Add an entry

1. Inspect the upstream `SKILL.md` at a full commit revision. Record its maintainer, license, relative path, and SHA-256 digest.
2. Add the upstream project to `catalog/sources.yaml` if needed. GitHub and GitCode repositories are supported; extend the URL resolver and validation together for another forge.
3. Create `catalog/skills/<skill-id>.yaml`. Follow the [catalogue format](docs/catalog-format.md) and choose one category from [the taxonomy](catalog/categories.yaml).
4. Write short Chinese and English summaries describing the task and output. Use tags for frameworks or components and the execution field for device requirements.
5. Add a dated source-inspection record under `evidence/`. Record execution reproduction separately according to the [validation policy](docs/validation-policy.md).
6. Generate both README catalogue blocks and run the checks below.

```bash
python3 scripts/render_catalog.py
python3 scripts/validate_catalog.py
python3 scripts/render_catalog.py --check
python3 scripts/validate_catalog.py --check-remote
```

The first three commands run locally. The last command fetches the pinned upstream skill definitions and verifies their content hashes. Network failures should be reported separately from catalogue errors.

To compare against a local source checkout, pass its registered source identifier and path:

```bash
python3 scripts/validate_catalog.py --source-root vllm-ascend-skills=../vllm-ascend-skills
python3 scripts/validate_catalog.py --source-root cannbot-skills=../cannbot-skills
```

Each checkout must be at the upstream commit recorded in `catalog/sources.yaml`. If your working copy is at another revision, use a separate checkout of the recorded commit or the remote check. Script options and metadata fields are described in the [catalogue format](docs/catalog-format.md).

## Update an entry

Changing a source project's pinned revision affects every entry referencing that source. Inspect those definitions, update their hashes and review records, and retain execution validation only when evidence exists for the new revision. Historical evidence files can remain for traceability.

When a skill changes its primary output, reconsider its category. Explain removals or replacements in the PR. Keep Chinese and English introductory text, examples, and generated entries aligned.

## Review expectations

- The source is accessible and has a clear maintainer and license.
- The task, input, expected output, and dependencies are understandable.
- The entry is distinct from existing entries, or explains its useful specialization.
- Device and framework compatibility claims have scoped evidence.
- Local links and generated README content pass checks.

Use the suggestion template for a new skill and the broken-entry template for stale sources or incorrect metadata. Contributions to this catalogue use its [CC0-1.0 license](LICENSE); upstream materials retain their licenses.
