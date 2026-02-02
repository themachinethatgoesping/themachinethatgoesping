"""Classes for getting interpolated values from within vectors"""

from collections.abc import Sequence
import enum
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

from . import bivectorinterpolators as bivectorinterpolators


class t_extr_mode(enum.Enum):
    """extrapolation mode type."""

    extrapolate = 0
    """interpolate using the closest value pair in the internal x vector"""

    nearest = 2
    """return nearest value in the vector."""

    fail = 1
    """
    throw out_of_range exception if x value exceeds boundaries of internal
    vector
    """

    nan = 1
    """
    return NaN if x value exceeds boundaries of internal vector (only for
    floating point types)
    """

class o_extr_mode:
    """
    Helper class to convert between strings and enum values of type 't_extr_mode'
    """

    @overload
    def __init__(self, value: t_extr_mode = t_extr_mode.extrapolate) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> t_extr_mode:
        """enum value"""

    @value.setter
    def value(self, arg: t_extr_mode, /) -> None: ...

    __default_value__: themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_extr_mode, /) -> bool: ...

    @overload
    def __eq__(self, arg: t_extr_mode, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_extr_mode:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_extr_mode: ...

    def __deepcopy__(self, arg: dict, /) -> o_extr_mode: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_extr_mode:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> None: ...

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class NearestInterpolator:
    """
    Interpolator class to find nearest neighbors within vector data

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: type of the y values (must be floating point)
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[float] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> float: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[float]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[float]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: float) -> None: ...

    def extend(self, X: Sequence[float], Y: Sequence[float]) -> None: ...

    def insert(self, X: Sequence[float], Y: Sequence[float], bool: bool = False) -> None: ...

    def __eq__(self, other: NearestInterpolator) -> bool: ...

    def copy(self) -> NearestInterpolator:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NearestInterpolator: ...

    def __deepcopy__(self, arg: dict, /) -> NearestInterpolator: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolator:
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

class NearestInterpolatorF:
    """
    Interpolator class to find nearest neighbors within vector data

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: type of the y values (must be floating point)
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[float] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> float: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[float]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[float]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: float) -> None: ...

    def extend(self, X: Sequence[float], Y: Sequence[float]) -> None: ...

    def insert(self, X: Sequence[float], Y: Sequence[float], bool: bool = False) -> None: ...

    def __eq__(self, other: NearestInterpolatorF) -> bool: ...

    def copy(self) -> NearestInterpolatorF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NearestInterpolatorF: ...

    def __deepcopy__(self, arg: dict, /) -> NearestInterpolatorF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorF:
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

class NearestInterpolatorDF:
    """
    Interpolator class to find nearest neighbors within vector data

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: type of the y values (must be floating point)
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[float] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> float: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[float]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[float]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: float) -> None: ...

    def extend(self, X: Sequence[float], Y: Sequence[float]) -> None: ...

    def insert(self, X: Sequence[float], Y: Sequence[float], bool: bool = False) -> None: ...

    def __eq__(self, other: NearestInterpolatorDF) -> bool: ...

    def copy(self) -> NearestInterpolatorDF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NearestInterpolatorDF: ...

    def __deepcopy__(self, arg: dict, /) -> NearestInterpolatorDF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorDF:
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

class NearestInterpolatorFD:
    """
    Interpolator class to find nearest neighbors within vector data

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: type of the y values (must be floating point)
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[float] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> float: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[float]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[float]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: float) -> None: ...

    def extend(self, X: Sequence[float], Y: Sequence[float]) -> None: ...

    def insert(self, X: Sequence[float], Y: Sequence[float], bool: bool = False) -> None: ...

    def __eq__(self, other: NearestInterpolatorFD) -> bool: ...

    def copy(self) -> NearestInterpolatorFD:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NearestInterpolatorFD: ...

    def __deepcopy__(self, arg: dict, /) -> NearestInterpolatorFD: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorFD:
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

