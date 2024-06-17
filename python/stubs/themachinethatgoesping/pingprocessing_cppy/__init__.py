"""
Python module process pings from echosounders.
"""
from __future__ import annotations
from . import watercolumn
__all__ = ['ostream_redirect', 'watercolumn']
class ostream_redirect:
    def __enter__(self) -> None:
        ...
    def __exit__(self, *args) -> None:
        ...
    def __init__(self, stdout: bool = True, stderr: bool = True) -> None:
        ...
__version__: str = '0.8.0'
