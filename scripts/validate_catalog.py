"""Validate catalogue metadata, local links, LF hygiene, and upstream sources.

[Role]
CLI validator (`scripts/validate_catalog.py`) enforcing YAML schema invariants,
local Markdown/SVG links, Unix LF line-ending hygiene, and optional pinned-source
SHA-256 verification across `awesome-mindie-skills`.

[Invariants]
- Every listed skill must map to a valid taxonomy category, pinned 40-char commit
  revision, 64-char SHA-256 digest, and existing local review/validation evidence.
- Required root documents (`README.md`, `README.en.md`, `CONTRIBUTING.md`,
  `CONTRIBUTING.zh.md`, `AGENTS.md`) must exist; all non-binary repository files
  are streamed in `64 KiB` chunks (`O(1)` memory) to reject Windows CRLF (`\\r`).
- Never mask missing files, hash mismatches, or remote fetch timeouts as success.

[Timeouts & Locks]
- Lock-free read-only checks. Local `git rev-parse` calls use `timeout=15` with
  Windows `CREATE_NO_WINDOW`; remote HTTP fetches use `timeout=20` per request
  across a CPU- and memory-bounded worker pool (`<= 6` workers, `<= 2` when host
  free-memory telemetry is unavailable).

[Side-Effect Policy]
- Strictly read-only on the catalogue root and any `--source-root` checkouts;
  performs outbound HTTPS GETs only when `--check-remote` is explicitly passed.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

import yaml

from catalog import ROOT, load_catalog, local_file, require, source_url

BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".woff", ".woff2"}
SKIP_DIR_NAMES = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
REQUIRED_ROOT_DOCS = ("README.md", "README.en.md", "CONTRIBUTING.md", "CONTRIBUTING.zh.md", "AGENTS.md")
STREAM_CHUNK_BYTES = 65536


def anchors(text):
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    used = {}
    for title in re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE):
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        count = used.get(slug, 0)
        result.add(slug if count == 0 else f"{slug}-{count}")
        used[slug] = count + 1
    return result


def _raise_walk_error(error):
    raise error


def _iter_repo_files(root):
    resolved_root = root.resolve()
    for dirpath, dirnames, filenames in os.walk(resolved_root, onerror=_raise_walk_error):
        dirnames[:] = sorted(name for name in dirnames if name not in SKIP_DIR_NAMES)
        current = Path(dirpath)
        for filename in sorted(filenames):
            candidate = current / filename
            if not candidate.is_symlink() and candidate.is_file():
                yield candidate


def _text_file_has_carriage_return(path):
    if path.suffix.lower() in BINARY_SUFFIXES:
        return False
    with path.open("rb") as handle:
        first_chunk = handle.read(STREAM_CHUNK_BYTES)
        if not first_chunk or b"\x00" in first_chunk:
            return False
        if b"\r" in first_chunk:
            return True
        while chunk := handle.read(STREAM_CHUNK_BYTES):
            if b"\x00" in chunk:
                return False
            if b"\r" in chunk:
                return True
    return False


def check_lf_hygiene(root):
    gitattributes = root / ".gitattributes"
    editorconfig = root / ".editorconfig"
    require(gitattributes.is_file(), "Missing '.gitattributes' at repository root")
    require(
        "* text=auto eol=lf" in gitattributes.read_text(encoding="utf-8"),
        "'.gitattributes' must declare '* text=auto eol=lf'",
    )
    require(editorconfig.is_file(), "Missing '.editorconfig' at repository root")
    require(
        re.search(r"^\s*end_of_line\s*=\s*lf\s*$", editorconfig.read_text(encoding="utf-8"), re.MULTILINE),
        "'.editorconfig' must declare 'end_of_line = lf'",
    )
    resolved_root = root.resolve()
    offending = [
        str(path.relative_to(resolved_root).as_posix())
        for path in _iter_repo_files(resolved_root)
        if _text_file_has_carriage_return(path)
    ]
    require(not offending, "CRLF line endings prohibited in: " + ", ".join(offending))


def check_links(root):
    checked = 0
    documents = [local_file(root, name) for name in REQUIRED_ROOT_DOCS]
    for folder in ("docs", "evidence", "assets", ".github", "skills"):
        base = root / folder
        if base.is_dir():
            documents.extend(path for path in _iter_repo_files(base) if path.suffix.lower() == ".md")
    for document in documents:
        text = document.read_text(encoding="utf-8")
        # Example commands and templates do not create rendered links.
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        links = re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text)
        links += re.findall(r'(?:src|srcset)="([^"]+)"', text)
        for link in links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (document.parent / unquote(parsed.path)).resolve() if parsed.path else document.resolve()
            require(target.is_relative_to(root.resolve()), f"{document.name}: link escapes repository: {link}")
            require(target.exists(), f"{document.name}: broken link: {link}")
            if parsed.fragment and target.suffix == ".md":
                require(
                    unquote(parsed.fragment) in anchors(target.read_text(encoding="utf-8")),
                    f"{document.name}: missing anchor: {link}",
                )
            checked += 1
    for svg in sorted((root / "assets").glob("*.svg")):
        require(ET.parse(svg).getroot().tag == "{http://www.w3.org/2000/svg}svg", f"Invalid SVG: {svg}")
    return checked


def check_sources(sources, skills, mappings):
    no_window = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    for mapping in mappings:
        ident, separator, value = mapping.partition("=")
        require(separator and ident in sources and value, f"Invalid source mapping: {mapping}")
        root = Path(value).resolve()
        revision = subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            text=True,
            timeout=15,
            creationflags=no_window,
        ).strip()
        require(revision == sources[ident]["revision"], f"{ident}: checkout revision differs from catalogue")
        for item in skills:
            if item["source"]["project"] == ident:
                file = (root / item["source"]["path"]).resolve()
                require(file.is_relative_to(root), f"{item['id']}: source path escapes checkout")
                require(
                    hashlib.sha256(file.read_bytes()).hexdigest() == item["source"]["sha256"],
                    f"{item['id']}: local source hash differs",
                )


def _available_memory_mib():
    meminfo = Path("/proc/meminfo")
    if meminfo.is_file():
        for line in meminfo.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("MemAvailable:"):
                parts = line.split()
                if len(parts) >= 2 and parts[1].isdigit():
                    return int(parts[1]) // 1024
    if hasattr(os, "sysconf") and "SC_AVPHYS_PAGES" in os.sysconf_names and "SC_PAGE_SIZE" in os.sysconf_names:
        pages = os.sysconf("SC_AVPHYS_PAGES")
        page_size = os.sysconf("SC_PAGE_SIZE")
        if pages > 0 and page_size > 0:
            return (pages * page_size) // (1024 * 1024)
    return None


def _bounded_workers(cap=6, per_worker_mib=32, unknown_mem_cap=2):
    cpu_budget = max(1, os.cpu_count() or 1)
    avail_mib = _available_memory_mib()
    if avail_mib is None:
        return max(1, min(cap, unknown_mem_cap, cpu_budget))
    mem_budget = max(1, avail_mib // per_worker_mib)
    return max(1, min(cap, cpu_budget, mem_budget))


def check_remote(item, sources):
    try:
        request = Request(
            source_url(item, sources, raw=True),
            headers={"User-Agent": "awesome-mindie-skills-catalog-check"},
        )
        with urlopen(request, timeout=20) as response:
            content = response.read()
        require(hashlib.sha256(content).hexdigest() == item["source"]["sha256"], "source hash differs")
        return None
    except TimeoutError as error:
        return f"{item['id']}: timeout after 20s ({error})"
    except Exception as error:
        return f"{item['id']}: {error}"


def main():
    parser = argparse.ArgumentParser(description="Validate catalogue metadata, local links, and LF hygiene.")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--source-root",
        action="append",
        default=[],
        metavar="PROJECT=PATH",
        help="Verify a local upstream checkout and SKILL.md hashes",
    )
    parser.add_argument(
        "--check-remote",
        action="store_true",
        help="Fetch pinned upstream SKILL.md files and verify their hashes",
    )
    args = parser.parse_args()
    try:
        check_lf_hygiene(args.root)
        categories, sources, skills = load_catalog(args.root)
        links = check_links(args.root)
        check_sources(sources, skills, args.source_root)
        if args.check_remote:
            workers = _bounded_workers(cap=6, per_worker_mib=32, unknown_mem_cap=2)
            with ThreadPoolExecutor(max_workers=workers) as executor:
                failures = [
                    result
                    for result in executor.map(lambda item: check_remote(item, sources), skills)
                    if result
                ]
            require(not failures, "Remote source check failed:\n" + "\n".join(failures))
        print(
            f"Validated {len(skills)} skills, {len(categories)} taxonomy categories, "
            f"{len(sources)} source project(s), and {links} local links."
        )
        if args.source_root:
            print("Local source revisions and SKILL.md hashes match.")
        if args.check_remote:
            print("All pinned upstream SKILL.md files are reachable and match their recorded hashes.")
    except (TimeoutError, subprocess.TimeoutExpired) as error:
        print(f"TIMEOUT: {error}", file=sys.stderr)
        return 1
    except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
