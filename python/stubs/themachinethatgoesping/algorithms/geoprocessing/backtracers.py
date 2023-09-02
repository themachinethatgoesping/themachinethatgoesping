"""
Submodule for backtracing echo sounder sample locations to beamangle and twoway traveltime
"""
from __future__ import annotations
import numpy
import pybind11_stubgen.typing_ext
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import typing
__all__ = ['BTConstantSVP', 'I_Backtracer']
class BTConstantSVP(I_Backtracer):
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> BTConstantSVP:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> BTConstantSVP:
        ...
    def __deepcopy__(self, arg0: dict) -> BTConstantSVP:
        ...
    def __eq__(self, other: BTConstantSVP) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self, sensor_location: ..., sound_velocity: float) -> None:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> BTConstantSVP:
        """
        return a copy using the c++ default copy constructor
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class I_Backtracer:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> I_Backtracer:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> I_Backtracer:
        ...
    def __deepcopy__(self, arg0: dict) -> I_Backtracer:
        ...
    def __eq__(self, other: I_Backtracer) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self, sensor_location: ..., backtracer_name: str) -> None:
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
    def backtrace_image(self, y_coordinates: numpy.ndarray[numpy.float32], z_coordinates: numpy.ndarray[numpy.float32], mp_cores: int = ...) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirections_2:
        """
        Backtrace the location of an image specified by two coordinate vectors
        x is assumed to be 0
        
        Parameter ``y_coordinates``:
            in m, positive starboard
        
        Parameter ``z_coordinates``:
            in m, positive downwards
        
        Parameter ``mp_cores``:
            Number of cores to use for parallelization
        
        Returns:
            datastructures::SampleDirections<2>, shape is
            (y_coordinates.size(), z_coordinates.size())
        """
    @typing.overload
    def backtrace_points(self, x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32], mp_cores: int = ...) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirections_1:
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
    @typing.overload
    def backtrace_points(self, xyz: themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1, mp_cores: int = ...) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirections_1:
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
    def get_sensor_location(self) -> ...:
        ...
    def get_sensor_orientation_quat_ypr(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_sensor_location(self, sensor_location: ...) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
