"""Classes for getting interpolated values from within vectors"""
from __future__ import annotations
import themachinethatgoesping.tools.vectorinterpolators
import typing
import pybind11_stubgen.typing_ext

__all__ = [
    "AkimaInterpolator",
    "LinearInterpolator",
    "NearestInterpolator",
    "SlerpInterpolator",
    "extrapolate",
    "fail",
    "nearest",
    "t_extr_mode"
]


class AkimaInterpolator():
    """
    Interpolator class to perform a (modified) akima interpolation. Uses
    boost makima interpolator. Note: this interpolator acts as linear
    interpolator if less than 4 values are stored.
    """
    @typing.overload
    def __call__(self, target_x: float) -> float: 
        """
        get the interpolated y value for given x target

        Parameter ``target_x``:
            find the corresponding y value for this x value

        Returns:
            corresponding y value

        get nearest y values for given x targets (vectorized call)

        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value

        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: typing.List[float]) -> typing.List[float]: ...
    def __copy__(self) -> AkimaInterpolator: ...
    def __deepcopy__(self, arg0: dict) -> AkimaInterpolator: ...
    def __eq__(self, other: AkimaInterpolator) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self, X: typing.List[float] = [], Y: typing.List[float] = [], extrapolation_mode: t_extr_mode = t_extr_mode.extrapolate) -> None: 
        """
        Construct a new Interpolator object from a vector of pairs usage:
        interpolated_y_value = interpolator.interpolate(x_value)

        Parameter ``X``:
            X vector; must be unique and sorted in ascending order. same size
            as Y!

        Parameter ``Y``:
            Y vector; must be unique and sorted in ascending order. same size
            as X!

        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object that describes the extrapolation mode
        """
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def append(self, x: float, y: float) -> None: 
        """
        append an x- and the corresponding y value to the interpolator data.
        Exception: raises domain error, strong exception guarantee

        Parameter ``x``:
            value, must be > than all existing x values

        Parameter ``y``:
            corresponding y value
        """
    def copy(self) -> AkimaInterpolator: 
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool: 
        """
        check if the interpolator contains data
        """
    def extend(self, X: typing.List[float], Y: typing.List[float]) -> None: 
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee

        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.

        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> AkimaInterpolator: 
        """
        create T_CLASS object from bytearray
        """
    def get_data_X(self) -> typing.List[float]: 
        """
        return the x component of the internal data vector

        Returns:
            std::vector<double>
        """
    def get_data_Y(self) -> typing.List[float]: 
        """
        return the y component of the internal data vector

        Returns:
            std::vector<YType>
        """
    def get_extrapolation_mode(self) -> t_extr_mode: 
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def insert(self, X: typing.List[float], Y: typing.List[float], bool: bool = False) -> None: 
        """
        append x and y value lists to the interpolator data (vectorized call)
        This call is much more expensive than extend as it requires copying
        data and sorting. Exception: raises domain error, strong exception
        guarantee

        Parameter ``X``:
            list of x values. (Does not have to be sorted. But must be unique)

        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X

        Parameter ``is_sorted``:
            this indicates that X is already sorted in ascending order.
            (default: false)
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_data_XY(self, X: typing.List[float], Y: typing.List[float]) -> None: 
        """
        change the input data to these X and Y vectors

        Parameter ``X:``:
            x vector (must be same size, must be sorted in ascending order)

        Parameter ``Y:``:
            y vector (must be same size)
        """
    def set_extrapolation_mode(self, extrapolation_mode: t_extr_mode) -> None: 
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
    pass
