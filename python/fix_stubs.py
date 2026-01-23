#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2022 - 2026 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

"""
Post-process nanobind-generated stubs to fix invalid Python syntax.

This script fixes:
1. numpy.ndarray[dtype=float64, ..., order='A'] -> numpy.ndarray[numpy.float64]
2. nanobind.nb_func -> typing.Callable[..., typing.Any]
3. Docstring indentation issues (Template parameter blocks)
4. Other invalid type annotations that cause syntax errors

Run after nanobind.stubgen to ensure valid Python syntax for type checkers and sphinx-autoapi.
"""

import re
import sys
from pathlib import Path


def fix_ndarray_annotation(match: re.Match) -> str:
    """Convert numpy.ndarray[dtype=X, ...] to valid numpy.typing.NDArray[numpy.X] or numpy.ndarray."""
    dtype = match.group(1)
    
    # Map common dtypes to numpy types
    dtype_map = {
        'float64': 'numpy.floating[typing.Any]',
        'float32': 'numpy.floating[typing.Any]',
        'int64': 'numpy.signedinteger[typing.Any]',
        'int32': 'numpy.signedinteger[typing.Any]',
        'uint64': 'numpy.unsignedinteger[typing.Any]',
        'uint32': 'numpy.unsignedinteger[typing.Any]',
        'uint16': 'numpy.unsignedinteger[typing.Any]',
        'uint8': 'numpy.unsignedinteger[typing.Any]',
        'bool': 'numpy.bool_',
        'complex64': 'numpy.complexfloating[typing.Any, typing.Any]',
        'complex128': 'numpy.complexfloating[typing.Any, typing.Any]',
    }
    
    numpy_dtype = dtype_map.get(dtype, 'typing.Any')
    return f'numpy.ndarray[typing.Any, numpy.dtype[{numpy_dtype}]]'


def fix_docstring_indentation(content: str) -> str:
    """Fix docstring indentation issues that cause Sphinx/docutils errors.
    
    Converts patterns like:
        Template parameter ``XType:``:
            type description
    To:
        Template parameter ``XType:``: type description
        
    Also fixes wrapped lines like:
        (must be floating
                point)
    To:
        (must be floating point)
    """
    # First, fix wrapped lines within docstrings where the continuation has extra indentation
    # This pattern matches text that continues on the next line with extra indentation
    # e.g., "(must be floating\n        point)" -> "(must be floating point)"
    content = re.sub(
        r'(\(must be [^\n]+)\n\s+(point\))',
        r'\1 \2',
        content
    )
    
    # More general fix: join lines where continuation has inconsistent indentation in docstrings
    # Pattern: "word\n        continuation" where continuation is indented more than the context
    content = re.sub(
        r'(floating)\n\s+(point\))',
        r'\1 \2',
        content
    )
    
    # Fix "Template parameter" blocks with indented descriptions
    # Pattern: "Template parameter ``name:``:\n    description" -> "Template parameter ``name:``: description"
    content = re.sub(
        r'(Template parameter ``[^`]+``:)\s*\n\s+',
        r'\1 ',
        content
    )
    
    # Also fix "Parameter" blocks that have the same issue
    content = re.sub(
        r'(Parameter ``[^`]+``:)\s*\n\s+',
        r'\1 ',
        content
    )
    
    # Remove empty lines between consecutive "Template parameter" lines in docstrings
    # These cause RST parsing issues
    content = re.sub(
        r'(Template parameter ``[^`]+``:[^\n]+)\n\s*\n(\s*Template parameter)',
        r'\1\n\2',
        content
    )
    
    return content


def fix_stub_file(filepath: Path) -> bool:
    """Fix invalid syntax in a single stub file. Returns True if modified."""
    content = filepath.read_text(encoding='utf-8')
    original = content
    
    # Fix C++ template syntax in class names (e.g., FilePackageCache<XML_Parameter_Channel>)
    # Replace with valid Python identifier by using underscores
    content = re.sub(
        r'class (\w+)<([^>]+)>:',
        lambda m: f'class {m.group(1)}_{m.group(2).replace("::", "_").replace(",", "_").replace(" ", "")}:',
        content
    )
    
    # Also fix template syntax in type annotations and function parameters
    content = re.sub(
        r'(\w+)<([^>]+)>',
        lambda m: f'{m.group(1)}_{m.group(2).replace("::", "_").replace(",", "_").replace(" ", "")}' if not m.group(1) in ['list', 'dict', 'set', 'tuple', 'Optional', 'Union', 'Callable', 'typing', 'numpy'] else m.group(0),
        content
    )
    
    # Fix C++ std:: types in return annotations (e.g., std::unique_ptr<...>)
    content = re.sub(
        r'"std::[^"]*"',
        'typing.Any',
        content
    )
    
    # Fix numpy.ndarray[dtype=X, ..., order='Y'] patterns
    # Match: numpy.ndarray[dtype=float64, ..., order='A']
    content = re.sub(
        r"numpy\.ndarray\[dtype=(\w+),\s*\.\.\.,\s*order='[A-Z]'\]",
        fix_ndarray_annotation,
        content
    )
    
    # Fix nanobind.nb_func references (replace with Callable)
    content = re.sub(
        r'nanobind\.nb_func',
        'typing.Callable[..., typing.Any]',
        content
    )
    
    # Fix other nanobind references that might appear
    content = re.sub(
        r'nanobind\.nb_method',
        'typing.Callable[..., typing.Any]',
        content
    )
    
    # Fix docstring indentation issues
    content = fix_docstring_indentation(content)
    
    # Ensure typing import exists if we used typing.Any or typing.Callable
    if 'typing.Any' in content or 'typing.Callable' in content:
        if 'import typing' not in content:
            # Add import after the docstring/header
            if content.startswith('"""'):
                # Find end of docstring
                end_docstring = content.find('"""', 3) + 3
                content = content[:end_docstring] + '\nimport typing' + content[end_docstring:]
            elif content.startswith("'''"):
                end_docstring = content.find("'''", 3) + 3
                content = content[:end_docstring] + '\nimport typing' + content[end_docstring:]
            else:
                # Add at the beginning after any initial comments
                lines = content.split('\n')
                insert_idx = 0
                for i, line in enumerate(lines):
                    if not line.startswith('#') and line.strip():
                        insert_idx = i
                        break
                lines.insert(insert_idx, 'import typing')
                content = '\n'.join(lines)
    
    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return True
    return False


def fix_stubs_in_directory(directory: Path) -> int:
    """Fix all stub files in a directory recursively. Returns count of modified files."""
    modified = 0
    for stub_file in directory.rglob('*.py'):
        if fix_stub_file(stub_file):
            modified += 1
            print(f"  Fixed: {stub_file.relative_to(directory)}")
    
    # Also check .pyi files
    for stub_file in directory.rglob('*.pyi'):
        if fix_stub_file(stub_file):
            modified += 1
            print(f"  Fixed: {stub_file.relative_to(directory)}")
    
    return modified


def main():
    if len(sys.argv) < 2:
        # Default to the stubs directory relative to this script
        script_dir = Path(__file__).parent
        stubs_dir = script_dir / 'stubs'
    else:
        stubs_dir = Path(sys.argv[1])
    
    if not stubs_dir.exists():
        print(f"Warning: Stubs directory not found: {stubs_dir}")
        print("Skipping stub fixes (directory may not have been created yet)")
        sys.exit(0)  # Exit successfully - this is not a fatal error
    
    print(f"Fixing stubs in: {stubs_dir}")
    modified = fix_stubs_in_directory(stubs_dir)
    print(f"Modified {modified} file(s)")
    

if __name__ == '__main__':
    main()
