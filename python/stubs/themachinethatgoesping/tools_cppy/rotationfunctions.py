"""
functions for rotating coordinates using libeigen quaternions
"""
from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import typing
__all__: list[str] = ['quaternion_from_rpy', 'quaternion_from_ypr', 'rotateXYZ', 'rotateYPR', 'rpy_from_quaternion', 'ypr_from_quaternion']
@typing.overload
def quaternion_from_rpy(rpy: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat], "FixedSize(3)"], input_in_degrees: bool = True) -> ...:
    """
    Create an Eigen quaternion by rotating roll (X), pitch (Y) and yaw
    (Z).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``rpy``:
        array containing roll, pitch, yaw
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(roll: typing.SupportsFloat, pitch: typing.SupportsFloat, yaw: typing.SupportsFloat, input_in_degrees: bool = True) -> ...:
    """
    Create an Eigen quaternion by rotating roll (X), pitch (Y) and yaw
    (Z).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``rpy``:
        array containing roll, pitch, yaw
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(RPY: collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat], "FixedSize(3)"]], input_in_degrees: bool = True) -> list[..., ...]:
    """
    Create an Eigen quaternion by rotating roll (X), pitch (Y) and yaw
    (Z).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``rpy``:
        array containing roll, pitch, yaw
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(roll: collections.abc.Sequence[typing.SupportsFloat], pitch: collections.abc.Sequence[typing.SupportsFloat], yaw: collections.abc.Sequence[typing.SupportsFloat], input_in_degrees: bool = True) -> list[..., ...]:
    """
    Create an Eigen quaternion by rotating roll (X), pitch (Y) and yaw
    (Z).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``rpy``:
        array containing roll, pitch, yaw
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(rpy: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat], "FixedSize(3)"], input_in_degrees: bool = True) -> ...:
    """
    Create an Eigen quaternion by rotating roll (X), pitch (Y) and yaw
    (Z).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``rpy``:
        array containing roll, pitch, yaw
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(roll: typing.SupportsFloat, pitch: typing.SupportsFloat, yaw: typing.SupportsFloat, input_in_degrees: bool = True) -> ...:
    """
    Create an Eigen quaternion by rotating roll (X), pitch (Y) and yaw
    (Z).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``rpy``:
        array containing roll, pitch, yaw
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(RPY: collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat], "FixedSize(3)"]], input_in_degrees: bool = True) -> list[..., ...]:
    """
    Create an Eigen quaternion by rotating roll (X), pitch (Y) and yaw
    (Z).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``rpy``:
        array containing roll, pitch, yaw
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(roll: collections.abc.Sequence[typing.SupportsFloat], pitch: collections.abc.Sequence[typing.SupportsFloat], yaw: collections.abc.Sequence[typing.SupportsFloat], input_in_degrees: bool = True) -> list[..., ...]:
    """
    Create an Eigen quaternion by rotating roll (X), pitch (Y) and yaw
    (Z).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``rpy``:
        array containing roll, pitch, yaw
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(ypr: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat], "FixedSize(3)"], input_in_degrees: bool = True) -> ...:
    """
    Create an Eigen quaternion by rotating yaw (Z), pitch (Y) and roll
    (X).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``ypr``:
        array containing yaw, pitch, roll
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(yaw: typing.SupportsFloat, pitch: typing.SupportsFloat, roll: typing.SupportsFloat, input_in_degrees: bool = True) -> ...:
    """
    Create an Eigen quaternion by rotating yaw (Z), pitch (Y) and roll
    (X).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``ypr``:
        array containing yaw, pitch, roll
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(YPR: collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat], "FixedSize(3)"]], input_in_degrees: bool = True) -> list[..., ...]:
    """
    Create an Eigen quaternion by rotating yaw (Z), pitch (Y) and roll
    (X).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``ypr``:
        array containing yaw, pitch, roll
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(yaw: collections.abc.Sequence[typing.SupportsFloat], pitch: collections.abc.Sequence[typing.SupportsFloat], roll: collections.abc.Sequence[typing.SupportsFloat], input_in_degrees: bool = True) -> list[..., ...]:
    """
    Create an Eigen quaternion by rotating yaw (Z), pitch (Y) and roll
    (X).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``ypr``:
        array containing yaw, pitch, roll
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(ypr: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat], "FixedSize(3)"], input_in_degrees: bool = True) -> ...:
    """
    Create an Eigen quaternion by rotating yaw (Z), pitch (Y) and roll
    (X).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``ypr``:
        array containing yaw, pitch, roll
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(yaw: typing.SupportsFloat, pitch: typing.SupportsFloat, roll: typing.SupportsFloat, input_in_degrees: bool = True) -> ...:
    """
    Create an Eigen quaternion by rotating yaw (Z), pitch (Y) and roll
    (X).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``ypr``:
        array containing yaw, pitch, roll
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(YPR: collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat], "FixedSize(3)"]], input_in_degrees: bool = True) -> list[..., ...]:
    """
    Create an Eigen quaternion by rotating yaw (Z), pitch (Y) and roll
    (X).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``ypr``:
        array containing yaw, pitch, roll
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(yaw: collections.abc.Sequence[typing.SupportsFloat], pitch: collections.abc.Sequence[typing.SupportsFloat], roll: collections.abc.Sequence[typing.SupportsFloat], input_in_degrees: bool = True) -> list[..., ...]:
    """
    Create an Eigen quaternion by rotating yaw (Z), pitch (Y) and roll
    (X).
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``ypr``:
        array containing yaw, pitch, roll
    
    Parameter ``input_in_degrees``:
        if true, inputs are degrees; otherwise radians
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def rotateXYZ(*args, **kwargs) -> typing.Annotated[numpy.typing.NDArray[numpy.float32], "[3, 1]"]:
    """
    Rotate a 3D vector (x, y, z) by quaternion q.
    
    Template parameter ``t_float``:
        floating point type
    
    Returns:
        rotated vector
    """
