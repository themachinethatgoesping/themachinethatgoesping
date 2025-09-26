"""
Classes that provide python helper functionality
"""
from __future__ import annotations
import typing
__all__: list[str] = ['PyIndexerSlice']
class PyIndexerSlice:
    """
    A structure to hold a slice
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> PyIndexerSlice:
        ...
    def __deepcopy__(self, arg: dict) -> PyIndexerSlice:
        ...
    def __eq__(self, other: PyIndexerSlice) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, start: int = 9223372036854775807, stop: int = 9223372036854775807, step: int = 1) -> None:
        """
        __init__(self, slice: object) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> PyIndexerSlice:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def start(self) -> int:
        """
        < the start index of the slice (None if not sliced)
        """
    @start.setter
    def start(self, arg: int) -> None:
        """
        < the start index of the slice (None if not sliced)
        """
    @property
    def step(self) -> int:
        """
        < the step size of the slice (1 if not sliced)
        """
    @step.setter
    def step(self, arg: int) -> None:
        """
        < the step size of the slice (1 if not sliced)
        """
    @property
    def stop(self) -> int:
        """
        < the stop index of the slice (None if not sliced) < (stop is
        exclusive)
        """
    @stop.setter
    def stop(self, arg: int) -> None:
        """
        < the stop index of the slice (None if not sliced) < (stop is
        exclusive)
        """
