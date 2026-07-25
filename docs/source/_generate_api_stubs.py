# SPDX-FileCopyrightText: 2022 - 2026 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

"""
Generate a docs-only Python stub tree for sphinx-autoapi.

The C++ core of themachinethatgoesping is exposed through nanobind and therefore
has no importable ``.py`` sources that autoapi could parse. To document the
docstrings of the main package *and* all subpackages automatically (and with as
little maintenance as possible), this helper regenerates a clean stub tree from
the *installed* package every time the documentation is built:

1. ``nanobind.stubgen`` writes ``.pyi`` stubs for ``themachinethatgoesping`` and
   all importable submodules.
2. The stubs are renamed to ``.py`` (autoapi treats them as regular modules).
3. ``python/fix_stubs.py`` repairs the invalid Python syntax that nanobind emits
   for C++ template types and docstring indentation.

The result lives in a build-only directory (``docs/source/_autoapi_stubs``) that
is git-ignored, so no stale stubs are ever committed. On Read the Docs the
package is installed from PyPI, so the generated stubs always match the
documented release.

The function is intentionally defensive: if stub generation fails (for example
because the package is not installed) it returns ``None`` and the caller can
decide how to proceed.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

# Package to document (root package name determines the autoapi namespace).
PACKAGE_NAME = "themachinethatgoesping"


def _is_section_header(lines: list[str], index: int) -> bool:
    """True if ``lines[index]`` is a numpydoc section header (word + underline)."""
    if index + 1 >= len(lines):
        return False
    title = lines[index].strip()
    underline = lines[index + 1].strip()
    return (
        bool(title)
        and all(ch.isalpha() or ch == " " for ch in title)
        and len(underline) >= 3
        and set(underline) == {"-"}
    )


def _strip_methods_sections_in_text(text: str) -> str:
    """Drop numpydoc "Methods" sections from all docstrings in ``text``.

    autoapi already documents the real methods; the hand-written "Methods"
    list only produces duplicate ``.. method::`` object descriptions.
    """
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "Methods" and _is_section_header(lines, i):
            header_indent = len(lines[i]) - len(lines[i].lstrip(" "))
            i += 2  # skip the "Methods" header and its underline
            # Consume the section body until the next section header, a dedent
            # below the header indent, or the end of the docstring.
            while i < len(lines):
                stripped = lines[i].strip()
                if stripped == "":
                    # Peek at the next non-blank line to decide whether the
                    # section continues.
                    j = i
                    while j < len(lines) and lines[j].strip() == "":
                        j += 1
                    if j >= len(lines):
                        break
                    nxt_indent = len(lines[j]) - len(lines[j].lstrip(" "))
                    nxt = lines[j].strip()
                    if (
                        nxt_indent < header_indent
                        or nxt.startswith(('"""', "'''"))
                        or _is_section_header(lines, j)
                    ):
                        break
                    i = j
                    continue
                indent = len(lines[i]) - len(lines[i].lstrip(" "))
                if (
                    indent < header_indent
                    or stripped.startswith(('"""', "'''"))
                    or _is_section_header(lines, i)
                ):
                    break
                i += 1
            continue
        output.append(lines[i])
        i += 1
    return "".join(output)


def _strip_methods_sections(package_dir: Path) -> None:
    """Remove redundant numpydoc "Methods" sections from stub docstrings."""
    for py_file in package_dir.rglob("*.py"):
        text = py_file.read_text(encoding="utf-8")
        stripped = _strip_methods_sections_in_text(text)
        if stripped != text:
            py_file.write_text(stripped, encoding="utf-8")


def _load_fix_stubs_module(repo_root: Path):
    """Import ``python/fix_stubs.py`` as a module without requiring a package."""
    fix_stubs_path = repo_root / "python" / "fix_stubs.py"
    if not fix_stubs_path.exists():
        return None

    spec = importlib.util.spec_from_file_location("_ping_fix_stubs", fix_stubs_path)
    if spec is None or spec.loader is None:
        return None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def generate_api_stubs(source_dir: Path) -> Path | None:
    """Regenerate the docs-only stub tree and return its parent directory.

    Parameters
    ----------
    source_dir
        The sphinx source directory (``docs/source``).

    Returns
    -------
    Path or None
        The directory to hand to ``autoapi_dirs`` (containing the
        ``themachinethatgoesping`` package), or ``None`` if generation failed.
    """
    source_dir = Path(source_dir).resolve()
    repo_root = source_dir.parents[1]

    output_root = source_dir / "_autoapi_stubs"
    package_dir = output_root / PACKAGE_NAME

    # Clean previous output so removed symbols do not linger between builds.
    if output_root.exists():
        import shutil

        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    # 1. Generate .pyi stubs from the installed package.
    result = subprocess.call(
        [
            sys.executable,
            "-m",
            "nanobind.stubgen",
            "-m",
            PACKAGE_NAME,
            "-r",  # recursive: include all submodules
            "-O",
            str(package_dir),
            "-M",
            "py.typed",
        ]
    )
    if result != 0 or not package_dir.exists():
        print(
            f"[autoapi] Warning: stub generation failed (exit code {result}); "
            "the API reference may be incomplete.",
            file=sys.stderr,
        )
        return None

    # 2. Rename .pyi -> .py so autoapi parses them as regular modules.
    for pyi_file in package_dir.rglob("*.pyi"):
        pyi_file.rename(pyi_file.with_suffix(".py"))

    # 3. Repair invalid Python syntax emitted by nanobind for C++ templates.
    fix_stubs = _load_fix_stubs_module(repo_root)
    if fix_stubs is not None:
        fix_stubs.fix_stubs_in_directory(package_dir)
    else:
        print(
            "[autoapi] Warning: python/fix_stubs.py not found; stubs are used as-is.",
            file=sys.stderr,
        )

    # 4. Drop redundant numpydoc "Methods" sections (autoapi documents the real
    #    methods; the hand-written list only creates duplicate descriptions).
    _strip_methods_sections(package_dir)

    return output_root
