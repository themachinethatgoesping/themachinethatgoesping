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
    def __init__(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None:
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
    def x(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """x coordinate in m, positive forward"""

    @x.setter
    def x(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], /) -> None: ...

    @property
    def y(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """y coordinate in m, positive starboard"""

    @y.setter
    def y(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], /) -> None: ...

    @property
    def z(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """z coordinate in m, positive downwards"""

    @z.setter
    def z(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], /) -> None: ...

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
    def __init__(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], y: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], z: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]) -> None:
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
    def x(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """x coordinate in m, positive forward"""

    @x.setter
    def x(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], /) -> None: ...

    @property
    def y(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """y coordinate in m, positive starboard"""

    @y.setter
    def y(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], /) -> None: ...

    @property
    def z(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """z coordinate in m, positive downwards"""

    @z.setter
    def z(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], /) -> None: ...

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
    def __init__(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], y: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], z: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]) -> None:
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
    def x(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]:
        """x coordinate in m, positive forward"""

    @x.setter
    def x(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], /) -> None: ...

    @property
    def y(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]:
        """y coordinate in m, positive starboard"""

    @y.setter
    def y(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], /) -> None: ...

    @property
    def z(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]:
        """z coordinate in m, positive downwards"""

    @z.setter
    def z(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], /) -> None: ...

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
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None:
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
    def alongtrack_angle(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """in °, positive bow up, 0 == downwards"""

    @alongtrack_angle.setter
    def alongtrack_angle(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], /) -> None: ...

    @property
    def crosstrack_angle(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """in °, positive starboard up, 0 == downwards"""

    @crosstrack_angle.setter
    def crosstrack_angle(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], /) -> None: ...

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
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]) -> None:
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
    def alongtrack_angle(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """in °, positive bow up, 0 == downwards"""

    @alongtrack_angle.setter
    def alongtrack_angle(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], /) -> None: ...

    @property
    def crosstrack_angle(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """in °, positive starboard up, 0 == downwards"""

    @crosstrack_angle.setter
    def crosstrack_angle(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], /) -> None: ...

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
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]) -> None:
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
    def alongtrack_angle(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]:
        """in °, positive bow up, 0 == downwards"""

    @alongtrack_angle.setter
    def alongtrack_angle(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], /) -> None: ...

    @property
    def crosstrack_angle(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]:
        """in °, positive starboard up, 0 == downwards"""

    @crosstrack_angle.setter
    def crosstrack_angle(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], /) -> None: ...

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
    def __init__(self, sample_directions: SampleDirections_1, range: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)

        Args:
            range: in m, accumulated ray path time
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], range: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None:
        """
        Construct a new SampleDirectionsRange object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
            range: in m, accumulated ray path length
        """

    def __eq__(self, other: SampleDirectionsRange_1) -> bool: ...

    @property
    def range(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """in m, accumulated ray path time"""

    @range.setter
    def range(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], /) -> None: ...

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
    def __init__(self, sample_directions: SampleDirections_2, range: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)

        Args:
            range: in m, accumulated ray path time
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], range: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]) -> None:
        """
        Construct a new SampleDirectionsRange object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
            range: in m, accumulated ray path length
        """

    def __eq__(self, other: SampleDirectionsRange_2) -> bool: ...

    @property
    def range(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """in m, accumulated ray path time"""

    @range.setter
    def range(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], /) -> None: ...

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
    def __init__(self, sample_directions: SampleDirections_3, range: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)

        Args:
            range: in m, accumulated ray path time
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], range: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]) -> None:
        """
        Construct a new SampleDirectionsRange object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
            range: in m, accumulated ray path length
        """

    def __eq__(self, other: SampleDirectionsRange_3) -> bool: ...

    @property
    def range(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]:
        """in m, accumulated ray path time"""

    @range.setter
    def range(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], /) -> None: ...

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
    def __init__(self, sample_directions: SampleDirections_1, two_way_travel_time: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)

        Args:
            two_way_travel_time: in s, accumulated ray path time
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], two_way_travel_time: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None:
        """
        Construct a new SampleDirectionsTime object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
            two_way_travel_time: in m, accumulated ray path length
        """

    def __eq__(self, other: SampleDirectionsTime_1) -> bool: ...

    @property
    def two_way_travel_time(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """in s, accumulated ray path time"""

    @two_way_travel_time.setter
    def two_way_travel_time(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], /) -> None: ...

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
    def __init__(self, sample_directions: SampleDirections_2, two_way_travel_time: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)

        Args:
            two_way_travel_time: in s, accumulated ray path time
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], two_way_travel_time: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]) -> None:
        """
        Construct a new SampleDirectionsTime object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
            two_way_travel_time: in m, accumulated ray path length
        """

    def __eq__(self, other: SampleDirectionsTime_2) -> bool: ...

    @property
    def two_way_travel_time(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """in s, accumulated ray path time"""

    @two_way_travel_time.setter
    def two_way_travel_time(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], /) -> None: ...

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
    def __init__(self, sample_directions: SampleDirections_3, two_way_travel_time: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]) -> None:
        """
        Construct a new SampleDirections object (from a SampleDirections
        object)

        Args:
            two_way_travel_time: in s, accumulated ray path time
        """

    @overload
    def __init__(self, alongtrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], crosstrack_angle: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], two_way_travel_time: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]) -> None:
        """
        Construct a new SampleDirectionsTime object

        Args:
            alongtrack_angle: in °, positive bow up, 0 == downwards
            crosstrack_angle: in °, positive starboard up, 0 == downwards
            two_way_travel_time: in m, accumulated ray path length
        """

    def __eq__(self, other: SampleDirectionsTime_3) -> bool: ...

    @property
    def two_way_travel_time(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]:
        """in s, accumulated ray path time"""

    @two_way_travel_time.setter
    def two_way_travel_time(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], /) -> None: ...

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
    def __init__(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], true_range: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None:
        """
        Construct a new RaytraceResults object

        Args:
            x: in m, positive forward
            y: in m, positive starboard
            z: in m, positive downwards
            true_range: in m, accumulated ray path length
        """

    @property
    def true_range(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """in m, accumulated ray path length"""

    @true_range.setter
    def true_range(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], /) -> None: ...

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
    def __init__(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], y: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], z: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], true_range: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]) -> None:
        """
        Construct a new RaytraceResults object

        Args:
            x: in m, positive forward
            y: in m, positive starboard
            z: in m, positive downwards
            true_range: in m, accumulated ray path length
        """

    @property
    def true_range(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """in m, accumulated ray path length"""

    @true_range.setter
    def true_range(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], /) -> None: ...

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
    def __init__(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], y: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], z: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], true_range: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]) -> None:
        """
        Construct a new RaytraceResults object

        Args:
            x: in m, positive forward
            y: in m, positive starboard
            z: in m, positive downwards
            true_range: in m, accumulated ray path length
        """

    @property
    def true_range(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]:
        """in m, accumulated ray path length"""

    @true_range.setter
    def true_range(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], /) -> None: ...

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
    def __init__(self, beam_numbers: Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')], sample_numbers: Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]) -> None:
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
    def beam_numbers(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]:
        """beam number of each sample"""

    @beam_numbers.setter
    def beam_numbers(self, arg: Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')], /) -> None: ...

    @property
    def sample_numbers(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]:
        """sample number of each sample"""

    @sample_numbers.setter
    def sample_numbers(self, arg: Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')], /) -> None: ...

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
    def __init__(self, beam_numbers: Annotated[NDArray[numpy.uint16], dict(shape=(None, None), order='C')], sample_numbers: Annotated[NDArray[numpy.uint16], dict(shape=(None, None), order='C')]) -> None:
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
    def beam_numbers(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None, None), order='C')]:
        """beam number of each sample"""

    @beam_numbers.setter
    def beam_numbers(self, arg: Annotated[NDArray[numpy.uint16], dict(shape=(None, None), order='C')], /) -> None: ...

    @property
    def sample_numbers(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None, None), order='C')]:
        """sample number of each sample"""

    @sample_numbers.setter
    def sample_numbers(self, arg: Annotated[NDArray[numpy.uint16], dict(shape=(None, None), order='C')], /) -> None: ...

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
    def __init__(self, beam_numbers: Annotated[NDArray[numpy.uint16], dict(shape=(None, None, None), order='C')], sample_numbers: Annotated[NDArray[numpy.uint16], dict(shape=(None, None, None), order='C')]) -> None:
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
    def beam_numbers(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None, None, None), order='C')]:
        """beam number of each sample"""

    @beam_numbers.setter
    def beam_numbers(self, arg: Annotated[NDArray[numpy.uint16], dict(shape=(None, None, None), order='C')], /) -> None: ...

    @property
    def sample_numbers(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None, None, None), order='C')]:
        """sample number of each sample"""

    @sample_numbers.setter
    def sample_numbers(self, arg: Annotated[NDArray[numpy.uint16], dict(shape=(None, None, None), order='C')], /) -> None: ...

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
    def __init__(self, alongtrack_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], crosstrack_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], first_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sample_interval: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], number_of_samples: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')]) -> None: ...

    def __eq__(self, other: BeamSampleParameters) -> bool: ...

    def get_alongtrack_angles(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_crosstrack_angles(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_first_sample_offset(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_sample_interval(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_number_of_samples(self) -> Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')]: ...

    def set_alongtrack_angles(self, alongtrack_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None: ...

    def set_crosstrack_angles(self, crosstrack_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None: ...

    def set_first_sample_offset(self, first_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None: ...

    def set_sample_interval(self, sample_interval: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None: ...

    def set_number_of_samples(self, number_of_samples: Annotated[NDArray[numpy.uint32], dict(shape=(None,), order='C')]) -> None: ...

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
