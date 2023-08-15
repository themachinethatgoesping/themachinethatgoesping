"""Submodule that holds datastructures that hold the raytracers/georeferncing results"""
from __future__ import annotations
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import typing
import numpy
import pybind11_stubgen.typing_ext
_Shape = typing.Tuple[int, ...]

__all__ = [
    "SampleLocationLocal",
    "SampleLocationsLocal_1",
    "SampleLocationsLocal_2",
    "SampleLocationsLocal_3"
]


class SampleLocationLocal():
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    def __copy__(self) -> SampleLocationLocal: ...
    def __deepcopy__(self, arg0: dict) -> SampleLocationLocal: ...
    def __eq__(self, other: SampleLocationLocal) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new sample location object (all values set to 0)

        Construct a new SampleLocationLocal object

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
    def copy(self) -> SampleLocationLocal: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleLocationLocal: 
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
class SampleLocationsLocal_1():
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    def __copy__(self) -> SampleLocationsLocal_1: ...
    def __deepcopy__(self, arg0: dict) -> SampleLocationsLocal_1: ...
    def __eq__(self, other: SampleLocationsLocal_1) -> bool: ...
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

        Construct a new SampleLocationsLocal object

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
    def copy(self) -> SampleLocationsLocal_1: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleLocationsLocal_1: 
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
class SampleLocationsLocal_2():
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    def __copy__(self) -> SampleLocationsLocal_2: ...
    def __deepcopy__(self, arg0: dict) -> SampleLocationsLocal_2: ...
    def __eq__(self, other: SampleLocationsLocal_2) -> bool: ...
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

        Construct a new SampleLocationsLocal object

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
    def copy(self) -> SampleLocationsLocal_2: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleLocationsLocal_2: 
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
class SampleLocationsLocal_3():
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    def __copy__(self) -> SampleLocationsLocal_3: ...
    def __deepcopy__(self, arg0: dict) -> SampleLocationsLocal_3: ...
    def __eq__(self, other: SampleLocationsLocal_3) -> bool: ...
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

        Construct a new SampleLocationsLocal object

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
    def copy(self) -> SampleLocationsLocal_3: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleLocationsLocal_3: 
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
