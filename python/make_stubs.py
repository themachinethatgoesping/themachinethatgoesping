#!/bin/env python3
"""
Generate Python type stubs for themachinethatgoesping using nanobind's native stubgen.

This script can be run:
1. Manually: cd python && python make_stubs.py
2. Via meson: meson compile -C builddir stubs

The module must be installed and importable before running this script.
"""

import os
import shutil as sh
import subprocess
import sys
from pathlib import Path

# Determine the output directory (python/stubs relative to this script)
script_dir = Path(__file__).parent.resolve()
stubs_dir = script_dir / 'stubs'

if stubs_dir.exists():
    sh.rmtree(stubs_dir)

# Use nanobind's native stubgen (better quality than pybind11-stubgen)
# -m: module to process
# -r: recursive (process all submodules)
# -O: output directory
# -M: generate py.typed marker file
result = subprocess.call([
    sys.executable, '-m', 'nanobind.stubgen',
    '-m', 'themachinethatgoesping',
    '-r',  # recursive
    '-O', str(stubs_dir),
    '-M', 'py.typed',
])

if result != 0:
    print(f"Warning: nanobind.stubgen exited with code {result}", file=sys.stderr)
    sys.exit(result)

# Rename all .pyi files in stubs/themachinethatgoesping to .py
# (for autoapi compatibility - it expects .py files)
stubs_pkg_dir = stubs_dir / 'themachinethatgoesping'
if stubs_pkg_dir.exists():
    for pyi_file in stubs_pkg_dir.rglob('*.pyi'):
        py_file = pyi_file.with_suffix('.py')
        pyi_file.rename(py_file)
    print(f"Stubs generated successfully in {stubs_dir}")
else:
    print(f"Warning: Expected stubs directory not found: {stubs_pkg_dir}", file=sys.stderr)

# Output a stamp for meson custom_target
print("stubgen completed")