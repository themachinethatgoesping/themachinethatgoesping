#!/usr/bin/env python3
"""Run GCC compilation commands with ``-H`` and capture include trees in log files.

This script replays the Meson/Ninja compilation database (``compile_commands.json``)
by forcing the compiler to run the preprocessor stage only while emitting header
include diagnostics (``-H``).  STDERR from the compiler is written to a per-object
log file so that the terminal output stays clean.

Typical usage::

    python capture_gcc_headers.py --builddir builddir

The script will create ``header-logs`` inside the build directory.  Each object
file listed in the compilation database produces one ``.headers.log`` file with
GCC's include depth output.  Only compilation entries that use GCC are executed;
commands for other compilers (Clang, MSVC, etc.) are ignored.
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Sequence


def _debug(msg: str, *, enabled: bool) -> None:
    if enabled:
        print(msg, file=sys.stderr)


def _load_compile_commands(path: Path) -> List[Dict[str, object]]:
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:  # pragma: no cover - user feedback
        raise SystemExit(f"compile_commands.json not found: {path}") from exc
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:  # pragma: no cover - user feedback
        raise SystemExit(f"Failed to parse {path}: {exc}") from exc


_COMPILER_HINTS = ("gcc", "g++", "c++", "cc")
_WRAPPER_HINTS = {"ccache", "sccache", "distcc", "icecc"}


def _looks_like_compiler(token: str) -> bool:
    base = os.path.basename(token)
    return any(hint in base for hint in _COMPILER_HINTS)


def _expand_response_files(args: Sequence[str], *, cwd: Path, debug: bool) -> List[str]:
    expanded: List[str] = []
    for arg in args:
        if arg.startswith("@"):
            rsp_path = (cwd / arg[1:]).resolve()
            try:
                rsp_content = rsp_path.read_text(encoding="utf-8")
            except FileNotFoundError as exc:  # pragma: no cover - user feedback
                raise SystemExit(f"Response file not found: {rsp_path}") from exc
            _debug(f"Expanding response file {rsp_path}", enabled=debug)
            expanded.extend(shlex.split(rsp_content))
        else:
            expanded.append(arg)
    return expanded


_SKIP_NEXT_FOR = {"-o", "-MF", "-MT", "-MQ"}
_SKIP_FLAGS = {
    "-c",
    "-S",
    "-MD",
    "-MMD",
    "-MG",
    "-MM",
    "-MP",
    "-M",
}


def _filter_preprocessor_args(args: Sequence[str]) -> List[str]:
    filtered: List[str] = []
    skip_next = 0
    for arg in args:
        if skip_next:
            skip_next -= 1
            continue
        if arg in _SKIP_FLAGS:
            continue
        if arg in _SKIP_NEXT_FOR:
            skip_next = 1
            continue
        if any(arg.startswith(prefix) for prefix in ("-o", "-MF", "-MT", "-MQ")):
            continue
        if arg.startswith("-Wp,") and "MD" in arg:
            # dependency generation pragmas – avoid touching .d files
            continue
        if arg == "-fdiagnostics-color=always":
            filtered.append("-fdiagnostics-color=never")
            continue
        filtered.append(arg)
    return filtered


def _extract_compiler_and_args(entry: Dict[str, object], *, debug: bool) -> tuple[str, List[str]] | None:
    raw_args: Sequence[str]
    if "arguments" in entry:
        raw_args = entry["arguments"]  # type: ignore[assignment]
    else:
        command: str = entry["command"]  # type: ignore[assignment]
        raw_args = shlex.split(command)

    if not raw_args:
        return None

    compiler_index = None
    for idx, token in enumerate(raw_args):
        base = os.path.basename(token)
        if base in _WRAPPER_HINTS:
            continue
        if _looks_like_compiler(token):
            compiler_index = idx
            break
    if compiler_index is None:
        return None

    compiler = raw_args[compiler_index]
    trailing_args = list(raw_args[compiler_index + 1:])
    if not trailing_args:
        return compiler, []
    return compiler, trailing_args


class CompilerInspector:
    def __init__(self) -> None:
        self._cache: Dict[str, bool] = {}

    def is_gcc(self, compiler: str) -> bool:
        if compiler not in self._cache:
            try:
                proc = subprocess.run(
                    [compiler, "--version"],
                    check=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
            except FileNotFoundError:
                self._cache[compiler] = False
            else:
                output = (proc.stdout + proc.stderr).lower()
                self._cache[compiler] = "gcc" in output and "clang" not in output
        return self._cache[compiler]


def _derive_log_path(output_rel: str | None, source: str, *, root: Path) -> Path:
    if output_rel:
        output_path = Path(output_rel)
        log_path = output_path.with_suffix(output_path.suffix + ".headers.log")
    else:
        source_name = Path(source).name
        log_path = Path(source_name + ".headers.log")
    return (root / log_path).resolve()


def _format_summary(index: int, total: int, rel_log: Path, *, skip: bool) -> str:
    status = "skip" if skip else f"{index + 1}/{total}"
    return f"[{status}] {rel_log}"


def capture_headers(
    builddir: Path,
    log_root: Path,
    *,
    force: bool,
    limit: int | None,
    debug: bool,
    dry_run: bool,
) -> None:
    compile_commands = _load_compile_commands(builddir / "compile_commands.json")
    inspector = CompilerInspector()

    log_root.mkdir(parents=True, exist_ok=True)

    total_entries = len(compile_commands)
    captured = 0

    for index, entry in enumerate(compile_commands):
        compiler_args = _extract_compiler_and_args(entry, debug=debug)
        if compiler_args is None:
            continue
        compiler, trailing_args = compiler_args
        if not inspector.is_gcc(compiler):
            continue

        directory = Path(entry["directory"])  # type: ignore[arg-type]
        trailing_args = _expand_response_files(trailing_args, cwd=directory, debug=debug)
        filtered_args = _filter_preprocessor_args(trailing_args)

        if "-E" not in filtered_args:
            filtered_args.insert(0, "-E")
        if "-H" not in filtered_args:
            filtered_args.insert(1, "-H")
        if "-fdiagnostics-color=never" not in filtered_args and not any(
            arg.startswith("-fdiagnostics-color=") for arg in filtered_args
        ):
            filtered_args.append("-fdiagnostics-color=never")

        source_file: str = entry.get("file", filtered_args[-1])  # type: ignore[assignment]
        output_rel: str | None = entry.get("output")  # type: ignore[assignment]
        logfile = _derive_log_path(output_rel, source_file, root=log_root)
        logfile.parent.mkdir(parents=True, exist_ok=True)

        if logfile.exists() and not force:
            _debug(_format_summary(index, total_entries, logfile.relative_to(log_root), skip=True), enabled=debug)
            continue

        command = [compiler] + filtered_args + ["-o", os.devnull]

        _debug(
            _format_summary(index, total_entries, logfile.relative_to(log_root), skip=False)
            + f" :: {' '.join(shlex.quote(arg) for arg in command)}",
            enabled=debug,
        )

        if dry_run:
            continue

        with logfile.open("w", encoding="utf-8") as log_stream:
            proc = subprocess.run(
                command,
                cwd=directory,
                stdout=subprocess.DEVNULL,
                stderr=log_stream,
            )
        if proc.returncode != 0:
            raise SystemExit(
                f"Command failed for {source_file} (compiler: {compiler}). "
                f"Exit code: {proc.returncode}. See {logfile} for details."
            )

        captured += 1
        if limit is not None and captured >= limit:
            break

    if captured == 0:
        print("No GCC compilation entries were processed.")
    else:
        rel_root = log_root.relative_to(builddir) if log_root.is_relative_to(builddir) else log_root
        print(f"Captured header logs for {captured} command(s). Logs stored in {rel_root}.")


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Capture GCC include trees into log files.")
    parser.add_argument(
        "--builddir",
        type=Path,
        default=Path("builddir"),
        help="Meson build directory containing compile_commands.json (default: builddir)",
    )
    parser.add_argument(
        "--log-dir",
        type=Path,
        default=None,
        help="Directory to store header logs (default: <builddir>/header-logs)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-run even if a log file already exists",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Process only the first N compile commands (useful for quick experiments)",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Print expanded commands while processing",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be executed without invoking the compiler",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    ns = parse_args(sys.argv[1:] if argv is None else argv)
    builddir = ns.builddir.resolve()
    log_dir = ns.log_dir.resolve() if ns.log_dir else (builddir / "header-logs").resolve()

    capture_headers(
        builddir,
        log_dir,
        force=ns.force,
        limit=ns.limit,
        debug=ns.debug,
        dry_run=ns.dry_run,
    )
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
