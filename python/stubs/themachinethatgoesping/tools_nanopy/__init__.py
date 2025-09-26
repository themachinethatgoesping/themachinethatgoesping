"""
Small python tool functions for themachinethatgoesping
"""
from __future__ import annotations
import typing
from . import classhelper
from . import helper
from . import progressbars
from . import pyhelper
from . import timeconv
from . import vectorinterpolators
__all__: list[str] = ['classhelper', 'helper', 'ostream_redirect', 'progressbars', 'pyhelper', 'timeconv', 'vectorinterpolators']
class ostream_redirect:
    """
    Context manager that redirects C++ stdout/stderr to Python sys.stdout/sys.stderr. Use as 'with ostream_redirect():' to capture C++ output in Python.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __enter__(self) -> ostream_redirect:
        """
        Enter the runtime context
        """
    def __exit__(self, exc_type: typing.Any | None = None, exc_value: typing.Any | None = None, traceback: typing.Any | None = None) -> bool:
        """
        Exit the runtime context
        """
    def __init__(self) -> None:
        """
        __init__(self, auto_start: bool = True) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Create ostream redirect with automatic start (RAII behavior)
        
        2. ``__init__(self, auto_start: bool = True) -> None``
        
        Create ostream redirect with optional auto-start
        """
    def enter(self) -> None:
        """
        Start redirection
        """
    def exit(self) -> None:
        """
        Stop redirection
        """
__version__: str = '0.30.0'
