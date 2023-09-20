"""
Python module to read, write and process single- and multibeam echosounder data formats
"""
from __future__ import annotations
from . import em3000
from . import filetemplates
from . import pingtools
from . import simrad
__all__ = ['em3000', 'filetemplates', 'ostream_redirect', 'pingtools', 'simrad']
class ostream_redirect:
    def __enter__(self) -> None:
        ...
    def __exit__(self, *args) -> None:
        ...
    def __init__(self, stdout: bool = ..., stderr: bool = ...) -> None:
        ...
__version__: str = '0.27.3'
