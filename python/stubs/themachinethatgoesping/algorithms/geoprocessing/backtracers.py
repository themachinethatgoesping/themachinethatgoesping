"""
Submodule for backtracing echo sounder sample locations to beamangle and twoway traveltime
"""
from __future__ import annotations
import numpy
import pybind11_stubgen.typing_ext
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import themachinethatgoesping.tools_cppy.vectorinterpolators
import typing
__all__ = ['BTConstantSVP', 'BacktracedWCI', 'I_Backtracer']
class BTConstantSVP(I_Backtracer):
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BTConstantSVP:
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
        hash function implemented using binary_hash
        """
    def __init__(self, sensor_location: ..., sensor_x: float, sensor_y: float) -> None:
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
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
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
class BacktracedWCI:
    """
    A structure to store a watercolumn image together with the necessary
    informations for raytracing.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BacktracedWCI:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> BacktracedWCI:
        ...
    def __deepcopy__(self, arg0: dict) -> BacktracedWCI:
        ...
    def __eq__(self, other: BacktracedWCI) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, wci: numpy.ndarray[numpy.float32], beam_reference_directions: themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_1, beam_reference_sample_numbers: list[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
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
    def copy(self) -> BacktracedWCI:
        """
        return a copy using the c++ default copy constructor
        """
    def get_angle_beamnumber_interpolator(self) -> ...:
        ...
    def get_max_angle(self) -> float:
        ...
    def get_min_angle(self) -> float:
        ...
    def get_range_samplenumber_interpolators(self) -> list[themachinethatgoesping.tools_cppy.vectorinterpolators.LinearInterpolatorF]:
        ...
    def get_wci(self) -> numpy.ndarray[numpy.float32]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def lookup(self, beam_angle: float, range: float) -> float:
        ...
    def lookup_const(self, beam_angle: float, range: float) -> float:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class I_Backtracer:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> I_Backtracer:
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
        hash function implemented using binary_hash
        """
    def __init__(self, sensor_location: ..., sensor_x: float, sensor_y: float, backtracer_name: str) -> None:
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
    def backtrace_image(self, y_coordinates: numpy.ndarray[numpy.float32], z_coordinates: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_2:
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
            datastructures::SampleDirectionsRange<2>, shape is
            (y_coordinates.size(), z_coordinates.size())
        """
    @typing.overload
    def backtrace_points(self, x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_1:
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
            datastructures::SampleDirectionsRange
        """
    @typing.overload
    def backtrace_points(self, xyz: themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1, mp_cores: int = 1) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_1:
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
            datastructures::SampleDirectionsRange
        """
    def copy(self) -> I_Backtracer:
        """
        return a copy using the c++ default copy constructor
        """
    def get_sensor_location(self) -> ...:
        ...
    def get_sensor_orientation_quat_ypr(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        ...
    def get_sensor_x(self) -> float:
        ...
    def get_sensor_y(self) -> float:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def lookup(self, wci: numpy.ndarray[numpy.float32], beam_reference_directions: themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_1, beam_reference_sample_numbers: list[int], target_directions: themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_2, mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
        ...
    def lookup_indices(self, beam_reference_directions: themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_1, beam_reference_sample_numbers: list[int], beam_reference_max_sample_numbers: list[int], target_directions: themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_2, mp_cores: int = 1) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleIndices_2:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def set_sensor_location(self, sensor_location: ..., sensor_x: float, sensor_y: float) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
