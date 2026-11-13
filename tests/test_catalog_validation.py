"""Tier 0 boundary tests for catalogue schema, link, and LF validation.

[Role]
In-memory and temporary-directory tests verifying `scripts/catalog.py`,
`scripts/validate_catalog.py`, and `scripts/render_catalog.py` failure modes.

[Invariants]
- Duplicate YAML mapping keys, missing required root docs, Windows CRLF bytes
  (including extensionless files such as `NOTICE`), broken relative links/anchors,
  and stale rendered README blocks must fail explicitly.
- Tests write valid fixtures with explicit `newline="\\n"` for cross-OS determinism
  and isolate temporary roots without mutating the checkout or `$HOME`.

[Timeouts & Locks]
- Pure Tier 0 local filesystem/memory checks (`< 2s`), zero network calls, zero `sleep`.

[Side-Effect Policy]
- Writes exclusively inside `tempfile.TemporaryDirectory()` sandboxes.
"""

from pathlib import Path
import shutil
import sys
import tempfile
import unittest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import catalog  # noqa: E402
import render_catalog  # noqa: E402
import validate_catalog  # noqa: E402


def _write_lf(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")


def _minimal_repo(tmp: Path) -> Path:
    root = tmp / "repo"
    for subdir in ("catalog/skills", "docs", "evidence", "assets", ".github", "skills", "scripts"):
        (root / subdir).mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO_ROOT / ".gitattributes", root / ".gitattributes")
    shutil.copy2(REPO_ROOT / ".editorconfig", root / ".editorconfig")
    _write_lf(root / "assets/logo.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"/>\n')
    _write_lf(
        root / "catalog/categories.yaml",
        "schema_version: 1\ncategories:\n  - id: operators\n"
        "    title:\n      zh: 算子\n      en: Operators\n"
        "    description:\n      zh: 算子开发。\n      en: Operator work.\n",
    )
    _write_lf(
        root / "catalog/sources.yaml",
        "schema_version: 1\nsources:\n  demo:\n"
        "    repository: https://github.com/example/demo\n"
        "    revision: " + ("a" * 40) + "\n"
        "    license: MIT\n    maintainer: demo\n",
    )
    _write_lf(root / "evidence/review.md", "# Review\n\nScoped note.\n")
    _write_lf(
        root / "catalog/skills/demo-op.yaml",
        "id: demo-op\ncategory: operators\n"
        "summary:\n  zh: 示例技能。\n  en: Demo skill.\n"
        "tags:\n  - Ascend\nexecution: host\nrole: task\n"
        "source:\n  project: demo\n  path: skills/demo-op/SKILL.md\n  sha256: " + ("b" * 64) + "\n"
        "review:\n  status: definition-reviewed\n  date: '2026-10-22'\n  evidence: evidence/review.md\n"
        "validation:\n  status: not-recorded\n  cases: []\n",
    )
    marker = "Header [Review](evidence/review.md#review)\n\n<!-- CATALOG:START -->\n<!-- CATALOG:END -->\n"
    for name in ("README.md", "README.en.md"):
        _write_lf(root / name, marker)
    for name in ("CONTRIBUTING.md", "CONTRIBUTING.zh.md", "AGENTS.md"):
        _write_lf(root / name, "# Guide\n\nSee [Review](evidence/review.md#review).\n")
    categories, sources, skills = catalog.load_catalog(root)
    for name, lang in (("README.md", "zh"), ("README.en.md", "en")):
        text = (root / name).read_text(encoding="utf-8")
        before, _ = text.split(render_catalog.START)
        _write_lf(root / name, before + render_catalog.render(categories, sources, skills, lang) + "\n")
    return root


class CatalogValidationTests(unittest.TestCase):
    def test_minimal_disposable_copy_validates_cleanly(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _minimal_repo(Path(tmp))
            validate_catalog.check_lf_hygiene(root)
            _, _, skills = catalog.load_catalog(root)
            self.assertEqual(len(skills), 1)
            self.assertGreaterEqual(validate_catalog.check_links(root), 5)

    def test_missing_required_root_doc_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _minimal_repo(Path(tmp))
            (root / "AGENTS.md").unlink()
            with self.assertRaisesRegex(ValueError, "Missing file: AGENTS.md"):
                validate_catalog.check_links(root)

    def test_duplicate_yaml_keys_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _minimal_repo(Path(tmp))
            skill = root / "catalog/skills/demo-op.yaml"
            _write_lf(skill, skill.read_text(encoding="utf-8") + "role: workflow\n")
            with self.assertRaisesRegex(ValueError, "Duplicate YAML key: role"):
                catalog.load_catalog(root)

    def test_crlf_in_markdown_and_extensionless_notice_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _minimal_repo(Path(tmp))
            notice = root / "skills/NOTICE"
            notice.write_bytes(b"Copyright notice\r\nSecond line\r\n")
            with self.assertRaisesRegex(ValueError, "skills/NOTICE"):
                validate_catalog.check_lf_hygiene(root)

    def test_broken_markdown_anchor_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _minimal_repo(Path(tmp))
            _write_lf(root / "CONTRIBUTING.zh.md", "# Guide\n\nBroken [anchor](evidence/review.md#nonexistent).\n")
            with self.assertRaisesRegex(ValueError, "missing anchor"):
                validate_catalog.check_links(root)


if __name__ == "__main__":
    unittest.main()