class LinearInterpolator():
    """
    Find linear interpolated values within vector data
    """
    @typing.overload
    def __call__(self, target_x: float) -> float: 
        """
        get the interpolated y value for given x target

        Parameter ``target_x``:
            find the corresponding y value for this x value

        Returns:
            corresponding y value

        get nearest y values for given x targets (vectorized call)

        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value

        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: typing.List[float]) -> typing.List[float]: ...
    def __copy__(self) -> LinearInterpolator: ...
    def __deepcopy__(self, arg0: dict) -> LinearInterpolator: ...
    def __eq__(self, other: LinearInterpolator) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self, X: typing.List[float] = [], Y: typing.List[float] = [], extrapolation_mode: t_extr_mode = t_extr_mode.extrapolate) -> None: 
        """
        Construct a new Interpolator object from a vector of pairs usage:
        interpolated_y_value = interpolator.interpolate(x_value)

        Parameter ``X``:
            X vector; must be unique and sorted in ascending order. same size
            as Y!

        Parameter ``Y``:
            Y vector; must be unique and sorted in ascending order. same size
            as X!

        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object that describes the extrapolation mode
        """
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def append(self, x: float, y: float) -> None: 
        """
        append an x- and the corresponding y value to the interpolator data.
        Exception: raises domain error, strong exception guarantee

        Parameter ``x``:
            value, must be > than all existing x values

        Parameter ``y``:
            corresponding y value
        """
    def copy(self) -> LinearInterpolator: 
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool: 
        """
        check if the interpolator contains data
        """
    def extend(self, X: typing.List[float], Y: typing.List[float]) -> None: 
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee

        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.

        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> LinearInterpolator: 
        """
        create T_CLASS object from bytearray
        """
    def get_data_X(self) -> typing.List[float]: 
        """
        return the x component of the internal data vector

        Returns:
            std::vector<double>
        """
    def get_data_Y(self) -> typing.List[float]: 
        """
        return the y component of the internal data vector

        Returns:
            std::vector<YType>
        """
    def get_extrapolation_mode(self) -> t_extr_mode: 
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def insert(self, X: typing.List[float], Y: typing.List[float], bool: bool = False) -> None: 
        """
        append x and y value lists to the interpolator data (vectorized call)
        This call is much more expensive than extend as it requires copying
        data and sorting. Exception: raises domain error, strong exception
        guarantee

        Parameter ``X``:
            list of x values. (Does not have to be sorted. But must be unique)

        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X

        Parameter ``is_sorted``:
            this indicates that X is already sorted in ascending order.
            (default: false)
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_data_XY(self, X: typing.List[float], Y: typing.List[float]) -> None: 
        """
        change the input data to these X and Y vectors

        Parameter ``X:``:
            x vector (must be same size, must be sorted in ascending order)

        Parameter ``Y:``:
            y vector (must be same size)
        """
    def set_extrapolation_mode(self, extrapolation_mode: t_extr_mode) -> None: 
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
    pass
class NearestInterpolator():
    """
    Interpolator class to find nearest neighbors within vector data
    """
    @typing.overload
    def __call__(self, target_x: float) -> float: 
        """
        get the interpolated y value for given x target

        Parameter ``target_x``:
            find the corresponding y value for this x value

        Returns:
            corresponding y value

        get nearest y values for given x targets (vectorized call)

        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value

        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: typing.List[float]) -> typing.List[float]: ...
    def __copy__(self) -> NearestInterpolator: ...
    def __deepcopy__(self, arg0: dict) -> NearestInterpolator: ...
    def __eq__(self, other: NearestInterpolator) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self, X: typing.List[float] = [], Y: typing.List[float] = [], extrapolation_mode: t_extr_mode = t_extr_mode.extrapolate) -> None: 
        """
        Construct a new Interpolator object from a vector of pairs usage:
        interpolated_y_value = interpolator.interpolate(x_value)

        Parameter ``X``:
            X vector; must be unique and sorted in ascending order. same size
            as Y!

        Parameter ``Y``:
            Y vector; must be unique and sorted in ascending order. same size
            as X!

        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object that describes the extrapolation mode
        """
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def append(self, x: float, y: float) -> None: 
        """
        append an x- and the corresponding y value to the interpolator data.
        Exception: raises domain error, strong exception guarantee

        Parameter ``x``:
            value, must be > than all existing x values

        Parameter ``y``:
            corresponding y value
        """
    def copy(self) -> NearestInterpolator: 
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool: 
        """
        check if the interpolator contains data
        """
    def extend(self, X: typing.List[float], Y: typing.List[float]) -> None: 
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee

        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.

        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolator: 
        """
        create T_CLASS object from bytearray
        """
    def get_data_X(self) -> typing.List[float]: 
        """
        return the x component of the internal data vector

        Returns:
            std::vector<double>
        """
    def get_data_Y(self) -> typing.List[float]: 
        """
        return the y component of the internal data vector

        Returns:
            std::vector<YType>
        """
    def get_extrapolation_mode(self) -> t_extr_mode: 
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def insert(self, X: typing.List[float], Y: typing.List[float], bool: bool = False) -> None: 
        """
        append x and y value lists to the interpolator data (vectorized call)
        This call is much more expensive than extend as it requires copying
        data and sorting. Exception: raises domain error, strong exception
        guarantee

        Parameter ``X``:
            list of x values. (Does not have to be sorted. But must be unique)

        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X

        Parameter ``is_sorted``:
            this indicates that X is already sorted in ascending order.
            (default: false)
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_data_XY(self, X: typing.List[float], Y: typing.List[float]) -> None: 
        """
        change the input data to these X and Y vectors

        Parameter ``X:``:
            x vector (must be same size, must be sorted in ascending order)

        Parameter ``Y:``:
            y vector (must be same size)
        """
    def set_extrapolation_mode(self, extrapolation_mode: t_extr_mode) -> None: 
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
    pass
