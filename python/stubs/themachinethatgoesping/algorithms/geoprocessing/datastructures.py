"""
Submodule that holds datastructures that hold the raytracers/georeferncing results
"""
from __future__ import annotations
import numpy
import pybind11_stubgen.typing_ext
import typing
__all__ = ['BeamSampleParameters', 'RaytraceResult', 'RaytraceResults_1', 'RaytraceResults_2', 'RaytraceResults_3', 'SampleDirectionsRange_1', 'SampleDirectionsRange_2', 'SampleDirectionsRange_3', 'SampleDirectionsTime_1', 'SampleDirectionsTime_2', 'SampleDirectionsTime_3', 'SampleDirections_1', 'SampleDirections_2', 'SampleDirections_3', 'SampleIndices_1', 'SampleIndices_2', 'SampleIndices_3', 'XYZ_1', 'XYZ_2', 'XYZ_3']
class BeamSampleParameters:
    """
    A structure to store directional parameters of multibeam system.
    Usefull as input for raytracing water column images.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BeamSampleParameters:
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
        hash function implemented using binary_hash
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
    def to_binary(self, resize_buffer: bool = True) -> bytes:
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
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RaytraceResult:
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
        hash function implemented using binary_hash
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
    def concat(arg0: list[RaytraceResults_1]) -> RaytraceResults_1:
        """
        Concatenate multiple RaytraceResults objects Note: the dimensionality
        of the RaytraceResults objects will be lost (transformed
        RaytraceResults XYZ<1>)
        
        Parameter ``vector``:
            of RaytraceResults objects
        
        Returns:
            RaytraceResults<1>
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RaytraceResults_1:
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
        hash function implemented using binary_hash
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
    def concat(arg0: list[RaytraceResults_2]) -> RaytraceResults_1:
        """
        Concatenate multiple RaytraceResults objects Note: the dimensionality
        of the RaytraceResults objects will be lost (transformed
        RaytraceResults XYZ<1>)
        
        Parameter ``vector``:
            of RaytraceResults objects
        
        Returns:
            RaytraceResults<1>
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RaytraceResults_2:
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
        hash function implemented using binary_hash
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
    def concat(arg0: list[RaytraceResults_3]) -> RaytraceResults_1:
        """
        Concatenate multiple RaytraceResults objects Note: the dimensionality
        of the RaytraceResults objects will be lost (transformed
        RaytraceResults XYZ<1>)
        
        Parameter ``vector``:
            of RaytraceResults objects
        
        Returns:
            RaytraceResults<1>
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RaytraceResults_3:
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
        hash function implemented using binary_hash
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
    @property
    def true_range(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length
        """
    @true_range.setter
    def true_range(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class SampleDirectionsRange_1(SampleDirections_1):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirectionsRange_1:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleDirectionsRange_1:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleDirectionsRange_1:
        ...
    def __eq__(self, other: SampleDirectionsRange_1) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new SampleDirections object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(1)]) -> None:
        """
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, sample_directions: SampleDirections_1, range: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)
        
        Parameter ``range``:
            in m, accumulated ray path time
        """
    @typing.overload
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32], range: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirectionsRange object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
        
        Parameter ``range``:
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
    def copy(self) -> SampleDirectionsRange_1:
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
    @property
    def range(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path time
        """
    @range.setter
    def range(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class SampleDirectionsRange_2(SampleDirections_2):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirectionsRange_2:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleDirectionsRange_2:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleDirectionsRange_2:
        ...
    def __eq__(self, other: SampleDirectionsRange_2) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new SampleDirections object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)]) -> None:
        """
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, sample_directions: SampleDirections_2, range: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)
        
        Parameter ``range``:
            in m, accumulated ray path time
        """
    @typing.overload
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32], range: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirectionsRange object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
        
        Parameter ``range``:
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
    def copy(self) -> SampleDirectionsRange_2:
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
    @property
    def range(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path time
        """
    @range.setter
    def range(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class SampleDirectionsRange_3(SampleDirections_3):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirectionsRange_3:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleDirectionsRange_3:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleDirectionsRange_3:
        ...
    def __eq__(self, other: SampleDirectionsRange_3) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new SampleDirections object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        """
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, sample_directions: SampleDirections_3, range: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)
        
        Parameter ``range``:
            in m, accumulated ray path time
        """
    @typing.overload
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32], range: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirectionsRange object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
        
        Parameter ``range``:
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
    def copy(self) -> SampleDirectionsRange_3:
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
    @property
    def range(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path time
        """
    @range.setter
    def range(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class SampleDirectionsTime_1(SampleDirections_1):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirectionsTime_1:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleDirectionsTime_1:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleDirectionsTime_1:
        ...
    def __eq__(self, other: SampleDirectionsTime_1) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new SampleDirections object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(1)]) -> None:
        """
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, sample_directions: SampleDirections_1, two_way_travel_time: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)
        
        Parameter ``two_way_travel_time``:
            in s, accumulated ray path time
        """
    @typing.overload
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32], two_way_travel_time: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirectionsTime object
        
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
    def copy(self) -> SampleDirectionsTime_1:
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
    @property
    def two_way_travel_time(self) -> numpy.ndarray[numpy.float32]:
        """
        < in s, accumulated ray path time
        """
    @two_way_travel_time.setter
    def two_way_travel_time(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class SampleDirectionsTime_2(SampleDirections_2):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirectionsTime_2:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleDirectionsTime_2:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleDirectionsTime_2:
        ...
    def __eq__(self, other: SampleDirectionsTime_2) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new SampleDirections object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)]) -> None:
        """
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, sample_directions: SampleDirections_2, two_way_travel_time: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)
        
        Parameter ``two_way_travel_time``:
            in s, accumulated ray path time
        """
    @typing.overload
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32], two_way_travel_time: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirectionsTime object
        
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
    def copy(self) -> SampleDirectionsTime_2:
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
    @property
    def two_way_travel_time(self) -> numpy.ndarray[numpy.float32]:
        """
        < in s, accumulated ray path time
        """
    @two_way_travel_time.setter
    def two_way_travel_time(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class SampleDirectionsTime_3(SampleDirections_3):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirectionsTime_3:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleDirectionsTime_3:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleDirectionsTime_3:
        ...
    def __eq__(self, other: SampleDirectionsTime_3) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new SampleDirections object (all values set to 0)
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        """
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        """
    @typing.overload
    def __init__(self, sample_directions: SampleDirections_3, two_way_travel_time: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)
        
        Parameter ``two_way_travel_time``:
            in s, accumulated ray path time
        """
    @typing.overload
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32], two_way_travel_time: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirectionsTime object
        
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
    def copy(self) -> SampleDirectionsTime_3:
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
    @property
    def two_way_travel_time(self) -> numpy.ndarray[numpy.float32]:
        """
        < in s, accumulated ray path time
        """
    @two_way_travel_time.setter
    def two_way_travel_time(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class SampleDirections_1:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirections_1:
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
        hash function implemented using binary_hash
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
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirections object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
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
    def check_shape(self) -> None:
        """
        check if the internal variables have the same shape
        """
    def copy(self) -> SampleDirections_1:
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
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(1)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
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
class SampleDirections_2:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirections_2:
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
        hash function implemented using binary_hash
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
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirections object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
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
    def check_shape(self) -> None:
        """
        check if the internal variables have the same shape
        """
    def copy(self) -> SampleDirections_2:
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
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
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
class SampleDirections_3:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirections_3:
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
        hash function implemented using binary_hash
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
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32]) -> None:
        """
        Construct a new SampleDirections object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
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
    def check_shape(self) -> None:
        """
        check if the internal variables have the same shape
        """
    def copy(self) -> SampleDirections_3:
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
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
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
class SampleIndices_1:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleIndices_1:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleIndices_1:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleIndices_1:
        ...
    def __eq__(self, other: SampleIndices_1) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
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
    def __init__(self, beam_numbers: numpy.ndarray[numpy.uint16], sample_numbers: numpy.ndarray[numpy.uint16]) -> None:
        """
        Construct a new SampleIndices object
        
        Parameter ``beam_numbers``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``sample_numbers``:
            in °, positive starboard up, 0 == downwards
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
    def check_shape(self) -> None:
        """
        check if the internal variables have the same shape
        """
    def copy(self) -> SampleIndices_1:
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
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(1)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def beam_numbers(self) -> numpy.ndarray[numpy.uint16]:
        """
        < beam number of each sample
        """
    @beam_numbers.setter
    def beam_numbers(self, arg0: numpy.ndarray[numpy.uint16]) -> None:
        ...
    @property
    def sample_numbers(self) -> numpy.ndarray[numpy.uint16]:
        """
        < sample number of each sample
        """
    @sample_numbers.setter
    def sample_numbers(self, arg0: numpy.ndarray[numpy.uint16]) -> None:
        ...
class SampleIndices_2:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleIndices_2:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleIndices_2:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleIndices_2:
        ...
    def __eq__(self, other: SampleIndices_2) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
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
    def __init__(self, beam_numbers: numpy.ndarray[numpy.uint16], sample_numbers: numpy.ndarray[numpy.uint16]) -> None:
        """
        Construct a new SampleIndices object
        
        Parameter ``beam_numbers``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``sample_numbers``:
            in °, positive starboard up, 0 == downwards
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
    def check_shape(self) -> None:
        """
        check if the internal variables have the same shape
        """
    def copy(self) -> SampleIndices_2:
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
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def beam_numbers(self) -> numpy.ndarray[numpy.uint16]:
        """
        < beam number of each sample
        """
    @beam_numbers.setter
    def beam_numbers(self, arg0: numpy.ndarray[numpy.uint16]) -> None:
        ...
    @property
    def sample_numbers(self) -> numpy.ndarray[numpy.uint16]:
        """
        < sample number of each sample
        """
    @sample_numbers.setter
    def sample_numbers(self, arg0: numpy.ndarray[numpy.uint16]) -> None:
        ...
class SampleIndices_3:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleIndices_3:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SampleIndices_3:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleIndices_3:
        ...
    def __eq__(self, other: SampleIndices_3) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
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
    def __init__(self, beam_numbers: numpy.ndarray[numpy.uint16], sample_numbers: numpy.ndarray[numpy.uint16]) -> None:
        """
        Construct a new SampleIndices object
        
        Parameter ``beam_numbers``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``sample_numbers``:
            in °, positive starboard up, 0 == downwards
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
    def check_shape(self) -> None:
        """
        check if the internal variables have the same shape
        """
    def copy(self) -> SampleIndices_3:
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
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def beam_numbers(self) -> numpy.ndarray[numpy.uint16]:
        """
        < beam number of each sample
        """
    @beam_numbers.setter
    def beam_numbers(self, arg0: numpy.ndarray[numpy.uint16]) -> None:
        ...
    @property
    def sample_numbers(self) -> numpy.ndarray[numpy.uint16]:
        """
        < sample number of each sample
        """
    @sample_numbers.setter
    def sample_numbers(self, arg0: numpy.ndarray[numpy.uint16]) -> None:
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
    def concat(arg0: list[XYZ_1]) -> XYZ_1:
        """
        Concatenate multiple XYZ objects Note: the dimensionality of the XYZ
        objects will be lost (transformed to XYZ<1>)
        
        Parameter ``vector``:
            of XYZ objects
        
        Returns:
            XYZ<1>
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XYZ_1:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    @typing.overload
    def rotate(*args, **kwargs) -> None:
        """
        Rotate the XYZ object using a quaternion
        
        Parameter ``q``:
            quaternion
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
        hash function implemented using binary_hash
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
    @typing.overload
    def rotate(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Rotate the XYZ object using yaw, pitch, roll in °
        
        Parameter ``yaw``:
            in °
        
        Parameter ``pitch``:
            in °
        
        Parameter ``roll``:
            in °
        """
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(1)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    def to_latlon(self, utm_zone: int, northern_hemisphere: bool) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
        ...
    def translate(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        ...
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
    def concat(arg0: list[XYZ_2]) -> XYZ_1:
        """
        Concatenate multiple XYZ objects Note: the dimensionality of the XYZ
        objects will be lost (transformed to XYZ<1>)
        
        Parameter ``vector``:
            of XYZ objects
        
        Returns:
            XYZ<1>
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XYZ_2:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    @typing.overload
    def rotate(*args, **kwargs) -> None:
        """
        Rotate the XYZ object using a quaternion
        
        Parameter ``q``:
            quaternion
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
        hash function implemented using binary_hash
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
    @typing.overload
    def rotate(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Rotate the XYZ object using yaw, pitch, roll in °
        
        Parameter ``yaw``:
            in °
        
        Parameter ``pitch``:
            in °
        
        Parameter ``roll``:
            in °
        """
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    def to_latlon(self, utm_zone: int, northern_hemisphere: bool) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
        ...
    def translate(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        ...
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
    def concat(arg0: list[XYZ_3]) -> XYZ_1:
        """
        Concatenate multiple XYZ objects Note: the dimensionality of the XYZ
        objects will be lost (transformed to XYZ<1>)
        
        Parameter ``vector``:
            of XYZ objects
        
        Returns:
            XYZ<1>
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XYZ_3:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    @typing.overload
    def rotate(*args, **kwargs) -> None:
        """
        Rotate the XYZ object using a quaternion
        
        Parameter ``q``:
            quaternion
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
        hash function implemented using binary_hash
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
    @typing.overload
    def rotate(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Rotate the XYZ object using yaw, pitch, roll in °
        
        Parameter ``yaw``:
            in °
        
        Parameter ``pitch``:
            in °
        
        Parameter ``roll``:
            in °
        """
    def shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    def to_latlon(self, utm_zone: int, northern_hemisphere: bool) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
        ...
    def translate(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        ...
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
