---
applyTo: "**/*.py"
---

# Python style for *themachinethatgoesping*

Apply these rules to all Python code. Match the existing conventions.

## General
- Start every file with the SPDX header (`MPL-2.0` for source).
- `from __future__ import annotations` at the top of modules.
- Use full **type hints** on public functions and methods.
- Use **numpy-style docstrings** (Parameters / Returns sections), as in
  `subprojects/tools/python/.../timeconv.py`.
- Formatting follows a black-compatible style (4-space indent). Keep imports
  tidy; only reformat code you actually change.

## Package structure & bindings
- Compiled cores are exposed as `themachinethatgoesping.<module>_nanopy`
  (nanobind). Pure-Python modules commonly `from
  themachinethatgoesping.<module>_nanopy.<sub> import *` and then add
  Python-only helpers on top (see the pattern in `tools/timeconv.py`).
- Python package sources live under each submodule's
  `python/themachinethatgoesping/<module>/`.
- Do not edit generated type stubs under `python/stubs/` or `*.pyi` by hand;
  they are produced by the stub-generation step during install.

## Testing
- Tests use **pytest** and live in each submodule's `python/tests/`. The
  aggregated `testpaths` are configured in the root `pyproject.toml`, so `pytest
  -v` from the repo root runs them all.
- Group related tests in a `Test_<area>` class and name methods
  `test_<thing>_should_<behaviour>`, matching the existing tests.
- Python tests import the **installed** module, so run `meson install -C
  builddir/` before `pytest` when C++ changed.