class SlerpInterpolator():
    """
    Class that implements a slerp interpolation for vectors. Data is
    internally represented in quaternions using lib eigen. Interfaces to
    represent the data in yaw, pitch, roll angles are provided. the
    __call__ equivalent to get interpolated yaw pitch roll is the ypr
    function
    """
    @typing.overload
    def __call__(self, target_x: float, output_in_degrees: bool = True) -> typing.Annotated[typing.List[float], pybind11_stubgen.typing_ext.FixedSize(3)]: 
        """
        get the interpolated yaw, pitch and roll values for given x target

        Parameter ``target_x``:
            find the corresponding y value for this x value

        Parameter ``output_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad

        Returns:
            corresponding y value

        get the interpolated yaw, pitch and roll values for given x target
        (vectorized call)

        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            yaw, pitch and roll value

        Parameter ``output_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad

        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: typing.List[float], output_in_degrees: bool = True) -> typing.List[typing.Annotated[typing.List[float], pybind11_stubgen.typing_ext.FixedSize(3)]]: ...
    def __copy__(self) -> SlerpInterpolator: ...
    def __deepcopy__(self, arg0: dict) -> SlerpInterpolator: ...
    def __eq__(self, other: SlerpInterpolator) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self, X: typing.List[float] = [], Yaw: typing.List[float] = [], Pitch: typing.List[float] = [], Roll: typing.List[float] = [], input_in_degrees: bool = True, extrapolation_mode: t_extr_mode = t_extr_mode.extrapolate) -> None: 
        """
        Construct a new Slerp Interpolator object using vectors of x, yaw,
        pitch and roll

        Parameter ``X``:
            vector; must be unique and sorted in ascending order

        Parameter ``yaw``:
            vector with yaw data (rotation around z axis). Must be same size
            as X!

        Parameter ``pitch``:
            vector with pitch data (rotation around y axis). Must be same size
            as X!

        Parameter ``roll``:
            vector with roll data (rotation around x axis). Must be same size
            as X!

        Parameter ``input_in_degrees``:
            if true (default) yaw,pitch and roll are in °, otherwise [rad]

        Parameter ``extrapolation_mode``:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object that describes the extrapolation mode
        """
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def append(self, x: float, yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> None: 
        """
        append an x, yaw, pitch, roll data point

        Parameter ``X``:
            must be larger than all internal data points

        Parameter ``yaw``:
            rotation around z axis

        Parameter ``pitch``:
            rotation around y axis

        Parameter ``roll``:
            rotation around x axis

        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad

        append an x, yaw, pitch, roll data point

        Parameter ``X``:
            must be larger than all internal data points

        Parameter ``ypr``:
            array with one yaw, pitch and roll data point

        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    @typing.overload
    def append(self, x: float, ypr: typing.Annotated[typing.List[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> None: ...
    def copy(self) -> SlerpInterpolator: 
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool: 
        """
        check if the interpolator contains data
        """
    @typing.overload
    def extend(self, X: typing.List[float], Yaw: typing.List[float], Pitch: typing.List[float], Roll: typing.List[float], input_in_degrees: bool = True) -> None: 
        """
        append data with lists of x, yaw, pitch, roll data (vectorized call)

        Parameter ``X``:
            vector; must be unique and sorted in ascending order

        Parameter ``yaw``:
            vector with yaw data (rotation around z axis). Must be same size
            as X!

        Parameter ``pitch``:
            vector with pitch data (rotation around y axis). Must be same size
            as X!

        Parameter ``roll``:
            vector with roll data (rotation around x axis). Must be same size
            as X!

        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad

        append data with list of x, yaw, pitch, roll data (vectorized call)

        Parameter ``X``:
            vector; must be unique and sorted in ascending order

        Parameter ``ypr``:
            vector with yaw, pitch and roll data points. Must be same size as
            X!

        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    @typing.overload
    def extend(self, X: typing.List[float], YPR: typing.List[typing.Annotated[typing.List[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> None: ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SlerpInterpolator: 
        """
        create T_CLASS object from bytearray
        """
    def get_data_X(self) -> typing.List[float]: 
        """
        return the x component of the internal data vector

        Returns:
            std::vector<double>
        """
    def get_data_YPR(self, output_in_degrees: bool = True) -> typing.List[typing.Annotated[typing.List[float], pybind11_stubgen.typing_ext.FixedSize(3)]]: 
        """
        return the internal yrp data vector

        Parameter ``output_in_degrees``:
            convert yaw, pitch and roll to degrees (default = True)

        Returns:
            std::vector<std::array<3, double>> YPR
        """
    def get_extrapolation_mode(self) -> t_extr_mode: 
        """
        Get the currently set extrapolation mode

        Returns:
            :py:class:`t_extr_mode
            <themachinethatgoesping.tools.vectorinterpolators.t_extr_mode>`
            object (enumerator) that describes the extrapolation mode
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def insert(self, X: typing.List[float], Yaw: typing.List[float], Pitch: typing.List[float], Roll: typing.List[float], input_in_degrees: bool = True, bool: bool = False) -> None: 
        """
        append data with lists of x, yaw, pitch, roll data (vectorized call)

        Parameter ``X``:
            vector; must be unique

        Parameter ``yaw``:
            vector with yaw data (rotation around z axis). Must be same size
            as X!

        Parameter ``pitch``:
            vector with pitch data (rotation around y axis). Must be same size
            as X!

        Parameter ``roll``:
            vector with roll data (rotation around x axis). Must be same size
            as X!

        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad

        append data with list of x, yaw, pitch, roll data (vectorized call)

        Parameter ``X``:
            vector; must be unique

        Parameter ``ypr``:
            vector with yaw, pitch and roll data points. Must be same size as
            X!

        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    @typing.overload
    def insert(self, X: typing.List[float], YPR: typing.List[typing.Annotated[typing.List[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True, bool: bool = False) -> None: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @typing.overload
    def set_data_XYPR(self, X: typing.List[float], Yaw: typing.List[float], Pitch: typing.List[float], Roll: typing.List[float], input_in_degrees: bool = True) -> None: 
        """
        change the input data to these X, yaw, pitch, roll vectors (will be
        converted to quaternion)

        Parameter ``X``:
            vector; must be unique and sorted in ascending order

        Parameter ``yaw``:
            vector with yaw data (rotation around z axis). Must be same size
            as X!

        Parameter ``pitch``:
            vector with pitch data (rotation around y axis). Must be same size
            as X!

        Parameter ``roll``:
            vector with roll data (rotation around x axis). Must be same size
            as X!

        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad

        change the input data to these X, yaw, pitch, roll vectors (will be
        converted to quaternion)

        Parameter ``X``:
            vector; must be unique and sorted in ascending order

        Parameter ``yaw``:
            vector with yaw data (rotation around z axis). Must be same size
            as X!

        Parameter ``pitch``:
            vector with pitch data (rotation around y axis). Must be same size
            as X!

        Parameter ``roll``:
            vector with roll data (rotation around x axis). Must be same size
            as X!

        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    @typing.overload
    def set_data_XYPR(self, X: typing.List[float], YPR: typing.List[typing.Annotated[typing.List[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> None: ...
    def set_extrapolation_mode(self, extrapolation_mode: t_extr_mode) -> None: 
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
    pass
class t_extr_mode():
    """
    extrapolation mode type.

    Members:

      extrapolate

      nearest

      fail
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    @typing.overload
    def __init__(self, value: int) -> None: 
        """
        Construct this enum type from string
        """
    @typing.overload
    def __init__(self, str: str) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    def str(self) -> str: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'extrapolate': <t_extr_mode.extrapolate: 0>, 'nearest': <t_extr_mode.nearest: 2>, 'fail': <t_extr_mode.fail: 1>}
    extrapolate: themachinethatgoesping.tools.vectorinterpolators.t_extr_mode # value = <t_extr_mode.extrapolate: 0>
    fail: themachinethatgoesping.tools.vectorinterpolators.t_extr_mode # value = <t_extr_mode.fail: 1>
    nearest: themachinethatgoesping.tools.vectorinterpolators.t_extr_mode # value = <t_extr_mode.nearest: 2>
    pass
extrapolate: themachinethatgoesping.tools.vectorinterpolators.t_extr_mode # value = <t_extr_mode.extrapolate: 0>
fail: themachinethatgoesping.tools.vectorinterpolators.t_extr_mode # value = <t_extr_mode.fail: 1>
nearest: themachinethatgoesping.tools.vectorinterpolators.t_extr_mode # value = <t_extr_mode.nearest: 2>
