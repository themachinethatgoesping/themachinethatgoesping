#!/usr/bin/env python3
"""Meson target include analysis helper.

The script inspects Meson introspection data (``intro-targets.json``) and, for
each C/C++ target, walks the include graph of all translation units to quantify
the impact of every *external* header. Internal headers (e.g. project sources)
are still traversed to discover the external dependencies they pull in, but the
report excludes them so that the resulting CSVs highlight candidates for
pre-compiled headers.

It produces two CSV reports (both external-only):

1. ``include_analysis_external.csv`` – per-target include cost summary for all
    external headers encountered during the traversal.
2. ``include_analysis_external_from_internal.csv`` – subset of the above where
    at least one including translation unit is classified as internal. This
    helps identify external headers that are *dragged in* by project headers.

For each (target, header) pair the reports contain:

* number of direct include statements encountered
* number of unique files containing those direct includes
* number of recursively included headers triggered by that header
* transitive line-of-code (LOC) sum (header + everything it includes)
* total inclusion cost (transitive LOC * direct include count)

Usage::

     python meson_include_analyzer.py \
          --project-root /path/to/themachinethatgoesping \
          --builddir /path/to/builddir \
          --output-dir /path/to/output \
          --internal-subproject tools --internal-subproject navigation

The script relies solely on the JSON files emitted by Meson's introspection API
(``<builddir>/meson-info/intro-targets.json``). No Meson command execution is
required at runtime.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

# ---------------------------------------------------------------------------
# Configuration constants
# ---------------------------------------------------------------------------
SOURCE_SUFFIXES: Tuple[str, ...] = (".c", ".cc", ".cpp", ".cxx", ".c++", ".mm")
HEADER_SUFFIXES: Tuple[str, ...] = (
    ".h",
    ".hh",
    ".hpp",
    ".hxx",
    ".h++",
    ".inl",
    ".ipp",
)
INCLUDE_PATTERN = re.compile(
    r"^#\s*include\s*(?:\"(?P<quoted>[^\"]+)\"|<(?P<angled>[^>]+)>)"
)

DEFAULT_INTERNAL_PREFIXES: Tuple[str, ...] = ("themachinethatgoesping/",)
DEFAULT_INTERNAL_SUBPROJECTS: Tuple[str, ...] = (
    "meta",
    "tools",
    "algorithms",
    "navigation",
    "echosounders",
    "pingprocessing",
    "gridding",
)

# ---------------------------------------------------------------------------
# Helper dataclasses
# ---------------------------------------------------------------------------


def _normalize_posix(path: Path, root: Path) -> str:
    """Return a POSIX style path relative to *root*, preserving '..' if needed."""
    try:
        rel = path.relative_to(root)
    except ValueError:
        return path.resolve().as_posix()
    return rel.as_posix()


@dataclass
class TargetDescription:
    name: str
    defined_in: Path
    sources: Set[Path] = field(default_factory=set)
    include_dirs: List[Path] = field(default_factory=list)


@dataclass
class IncludeRecord:
    include_key: str
    include_display: str
    resolved_path: Optional[Path]
    occurrences: int
    including_files: Set[Path]
    recursive_count: Optional[int]
    transitive_loc: Optional[int]
    total_cost: Optional[int]
    internal_includer_count: int
    is_internal_header: bool

    def to_row(self, target_name: str, root: Path) -> Dict[str, object]:
        rel_path = (
            _normalize_posix(self.resolved_path, root)
            if self.resolved_path is not None
            else ""
        )
        including_files_rel = sorted(_normalize_posix(p, root) for p in self.including_files)

        return {
            "target": target_name,
            "include": rel_path or self.include_display,
            "include_display": self.include_display,
            "resolved": bool(self.resolved_path),
            "occurrences": self.occurrences,
            "including_files": "|".join(including_files_rel),
            "including_file_count": len(self.including_files),
            "recursive_include_count": self.recursive_count,
            "transitive_loc": self.transitive_loc,
            "total_cost": self.total_cost,
            "internal_includer_count": self.internal_includer_count,
        }


# ---------------------------------------------------------------------------
# Builders and parsers
# ---------------------------------------------------------------------------


class IncludeParser:
    """Parses include directives and counts lines of code for files."""

    def __init__(self) -> None:
        self._include_cache: Dict[Path, List[str]] = {}
        self._loc_cache: Dict[Path, int] = {}

    def get_includes(self, path: Path) -> List[str]:
        if path in self._include_cache:
            return self._include_cache[path]

        includes: List[str] = []
        try:
            with path.open("r", encoding="utf-8", errors="ignore") as handle:
                for line in handle:
                    match = INCLUDE_PATTERN.match(line.strip())
                    if match:
                        path = match.group("quoted") or match.group("angled")
                        includes.append(path.strip())
        except (OSError, UnicodeDecodeError):
            includes = []

        self._include_cache[path] = includes
        return includes

    def get_loc(self, path: Path) -> int:
        if path in self._loc_cache:
            return self._loc_cache[path]

        loc = 0
        try:
            with path.open("r", encoding="utf-8", errors="ignore") as handle:
                for _ in handle:
                    loc += 1
        except (OSError, UnicodeDecodeError):
            loc = 0

        self._loc_cache[path] = loc
        return loc


class IncludeResolver:
    """Resolves include strings to file paths using search directories."""

    def __init__(self, root: Path, header_index: Dict[str, List[Path]]) -> None:
        self.root = root
        self.header_index = header_index

    def resolve(
        self, include: str, current_file: Path, search_paths: Sequence[Path]
    ) -> Optional[Path]:
        candidate = self._candidate_from_local(include, current_file)
        if candidate is not None:
            return candidate

        for base in search_paths:
            candidate = self._candidate_from_dir(include, base)
            if candidate is not None:
                return candidate

        rel_entry = self.header_index.get(include)
        if rel_entry:
            return rel_entry[0]

        # Fallback: attempt with stripped leading project namespace
        if include.startswith("themachinethatgoesping/"):
            rel_include = include[len("themachinethatgoesping/") :]
            rel_entry = self.header_index.get(rel_include)
            if rel_entry:
                return rel_entry[0]

        return None

    def _candidate_from_local(self, include: str, current_file: Path) -> Optional[Path]:
        inclusive_path = (current_file.parent / include).resolve()
        if inclusive_path.is_file():
            return inclusive_path
        return None

    def _candidate_from_dir(self, include: str, base: Path) -> Optional[Path]:
        base = base.resolve()
        inclusive_path = (base / include).resolve()
        if inclusive_path.is_file():
            return inclusive_path
        return None


# ---------------------------------------------------------------------------
# Core analyzer
# ---------------------------------------------------------------------------


class InternalClassifier:
    """Classifies paths and include strings as internal/external."""

    def __init__(
        self,
        project_root: Path,
        prefixes: Sequence[str],
        subprojects: Sequence[str],
    ) -> None:
        self.project_root = project_root.resolve()
        self.prefixes = [p.strip().lower().rstrip("/") + "/" for p in prefixes]
        self.subproject_roots: List[Path] = []
        for name in subprojects:
            candidate = (self.project_root / "subprojects" / name).resolve()
            if candidate.exists():
                self.subproject_roots.append(candidate)

    def is_internal_path(self, path: Path) -> bool:
        path = path.resolve()
        try:
            rel = path.relative_to(self.project_root)
            rel_posix = rel.as_posix().lower()
            if any(rel_posix.startswith(prefix) for prefix in self.prefixes):
                return True
        except ValueError:
            pass

        for root in self.subproject_roots:
            try:
                path.relative_to(root)
                return True
            except ValueError:
                continue
        return False

    def is_internal_display(self, include_display: str) -> bool:
        disp = include_display.replace("\\", "/").lower()
        return any(disp.startswith(prefix) for prefix in self.prefixes)

    def count_internal_includers(self, includers: Iterable[Path]) -> int:
        return sum(1 for inc in includers if self.is_internal_path(inc))


class MesonIncludeAnalyzer:
    def __init__(
        self,
        project_root: Path,
        builddir: Path,
        classifier: InternalClassifier,
    ) -> None:
        self.project_root = project_root.resolve()
        self.builddir = builddir.resolve()
        self.parser = IncludeParser()
        self.header_index = self._build_header_index()
        self.resolver = IncludeResolver(self.project_root, self.header_index)
        self.classifier = classifier

    # -------------------------- public entry points ---------------------
    def analyze(
        self, targets: Sequence[TargetDescription]
    ) -> List[Tuple[TargetDescription, List[IncludeRecord]]]:
        results: List[Tuple[TargetDescription, List[IncludeRecord]]] = []
        for target in targets:
            include_records = self._analyze_single_target(target)
            results.append((target, include_records))
        return results

    # -------------------------- include graph logic ---------------------
    def _analyze_single_target(self, target: TargetDescription) -> List[IncludeRecord]:
        occurrences: Counter = Counter()
        include_display: Dict[object, str] = {}
        including_files: Dict[object, Set[Path]] = defaultdict(set)
        resolved_map: Dict[object, Optional[Path]] = {}
        graph: Dict[Path, Set[Path]] = defaultdict(set)
        visited: Set[Path] = set()

        search_paths = self._build_search_paths(target)

        def visit(file_path: Path) -> None:
            file_path = file_path.resolve()
            if not file_path.is_file():
                return
            if file_path in visited:
                return
            visited.add(file_path)

            includes = self.parser.get_includes(file_path)
            for raw_include in includes:
                resolved = self.resolver.resolve(raw_include, file_path, search_paths)
                if resolved is not None:
                    key: object = resolved
                else:
                    key = ("unresolved", raw_include)

                occurrences[key] += 1
                include_display.setdefault(key, raw_include)
                resolved_map.setdefault(key, resolved)
                including_files[key].add(file_path)

                if resolved is not None:
                    graph[file_path].add(resolved)
                    visit(resolved)

        for source in sorted(target.sources):
            visit(source)

        transitive_cache: Dict[Path, Tuple[int, int]] = {}

        def transitive_stats(start: Path) -> Tuple[int, int]:
            if start in transitive_cache:
                return transitive_cache[start]

            seen: Set[Path] = set()

            def dfs(node: Path) -> int:
                if node in seen:
                    return 0
                seen.add(node)
                total_loc = self.parser.get_loc(node)
                for child in graph.get(node, set()):
                    total_loc += dfs(child)
                return total_loc

            total_loc = dfs(start)
            count = max(0, len(seen) - 1)
            transitive_cache[start] = (count, total_loc)
            return transitive_cache[start]

        records: List[IncludeRecord] = []
        for key, count in occurrences.items():
            resolved = resolved_map.get(key)
            display = include_display.get(key, "")
            rec_count: Optional[int] = None
            transitive_loc: Optional[int] = None
            total_cost: Optional[int] = None

            if isinstance(key, Path):
                rec_count, transitive_loc = transitive_stats(key)
                total_cost = transitive_loc * count

            internal_includer_count = self.classifier.count_internal_includers(
                including_files[key]
            )
            is_internal_header = False
            if resolved is not None:
                is_internal_header = self.classifier.is_internal_path(resolved)
            else:
                is_internal_header = self.classifier.is_internal_display(display)

            record = IncludeRecord(
                include_key=_normalize_posix(resolved, self.project_root)
                if resolved is not None
                else str(key),
                include_display=display,
                resolved_path=resolved,
                occurrences=count,
                including_files=including_files[key],
                recursive_count=rec_count,
                transitive_loc=transitive_loc,
                total_cost=total_cost,
                internal_includer_count=internal_includer_count,
                is_internal_header=is_internal_header,
            )
            records.append(record)

        records.sort(key=lambda r: (r.resolved_path is None, -(r.total_cost or 0), r.include_display))
        return records

    # -------------------------- helpers ---------------------------------
    def _build_header_index(self) -> Dict[str, List[Path]]:
        index: Dict[str, List[Path]] = defaultdict(list)
        for path in self.project_root.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() in HEADER_SUFFIXES:
                rel = _normalize_posix(path, self.project_root)
                index[rel].append(path)
        return index

    def _build_search_paths(self, target: TargetDescription) -> List[Path]:
        search_paths: List[Path] = []
        seen: Set[Path] = set()

        def push(path: Path) -> None:
            path = path.resolve()
            if path in seen:
                return
            seen.add(path)
            search_paths.append(path)

        for source in target.sources:
            push(source.parent)
        for inc in target.include_dirs:
            push(inc)
        push(self.project_root)
        push(self.builddir)
        return search_paths


# ---------------------------------------------------------------------------
# Meson target loading & grouping
# ---------------------------------------------------------------------------


def load_targets(intro_targets_path: Path) -> List[TargetDescription]:
    with intro_targets_path.open("r", encoding="utf-8") as handle:
        raw_targets = json.load(handle)

    builddir = intro_targets_path.parent.parent
    targets: List[TargetDescription] = []

    for entry in raw_targets:
        target = _build_target_description(entry, builddir)
        if target.sources:
            targets.append(target)

    grouped = _group_test_targets(targets)
    return grouped


def _build_target_description(entry: dict, builddir: Path) -> TargetDescription:
    defined_in = Path(entry.get("defined_in", "")).resolve()
    include_dirs: List[Path] = []
    sources: Set[Path] = set()

    for source_block in entry.get("target_sources", []):
        language = source_block.get("language")
        if language and language.lower() not in {"c", "cpp", "c++", "objcxx"}:
            continue

        for token in source_block.get("sources", []):
            path = Path(token)
            if not path.is_absolute():
                path = (builddir / token).resolve()
            if path.suffix.lower() in SOURCE_SUFFIXES:
                sources.add(path)

        include_dirs.extend(_extract_include_dirs(source_block.get("parameters", []), builddir))

    for token in entry.get("sources", []):
        path = Path(token)
        if not path.is_absolute():
            path = (builddir / token).resolve()
        if path.suffix.lower() in SOURCE_SUFFIXES:
            sources.add(path)

    unique_dirs: List[Path] = []
    seen_dirs: Set[Path] = set()
    for inc in include_dirs:
        inc = inc.resolve()
        if inc not in seen_dirs:
            seen_dirs.add(inc)
            unique_dirs.append(inc)

    return TargetDescription(
        name=str(entry.get("name")),
        defined_in=defined_in,
        sources=sources,
        include_dirs=unique_dirs,
    )


def _extract_include_dirs(parameters: Sequence[str], builddir: Path) -> List[Path]:
    include_dirs: List[Path] = []

    def normalize(path_str: str) -> Path:
        raw = path_str.strip()
        if not raw:
            return builddir
        candidate = Path(raw)
        if not candidate.is_absolute():
            candidate = (builddir / raw).resolve()
        return candidate

    tokens = list(parameters or [])
    idx = 0
    while idx < len(tokens):
        token = tokens[idx]
        if token in {"-I", "-isystem"}:
            if idx + 1 < len(tokens):
                include_dirs.append(normalize(tokens[idx + 1]))
                idx += 2
                continue
        if token.startswith("-I") and len(token) > 2:
            include_dirs.append(normalize(token[2:]))
        elif token.startswith("-isystem") and len(token) > 8:
            include_dirs.append(normalize(token[8:]))
        idx += 1

    return include_dirs


def _group_test_targets(targets: List[TargetDescription]) -> List[TargetDescription]:
    grouped: List[TargetDescription] = []
    buckets: Dict[Tuple[Path, str], TargetDescription] = {}

    for target in targets:
        if not target.defined_in.as_posix().endswith("tests/meson.build"):
            grouped.append(target)
            continue

        # Heuristic: consolidate single-source executables generated inside
        # foreach loops (names usually contain many dots and end with '_.test').
        if len(target.sources) == 1 and target.name.endswith("_.test"):
            bucket_key = (target.defined_in, target.name.split("._")[0])
            bucket = buckets.get(bucket_key)
            if bucket is None:
                bucket = TargetDescription(
                    name=f"loop::{_normalize_posix(target.defined_in.parent, target.defined_in.parent.parent)}",
                    defined_in=target.defined_in,
                    sources=set(),
                    include_dirs=list(target.include_dirs),
                )
                buckets[bucket_key] = bucket
            bucket.sources.update(target.sources)
            for inc in target.include_dirs:
                if inc not in bucket.include_dirs:
                    bucket.include_dirs.append(inc)
        else:
            grouped.append(target)

    grouped.extend(buckets.values())
    return grouped


# ---------------------------------------------------------------------------
# CSV writers
# ---------------------------------------------------------------------------


def write_csv(rows: Iterable[Dict[str, object]], headers: Sequence[str], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
def filter_rows_with_internal_includers(
    rows: Iterable[Dict[str, object]]
) -> Iterable[Dict[str, object]]:
    for row in rows:
        if int(row.get("internal_includer_count", 0)) > 0:
            yield row


# ---------------------------------------------------------------------------
# Main CLI
# ---------------------------------------------------------------------------


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze include usage per Meson target.")
    parser.add_argument("--project-root", type=Path, default=Path.cwd(), help="Path to the project root")
    parser.add_argument("--builddir", type=Path, default=Path("builddir"), help="Path to the Meson build directory")
    parser.add_argument("--output-dir", type=Path, default=Path("include_analysis"), help="Directory for generated CSV files")
    parser.add_argument("--targets-json", type=Path, default=None, help="Optional explicit path to intro-targets.json")
    parser.add_argument(
        "--internal-prefix",
        action="append",
        default=list(DEFAULT_INTERNAL_PREFIXES),
        help="Relative include prefixes that should be considered internal (repeatable)",
    )
    parser.add_argument(
        "--internal-subproject",
        action="append",
        default=list(DEFAULT_INTERNAL_SUBPROJECTS),
        help="Subproject names to treat as internal (repeatable)",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    project_root = args.project_root.resolve()
    builddir = args.builddir.resolve()

    intro_targets_path = (
        args.targets_json.resolve()
        if args.targets_json is not None
        else builddir / "meson-info" / "intro-targets.json"
    )

    if not intro_targets_path.is_file():
        print(f"[error] Could not find Meson introspection file: {intro_targets_path}", file=sys.stderr)
        return 1

    targets = load_targets(intro_targets_path)
    if not targets:
        print("[warning] No C/C++ targets detected in introspection data.")
        return 0

    classifier = InternalClassifier(
        project_root,
        prefixes=args.internal_prefix,
        subprojects=args.internal_subproject,
    )

    analyzer = MesonIncludeAnalyzer(project_root, builddir, classifier)
    analysis_results = analyzer.analyze(targets)

    headers = [
        "target",
        "include",
        "include_display",
        "resolved",
        "occurrences",
        "including_files",
        "including_file_count",
        "recursive_include_count",
        "transitive_loc",
        "total_cost",
        "internal_includer_count",
    ]

    all_rows: List[Dict[str, object]] = []
    for target, records in analysis_results:
        for record in records:
            if record.is_internal_header:
                continue
            row = record.to_row(target.name, project_root)
            all_rows.append(row)

    output_dir: Path = args.output_dir.resolve()
    external_csv = output_dir / "include_analysis_external.csv"
    write_csv(all_rows, headers, external_csv)

    external_from_internal_csv = output_dir / "include_analysis_external_from_internal.csv"
    write_csv(list(filter_rows_with_internal_includers(all_rows)), headers, external_from_internal_csv)

    print(f"[info] Wrote external include analysis to {external_csv}")
    print(f"[info] Wrote external includes originating from internal sources to {external_from_internal_csv}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
