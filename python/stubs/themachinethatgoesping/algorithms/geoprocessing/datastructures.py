"""
Submodule that holds datastructures that hold the raytracers/georeferncing results
"""
from __future__ import annotations
import numpy
import pybind11_stubgen.typing_ext
import typing
__all__ = ['BeamSampleParameters', 'RaytraceResult', 'RaytraceResults_1', 'RaytraceResults_2', 'RaytraceResults_3', 'SampleDirections_1', 'SampleDirections_2', 'SampleDirections_3', 'SampleIndices', 'XYZ_1', 'XYZ_2', 'XYZ_3']
class BeamSampleParameters:
    """
    A structure to store directional parameters of multibeam system.
    Usefull as input for raytracing water column images.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> BeamSampleParameters:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> BeamSampleParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> BeamSampleParameters:
        ...
    def __eq__(self, other: BeamSampleParameters) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self, number_of_beams: int) -> None:
        """
        Construct a new BeamSampleParameters object (all values uninitialized)
        
        Parameter ``number_of_beams``:
            number of beams
        """
    @typing.overload
    def __init__(self, alongtrack_angles: numpy.ndarray[numpy.float32], crosstrack_angles: numpy.ndarray[numpy.float32], first_sample_offset: numpy.ndarray[numpy.float32], sample_interval: numpy.ndarray[numpy.float32], number_of_samples: numpy.ndarray[numpy.uint32]) -> None:
        """
        Construct a new BeamSampleParameters object (all values uninitialized)
        
        Parameter ``number_of_beams``:
            number of beams
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
    def copy(self) -> BeamSampleParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def get_alongtrack_angles(self) -> numpy.ndarray[numpy.float32]:
        ...
    def get_crosstrack_angles(self) -> numpy.ndarray[numpy.float32]:
        ...
    def get_first_sample_offset(self) -> numpy.ndarray[numpy.float32]:
        ...
    def get_number_of_samples(self) -> numpy.ndarray[numpy.uint32]:
        ...
    def get_sample_interval(self) -> numpy.ndarray[numpy.float32]:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_alongtrack_angles(self, alongtrack_angles: numpy.ndarray[numpy.float32]) -> None:
        ...
    def set_crosstrack_angles(self, crosstrack_angles: numpy.ndarray[numpy.float32]) -> None:
        ...
    def set_first_sample_offset(self, first_sample_offset: numpy.ndarray[numpy.float32]) -> None:
        ...
    def set_number_of_samples(self, number_of_samples: numpy.ndarray[numpy.uint32]) -> None:
        ...
    def set_sample_interval(self, sample_interval: numpy.ndarray[numpy.float32]) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class RaytraceResult:
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> RaytraceResult:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> RaytraceResult:
        ...
    def __deepcopy__(self, arg0: dict) -> RaytraceResult:
        ...
    def __eq__(self, other: RaytraceResult) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new sample location object (all values set to 0)
        """
    @typing.overload
    def __init__(self, x: float, y: float, z: float, true_range: float) -> None:
        """
        Construct a new RaytraceResult object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
        
        Parameter ``true_range``:
            in m, accumulated ray path length
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
    def copy(self) -> RaytraceResult:
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
    @property
    def true_range(self) -> float:
        """
        < in m, accumulated ray path length
        """
    @true_range.setter
    def true_range(self, arg0: float) -> None:
        ...
    @property
    def x(self) -> float:
        """
        < in m, positive forward
        """
    @x.setter
    def x(self, arg0: float) -> None:
        ...
    @property
    def y(self) -> float:
        """
        < in m, positive starboard
        """
    @y.setter
    def y(self, arg0: float) -> None:
        ...
    @property
    def z(self) -> float:
        """
        < in m, positive downwards
        """
    @z.setter
    def z(self, arg0: float) -> None:
        ...
