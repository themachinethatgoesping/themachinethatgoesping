"""Submodule that holds datastructures that hold the raytracers/georeferncing results"""
from __future__ import annotations
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import typing
import numpy
import pybind11_stubgen.typing_ext
_Shape = typing.Tuple[int, ...]

__all__ = [
    "RaytraceResult",
    "RaytraceResults_1",
    "RaytraceResults_2",
    "RaytraceResults_3",
    "SampleDirections_1",
    "SampleDirections_2",
    "SampleDirections_3",
    "SampleIndices"
]


class RaytraceResult():
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    def __copy__(self) -> RaytraceResult: ...
    def __deepcopy__(self, arg0: dict) -> RaytraceResult: ...
    def __eq__(self, other: RaytraceResult) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new sample location object (all values set to 0)

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
    @typing.overload
    def __init__(self, x: float, y: float, z: float, true_range: float) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> RaytraceResult: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RaytraceResult: 
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
    @property
    def true_range(self) -> float:
        """
        < in m, accumulated ray path length

        :type: float
        """
    @true_range.setter
    def true_range(self, arg0: float) -> None:
        """
        < in m, accumulated ray path length
        """
    @property
    def x(self) -> float:
        """
        < in m, positive forward

        :type: float
        """
    @x.setter
    def x(self, arg0: float) -> None:
        """
        < in m, positive forward
        """
    @property
    def y(self) -> float:
        """
        < in m, positive starboard

        :type: float
        """
    @y.setter
    def y(self, arg0: float) -> None:
        """
        < in m, positive starboard
        """
    @property
    def z(self) -> float:
        """
        < in m, positive downwards

        :type: float
        """
    @z.setter
    def z(self, arg0: float) -> None:
        """
        < in m, positive downwards
        """
    pass
