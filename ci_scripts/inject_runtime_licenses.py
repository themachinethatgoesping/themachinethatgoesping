# SPDX-FileCopyrightText: 2026 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

"""Inject license texts for bundled runtime libraries into a built wheel.

macOS wheels are built with Homebrew GCC and the GCC runtime libraries
(libstdc++, libgcc_s, libgomp) are bundled into the wheel by delocate /
repairwheel. Those libraries are licensed ``GPL-3.0-or-later WITH
GCC-exception-3.1``; this helper adds their license texts to the wheel under
``<name>-<version>.dist-info/licenses/`` and updates ``RECORD`` accordingly so
the files install cleanly with pip.

Usage::

    python inject_runtime_licenses.py path/to/pkg.whl \\
        --license GPL-3.0-or-later.txt=COPYING3 \\
        --license GCC-Runtime-Library-Exception-3.1.txt=COPYING.RUNTIME
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import zipfile
from pathlib import Path


def _record_hash(data: bytes) -> str:
    digest = base64.urlsafe_b64encode(hashlib.sha256(data).digest()).decode().rstrip("=")
    return f"sha256={digest}"


def inject(wheel: Path, files: dict[str, bytes]) -> None:
    with zipfile.ZipFile(wheel) as zf:
        names = zf.namelist()
        try:
            dist_info = next(n.split("/")[0] for n in names if n.endswith(".dist-info/RECORD"))
        except StopIteration as exc:
            raise SystemExit(f"{wheel}: no .dist-info/RECORD found") from exc
        record_name = f"{dist_info}/RECORD"
        contents = {n: zf.read(n) for n in names}

    record_lines = contents[record_name].decode().splitlines()
    for target, data in files.items():
        arcname = f"{dist_info}/licenses/{target}"
        contents[arcname] = data
        record_lines.append(f"{arcname},{_record_hash(data)},{len(data)}")
    contents[record_name] = ("\n".join(record_lines) + "\n").encode()

    tmp = wheel.with_name(wheel.name + ".tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zf:
        for arcname, data in contents.items():
            zf.writestr(arcname, data)
    tmp.replace(wheel)
    print(f"{wheel.name}: added {len(files)} license file(s): {', '.join(files)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wheel", type=Path)
    parser.add_argument(
        "--license",
        action="append",
        default=[],
        metavar="TARGET=SOURCE",
        help="Add SOURCE into the wheel as <dist-info>/licenses/TARGET.",
    )
    args = parser.parse_args()

    files: dict[str, bytes] = {}
    for spec in args.license:
        target, sep, source = spec.partition("=")
        if not sep:
            raise SystemExit(f"invalid --license entry (expected TARGET=SOURCE): {spec}")
        files[target] = Path(source).read_bytes()

    inject(args.wheel, files)


if __name__ == "__main__":
    main()
