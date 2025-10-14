#!/usr/bin/env python3
"""Minimal Meson build target parser.

This script performs a lightweight textual pass over a ``meson.build`` file and
(optionally) a selected set of subprojects to discover declared build targets
(``executable()``, ``library()``, ``static_library()``, ``shared_library()``).

For each detected target the script collects string literal source entries that
look like C/C++ source files (``.c``, ``.cpp``, etc.) and stores them as
absolute paths so that follow-up tooling can analyse them further.

The parsing logic deliberately stays simple – it handles the common patterns
used throughout this repository (direct string arguments and ``files(...)``
helpers) while ignoring more advanced Meson constructs (generator outputs,
variables, custom helper functions, …). The goal is to establish a reliable,
transparent starting point that can be refined iteratively.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Sequence, Tuple

TARGET_FUNCTIONS: Tuple[str, ...] = (
    "executable",
    "library",
    "static_library",
    "shared_library",
    "extension_module",
)
SOURCE_SUFFIXES: Tuple[str, ...] = (
    ".c",
    ".cc",
    ".cxx",
    ".cpp",
    ".c++",
    ".h",
    ".m",
    ".mm",
    ".ixx",
    ".hpp",
    ".hh",
    ".hxx",
    ".h++",
    ".inl",
    ".ipp",
)
STRING_LITERAL_RE = re.compile(r"'([^'\\]*(?:\\.[^'\\]*)*)'")
CALL_HEAD_RE = re.compile(
    r"(?P<func>(?:[A-Za-z_][A-Za-z0-9_]*\.)*(?:" + "|".join(TARGET_FUNCTIONS) + r"))\s*\("
)
SUBDIR_RE = re.compile(r"subdir\s*\(\s*'([^']+)'\s*\)")
def _extract_balanced_block(
    text: str,
    start: int,
    opening: str,
    closing: str,
) -> Tuple[Optional[str], int]:
    depth = 1
    i = start
    text_len = len(text)
    in_single = False
    in_double = False
    escape = False

    while i < text_len:
        ch = text[i]
        if escape:
            escape = False
        elif ch == "\\":
            escape = True
        elif ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif not in_single and not in_double:
            if ch == opening:
                depth += 1
            elif ch == closing:
                depth -= 1
                if depth == 0:
                    return text[start:i], i + 1
        i += 1

    return None, text_len


@dataclass
class TargetRecord:
    """Represents a Meson build target extracted from a file."""

    name: str
    origin: Path
    source_paths: List[Path] = field(default_factory=list)

    def add_sources(self, sources: Iterable[Path]) -> None:
        for src in sources:
            if src not in self.source_paths:
                self.source_paths.append(src)


class MesonCallExtractor:
    """Utility to extract function call blocks from Meson files."""

    def __init__(self, text: str) -> None:
        self.text = text

    def iter_calls(self) -> Iterator[Tuple[str, str]]:
        pos = 0
        while True:
            match = CALL_HEAD_RE.search(self.text, pos)
            if not match:
                break
            func_name = match.group("func").split(".")[-1]
            args_block, end_pos = self._extract_argument_block(match.end())
            if args_block is None:
                break
            yield func_name, args_block
            pos = end_pos

    def _extract_argument_block(self, start: int) -> Tuple[Optional[str], int]:
        return _extract_balanced_block(self.text, start, "(", ")")


class MesonTargetCollector:
    """Parses Meson files to gather targets and their sources."""

    def __init__(self, project_root: Path, subprojects: Sequence[str]) -> None:
        self.project_root = project_root.resolve()
        if not self.project_root.is_dir():
            raise FileNotFoundError(f"Project root not found: {self.project_root}")
        self.meson_file = (self.project_root / "meson.build").resolve()
        self.requested_subprojects = sorted({name.strip() for name in subprojects if name.strip()})
        self.targets: Dict[str, TargetRecord] = {}
        self._visited: set[Path] = set()

    def run(self) -> None:
        if not self.meson_file.is_file():
            raise FileNotFoundError(f"Meson file not found: {self.meson_file}")

        self._parse_meson_file(self.meson_file, label="root", list_scope={}, string_scope={})

        for subproject in self.requested_subprojects:
            sub_meson = self.project_root / "subprojects" / subproject / "meson.build"
            if not sub_meson.is_file():
                print(f"[warning] Requested subproject '{subproject}' is missing: {sub_meson}", file=sys.stderr)
                continue
            self._parse_meson_file(
                sub_meson,
                label=subproject,
                list_scope={},
                string_scope={},
            )

    # ------------------------------------------------------------------
    def _parse_meson_file(
        self,
        meson_file: Path,
        label: str,
        list_scope: Optional[Dict[str, List[str]]] = None,
        string_scope: Optional[Dict[str, str]] = None,
    ) -> None:
        meson_file = meson_file.resolve()
        if meson_file in self._visited:
            return
        self._visited.add(meson_file)

        text = meson_file.read_text(encoding="utf-8")

        local_list_scope: Dict[str, List[str]] = {}
        if list_scope:
            local_list_scope.update(list_scope)

        local_string_scope: Dict[str, str] = {}
        if string_scope:
            local_string_scope.update(string_scope)

        list_updates, string_updates = self._collect_literal_lists(text, local_string_scope)
        local_list_scope.update(list_updates)
        local_string_scope.update(string_updates)

        extractor = MesonCallExtractor(text)

        for func, args in extractor.iter_calls():
            target_name, raw_sources = self._parse_call_arguments(
                args, local_list_scope, local_string_scope
            )
            if target_name is None:
                continue

            abs_sources = [self._resolve_source(meson_file.parent, raw) for raw in raw_sources]

            key = f"{label}:{target_name}"
            record = self.targets.get(key)
            if record is None:
                record = TargetRecord(name=target_name, origin=meson_file)
                self.targets[key] = record
            record.add_sources(abs_sources)

        for subdir in SUBDIR_RE.findall(text):
            sub_meson = meson_file.parent / subdir / "meson.build"
            if sub_meson.is_file():
                self._parse_meson_file(
                    sub_meson,
                    label=label,
                    list_scope=dict(local_list_scope),
                    string_scope=dict(local_string_scope),
                )

    def _parse_call_arguments(
        self,
        args: str,
        list_scope: Dict[str, List[str]],
        string_scope: Dict[str, str],
    ) -> Tuple[Optional[str], List[str]]:
        arg_slices = self._split_top_level_arguments(args)
        if not arg_slices:
            return None, []

        target_expr = arg_slices[0].strip()
        target_name = self._normalise_target_name(target_expr, string_scope)

        remaining = arg_slices[1:]
        literal_text = ",".join(remaining)
        source_literals: List[str] = []

        for match in STRING_LITERAL_RE.finditer(literal_text):
            literal = self._unescape_literal(match.group(1))
            if literal.lower().endswith(SOURCE_SUFFIXES):
                source_literals.append(literal)

        for argument in remaining:
            source_literals.extend(self._lookup_variable_sources(argument, list_scope))

        deduped: List[str] = []
        seen = set()
        for literal in source_literals:
            if literal not in seen:
                seen.add(literal)
                deduped.append(literal)

        return target_name, deduped

    def _split_top_level_arguments(self, args: str) -> List[str]:
        pieces: List[str] = []
        current: List[str] = []
        paren_depth = 0
        bracket_depth = 0
        brace_depth = 0
        in_single = False
        in_double = False
        escape = False

        for ch in args:
            if escape:
                current.append(ch)
                escape = False
                continue

            if ch == "\\":
                current.append(ch)
                escape = True
                continue

            if ch == "'" and not in_double:
                current.append(ch)
                in_single = not in_single
                continue

            if ch == '"' and not in_single:
                current.append(ch)
                in_double = not in_double
                continue

            if in_single or in_double:
                current.append(ch)
                continue

            if ch == '(':
                paren_depth += 1
            elif ch == ')':
                paren_depth -= 1
            elif ch == '[':
                bracket_depth += 1
            elif ch == ']':
                bracket_depth -= 1
            elif ch == '{':
                brace_depth += 1
            elif ch == '}':
                brace_depth -= 1

            if (
                ch == ","
                and paren_depth == 0
                and bracket_depth == 0
                and brace_depth == 0
            ):
                pieces.append("".join(current).strip())
                current = []
            else:
                current.append(ch)

        if current:
            pieces.append("".join(current).strip())

        return pieces

    def _lookup_variable_sources(self, argument: str, scope: Dict[str, List[str]]) -> List[str]:
        expr = argument.strip()
        if not expr:
            return []

        if ":" in expr:
            _, rhs = expr.split(":", 1)
            expr = rhs.strip()

        candidates = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", expr)
        sources: List[str] = []
        for candidate in candidates:
            if candidate in scope:
                for literal in scope[candidate]:
                    if literal.lower().endswith(SOURCE_SUFFIXES):
                        sources.append(literal)
        return sources

    def _normalise_target_name(self, expression: str, string_scope: Dict[str, str]) -> str:
        expr = expression.strip()
        if not expr:
            return "<unnamed>"
        if expr.startswith("'") and expr.endswith("'"):
            return self._unescape_literal(expr[1:-1])
        if expr.startswith('"') and expr.endswith('"'):
            return self._unescape_literal(expr[1:-1])
        if expr in string_scope:
            return string_scope[expr]
        return expr

    def _evaluate_string_expression(self, expression: str, scope: Dict[str, str]) -> Optional[str]:
        expr = expression.strip()
        if not expr:
            return None
        expr = expr.rstrip(",").strip()
        if not expr:
            return None
        if any(ch in expr for ch in "(){}[]"):
            return None

        tokens: List[str] = []
        current: List[str] = []
        in_single = False
        in_double = False
        escape = False

        for ch in expr:
            if escape:
                current.append(ch)
                escape = False
                continue

            if ch == "\\":
                current.append(ch)
                escape = True
                continue

            if ch == "'" and not in_double:
                current.append(ch)
                in_single = not in_single
                continue

            if ch == '"' and not in_single:
                current.append(ch)
                in_double = not in_double
                continue

            if in_single or in_double:
                current.append(ch)
                continue

            if ch == '+':
                tokens.append("".join(current).strip())
                current = []
            else:
                current.append(ch)

        if current:
            tokens.append("".join(current).strip())

        if not tokens:
            return None

        resolved: List[str] = []
        for token in tokens:
            if not token:
                continue
            if token.startswith("'") and token.endswith("'"):
                resolved.append(self._unescape_literal(token[1:-1]))
            elif token.startswith('"') and token.endswith('"'):
                resolved.append(self._unescape_literal(token[1:-1]))
            elif token in scope:
                resolved.append(scope[token])
            else:
                return None

        return "".join(resolved)

    def _collect_literal_lists(
        self,
        text: str,
        inherited_string_scope: Dict[str, str],
    ) -> Tuple[Dict[str, List[str]], Dict[str, str]]:
        list_scope: Dict[str, List[str]] = {}
        string_scope: Dict[str, str] = {}

        list_assign_re = re.compile(r"(?m)^(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*\[")
        files_assign_re = re.compile(r"(?m)^(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*files\s*\(")
        string_assign_re = re.compile(
            r"(?m)^(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?P<value>[^#\n]+)"
        )
        foreach_alias_re = re.compile(
            r"(?m)^\s*foreach\s+(?P<item>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*(?P<source>[A-Za-z_][A-Za-z0-9_]*)\b"
        )

        for match in list_assign_re.finditer(text):
            name = match.group("name")
            body, _ = _extract_balanced_block(text, match.end(), "[", "]")
            if body is None:
                continue
            literals = [self._unescape_literal(m.group(1)) for m in STRING_LITERAL_RE.finditer(body)]
            list_scope[name] = literals

        for match in files_assign_re.finditer(text):
            name = match.group("name")
            body, _ = _extract_balanced_block(text, match.end(), "(", ")")
            if body is None:
                continue
            literals = [self._unescape_literal(m.group(1)) for m in STRING_LITERAL_RE.finditer(body)]
            existing = list_scope.setdefault(name, [])
            for literal in literals:
                if literal not in existing:
                    existing.append(literal)

        evaluation_scope = dict(inherited_string_scope)

        for match in string_assign_re.finditer(text):
            name = match.group("name")
            expr = match.group("value").split("#", 1)[0].strip()
            if not expr:
                continue
            if expr[0] in "[{":
                continue
            if expr.startswith("files"):
                continue
            value = self._evaluate_string_expression(expr, evaluation_scope)
            if value is None:
                continue
            string_scope[name] = value
            evaluation_scope[name] = value

        for match in foreach_alias_re.finditer(text):
            item = match.group("item")
            source_name = match.group("source")
            referenced = list_scope.get(source_name)
            if referenced:
                list_scope[item] = referenced

        return list_scope, string_scope

    def _resolve_source(self, base_dir: Path, literal: str) -> Path:
        candidate = (base_dir / literal).resolve()
        # In Meson, paths inside files() are typically relative to current directory.
        # Even if the file does not exist yet (generated later), keep the resolved path
        # so that downstream tooling has a deterministic location to inspect.
        return candidate

    @staticmethod
    def _unescape_literal(value: str) -> str:
        return value.encode("utf-8").decode("unicode_escape")

    # ------------------------------------------------------------------
    def display(self) -> None:
        if not self.targets:
            print("[info] No targets detected.")
            return

        for key in sorted(self.targets):
            record = self.targets[key]
            label = key.split(":", 1)[0]
            print(f"[{label}] {record.name}")
            if not record.source_paths:
                print("  (no source files detected in this pass)")
                continue
            for src in sorted(record.source_paths):
                print(f"  {src}")


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------

def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parse Meson targets from a Meson project root.")
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
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    subprojects = [name.strip() for name in args.subprojects.split(",") if name.strip()]

    collector = MesonTargetCollector(args.project_root, subprojects)
    collector.run()
    collector.display()
    return 0


if __name__ == "__main__":
    sys.exit(main())
