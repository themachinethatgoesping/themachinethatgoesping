# Copilot / AI agent instructions for *themachinethatgoesping*

> Purpose of this file: give AI assistants (GitHub Copilot coding agent, Copilot
> Chat in VS Code, and similar tools) enough up-front context that they do **not**
> need to re-explore the whole repository on every task. This keeps answers
> correct **and** reduces token usage / AI cost. Keep it short, factual and
> up to date.

## What this project is

*themachinethatgoesping* (short: **ping** / `tmtgp`) processes multibeam and
singlebeam echosounder data. Performance-critical cores are written in **C++23**
and exposed to **Python** via **nanobind** (older code uses pybind11). Pure
Python tools/widgets sit on top of that core.

This repository is the **super-project**: it does not contain much code of its
own. Instead it aggregates the module repositories as **git submodules** under
`subprojects/` and builds them together with **Meson**.

Submodules (each is its own repo, keep changes scoped to the right one):

| Submodule | Language | Purpose |
|-----------|----------|---------|
| `subprojects/tools` | C++/Python | shared functions & interfaces (base for everything) |
| `subprojects/meta` | build | shared meson helpers / metadata |
| `subprojects/algorithms` | C++/Python | absorption, raytracing, bottom detection, … |
| `subprojects/navigation` | C++/Python | store & transform navigation data |
| `subprojects/echosounders` | C++/Python | read/write/process EK80, Kongsberg .all/.wcd/.kmall |
| `subprojects/pingprocessing` | Python | higher-level processing (e.g. echograms) |
| `subprojects/widgets` | C++/Python | GUI widgets |
| `subprojects/gridding` | Python | gridding functions |

Most real work happens **inside a submodule**, not in this super-project. Before
editing, confirm which submodule owns the code. Do not commit unrelated
submodule pointer bumps.

## Build, test, recursively (verified commands)

The super-project builds **all** subprojects in one Meson tree. C++ is C++23, so
use **gcc ≥ 14** or **clang ≥ 18**. Meson must be **≥ 1.8.1**.

1. **Get the submodules first (recursive)** — nothing builds without this:

   ```bash
   git submodule update --init --recursive
   # or: ./ci_scripts/init_submodules.sh
   ```

2. **Configure** (same flags as CI, static linking + unity build):

   ```bash
   CXX=g++-14 meson setup builddir \
     -Dunity=on -Dunity_size=9999999 \
     -Dpython.install_env=auto \
     --default-library=static
   ```

3. **Compile everything (recursively builds all subprojects):**

   ```bash
   meson compile -C builddir/
   ```

4. **C++ tests (Catch2):**

   ```bash
   meson test -C builddir/ --print-errorlogs
   ```

5. **Install** — required before the Python tests, because they import the
   installed module:

   ```bash
   meson install -C builddir/     # prefix a sudo if installing system-wide
   ```

6. **Python tests (pytest):** test paths for every subproject are configured in
   `pyproject.toml`, so just run:

   ```bash
   pytest -v
   ```

### Dependencies (important for cost / offline runs)

C++ dependencies (boost, eigen3, fmt, xtensor, magic_enum, nanobind, catch2,
proj, geographiclib, …) are pulled by **Meson wrap files** (`.wrap`) and
therefore need **network access** on the first configure. CI avoids this by
running inside the prebuilt container
`ghcr.io/themachinethatgoesping/ubuntu-dep:latest`, which already contains all
dependencies. When the network is restricted, prefer that image (see
`.github/workflows/copilot-setup-steps.yml`) instead of repeatedly retrying wrap
downloads — retrying wastes time and tokens.

If you only touch Python or docs, you usually do **not** need a full C++ build.

## Coding style (match the existing code — do not reformat unrelated code)

### General
- Every source file starts with an **SPDX header**. Source code is `MPL-2.0`;
  build files (`meson.build`, `meson_options.txt`, `pyproject.toml`) are
  `CC0-1.0`. Copy the exact header style already used in neighbouring files.
- Keep changes **surgical**. Do not run a formatter over files you did not
  functionally change.

### C++ (see also `.github/instructions/cpp.instructions.md`)
- Formatting is enforced by **`.clang-format`** (custom Mozilla-based: 4-space
  indent, 100-column limit, pointers bind left, braces on their own line for
  functions/classes/control statements). Always format with it.
- Namespaces: `themachinethatgoesping::<module>::<submodule>`.
- File names are lowercase (`i_interpolator.hpp`, `stringconversion.hpp`).
  Headers use `#pragma once` and, right after the SPDX header, include the
  generated docstrings: `#include ".docstrings/<name>.doc.hpp"`.
- Naming: classes `PascalCase`; interface/abstract classes prefixed `I_`
  (`I_Interpolator`); enums prefixed `t_` (`t_extr_mode`) with `o_…` option
  wrappers (`o_extr_mode`); template params like `t_float` / `XType`; private
  members prefixed with an underscore (`_extr_mode`).
- Documentation is Doxygen (`@brief`, `@param`, `@tparam`, `@return`,
  `@authors`).
- Classes that are printable/serializable use the classhelper pattern: a
  `__printer__(...)` method returning `classhelper::ObjectPrinter` plus the
  `__CLASSHELPER_DEFAULT_PRINTING_FUNCTIONS__` macro (gives `info_string`,
  `print`, `to_binary`, `from_binary`, `copy`, `==`).

### Python (see also `.github/instructions/python.instructions.md`)
- `from __future__ import annotations`, full **type hints**, **numpy-style
  docstrings**.
- Pure-Python modules typically extend the compiled module by re-exporting from
  `themachinethatgoesping.<module>_nanopy...` and adding Python-only helpers.
- Bindings live in `src/nanomodule/**` and follow the `init_m_<name>` /
  `init_c_<name>` submodule-registration pattern.

## Do / don't for AI agents
- **Do** keep edits inside the correct submodule and mirror the surrounding
  style exactly.
- **Do** build/test only what your change affects; reuse `builddir/` instead of
  reconfiguring from scratch.
- **Don't** upgrade dependency or `.wrap` versions unless the task asks for it.
- **Don't** rewrite git history or bump submodule pointers as a side effect.
- **Don't** commit `builddir/`, `__pycache__/`, generated `.docstrings/`, or
  secrets.
