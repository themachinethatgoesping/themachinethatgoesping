---
name: tmtgp-ping-jupyter
description: 'How to work with themachinethatgoesping (theping) in Jupyter notebooks in this workspace: the dev conda/mamba environment the kernels use, the CRITICAL rule that after a C++/nanobind rebuild+install the notebook kernel must be RESTARTED (and that agent-driven restart is a no-op here, so verify module changes in a fresh terminal python process and ask the user to restart), loading echosounder files (find_files_and_index + FileHandler), common inspection patterns (datagram_interface, datagrams(), get_pings, ping.file_data.datagrams()), the widget/matplotlib magics, test-data locations, and reliable notebook-cell editing. USE whenever running, testing or debugging ping code in a .ipynb (e.g. the s7k test.ipynb / view.ipynb). For building see tmtgp-build-and-test.'
---

# Working with theping in Jupyter notebooks

Practical workflow for running/validating `themachinethatgoesping` (imported as `theping`) in
notebooks in this workspace (e.g. `/home/data/test_data/s7k/test.ipynb`,
`/home/data/aqualicous/view.ipynb`). For building the C++/nanobind modules see
**tmtgp-build-and-test**.

## The dev environment
The notebook kernels run in the **`dev` mamba/conda env** (Python 3.14) where `meson install` puts the
modules (`.../envs/dev/lib/python3.14/site-packages/themachinethatgoesping`). In a terminal, reproduce
it with `source ~/.bash_aliases && use_dev_miniforge` and run scripts via `mamba run python ...`. A
notebook typically opens with `%matplotlib widget` (and `%gui qt6` for the Qt viewers) then
`import themachinethatgoesping as theping`.

## CRITICAL: rebuild → RESTART the kernel (and how to verify)
`themachinethatgoesping` is a compiled extension. A running kernel keeps the **old** `.so` in memory,
so after you rebuild+install (the `Ping: Build and Test python (j8)` task) the notebook still runs the
old module until its **kernel is restarted**. Notebook-only edits (pure Python in a cell) do **not**
need a build or restart.

- **Agent-driven restart is UNRELIABLE here.** `run_vscode_command` with `jupyter.restartkernel` /
  `notebook.restartKernel` reports "Finished"/"Failed" but does **not** actually restart the kernel
  (the module stays old). Probe it: run a cell using a previously-defined variable (e.g. `fh`); if it
  still resolves, the kernel did not restart. (The VS Code execution counter is global and does not
  reset on restart, so it is not a reliable signal.)
- **Authoritative verification of a C++/module change = a FRESH terminal process**, which dlopens the
  freshly installed module:
  ```bash
  source ~/.bash_aliases && use_dev_miniforge && mamba run python - <<'PY'
  import themachinethatgoesping as theping
  # ... exercise the changed API ...
  PY
  ```
- After verifying in a fresh process, **tell the user to restart the notebook kernel manually**
  (Restart button / "Jupyter: Restart Kernel") and re-run the setup cells — the agent cannot do it
  reliably.
- Tell whether the kernel has the new code by checking a *known-new behavior*, e.g. after the
  identifier-string fix `datagram_interface.datagrams().count_datagrams_per_type()` returns **string**
  keys (`{'1003': ...}`); the old module returned enum keys (`{t_S7KDatagramIdentifier.Position: ...}`)
  or raised.

## Loading files & common inspection patterns
```python
files, index = theping.echosounders.index_functions.find_files_and_index(folder, ['.s7k'])  # or .kmall/.kmwcd
fh = theping.echosounders.s7k.S7KFileHandler(files, index, show_progress=False, mp_cores=8)
print(fh)                                            # file infos + per-type datagram counts
fh.datagram_interface.print()                        # interface printer (per-type counts)
d = fh.datagram_interface.datagrams()                # whole-file variant container
d.print(); d.count_datagrams_per_type()              # per-type counts (string keys, robust)
raw  = fh.datagram_interface.datagrams_raw()          # unparsed
typed = fh.datagram_interface.datagrams('7027')       # typed; accepts number/name/enum (o_ wrapper)
```
Pings (after the ping interface is implemented — see tmtgp-echosounders-ping-interface):
```python
pings = fh.get_pings()
p = pings[100]
p.get_timestamp(); p.get_geolocation()               # geolocation needs navigation set on the ping
p.file_data.datagrams().print()                      # ALL datagrams that belong to this ping
p.file_data.datagrams('7027')[0]                     # a typed record of the ping
```
Higher-level: `theping.pingprocessing.*` (filter_pings, overview, watercolumn.echograms),
`theping.widgets.WCIViewerQt(pings, ...)`, `EchogramViewerQt(...)` (need `%gui qt6`).

## Reliable notebook-cell editing (agent)
- `edit_notebook_file` with `editType='edit'` can **silently fail on large cells** (returns
  "Notebook edited successfully" but the content is unchanged). The message
  "The notebook file was successfully edited." = applied; "Notebook edited successfully. Use the
  read_file…" = likely a silent no-op. Prefer **insert a new cell + delete the old one** (both
  reliable) and always `copilot_getNotebookSummary` / grep to confirm.
- Notebook edits (and `run_notebook_cell`) act on the **in-memory** VS Code model; the `.ipynb` on
  disk stays stale until the user saves. `copilot_getNotebookSummary` shows the live model (trust it);
  disk `grep`/`read_file` may be stale. Do **not** hand-write the `.ipynb` JSON while it is open.

## Test data
- s7k: `/home/data/test_data/s7k/{kh1908, thomaslake, ultfarms}` (ignore any `index/` subfolder).
  `kh1908` has the full record set (nav 1003/1012/1013/1015/1016 + ping 7000/7004/7027/7028/7058);
  `thomaslake`/`ultfarms` are smaller (ping 7000/7027/7028/7042).
- kmall: `/home/data/aqualicous/test_1` (contains `#CHE`, a record not in the enum — good for testing
  robustness of per-type counting / printing).

## Gotchas
- A `UnicodeDecodeError` or `nanobind::str(): conversion error!` from a `print()` / `info_string()`
  usually means a datagram-identifier→string conversion emitted **raw bytes** (invalid UTF-8); for a
  numeric-id format (s7k) the fix is a decimal string, not `int_as_string` (see
  tmtgp-echosounders-datagram-indexing).
- `count_datagrams_per_type()` returning `ValueError: <n> is not a valid t_...Identifier` means a file
  has a record type not named in the enum and a binding returned the raw enum to Python; the container
  now returns **string** keys to avoid this (see tmtgp-cpp-nanobind-style).
- Qt viewers need `%gui qt6` in the first cell; matplotlib-widget plots need `%matplotlib widget`.
