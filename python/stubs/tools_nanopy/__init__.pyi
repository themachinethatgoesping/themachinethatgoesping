"""Small python tool functions for themachinethatgoesping"""

from typing import overload

from . import (
    classhelper as classhelper,
    helper as helper,
    progressbars as progressbars,
    pyhelper as pyhelper,
    timeconv as timeconv,
    vectorinterpolators as vectorinterpolators
)


class ostream_redirect:
    """
    Context manager that redirects C++ stdout/stderr to Python sys.stdout/sys.stderr. Use as 'with ostream_redirect():' to capture C++ output in Python.
    """

    @overload
    def __init__(self) -> None:
        """Create ostream redirect with automatic start (RAII behavior)"""

    @overload
    def __init__(self, auto_start: bool = True) -> None:
        """Create ostream redirect with optional auto-start"""

    def enter(self) -> None:
        """Start redirection"""

    def exit(self) -> None:
        """Stop redirection"""

    def __enter__(self) -> ostream_redirect:
        """Enter the runtime context"""

    def __exit__(self, exc_type: object | None = None, exc_value: object | None = None, traceback: object | None = None) -> bool:
        """Exit the runtime context"""