class RaytraceResults_1():
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    def __copy__(self) -> RaytraceResults_1: ...
    def __deepcopy__(self, arg0: dict) -> RaytraceResults_1: ...
    def __eq__(self, other: RaytraceResults_1) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new sample location object (all values set to 0)

        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Parameter ``shape``:
            shape of the internal tensors

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
    @typing.overload
    def __init__(self, shape: typing.Annotated[typing.List[int], pybind11_stubgen.typing_ext.FixedSize(1)]) -> None: ...
    @typing.overload
    def __init__(self, x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32], true_range: numpy.ndarray[numpy.float32]) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> RaytraceResults_1: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RaytraceResults_1: 
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
    def size(self) -> int: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def true_range(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length

        :type: numpy.ndarray[numpy.float32]
        """
    @true_range.setter
    def true_range(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, accumulated ray path length
        """
    @property
    def x(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, positive forward

        :type: numpy.ndarray[numpy.float32]
        """
    @x.setter
    def x(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, positive forward
        """
    @property
    def y(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, positive starboard

        :type: numpy.ndarray[numpy.float32]
        """
    @y.setter
    def y(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, positive starboard
        """
    @property
    def z(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, positive downwards

        :type: numpy.ndarray[numpy.float32]
        """
    @z.setter
    def z(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, positive downwards
        """
    pass
class RaytraceResults_2():
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    def __copy__(self) -> RaytraceResults_2: ...
    def __deepcopy__(self, arg0: dict) -> RaytraceResults_2: ...
    def __eq__(self, other: RaytraceResults_2) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new sample location object (all values set to 0)

        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Parameter ``shape``:
            shape of the internal tensors

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
    @typing.overload
    def __init__(self, shape: typing.Annotated[typing.List[int], pybind11_stubgen.typing_ext.FixedSize(2)]) -> None: ...
    @typing.overload
    def __init__(self, x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32], true_range: numpy.ndarray[numpy.float32]) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> RaytraceResults_2: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RaytraceResults_2: 
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
    def size(self) -> int: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def true_range(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length

        :type: numpy.ndarray[numpy.float32]
        """
    @true_range.setter
    def true_range(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, accumulated ray path length
        """
    @property
    def x(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, positive forward

        :type: numpy.ndarray[numpy.float32]
        """
    @x.setter
    def x(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, positive forward
        """
    @property
    def y(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, positive starboard

        :type: numpy.ndarray[numpy.float32]
        """
    @y.setter
    def y(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, positive starboard
        """
    @property
    def z(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, positive downwards

        :type: numpy.ndarray[numpy.float32]
        """
    @z.setter
    def z(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, positive downwards
        """
    pass
class RaytraceResults_3():
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    def __copy__(self) -> RaytraceResults_3: ...
    def __deepcopy__(self, arg0: dict) -> RaytraceResults_3: ...
    def __eq__(self, other: RaytraceResults_3) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new sample location object (all values set to 0)

        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Parameter ``shape``:
            shape of the internal tensors

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
    @typing.overload
    def __init__(self, shape: typing.Annotated[typing.List[int], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None: ...
    @typing.overload
    def __init__(self, x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32], true_range: numpy.ndarray[numpy.float32]) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> RaytraceResults_3: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RaytraceResults_3: 
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
    def size(self) -> int: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def true_range(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length

        :type: numpy.ndarray[numpy.float32]
        """
    @true_range.setter
    def true_range(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, accumulated ray path length
        """
    @property
    def x(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, positive forward

        :type: numpy.ndarray[numpy.float32]
        """
    @x.setter
    def x(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, positive forward
        """
    @property
    def y(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, positive starboard

        :type: numpy.ndarray[numpy.float32]
        """
    @y.setter
    def y(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, positive starboard
        """
    @property
    def z(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, positive downwards

        :type: numpy.ndarray[numpy.float32]
        """
    @z.setter
    def z(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, positive downwards
        """
    pass
class SampleDirections_1():
    """
    A structure to store beamsample directsion (along angle, across angle
    and range).
    """
    def __copy__(self) -> SampleDirections_1: ...
    def __deepcopy__(self, arg0: dict) -> SampleDirections_1: ...
    def __eq__(self, other: SampleDirections_1) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new sample location object (all values set to 0)

        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Parameter ``shape``:
            shape of the internal tensors

        Construct a new SampleDirections object

        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards

        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards

        Parameter ``two_way_travel_time``:
            in m, accumulated ray path length
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[typing.List[int], pybind11_stubgen.typing_ext.FixedSize(1)]) -> None: ...
    @typing.overload
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32], two_way_travel_time: numpy.ndarray[numpy.float32]) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> SampleDirections_1: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirections_1: 
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
    def size(self) -> int: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def alongtrack_angle(self) -> numpy.ndarray[numpy.float32]:
        """
        < in °, positive bow up, 0 == downwards

        :type: numpy.ndarray[numpy.float32]
        """
    @alongtrack_angle.setter
    def alongtrack_angle(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in °, positive bow up, 0 == downwards
        """
    @property
    def crosstrack_angle(self) -> numpy.ndarray[numpy.float32]:
        """
        < in °, positive starboard up, 0 == downwards

        :type: numpy.ndarray[numpy.float32]
        """
    @crosstrack_angle.setter
    def crosstrack_angle(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in °, positive starboard up, 0 == downwards
        """
    @property
    def two_way_travel_time(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length

        :type: numpy.ndarray[numpy.float32]
        """
    @two_way_travel_time.setter
    def two_way_travel_time(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, accumulated ray path length
        """
    pass
class SampleDirections_2():
    """
    A structure to store beamsample directsion (along angle, across angle
    and range).
    """
    def __copy__(self) -> SampleDirections_2: ...
    def __deepcopy__(self, arg0: dict) -> SampleDirections_2: ...
    def __eq__(self, other: SampleDirections_2) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new sample location object (all values set to 0)

        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Parameter ``shape``:
            shape of the internal tensors

        Construct a new SampleDirections object

        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards

        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards

        Parameter ``two_way_travel_time``:
            in m, accumulated ray path length
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[typing.List[int], pybind11_stubgen.typing_ext.FixedSize(2)]) -> None: ...
    @typing.overload
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32], two_way_travel_time: numpy.ndarray[numpy.float32]) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> SampleDirections_2: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirections_2: 
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
    def size(self) -> int: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def alongtrack_angle(self) -> numpy.ndarray[numpy.float32]:
        """
        < in °, positive bow up, 0 == downwards

        :type: numpy.ndarray[numpy.float32]
        """
    @alongtrack_angle.setter
    def alongtrack_angle(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in °, positive bow up, 0 == downwards
        """
    @property
    def crosstrack_angle(self) -> numpy.ndarray[numpy.float32]:
        """
        < in °, positive starboard up, 0 == downwards

        :type: numpy.ndarray[numpy.float32]
        """
    @crosstrack_angle.setter
    def crosstrack_angle(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in °, positive starboard up, 0 == downwards
        """
    @property
    def two_way_travel_time(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length

        :type: numpy.ndarray[numpy.float32]
        """
    @two_way_travel_time.setter
    def two_way_travel_time(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, accumulated ray path length
        """
    pass
class SampleDirections_3():
    """
    A structure to store beamsample directsion (along angle, across angle
    and range).
    """
    def __copy__(self) -> SampleDirections_3: ...
    def __deepcopy__(self, arg0: dict) -> SampleDirections_3: ...
    def __eq__(self, other: SampleDirections_3) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new sample location object (all values set to 0)

        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Parameter ``shape``:
            shape of the internal tensors

        Construct a new SampleDirections object

        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards

        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards

        Parameter ``two_way_travel_time``:
            in m, accumulated ray path length
        """
    @typing.overload
    def __init__(self, shape: typing.Annotated[typing.List[int], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None: ...
    @typing.overload
    def __init__(self, alongtrack_angle: numpy.ndarray[numpy.float32], crosstrack_angle: numpy.ndarray[numpy.float32], two_way_travel_time: numpy.ndarray[numpy.float32]) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> SampleDirections_3: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirections_3: 
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
    def size(self) -> int: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def alongtrack_angle(self) -> numpy.ndarray[numpy.float32]:
        """
        < in °, positive bow up, 0 == downwards

        :type: numpy.ndarray[numpy.float32]
        """
    @alongtrack_angle.setter
    def alongtrack_angle(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in °, positive bow up, 0 == downwards
        """
    @property
    def crosstrack_angle(self) -> numpy.ndarray[numpy.float32]:
        """
        < in °, positive starboard up, 0 == downwards

        :type: numpy.ndarray[numpy.float32]
        """
    @crosstrack_angle.setter
    def crosstrack_angle(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in °, positive starboard up, 0 == downwards
        """
    @property
    def two_way_travel_time(self) -> numpy.ndarray[numpy.float32]:
        """
        < in m, accumulated ray path length

        :type: numpy.ndarray[numpy.float32]
        """
    @two_way_travel_time.setter
    def two_way_travel_time(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < in m, accumulated ray path length
        """
    pass
class SampleIndices():
    """
    A structure to store sample indices (sample nr, beam nr) for a set of
    beams. It is used as output for the backmapper functions and as input
    for the get_wci_amplitude functions.
    """
    def __copy__(self) -> SampleIndices: ...
    def __deepcopy__(self, arg0: dict) -> SampleIndices: ...
    def __eq__(self, other: SampleIndices) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new SampleIndices object (all values set to 0)

        Construct a new SampleIndices object

        Parameter ``beam_sample_map_``:
            map <beam number, sample_number>
        """
    @typing.overload
    def __init__(self, beam_sample_map: typing.Dict[int, typing.List[int]]) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> SampleIndices: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleIndices: 
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
    @property
    def beam_sample_map(self) -> typing.Dict[int, typing.List[int]]:
        """
        < map <beam number, sample_number>

        :type: typing.Dict[int, typing.List[int]]
        """
    @beam_sample_map.setter
    def beam_sample_map(self, arg0: typing.Dict[int, typing.List[int]]) -> None:
        """
        < map <beam number, sample_number>
        """
    pass
