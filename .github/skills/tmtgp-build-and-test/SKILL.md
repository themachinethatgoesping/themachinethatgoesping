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
**If the run-task tool returns `Task not found`** (it often cannot resolve this folder-scoped task in
the multi-root `.code-workspace` — tried bare label and `shell:` prefix, both folder paths), fall back
to running the task's **exact** command yourself in a terminal (the full block in the "ALWAYS finish"
section below), `cwd = builddir`. That is functionally identical and is what the task runs.
Other useful tasks: **`Ping: Build and Test cpp`** (C++ only), **`Ping: Test python`** (pytest only).

### ⚠️ ALWAYS finish with the full `(j8)` command (the one that runs `meson compile mkdoc`)
Fast-iteration shortcuts (`meson compile`, `meson compile -j8`, the `(no doc)` / `(j8, no doc)` tasks,
`meson test`, `pytest`) **skip `meson compile mkdoc`** and therefore will **not** catch docstring
(mkdoc/libclang) parse failures. mkdoc is **hash-incremental** — it only re-parses a header whose
content changed — so a header you did not touch can carry a **latent** mkdoc failure that stays
dormant until the day you edit it. The authoritative final check is the full pipeline, run exactly as
the task does, from `builddir`:
```bash
source ~/.bash_aliases && use_dev_miniforge && \
mamba run meson compile mkdoc && \
mamba run meson compile -j8 && \
mamba run meson test --print-errorlogs && \
mamba run meson install --no-rebuild && \
cd .. && mamba run pytest
```
Never report a C++/nanobind/header change as "done/green" until this exact command (or the
`Ping: Build and Test python (j8)` task) has passed end-to-end. `meson compile` + `meson test` + `pytest`
passing is **not** sufficient — they do not run mkdoc.

## mkdoc needs compilable headers → two-phase build when you ADDED/CHANGED headers
`meson compile mkdoc` (step 1 of the `(j8)` task) runs pybind11-mkdoc, which **parses every changed
header with libclang using the main `builddir` `compile_commands.json`**. mkdoc therefore **fails
whenever a changed header does not compile** (a real C++ syntax/type error, a missing include, a bad
signature) — the failure is reported as a confusing clang/`mkdoc_log.log` traceback, NOT as the
underlying compiler error, and the stale `.doc.hpp` is kept (so `DOC(...)` for any **new** method is
still missing). Do **not** try to fix mkdoc from that traceback.

When you added new classes/methods or changed signatures, build in **two phases**:
1. **First** run **`Ping: Build and Test python (j8, no doc)`** (`meson compile -j8` **without**
   mkdoc). This shows the *real* compiler errors directly. Fix every error **except** the expected
   `DOC(...)` / `__doc_..._<newmethod>` "was not declared" errors — those cannot be resolved until the
   docstrings are regenerated, because the `.def(... DOC(...))` for a brand-new method references a
   doc var that does not exist yet.
2. **Then**, once the only remaining errors are those `DOC(...)` ones (i.e. all genuine header/code
   errors are gone), run the full **`Ping: Build and Test python (j8)`**. Its `meson compile mkdoc`
   step now parses the clean headers successfully, regenerates `.docstrings/*.doc.hpp` (creating the
   new `__doc_..._<newmethod>` vars), and the subsequent compile picks up the DOC strings for the
   nanobind module.

(If `(j8)` fails at the mkdoc step, that is the signal a header still does not compile → go back to
phase 1.) A convenient way to iterate phase 1 on just the affected subproject's C++ test is
`meson compile <full.test.target.name>` (see below) — it builds the catch2 test without the nanobind
DOC dependency, so you get test results even while new DOC vars are still missing.

Note: `make_pybind_doc.py` run **manually without `--build-root builddir`** falls back to each
*subproject* `builddir`, whose `compile_commands.json` may lack sibling-subproject include paths
(e.g. navigation → `tools/.../rotation.hpp` "file not found"). Always regenerate docs via the meson
target (`meson compile mkdoc`, i.e. the `(j8)` task) or pass `--build-root builddir`.

