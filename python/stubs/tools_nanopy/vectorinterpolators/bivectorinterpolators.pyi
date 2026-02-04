"""2D interpolators"""

from collections.abc import Sequence
from typing import Annotated

import numpy
from numpy.typing import NDArray

import themachinethatgoesping.tools_nanopy.vectorinterpolators


class BiLinearInterpolator:
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None: ...

    def clear(self) -> None: ...

    def size(self) -> int: ...

    def get_row_coordinates(self) -> list[float]: ...

    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolator]: ...

    def __call__(self, row_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], column_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding y value

        Returns:
            corresponding y value
        """

    def empty(self) -> bool: ...

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """

    def append_row(self, row_coordinate: float, column_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> None: ...

    def insert_row(self, row_coordinate: float, column_coordinates: Sequence[float], values: Sequence[float]) -> None: ...

    def __eq__(self, other: BiLinearInterpolator) -> bool: ...

    def copy(self) -> BiLinearInterpolator:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BiLinearInterpolator: ...

    def __deepcopy__(self, arg: dict, /) -> BiLinearInterpolator: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiLinearInterpolator:
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

class BiLinearInterpolatorF:
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None: ...

    def clear(self) -> None: ...

    def size(self) -> int: ...

    def get_row_coordinates(self) -> list[float]: ...

    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolatorF]: ...

    def __call__(self, row_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], column_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding y value

        Returns:
            corresponding y value
        """

    def empty(self) -> bool: ...

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """

    def append_row(self, row_coordinate: float, column_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> None: ...

    def insert_row(self, row_coordinate: float, column_coordinates: Sequence[float], values: Sequence[float]) -> None: ...

    def __eq__(self, other: BiLinearInterpolatorF) -> bool: ...

    def copy(self) -> BiLinearInterpolatorF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BiLinearInterpolatorF: ...

    def __deepcopy__(self, arg: dict, /) -> BiLinearInterpolatorF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiLinearInterpolatorF:
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

class BiLinearInterpolatorDF:
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None: ...

    def clear(self) -> None: ...

    def size(self) -> int: ...

    def get_row_coordinates(self) -> list[float]: ...

    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolatorDF]: ...

    def __call__(self, row_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], column_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding y value

        Returns:
            corresponding y value
        """

    def empty(self) -> bool: ...

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """

    def append_row(self, row_coordinate: float, column_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> None: ...

    def insert_row(self, row_coordinate: float, column_coordinates: Sequence[float], values: Sequence[float]) -> None: ...

    def __eq__(self, other: BiLinearInterpolatorDF) -> bool: ...

    def copy(self) -> BiLinearInterpolatorDF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BiLinearInterpolatorDF: ...

    def __deepcopy__(self, arg: dict, /) -> BiLinearInterpolatorDF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiLinearInterpolatorDF:
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

class BiLinearInterpolatorFD:
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None: ...

    def clear(self) -> None: ...

    def size(self) -> int: ...

    def get_row_coordinates(self) -> list[float]: ...

    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolatorFD]: ...

    def __call__(self, row_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], column_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding y value

        Returns:
            corresponding y value
        """

    def empty(self) -> bool: ...

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """

    def append_row(self, row_coordinate: float, column_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> None: ...

    def insert_row(self, row_coordinate: float, column_coordinates: Sequence[float], values: Sequence[float]) -> None: ...

    def __eq__(self, other: BiLinearInterpolatorFD) -> bool: ...

    def copy(self) -> BiLinearInterpolatorFD:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BiLinearInterpolatorFD: ...

    def __deepcopy__(self, arg: dict, /) -> BiLinearInterpolatorFD: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiLinearInterpolatorFD:
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

class BiAkimaInterpolator:
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None: ...

    def clear(self) -> None: ...

    def size(self) -> int: ...

    def get_row_coordinates(self) -> list[float]: ...

    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator]: ...

    def __call__(self, row_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], column_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding y value

        Returns:
            corresponding y value
        """

    def empty(self) -> bool: ...

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """

    def append_row(self, row_coordinate: float, column_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> None: ...

    def insert_row(self, row_coordinate: float, column_coordinates: Sequence[float], values: Sequence[float]) -> None: ...

    def __eq__(self, other: BiAkimaInterpolator) -> bool: ...

    def copy(self) -> BiAkimaInterpolator:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BiAkimaInterpolator: ...

    def __deepcopy__(self, arg: dict, /) -> BiAkimaInterpolator: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiAkimaInterpolator:
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

class BiAkimaInterpolatorF:
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None: ...

    def clear(self) -> None: ...

    def size(self) -> int: ...

    def get_row_coordinates(self) -> list[float]: ...

    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolatorF]: ...

    def __call__(self, row_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], column_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding y value

        Returns:
            corresponding y value
        """

    def empty(self) -> bool: ...

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """

    def append_row(self, row_coordinate: float, column_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> None: ...

    def insert_row(self, row_coordinate: float, column_coordinates: Sequence[float], values: Sequence[float]) -> None: ...

    def __eq__(self, other: BiAkimaInterpolatorF) -> bool: ...

    def copy(self) -> BiAkimaInterpolatorF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BiAkimaInterpolatorF: ...

    def __deepcopy__(self, arg: dict, /) -> BiAkimaInterpolatorF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiAkimaInterpolatorF:
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

class BiNearestInterpolator:
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None: ...

    def clear(self) -> None: ...

    def size(self) -> int: ...

    def get_row_coordinates(self) -> list[float]: ...

    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.NearestInterpolator]: ...

    def __call__(self, row_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], column_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding y value

        Returns:
            corresponding y value
        """

    def empty(self) -> bool: ...

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """

    def append_row(self, row_coordinate: float, column_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> None: ...

    def insert_row(self, row_coordinate: float, column_coordinates: Sequence[float], values: Sequence[float]) -> None: ...

    def __eq__(self, other: BiNearestInterpolator) -> bool: ...

    def copy(self) -> BiNearestInterpolator:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BiNearestInterpolator: ...

    def __deepcopy__(self, arg: dict, /) -> BiNearestInterpolator: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiNearestInterpolator:
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

class BiNearestInterpolatorF:
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None: ...

    def clear(self) -> None: ...

    def size(self) -> int: ...

    def get_row_coordinates(self) -> list[float]: ...

    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.NearestInterpolatorF]: ...

    def __call__(self, row_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], column_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding y value

        Returns:
            corresponding y value
        """

    def empty(self) -> bool: ...

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """

    def append_row(self, row_coordinate: float, column_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> None: ...

    def insert_row(self, row_coordinate: float, column_coordinates: Sequence[float], values: Sequence[float]) -> None: ...

    def __eq__(self, other: BiNearestInterpolatorF) -> bool: ...

    def copy(self) -> BiNearestInterpolatorF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BiNearestInterpolatorF: ...

    def __deepcopy__(self, arg: dict, /) -> BiNearestInterpolatorF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiNearestInterpolatorF:
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

class BiNearestInterpolatorDF:
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None: ...

    def clear(self) -> None: ...

    def size(self) -> int: ...

    def get_row_coordinates(self) -> list[float]: ...

    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.NearestInterpolatorDF]: ...

    def __call__(self, row_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], column_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding y value

        Returns:
            corresponding y value
        """

    def empty(self) -> bool: ...

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """

    def append_row(self, row_coordinate: float, column_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> None: ...

    def insert_row(self, row_coordinate: float, column_coordinates: Sequence[float], values: Sequence[float]) -> None: ...

    def __eq__(self, other: BiNearestInterpolatorDF) -> bool: ...

    def copy(self) -> BiNearestInterpolatorDF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BiNearestInterpolatorDF: ...

    def __deepcopy__(self, arg: dict, /) -> BiNearestInterpolatorDF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiNearestInterpolatorDF:
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

class BiNearestInterpolatorFD:
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None: ...

    def clear(self) -> None: ...

    def size(self) -> int: ...

    def get_row_coordinates(self) -> list[float]: ...

    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.NearestInterpolatorFD]: ...

    def __call__(self, row_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], column_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding y value

        Returns:
            corresponding y value
        """

    def empty(self) -> bool: ...

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """

    def append_row(self, row_coordinate: float, column_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> None: ...

    def insert_row(self, row_coordinate: float, column_coordinates: Sequence[float], values: Sequence[float]) -> None: ...

    def __eq__(self, other: BiNearestInterpolatorFD) -> bool: ...

    def copy(self) -> BiNearestInterpolatorFD:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BiNearestInterpolatorFD: ...

    def __deepcopy__(self, arg: dict, /) -> BiNearestInterpolatorFD: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiNearestInterpolatorFD:
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

class BiNearestInterpolatorDI:
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None: ...

    def clear(self) -> None: ...

    def size(self) -> int: ...

    def get_row_coordinates(self) -> list[float]: ...

    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.NearestInterpolatorDI]: ...

    def __call__(self, row_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], column_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.int64], dict(order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding y value

        Returns:
            corresponding y value
        """

    def empty(self) -> bool: ...

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """

    def append_row(self, row_coordinate: float, column_coordinates: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values: Annotated[NDArray[numpy.int64], dict(shape=(None,), order='A')]) -> None: ...

    def insert_row(self, row_coordinate: float, column_coordinates: Sequence[float], values: Sequence[int]) -> None: ...

    def __eq__(self, other: BiNearestInterpolatorDI) -> bool: ...

    def copy(self) -> BiNearestInterpolatorDI:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BiNearestInterpolatorDI: ...

    def __deepcopy__(self, arg: dict, /) -> BiNearestInterpolatorDI: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiNearestInterpolatorDI:
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

class BiNearestInterpolatorFI:
    def __init__(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None: ...

    def clear(self) -> None: ...

    def size(self) -> int: ...

    def get_row_coordinates(self) -> list[float]: ...

    def get_col_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.NearestInterpolatorFI]: ...

    def __call__(self, row_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], column_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.int64], dict(order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding y value

        Returns:
            corresponding y value
        """

    def empty(self) -> bool: ...

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """

    def append_row(self, row_coordinate: float, column_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values: Annotated[NDArray[numpy.int64], dict(shape=(None,), order='A')]) -> None: ...

    def insert_row(self, row_coordinate: float, column_coordinates: Sequence[float], values: Sequence[int]) -> None: ...

    def __eq__(self, other: BiNearestInterpolatorFI) -> bool: ...

    def copy(self) -> BiNearestInterpolatorFI:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BiNearestInterpolatorFI: ...

    def __deepcopy__(self, arg: dict, /) -> BiNearestInterpolatorFI: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BiNearestInterpolatorFI:
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
