"""Classes that provide python helper functionality"""

from typing import overload


class PyIndexerSlice:
    """A structure to hold a slice"""

    @overload
    def __init__(self, start: int = 9223372036854775807, stop: int = 9223372036854775807, step: int = 1) -> None: ...

    @overload
    def __init__(self, slice: object) -> None: ...

    @property
    def start(self) -> int:
        """the start index of the slice (None if not sliced)"""

    @start.setter
    def start(self, arg: int, /) -> None: ...

    @property
    def stop(self) -> int:
        """the stop index of the slice (None if not sliced) (stop is exclusive)"""

    @stop.setter
    def stop(self, arg: int, /) -> None: ...

    @property
    def step(self) -> int:
        """the step size of the slice (1 if not sliced)"""

    @step.setter
    def step(self, arg: int, /) -> None: ...

    def __eq__(self, other: PyIndexerSlice) -> bool: ...

    def copy(self) -> PyIndexerSlice:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> PyIndexerSlice: ...

    def __deepcopy__(self, arg: dict, /) -> PyIndexerSlice: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> PyIndexerSlice:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
