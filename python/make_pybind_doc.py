#!/usr/bin/env python3
"""Regenerate pybind11 docstrings for the themachinethatgoesping C++ modules.

Delegates to :mod:`pybind11_mkdoc.meson_mkdoc`, which reads the compiler include
flags from the Meson build's ``compile_commands.json`` and pins libclang to the
active Python environment (so it works with both the fork and upstream
pybind11_mkdoc).

Examples
--------
    # all modules (needs a configured build dir for the include flags)
    python python/make_pybind_doc.py --build-root builddir
    # one module, force regeneration
    python python/make_pybind_doc.py --module navigation --regenerate --build-root builddir
    # debug a single header with full clang diagnostics
    python python/make_pybind_doc.py --module pingprocessing --only echogrambase --verbose --build-root builddir

The equivalent Meson targets supply the build dir automatically:
    meson compile -C builddir mkdoc              # all modules
    meson compile -C builddir mkdoc-navigation   # one module
"""

import argparse
import os
import sys

from pybind11_mkdoc.meson_mkdoc import main as driver_main

MODULES = ["tools", "navigation", "algorithms", "echosounders", "pingprocessing"]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--module", choices=MODULES, help="Only this module (default: all).")
    parser.add_argument("--regenerate", action="store_true", help="Ignore the source hash.")
    parser.add_argument("--renew", action="store_true", help="Delete all .docstrings folders.")
    parser.add_argument("--build-root", default=None, help="Build dir with compile_commands.json.")
    parser.add_argument("--only", default=None, metavar="SUBSTR", help="Only headers containing SUBSTR.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Echo clang diagnostics to the console.")
    args = parser.parse_args()

    forwarded = []
    if args.regenerate:
        forwarded.append("--regenerate")
    if args.renew:
        forwarded.append("--renew")
    if args.only:
        forwarded += ["--only", args.only]
    if args.verbose:
        forwarded.append("--verbose")
    if args.build_root:
        forwarded += ["--build-root", os.path.abspath(args.build_root)]

    exit_code = 0
    for mod in [args.module] if args.module else MODULES:
        sub = os.path.join(ROOT, "subprojects", mod)
        doc_header = os.path.join(sub, "src", "nanomodule", "new_doc_header.hpp")
        if not os.path.isfile(doc_header):
            print(f"skipping {mod}: {doc_header} not found", file=sys.stderr)
            continue
        print(f"=== {mod} ===")
        sys.argv = [
            sys.argv[0],
            "--module-root", os.path.join(sub, "src", "themachinethatgoesping"),
            "--doc-header", doc_header,
            *forwarded,
        ]
        exit_code |= driver_main()
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
