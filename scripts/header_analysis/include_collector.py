#!/usr/bin/env python3
"""Minimal include collection helper.

The module exposes :class:`IncludeCollector`, a tiny utility that scans source
files for ``#include`` directives and splits them into three categories:

* ``internal`` – headers included with double quotes (``"header.h"``)
* ``ext_internal`` – angled headers (``<header>``) that start with one of the
    user-supplied ``--include-prefix`` values
* ``external`` – all other angled headers

The collector caches results per source file so repeated queries are
essentially free. A lightweight CLI is provided to exercise the functionality
with the output of :mod:`meson_target_parser`.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
from collections import defaultdict
from tqdm.auto import tqdm

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parent))
    from meson_target_parser import MesonTargetCollector, SOURCE_SUFFIXES  # type: ignore
else:
    from .meson_target_parser import MesonTargetCollector, SOURCE_SUFFIXES

INCLUDE_PATTERN = re.compile(r"^\s*#\s*include\s*(<[^>]+>|\"[^\"]+\")", re.MULTILINE)


class IncludeSets:
    """Categorised include lists for a single source file."""

    def __init__(self, internal: List[str], ext_internal: List[str], external: List[str]) -> None:
        self.internal = set(internal)
        self.ext_internal = set(ext_internal)
        self.external = set(external)
        self.resolved = {}
        
        self.include_count = defaultdict(int)
        for header in list(self.internal) + list(self.ext_internal) + list(self.external):
            self.include_count[header] = 1
        
    def add(self, other: IncludeSets) -> None:
        self.internal.update(other.internal)
        self.ext_internal.update(other.ext_internal)
        self.external.update(other.external)
        self.resolved.update(other.resolved)
        for header in list(self.internal) + list(self.ext_internal) + list(self.external):
            self.include_count[header] = 1
        
    def sum(self, other: IncludeSets) -> None:
        self.internal.update(other.internal)
        self.ext_internal.update(other.ext_internal)
        self.external.update(other.external)
        self.resolved.update(other.resolved)
        
        for header in list(self.internal) + list(self.ext_internal) + list(self.external):
            self.include_count[header] += other.include_count[header] 
        
    def add_header_paths(self, internal, paths):
        for header, path in zip(internal, paths):
            self.resolved[header] = path
            
    def get_internal_headers(self, sorted_by_count=True):
        
        headers = list(self.internal) + list(self.ext_internal)
        if sorted_by_count:
            headers.sort(key=lambda h: self.include_count[h], reverse=True)
        
        return headers
    
    def get_external_headers(self, sorted_by_count=True):
        headers = list(self.external)
        if sorted_by_count:
            headers.sort(key=lambda h: self.include_count[h], reverse=True)
        return headers
    
    def get_header_count(self, header):
        return self.include_count.get(header, 0)
            
    def get_header_path(self, header, default='<unresolved>'):
        return self.resolved.get(header, default)
            
    def get_header_paths(self, headers):
        paths = []
        for header in headers:
            paths.append(self.get_header_path(header))
        return paths
        
    


class IncludeCollector:
    """Cache-backed include parser for individual source files."""

    def __init__(self, include_prefixes: Sequence[str], encoding: str = "utf-8") -> None:
        self.include_prefixes = tuple(prefix for prefix in include_prefixes if prefix)
        self.encoding = encoding
        self._cache: Dict[Path, IncludeSets] = {}

    def collect(self, source: Path) -> IncludeSets:
        """Return cached include sets for *source*, scanning the file if needed."""

        source = source.resolve()
        cached = self._cache.get(source)
        if cached is not None:
            return cached

        includes = self._scan_file(source)
        self._cache[source] = includes
        return includes

    def collect_many(self, sources: Iterable[Path]) -> Dict[Path, IncludeSets]:
        """Convenience wrapper returning include sets for ``sources`` as a dict."""

        results: Dict[Path, IncludeSets] = {}
        for src in sources:
            results[src] = self.collect(src)
        return results

    def _scan_file(self, source: Path) -> IncludeSets:
        if not source.is_file():
            return IncludeSets(internal=[], ext_internal=[], external=[])

        try:
            content = source.read_text(encoding=self.encoding, errors="ignore")
        except (OSError, UnicodeDecodeError) as exc:
            print(f"[warning] Failed to read {source}: {exc}", file=sys.stderr)
            return IncludeSets(internal=[], ext_internal=[], external=[])

        internal: List[str] = []
        ext_internal: List[str] = []
        external: List[str] = []

        for match in INCLUDE_PATTERN.finditer(content):
            token = match.group(1)
            header = token[1:-1]
            if token.startswith('"'):
                internal.append(header)
                continue
            if any(header.startswith(prefix) for prefix in self.include_prefixes):
                ext_internal.append(header)
            else:
                external.append(header)

        return IncludeSets(
            internal=_dedupe_preserve_order(internal),
            ext_internal=_dedupe_preserve_order(ext_internal),
            external=_dedupe_preserve_order(external),
        )


def _dedupe_preserve_order(values: Iterable[str]) -> List[str]:
    seen: Dict[str, None] = {}
    for value in values:
        if value not in seen:
            seen[value] = None
    return list(seen.keys())


def resolve_include_paths(
    headings: Sequence[str],
    include_directories: Sequence[Path],
    source_file: Path,
    *,
    relative_to_source: bool,
) -> List[Path]:
    """Resolve *headings* to absolute file paths.

    Parameters
    ----------
    headings:
        Ordered include header strings to resolve.
    include_directories:
        Candidate include search paths (typically Meson include directories).
    source_file:
        Source file that issued the include directive.
    relative_to_source:
        When ``True`` the headings are treated as relative to ``source_file``;
        otherwise they are searched within ``include_directories``.
    """

    resolved: List[Path] = []
    source_dir = source_file.parent.resolve()
    candidate_roots = [inc.resolve() for inc in include_directories]

    for heading in headings:
        candidates: List[Path] = []
        if relative_to_source:
            candidates.append((source_dir / heading).resolve())
        else:
            for root in candidate_roots:
                candidates.append((root / heading).resolve())

        chosen: Optional[Path] = None
        for candidate in candidates:
            if candidate.exists():
                chosen = candidate
                break

        if chosen is None:
            if candidates:
                chosen = candidates[0]
            else:
                chosen = (source_dir / heading).resolve()

        resolved.append(chosen)

    return resolved


def _sanitize_pch_name(key: str) -> str:
    # Replace characters that are awkward in filenames (colon, whitespace, etc.).
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "_", key)
    if not cleaned:
        cleaned = "pch"
    return cleaned + ".hpp"


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect includes for Meson targets.")
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
        help="Treat angled includes starting with this prefix as ext-internal (can be repeated).",
    )
    parser.add_argument(
        "--pch-output",
        type=Path,
        default=None,
        help="Directory to emit per-target PCH headers (auto-created, files end with .hpp)",
    )
    return parser.parse_args(argv)

def get_includes_for_source(
    source: Path,
    record: MesonTargetCollector.TargetRecord,
    include_collector: IncludeCollector):
    
    if not _is_relevant_source(source):
        raise ValueError(f"Source {source} is not a relevant source file.")
    
    includes = include_collector.collect(source)
    include_dirs = record.include_paths
    resolved_internal = resolve_include_paths(
        includes.internal,
        include_dirs,
        source,
        relative_to_source=True,
    )
    resolved_ext_internal = resolve_include_paths(
        includes.ext_internal,
        include_dirs,
        source,
        relative_to_source=False,
    )
    
    includes.add_header_paths(includes.internal, resolved_internal)
    includes.add_header_paths(includes.ext_internal, resolved_ext_internal)
    
    return includes, resolved_internal + resolved_ext_internal
    

def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    subprojects = [name.strip() for name in args.subprojects.split(",") if name.strip()]

    target_collector = MesonTargetCollector(args.project_root, subprojects)
    target_collector.run()

    include_collector = IncludeCollector(args.internal_prefixes)
    pch_dir: Optional[Path] = None
    if args.pch_output:
        pch_dir = args.pch_output.resolve()
        pch_dir.mkdir(parents=True, exist_ok=True)

    for key in sorted(target_collector.targets):
        record = target_collector.targets[key]
        print()
        print("-" * 60)
        print(f"[{key}] {record.name}")
        target_includes = IncludeSets(internal=[], ext_internal=[], external=[])

        prg1 = tqdm(sorted(record.source_paths), desc="Collecting includes", unit="files")
        #prg2 = tqdm(    desc="Collecting includes (internal)", unit="files")
        for source in prg1:            
            if not _is_relevant_source(source):
                continue
            
            includes, header_sources = get_includes_for_source(
                source,
                record,
                include_collector,
            )
            nheaderstotal=0
            nheaders=0
            done_headers = set()
            while len(header_sources) > 0:
                header_sources_ = header_sources
                header_sources = []
                nheaderstotal += len(header_sources_)
                nheaders_still = len(header_sources_)
                for header in header_sources_:
                    if header in done_headers:
                        continue
                    done_headers.add(header)
                    nheaders+=1
                    #prg2.update(1)
                    #prg2.set_postfix_str(f'{nheaders}/{nheaders_still}/{nheaderstotal}')
                    includes_, header_sources__ = get_includes_for_source(
                        header,
                        record,
                        include_collector,
                    )
                    includes.add(includes_)
                    header_sources.extend(header_sources__)
                    
            target_includes.sum(includes)
                        
        if target_includes.internal:
            for header in target_includes.get_internal_headers():
                #print(f"      {header} -> {target_includes.get_header_path(header)}")
                if target_includes.get_header_path(header) == '<unresolved>':
                    print(f"WARNING: {header} (unresolved)")
        if target_includes.external:
            print("external includes:")
            for header in target_includes.get_external_headers():
                print(f"{header} [{target_includes.get_header_count(header)}]")

        if pch_dir is not None:
            pch_path = pch_dir / _sanitize_pch_name(key)
            external_headers = target_includes.get_external_headers()
            include_lines: List[str] = []
            for header in external_headers:
                if target_includes.get_header_count(header) > 1:
                    include_lines.append(f'#include <{header}>')

            content_lines = [
                "// Auto-generated precompiled header",
                f"// Target: {key}",
                "#pragma once",
                "",
            ]
            content_lines.extend(include_lines)
            content = "\n".join(content_lines) + "\n"
            try:
                pch_path.write_text(content, encoding="utf-8")
            except OSError as exc:
                print(f"[warning] Failed to write PCH header {pch_path}: {exc}", file=sys.stderr)
            else:
                print(f"[info] Wrote PCH header: {pch_path}")
    return 0


def _is_relevant_source(path: Path) -> bool:
    suffix = path.suffix.lower()
    if suffix in {".h", ".hpp", ".hh", ".hxx", ".inl", ".ipp"}:
        return True
    return path.name.lower().endswith(SOURCE_SUFFIXES)


if __name__ == "__main__":
    sys.exit(main())
