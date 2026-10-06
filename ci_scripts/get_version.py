#!/usr/bin/env python3
"""Print the single-source project version.

The version of ``themachinethatgoesping`` is declared exclusively in the
top-level ``meson.build`` (``project(... version: 'X.Y.Z' ...)``). Everything
else derives from it:

* ``pyproject.toml`` uses ``dynamic = ["version"]`` so meson-python already
  reads the version from ``meson.build``.
* The conda recipe (``conda.recipe/recipe.yaml``) reads it from the
  ``PKG_VERSION`` environment variable, which CI (and the pixi ``build-conda``
  task) populate with the output of this script.

Usage::

    python ci_scripts/get_version.py            # -> e.g. 0.35.2.dev6
    python ci_scripts/get_version.py --is-dev   # -> exit 0 if dev, 1 otherwise

A *dev* version is any version whose release segment is followed by a
``.devN`` / ``devN`` suffix (PEP 440 developmental release), e.g.
``0.35.2.dev6``.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

# Repository root is the parent of the directory containing this script.
ROOT = pathlib.Path(__file__).resolve().parent.parent
MESON_BUILD = ROOT / "meson.build"


def read_version(meson_build: pathlib.Path = MESON_BUILD) -> str:
    """Extract the project() version string from the top-level meson.build."""
    text = meson_build.read_text(encoding="utf-8")

    # Isolate the project(...) call so a stray `version:` kwarg elsewhere in the
    # file cannot be picked up by mistake.
    start = text.find("project(")
    if start == -1:
        raise SystemExit(f"error: no project() call found in {meson_build}")

    # Find the matching closing parenthesis of project(...).
    depth = 0
    end = -1
    for i in range(start + len("project("), len(text)):
        ch = text[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            if depth == 0:
                end = i
                break
            depth -= 1
    block = text[start:end] if end != -1 else text

    match = re.search(r"version\s*:\s*'([^']+)'", block)
    if not match:
        raise SystemExit(f"error: no project version found in {meson_build}")
    return match.group(1)


# PEP 440 developmental release suffix, e.g. 1.2.3.dev4 / 1.2.3dev4 / 1.2.3.dev
_DEV_RE = re.compile(r"\.?dev\d*$")


def is_dev(version: str) -> bool:
    return bool(_DEV_RE.search(version))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--is-dev",
        action="store_true",
        help="exit 0 if the version is a .dev release, 1 otherwise",
    )
    args = parser.parse_args(argv)

    version = read_version()

    if args.is_dev:
        return 0 if is_dev(version) else 1

    print(version)
    return 0


if __name__ == "__main__":
    sys.exit(main())
