# Header include analysis helpers

This directory contains two small utilities that help inspect the include
pressure of the C++ targets in this project when compiling with GCC.

## 1. Capture GCC include trees

```
python capture_gcc_headers.py --builddir <path-to-builddir>
```

The script replays the commands from `compile_commands.json` in **preprocessor
only** mode.  Each command runs the real GCC binary with the `-H` flag and writes
the include depth output to `header-logs/<target>/<object>.headers.log` inside
the chosen build directory.  The original build artefacts are untouched.

Useful switches:

- `--limit N` – capture the first _N_ commands (quick smoke test)
- `--force` – regenerate logs even if they exist
- `--debug` – show the exact commands that are re-run

## 2. Analyse the captured logs

```
python analyze_header_logs.py <builddir>/header-logs --top 40
```

The analyser walks every `.headers.log` file, reconstructs the include tree, and
reports a score for each header:

- **Score** = times the header appears × average descendants it brings in
- **Times** = number of occurrences across all logs
- **Includes caused** = average number of headers pulled in (including
  transitive includes)
- **Unique includes** = average unique headers pulled in
- **Logs** = number of translation units that referenced the header

Headers with a high score are good candidates for precompiled header (PCH)
experiments.  Sort or filter the output further to tailor PCH lists per module.
