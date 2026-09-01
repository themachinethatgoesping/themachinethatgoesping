---
name: tmtgp-build-and-test
description: 'How to build, test and install themachinethatgoesping (C++ + nanobind + Python) using the VS Code task "Ping: Build and Test python (j8)" and the equivalent manual meson commands. USE when you changed C++/nanobind/Python source in themachinethatgoesping (or any subproject: echosounders, tools, navigation, gridding, pingprocessing, widgets, algorithms) and need to compile, run catch2/pytest tests, regenerate pybind docstrings, or install the module so Python can import it.'
---

# Build & test themachinethatgoesping

Always build from the **themachinethatgoesping** workspace folder
(`/home/ssd/src/themachinethatgoesping/themachinethatgoesping`), never from a subproject folder
(the subproject build tasks have known issues).

## Preferred: the VS Code task (full pipeline)
Run task **`Ping: Build and Test python (j8)`** from the `themachinethatgoesping` folder.
It runs, from `builddir`:
1. `make_pybind_doc.py` — regenerate `.docstrings/*.doc.hpp` from header comments (hash-based, only
   changed headers) — **must** run before compiling if you added/edited headers.
2. `meson compile -j8` — build the echosounders lib + `*_nanopy` modules + catch2 tests.
3. `meson test --print-errorlogs` — run all C++ tests.
4. `meson install --no-rebuild` — install the Python modules (+ regenerate stubs).
5. `pytest` — run the Python test suite.

Invoke it with the run-task tool: `id="shell: Ping: Build and Test python (j8)"`,
`workspaceFolder="/home/ssd/src/themachinethatgoesping/themachinethatgoesping"`.
Other useful tasks: **`Ping: Build and Test cpp`** (C++ only), **`Ping: Test python`** (pytest only).

## Manual equivalent (fast iteration in a terminal)
Prefix every terminal command with the dev environment:
```bash
source ~/.bash_aliases && use_dev_miniforge
```
Then, from `themachinethatgoesping/`:
```bash
# 1. regenerate docstrings (only when headers changed)
cd python && mamba run python make_pybind_doc.py && cd ..
# 2. compile
cd builddir && mamba run meson compile -j8
# 3. run C++ tests (all, or a subset by full test name)
mamba run meson test --print-errorlogs
mamba run meson test --print-errorlogs "themachinethatgoesping._echosounders.s7k.datagrams.s7kdatagram_.test"
# 4. install so Python can import the module
mamba run meson install
# 5. run python
cd .. && mamba run pytest -v
```
C++ test names are the dotted target names, e.g.
`themachinethatgoesping._echosounders.<format>.datagrams.<name>_.test` (wildcards like `s7k*` do
**not** match — use the full name).

## Gotchas
- If you added a new header, `make_pybind_doc.py` auto-creates its `.docstrings/*.doc.hpp` (it walks
  the tree). Committing a placeholder `.doc.hpp` (boilerplate + `//sourcehash: 0`) is safe insurance.
- Every new `.cpp`/`.hpp` and its `.doc.hpp` must be listed in the relevant `meson.build`
  (`src/themachinethatgoesping/echosounders/meson.build`, `src/nanomodule/meson.build`,
  `src/tests/meson.build`).
- After a successful build **+ install**, restart any running notebook kernel so it picks up the
  rebuilt module. Notebook-only edits do not need a build.
- The prefix `/ssd/local` is the install prefix (`-Dprefix='/ssd/local'`).
