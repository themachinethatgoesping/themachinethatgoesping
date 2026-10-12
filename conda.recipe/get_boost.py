#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0
"""
Download and *statically* compile the Boost libraries that themachinethatgoesping
needs, with the SAME compiler as the current build environment (read from the
``CC`` / ``CXX`` / ``AR`` environment variables), so the result is ABI-compatible
with the project. Produces a self-contained Boost install (headers + static libs)
under ``--prefix``; point meson at it with ``BOOST_ROOT=<prefix>`` and build with
``-Ddynamic_boost=disabled`` (static).

Works on Linux (gcc), macOS (clang/libc++) and Windows (clang-cl + llvm-lib).
Only the libraries listed in ``BOOST_LIBRARIES`` are compiled (everything else in
Boost is header-only); mirror of the ``--with-<lib>`` approach used in
``.github/workflows/ci-windows.yml``.

Usage:
    python conda.recipe/get_boost.py --prefix <install-dir> [--jobs N] [--force]
"""

# =============================================================================
#  Configuration  --  edit these two lines to change what Boost is built
# =============================================================================
BOOST_VERSION   = "1.92.0"          # Boost release to download and build
BOOST_LIBRARIES = ["iostreams"]     # non-header-only libs to compile (static)
# =============================================================================

import argparse
import os
import platform
import shutil
import subprocess
import sys
import tarfile
import urllib.request
from pathlib import Path


def log(msg: str) -> None:
    print(f"[get_boost] {msg}", flush=True)


def run(cmd, cwd=None, env=None) -> None:
    """Run a command, echoing it; raise on failure."""
    printable = cmd if isinstance(cmd, str) else " ".join(str(c) for c in cmd)
    log(f"$ {printable}")
    subprocess.run(cmd, cwd=cwd, env=env, shell=isinstance(cmd, str), check=True)


def download(version: str, dest_dir: Path) -> Path:
    """Download the Boost source tarball (with mirrors) into dest_dir."""
    v_ = version.replace(".", "_")
    name = f"boost_{v_}.tar.gz"
    out = dest_dir / name
    if out.exists() and out.stat().st_size > 0:
        log(f"already downloaded: {out}")
        return out
    urls = [
        f"https://archives.boost.io/release/{version}/source/{name}",
        f"https://sourceforge.net/projects/boost/files/boost/{version}/{name}/download",
    ]
    last_err = None
    for url in urls:
        try:
            log(f"downloading {url}")
            tmp = out.with_suffix(".part")
            with urllib.request.urlopen(url) as resp, open(tmp, "wb") as fh:
                shutil.copyfileobj(resp, fh)
            tmp.replace(out)
            log(f"downloaded {out} ({out.stat().st_size // (1024 * 1024)} MiB)")
            return out
        except Exception as exc:  # noqa: BLE001 - try the next mirror
            last_err = exc
            log(f"  failed: {exc}")
    raise RuntimeError(f"could not download Boost {version}: {last_err}")


def extract(archive: Path, dest_dir: Path) -> Path:
    """Extract the tarball; return the extracted boost_<ver> directory."""
    v_ = BOOST_VERSION.replace(".", "_")
    src = dest_dir / f"boost_{v_}"
    if (src / "bootstrap.sh").exists() or (src / "bootstrap.bat").exists():
        log(f"already extracted: {src}")
        return src
    log(f"extracting {archive}")
    with tarfile.open(archive, "r:gz") as tar:
        # filter='data' (py>=3.12) is a no-op on trusted content but silences the warning
        try:
            tar.extractall(dest_dir, filter="data")
        except TypeError:
            tar.extractall(dest_dir)
    if not src.exists():
        raise RuntimeError(f"expected {src} after extraction")
    return src


