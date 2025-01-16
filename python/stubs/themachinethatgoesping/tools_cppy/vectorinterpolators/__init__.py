"""
Classes for getting interpolated values from within vectors
"""
from __future__ import annotations
import pybind11_stubgen.typing_ext
import typing
from . import bivectorinterpolators
__all__ = ['AkimaInterpolator', 'AkimaInterpolatorF', 'LinearInterpolator', 'LinearInterpolatorDF', 'LinearInterpolatorF', 'LinearInterpolatorFD', 'NearestInterpolator', 'NearestInterpolatorDF', 'NearestInterpolatorDI', 'NearestInterpolatorDO', 'NearestInterpolatorF', 'NearestInterpolatorFD', 'NearestInterpolatorFI', 'NearestInterpolatorFO', 'SlerpInterpolator', 'SlerpInterpolatorDF', 'SlerpInterpolatorF', 'SlerpInterpolatorFD', 'bivectorinterpolators', 'extrapolate', 'fail', 'nearest', 't_extr_mode']
class AkimaInterpolator:
    """
    Interpolator class to perform a (modified) akima interpolation. Uses
    boost makima interpolator. Note: this interpolator acts as linear
    interpolator if less than 4 values are stored.
    
    Template parameter ``XYType:``:
        type of the x and y values (must be floating point))
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> AkimaInterpolator:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[float]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> AkimaInterpolator:
        ...
    def __deepcopy__(self, arg0: dict) -> AkimaInterpolator:
        ...
    def __eq__(self, other: AkimaInterpolator) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[float] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
    def extend(self, X: list[float], Y: list[float]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[float]:
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
    def get_y(self, target_x: float) -> float:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[float], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[float]) -> None:
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
class AkimaInterpolatorF:
    """
    Interpolator class to perform a (modified) akima interpolation. Uses
    boost makima interpolator. Note: this interpolator acts as linear
    interpolator if less than 4 values are stored.
    
    Template parameter ``XYType:``:
        type of the x and y values (must be floating point))
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> AkimaInterpolatorF:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[float]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> AkimaInterpolatorF:
        ...
    def __deepcopy__(self, arg0: dict) -> AkimaInterpolatorF:
        ...
    def __eq__(self, other: AkimaInterpolatorF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[float] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
    def copy(self) -> AkimaInterpolatorF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    def extend(self, X: list[float], Y: list[float]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[float]:
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
    def get_y(self, target_x: float) -> float:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[float], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[float]) -> None:
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
class LinearInterpolator:
    """
    Find linear interpolated values within vector data
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        type of the y values (must be floating point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> LinearInterpolator:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[float]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> LinearInterpolator:
        ...
    def __deepcopy__(self, arg0: dict) -> LinearInterpolator:
        ...
    def __eq__(self, other: LinearInterpolator) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[float] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
    def extend(self, X: list[float], Y: list[float]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[float]:
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
    def get_y(self, target_x: float) -> float:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[float], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[float]) -> None:
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
class LinearInterpolatorDF:
    """
    Find linear interpolated values within vector data
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        type of the y values (must be floating point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> LinearInterpolatorDF:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[float]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> LinearInterpolatorDF:
        ...
    def __deepcopy__(self, arg0: dict) -> LinearInterpolatorDF:
        ...
    def __eq__(self, other: LinearInterpolatorDF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[float] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
    def copy(self) -> LinearInterpolatorDF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    def extend(self, X: list[float], Y: list[float]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[float]:
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
    def get_y(self, target_x: float) -> float:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[float], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[float]) -> None:
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
class LinearInterpolatorF:
    """
    Find linear interpolated values within vector data
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        type of the y values (must be floating point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> LinearInterpolatorF:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[float]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> LinearInterpolatorF:
        ...
    def __deepcopy__(self, arg0: dict) -> LinearInterpolatorF:
        ...
    def __eq__(self, other: LinearInterpolatorF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[float] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
    def copy(self) -> LinearInterpolatorF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    def extend(self, X: list[float], Y: list[float]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[float]:
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
    def get_y(self, target_x: float) -> float:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[float], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[float]) -> None:
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
class LinearInterpolatorFD:
    """
    Find linear interpolated values within vector data
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        type of the y values (must be floating point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> LinearInterpolatorFD:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[float]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> LinearInterpolatorFD:
        ...
    def __deepcopy__(self, arg0: dict) -> LinearInterpolatorFD:
        ...
    def __eq__(self, other: LinearInterpolatorFD) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[float] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
    def copy(self) -> LinearInterpolatorFD:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    def extend(self, X: list[float], Y: list[float]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[float]:
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
    def get_y(self, target_x: float) -> float:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[float], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[float]) -> None:
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
class NearestInterpolator:
    """
    Interpolator class to find nearest neighbors within vector data
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        type of the y values (must be floating point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolator:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[float]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> NearestInterpolator:
        ...
    def __deepcopy__(self, arg0: dict) -> NearestInterpolator:
        ...
    def __eq__(self, other: NearestInterpolator) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[float] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
    def extend(self, X: list[float], Y: list[float]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[float]:
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
    def get_y(self, target_x: float) -> float:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[float], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[float]) -> None:
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
class NearestInterpolatorDF:
    """
    Interpolator class to find nearest neighbors within vector data
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        type of the y values (must be floating point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorDF:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[float]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> NearestInterpolatorDF:
        ...
    def __deepcopy__(self, arg0: dict) -> NearestInterpolatorDF:
        ...
    def __eq__(self, other: NearestInterpolatorDF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[float] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
    def copy(self) -> NearestInterpolatorDF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    def extend(self, X: list[float], Y: list[float]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[float]:
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
    def get_y(self, target_x: float) -> float:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[float], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[float]) -> None:
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
class NearestInterpolatorDI:
    """
    Interpolator class to find nearest neighbors within vector data
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        type of the y values (must be floating point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorDI:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> int:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[int]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> NearestInterpolatorDI:
        ...
    def __deepcopy__(self, arg0: dict) -> NearestInterpolatorDI:
        ...
    def __eq__(self, other: NearestInterpolatorDI) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[int] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append(self, x: float, y: int) -> None:
        """
        append an x- and the corresponding y value to the interpolator data.
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``x``:
            value, must be > than all existing x values
        
        Parameter ``y``:
            corresponding y value
        """
    def copy(self) -> NearestInterpolatorDI:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    def extend(self, X: list[float], Y: list[int]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[int]:
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
    def get_y(self, target_x: float) -> int:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[int], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[int]) -> None:
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
class NearestInterpolatorDO:
    """
    Interpolator class to find nearest neighbors within vector data
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        type of the y values (must be floating point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorDO:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> typing.Any:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[typing.Any]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> NearestInterpolatorDO:
        ...
    def __deepcopy__(self, arg0: dict) -> NearestInterpolatorDO:
        ...
    def __eq__(self, other: NearestInterpolatorDO) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[typing.Any] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append(self, x: float, y: typing.Any) -> None:
        """
        append an x- and the corresponding y value to the interpolator data.
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``x``:
            value, must be > than all existing x values
        
        Parameter ``y``:
            corresponding y value
        """
    def copy(self) -> NearestInterpolatorDO:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    def extend(self, X: list[float], Y: list[typing.Any]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[typing.Any]:
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
    def get_y(self, target_x: float) -> typing.Any:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[typing.Any], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[typing.Any]) -> None:
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
class NearestInterpolatorF:
    """
    Interpolator class to find nearest neighbors within vector data
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        type of the y values (must be floating point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorF:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[float]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> NearestInterpolatorF:
        ...
    def __deepcopy__(self, arg0: dict) -> NearestInterpolatorF:
        ...
    def __eq__(self, other: NearestInterpolatorF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[float] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
    def copy(self) -> NearestInterpolatorF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    def extend(self, X: list[float], Y: list[float]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[float]:
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
    def get_y(self, target_x: float) -> float:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[float], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[float]) -> None:
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
class NearestInterpolatorFD:
    """
    Interpolator class to find nearest neighbors within vector data
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        type of the y values (must be floating point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorFD:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> float:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[float]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> NearestInterpolatorFD:
        ...
    def __deepcopy__(self, arg0: dict) -> NearestInterpolatorFD:
        ...
    def __eq__(self, other: NearestInterpolatorFD) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[float] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
    def copy(self) -> NearestInterpolatorFD:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    def extend(self, X: list[float], Y: list[float]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[float]:
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
    def get_y(self, target_x: float) -> float:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[float], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[float]) -> None:
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
class NearestInterpolatorFI:
    """
    Interpolator class to find nearest neighbors within vector data
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        type of the y values (must be floating point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorFI:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> int:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[int]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> NearestInterpolatorFI:
        ...
    def __deepcopy__(self, arg0: dict) -> NearestInterpolatorFI:
        ...
    def __eq__(self, other: NearestInterpolatorFI) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[int] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append(self, x: float, y: int) -> None:
        """
        append an x- and the corresponding y value to the interpolator data.
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``x``:
            value, must be > than all existing x values
        
        Parameter ``y``:
            corresponding y value
        """
    def copy(self) -> NearestInterpolatorFI:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    def extend(self, X: list[float], Y: list[int]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[int]:
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
    def get_y(self, target_x: float) -> int:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[int], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[int]) -> None:
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
class NearestInterpolatorFO:
    """
    Interpolator class to find nearest neighbors within vector data
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        type of the y values (must be floating point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestInterpolatorFO:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float) -> typing.Any:
        """
        get the interpolated y value for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float]) -> list[typing.Any]:
        """
        get nearest y values for given x targets (vectorized call)
        
        Parameter ``targets_x``:
            vector of x values. For each of these values find the corrsponding
            y value
        
        Returns:
            corresponding y value
        """
    def __copy__(self) -> NearestInterpolatorFO:
        ...
    def __deepcopy__(self, arg0: dict) -> NearestInterpolatorFO:
        ...
    def __eq__(self, other: NearestInterpolatorFO) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Y: list[typing.Any] = [], extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def append(self, x: float, y: typing.Any) -> None:
        """
        append an x- and the corresponding y value to the interpolator data.
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``x``:
            value, must be > than all existing x values
        
        Parameter ``y``:
            corresponding y value
        """
    def copy(self) -> NearestInterpolatorFO:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    def extend(self, X: list[float], Y: list[typing.Any]) -> None:
        """
        append x and y value lists to the interpolator data (vectorized call)
        Exception: raises domain error, strong exception guarantee
        
        Parameter ``X``:
            list of x values. Must be sorted in ascending order. All x values
            must be larger than the largest x value in the interpolator data.
        
        Parameter ``Y``:
            list of corresponding Y values. Must be same size as X
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_Y(self) -> list[typing.Any]:
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
    def get_y(self, target_x: float) -> typing.Any:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def insert(self, X: list[float], Y: list[typing.Any], bool: bool = False) -> None:
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_XY(self, X: list[float], Y: list[typing.Any]) -> None:
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
class SlerpInterpolator:
    """
    Class that implements a slerp interpolation for vectors. Data is
    internally represented in quaternions using lib eigen. Interfaces to
    represent the data in yaw, pitch, roll angles are provided. the
    __call__ equivalent to get interpolated yaw pitch roll is the ypr
    function
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        floating point type of the y quaternion values (must be floating
        point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SlerpInterpolator:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float, output_in_degrees: bool = True) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Parameter ``output_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float], output_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
        """
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
    def __copy__(self) -> SlerpInterpolator:
        ...
    def __deepcopy__(self, arg0: dict) -> SlerpInterpolator:
        ...
    def __eq__(self, other: SlerpInterpolator) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Yaw: list[float] = [], Pitch: list[float] = [], Roll: list[float] = [], input_in_degrees: bool = True, extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
        """
    @typing.overload
    def append(self, x: float, ypr: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> None:
        """
        append an x, yaw, pitch, roll data point
        
        Parameter ``X``:
            must be larger than all internal data points
        
        Parameter ``ypr``:
            array with one yaw, pitch and roll data point
        
        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    def copy(self) -> SlerpInterpolator:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    @typing.overload
    def extend(self, X: list[float], Yaw: list[float], Pitch: list[float], Roll: list[float], input_in_degrees: bool = True) -> None:
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
        """
    @typing.overload
    def extend(self, X: list[float], YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)
        
        Parameter ``X``:
            vector; must be unique and sorted in ascending order
        
        Parameter ``ypr``:
            vector with yaw, pitch and roll data points. Must be same size as
            X!
        
        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_YPR(self, output_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
        """
        return the internal yrp data vector
        
        Parameter ``output_in_degrees``:
            convert yaw, pitch and roll to degrees (default = True)
        
        Returns:
            std::vector<std::array<3, YType>> YPR
        """
    def get_extrapolation_mode(self) -> t_extr_mode:
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
    @typing.overload
    def insert(self, X: list[float], Yaw: list[float], Pitch: list[float], Roll: list[float], input_in_degrees: bool = True, bool: bool = False) -> None:
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
        """
    @typing.overload
    def insert(self, X: list[float], YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True, bool: bool = False) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)
        
        Parameter ``X``:
            vector; must be unique
        
        Parameter ``ypr``:
            vector with yaw, pitch and roll data points. Must be same size as
            X!
        
        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @typing.overload
    def set_data_XYPR(self, X: list[float], Yaw: list[float], Pitch: list[float], Roll: list[float], input_in_degrees: bool = True) -> None:
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
        """
    @typing.overload
    def set_data_XYPR(self, X: list[float], YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> None:
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
    @typing.overload
    def ypr(self, target_x: float, output_in_degrees: bool = True) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Parameter ``output_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def ypr(self, targets_x: list[float], output_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
        """
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
class SlerpInterpolatorDF:
    """
    Class that implements a slerp interpolation for vectors. Data is
    internally represented in quaternions using lib eigen. Interfaces to
    represent the data in yaw, pitch, roll angles are provided. the
    __call__ equivalent to get interpolated yaw pitch roll is the ypr
    function
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        floating point type of the y quaternion values (must be floating
        point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SlerpInterpolatorDF:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float, output_in_degrees: bool = True) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Parameter ``output_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float], output_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
        """
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
    def __copy__(self) -> SlerpInterpolatorDF:
        ...
    def __deepcopy__(self, arg0: dict) -> SlerpInterpolatorDF:
        ...
    def __eq__(self, other: SlerpInterpolatorDF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Yaw: list[float] = [], Pitch: list[float] = [], Roll: list[float] = [], input_in_degrees: bool = True, extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
        """
    @typing.overload
    def append(self, x: float, ypr: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> None:
        """
        append an x, yaw, pitch, roll data point
        
        Parameter ``X``:
            must be larger than all internal data points
        
        Parameter ``ypr``:
            array with one yaw, pitch and roll data point
        
        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    def copy(self) -> SlerpInterpolatorDF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    @typing.overload
    def extend(self, X: list[float], Yaw: list[float], Pitch: list[float], Roll: list[float], input_in_degrees: bool = True) -> None:
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
        """
    @typing.overload
    def extend(self, X: list[float], YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)
        
        Parameter ``X``:
            vector; must be unique and sorted in ascending order
        
        Parameter ``ypr``:
            vector with yaw, pitch and roll data points. Must be same size as
            X!
        
        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_YPR(self, output_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
        """
        return the internal yrp data vector
        
        Parameter ``output_in_degrees``:
            convert yaw, pitch and roll to degrees (default = True)
        
        Returns:
            std::vector<std::array<3, YType>> YPR
        """
    def get_extrapolation_mode(self) -> t_extr_mode:
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
    @typing.overload
    def insert(self, X: list[float], Yaw: list[float], Pitch: list[float], Roll: list[float], input_in_degrees: bool = True, bool: bool = False) -> None:
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
        """
    @typing.overload
    def insert(self, X: list[float], YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True, bool: bool = False) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)
        
        Parameter ``X``:
            vector; must be unique
        
        Parameter ``ypr``:
            vector with yaw, pitch and roll data points. Must be same size as
            X!
        
        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @typing.overload
    def set_data_XYPR(self, X: list[float], Yaw: list[float], Pitch: list[float], Roll: list[float], input_in_degrees: bool = True) -> None:
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
        """
    @typing.overload
    def set_data_XYPR(self, X: list[float], YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> None:
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
    @typing.overload
    def ypr(self, target_x: float, output_in_degrees: bool = True) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Parameter ``output_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def ypr(self, targets_x: list[float], output_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
        """
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
class SlerpInterpolatorF:
    """
    Class that implements a slerp interpolation for vectors. Data is
    internally represented in quaternions using lib eigen. Interfaces to
    represent the data in yaw, pitch, roll angles are provided. the
    __call__ equivalent to get interpolated yaw pitch roll is the ypr
    function
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        floating point type of the y quaternion values (must be floating
        point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SlerpInterpolatorF:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float, output_in_degrees: bool = True) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Parameter ``output_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float], output_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
        """
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
    def __copy__(self) -> SlerpInterpolatorF:
        ...
    def __deepcopy__(self, arg0: dict) -> SlerpInterpolatorF:
        ...
    def __eq__(self, other: SlerpInterpolatorF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Yaw: list[float] = [], Pitch: list[float] = [], Roll: list[float] = [], input_in_degrees: bool = True, extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
        """
    @typing.overload
    def append(self, x: float, ypr: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> None:
        """
        append an x, yaw, pitch, roll data point
        
        Parameter ``X``:
            must be larger than all internal data points
        
        Parameter ``ypr``:
            array with one yaw, pitch and roll data point
        
        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    def copy(self) -> SlerpInterpolatorF:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    @typing.overload
    def extend(self, X: list[float], Yaw: list[float], Pitch: list[float], Roll: list[float], input_in_degrees: bool = True) -> None:
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
        """
    @typing.overload
    def extend(self, X: list[float], YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)
        
        Parameter ``X``:
            vector; must be unique and sorted in ascending order
        
        Parameter ``ypr``:
            vector with yaw, pitch and roll data points. Must be same size as
            X!
        
        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_YPR(self, output_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
        """
        return the internal yrp data vector
        
        Parameter ``output_in_degrees``:
            convert yaw, pitch and roll to degrees (default = True)
        
        Returns:
            std::vector<std::array<3, YType>> YPR
        """
    def get_extrapolation_mode(self) -> t_extr_mode:
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
    @typing.overload
    def insert(self, X: list[float], Yaw: list[float], Pitch: list[float], Roll: list[float], input_in_degrees: bool = True, bool: bool = False) -> None:
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
        """
    @typing.overload
    def insert(self, X: list[float], YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True, bool: bool = False) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)
        
        Parameter ``X``:
            vector; must be unique
        
        Parameter ``ypr``:
            vector with yaw, pitch and roll data points. Must be same size as
            X!
        
        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @typing.overload
    def set_data_XYPR(self, X: list[float], Yaw: list[float], Pitch: list[float], Roll: list[float], input_in_degrees: bool = True) -> None:
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
        """
    @typing.overload
    def set_data_XYPR(self, X: list[float], YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> None:
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
    @typing.overload
    def ypr(self, target_x: float, output_in_degrees: bool = True) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Parameter ``output_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def ypr(self, targets_x: list[float], output_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
        """
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
class SlerpInterpolatorFD:
    """
    Class that implements a slerp interpolation for vectors. Data is
    internally represented in quaternions using lib eigen. Interfaces to
    represent the data in yaw, pitch, roll angles are provided. the
    __call__ equivalent to get interpolated yaw pitch roll is the ypr
    function
    
    Template parameter ``XType:``:
        type of the x values (must be floating point)
    
    Template parameter ``YType:``:
        floating point type of the y quaternion values (must be floating
        point)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SlerpInterpolatorFD:
        """
        create T_CLASS object from bytearray
        """
    @typing.overload
    def __call__(self, target_x: float, output_in_degrees: bool = True) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Parameter ``output_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def __call__(self, targets_x: list[float], output_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
        """
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
    def __copy__(self) -> SlerpInterpolatorFD:
        ...
    def __deepcopy__(self, arg0: dict) -> SlerpInterpolatorFD:
        ...
    def __eq__(self, other: SlerpInterpolatorFD) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, X: list[float] = [], Yaw: list[float] = [], Pitch: list[float] = [], Roll: list[float] = [], input_in_degrees: bool = True, extrapolation_mode: t_extr_mode = ...) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
        """
    @typing.overload
    def append(self, x: float, ypr: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> None:
        """
        append an x, yaw, pitch, roll data point
        
        Parameter ``X``:
            must be larger than all internal data points
        
        Parameter ``ypr``:
            array with one yaw, pitch and roll data point
        
        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    def copy(self) -> SlerpInterpolatorFD:
        """
        return a copy using the c++ default copy constructor
        """
    def empty(self) -> bool:
        """
        check if the interpolator contains data
        """
    @typing.overload
    def extend(self, X: list[float], Yaw: list[float], Pitch: list[float], Roll: list[float], input_in_degrees: bool = True) -> None:
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
        """
    @typing.overload
    def extend(self, X: list[float], YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)
        
        Parameter ``X``:
            vector; must be unique and sorted in ascending order
        
        Parameter ``ypr``:
            vector with yaw, pitch and roll data points. Must be same size as
            X!
        
        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    def get_data_X(self) -> list[float]:
        """
        return the x component of the internal data vector
        
        Returns:
            std::vector<XType>
        """
    def get_data_YPR(self, output_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
        """
        return the internal yrp data vector
        
        Parameter ``output_in_degrees``:
            convert yaw, pitch and roll to degrees (default = True)
        
        Returns:
            std::vector<std::array<3, YType>> YPR
        """
    def get_extrapolation_mode(self) -> t_extr_mode:
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
    @typing.overload
    def insert(self, X: list[float], Yaw: list[float], Pitch: list[float], Roll: list[float], input_in_degrees: bool = True, bool: bool = False) -> None:
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
        """
    @typing.overload
    def insert(self, X: list[float], YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True, bool: bool = False) -> None:
        """
        append data with list of x, yaw, pitch, roll data (vectorized call)
        
        Parameter ``X``:
            vector; must be unique
        
        Parameter ``ypr``:
            vector with yaw, pitch and roll data points. Must be same size as
            X!
        
        Parameter ``input_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @typing.overload
    def set_data_XYPR(self, X: list[float], Yaw: list[float], Pitch: list[float], Roll: list[float], input_in_degrees: bool = True) -> None:
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
        """
    @typing.overload
    def set_data_XYPR(self, X: list[float], YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> None:
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
    @typing.overload
    def ypr(self, target_x: float, output_in_degrees: bool = True) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        get the interpolated yaw, pitch and roll values for given x target
        
        Parameter ``target_x``:
            find the corresponding y value for this x value
        
        Parameter ``output_in_degrees``:
            if true, yaw pitch and roll input values are in ° otherwise rad
        
        Returns:
            corresponding y value
        """
    @typing.overload
    def ypr(self, targets_x: list[float], output_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
        """
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
class t_extr_mode:
    """
    extrapolation mode type.
    
    Members:
    
      extrapolate
    
      nearest
    
      fail
    """
    __members__: typing.ClassVar[dict[str, t_extr_mode]]  # value = {'extrapolate': <t_extr_mode.extrapolate: 0>, 'nearest': <t_extr_mode.nearest: 2>, 'fail': <t_extr_mode.fail: 1>}
    extrapolate: typing.ClassVar[t_extr_mode]  # value = <t_extr_mode.extrapolate: 0>
    fail: typing.ClassVar[t_extr_mode]  # value = <t_extr_mode.fail: 1>
    nearest: typing.ClassVar[t_extr_mode]  # value = <t_extr_mode.nearest: 2>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    @typing.overload
    def __init__(self, value: int) -> None:
        ...
    @typing.overload
    def __init__(self, str: str) -> None:
        """
        Construct this enum type from string
        """
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def str(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
extrapolate: t_extr_mode  # value = <t_extr_mode.extrapolate: 0>
fail: t_extr_mode  # value = <t_extr_mode.fail: 1>
nearest: t_extr_mode  # value = <t_extr_mode.nearest: 2>
