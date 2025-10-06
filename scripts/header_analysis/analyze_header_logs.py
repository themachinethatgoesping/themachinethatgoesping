#!/usr/bin/env python3
"""Analyse GCC include logs produced by ``capture_gcc_headers.py``.

The script walks every ``.headers.log`` file inside the given directory,
reconstructs the include tree for each translation unit, and accumulates
statistics per header:

- ``times_included`` – how often the header appeared in the logs
- ``includes_caused`` – average number of descendant includes triggered
  by the header per occurrence
- ``score`` – the product of ``times_included`` and ``includes_caused``

Headers with the highest score are prime candidates for precompiled header
(PCH) experiments because they are included often *and* contribute large
chains of additional includes.
"""

from __future__ import annotations

import argparse
import math
import sys
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

HEADER_LINE_RE = re.compile(r"^(?P<dots>\.+)\s+(?P<header>.+)$")


@dataclass
class HeaderNode:
    name: str
    children: List["HeaderNode"] = field(default_factory=list)


@dataclass
class HeaderAggregate:
    times_included: int = 0
    descendant_total: int = 0
    unique_descendant_total: int = 0
    logs: set[str] = field(default_factory=set)

    def includes_caused(self) -> float:
        if self.times_included == 0:
            return 0.0
        return self.descendant_total / self.times_included

    def unique_includes_caused(self) -> float:
        if self.times_included == 0:
            return 0.0
        return self.unique_descendant_total / self.times_included

    def score(self) -> float:
        return self.times_included * self.includes_caused()


def _parse_log(path: Path) -> List[HeaderNode]:
    roots: List[HeaderNode] = []
    stack: List[HeaderNode] = []

    for raw_line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = HEADER_LINE_RE.match(raw_line)
        if not match:
            continue
        depth = len(match.group("dots"))
        header_name = match.group("header").strip()
        node = HeaderNode(header_name)

        while len(stack) >= depth:
            stack.pop()
        if stack:
            stack[-1].children.append(node)
        else:
            roots.append(node)
        stack.append(node)

    return roots


def _accumulate(node: HeaderNode, aggregates: Dict[str, HeaderAggregate], log_label: str) -> Tuple[int, set[str]]:
    total_descendants = 0
    unique_headers: set[str] = set()

    for child in node.children:
        child_descendants, child_unique = _accumulate(child, aggregates, log_label)
        total_descendants += 1 + child_descendants
        unique_headers.add(child.name)
        unique_headers.update(child_unique)

    aggregate = aggregates.setdefault(node.name, HeaderAggregate())
    aggregate.times_included += 1
    aggregate.descendant_total += total_descendants
    aggregate.unique_descendant_total += len(unique_headers)
    aggregate.logs.add(log_label)

    return total_descendants, unique_headers


def analyse_logs(log_dir: Path, *, min_times: int, top: int | None) -> List[Tuple[str, HeaderAggregate]]:
    aggregates: Dict[str, HeaderAggregate] = {}

    log_files = sorted(log_dir.rglob("*.headers.log"))
    if not log_files:
        raise SystemExit(f"No .headers.log files found in {log_dir}")

    for log_file in log_files:
        roots = _parse_log(log_file)
        log_label = str(log_file.relative_to(log_dir))
        for root in roots:
            _accumulate(root, aggregates, log_label)

    filtered = [item for item in aggregates.items() if item[1].times_included >= min_times]
    filtered.sort(key=lambda item: item[1].score(), reverse=True)
    if top is not None:
        filtered = filtered[:top]
    return filtered


def _format_number(value: float) -> str:
    if math.isclose(value, round(value)):
        return str(int(round(value)))
    return f"{value:.2f}"


def print_table(rows: List[Tuple[str, HeaderAggregate]]) -> None:
    columns = ("Header", "Score", "Times", "Includes caused", "Unique includes", "Logs")

    table: List[Tuple[str, str, str, str, str, str]] = []
    for header, agg in rows:
        score = _format_number(agg.score())
        times = str(agg.times_included)
        includes = _format_number(agg.includes_caused())
        unique = _format_number(agg.unique_includes_caused())
        logs = str(len(agg.logs))
        table.append((header, score, times, includes, unique, logs))

    widths = [len(col) for col in columns]
    for row in table:
        for idx, cell in enumerate(row):
            widths[idx] = max(widths[idx], len(cell))

    header_line = "  ".join(col.ljust(widths[idx]) for idx, col in enumerate(columns))
    separator = "  ".join("-" * width for width in widths)
    print(header_line)
    print(separator)
    for row in table:
        print("  ".join(cell.ljust(widths[idx]) for idx, cell in enumerate(row)))


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyse GCC include logs and rank headers by impact.")
    parser.add_argument(
        "log_dir",
        type=Path,
        help="Directory that contains .headers.log files (typically builddir/header-logs)",
    )
    parser.add_argument(
        "--min-times",
        type=int,
        default=1,
        help="Only show headers that appear at least N times (default: 1)",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=None,
        help="Limit output to the top-N headers by score",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    ns = parse_args(argv or [])
    log_dir = ns.log_dir.resolve()
    results = analyse_logs(log_dir, min_times=ns.min_times, top=ns.top)
    if not results:
        print("No headers matched the filter.")
        return 0
    print_table(results)
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main(sys.argv[1:]))