### mkdoc of a nanobind-dependent *library* header (`'nanobind/nanobind.h' file not found`)
mkdoc reads its clang `-I`/`-isystem` flags from `compile_commands.json`, keeping only entries whose
source file sits under `--target-filter` (which defaults to `--module-root`,
`subprojects/<mod>/src/themachinethatgoesping`). Most library headers there do **not** include
nanobind, so that worked — but a few *library* headers do (notably `tools_nanobind/*.hpp`:
`enumhelper.hpp`, `classhelper.hpp`, …). Their only nanobind `-I` flags live on the **nanomodule**
TUs under `subprojects/<mod>/src/nanomodule`, which the default filter **excludes**, so libclang
fails with `fatal error: 'nanobind/nanobind.h' file not found` and the header "fails to parse". The
fix (in the top-level [meson.build](../../../meson.build) `mkdoc-<mod>` `run_target`) is to pass an
explicit **`--target-filter subprojects/<mod>/src`** — broader than `--module-root`, so flags are
collected from the whole `src/` tree (library **+** nanomodule) while only the
`src/themachinethatgoesping` headers are documented. Collected flags are unioned (first-seen order
kept), so the extra include dirs are harmless for the modules that don't need nanobind.
Because mkdoc is hash-incremental, this latent failure only surfaces the moment you edit such a header
— another reason to **always finish with the full `(j8)` command** (see the rule above).

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
  platform then works on every Python ≥ 3.12 (`cp312-abi3`).
- **Conda is also build-once-per-OS (abi3).** The conda recipe
  (`conda.recipe/recipe.yaml`) sets `build.python.version_independent: true` (CEP 20) and
  `variants.yaml` pins a single Python (3.12), so rattler-build produces one package per OS
  (`subdir: <platform>` + `noarch: python`, run dep `python >=3.12`) that installs on 3.12-3.14. The
  recipe's `tests.python.python_version: [3.12, 3.13, 3.14]` imports the package **and each
  `*_nanopy` module** on all three versions (each test env pulls the matching per-version
  `nanobind-backend`). rattler-build relocates meson-python's `lib/pythonX.Y/site-packages` files
  into the noarch `site-packages` automatically.
