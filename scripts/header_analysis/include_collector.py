#!/usr/bin/env python3
"""Collect include directives for Meson build targets.

This helper reuses ``meson_target_parser`` to enumerate build targets and their
associated source files, then scans every source for ``#include`` directives.

For each analysed source file the includes are grouped into *internal* and
*external* lists:

* Internal: ``"quoted"`` includes, plus any ``<angled>`` includes whose header
  begins with a user-provided ``--internal-prefix`` value.
* External: all remaining ``<angled>`` includes.

Results are printed grouped by target label/name for easy inspection.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parent))
    from meson_target_parser import MesonTargetCollector, SOURCE_SUFFIXES  # type: ignore
else:
    from .meson_target_parser import MesonTargetCollector, SOURCE_SUFFIXES

INCLUDE_PATTERN = re.compile(r"^\s*#\s*include\s*(<[^>]+>|\"[^\"]+\")", re.MULTILINE)
HEADER_SUFFIXES: Set[str] = {".h", ".hpp", ".hh", ".hxx", ".inl", ".ipp"}
OPTIONAL_HAS_INCLUDE_HEADERS: Set[str] = {
    "arm_neon.h",
    "intrin.h",
    "machine/endian.h",
    "sys/byteorder.h",
    "sys/endian.h",
}


@dataclass
class IncludeReport:
    """Holds include categorisation for a single source file."""

    source: Path
    internal: List[str]
    external: List[str]
    missing: bool = False


@dataclass
class TargetSummary:
    """Aggregated include statistics for a target."""

    label: str
    name: str
    internal_counts: Dict[str, int]
    external_counts: Dict[str, int]
    source_count: int


class IncludeCollector:
    """Collects include information for Meson targets."""

    def __init__(self, project_root: Path, subprojects: Sequence[str], internal_prefixes: Sequence[str]) -> None:
        self.project_root = project_root.resolve()
        self.subprojects = subprojects
        self.internal_prefixes = tuple(prefix for prefix in internal_prefixes if prefix)
        self.collector = MesonTargetCollector(self.project_root, self.subprojects)
        self._cache: Dict[Path, IncludeReport] = {}
        self._scan_cache: Dict[Path, Tuple[IncludeReport, List[Path]]] = {}
    self._header_index: Dict[str, Path] = {}
    self._header_suffix_index: Dict[str, List[Path]] = {}
        self._header_basename_index: Dict[str, List[Path]] = {}
        self._header_index_ready = False
        self._resolve_cache: Dict[Tuple[Path, str], Optional[Path]] = {}
        self._ignore_dirs = {
            "build",
            "builddir",
            "builddir-clang",
            "dist",
            "node_modules",
            "__pycache__",
            ".git",
            ".mypy_cache",
            ".pytest_cache",
            ".venv",
        }
        self.target_summaries: Dict[str, TargetSummary] = {}

    def run(self) -> Dict[str, List[IncludeReport]]:
        self.collector.run()

        all_sources: List[Path] = []
        target_sources: Dict[str, List[Path]] = {}

        for key in sorted(self.collector.targets):
            record = self.collector.targets[key]
            relevant_sources = [src for src in sorted(record.source_paths) if self._is_relevant_source(src)]
            target_sources[key] = relevant_sources
            all_sources.extend(relevant_sources)

        unique_sources = sorted({path for path in all_sources})

        iterator: Iterable[Path]
        try:
            from tqdm import tqdm

            iterator = tqdm(unique_sources, desc="Collecting includes", unit="file")
        except ImportError:  # pragma: no cover - tqdm optional
            iterator = unique_sources

        for path in iterator:
            self._get_or_collect(path)

        results: Dict[str, List[IncludeReport]] = {}
        for key, paths in target_sources.items():
            reports: List[IncludeReport] = []
            for path in paths:
                report = self._cache.get(path)
                if report is not None:
                    reports.append(report)
            results[key] = reports
        self.target_summaries = self._summarise_target_reports(results)
        return results

    def _get_or_collect(self, source_path: Path, visited: Optional[Set[Path]] = None) -> Optional[IncludeReport]:
        if not self._is_relevant_source(source_path):
            return None

        if visited is None:
            visited = set()

        cached = self._cache.get(source_path)
        if cached is not None:
            return cached

        if source_path in visited:
            return cached

        visited.add(source_path)

        direct_report, resolved_internal = self._scan_source(source_path)
        if direct_report.missing:
            self._cache[source_path] = direct_report
            return direct_report

        aggregate_internal: Set[str] = set(direct_report.internal)
        aggregate_external: Set[str] = set(direct_report.external)

        for internal_path in resolved_internal:
            nested_report = self._get_or_collect(internal_path, visited)
            if nested_report is None or nested_report.missing:
                continue
            aggregate_internal.update(nested_report.internal)
            aggregate_external.update(nested_report.external)

        final_report = IncludeReport(
            source=source_path,
            internal=sorted(aggregate_internal),
            external=sorted(aggregate_external),
            missing=False,
        )
        self._cache[source_path] = final_report
        return final_report

    def _scan_source(self, source_path: Path) -> Tuple[IncludeReport, List[Path]]:
        cached = self._scan_cache.get(source_path)
        if cached is not None:
            return cached

        report = IncludeReport(source=source_path, internal=[], external=[], missing=False)

        if not source_path.is_file():
            report.missing = True
            self._scan_cache[source_path] = (report, [])
            return report, []

        try:
            content = source_path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            print(f"[warning] Failed to read {source_path}: {exc}", file=sys.stderr)
            report.missing = True
            self._scan_cache[source_path] = (report, [])
            return report, []

        internal: set[str] = set()
        external: set[str] = set()
        resolved_internal: Set[Path] = set()

        for match in INCLUDE_PATTERN.finditer(content):
            token = match.group(1)
            header = token[1:-1]
            is_quoted = token.startswith('"')
            if is_quoted or any(header.startswith(prefix) for prefix in self.internal_prefixes):
                internal.add(header)
                resolved = self._resolve_internal_header(source_path, header, is_quoted)
                if resolved is not None:
                    resolved_internal.add(resolved)
            else:
                external.add(header)

        report.internal = sorted(internal)
        report.external = sorted(external)
        resolved_list = sorted(resolved_internal)
        self._scan_cache[source_path] = (report, resolved_list)
        return report, resolved_list

    def _summarise_target_reports(self, results: Dict[str, List[IncludeReport]]) -> Dict[str, TargetSummary]:
        summaries: Dict[str, TargetSummary] = {}
        for key, reports in results.items():
            internal_counter: Counter[str] = Counter()
            external_counter: Counter[str] = Counter()
            label, name = key.split(":", 1)
            valid_reports = 0
            for report in reports:
                if report.missing:
                    continue
                valid_reports += 1
                for header in report.internal:
                    internal_counter[header] += 1
                for header in report.external:
                    external_counter[header] += 1
            summaries[key] = TargetSummary(
                label=label,
                name=name,
                internal_counts=dict(sorted(internal_counter.items())),
                external_counts=dict(sorted(external_counter.items())),
                source_count=valid_reports,
            )
        return summaries

    def _prepare_header_index(self) -> None:
        if self._header_index_ready:
            return

        for root, dirs, files in os.walk(self.project_root):
            root_path = Path(root)
            dirs[:] = [d for d in dirs if d not in self._ignore_dirs]
            for filename in files:
                lower_name = filename.lower()
                if not any(lower_name.endswith(suffix) for suffix in HEADER_SUFFIXES):
                    continue
                full_path = (root_path / filename).resolve()
                rel_path = full_path.relative_to(self.project_root).as_posix()
                self._register_header_key(rel_path, full_path)
                parts = rel_path.split("/")
                for i in range(1, len(parts)):
                    trimmed = "/".join(parts[i:])
                    if trimmed:
                        self._register_header_key(trimmed, full_path)
                self._header_basename_index.setdefault(full_path.name, []).append(full_path)

        self._header_index_ready = True

    def _register_header_key(self, key: str, path: Path) -> None:
        normalized = key.lstrip("./")
        existing = self._header_index.get(normalized)
        if existing is None:
            self._header_index[normalized] = path
        self._header_suffix_index.setdefault(normalized, []).append(path)

    def _resolve_internal_header(self, origin: Path, header: str, is_quoted: bool) -> Optional[Path]:
        cache_key = (origin, header)
        if cache_key in self._resolve_cache:
            return self._resolve_cache[cache_key]

        header_norm = header.lstrip("./")
        candidates: List[Path] = []
        header_path = Path(header_norm)

        if is_quoted:
            quoted_candidate = (origin.parent / header_path).resolve()
            candidates.append(quoted_candidate)
            if quoted_candidate.is_file():
                self._resolve_cache[cache_key] = quoted_candidate
                return quoted_candidate

        if header_path.is_absolute():
            if header_path.is_file():
                self._resolve_cache[cache_key] = header_path
                return header_path
            candidates.append(header_path)
        else:
            project_candidate = (self.project_root / header_path).resolve()
            candidates.append(project_candidate)
            if project_candidate.is_file():
                self._resolve_cache[cache_key] = project_candidate
                return project_candidate

        # Fall back to indexed lookup only when direct resolution failed.
        self._prepare_header_index()

        if header_norm in self._header_index:
            candidates.append(self._header_index[header_norm])

        header_posix = header_norm.replace("\\", "/")
        if header_posix in self._header_index and self._header_index[header_posix] not in candidates:
            candidates.append(self._header_index[header_posix])

        suffix_matches = self._find_suffix_matches(header_posix)
        for candidate in suffix_matches:
            if candidate not in candidates:
                candidates.append(candidate)

        resolved: Optional[Path] = None
        for candidate in candidates:
            if candidate.is_file():
                resolved = candidate
                break

        self._resolve_cache[cache_key] = resolved
        return resolved

    def _find_suffix_matches(self, header: str) -> List[Path]:
        if not header:
            return []
        header = header.replace("\\", "/")
        matches = list(self._header_suffix_index.get(header, []))
        if matches:
            return matches
        base = header.split("/")[-1]
        return list(self._header_basename_index.get(base, []))

    @staticmethod
    def _sanitize_for_filename(value: str) -> str:
        safe = re.sub(r"[^A-Za-z0-9_.-]", "_", value)
        return safe or "unnamed"

    def write_pch_files(self, output_dir: Path) -> None:
        if not self.target_summaries:
            raise RuntimeError("Target summaries are not available. Run collector.run() first.")

        output_dir = output_dir.resolve()
        output_dir.mkdir(parents=True, exist_ok=True)

        for old_file in output_dir.glob("*.pch"):
            try:
                old_file.unlink()
            except OSError:
                pass

        for key, summary in self.target_summaries.items():
            if not summary.external_counts:
                continue
            label_safe = self._sanitize_for_filename(summary.label)
            name_safe = self._sanitize_for_filename(summary.name)
            filename = output_dir / f"{label_safe}_{name_safe}.hpp"
            lines = [
                "// Auto-generated precompiled header",
                "#pragma once",
                "",
            ]
            for header in sorted(summary.external_counts):
                lines.extend(self._format_include_block(header))
            filename.write_text("\n".join(lines) + "\n", encoding="utf-8")

    @staticmethod
    def _is_relevant_source(path: Path) -> bool:
        suffix = path.suffix.lower()
        if suffix in HEADER_SUFFIXES:
            return True
        return path.name.lower().endswith(SOURCE_SUFFIXES)

    @staticmethod
    def _format_include_block(header: str) -> List[str]:
        header = header.strip()
        if not header:
            return []
        if header in OPTIONAL_HAS_INCLUDE_HEADERS:
            return [
                "#if defined(__has_include)",
                f"#  if __has_include(<{header}>)",
                f"#    include <{header}>",
                "#  endif",
                "#endif",
            ]
        return [f"#include <{header}>"]


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect include directives for Meson targets.")
    parser.add_argument(
        "project_root",
        type=Path,
        nargs="?",
        default=Path.cwd(),
        help="Path to the Meson project root (defaults to current directory).",
    )
    parser.add_argument(
        "--subprojects",
        type=str,
        default="",
        help="Comma-separated list of subprojects to parse in addition to the root meson file",
    )
    parser.add_argument(
        "--internal-prefix",
        dest="internal_prefixes",
        action="append",
        default=[],
        help="Treat angled includes starting with this prefix as internal (can be repeated).",
    )
    parser.add_argument(
        "--pch-output",
        type=Path,
        default=None,
        help="Directory to write generated precompiled headers (one per target).",
    )
    return parser.parse_args(argv)


def display(results: Dict[str, List[IncludeReport]]) -> None:
    if not results:
        print("[info] No targets detected.")
        return

    for key in sorted(results):
        label, target = key.split(":", 1)
        print(f"[{label}] {target}")
        reports = results[key]
        if not reports:
            print("  (no relevant source files)")
            continue
        for report in reports:
            status = " (missing)" if report.missing else ""
            print(f"  {report.source}{status}")
            if report.missing:
                continue
            if report.internal:
                print("    internal:")
                for header in report.internal:
                    print(f"      {header}")
            if report.external:
                print("    external:")
                for header in report.external:
                    print(f"      {header}")


def display_target_summaries(summaries: Dict[str, TargetSummary]) -> None:
    if not summaries:
        return

    print("\n[summary] Aggregate includes per target")
    for key in sorted(summaries):
        summary = summaries[key]
        print(f"[{summary.label}] {summary.name}")
        if summary.internal_counts:
            print("  internal includes (source count):")
            for header, count in sorted(summary.internal_counts.items(), key=lambda item: (-item[1], item[0])):
                print(f"    {header}: {count}")
        if summary.external_counts:
            print("  external includes (source count):")
            for header, count in sorted(summary.external_counts.items(), key=lambda item: (-item[1], item[0])):
                print(f"    {header}: {count}")
        print(f"  analysed sources: {summary.source_count}")


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    subprojects = [name.strip() for name in args.subprojects.split(",") if name.strip()]

    collector = IncludeCollector(args.project_root, subprojects, args.internal_prefixes)
    results = collector.run()
    display(results)
    display_target_summaries(collector.target_summaries)
    if args.pch_output is not None:
        collector.write_pch_files(args.pch_output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
