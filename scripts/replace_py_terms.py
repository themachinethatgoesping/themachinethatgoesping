#!/usr/bin/env python3
"""Bulk rename targeted terms within Python source files.

This utility walks a directory tree, finds every ``.py`` file, and applies a
couple of straightforward string substitutions:

* Replace every occurrence of ``_nanopy`` with ``_cppy``.
* Replace every occurrence of ``themachinethatgoesping`` with
  ``themachinethatgoesping_cppy``.

Example
-------

    ./replace_py_terms.py path/to/folder --dry-run

Use ``--apply`` to actually rewrite files once you are satisfied with the
preview.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterator


REPLACEMENTS = (
    ("_nanopy", "_cppy"),
    ("themachinethatgoesping", "themachinethatgoesping_cppy"),
)


def iter_python_files(root: Path) -> Iterator[Path]:
    """Yield every ``.py`` file beneath *root* (inclusive)."""
    if root.is_file() and root.suffix == ".py":
        yield root
        return

    for path in root.rglob("*.py"):
        if path.is_file():
            yield path


def transform_contents(text: str) -> tuple[str, bool]:
    """Apply the configured replacements and report if anything changed."""
    changed = False
    for needle, replacement in REPLACEMENTS:
        if needle in text:
            text = text.replace(needle, replacement)
            changed = True
    return text, changed


def process_file(path: Path, apply_changes: bool, verbose: bool) -> bool:
    """Process *path* and optionally write back the transformed text."""
    original = path.read_text(encoding="utf-8")
    updated, changed = transform_contents(original)

    if not changed:
        if verbose:
            print(f"UNCHANGED: {path}")
        return False

    if apply_changes:
        path.write_text(updated, encoding="utf-8")
        if verbose:
            print(f"UPDATED:   {path}")
    else:
        print(f"WOULD UPDATE: {path}")

    return True


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        type=Path,
        help="Directory (or single .py file) to process",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write the replacements back to disk (default is dry-run)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print a line for every inspected file",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    root: Path = args.root

    if not root.exists():
        raise SystemExit(f"error: path does not exist: {root}")

    total = 0
    changed = 0

    for file_path in iter_python_files(root):
        total += 1
        if process_file(file_path, args.apply, args.verbose):
            changed += 1

    summary = f"Processed {total} file(s); "
    if args.apply:
        summary += f"updated {changed}."
    else:
        summary += f"would update {changed}."
    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