class NearestInterpolatorDI:
    """
    Interpolator class to find nearest neighbors within vector data

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: type of the y values (must be floating point)
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[int] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> int:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.int64], dict(shape=(None,), order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> int: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[int]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[int]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: int) -> None: ...

    def extend(self, X: Sequence[float], Y: Sequence[int]) -> None: ...

    def insert(self, X: Sequence[float], Y: Sequence[int], bool: bool = False) -> None: ...

    def __eq__(self, other: NearestInterpolatorDI) -> bool: ...

    def copy(self) -> NearestInterpolatorDI:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NearestInterpolatorDI: ...

    def __deepcopy__(self, arg: dict, /) -> NearestInterpolatorDI: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorDI:
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

class NearestInterpolatorFI:
    """
    Interpolator class to find nearest neighbors within vector data

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: type of the y values (must be floating point)
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[int] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> int:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.int64], dict(shape=(None,), order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> int: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[int]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[int]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: int) -> None: ...

    def extend(self, X: Sequence[float], Y: Sequence[int]) -> None: ...

    def insert(self, X: Sequence[float], Y: Sequence[int], bool: bool = False) -> None: ...

    def __eq__(self, other: NearestInterpolatorFI) -> bool: ...

    def copy(self) -> NearestInterpolatorFI:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NearestInterpolatorFI: ...

    def __deepcopy__(self, arg: dict, /) -> NearestInterpolatorFI: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorFI:
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

class NearestInterpolatorDO:
    """
    Interpolator class to find nearest neighbors within vector data

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: type of the y values (must be floating point)
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[object] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> object:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Sequence[float], mp_cores: int = 1) -> list[object]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> object: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[object]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[object]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: object) -> None: ...

    def extend(self, X: Sequence[float], Y: Sequence[object]) -> None: ...

    def insert(self, X: Sequence[float], Y: Sequence[object], bool: bool = False) -> None: ...

    def __eq__(self, other: NearestInterpolatorDO) -> bool: ...

    def copy(self) -> NearestInterpolatorDO:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NearestInterpolatorDO: ...

    def __deepcopy__(self, arg: dict, /) -> NearestInterpolatorDO: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorDO:
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

class NearestInterpolatorFO:
    """
    Interpolator class to find nearest neighbors within vector data

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: type of the y values (must be floating point)
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[object] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> object:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Sequence[float], mp_cores: int = 1) -> list[object]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> object: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[object]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[object]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: object) -> None: ...

    def extend(self, X: Sequence[float], Y: Sequence[object]) -> None: ...

    def insert(self, X: Sequence[float], Y: Sequence[object], bool: bool = False) -> None: ...

    def __eq__(self, other: NearestInterpolatorFO) -> bool: ...

    def copy(self) -> NearestInterpolatorFO:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NearestInterpolatorFO: ...

    def __deepcopy__(self, arg: dict, /) -> NearestInterpolatorFO: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorFO:
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

class LinearInterpolator:
    """
    Find linear interpolated values within vector data

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: type of the y values (must be floating point)
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[float] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> float: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[float]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[float]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: float) -> None: ...

    def extend(self, X: Sequence[float], Y: Sequence[float]) -> None: ...

    def insert(self, X: Sequence[float], Y: Sequence[float], bool: bool = False) -> None: ...

    def __eq__(self, other: LinearInterpolator) -> bool: ...

    def copy(self) -> LinearInterpolator:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> LinearInterpolator: ...

    def __deepcopy__(self, arg: dict, /) -> LinearInterpolator: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> LinearInterpolator:
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

class LinearInterpolatorF:
    """
    Find linear interpolated values within vector data

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: type of the y values (must be floating point)
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[float] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> float: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[float]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[float]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: float) -> None: ...

    def extend(self, X: Sequence[float], Y: Sequence[float]) -> None: ...

    def insert(self, X: Sequence[float], Y: Sequence[float], bool: bool = False) -> None: ...

    def __eq__(self, other: LinearInterpolatorF) -> bool: ...

    def copy(self) -> LinearInterpolatorF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> LinearInterpolatorF: ...

    def __deepcopy__(self, arg: dict, /) -> LinearInterpolatorF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> LinearInterpolatorF:
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

