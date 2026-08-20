"""
Rotation class (Rotation = float, RotationD = double) built on Eigen quaternions, with yaw/pitch/roll construction and (vectorized) vector rotation
"""

from collections.abc import Sequence
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray


class Rotation:
    """
    A rotation stored as a normalized Eigen quaternion.

    Rotation is an Eigen::Quaternion, so it can be used directly in any
    quaternion expression (composition, inverse, slerp, ...). On top of
    that it offers:
      * (implicit) construction from yaw/pitch/roll (degrees by default),
        * extraction to yaw/pitch/roll and roll/pitch/yaw, * rotation of a
        single xyz vector, of another Rotation (composition) and of a
        batch of xyz vectors (vectorized, one shared rotation matrix),
      * copy, binary streaming and object printing like the other classes.

    The quaternion is kept normalized after every construction so vector
    rotation is always metric. yaw/pitch/roll follow the ping convention:
    yaw about z (down, 0 deg = north), pitch about y (starboard, positive
    = bow up), roll about x (forward, positive = port up); rotations are
    applied yaw, then pitch, then roll.

    Template Args:
        t_float: floating point type of the quaternion coefficients (float
                 or double).
    """

    @overload
    def __init__(self) -> None:
        """Construct an identity rotation (no rotation)."""

    @overload
    def __init__(self, ypr: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        Construct a Rotation from yaw, pitch and roll (implicit).

        Args:
            ypr: array containing {yaw, pitch, roll}.
            input_in_degrees: if true (default) yaw/pitch/roll are in degrees,
                              otherwise radians.
        """

    @overload
    def __init__(self, yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> None:
        """
        Construct a Rotation from yaw, pitch and roll.

        Args:
            yaw: rotation around z (down) [deg or rad], 0 deg = north.
            pitch: rotation around y (starboard) [deg or rad], positive = bow
                   up.
            roll: rotation around x (forward) [deg or rad], positive = port
                  up.
            input_in_degrees: if true (default) yaw/pitch/roll are in degrees,
                              otherwise radians.
        """

    @staticmethod
    def from_quaternion(w: float, x: float, y: float, z: float) -> Rotation:
        """
        Build a Rotation from raw quaternion coefficients (w, x, y, z).

        Args:
            w: scalar (real) part.
            x: i coefficient.
            y: j coefficient.
            z: k coefficient.

        Returns:
            normalized Rotation.
        """

    @overload
    @staticmethod
    def from_ypr(yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> Rotation:
        """
        Build a Rotation from yaw, pitch and roll.
        Args:
            yaw: rotation around z (down) [deg or rad].
            pitch: rotation around y (starboard) [deg or rad].
            roll: rotation around x (forward) [deg or rad].
            input_in_degrees: if true (default) inputs are degrees, otherwise
                              radians.

        Returns:
            normalized Rotation.
        """

    @overload
    @staticmethod
    def from_ypr(ypr: Sequence[float], input_in_degrees: bool = True) -> Rotation:
        """
        Build a Rotation from a {yaw, pitch, roll} array.
        Args:
            ypr: array containing {yaw, pitch, roll}.
            input_in_degrees: if true (default) inputs are degrees, otherwise
                              radians.

        Returns:
            normalized Rotation.
        """

    @overload
    @staticmethod
    def from_rpy(roll: float, pitch: float, yaw: float, input_in_degrees: bool = True) -> Rotation:
        """
        Build a Rotation from roll, pitch and yaw.
        Args:
            roll: rotation around x (forward) [deg or rad].
            pitch: rotation around y (starboard) [deg or rad].
            yaw: rotation around z (down) [deg or rad].
            input_in_degrees: if true (default) inputs are degrees, otherwise
                              radians.

        Returns:
            normalized Rotation.
        """

    @overload
    @staticmethod
    def from_rpy(rpy: Sequence[float], input_in_degrees: bool = True) -> Rotation:
        """
        Build a Rotation from a {roll, pitch, yaw} array.
        Args:
            rpy: array containing {roll, pitch, yaw}.
            input_in_degrees: if true (default) inputs are degrees, otherwise
                              radians.

        Returns:
            normalized Rotation.
        """

    def ypr(self, output_in_degrees: bool = True) -> list[float]:
        """
        Extract yaw, pitch and roll from the rotation.
        Args:
            output_in_degrees: if true (default) the output is in degrees,
                               otherwise radians.

        Returns:
            array containing {yaw, pitch, roll}.
        """

    def rpy(self, output_in_degrees: bool = True) -> list[float]:
        """
        Extract roll, pitch and yaw from the rotation.
        Args:
            output_in_degrees: if true (default) the output is in degrees,
                               otherwise radians.

        Returns:
            array containing {roll, pitch, yaw}.
        """

    def wxyz(self) -> list[float]:
        """
        Get the raw quaternion coefficients as {w, x, y, z}.
        Returns:
            array containing {w, x, y, z}.
        """

    @overload
    def rotate(self, x: float, y: float, z: float) -> list[float]:
        """
        Rotate a single 3D vector by this rotation.
        Args:
            x: x component (forward).
            y: y component (starboard).
            z: z component (down).

        Returns:
            the rotated {x, y, z} vector.
        """

    @overload
    def rotate(self, xyz: Sequence[float]) -> list[float]:
        """
        Rotate a single 3D vector by this rotation.
        Args:
            xyz: the {x, y, z} vector to rotate.

        Returns:
            the rotated {x, y, z} vector.
        """

    @overload
    def rotate(self, rotation: Rotation) -> Rotation:
        """
        Rotate (compose with) another rotation: apply this rotation to
        ``rotation.``
        Args:
            rotation: the rotation to be rotated.

        Returns:
            the combined rotation (this * rotation).
        """

    @overload
    def rotate(self, points: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Rotate a batch of 3D vectors by this rotation (vectorized).

        The rotation matrix is built once and applied to every row, which is
        the fast path for rotating many points by the same rotation.

        Args:
            points: [n, 3] tensor of (x, y, z) row vectors.

        Returns:
            [n, 3] tensor of rotated row vectors.

        Raises:
            std::invalid_argument: if the second dimension is not 3.
        """

    def __eq__(self, other: Rotation) -> bool:
        """
        Two rotations are equal if their quaternions describe the same
        orientation (q == -q).
        """

    def __mul__(self, other: Rotation) -> Rotation: ...

    def copy(self) -> Rotation:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> Rotation: ...

    def __deepcopy__(self, arg: dict, /) -> Rotation: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Rotation:
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

class RotationD:
    """
    A rotation stored as a normalized Eigen quaternion.

    Rotation is an Eigen::Quaternion, so it can be used directly in any
    quaternion expression (composition, inverse, slerp, ...). On top of
    that it offers:
      * (implicit) construction from yaw/pitch/roll (degrees by default),
        * extraction to yaw/pitch/roll and roll/pitch/yaw, * rotation of a
        single xyz vector, of another Rotation (composition) and of a
        batch of xyz vectors (vectorized, one shared rotation matrix),
      * copy, binary streaming and object printing like the other classes.

    The quaternion is kept normalized after every construction so vector
    rotation is always metric. yaw/pitch/roll follow the ping convention:
    yaw about z (down, 0 deg = north), pitch about y (starboard, positive
    = bow up), roll about x (forward, positive = port up); rotations are
    applied yaw, then pitch, then roll.

    Template Args:
        t_float: floating point type of the quaternion coefficients (float
                 or double).
    """

    @overload
    def __init__(self) -> None:
        """Construct an identity rotation (no rotation)."""

    @overload
    def __init__(self, ypr: Sequence[float], input_in_degrees: bool = True) -> None:
        """
        Construct a Rotation from yaw, pitch and roll (implicit).

        Args:
            ypr: array containing {yaw, pitch, roll}.
            input_in_degrees: if true (default) yaw/pitch/roll are in degrees,
                              otherwise radians.
        """

    @overload
    def __init__(self, yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> None:
        """
        Construct a Rotation from yaw, pitch and roll.

        Args:
            yaw: rotation around z (down) [deg or rad], 0 deg = north.
            pitch: rotation around y (starboard) [deg or rad], positive = bow
                   up.
            roll: rotation around x (forward) [deg or rad], positive = port
                  up.
            input_in_degrees: if true (default) yaw/pitch/roll are in degrees,
                              otherwise radians.
        """

    @staticmethod
    def from_quaternion(w: float, x: float, y: float, z: float) -> RotationD:
        """
        Build a Rotation from raw quaternion coefficients (w, x, y, z).

        Args:
            w: scalar (real) part.
            x: i coefficient.
            y: j coefficient.
            z: k coefficient.

        Returns:
            normalized Rotation.
        """

    @overload
    @staticmethod
    def from_ypr(yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> RotationD:
        """
        Build a Rotation from yaw, pitch and roll.
        Args:
            yaw: rotation around z (down) [deg or rad].
            pitch: rotation around y (starboard) [deg or rad].
            roll: rotation around x (forward) [deg or rad].
            input_in_degrees: if true (default) inputs are degrees, otherwise
                              radians.

        Returns:
            normalized Rotation.
        """

    @overload
    @staticmethod
    def from_ypr(ypr: Sequence[float], input_in_degrees: bool = True) -> RotationD:
        """
        Build a Rotation from a {yaw, pitch, roll} array.
        Args:
            ypr: array containing {yaw, pitch, roll}.
            input_in_degrees: if true (default) inputs are degrees, otherwise
                              radians.

        Returns:
            normalized Rotation.
        """

    @overload
    @staticmethod
    def from_rpy(roll: float, pitch: float, yaw: float, input_in_degrees: bool = True) -> RotationD:
        """
        Build a Rotation from roll, pitch and yaw.
        Args:
            roll: rotation around x (forward) [deg or rad].
            pitch: rotation around y (starboard) [deg or rad].
            yaw: rotation around z (down) [deg or rad].
            input_in_degrees: if true (default) inputs are degrees, otherwise
                              radians.

        Returns:
            normalized Rotation.
        """

    @overload
    @staticmethod
    def from_rpy(rpy: Sequence[float], input_in_degrees: bool = True) -> RotationD:
        """
        Build a Rotation from a {roll, pitch, yaw} array.
        Args:
            rpy: array containing {roll, pitch, yaw}.
            input_in_degrees: if true (default) inputs are degrees, otherwise
                              radians.

        Returns:
            normalized Rotation.
        """

    def ypr(self, output_in_degrees: bool = True) -> list[float]:
        """
        Extract yaw, pitch and roll from the rotation.
        Args:
            output_in_degrees: if true (default) the output is in degrees,
                               otherwise radians.

        Returns:
            array containing {yaw, pitch, roll}.
        """

    def rpy(self, output_in_degrees: bool = True) -> list[float]:
        """
        Extract roll, pitch and yaw from the rotation.
        Args:
            output_in_degrees: if true (default) the output is in degrees,
                               otherwise radians.

        Returns:
            array containing {roll, pitch, yaw}.
        """

    def wxyz(self) -> list[float]:
        """
        Get the raw quaternion coefficients as {w, x, y, z}.
        Returns:
            array containing {w, x, y, z}.
        """

    @overload
    def rotate(self, x: float, y: float, z: float) -> list[float]:
        """
        Rotate a single 3D vector by this rotation.
        Args:
            x: x component (forward).
            y: y component (starboard).
            z: z component (down).

        Returns:
            the rotated {x, y, z} vector.
        """

    @overload
    def rotate(self, xyz: Sequence[float]) -> list[float]:
        """
        Rotate a single 3D vector by this rotation.
        Args:
            xyz: the {x, y, z} vector to rotate.

        Returns:
            the rotated {x, y, z} vector.
        """

    @overload
    def rotate(self, rotation: RotationD) -> RotationD:
        """
        Rotate (compose with) another rotation: apply this rotation to
        ``rotation.``
        Args:
            rotation: the rotation to be rotated.

        Returns:
            the combined rotation (this * rotation).
        """

    @overload
    def rotate(self, points: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]) -> Annotated[NDArray[numpy.float64], dict(order='C')]:
        """
        Rotate a batch of 3D vectors by this rotation (vectorized).

        The rotation matrix is built once and applied to every row, which is
        the fast path for rotating many points by the same rotation.

        Args:
            points: [n, 3] tensor of (x, y, z) row vectors.

        Returns:
            [n, 3] tensor of rotated row vectors.

        Raises:
            std::invalid_argument: if the second dimension is not 3.
        """

    def __eq__(self, other: RotationD) -> bool:
        """
        Two rotations are equal if their quaternions describe the same
        orientation (q == -q).
        """

    def __mul__(self, other: RotationD) -> RotationD: ...

    def copy(self) -> RotationD:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RotationD: ...

    def __deepcopy__(self, arg: dict, /) -> RotationD: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RotationD:
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