- **The dev env MUST have the backend**: `pip install nanobind-backend` (already a build/runtime
  requirement). Without it, `import themachinethatgoesping` fails with
  *"the nanobind backend module 'nanobind_backend' is not installed"*. The backend is a plain
  (non-limited-API) module, one per Python version. **pip** gets it from PyPI (`nanobind-backend`);
  **conda** gets it from the `themachinethatgoesping` channel, where it is published by the **nanobind
  fork** `peter-urban/nanobind` (branch `meson-v3.1.0`), which builds it with **Meson**
  (`-Dnb_build_backend=true`, see that repo's `meson.build` + `conda.recipe/` + `rattler.yml`). The
  fork's `meson.build` mirrors the frontend packagefile and also builds the backend at `-O3` with full
  assertions; it deliberately does **not** pass `-mtls-dialect=gnu2`, so the backend has no
  `GLIBC_ABI_GNU2_TLS` requirement (portable). The fork builds each Python variant's package into an
  output dir **outside** the checkout (its recipe uses `source: path: ..`, so an in-repo output dir
  recurses into `ENAMETOOLONG`). The fork and the version pinned by the wrap must stay on the **same
  nanobind version** (currently 3.1.0) so backend and frontend ABIs match.
- **abi3 floor = 3.12** (matches `requires-python`; **Python 3.11 is no longer supported**).
  meson-python tags the wheel with the *build* interpreter's version, so **build wheels with the
  minimum Python (3.12)** to get `cp312-abi3`.
- **Classic (linked) build**: `meson setup … -Dsplit_mode=disabled` → modules are version-specific
  `…cpython-3XX-….so`, no backend needed. Both paths must keep compiling.
- **Standalone subproject builds are always classic.** The `split_mode` option defaults to
  **enabled** only in the top-level `themachinethatgoesping` `meson_options.txt`; every **subproject**
  `meson_options.txt` defaults it to **disabled** with `yield: true`. So the main-package build
  propagates `enabled` down to all subprojects (even nested ones, via `yield`), while a subproject
  built on its own (e.g. the `tools`/`echosounders`/… repo CI) uses the classic linked build and
  needs **no** backend. (Do **not** gate on `meson.is_subproject()` — a subproject of a subproject,
  e.g. `tools` under a standalone `algorithms` build, is still a subproject and would wrongly enter
  split mode, injecting `-DNB_BACKEND_MODULE` without `Py_LIMITED_API`.) Force either mode explicitly
  with `-Dsplit_mode=enabled|disabled`. This also avoids the Windows `python3.lib` limited-API link
  issue in standalone subproject CIs.
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
- ⚠️ **Windows abi3 / nested python deps**: Meson's `limited_api` only swaps the *top-level* python
  dependency of an `extension_module` to the stable `python3.lib`; a python dep **nested** inside an
  `InternalDependency` is NOT swapped and leaks the version-specific `python3XX.lib`, making the abi3
  `.pyd` depend on `python3XX.dll` → *"DLL load failed"* on any other Python. So any dependency that
  bundles a python dep (`nanobind_frontend_dep`, `tools_nanobind_dep`) takes it as
  `py_dep.partial_dependency(compile_args: true, includes: true)` (headers only, no link lib); the
  module's own top-level python dep does the (limited) linking. Keep the full python dep only in the
  classic `nanobind_dep`.
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

## Large semantic renames across the ping hierarchy (compiler-driven auto-fix)
A method name may exist on **both** a ping interface **and** many datagram/substruct classes (e.g.
`get_number_of_beams` is also on `BeamSelection` and on dozens of `*BeamsContainer`), so a global
text rename is **unsafe**. `clang-rename` is not installed; drive the rename with the **compiler**:
1. Blanket-rename the method (and its paired `has_`) **only inside the ping-class/binding files**
   (interfaces + `*/filedatatypes/*ping*.hpp` + the `py_*` ping bindings). This makes ping objects
   carry the new name while datagrams keep the old one.
2. Loop: `meson compile`, parse every **`error: '…' has no member named 'OLD'; did you mean 'NEW'?`**
   and apply `OLD→NEW` at that site; recompile. It **converges**: under-renamed ping call sites get
   `_legacy`, over-renamed datagram/selection calls get reverted — both via the compiler's suggestion.
   - **GCC diagnostics go to STDOUT** (not stderr) under meson/ninja, and use **Unicode curly quotes**
     `'…'` (U+2018/U+2019) — your regex must match those, not ASCII `'`.
   - **Beware closer-edit-distance wrong neighbours:** after you add a new sibling method, the
     compiler may suggest it instead of `_legacy` (e.g. `get_number_of_beams`→`get_number_of_sectors`,
     `get_beam_crosstrack_angles`→`get_beam_alongtrack_angles`). After convergence, grep the diff for
     any ping-object call rewritten to a *different* method (not `…_legacy`) and fix by hand.
3. Then regenerate docstrings (mkdoc) for the `_legacy` names and fix the `_2` overload DOC suffixes
   (`DOC_...(get_x_2)` → `DOC_...(get_x_legacy_2)`).
4. Python has no compiler: grep the test/py dirs for the renamed calls and fix ping-object ones
   (keep `selection.get_number_of_beams()` on `BeamSelection`); `pytest` is the oracle. Also rename
   the `t_pingfeature` enum entry + its `.value(...)` binding so the dynamic feature evaluator works.
   - Grep the **whole repo**, not just `tests/`, and **exclude build-artifact copies** that otherwise
     flood results: `grep -rn … --include=*.py | grep -v conda.recipe/output | grep -v /builddir/ |
     grep -v site-packages`. Rename **both** `get_<x>` and `has_<x>` at call sites (a stale
     `ping.bottom.has_<x>()` only blows up at runtime).
   - `pytest` is necessary but **not sufficient**: a stale caller inside a rarely-taken branch (e.g.
     `apply_pss(..., apply_pss_to_bottom=True)` in `select_get_wci_image.py`) passes all tests yet
     `AttributeError`s in real use — so the grep sweep is the primary oracle for Python, pytest the
     secondary. `pingprocessing`/`echosounders` Python loads **directly from source** (editable), so a
     `.py` edit is live without reinstall (only `meson install` is needed for C++/binding changes).

## Bootstrapping a brand-new header's `.doc.hpp` (before mkdoc has run)
A new header `#include ".docstrings/<name>.doc.hpp"` won't compile until the file exists. Create a
**placeholder** = the boilerplate of an existing `.doc.hpp` (`head -42 other.doc.hpp` — the
`#pragma once` + `__DOCSTRINGS_HPP__`-guarded macro block + the `#if defined(__GNUG__)` push) followed
by the matching `#pragma GCC diagnostic pop` / `#endif`, with **no** class-specific `mkd_doc_*` vars.
mkdoc then populates it. List the new `.cpp`, `.hpp` **and** `.docstrings/<name>.doc.hpp` in the
subproject `meson.build`.

## pingtools was split (navigation of the include/namespace)
`BeamSelection` / `BeamSampleSelection` / `ReadSampleRange` moved to **`algorithms::pingtools`**
(`algorithms/pingtools/…`, python `algorithms.pingtools`), while **`PingSampleSelector` moved to
`pingprocessing::pingtools`** (historically it was tied to `I_PingBottom`/`I_PingWatercolumn`). Inside
the algorithms library, include a sibling header **relatively**
(`"../../pingtools/beamselection.hpp"`), not as `<themachinethatgoesping/algorithms/…>` (the lib's own
include root is `…/algorithms`, not `…/src`).

## Project structure: pingprocessing ↔ echosounders (dependency inversion)
The format-independent **ping value interfaces** now live in **`pingprocessing::datatypes`**
(`subprojects/pingprocessing/src/.../pingprocessing/datatypes/`), **not** in echosounders:
`I_Ping`, `I_PingCommon`, `I_PingBottom`, `I_PingWatercolumn`, `I_PingFileData`, `PingInfo`, the
calibration base classes (`calibration::WaterColumnCalibration`, `MultiSectorWaterColumnCalibration`,
`AmplitudeCalibration`) and `PingContainer`. Python: `pingprocessing.datatypes.*` /
`pingprocessing_nanopy.datatypes.*`; their nanobind bindings live in the pingprocessing nanomodule
`src/nanomodule/py_datatypes/`.

### Shared `PingInfo` (channel id / timestamp / sensor configuration / navigation)
The per-ping meta info (channel id, timestamp, sensor configuration, navigation interpolator) lives in
a small **`PingInfo`** value class, **not** directly on `I_Ping` anymore. `I_PingCommon` holds it as a
`protected std::shared_ptr<PingInfo> _ping_info` (+ `has_ping_info()`/`get_ping_info()`/`set_ping_info()`
and a `ping_info` entry in `t_pingfeature`), so an `I_Ping` **and its `bottom()`/`watercolumn()`
sub-objects share the exact same `PingInfo` instance.
- `I_Ping` creates the `PingInfo` in its ctor and keeps the native thin wrappers
  (`has_/get_/set_timestamp`, `…_channel_id`, `…_sensor_configuration`, `…_navigation_interpolator_latlon`,
  `get_geolocation`, …) that simply delegate to `_ping_info`. Its **copy ctor / copy-assign deep-copy**
  the `PingInfo` so each ping (incl. every echosounder `deep_copy()`) stays independent.
- `PingInfo` stores the channel id (plus future string metadata) in a single
  `boost::flyweight<PingInfoData>` struct (so adding more strings costs **no** extra pointer), and the
  sensor configuration + navigation interpolator as their own flyweights. The `has_*` getters check the
  flyweight content (default-constructed ⇒ "not set") — there are **no** `_..._set` bool members.
- The echosounder ping implementations hand the ping's `PingInfo` pointer to the bottom/watercolumn (see
  the `tmtgp-echosounders-add-format` skill). Nanobind exposes `ping_info` as a **read-only property**
  (`reference_internal`) + `get_ping_info()`; `bottom.ping_info` / `watercolumn.ping_info` return the
  same object as `ping.ping_info`.

