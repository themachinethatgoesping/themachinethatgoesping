"""
Small python tool functions for themachinethatgoesping
"""
from __future__ import annotations
from . import classhelper
from . import helper
from . import progressbars
from . import pyhelper
from . import timeconv
from . import vectorinterpolators
__all__ = ['classhelper', 'helper', 'ostream_redirect', 'progressbars', 'pyhelper', 'timeconv', 'vectorinterpolators']
class ostream_redirect:
    def __enter__(self) -> None:
        ...
    def __exit__(self, *args) -> None:
        ...
    def __init__(self, stdout: bool = True, stderr: bool = True) -> None:
        ...
__version__: str = '0.21.5'