@typing.overload
def rotateXYZ(*args, **kwargs) -> typing.Annotated[numpy.typing.NDArray[numpy.float32], "[3, 1]"]:
    """
    Rotate a 3D vector (x, y, z) by quaternion q.
    
    Template parameter ``t_float``:
        floating point type
    
    Returns:
        rotated vector
    """
@typing.overload
def rotateXYZ(*args, **kwargs) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]:
    """
    Rotate a 3D vector (x, y, z) by quaternion q.
    
    Template parameter ``t_float``:
        floating point type
    
    Returns:
        rotated vector
    """
@typing.overload
def rotateXYZ(*args, **kwargs) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]:
    """
    Rotate a 3D vector (x, y, z) by quaternion q.
    
    Template parameter ``t_float``:
        floating point type
    
    Returns:
        rotated vector
    """
@typing.overload
def rotateYPR(yaw1: typing.SupportsFloat, pitch1: typing.SupportsFloat, roll1: typing.SupportsFloat, yaw2: typing.SupportsFloat, pitch2: typing.SupportsFloat, roll2: typing.SupportsFloat, input_in_degrees: bool = True) -> typing.Annotated[list[float], "FixedSize(3)"]:
    """
    Rotate yaw pitch roll angles by other yaw pitch and roll angles
    """
@typing.overload
def rotateYPR(yaw1: collections.abc.Sequence[typing.SupportsFloat], pitch1: collections.abc.Sequence[typing.SupportsFloat], roll1: collections.abc.Sequence[typing.SupportsFloat], yaw2: typing.SupportsFloat, pitch2: typing.SupportsFloat, roll2: typing.SupportsFloat, input_in_degrees: bool = True) -> list[typing.Annotated[list[float], "FixedSize(3)"]]:
    """
    Rotate yaw pitch roll angles by other yaw pitch and roll angles
    """
@typing.overload
def rotateYPR(yaw1: typing.SupportsFloat, pitch1: typing.SupportsFloat, roll1: typing.SupportsFloat, yaw2: typing.SupportsFloat, pitch2: typing.SupportsFloat, roll2: typing.SupportsFloat, input_in_degrees: bool = True) -> typing.Annotated[list[float], "FixedSize(3)"]:
    """
    Rotate yaw pitch roll angles by other yaw pitch and roll angles
    """
@typing.overload
def rotateYPR(yaw1: collections.abc.Sequence[typing.SupportsFloat], pitch1: collections.abc.Sequence[typing.SupportsFloat], roll1: collections.abc.Sequence[typing.SupportsFloat], yaw2: typing.SupportsFloat, pitch2: typing.SupportsFloat, roll2: typing.SupportsFloat, input_in_degrees: bool = True) -> list[typing.Annotated[list[float], "FixedSize(3)"]]:
    """
    Rotate yaw pitch roll angles by other yaw pitch and roll angles
    """
