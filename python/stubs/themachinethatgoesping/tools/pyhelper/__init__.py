"""Classes that provide python helper functionality"""
from __future__ import annotations
import themachinethatgoesping.tools.pyhelper
import typing

__all__ = [
    "PyIndexerSlice"
]


class PyIndexerSlice():
    """
    A structure to hold a slice
    """
    def __copy__(self) -> PyIndexerSlice: ...
    def __deepcopy__(self, arg0: dict) -> PyIndexerSlice: ...
    def __eq__(self, other: PyIndexerSlice) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self, start: int = 9223372036854775807, stop: int = 9223372036854775807, step: int = 1) -> None: ...
    @typing.overload
    def __init__(self, slice: object) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> PyIndexerSlice: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> PyIndexerSlice: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
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

        :type: int
        """
    @start.setter
    def start(self, arg0: int) -> None:
        """
        < the start index of the slice (None if not sliced)
        """
    @property
    def step(self) -> int:
        """
        < the step size of the slice (1 if not sliced)

        :type: int
        """
    @step.setter
    def step(self, arg0: int) -> None:
        """
        < the step size of the slice (1 if not sliced)
        """
    @property
    def stop(self) -> int:
        """
        < the stop index of the slice (None if not sliced) < (stop is
        exclusive)

        :type: int
        """
    @stop.setter
    def stop(self, arg0: int) -> None:
        """
        < the stop index of the slice (None if not sliced) < (stop is
        exclusive)
        """
    pass