Dependency direction (reversed from before): **`pingprocessing` depends on `algorithms` + `navigation`
+ `tools`** (NOT echosounders); **`echosounders` depends on `pingprocessing`** and implements the
format-specific derived classes (`KMALLPingBottom : pingprocessing::datatypes::I_PingBottom`, etc.).
Only the `datatypes` sub-namespace moved — the **file-reading interfaces stay in echosounders**
(`filetemplates::datainterfaces::{I_DatagramInterface,I_InputFileHandler,I_NavigationDataInterface,…}`,
`filetemplates::datastreams/…`, `filetemplates::cache_structures/…`, `filecache`).

Python gotchas from the move:
- pingprocessing `__init__.py` must **not** do `from ...pingprocessing_nanopy import *` — that shadows
  the **python** `pingprocessing.watercolumn` subpackage (which has `helper`/`image`/`echograms`) with
  the C++ `pingprocessing_nanopy.watercolumn` submodule → `ImportError: cannot import name 'helper'`.
  Expose the C++ interfaces explicitly: `from themachinethatgoesping.pingprocessing_nanopy import
  datatypes`.
- pingprocessing python annotates ping params as `datatypes.I_Ping` via `from
  themachinethatgoesping.pingprocessing_nanopy import datatypes` — **never** `echosounders.datatypes.*`
  (that attribute no longer exists; a stale annotation makes **`meson install`/stubgen fail**, because
  Python-3.14 deferred annotations are evaluated by nanobind's `stubgen.py`).
- meta/top-level `__init__` import order already lists pingprocessing **before** echosounders.

## ⚠️ `boost::flyweight` member across two extension `.so`s → `bad_array_new_length`
A `boost::flyweight<T>` member of a class in a **static lib linked into two Python extension `.so`s**
(any `pingprocessing::datatypes` interface now qualifies — the pingprocessing static lib is linked into
**both** `pingprocessing_nanopy.so` and `echosounders_nanopy.so`) gets a **per-`.so` factory**
(hidden-visibility static). If that flyweight is **lazily interned from shared code and later
destroyed**, the intern (in one `.so`'s factory) and destroy (in the other's) mismatch and **corrupt
the heap** → a later unrelated allocation throws **`std::bad_array_new_length`** (Python:
`MemoryError: std::bad_array_new_length`). It looks like it "accumulates" across objects and only bites
**after** the interning getter was called **and** the holding object was destroyed, then the next
allocation runs. It is layout-sensitive UB, so **gdb/valgrind mask it**; bisect in **fresh processes**
(the corruption is process-global) by which getter, called before destruction, makes the next
allocation throw.
- Real case: `I_PingWatercolumn::get_beam_sample_selection_all()` interned
  `boost::flyweight<BeamSampleSelection> _beam_sample_selection_all`; every amplitude getter
  (`get_amplitudes`/`ap`/`rp`/`rv`/`pp`/`pv`/`power`) routes through it → crash on next file-handler
  construction.
- **Fix = keep the flyweight, give it a cross-module factory**: add
  `#include <boost/flyweight/intermodule_holder.hpp>` and declare
  `boost::flyweight<BeamSampleSelection, boost::flyweights::intermodule_holder> _beam_sample_selection_all;`.
  `intermodule_holder` "guarantees a unique instance across all dynamic modules", so interning in one
  `.so` and destroying in another use the **same** factory. No getter/`.cpp` changes needed.
- **🚫 NEVER downgrade a flyweight to a plain value member to work around this (or any) bug.**
  `boost::flyweight` is a deliberate memory + performance choice (structural dedup of identical values,
  cheap copy/compare/hash by handle); replacing it with a plain `T` member silently regresses memory
  and performance and is **out of scope** — changing a chosen data structure is not an acceptable
  "fix". Preserve the design and fix the real cause (here: the per-`.so` factory → `intermodule_holder`).
- Flyweights that are **set from the echosounders derived class and only read in the base** are
  **safe** — they intern+destroy entirely inside `echosounders_nanopy.so`. This now applies to the
  `PingInfo` flyweights (channel-id `flyweight<PingInfoData>` struct, `_sensor_configuration`,
  `_navigation_interpolator_latlon`): they are set during `read_pings` (echosounders) and the `PingInfo`
  is destroyed together with the owning ping in `echosounders_nanopy.so`. Keep the `ping_info` nanobind
  property on **`reference_internal`** (never return the `shared_ptr<PingInfo>` by value) so Python can
  never independently outlive-and-destroy a `PingInfo` in `pingprocessing_nanopy.so` — that would
  reintroduce the cross-module intern/destroy mismatch.