class RaytraceResults_1(XYZ_1):
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> RaytraceResults_1:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> RaytraceResults_1:
        ...
    def __deepcopy__(self, arg0: dict) -> RaytraceResults_1:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new sample location object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(1)]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32], true_range: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new RaytraceResults object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
        
        Parameter ``true_range``:
            in m, accumulated ray path length
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
    def copy(self) -> RaytraceResults_1:
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
    @property
    def true_range(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length
        """
    @true_range.setter
    def true_range(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class RaytraceResults_2(XYZ_2):
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> RaytraceResults_2:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> RaytraceResults_2:
        ...
    def __deepcopy__(self, arg0: dict) -> RaytraceResults_2:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new sample location object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32], true_range: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new RaytraceResults object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
        
        Parameter ``true_range``:
            in m, accumulated ray path length
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
    def copy(self) -> RaytraceResults_2:
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
    @property
    def true_range(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length
        """
    @true_range.setter
    def true_range(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class RaytraceResults_3(XYZ_3):
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> RaytraceResults_3:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> RaytraceResults_3:
        ...
    def __deepcopy__(self, arg0: dict) -> RaytraceResults_3:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new sample location object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32], true_range: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new RaytraceResults object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
        
        Parameter ``true_range``:
            in m, accumulated ray path length
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
    def copy(self) -> RaytraceResults_3:
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
    @property
    def true_range(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length
        """
    @true_range.setter
    def true_range(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class SampleDirections_1:
    """
    A structure to store beamsample directsion (along angle, across angle
    and range).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> SampleDirections_1:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleDirections_1:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleDirections_1:
        ...
    def __eq__(self, other: SampleDirections_1) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new sample location object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(1)]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32], two_way_travel_time: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirections object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
        
        Parameter ``two_way_travel_time``:
            in m, accumulated ray path length
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
    def copy(self) -> SampleDirections_1:
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
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def alongtrack_angle(self) -> numpy.ndarray[numpy.float32]:
        """
        < in °, positive bow up, 0 == downwards
        """
    @alongtrack_angle.setter
    def alongtrack_angle(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
    @property
    def crosstrack_angle(self) -> numpy.ndarray[numpy.float32]:
        """
        < in °, positive starboard up, 0 == downwards
        """
    @crosstrack_angle.setter
    def crosstrack_angle(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
    @property
    def two_way_travel_time(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length
        """
    @two_way_travel_time.setter
    def two_way_travel_time(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class SampleDirections_2:
    """
    A structure to store beamsample directsion (along angle, across angle
    and range).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> SampleDirections_2:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleDirections_2:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleDirections_2:
        ...
    def __eq__(self, other: SampleDirections_2) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new sample location object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32], two_way_travel_time: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirections object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
        
        Parameter ``two_way_travel_time``:
            in m, accumulated ray path length
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
    def copy(self) -> SampleDirections_2:
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
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def alongtrack_angle(self) -> numpy.ndarray[numpy.float32]:
        """
        < in °, positive bow up, 0 == downwards
        """
    @alongtrack_angle.setter
    def alongtrack_angle(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
    @property
    def crosstrack_angle(self) -> numpy.ndarray[numpy.float32]:
        """
        < in °, positive starboard up, 0 == downwards
        """
    @crosstrack_angle.setter
    def crosstrack_angle(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
    @property
    def two_way_travel_time(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length
        """
    @two_way_travel_time.setter
    def two_way_travel_time(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class SampleDirections_3:
    """
    A structure to store beamsample directsion (along angle, across angle
    and range).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> SampleDirections_3:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleDirections_3:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleDirections_3:
        ...
    def __eq__(self, other: SampleDirections_3) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new sample location object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32], two_way_travel_time: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirections object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
        
        Parameter ``two_way_travel_time``:
            in m, accumulated ray path length
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
    def copy(self) -> SampleDirections_3:
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
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def alongtrack_angle(self) -> numpy.ndarray[numpy.float32]:
        """
        < in °, positive bow up, 0 == downwards
        """
    @alongtrack_angle.setter
    def alongtrack_angle(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
    @property
    def crosstrack_angle(self) -> numpy.ndarray[numpy.float32]:
        """
        < in °, positive starboard up, 0 == downwards
        """
    @crosstrack_angle.setter
    def crosstrack_angle(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
    @property
    def two_way_travel_time(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length
        """
    @two_way_travel_time.setter
    def two_way_travel_time(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class SampleIndices:
    """
    A structure to store sample indices (sample nr, beam nr) for a set of
    beams. It is used as output for the backmapper functions and as input
    for the get_wci_amplitude functions.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> SampleIndices:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleIndices:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleIndices:
        ...
    def __eq__(self, other: SampleIndices) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new SampleIndices object (all values set to 0)
        """
    @typing.overload
    def __init__(self, beam_sample_map: dict[int, list[int]]) -> None:
        """
        Construct a new SampleIndices object
        
        Parameter ``beam_sample_map_``:
            map <beam number, sample_number>
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
    def copy(self) -> SampleIndices:
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
    @property
    def beam_sample_map(self) -> dict[int, list[int]]:
        """
        < map <beam number, sample_number>
        """
    @beam_sample_map.setter
    def beam_sample_map(self, arg0: dict[int, list[int]]) -> None:
        ...
class XYZ_1:
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) and z (depth). These
    coordinates can be converted to UTM or Lat/Lon if a reference position
    (for coordinate 0) is known.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> XYZ_1:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XYZ_1:
        ...
    def __deepcopy__(self, arg0: dict) -> XYZ_1:
        ...
    def __eq__(self, other: XYZ_1) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new sample location object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(1)]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new XYZ object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
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
    def copy(self) -> XYZ_1:
        """
        return a copy using the c++ default copy constructor
        """
    def get_minmax_x(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def get_minmax_y(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def get_minmax_z(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(1)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def x(self) -> numpy.ndarray[numpy.float32]:
        """
        < x coordinate in m, positive forward
        """
    @x.setter
    def x(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
    @property
    def y(self) -> numpy.ndarray[numpy.float32]:
        """
        < y coordinate in m, positive starboard
        """
    @y.setter
    def y(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
    @property
    def z(self) -> numpy.ndarray[numpy.float32]:
        """
        < z coordinate in m, positive downwards
        """
    @z.setter
    def z(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class XYZ_2:
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) and z (depth). These
    coordinates can be converted to UTM or Lat/Lon if a reference position
    (for coordinate 0) is known.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> XYZ_2:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XYZ_2:
        ...
    def __deepcopy__(self, arg0: dict) -> XYZ_2:
        ...
    def __eq__(self, other: XYZ_2) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new sample location object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new XYZ object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
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
    def copy(self) -> XYZ_2:
        """
        return a copy using the c++ default copy constructor
        """
    def get_minmax_x(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def get_minmax_y(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def get_minmax_z(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def x(self) -> numpy.ndarray[numpy.float32]:
        """
        < x coordinate in m, positive forward
        """
    @x.setter
    def x(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
    @property
    def y(self) -> numpy.ndarray[numpy.float32]:
        """
        < y coordinate in m, positive starboard
        """
    @y.setter
    def y(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
    @property
    def z(self) -> numpy.ndarray[numpy.float32]:
        """
        < z coordinate in m, positive downwards
        """
    @z.setter
    def z(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class XYZ_3:
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) and z (depth). These
    coordinates can be converted to UTM or Lat/Lon if a reference position
    (for coordinate 0) is known.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> XYZ_3:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XYZ_3:
        ...
    def __deepcopy__(self, arg0: dict) -> XYZ_3:
        ...
    def __eq__(self, other: XYZ_3) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new sample location object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new XYZ object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
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
    def copy(self) -> XYZ_3:
        """
        return a copy using the c++ default copy constructor
        """
    def get_minmax_x(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def get_minmax_y(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def get_minmax_z(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def x(self) -> numpy.ndarray[numpy.float32]:
        """
        < x coordinate in m, positive forward
        """
    @x.setter
    def x(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
    @property
    def y(self) -> numpy.ndarray[numpy.float32]:
        """
        < y coordinate in m, positive starboard
        """
    @y.setter
    def y(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
    @property
    def z(self) -> numpy.ndarray[numpy.float32]:
        """
        < z coordinate in m, positive downwards
        """
    @z.setter
    def z(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