class LinearInterpolatorDF:
    """
    Find linear interpolated values within vector data

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: type of the y values (must be floating point)
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[float] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> float: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[float]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[float]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: float) -> None: ...

    def extend(self, X: Sequence[float], Y: Sequence[float]) -> None: ...

    def insert(self, X: Sequence[float], Y: Sequence[float], bool: bool = False) -> None: ...

    def __eq__(self, other: LinearInterpolatorDF) -> bool: ...

    def copy(self) -> LinearInterpolatorDF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> LinearInterpolatorDF: ...

    def __deepcopy__(self, arg: dict, /) -> LinearInterpolatorDF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> LinearInterpolatorDF:
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

class LinearInterpolatorFD:
    """
    Find linear interpolated values within vector data

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: type of the y values (must be floating point)
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[float] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> float: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[float]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[float]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: float) -> None: ...

    def extend(self, X: Sequence[float], Y: Sequence[float]) -> None: ...

    def insert(self, X: Sequence[float], Y: Sequence[float], bool: bool = False) -> None: ...

    def __eq__(self, other: LinearInterpolatorFD) -> bool: ...

    def copy(self) -> LinearInterpolatorFD:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> LinearInterpolatorFD: ...

    def __deepcopy__(self, arg: dict, /) -> LinearInterpolatorFD: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> LinearInterpolatorFD:
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

