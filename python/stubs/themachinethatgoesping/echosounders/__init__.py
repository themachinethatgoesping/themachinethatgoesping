"""Python module to read, write and process single- and multibeam echosounder data formats"""
from __future__ import annotations
import themachinethatgoesping.echosounders
import typing

__all__ = [
    "ostream_redirect",
    "simrad"
]


class ostream_redirect():
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...
    def __init__(self, stdout: bool = True, stderr: bool = True) -> None: ...
    pass
__version__ = '0.5.6'
