"""
Python module to read, write and process single- and multibeam echosounder data formats
"""
from __future__ import annotations
from . import filetemplates
from . import kongsbergall
from . import pingtools
from . import simradraw
__all__ = ['filetemplates', 'kongsbergall', 'ostream_redirect', 'pingtools', 'simradraw']
class ostream_redirect:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __enter__(self) -> None:
        ...
    def __exit__(self, *args) -> None:
        ...
    def __init__(self, stdout: bool = True, stderr: bool = True) -> None:
        ...
__version__: str = '0.43.0'
