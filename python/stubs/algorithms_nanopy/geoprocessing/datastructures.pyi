"""
Submodule that holds datastructures that hold the raytracers/georeferncing results
"""
import typing

from collections.abc import Sequence
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray


class XYZ_1:
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) and z (depth). These
    coordinates can be converted to UTM or Lat/Lon if a reference position
    (for coordinate 0) is known.
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, x: Annotated[NDArray[numpy.float32], dict(order='C')], y: Annotated[NDArray[numpy.float32], dict(order='C')], z: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new XYZ object

        Args:
            x: in m, positive forward
            y: in m, positive starboard
            z: in m, positive downwards
        """

    def __eq__(self, other: XYZ_1) -> bool: ...

    def size(self) -> int: ...

    def shape(self) -> list[int]: ...

    @staticmethod
    def concat(arg: Sequence[typing.Any], /) -> XYZ_1:
        """
        Concatenate multiple XYZ objects
        Note: the dimensionality of the XYZ objects will be lost (transformed
              to XYZ_1)

        Args:
            vector: of XYZ objects

        Returns:
            XYZ_1
        """

    @overload
    def rotate(self, quat: "Eigen::Quaternion_float_0") -> None:
        """
        Rotate the XYZ object using a quaternion

        Args:
            q: quaternion
        """

    @overload
    def rotate(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Rotate the XYZ object using yaw, pitch, roll in °

        Args:
            yaw: in °
            pitch: in °
            roll: in °
        """

    def translate(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None: ...

    def to_latlon(self, utm_zone: int, northern_hemisphere: bool) -> typing.Any: ...

    @property
    def x(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """x coordinate in m, positive forward"""

    @x.setter
    def x(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @property
    def y(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """y coordinate in m, positive starboard"""

    @y.setter
    def y(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @property
    def z(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """z coordinate in m, positive downwards"""

    @z.setter
    def z(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def get_minmax_x(self) -> list[float]: ...

    def get_minmax_y(self) -> list[float]: ...

    def get_minmax_z(self) -> list[float]: ...

    def copy(self) -> XYZ_1:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XYZ_1: ...

    def __deepcopy__(self, arg: dict, /) -> XYZ_1: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XYZ_1:
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

class XYZ_2:
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) and z (depth). These
    coordinates can be converted to UTM or Lat/Lon if a reference position
    (for coordinate 0) is known.
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, x: Annotated[NDArray[numpy.float32], dict(order='C')], y: Annotated[NDArray[numpy.float32], dict(order='C')], z: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new XYZ object

        Args:
            x: in m, positive forward
            y: in m, positive starboard
            z: in m, positive downwards
        """

    def __eq__(self, other: XYZ_2) -> bool: ...

    def size(self) -> int: ...

    def shape(self) -> list[int]: ...

    @staticmethod
    def concat(arg: Sequence[typing.Any], /) -> XYZ_1:
        """
        Concatenate multiple XYZ objects
        Note: the dimensionality of the XYZ objects will be lost (transformed
              to XYZ_1)

        Args:
            vector: of XYZ objects

        Returns:
            XYZ_1
        """

    @overload
    def rotate(self, quat: "Eigen::Quaternion_float_0") -> None:
        """
        Rotate the XYZ object using a quaternion

        Args:
            q: quaternion
        """

    @overload
    def rotate(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Rotate the XYZ object using yaw, pitch, roll in °

        Args:
            yaw: in °
            pitch: in °
            roll: in °
        """

    def translate(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None: ...

    def to_latlon(self, utm_zone: int, northern_hemisphere: bool) -> typing.Any: ...

    @property
    def x(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """x coordinate in m, positive forward"""

    @x.setter
    def x(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @property
    def y(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """y coordinate in m, positive starboard"""

    @y.setter
    def y(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @property
    def z(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """z coordinate in m, positive downwards"""

    @z.setter
    def z(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def get_minmax_x(self) -> list[float]: ...

    def get_minmax_y(self) -> list[float]: ...

    def get_minmax_z(self) -> list[float]: ...

    def copy(self) -> XYZ_2:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XYZ_2: ...

    def __deepcopy__(self, arg: dict, /) -> XYZ_2: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XYZ_2:
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

class XYZ_3:
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) and z (depth). These
    coordinates can be converted to UTM or Lat/Lon if a reference position
    (for coordinate 0) is known.
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, x: Annotated[NDArray[numpy.float32], dict(order='C')], y: Annotated[NDArray[numpy.float32], dict(order='C')], z: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new XYZ object

        Args:
            x: in m, positive forward
            y: in m, positive starboard
            z: in m, positive downwards
        """

    def __eq__(self, other: XYZ_3) -> bool: ...

    def size(self) -> int: ...

    def shape(self) -> list[int]: ...

    @staticmethod
    def concat(arg: Sequence[typing.Any], /) -> XYZ_1:
        """
        Concatenate multiple XYZ objects
        Note: the dimensionality of the XYZ objects will be lost (transformed
              to XYZ_1)

        Args:
            vector: of XYZ objects

        Returns:
            XYZ_1
        """

    @overload
    def rotate(self, quat: "Eigen::Quaternion_float_0") -> None:
        """
        Rotate the XYZ object using a quaternion

        Args:
            q: quaternion
        """

    @overload
    def rotate(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Rotate the XYZ object using yaw, pitch, roll in °

        Args:
            yaw: in °
            pitch: in °
            roll: in °
        """

    def translate(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None: ...

    def to_latlon(self, utm_zone: int, northern_hemisphere: bool) -> typing.Any: ...

    @property
    def x(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """x coordinate in m, positive forward"""

    @x.setter
    def x(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @property
    def y(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """y coordinate in m, positive starboard"""

    @y.setter
    def y(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @property
    def z(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """z coordinate in m, positive downwards"""

    @z.setter
    def z(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def get_minmax_x(self) -> list[float]: ...

    def get_minmax_y(self) -> list[float]: ...

    def get_minmax_z(self) -> list[float]: ...

    def copy(self) -> XYZ_3:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XYZ_3: ...

    def __deepcopy__(self, arg: dict, /) -> XYZ_3: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XYZ_3:
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

class SampleDirections_1:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirections object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
        """

    def __eq__(self, other: SampleDirections_1) -> bool: ...

    def size(self) -> int: ...

    def shape(self) -> list[int]: ...

    def check_shape(self) -> None:
        """check if the internal variables have the same shape"""

    @property
    def alongtrack_angle(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in °, positive bow up, 0 == downwards"""

    @alongtrack_angle.setter
    def alongtrack_angle(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @property
    def crosstrack_angle(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in °, positive starboard up, 0 == downwards"""

    @crosstrack_angle.setter
    def crosstrack_angle(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def copy(self) -> SampleDirections_1:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SampleDirections_1: ...

    def __deepcopy__(self, arg: dict, /) -> SampleDirections_1: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirections_1:
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

class SampleDirections_2:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirections object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
        """

    def __eq__(self, other: SampleDirections_2) -> bool: ...

    def size(self) -> int: ...

    def shape(self) -> list[int]: ...

    def check_shape(self) -> None:
        """check if the internal variables have the same shape"""

    @property
    def alongtrack_angle(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in °, positive bow up, 0 == downwards"""

    @alongtrack_angle.setter
    def alongtrack_angle(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @property
    def crosstrack_angle(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in °, positive starboard up, 0 == downwards"""

    @crosstrack_angle.setter
    def crosstrack_angle(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def copy(self) -> SampleDirections_2:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SampleDirections_2: ...

    def __deepcopy__(self, arg: dict, /) -> SampleDirections_2: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirections_2:
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

class SampleDirections_3:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirections object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
        """

    def __eq__(self, other: SampleDirections_3) -> bool: ...

    def size(self) -> int: ...

    def shape(self) -> list[int]: ...

    def check_shape(self) -> None:
        """check if the internal variables have the same shape"""

    @property
    def alongtrack_angle(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in °, positive bow up, 0 == downwards"""

    @alongtrack_angle.setter
    def alongtrack_angle(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @property
    def crosstrack_angle(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in °, positive starboard up, 0 == downwards"""

    @crosstrack_angle.setter
    def crosstrack_angle(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def copy(self) -> SampleDirections_3:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SampleDirections_3: ...

    def __deepcopy__(self, arg: dict, /) -> SampleDirections_3: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirections_3:
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

class SampleDirectionsRange_1(SampleDirections_1):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """

    @overload
    def __init__(self) -> None:
        """Construct a new SampleDirections object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, sample_directions: SampleDirections_1, range: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)

        Args:
            range: in m, accumulated ray path time
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], range: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirectionsRange object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
            range: in m, accumulated ray path length
        """

    def __eq__(self, other: SampleDirectionsRange_1) -> bool: ...

    @property
    def range(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in m, accumulated ray path time"""

    @range.setter
    def range(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def copy(self) -> SampleDirectionsRange_1:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SampleDirectionsRange_1: ...

    def __deepcopy__(self, arg: dict, /) -> SampleDirectionsRange_1: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirectionsRange_1:
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

class SampleDirectionsRange_2(SampleDirections_2):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """

    @overload
    def __init__(self) -> None:
        """Construct a new SampleDirections object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, sample_directions: SampleDirections_2, range: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)

        Args:
            range: in m, accumulated ray path time
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], range: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirectionsRange object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
            range: in m, accumulated ray path length
        """

    def __eq__(self, other: SampleDirectionsRange_2) -> bool: ...

    @property
    def range(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in m, accumulated ray path time"""

    @range.setter
    def range(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def copy(self) -> SampleDirectionsRange_2:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SampleDirectionsRange_2: ...

    def __deepcopy__(self, arg: dict, /) -> SampleDirectionsRange_2: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirectionsRange_2:
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

class SampleDirectionsRange_3(SampleDirections_3):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """

    @overload
    def __init__(self) -> None:
        """Construct a new SampleDirections object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, sample_directions: SampleDirections_3, range: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)

        Args:
            range: in m, accumulated ray path time
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], range: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirectionsRange object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
            range: in m, accumulated ray path length
        """

    def __eq__(self, other: SampleDirectionsRange_3) -> bool: ...

    @property
    def range(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in m, accumulated ray path time"""

    @range.setter
    def range(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def copy(self) -> SampleDirectionsRange_3:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SampleDirectionsRange_3: ...

    def __deepcopy__(self, arg: dict, /) -> SampleDirectionsRange_3: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirectionsRange_3:
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

class SampleDirectionsTime_1(SampleDirections_1):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """

    @overload
    def __init__(self) -> None:
        """Construct a new SampleDirections object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, sample_directions: SampleDirections_1, two_way_travel_time: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)

        Args:
            two_way_travel_time: in s, accumulated ray path time
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], two_way_travel_time: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirectionsTime object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
            two_way_travel_time: in m, accumulated ray path length
        """

    def __eq__(self, other: SampleDirectionsTime_1) -> bool: ...

    @property
    def two_way_travel_time(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in s, accumulated ray path time"""

    @two_way_travel_time.setter
    def two_way_travel_time(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def copy(self) -> SampleDirectionsTime_1:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SampleDirectionsTime_1: ...

    def __deepcopy__(self, arg: dict, /) -> SampleDirectionsTime_1: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirectionsTime_1:
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

class SampleDirectionsTime_2(SampleDirections_2):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """

    @overload
    def __init__(self) -> None:
        """Construct a new SampleDirections object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, sample_directions: SampleDirections_2, two_way_travel_time: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)

        Args:
            two_way_travel_time: in s, accumulated ray path time
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], two_way_travel_time: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirectionsTime object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
            two_way_travel_time: in m, accumulated ray path length
        """

    def __eq__(self, other: SampleDirectionsTime_2) -> bool: ...

    @property
    def two_way_travel_time(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in s, accumulated ray path time"""

    @two_way_travel_time.setter
    def two_way_travel_time(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def copy(self) -> SampleDirectionsTime_2:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SampleDirectionsTime_2: ...

    def __deepcopy__(self, arg: dict, /) -> SampleDirectionsTime_2: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirectionsTime_2:
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

class SampleDirectionsTime_3(SampleDirections_3):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """

    @overload
    def __init__(self) -> None:
        """Construct a new SampleDirections object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, sample_directions: SampleDirections_3, two_way_travel_time: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)

        Args:
            two_way_travel_time: in s, accumulated ray path time
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(order='C')], two_way_travel_time: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new SampleDirectionsTime object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
            two_way_travel_time: in m, accumulated ray path length
        """

    def __eq__(self, other: SampleDirectionsTime_3) -> bool: ...

    @property
    def two_way_travel_time(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in s, accumulated ray path time"""

    @two_way_travel_time.setter
    def two_way_travel_time(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def copy(self) -> SampleDirectionsTime_3:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SampleDirectionsTime_3: ...

    def __deepcopy__(self, arg: dict, /) -> SampleDirectionsTime_3: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleDirectionsTime_3:
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

class RaytraceResult:
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, x: float, y: float, z: float, true_range: float) -> None:
        """
        Construct a new RaytraceResult object

        Args:
            x: in m, positive forward
            y: in m, positive starboard
            z: in m, positive downwards
            true_range: in m, accumulated ray path length
        """

    def __eq__(self, other: RaytraceResult) -> bool: ...

    @property
    def x(self) -> float:
        """in m, positive forward"""

    @x.setter
    def x(self, arg: float, /) -> None: ...

    @property
    def y(self) -> float:
        """in m, positive starboard"""

    @y.setter
    def y(self, arg: float, /) -> None: ...

    @property
    def z(self) -> float:
        """in m, positive downwards"""

    @z.setter
    def z(self, arg: float, /) -> None: ...

    @property
    def true_range(self) -> float:
        """in m, accumulated ray path length"""

    @true_range.setter
    def true_range(self, arg: float, /) -> None: ...

    def copy(self) -> RaytraceResult:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RaytraceResult: ...

    def __deepcopy__(self, arg: dict, /) -> RaytraceResult: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RaytraceResult:
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

class RaytraceResults_1(XYZ_1):
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, x: Annotated[NDArray[numpy.float32], dict(order='C')], y: Annotated[NDArray[numpy.float32], dict(order='C')], z: Annotated[NDArray[numpy.float32], dict(order='C')], true_range: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new RaytraceResults object

        Args:
            x: in m, positive forward
            y: in m, positive starboard
            z: in m, positive downwards
            true_range: in m, accumulated ray path length
        """

    @property
    def true_range(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in m, accumulated ray path length"""

    @true_range.setter
    def true_range(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @staticmethod
    def concat(arg: Sequence[typing.Any], /) -> RaytraceResults_1:
        """
        Concatenate multiple RaytraceResults objects
        Note: the dimensionality of the RaytraceResults objects will be lost
              (transformed
        RaytraceResults XYZ_1)

        Args:
            vector: of RaytraceResults objects

        Returns:
            RaytraceResults_1
        """

    def copy(self) -> RaytraceResults_1:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RaytraceResults_1: ...

    def __deepcopy__(self, arg: dict, /) -> RaytraceResults_1: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RaytraceResults_1:
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

class RaytraceResults_2(XYZ_2):
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, x: Annotated[NDArray[numpy.float32], dict(order='C')], y: Annotated[NDArray[numpy.float32], dict(order='C')], z: Annotated[NDArray[numpy.float32], dict(order='C')], true_range: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new RaytraceResults object

        Args:
            x: in m, positive forward
            y: in m, positive starboard
            z: in m, positive downwards
            true_range: in m, accumulated ray path length
        """

    @property
    def true_range(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in m, accumulated ray path length"""

    @true_range.setter
    def true_range(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @staticmethod
    def concat(arg: Sequence[typing.Any], /) -> RaytraceResults_1:
        """
        Concatenate multiple RaytraceResults objects
        Note: the dimensionality of the RaytraceResults objects will be lost
              (transformed
        RaytraceResults XYZ_1)

        Args:
            vector: of RaytraceResults objects

        Returns:
            RaytraceResults_1
        """

    def copy(self) -> RaytraceResults_2:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RaytraceResults_2: ...

    def __deepcopy__(self, arg: dict, /) -> RaytraceResults_2: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RaytraceResults_2:
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

class RaytraceResults_3(XYZ_3):
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, x: Annotated[NDArray[numpy.float32], dict(order='C')], y: Annotated[NDArray[numpy.float32], dict(order='C')], z: Annotated[NDArray[numpy.float32], dict(order='C')], true_range: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a new RaytraceResults object

        Args:
            x: in m, positive forward
            y: in m, positive starboard
            z: in m, positive downwards
            true_range: in m, accumulated ray path length
        """

    @property
    def true_range(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """in m, accumulated ray path length"""

    @true_range.setter
    def true_range(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @staticmethod
    def concat(arg: Sequence[typing.Any], /) -> RaytraceResults_1:
        """
        Concatenate multiple RaytraceResults objects
        Note: the dimensionality of the RaytraceResults objects will be lost
              (transformed
        RaytraceResults XYZ_1)

        Args:
            vector: of RaytraceResults objects

        Returns:
            RaytraceResults_1
        """

    def copy(self) -> RaytraceResults_3:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RaytraceResults_3: ...

    def __deepcopy__(self, arg: dict, /) -> RaytraceResults_3: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RaytraceResults_3:
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

class SampleIndices_1:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, beam_numbers: Annotated[NDArray[numpy.uint16], dict(order='C')], sample_numbers: Annotated[NDArray[numpy.uint16], dict(order='C')]) -> None:
        """
        Construct a new SampleIndices object

        Args:
            beam_numbers: in °, positive bow up, 0 == downwards
            sample_numbers: in °, positive starboard up, 0 == downwards
        """

    def __eq__(self, other: SampleIndices_1) -> bool: ...

    def size(self) -> int: ...

    def shape(self) -> list[int]: ...

    def check_shape(self) -> None:
        """check if the internal variables have the same shape"""

    @property
    def beam_numbers(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]:
        """beam number of each sample"""

    @beam_numbers.setter
    def beam_numbers(self, arg: Annotated[NDArray[numpy.uint16], dict(order='C')], /) -> None: ...

    @property
    def sample_numbers(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]:
        """sample number of each sample"""

    @sample_numbers.setter
    def sample_numbers(self, arg: Annotated[NDArray[numpy.uint16], dict(order='C')], /) -> None: ...

    def copy(self) -> SampleIndices_1:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SampleIndices_1: ...

    def __deepcopy__(self, arg: dict, /) -> SampleIndices_1: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleIndices_1:
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

class SampleIndices_2:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, beam_numbers: Annotated[NDArray[numpy.uint16], dict(order='C')], sample_numbers: Annotated[NDArray[numpy.uint16], dict(order='C')]) -> None:
        """
        Construct a new SampleIndices object

        Args:
            beam_numbers: in °, positive bow up, 0 == downwards
            sample_numbers: in °, positive starboard up, 0 == downwards
        """

    def __eq__(self, other: SampleIndices_2) -> bool: ...

    def size(self) -> int: ...

    def shape(self) -> list[int]: ...

    def check_shape(self) -> None:
        """check if the internal variables have the same shape"""

    @property
    def beam_numbers(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]:
        """beam number of each sample"""

    @beam_numbers.setter
    def beam_numbers(self, arg: Annotated[NDArray[numpy.uint16], dict(order='C')], /) -> None: ...

    @property
    def sample_numbers(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]:
        """sample number of each sample"""

    @sample_numbers.setter
    def sample_numbers(self, arg: Annotated[NDArray[numpy.uint16], dict(order='C')], /) -> None: ...

    def copy(self) -> SampleIndices_2:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SampleIndices_2: ...

    def __deepcopy__(self, arg: dict, /) -> SampleIndices_2: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleIndices_2:
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

class SampleIndices_3:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """

    @overload
    def __init__(self) -> None:
        """Construct a new sample location object (all values set to 0)"""

    @overload
    def __init__(self, shape: Sequence[int]) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            shape: shape of the internal tensors
        """

    @overload
    def __init__(self, beam_numbers: Annotated[NDArray[numpy.uint16], dict(order='C')], sample_numbers: Annotated[NDArray[numpy.uint16], dict(order='C')]) -> None:
        """
        Construct a new SampleIndices object

        Args:
            beam_numbers: in °, positive bow up, 0 == downwards
            sample_numbers: in °, positive starboard up, 0 == downwards
        """

    def __eq__(self, other: SampleIndices_3) -> bool: ...

    def size(self) -> int: ...

    def shape(self) -> list[int]: ...

    def check_shape(self) -> None:
        """check if the internal variables have the same shape"""

    @property
    def beam_numbers(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]:
        """beam number of each sample"""

    @beam_numbers.setter
    def beam_numbers(self, arg: Annotated[NDArray[numpy.uint16], dict(order='C')], /) -> None: ...

    @property
    def sample_numbers(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]:
        """sample number of each sample"""

    @sample_numbers.setter
    def sample_numbers(self, arg: Annotated[NDArray[numpy.uint16], dict(order='C')], /) -> None: ...

    def copy(self) -> SampleIndices_3:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SampleIndices_3: ...

    def __deepcopy__(self, arg: dict, /) -> SampleIndices_3: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SampleIndices_3:
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

class BeamSampleParameters:
    """
    A structure to store directional parameters of multibeam system.
    Usefull as input for raytracing water column images.
    """

    @overload
    def __init__(self, number_of_beams: int) -> None:
        """
        Construct a new BeamSampleParameters object (all values uninitialized)

        Args:
            number_of_beams: number of beams
        """

    @overload
    def __init__(self, alongtrack_angles: Annotated[NDArray[numpy.float32], dict(order='C')], crosstrack_angles: Annotated[NDArray[numpy.float32], dict(order='C')], first_sample_offset: Annotated[NDArray[numpy.float32], dict(order='C')], sample_interval: Annotated[NDArray[numpy.float32], dict(order='C')], number_of_samples: Annotated[NDArray[numpy.uint32], dict(order='C')]) -> None: ...

    def __eq__(self, other: BeamSampleParameters) -> bool: ...

    def get_alongtrack_angles(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_crosstrack_angles(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_first_sample_offset(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_sample_interval(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_number_of_samples(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def set_alongtrack_angles(self, alongtrack_angles: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None: ...

    def set_crosstrack_angles(self, crosstrack_angles: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None: ...

    def set_first_sample_offset(self, first_sample_offset: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None: ...

    def set_sample_interval(self, sample_interval: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None: ...

    def set_number_of_samples(self, number_of_samples: Annotated[NDArray[numpy.uint32], dict(order='C')]) -> None: ...

    def copy(self) -> BeamSampleParameters:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BeamSampleParameters: ...

    def __deepcopy__(self, arg: dict, /) -> BeamSampleParameters: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BeamSampleParameters:
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

class BeamAffine1D:
    """
    A 1D affine transform per beam: value = offset + slope * sample_nr

    Stores one offset and one slope per beam in contiguous arrays (SoA
    layout), enabling SIMD vectorization across beams.
    """

    @overload
    def __init__(self) -> None:
        """Construct an empty BeamAffine1D"""

    @overload
    def __init__(self, n_beams: int) -> None:
        """
        Construct a BeamAffine1D for a given number of beams (uninitialized
        values)

        Args:
            n_beams: number of beams
        """

    @overload
    def __init__(self, offsets: Annotated[NDArray[numpy.float32], dict(order='C')], slopes: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct a BeamAffine1D from existing offsets and slopes

        Args:
            offsets_: base value per beam [n_beams]
            slopes_: slope per beam [n_beams]
        """

    def __eq__(self, other: BeamAffine1D) -> bool: ...

    @property
    def offsets(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """[n_beams] base value per beam"""

    @offsets.setter
    def offsets(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    @property
    def slopes(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """[n_beams] slope (change per sample) per beam"""

    @slopes.setter
    def slopes(self, arg: Annotated[NDArray[numpy.float32], dict(order='C')], /) -> None: ...

    def size(self) -> int: ...

    def forward(self, beam_index: int, sample_nr: float) -> float:
        """
        Compute value = offset + slope * sample_nr for a single beam

        Args:
            beam_index: beam index
            sample_nr: sample number (float for sub-sample interpolation)

        Returns:
            float
        """

    def inverse(self, beam_index: int, value: float) -> float:
        """
        Compute sample_nr = (value - offset) / slope for a single beam

        Args:
            beam_index: beam index
            value: the value to invert

        Returns:
            float sample number
        """

    @staticmethod
    def from_base_and_endpoints(base_value: float, end_values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], end_sample_numbers: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> BeamAffine1D:
        """
        Create a BeamAffine1D from a base value and per-beam end values at
        known sample numbers.

        slope = (end_values - base_value) / end_sample_numbers offset =
        base_value (for all beams)

        Args:
            base_value: scalar base value (at sample 0)
            end_values: per-beam values at the end sample [n_beams]
            end_sample_numbers: per-beam sample number of the end values
                                [n_beams]

        Returns:
            BeamAffine1D
        """

    def copy(self) -> BeamAffine1D:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BeamAffine1D: ...

    def __deepcopy__(self, arg: dict, /) -> BeamAffine1D: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BeamAffine1D:
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

class BeamSampleGeometryBounds:
    """Bounding box of beam/sample coordinates."""

    def __init__(self) -> None: ...

    @property
    def x_min(self) -> float: ...

    @x_min.setter
    def x_min(self, arg: float, /) -> None: ...

    @property
    def x_max(self) -> float: ...

    @x_max.setter
    def x_max(self, arg: float, /) -> None: ...

    @property
    def y_min(self) -> float: ...

    @y_min.setter
    def y_min(self, arg: float, /) -> None: ...

    @property
    def y_max(self) -> float: ...

    @y_max.setter
    def y_max(self, arg: float, /) -> None: ...

    @property
    def z_min(self) -> float: ...

    @z_min.setter
    def z_min(self, arg: float, /) -> None: ...

    @property
    def z_max(self) -> float: ...

    @z_max.setter
    def z_max(self, arg: float, /) -> None: ...

    def __eq__(self, other: BeamSampleGeometryBounds) -> bool: ...

    def __repr__(self) -> str: ...

class BeamSampleGeometry:
    """
    Stores per-ping beam/sample geometry as linear affines.

    Each optional affine maps sample_nr → a coordinate (x, y, or z) per
    beam:
      coord[beam] = affine.offsets[beam] + affine.slopes[beam] * sample_nr

    The user can set only the affines they need (e.g. z-only for depth
    images). Transformation functions will throw if the required affine is
    not set.
    """

    @overload
    def __init__(self) -> None:
        """Construct an empty BeamSampleGeometry"""

    @overload
    def __init__(self, first_sample_numbers: Annotated[NDArray[numpy.float32], dict(order='C')], number_of_samples: Annotated[NDArray[numpy.uint32], dict(order='C')]) -> None:
        """
        Construct a BeamSampleGeometry with beam metadata only (no affines
        set)

        Args:
            first_sample_numbers: first valid sample number per beam [n_beams]
            number_of_samples: number of samples per beam [n_beams]
        """

    def __eq__(self, other: BeamSampleGeometry) -> bool: ...

    def get_n_beams(self) -> int: ...

    def get_first_sample_numbers(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_number_of_samples(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_last_sample_numbers(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def has_x_affine(self) -> bool: ...

    def has_y_affine(self) -> bool: ...

    def has_z_affine(self) -> bool: ...

    def get_x_affine(self) -> BeamAffine1D: ...

    def get_y_affine(self) -> BeamAffine1D: ...

    def get_z_affine(self) -> BeamAffine1D: ...

    def set_x_affine(self, affine: BeamAffine1D) -> None: ...

    def set_y_affine(self, affine: BeamAffine1D) -> None: ...

    def set_z_affine(self, affine: BeamAffine1D) -> None: ...

    def set_xyz_affines(self, affine_x: BeamAffine1D, affine_y: BeamAffine1D, affine_z: BeamAffine1D) -> None: ...

    @staticmethod
    def from_bottom_xyz(bottom_xyz: XYZ_1, base_x: float, base_y: float, base_z: float, bottom_sample_numbers: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], first_sample_numbers: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], number_of_samples: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')]) -> BeamSampleGeometry:
        """
        Create a BeamSampleGeometry from a base XYZ location and per-beam
        bottom XYZ locations with their corresponding sample numbers.

        Computes affines such that:
          coord(sample_nr) = base_coord + (bottom_coord - base_coord) /
          bottom_sample_nr *
        sample_nr

        Args:
            base_xyz: base location (single point, e.g. transducer position)
            bottom_xyz: per-beam bottom locations [n_beams]
            bottom_sample_numbers: per-beam sample number at the bottom
                                   [n_beams]
            first_sample_numbers: per-beam first valid sample number [n_beams]
            number_of_samples: per-beam number of samples [n_beams]

        Returns:
            BeamSampleGeometry with x, y, z affines set
        """

    @staticmethod
    def from_bottom_z(base_z: float, bottom_depths: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], bottom_sample_numbers: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], first_sample_numbers: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], number_of_samples: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')]) -> BeamSampleGeometry:
        """
        Create a BeamSampleGeometry with z affine only, from a base depth and
        per-beam bottom depths at known sample numbers.

        Args:
            base_z: base depth (e.g. transducer depth)
            bottom_depths: per-beam bottom depths [n_beams]
            bottom_sample_numbers: per-beam sample number at the bottom
                                   [n_beams]
            first_sample_numbers: per-beam first valid sample number [n_beams]
            number_of_samples: per-beam number of samples [n_beams]

        Returns:
            BeamSampleGeometry with z affine set
        """

    @staticmethod
    def from_angle_and_range(crosstrack_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], range_sample_numbers: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], first_sample_numbers: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], number_of_samples: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')]) -> BeamSampleGeometry:
        """
        Create a BeamSampleGeometry from crosstrack angles and ranges.

        Computes y and z affines from the crosstrack angle and range at a
        known sample number per beam (no x affine set since no alongtrack
        info):
          y(sample_nr) = (-range * sin(crosstrack_angle)) / range_sample_nr *
          sample_nr z(sample_nr) = ( range * cos(crosstrack_angle)) /
          range_sample_nr * sample_nr

        Args:
            crosstrack_angles: in °, positive portside up, 0 == downwards
                               [n_beams]
            ranges: in m, per beam [n_beams]
            range_sample_numbers: sample number at which the range was
                                  measured [n_beams]
            first_sample_numbers: first valid sample number per beam [n_beams]
            number_of_samples: number of samples per beam [n_beams]

        Returns:
            BeamSampleGeometry with y and z affines set
        """

    @staticmethod
    def from_angles_and_range(alongtrack_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], crosstrack_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], range_sample_numbers: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], first_sample_numbers: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], number_of_samples: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')]) -> BeamSampleGeometry:
        """
        Create a BeamSampleGeometry from alongtrack angles, crosstrack angles,
        and ranges.

        Uses the independent / Mills Cross formulation: the TX and RX arrays
        measure angles independently in perpendicular planes, so each angle
        contributes one horizontal displacement:
          x(sample_nr) = ( range * sin(at_angle))  / range_sample_nr *
          sample_nr y(sample_nr) = (-range * sin(ct_angle))  / range_sample_nr
          * sample_nr z(sample_nr) = sqrt(range² - x² - y²)    /
          range_sample_nr * sample_nr

        Args:
            alongtrack_angles: in °, positive bow up, 0 == downwards [n_beams]
            crosstrack_angles: in °, positive portside up, 0 == downwards
                               [n_beams]
            ranges: in m, per beam [n_beams]
            range_sample_numbers: sample number at which the range was
                                  measured [n_beams]
            first_sample_numbers: first valid sample number per beam [n_beams]
            number_of_samples: number of samples per beam [n_beams]

        Returns:
            BeamSampleGeometry with x, y, z affines set
        """

    @overload
    def forward_x(self, beam_indices: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')], sample_numbers: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Compute x for (beam_index, sample_number) pairs. Sorted beam_indices yield best SIMD throughput.
        """

    @overload
    def forward_x(self, beam_indices: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')], first_sample_numbers: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')], last_sample_numbers: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')], sample_step: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Compute x for sample ranges per beam. Returns 2D [n_beams x max_samples], NaN-padded.
        """

    @overload
    def forward_y(self, beam_indices: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')], sample_numbers: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """Compute y for (beam_index, sample_number) pairs."""

    @overload
    def forward_y(self, beam_indices: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')], first_sample_numbers: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')], last_sample_numbers: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')], sample_step: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Compute y for sample ranges per beam. Returns 2D [n_beams x max_samples], NaN-padded.
        """

    @overload
    def forward_z(self, beam_indices: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')], sample_numbers: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """Compute z for (beam_index, sample_number) pairs."""

    @overload
    def forward_z(self, beam_indices: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')], first_sample_numbers: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')], last_sample_numbers: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')], sample_step: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Compute z for sample ranges per beam. Returns 2D [n_beams x max_samples], NaN-padded.
        """

    def get_flat_offsets(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]:
        """
        Compute per-beam cumulative offsets into a flat sample array.

        flat_offsets[b] = sum(number_of_samples[0..b-1])

        Use with: flat_index = flat_offsets[beam] + (sample_nr -
        first_sample_numbers[beam])

        Returns:
            xt::xtensor_unsignedint_1 [n_beams]
        """

    def get_total_samples(self) -> int:
        """Total number of samples across all beams."""

    def forward_x_flat(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Compute the full flat x coordinate array for all beams and samples.

        The result has get_total_samples() elements laid out contiguously per
        beam. Index with:
          flat_index = get_flat_offsets()[beam] + (sample_nr -
          first_sample_numbers[beam])
        """

    def forward_y_flat(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """@copydoc forward_x_flat"""

    def forward_z_flat(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """@copydoc forward_x_flat"""

    def get_bounds(self) -> BeamSampleGeometryBounds:
        """
        Compute the bounding box of all beam/sample coordinates.

        Evaluates the forward transform at the first and last sample of every
        beam and takes min/max.  Only populates bounds for dimensions that
        have a set affine; others stay NaN.
        """

    def backward_nearest(self, data: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], y_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], z_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], supersampling: int = 1, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """
        Backward-map WCI data to (y, z) image via nearest-neighbor.
        Sample numbers use Euclidean range from the sensor to each pixel.
        When supersampling > 1, probes S*S sub-pixel locations per pixel
        and averages (equivalent to render-at-high-res-then-downsample).
        """

    def backward_bilinear(self, data: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], y_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], z_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], supersampling: int = 1, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """
        Backward-map WCI data to (y, z) image via bilinear interpolation.
        Sample numbers use Euclidean range from the sensor to each pixel.
        When supersampling > 1, probes S*S sub-pixel locations per pixel
        and averages (equivalent to render-at-high-res-then-downsample).
        """

    def copy(self) -> BeamSampleGeometry:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BeamSampleGeometry: ...

    def __deepcopy__(self, arg: dict, /) -> BeamSampleGeometry: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BeamSampleGeometry:
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
