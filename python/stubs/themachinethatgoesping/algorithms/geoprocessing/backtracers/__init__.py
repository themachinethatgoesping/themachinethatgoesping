"""Submodule for backtracing echo sounder sample locations to beamangle and twoway traveltime"""
from __future__ import annotations
import themachinethatgoesping.algorithms.geoprocessing.backtracers
import typing
import numpy
import pybind11_stubgen.typing_ext
import themachinethatgoesping.algorithms.geoprocessing.datastructures
_Shape = typing.Tuple[int, ...]

__all__ = [
    "BTConstantSVP",
    "I_Backtracer"
]


class I_Backtracer():
    def __copy__(self) -> I_Backtracer: ...
    def __deepcopy__(self, arg0: dict) -> I_Backtracer: ...
    def __eq__(self, other: I_Backtracer) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @staticmethod
    def __init__(*args, **kwargs) -> typing.Any: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def backtrace_image(self, y_coordinates: numpy.ndarray[numpy.float32], z_coordinates: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirections_2: 
        """
        Backtrace the location of a set of points.

        Parameter ``x``:
            in m, positive forward

        Parameter ``y``:
            in m, positive starboard

        Parameter ``z``:
            in m, positive downwards

        Parameter ``mp_cores``:
            Number of cores to use for parallelization

        Returns:
            datastructures::SampleDirections
        """
    def backtrace_points(self, x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirections_1: 
        """
        Backtrace the location of a set of points.

        Parameter ``x``:
            in m, positive forward

        Parameter ``y``:
            in m, positive starboard

        Parameter ``z``:
            in m, positive downwards

        Parameter ``mp_cores``:
            Number of cores to use for parallelization

        Returns:
            datastructures::SampleDirections
        """
    def copy(self) -> I_Backtracer: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> I_Backtracer: 
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def get_sensor_location(*args, **kwargs) -> typing.Any: ...
    def get_sensor_orientation_quat_ypr(self) -> typing.Annotated[typing.List[float], pybind11_stubgen.typing_ext.FixedSize(3)]: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @staticmethod
    def set_sensor_location(*args, **kwargs) -> typing.Any: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
class BTConstantSVP(I_Backtracer):
    def __copy__(self) -> BTConstantSVP: ...
    def __deepcopy__(self, arg0: dict) -> BTConstantSVP: ...
    def __eq__(self, other: BTConstantSVP) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @staticmethod
    def __init__(*args, **kwargs) -> typing.Any: 
        """
        Construct a new BTConstantSVP object

        Parameter ``sensor_location``:
            Orientation and depth of the echo sounder

        Parameter ``sound_velocity``:
            Sound velocity in m/s
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
    def copy(self) -> BTConstantSVP: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BTConstantSVP: 
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
    pass
