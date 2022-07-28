"""Small python tool functions for themachinethatgoesping"""
from __future__ import annotations
import themachinethatgoesping.tools
import typing

__all__ = [
    "classhelpers",
    "ostream_redirect",
    "timeconv",
    "vectorinterpolators"
]


class ostream_redirect():
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...
    def __init__(self, stdout: bool = True, stderr: bool = True) -> None: ...
    pass