class AkimaInterpolator:
    """
    Interpolator class to perform a (modified) akima interpolation. Uses
    boost makima interpolator. Note: this interpolator acts as linear
    interpolator if less than 4 values are stored.

    Template Args:
        XYType:: type of the x and y values (must be floating point))
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[float] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> float: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[float]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[float]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: float) -> None:
        """
        append an x- and the corresponding y value to the interpolator data.
        Exception: raises domain error, strong exception guarantee

        Args:
            x: value, must be > than all existing x values
            y: corresponding y value
        """

    def extend(self, X: Sequence[float], Y: Sequence[float]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee

        Args:
            X: list of x values. Must be sorted in ascending order. All x
               values must be larger than the largest x value in the
               interpolator data.
            Y: list of corresponding Y values. Must be same size as X
        """

    def insert(self, X: Sequence[float], Y: Sequence[float], bool: bool = False) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        This call is much more expensive than extend as it requires copying
        data and sorting.
        Exception: raises domain error, strong exception guarantee

        Args:
            X: list of x values. (Does not have to be sorted. But must be
               unique)
            Y: list of corresponding Y values. Must be same size as X
            is_sorted: this indicates that X is already sorted in ascending
                       order. (default: false)
        """

    def __eq__(self, other: AkimaInterpolator) -> bool: ...

    def copy(self) -> AkimaInterpolator:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> AkimaInterpolator: ...

    def __deepcopy__(self, arg: dict, /) -> AkimaInterpolator: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> AkimaInterpolator:
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

class AkimaInterpolatorF:
    """
    Interpolator class to perform a (modified) akima interpolation. Uses
    boost makima interpolator. Note: this interpolator acts as linear
    interpolator if less than 4 values are stored.

    Template Args:
        XYType:: type of the x and y values (must be floating point))
    """

    def __init__(self, X: Sequence[float] = [], Y: Sequence[float] = [], extrapolation_mode: o_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Interpolator object from a vector of pairs
        usage: interpolated_y_value = interpolator.interpolate(x_value)

        Args:
            X: X vector; must be unique and sorted in ascending order. same
               size as Y!
            Y: Y vector; must be unique and sorted in ascending order. same
               size as X!
            extrapolation_mode: :option o_extr_mode <themachinethatgoesping.to
                                ols.vectorinterpolators.t_extr_mode>` object
                                that describes the extrapolation mode
        """

    @overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target

        Args:
            target_x: find the corresponding y value for this x value

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        get interpolated y values for given x targets (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corresponding y value
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1 (no parallelism). Set to higher values to
                      enable parallel interpolation.

        Returns:
            std::vector_YType corresponding y values
        """

    def get_y(self, target_x: float) -> float: ...

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    def set_data_XY(self, X: Sequence[float], Y: Sequence[float]) -> None:
        """
        change the input data to these X and Y vectors

        Args:
            X:: x vector (must be same size, must be sorted in ascending
              order)
            Y:: y vector (must be same size)
        """

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_data_Y(self) -> list[float]:
        """
        return the y component of the internal data vector

        Returns:
            std::vector_YType
        """

    def append(self, x: float, y: float) -> None:
        """
        append an x- and the corresponding y value to the interpolator data.
        Exception: raises domain error, strong exception guarantee

        Args:
            x: value, must be > than all existing x values
            y: corresponding y value
        """

    def extend(self, X: Sequence[float], Y: Sequence[float]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee

        Args:
            X: list of x values. Must be sorted in ascending order. All x
               values must be larger than the largest x value in the
               interpolator data.
            Y: list of corresponding Y values. Must be same size as X
        """

    def insert(self, X: Sequence[float], Y: Sequence[float], bool: bool = False) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        This call is much more expensive than extend as it requires copying
        data and sorting.
        Exception: raises domain error, strong exception guarantee

        Args:
            X: list of x values. (Does not have to be sorted. But must be
               unique)
            Y: list of corresponding Y values. Must be same size as X
            is_sorted: this indicates that X is already sorted in ascending
                       order. (default: false)
        """

    def __eq__(self, other: AkimaInterpolatorF) -> bool: ...

    def copy(self) -> AkimaInterpolatorF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> AkimaInterpolatorF: ...

    def __deepcopy__(self, arg: dict, /) -> AkimaInterpolatorF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> AkimaInterpolatorF:
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

class SlerpInterpolator:
    """
    Class that implements a slerp interpolation for vectors. Data is
    internally represented in quaternions using lib eigen. Interfaces to
    represent the data in yaw, pitch, roll angles are provided. the
    __call__ equivalent to get interpolated yaw pitch roll is the ypr
    function

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: floating point type of the y quaternion values (must be
              floating point)
    """

    def __init__(self, X: Sequence[float] = [], Yaw: Sequence[float] = [], Pitch: Sequence[float] = [], Roll: Sequence[float] = [], input_in_degrees: bool = True, extrapolation_mode: t_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Slerp Interpolator object using vectors of x, yaw,
        pitch and roll

        Args:
            X: vector; must be unique and sorted in ascending order
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true (default) yaw,pitch and roll are in °,
                              otherwise [rad]
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object that describes the extrapolation mode
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    @overload
    def __call__(self, target_x: float, output_in_degrees: bool = True) -> list[float]:
        """
        get the interpolated yaw, pitch and roll values for given x target

        Args:
            target_x: find the corresponding y value for this x value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Sequence[float], output_in_degrees: bool = True) -> list[list[float]]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding yaw, pitch and roll value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    @overload
    def ypr(self, target_x: float, output_in_degrees: bool = True) -> list[float]:
        """
        get the interpolated yaw, pitch and roll values for given x target

        Args:
            target_x: find the corresponding y value for this x value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    @overload
    def ypr(self, targets_x: Sequence[float], output_in_degrees: bool = True) -> list[list[float]]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding yaw, pitch and roll value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    @overload
    def set_data_XYPR(self, X: Sequence[float], Yaw: Sequence[float], Pitch: Sequence[float], Roll: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        change the input data to these X, yaw, pitch, roll vectors (will be
        converted to quaternion)

        Args:
            X: vector; must be unique and sorted in ascending order
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def set_data_XYPR(self, X: Sequence[float], YPR: Sequence[Sequence[float]], input_in_degrees: bool = True) -> None: ...

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> "xt::xtensor_container_xt_uvector<double_xsimd_aligned_allocator<double_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>":
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def get_data_YPR(self, output_in_degrees: bool = True) -> list[list[float]]:
        """
        return the internal yrp data vector

        Args:
            output_in_degrees: convert yaw, pitch and roll to degrees (default
                               = True)

        Returns:
            std::vector_std_array<3_YType> YPR
        """

    @overload
    def append(self, x: float, yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> None:
        """
        append an x, yaw, pitch, roll data point

        Args:
            X: must be larger than all internal data points
            yaw: rotation around z axis
            pitch: rotation around y axis
            roll: rotation around x axis
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def append(self, x: float, ypr: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        append an x, yaw, pitch, roll data point

        Args:
            X: must be larger than all internal data points
            ypr: array with one yaw, pitch and roll data point
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def extend(self, X: Sequence[float], Yaw: Sequence[float], Pitch: Sequence[float], Roll: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        append data with lists of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique and sorted in ascending order
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def extend(self, X: Sequence[float], YPR: Sequence[Sequence[float]], input_in_degrees: bool = True) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique and sorted in ascending order
            ypr: vector with yaw, pitch and roll data points. Must be same
                 size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def insert(self, X: Sequence[float], Yaw: Sequence[float], Pitch: Sequence[float], Roll: Sequence[float], input_in_degrees: bool = True, bool: bool = False) -> None:
        """
        append data with lists of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def insert(self, X: Sequence[float], YPR: Sequence[Sequence[float]], input_in_degrees: bool = True, bool: bool = False) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique
            ypr: vector with yaw, pitch and roll data points. Must be same
                 size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    def __eq__(self, other: SlerpInterpolator) -> bool: ...

    def copy(self) -> SlerpInterpolator:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SlerpInterpolator: ...

    def __deepcopy__(self, arg: dict, /) -> SlerpInterpolator: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SlerpInterpolator:
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

class SlerpInterpolatorF:
    """
    Class that implements a slerp interpolation for vectors. Data is
    internally represented in quaternions using lib eigen. Interfaces to
    represent the data in yaw, pitch, roll angles are provided. the
    __call__ equivalent to get interpolated yaw pitch roll is the ypr
    function

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: floating point type of the y quaternion values (must be
              floating point)
    """

    def __init__(self, X: Sequence[float] = [], Yaw: Sequence[float] = [], Pitch: Sequence[float] = [], Roll: Sequence[float] = [], input_in_degrees: bool = True, extrapolation_mode: t_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Slerp Interpolator object using vectors of x, yaw,
        pitch and roll

        Args:
            X: vector; must be unique and sorted in ascending order
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true (default) yaw,pitch and roll are in °,
                              otherwise [rad]
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object that describes the extrapolation mode
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    @overload
    def __call__(self, target_x: float, output_in_degrees: bool = True) -> list[float]:
        """
        get the interpolated yaw, pitch and roll values for given x target

        Args:
            target_x: find the corresponding y value for this x value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Sequence[float], output_in_degrees: bool = True) -> list[list[float]]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding yaw, pitch and roll value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    @overload
    def ypr(self, target_x: float, output_in_degrees: bool = True) -> list[float]:
        """
        get the interpolated yaw, pitch and roll values for given x target

        Args:
            target_x: find the corresponding y value for this x value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    @overload
    def ypr(self, targets_x: Sequence[float], output_in_degrees: bool = True) -> list[list[float]]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding yaw, pitch and roll value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    @overload
    def set_data_XYPR(self, X: Sequence[float], Yaw: Sequence[float], Pitch: Sequence[float], Roll: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        change the input data to these X, yaw, pitch, roll vectors (will be
        converted to quaternion)

        Args:
            X: vector; must be unique and sorted in ascending order
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def set_data_XYPR(self, X: Sequence[float], YPR: Sequence[Sequence[float]], input_in_degrees: bool = True) -> None: ...

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>":
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def get_data_YPR(self, output_in_degrees: bool = True) -> list[list[float]]:
        """
        return the internal yrp data vector

        Args:
            output_in_degrees: convert yaw, pitch and roll to degrees (default
                               = True)

        Returns:
            std::vector_std_array<3_YType> YPR
        """

    @overload
    def append(self, x: float, yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> None:
        """
        append an x, yaw, pitch, roll data point

        Args:
            X: must be larger than all internal data points
            yaw: rotation around z axis
            pitch: rotation around y axis
            roll: rotation around x axis
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def append(self, x: float, ypr: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        append an x, yaw, pitch, roll data point

        Args:
            X: must be larger than all internal data points
            ypr: array with one yaw, pitch and roll data point
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def extend(self, X: Sequence[float], Yaw: Sequence[float], Pitch: Sequence[float], Roll: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        append data with lists of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique and sorted in ascending order
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def extend(self, X: Sequence[float], YPR: Sequence[Sequence[float]], input_in_degrees: bool = True) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique and sorted in ascending order
            ypr: vector with yaw, pitch and roll data points. Must be same
                 size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def insert(self, X: Sequence[float], Yaw: Sequence[float], Pitch: Sequence[float], Roll: Sequence[float], input_in_degrees: bool = True, bool: bool = False) -> None:
        """
        append data with lists of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def insert(self, X: Sequence[float], YPR: Sequence[Sequence[float]], input_in_degrees: bool = True, bool: bool = False) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique
            ypr: vector with yaw, pitch and roll data points. Must be same
                 size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    def __eq__(self, other: SlerpInterpolatorF) -> bool: ...

    def copy(self) -> SlerpInterpolatorF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SlerpInterpolatorF: ...

    def __deepcopy__(self, arg: dict, /) -> SlerpInterpolatorF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SlerpInterpolatorF:
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

class SlerpInterpolatorFD:
    """
    Class that implements a slerp interpolation for vectors. Data is
    internally represented in quaternions using lib eigen. Interfaces to
    represent the data in yaw, pitch, roll angles are provided. the
    __call__ equivalent to get interpolated yaw pitch roll is the ypr
    function

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: floating point type of the y quaternion values (must be
              floating point)
    """

    def __init__(self, X: Sequence[float] = [], Yaw: Sequence[float] = [], Pitch: Sequence[float] = [], Roll: Sequence[float] = [], input_in_degrees: bool = True, extrapolation_mode: t_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Slerp Interpolator object using vectors of x, yaw,
        pitch and roll

        Args:
            X: vector; must be unique and sorted in ascending order
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true (default) yaw,pitch and roll are in °,
                              otherwise [rad]
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object that describes the extrapolation mode
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    @overload
    def __call__(self, target_x: float, output_in_degrees: bool = True) -> list[float]:
        """
        get the interpolated yaw, pitch and roll values for given x target

        Args:
            target_x: find the corresponding y value for this x value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Sequence[float], output_in_degrees: bool = True) -> list[list[float]]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding yaw, pitch and roll value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    @overload
    def ypr(self, target_x: float, output_in_degrees: bool = True) -> list[float]:
        """
        get the interpolated yaw, pitch and roll values for given x target

        Args:
            target_x: find the corresponding y value for this x value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    @overload
    def ypr(self, targets_x: Sequence[float], output_in_degrees: bool = True) -> list[list[float]]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding yaw, pitch and roll value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    @overload
    def set_data_XYPR(self, X: Sequence[float], Yaw: Sequence[float], Pitch: Sequence[float], Roll: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        change the input data to these X, yaw, pitch, roll vectors (will be
        converted to quaternion)

        Args:
            X: vector; must be unique and sorted in ascending order
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def set_data_XYPR(self, X: Sequence[float], YPR: Sequence[Sequence[float]], input_in_degrees: bool = True) -> None: ...

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>":
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def get_data_YPR(self, output_in_degrees: bool = True) -> list[list[float]]:
        """
        return the internal yrp data vector

        Args:
            output_in_degrees: convert yaw, pitch and roll to degrees (default
                               = True)

        Returns:
            std::vector_std_array<3_YType> YPR
        """

    @overload
    def append(self, x: float, yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> None:
        """
        append an x, yaw, pitch, roll data point

        Args:
            X: must be larger than all internal data points
            yaw: rotation around z axis
            pitch: rotation around y axis
            roll: rotation around x axis
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def append(self, x: float, ypr: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        append an x, yaw, pitch, roll data point

        Args:
            X: must be larger than all internal data points
            ypr: array with one yaw, pitch and roll data point
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def extend(self, X: Sequence[float], Yaw: Sequence[float], Pitch: Sequence[float], Roll: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        append data with lists of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique and sorted in ascending order
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def extend(self, X: Sequence[float], YPR: Sequence[Sequence[float]], input_in_degrees: bool = True) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique and sorted in ascending order
            ypr: vector with yaw, pitch and roll data points. Must be same
                 size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def insert(self, X: Sequence[float], Yaw: Sequence[float], Pitch: Sequence[float], Roll: Sequence[float], input_in_degrees: bool = True, bool: bool = False) -> None:
        """
        append data with lists of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def insert(self, X: Sequence[float], YPR: Sequence[Sequence[float]], input_in_degrees: bool = True, bool: bool = False) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique
            ypr: vector with yaw, pitch and roll data points. Must be same
                 size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    def __eq__(self, other: SlerpInterpolatorFD) -> bool: ...

    def copy(self) -> SlerpInterpolatorFD:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SlerpInterpolatorFD: ...

    def __deepcopy__(self, arg: dict, /) -> SlerpInterpolatorFD: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SlerpInterpolatorFD:
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

class SlerpInterpolatorDF:
    """
    Class that implements a slerp interpolation for vectors. Data is
    internally represented in quaternions using lib eigen. Interfaces to
    represent the data in yaw, pitch, roll angles are provided. the
    __call__ equivalent to get interpolated yaw pitch roll is the ypr
    function

    Template Args:
        XType:: type of the x values (must be floating point)
        YType:: floating point type of the y quaternion values (must be
              floating point)
    """

    def __init__(self, X: Sequence[float] = [], Yaw: Sequence[float] = [], Pitch: Sequence[float] = [], Roll: Sequence[float] = [], input_in_degrees: bool = True, extrapolation_mode: t_extr_mode = t_extr_mode.extrapolate) -> None:
        """
        Construct a new Slerp Interpolator object using vectors of x, yaw,
        pitch and roll

        Args:
            X: vector; must be unique and sorted in ascending order
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true (default) yaw,pitch and roll are in °,
                              otherwise [rad]
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object that describes the extrapolation mode
        """

    def empty(self) -> bool:
        """check if the interpolator contains data"""

    @overload
    def __call__(self, target_x: float, output_in_degrees: bool = True) -> list[float]:
        """
        get the interpolated yaw, pitch and roll values for given x target

        Args:
            target_x: find the corresponding y value for this x value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    @overload
    def __call__(self, targets_x: Sequence[float], output_in_degrees: bool = True) -> list[list[float]]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding yaw, pitch and roll value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    @overload
    def ypr(self, target_x: float, output_in_degrees: bool = True) -> list[float]:
        """
        get the interpolated yaw, pitch and roll values for given x target

        Args:
            target_x: find the corresponding y value for this x value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    @overload
    def ypr(self, targets_x: Sequence[float], output_in_degrees: bool = True) -> list[list[float]]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        (vectorized call)

        Args:
            targets_x: vector of x values. For each of these values find the
                       corrsponding yaw, pitch and roll value
            output_in_degrees: if true, yaw pitch and roll input values are in
                               ° otherwise rad

        Returns:
            corresponding y value
        """

    def set_extrapolation_mode(self, extrapolation_mode: o_extr_mode) -> None:
        """
        Set the extrapolation mode

        Args:
            extrapolation_mode: :py:class:`t_extr_mode <themachinethatgoesping
                                .tools.vectorinterpolators.t_extr_mode>`
                                object (enumerator) that describes the
                                extrapolation mode
        """

    def get_extrapolation_mode(self) -> o_extr_mode:
        """
        Get the currently set extrapolation mode

        Returns:
            :o_extr_mode
        """

    @overload
    def set_data_XYPR(self, X: Sequence[float], Yaw: Sequence[float], Pitch: Sequence[float], Roll: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        change the input data to these X, yaw, pitch, roll vectors (will be
        converted to quaternion)

        Args:
            X: vector; must be unique and sorted in ascending order
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def set_data_XYPR(self, X: Sequence[float], YPR: Sequence[Sequence[float]], input_in_degrees: bool = True) -> None: ...

    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector

        Returns:
            std::vector_XType
        """

    def get_sampled_X(self, downsample_interval: float, max_gap: float = float('nan')) -> "xt::xtensor_container_xt_uvector<double_xsimd_aligned_allocator<double_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>":
        """
        Get downsampled x values from the interpolator data.

        This function returns x values at regular intervals, respecting gaps
        in the data. Useful for reducing the number of interpolation points
        when dealing with large datasets.

        Args:
            downsample_interval: The interval between consecutive sampled x
                                 values
            max_gap: Maximum allowed gap between consecutive x values. If the
                     gap between consecutive x values exceeds this, a new
                     sampling segment is started.

        Returns:
            xt::xtensor_XType_1 A 1D tensor containing the downsampled x
               values

        @note The returned values are actual x values from the data, not
        interpolated positions.
              Use these values with the interpolator to get corresponding y
              values.
        """

    def get_data_YPR(self, output_in_degrees: bool = True) -> list[list[float]]:
        """
        return the internal yrp data vector

        Args:
            output_in_degrees: convert yaw, pitch and roll to degrees (default
                               = True)

        Returns:
            std::vector_std_array<3_YType> YPR
        """

    @overload
    def append(self, x: float, yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> None:
        """
        append an x, yaw, pitch, roll data point

        Args:
            X: must be larger than all internal data points
            yaw: rotation around z axis
            pitch: rotation around y axis
            roll: rotation around x axis
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def append(self, x: float, ypr: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        append an x, yaw, pitch, roll data point

        Args:
            X: must be larger than all internal data points
            ypr: array with one yaw, pitch and roll data point
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def extend(self, X: Sequence[float], Yaw: Sequence[float], Pitch: Sequence[float], Roll: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        append data with lists of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique and sorted in ascending order
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def extend(self, X: Sequence[float], YPR: Sequence[Sequence[float]], input_in_degrees: bool = True) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique and sorted in ascending order
            ypr: vector with yaw, pitch and roll data points. Must be same
                 size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def insert(self, X: Sequence[float], Yaw: Sequence[float], Pitch: Sequence[float], Roll: Sequence[float], input_in_degrees: bool = True, bool: bool = False) -> None:
        """
        append data with lists of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique
            yaw: vector with yaw data (rotation around z axis). Must be same
                 size as X!
            pitch: vector with pitch data (rotation around y axis). Must be
                   same size as X!
            roll: vector with roll data (rotation around x axis). Must be same
                  size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    @overload
    def insert(self, X: Sequence[float], YPR: Sequence[Sequence[float]], input_in_degrees: bool = True, bool: bool = False) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)

        Args:
            X: vector; must be unique
            ypr: vector with yaw, pitch and roll data points. Must be same
                 size as X!
            input_in_degrees: if true, yaw pitch and roll input values are in
                              ° otherwise rad
        """

    def __eq__(self, other: SlerpInterpolatorDF) -> bool: ...

    def copy(self) -> SlerpInterpolatorDF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SlerpInterpolatorDF: ...

    def __deepcopy__(self, arg: dict, /) -> SlerpInterpolatorDF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SlerpInterpolatorDF:
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