def toolchain() -> tuple[str, str, list[str]]:
    """Return (b2_toolset, user_config_jam_text, extra_b2_args) for this OS,
    using the compiler from the environment so Boost matches the project ABI."""
    system = platform.system()
    cxx = os.environ.get("CXX", "").strip().strip('"')
    ar = os.environ.get("AR", "").strip().strip('"')
    machine = platform.machine().lower()
    extra: list[str] = []

    if system == "Windows":
        # Match the project: clang-cl (MSVC-compatible) + the LLVM archiver.
        compiler = cxx or "clang-cl"
        opts = []
        archiver = ar or "llvm-lib"
        opts.append(f'<archiver>"{archiver}"')
        opts.append('<ranlib>"llvm-ranlib"')
        jam = f'using clang-win : : "{compiler}" : {" ".join(opts)} ;\n'
        return "clang-win", jam, extra

    if system == "Darwin":
        compiler = cxx or "clang++"
        cxxflags = ["-stdlib=libc++"]
        dep = os.environ.get("MACOSX_DEPLOYMENT_TARGET")
        if dep:
            cxxflags.append(f"-mmacosx-version-min={dep}")
        opts = " ".join(f'<cxxflags>"{f}"' for f in cxxflags)
        opts += ' <linkflags>"-stdlib=libc++"'
        jam = f'using clang : : "{compiler}" : {opts} ;\n'
        if machine in ("arm64", "aarch64"):
            extra += ["architecture=arm", "address-model=64"]
        return "clang", jam, extra

    # Linux (and any other unix): gcc, matching the conda compiler + its libstdc++ ABI.
    compiler = cxx or "g++"
    jam = f'using gcc : : "{compiler}" ;\n'
    return "gcc", jam, extra


def already_built(prefix: Path) -> bool:
    """True if a previous run already installed the requested libraries."""
    inc = prefix / "include" / "boost" / "version.hpp"
    libdir = prefix / "lib"
    if not inc.exists() or not libdir.is_dir():
        return False
    for lib in BOOST_LIBRARIES:
        if not list(libdir.glob(f"*boost_{lib}*")):
            return False
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description="Build static Boost for themachinethatgoesping")
    ap.add_argument("--prefix", required=True, help="install prefix (headers -> include/, libs -> lib/)")
    ap.add_argument("--jobs", default=str(os.cpu_count() or 4), help="parallel build jobs")
    ap.add_argument("--build-dir", default=None, help="scratch dir for download/extract (default: <prefix>/../boost_build)")
    ap.add_argument("--force", action="store_true", help="rebuild even if already installed")
    args = ap.parse_args()

    prefix = Path(args.prefix).resolve()
    build_dir = Path(args.build_dir).resolve() if args.build_dir else prefix.parent / "boost_build"
    build_dir.mkdir(parents=True, exist_ok=True)

    log(f"Boost {BOOST_VERSION}; libraries={BOOST_LIBRARIES}; prefix={prefix}")

    if already_built(prefix) and not args.force:
        log("requested libraries already present -> skipping (use --force to rebuild)")
        return 0

    archive = download(BOOST_VERSION, build_dir)
    src = extract(archive, build_dir)

    toolset, jam_text, extra_args = toolchain()
    jam_path = build_dir / "user-config.jam"
    jam_path.write_text(jam_text)
    log(f"toolset={toolset}; user-config.jam:\n{jam_text.rstrip()}")

    is_windows = platform.system() == "Windows"

    # 1) bootstrap: build the b2 driver (its own compiler is irrelevant to Boost's ABI).
    if is_windows:
        run("bootstrap.bat", cwd=src)
        b2 = str(src / "b2.exe")
    else:
        run(["./bootstrap.sh", f"--with-libraries={','.join(BOOST_LIBRARIES)}"], cwd=src)
        b2 = "./b2"

    # 2) build + install only the requested libraries, static, release.
    b2_cmd = [
        b2,
        f"--user-config={jam_path}",
        f"--prefix={prefix}",
        f"--build-dir={build_dir / 'b2'}",
        f"-j{args.jobs}",
        f"toolset={toolset}",
        "link=static",
        "runtime-link=shared",
        "variant=release",
        "threading=multi",
        # iostreams: no external compression backends are used by the project
        "-sNO_ZLIB=1",
        "-sNO_BZIP2=1",
        "-sNO_LZMA=1",
        "-sNO_ZSTD=1",
    ]
    b2_cmd += extra_args
    b2_cmd += [f"--with-{lib}" for lib in BOOST_LIBRARIES]
    b2_cmd += ["install"]
    run(b2_cmd, cwd=src)

    if not already_built(prefix):
        log("ERROR: build finished but expected libraries are missing under the prefix")
        return 1
    log(f"done. Set BOOST_ROOT={prefix} and build meson with -Ddynamic_boost=disabled")
    return 0


if __name__ == "__main__":
    sys.exit(main())
