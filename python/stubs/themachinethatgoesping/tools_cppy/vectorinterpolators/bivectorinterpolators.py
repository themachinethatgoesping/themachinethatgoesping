"""
2D interpolators
"""
from __future__ import annotations
import numpy
import themachinethatgoesping.tools_cppy.vectorinterpolators
__all__: list[str] = ['BiAkimaInterpolator', 'BiAkimaInterpolatorF', 'BiLinearInterpolator', 'BiLinearInterpolatorDF', 'BiLinearInterpolatorF', 'BiLinearInterpolatorFD', 'BiNearestInterpolator', 'BiNearestInterpolatorDF', 'BiNearestInterpolatorDI', 'BiNearestInterpolatorF', 'BiNearestInterpolatorFD', 'BiNearestInterpolatorFI']
class BiAkimaInterpolator:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiAkimaInterpolator:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, row_coordinates: list[float], column_coordinates: list[float], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
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
    def __deepcopy__(self, arg0: dict) -> BiAkimaInterpolator:
        ...
    def __eq__(self, other: BiAkimaInterpolator) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append_row(self, row_coordinate: float, column_coordinates: list[float], values: list[float]) -> None:
        ...
    def copy(self) -> BiAkimaInterpolator:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
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
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiAkimaInterpolatorF:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiAkimaInterpolatorF:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, row_coordinates: list[float], column_coordinates: list[float], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
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
    def __deepcopy__(self, arg0: dict) -> BiAkimaInterpolatorF:
        ...
    def __eq__(self, other: BiAkimaInterpolatorF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append_row(self, row_coordinate: float, column_coordinates: list[float], values: list[float]) -> None:
        ...
    def copy(self) -> BiAkimaInterpolatorF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
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
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiLinearInterpolator:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiLinearInterpolator:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, row_coordinates: list[float], column_coordinates: list[float], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
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
    def __deepcopy__(self, arg0: dict) -> BiLinearInterpolator:
        ...
    def __eq__(self, other: BiLinearInterpolator) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append_row(self, row_coordinate: float, column_coordinates: list[float], values: list[float]) -> None:
        ...
    def copy(self) -> BiLinearInterpolator:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
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
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiLinearInterpolatorDF:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiLinearInterpolatorDF:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, row_coordinates: list[float], column_coordinates: list[float], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
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
    def __deepcopy__(self, arg0: dict) -> BiLinearInterpolatorDF:
        ...
    def __eq__(self, other: BiLinearInterpolatorDF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append_row(self, row_coordinate: float, column_coordinates: list[float], values: list[float]) -> None:
        ...
    def copy(self) -> BiLinearInterpolatorDF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
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
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiLinearInterpolatorF:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiLinearInterpolatorF:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, row_coordinates: list[float], column_coordinates: list[float], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
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
    def __deepcopy__(self, arg0: dict) -> BiLinearInterpolatorF:
        ...
    def __eq__(self, other: BiLinearInterpolatorF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append_row(self, row_coordinate: float, column_coordinates: list[float], values: list[float]) -> None:
        ...
    def copy(self) -> BiLinearInterpolatorF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
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
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiLinearInterpolatorFD:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiLinearInterpolatorFD:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, row_coordinates: list[float], column_coordinates: list[float], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
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
    def __deepcopy__(self, arg0: dict) -> BiLinearInterpolatorFD:
        ...
    def __eq__(self, other: BiLinearInterpolatorFD) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append_row(self, row_coordinate: float, column_coordinates: list[float], values: list[float]) -> None:
        ...
    def copy(self) -> BiLinearInterpolatorFD:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
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
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiNearestInterpolator:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiNearestInterpolator:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, row_coordinates: list[float], column_coordinates: list[float], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
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
    def __deepcopy__(self, arg0: dict) -> BiNearestInterpolator:
        ...
    def __eq__(self, other: BiNearestInterpolator) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append_row(self, row_coordinate: float, column_coordinates: list[float], values: list[float]) -> None:
        ...
    def copy(self) -> BiNearestInterpolator:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
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
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiNearestInterpolatorDF:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiNearestInterpolatorDF:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, row_coordinates: list[float], column_coordinates: list[float], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
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
    def __deepcopy__(self, arg0: dict) -> BiNearestInterpolatorDF:
        ...
    def __eq__(self, other: BiNearestInterpolatorDF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append_row(self, row_coordinate: float, column_coordinates: list[float], values: list[float]) -> None:
        ...
    def copy(self) -> BiNearestInterpolatorDF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
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
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiNearestInterpolatorDI:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiNearestInterpolatorDI:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, row_coordinates: list[float], column_coordinates: list[float], mp_cores: int = 1) -> numpy.ndarray[numpy.int64]:
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
    def __deepcopy__(self, arg0: dict) -> BiNearestInterpolatorDI:
        ...
    def __eq__(self, other: BiNearestInterpolatorDI) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append_row(self, row_coordinate: float, column_coordinates: list[float], values: list[int]) -> None:
        ...
    def copy(self) -> BiNearestInterpolatorDI:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
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
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiNearestInterpolatorF:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiNearestInterpolatorF:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, row_coordinates: list[float], column_coordinates: list[float], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
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
    def __deepcopy__(self, arg0: dict) -> BiNearestInterpolatorF:
        ...
    def __eq__(self, other: BiNearestInterpolatorF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append_row(self, row_coordinate: float, column_coordinates: list[float], values: list[float]) -> None:
        ...
    def copy(self) -> BiNearestInterpolatorF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
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
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiNearestInterpolatorFD:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiNearestInterpolatorFD:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, row_coordinates: list[float], column_coordinates: list[float], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
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
    def __deepcopy__(self, arg0: dict) -> BiNearestInterpolatorFD:
        ...
    def __eq__(self, other: BiNearestInterpolatorFD) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append_row(self, row_coordinate: float, column_coordinates: list[float], values: list[float]) -> None:
        ...
    def copy(self) -> BiNearestInterpolatorFD:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
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
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class BiNearestInterpolatorFI:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiNearestInterpolatorFI:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, row_coordinates: list[float], column_coordinates: list[float], mp_cores: int = 1) -> numpy.ndarray[numpy.int64]:
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
    def __deepcopy__(self, arg0: dict) -> BiNearestInterpolatorFI:
        ...
    def __eq__(self, other: BiNearestInterpolatorFI) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append_row(self, row_coordinate: float, column_coordinates: list[float], values: list[int]) -> None:
        ...
    def copy(self) -> BiNearestInterpolatorFI:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        ...
    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode
        
        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
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
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode
        
        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