@typing.overload
def rpy_from_quaternion(*args, **kwargs) -> typing.Annotated[list[float], "FixedSize(3)"]:
    """
    Convert quaternion to roll, pitch, yaw.
    
    Pitch is constrained to [-90°, 90°) to avoid ambiguities and gimbal
    lock notes apply.
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``q``:
        quaternion
    
    Parameter ``output_to_degrees``:
        if true, outputs are degrees; otherwise radians
    
    Returns:
        {roll, pitch, yaw}
    """
@typing.overload
def rpy_from_quaternion(Q: collections.abc.Sequence[..., ...], output_to_degrees: bool = True) -> list[typing.Annotated[list[float], "FixedSize(3)"]]:
    """
    Convert quaternion to roll, pitch, yaw.
    
    Pitch is constrained to [-90°, 90°) to avoid ambiguities and gimbal
    lock notes apply.
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``q``:
        quaternion
    
    Parameter ``output_to_degrees``:
        if true, outputs are degrees; otherwise radians
    
    Returns:
        {roll, pitch, yaw}
    """
@typing.overload
def rpy_from_quaternion(*args, **kwargs) -> typing.Annotated[list[float], "FixedSize(3)"]:
    """
    Convert quaternion to roll, pitch, yaw.
    
    Pitch is constrained to [-90°, 90°) to avoid ambiguities and gimbal
    lock notes apply.
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``q``:
        quaternion
    
    Parameter ``output_to_degrees``:
        if true, outputs are degrees; otherwise radians
    
    Returns:
        {roll, pitch, yaw}
    """
@typing.overload
def rpy_from_quaternion(Q: collections.abc.Sequence[..., ...], output_to_degrees: bool = True) -> list[typing.Annotated[list[float], "FixedSize(3)"]]:
    """
    Convert quaternion to roll, pitch, yaw.
    
    Pitch is constrained to [-90°, 90°) to avoid ambiguities and gimbal
    lock notes apply.
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``q``:
        quaternion
    
    Parameter ``output_to_degrees``:
        if true, outputs are degrees; otherwise radians
    
    Returns:
        {roll, pitch, yaw}
    """
@typing.overload
def ypr_from_quaternion(*args, **kwargs) -> typing.Annotated[list[float], "FixedSize(3)"]:
    """
    Convert quaternion to yaw, pitch, roll.
    
    Pitch is constrained to [-90°, 90°) to avoid ambiguities and gimbal
    lock notes apply.
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``q``:
        quaternion
    
    Parameter ``output_to_degrees``:
        if true, outputs are degrees; otherwise radians
    
    Returns:
        {yaw, pitch, roll}
    """
@typing.overload
def ypr_from_quaternion(Q: collections.abc.Sequence[..., ...], output_to_degrees: bool = True) -> list[typing.Annotated[list[float], "FixedSize(3)"]]:
    """
    Convert quaternion to yaw, pitch, roll.
    
    Pitch is constrained to [-90°, 90°) to avoid ambiguities and gimbal
    lock notes apply.
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``q``:
        quaternion
    
    Parameter ``output_to_degrees``:
        if true, outputs are degrees; otherwise radians
    
    Returns:
        {yaw, pitch, roll}
    """
@typing.overload
def ypr_from_quaternion(*args, **kwargs) -> typing.Annotated[list[float], "FixedSize(3)"]:
    """
    Convert quaternion to yaw, pitch, roll.
    
    Pitch is constrained to [-90°, 90°) to avoid ambiguities and gimbal
    lock notes apply.
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``q``:
        quaternion
    
    Parameter ``output_to_degrees``:
        if true, outputs are degrees; otherwise radians
    
    Returns:
        {yaw, pitch, roll}
    """
@typing.overload
def ypr_from_quaternion(Q: collections.abc.Sequence[..., ...], output_to_degrees: bool = True) -> list[typing.Annotated[list[float], "FixedSize(3)"]]:
    """
    Convert quaternion to yaw, pitch, roll.
    
    Pitch is constrained to [-90°, 90°) to avoid ambiguities and gimbal
    lock notes apply.
    
    Template parameter ``t_float``:
        floating point type
    
    Parameter ``q``:
        quaternion
    
    Parameter ``output_to_degrees``:
        if true, outputs are degrees; otherwise radians
    
    Returns:
        {yaw, pitch, roll}
    """
