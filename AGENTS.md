# Repository guidance

- Maintain Chinese `README.md` and English `README.en.md` (along with paired `*.zh.md` / `*.md` guides where present) with matching examples and reciprocal links. Write standalone governance, topic, and evidence Markdown documents in English.
- Edit skill metadata in `catalog/skills/`, taxonomy in `catalog/categories.yaml`, and upstream snapshots in `catalog/sources.yaml`.
- Generate README content between `CATALOG:START` and `CATALOG:END` with `python3 scripts/render_catalog.py`. Preserve the surrounding editorial content.
- Each skill has one primary category. Use tags for frameworks and components, and record execution conditions separately.
- Link to upstream skill directories at a full commit revision. Preserve their complete layout when documenting installation.
- A definition review records source inspection. Hardware validation requires a reproducible case, environment and evidence for the same source revision.
- Keep runtime validation records in `evidence/`; reusable maintenance rules belong in `docs/`.
- Run `python3 scripts/validate_catalog.py` and `python3 scripts/render_catalog.py --check` after changes. Use a disposable copy to exercise invalid-input cases.
- The catalogue and original assets use CC0-1.0. Referenced projects retain their own licenses.
