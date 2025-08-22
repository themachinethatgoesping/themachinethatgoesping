"""
functions for rotating coordinates using libeigen quaternions
"""
from __future__ import annotations
import numpy
import pybind11_stubgen.typing_ext
import typing
__all__: list[str] = ['quaternion_from_rpy', 'quaternion_from_ypr', 'rotateXYZ', 'rotateYPR', 'rpy_from_quaternion', 'ypr_from_quaternion']
@typing.overload
def quaternion_from_rpy(rpy: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> ...:
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
def quaternion_from_rpy(roll: float, pitch: float, yaw: float, input_in_degrees: bool = True) -> ...:
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
def quaternion_from_rpy(RPY: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> list[..., ...]:
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
def quaternion_from_rpy(roll: list[float], pitch: list[float], yaw: list[float], input_in_degrees: bool = True) -> list[..., ...]:
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
def quaternion_from_rpy(rpy: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> ...:
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
def quaternion_from_rpy(roll: float, pitch: float, yaw: float, input_in_degrees: bool = True) -> ...:
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
def quaternion_from_rpy(RPY: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> list[..., ...]:
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
def quaternion_from_rpy(roll: list[float], pitch: list[float], yaw: list[float], input_in_degrees: bool = True) -> list[..., ...]:
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
def quaternion_from_ypr(ypr: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> ...:
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
def quaternion_from_ypr(yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> ...:
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
def quaternion_from_ypr(YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> list[..., ...]:
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
def quaternion_from_ypr(yaw: list[float], pitch: list[float], roll: list[float], input_in_degrees: bool = True) -> list[..., ...]:
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
def quaternion_from_ypr(ypr: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> ...:
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
def quaternion_from_ypr(yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> ...:
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
def quaternion_from_ypr(YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> list[..., ...]:
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
def quaternion_from_ypr(yaw: list[float], pitch: list[float], roll: list[float], input_in_degrees: bool = True) -> list[..., ...]:
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
def rotateXYZ(*args, **kwargs) -> numpy.ndarray[numpy.float32[3, 1]]:
    """
    Rotate a 3D vector (x, y, z) by quaternion q.
    
    Template parameter ``t_float``:
        floating point type
    
    Returns:
        rotated vector
    """
@typing.overload
def rotateXYZ(*args, **kwargs) -> numpy.ndarray[numpy.float32[3, 1]]:
    """
    Rotate a 3D vector (x, y, z) by quaternion q.
    
    Template parameter ``t_float``:
        floating point type
    
    Returns:
        rotated vector
    """
@typing.overload
def rotateXYZ(*args, **kwargs) -> numpy.ndarray[numpy.float64[3, 1]]:
    """
    Rotate a 3D vector (x, y, z) by quaternion q.
    
    Template parameter ``t_float``:
        floating point type
    
    Returns:
        rotated vector
    """
@typing.overload
def rotateXYZ(*args, **kwargs) -> numpy.ndarray[numpy.float64[3, 1]]:
    """
    Rotate a 3D vector (x, y, z) by quaternion q.
    
    Template parameter ``t_float``:
        floating point type
    
    Returns:
        rotated vector
    """
@typing.overload
def rotateYPR(yaw1: float, pitch1: float, roll1: float, yaw2: float, pitch2: float, roll2: float, input_in_degrees: bool = True) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
    """
    Rotate yaw pitch roll angles by other yaw pitch and roll angles
    """
@typing.overload
def rotateYPR(yaw1: list[float], pitch1: list[float], roll1: list[float], yaw2: float, pitch2: float, roll2: float, input_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
    """
    Rotate yaw pitch roll angles by other yaw pitch and roll angles
    """
@typing.overload
def rotateYPR(yaw1: float, pitch1: float, roll1: float, yaw2: float, pitch2: float, roll2: float, input_in_degrees: bool = True) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
    """
    Rotate yaw pitch roll angles by other yaw pitch and roll angles
    """
@typing.overload
def rotateYPR(yaw1: list[float], pitch1: list[float], roll1: list[float], yaw2: float, pitch2: float, roll2: float, input_in_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
    """
    Rotate yaw pitch roll angles by other yaw pitch and roll angles
    """
@typing.overload
def rpy_from_quaternion(*args, **kwargs) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
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
def rpy_from_quaternion(Q: list[..., ...], output_to_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
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
def rpy_from_quaternion(*args, **kwargs) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
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
def rpy_from_quaternion(Q: list[..., ...], output_to_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
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
def ypr_from_quaternion(*args, **kwargs) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
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
def ypr_from_quaternion(Q: list[..., ...], output_to_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
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
def ypr_from_quaternion(*args, **kwargs) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
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
def ypr_from_quaternion(Q: list[..., ...], output_to_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
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
