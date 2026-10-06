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

## Split mode (nanobind) / abi3 — DEFAULT
Since nanobind 3, the project builds every `*_nanopy` extension in **split mode**: the binding code
(frontend) is compiled against the Python **stable ABI (abi3)** and the compiled `libnanobind`
(backend) lives in a **separate** Python module, `nanobind_backend`, imported at runtime. This is
controlled by the meson feature option **`split_mode`** (default **enabled**), declared in every
`meson_options.txt` (main + subprojects) and consumed in each subproject `meson.build`.

- Installed modules are named **`<fmt>_nanopy.abi3.so`** (not `…cpython-3XX-….so`). One wheel per
  platform then works on every Python ≥ 3.11 (`cp311-abi3`).
- **The dev env MUST have the backend**: `pip install nanobind-backend` (already a build/runtime
  requirement). Without it, `import themachinethatgoesping` fails with
  *"the nanobind backend module 'nanobind_backend' is not installed"*. The backend is a plain
  (non-limited-API) module, one per Python version; conda gets it from the themachinethatgoesping
  channel (recipe in `conda.recipe/nanobind-backend/`), pip from PyPI.
- **abi3 floor = 3.11** (matches `requires-python`). meson-python tags the wheel with the *build*
  interpreter's version, so **build wheels with the minimum Python (3.11)** to get `cp311-abi3`.
- **Classic (linked) build**: `meson setup … -Dsplit_mode=disabled` → modules are version-specific
  `…cpython-3XX-….so`, no backend needed. Both paths must keep compiling.
- ⚠️ **Switching modes leaves stale modules**: `meson install` does not delete the previously
  installed `*_nanopy.*.so`. Because Python prefers the version-specific `…cpython-3XX….so` over
  `…abi3.so`, stale classic modules **shadow** the abi3 ones (and vice-versa). After switching
  `split_mode`, delete the stale ones once:
  `rm <site-packages>/themachinethatgoesping/*_nanopy.cpython-*.so` (or the `*.abi3.so`). Fresh wheel
  / conda installs are unaffected.
- The split-mode frontend dep is provided by the nanobind wrap packagefile
  (`subprojects/tools/subprojects/packagefiles/nanobind/meson.build`, exposing `nanobind_frontend_dep`
  + `nanobind_stable_abi`); each subproject picks it with
  `get_option('split_mode').allowed()` and passes `limited_api: nanobind_limited_api` to
  `extension_module(...)`.
- abi3 means **no non-limited CPython C-API**. The only project dependency that needed a fix was the
  xtensor-python nanobind caster (`PySequence_Fast_GET_SIZE/_ITEMS` → `PySequence_Size/GetItem`),
  patched via a wrap `diff_files` patch
  (`subprojects/tools/subprojects/packagefiles/xtensor-python-abi3-limited-api.patch`).

## Gotchas
- If you added a new header, `make_pybind_doc.py` auto-creates its `.docstrings/*.doc.hpp` (it walks
  the tree). Committing a placeholder `.doc.hpp` (boilerplate + `//sourcehash: 0`) is safe insurance.
- Every new `.cpp`/`.hpp` and its `.doc.hpp` must be listed in the relevant `meson.build`
  (`src/themachinethatgoesping/echosounders/meson.build`, `src/nanomodule/meson.build`,
  `src/tests/meson.build`).
- After a successful build **+ install**, restart any running notebook kernel so it picks up the
  rebuilt module (notebook-only edits do not need a build). **Agent-driven kernel restart is a no-op
  here**: `run_vscode_command jupyter.restartkernel` / `notebook.restartKernel` report success but do
  NOT reload the module. Verify a module change in a FRESH `mamba run python` terminal process (it
  dlopens the freshly installed module) and ask the user to restart the kernel manually. See the
  **tmtgp-ping-jupyter** skill.
- The prefix `/ssd/local` is the install prefix (`-Dprefix='/ssd/local'`).
