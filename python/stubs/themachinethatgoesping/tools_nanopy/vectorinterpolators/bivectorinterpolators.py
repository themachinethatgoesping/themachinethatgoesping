"""
2D interpolators
"""
from __future__ import annotations
import collections.abc
import themachinethatgoesping.tools_nanopy.vectorinterpolators
import typing
__all__: list[str] = ['BiAkimaInterpolator', 'BiAkimaInterpolatorF', 'BiLinearInterpolator', 'BiLinearInterpolatorDF', 'BiLinearInterpolatorF', 'BiLinearInterpolatorFD', 'BiNearestInterpolator', 'BiNearestInterpolatorDF', 'BiNearestInterpolatorDI', 'BiNearestInterpolatorF', 'BiNearestInterpolatorFD', 'BiNearestInterpolatorFI']
class BiAkimaInterpolator:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, row_coordinates: collections.abc.Sequence[float], column_coordinates: collections.abc.Sequence[float], mp_cores: int = 1) -> ...:
        """
        get interpolated y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> BiAkimaInterpolator:
        ...
    def __deepcopy__(self, arg: dict) -> BiAkimaInterpolator:
        ...
    def __eq__(self, other: BiAkimaInterpolator) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = ...) -> None:
        ...
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
    def append_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def clear(self) -> None:
        ...
    def copy(self) -> BiAkimaInterpolator:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator]:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def get_row_coordinates(self) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiAkimaInterpolatorF:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, row_coordinates: collections.abc.Sequence[float], column_coordinates: collections.abc.Sequence[float], mp_cores: int = 1) -> ...:
        """
        get interpolated y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> BiAkimaInterpolatorF:
        ...
    def __deepcopy__(self, arg: dict) -> BiAkimaInterpolatorF:
        ...
    def __eq__(self, other: BiAkimaInterpolatorF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = ...) -> None:
        ...
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
    def append_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def clear(self) -> None:
        ...
    def copy(self) -> BiAkimaInterpolatorF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolatorF]:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def get_row_coordinates(self) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiLinearInterpolator:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, row_coordinates: collections.abc.Sequence[float], column_coordinates: collections.abc.Sequence[float], mp_cores: int = 1) -> ...:
        """
        get interpolated y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> BiLinearInterpolator:
        ...
    def __deepcopy__(self, arg: dict) -> BiLinearInterpolator:
        ...
    def __eq__(self, other: BiLinearInterpolator) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = ...) -> None:
        ...
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
    def append_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def clear(self) -> None:
        ...
    def copy(self) -> BiLinearInterpolator:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolator]:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def get_row_coordinates(self) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiLinearInterpolatorDF:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, row_coordinates: collections.abc.Sequence[float], column_coordinates: collections.abc.Sequence[float], mp_cores: int = 1) -> ...:
        """
        get interpolated y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> BiLinearInterpolatorDF:
        ...
    def __deepcopy__(self, arg: dict) -> BiLinearInterpolatorDF:
        ...
    def __eq__(self, other: BiLinearInterpolatorDF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = ...) -> None:
        ...
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
    def append_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def clear(self) -> None:
        ...
    def copy(self) -> BiLinearInterpolatorDF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolatorDF]:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def get_row_coordinates(self) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiLinearInterpolatorF:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, row_coordinates: collections.abc.Sequence[float], column_coordinates: collections.abc.Sequence[float], mp_cores: int = 1) -> ...:
        """
        get interpolated y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> BiLinearInterpolatorF:
        ...
    def __deepcopy__(self, arg: dict) -> BiLinearInterpolatorF:
        ...
    def __eq__(self, other: BiLinearInterpolatorF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = ...) -> None:
        ...
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
    def append_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def clear(self) -> None:
        ...
    def copy(self) -> BiLinearInterpolatorF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolatorF]:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def get_row_coordinates(self) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiLinearInterpolatorFD:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, row_coordinates: collections.abc.Sequence[float], column_coordinates: collections.abc.Sequence[float], mp_cores: int = 1) -> ...:
        """
        get interpolated y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> BiLinearInterpolatorFD:
        ...
    def __deepcopy__(self, arg: dict) -> BiLinearInterpolatorFD:
        ...
    def __eq__(self, other: BiLinearInterpolatorFD) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = ...) -> None:
        ...
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
    def append_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def clear(self) -> None:
        ...
    def copy(self) -> BiLinearInterpolatorFD:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolatorFD]:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def get_row_coordinates(self) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiNearestInterpolator:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, row_coordinates: collections.abc.Sequence[float], column_coordinates: collections.abc.Sequence[float], mp_cores: int = 1) -> ...:
        """
        get interpolated y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> BiNearestInterpolator:
        ...
    def __deepcopy__(self, arg: dict) -> BiNearestInterpolator:
        ...
    def __eq__(self, other: BiNearestInterpolator) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = ...) -> None:
        ...
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
    def append_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def clear(self) -> None:
        ...
    def copy(self) -> BiNearestInterpolator:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.NearestInterpolator]:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def get_row_coordinates(self) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiNearestInterpolatorDF:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, row_coordinates: collections.abc.Sequence[float], column_coordinates: collections.abc.Sequence[float], mp_cores: int = 1) -> ...:
        """
        get interpolated y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> BiNearestInterpolatorDF:
        ...
    def __deepcopy__(self, arg: dict) -> BiNearestInterpolatorDF:
        ...
    def __eq__(self, other: BiNearestInterpolatorDF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = ...) -> None:
        ...
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
    def append_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def clear(self) -> None:
        ...
    def copy(self) -> BiNearestInterpolatorDF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.NearestInterpolatorDF]:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def get_row_coordinates(self) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiNearestInterpolatorDI:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, row_coordinates: collections.abc.Sequence[float], column_coordinates: collections.abc.Sequence[float], mp_cores: int = 1) -> ...:
        """
        get interpolated y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> BiNearestInterpolatorDI:
        ...
    def __deepcopy__(self, arg: dict) -> BiNearestInterpolatorDI:
        ...
    def __eq__(self, other: BiNearestInterpolatorDI) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = ...) -> None:
        ...
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
    def append_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[int]) -> None:
        ...
    def clear(self) -> None:
        ...
    def copy(self) -> BiNearestInterpolatorDI:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.NearestInterpolatorDI]:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def get_row_coordinates(self) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[int]) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiNearestInterpolatorF:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, row_coordinates: collections.abc.Sequence[float], column_coordinates: collections.abc.Sequence[float], mp_cores: int = 1) -> ...:
        """
        get interpolated y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> BiNearestInterpolatorF:
        ...
    def __deepcopy__(self, arg: dict) -> BiNearestInterpolatorF:
        ...
    def __eq__(self, other: BiNearestInterpolatorF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = ...) -> None:
        ...
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
    def append_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def clear(self) -> None:
        ...
    def copy(self) -> BiNearestInterpolatorF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.NearestInterpolatorF]:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def get_row_coordinates(self) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiNearestInterpolatorFD:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, row_coordinates: collections.abc.Sequence[float], column_coordinates: collections.abc.Sequence[float], mp_cores: int = 1) -> ...:
        """
        get interpolated y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> BiNearestInterpolatorFD:
        ...
    def __deepcopy__(self, arg: dict) -> BiNearestInterpolatorFD:
        ...
    def __eq__(self, other: BiNearestInterpolatorFD) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = ...) -> None:
        ...
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
    def append_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def clear(self) -> None:
        ...
    def copy(self) -> BiNearestInterpolatorFD:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.NearestInterpolatorFD]:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def get_row_coordinates(self) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[float]) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiNearestInterpolatorFI:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, row_coordinates: collections.abc.Sequence[float], column_coordinates: collections.abc.Sequence[float], mp_cores: int = 1) -> ...:
        """
        get interpolated y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> BiNearestInterpolatorFI:
        ...
    def __deepcopy__(self, arg: dict) -> BiNearestInterpolatorFI:
        ...
    def __eq__(self, other: BiNearestInterpolatorFI) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = ...) -> None:
        ...
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
    def append_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[int]) -> None:
        ...
    def clear(self) -> None:
        ...
    def copy(self) -> BiNearestInterpolatorFI:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.NearestInterpolatorFI]:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def get_row_coordinates(self) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert_row(self, row_coordinate: float, column_coordinates: collections.abc.Sequence[float], values: collections.abc.Sequence[int]) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
