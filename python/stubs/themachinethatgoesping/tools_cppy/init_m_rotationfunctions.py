"""
functions for rotating coordinates using libeigen quaternions
"""
from __future__ import annotations
import numpy
import pybind11_stubgen.typing_ext
import typing
__all__ = ['quaternion_from_rpy', 'quaternion_from_ypr', 'rotateXYZ', 'rpy_from_quaternion', 'ypr_from_quaternion']
@typing.overload
def quaternion_from_rpy(rpy: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> ...:
    """
    create an eigen quaternion by rotating roll (x axis), pitch (y axis)
    and yaw (z axis)
    
    Template parameter ``t_float``:
        $Parameter ``rpy``:
    
    array that contains roll, pitch and yaw value
    
    Parameter ``input_in_degrees``:
        if true, roll, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(roll: float, pitch: float, yaw: float, input_in_degrees: bool = True) -> ...:
    """
    create an eigen quaternion by rotating roll (x axis), pitch (y axis)
    and yaw (z axis)
    
    Template parameter ``t_float``:
        $Parameter ``rpy``:
    
    array that contains roll, pitch and yaw value
    
    Parameter ``input_in_degrees``:
        if true, roll, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(RPY: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> list[..., ...]:
    """
    create an eigen quaternion by rotating roll (x axis), pitch (y axis)
    and yaw (z axis)
    
    Template parameter ``t_float``:
        $Parameter ``rpy``:
    
    array that contains roll, pitch and yaw value
    
    Parameter ``input_in_degrees``:
        if true, roll, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(roll: list[float], pitch: list[float], yaw: list[float], input_in_degrees: bool = True) -> list[..., ...]:
    """
    create an eigen quaternion by rotating roll (x axis), pitch (y axis)
    and yaw (z axis)
    
    Template parameter ``t_float``:
        $Parameter ``rpy``:
    
    array that contains roll, pitch and yaw value
    
    Parameter ``input_in_degrees``:
        if true, roll, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(rpy: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> ...:
    """
    create an eigen quaternion by rotating roll (x axis), pitch (y axis)
    and yaw (z axis)
    
    Template parameter ``t_float``:
        $Parameter ``rpy``:
    
    array that contains roll, pitch and yaw value
    
    Parameter ``input_in_degrees``:
        if true, roll, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(roll: float, pitch: float, yaw: float, input_in_degrees: bool = True) -> ...:
    """
    create an eigen quaternion by rotating roll (x axis), pitch (y axis)
    and yaw (z axis)
    
    Template parameter ``t_float``:
        $Parameter ``rpy``:
    
    array that contains roll, pitch and yaw value
    
    Parameter ``input_in_degrees``:
        if true, roll, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(RPY: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> list[..., ...]:
    """
    create an eigen quaternion by rotating roll (x axis), pitch (y axis)
    and yaw (z axis)
    
    Template parameter ``t_float``:
        $Parameter ``rpy``:
    
    array that contains roll, pitch and yaw value
    
    Parameter ``input_in_degrees``:
        if true, roll, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_rpy(roll: list[float], pitch: list[float], yaw: list[float], input_in_degrees: bool = True) -> list[..., ...]:
    """
    create an eigen quaternion by rotating roll (x axis), pitch (y axis)
    and yaw (z axis)
    
    Template parameter ``t_float``:
        $Parameter ``rpy``:
    
    array that contains roll, pitch and yaw value
    
    Parameter ``input_in_degrees``:
        if true, roll, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(ypr: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> ...:
    """
    create an eigen quaternion by rotating yaw (z axis), pitch (y axis)
    and roll (x axis)
    
    Template parameter ``t_float``:
        $Parameter ``ypr``:
    
    array that contains yaw, pitch and roll value
    
    Parameter ``input_in_degrees``:
        if true, yaw, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> ...:
    """
    create an eigen quaternion by rotating yaw (z axis), pitch (y axis)
    and roll (x axis)
    
    Template parameter ``t_float``:
        $Parameter ``ypr``:
    
    array that contains yaw, pitch and roll value
    
    Parameter ``input_in_degrees``:
        if true, yaw, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> list[..., ...]:
    """
    create an eigen quaternion by rotating yaw (z axis), pitch (y axis)
    and roll (x axis)
    
    Template parameter ``t_float``:
        $Parameter ``ypr``:
    
    array that contains yaw, pitch and roll value
    
    Parameter ``input_in_degrees``:
        if true, yaw, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(yaw: list[float], pitch: list[float], roll: list[float], input_in_degrees: bool = True) -> list[..., ...]:
    """
    create an eigen quaternion by rotating yaw (z axis), pitch (y axis)
    and roll (x axis)
    
    Template parameter ``t_float``:
        $Parameter ``ypr``:
    
    array that contains yaw, pitch and roll value
    
    Parameter ``input_in_degrees``:
        if true, yaw, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(ypr: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], input_in_degrees: bool = True) -> ...:
    """
    create an eigen quaternion by rotating yaw (z axis), pitch (y axis)
    and roll (x axis)
    
    Template parameter ``t_float``:
        $Parameter ``ypr``:
    
    array that contains yaw, pitch and roll value
    
    Parameter ``input_in_degrees``:
        if true, yaw, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(yaw: float, pitch: float, roll: float, input_in_degrees: bool = True) -> ...:
    """
    create an eigen quaternion by rotating yaw (z axis), pitch (y axis)
    and roll (x axis)
    
    Template parameter ``t_float``:
        $Parameter ``ypr``:
    
    array that contains yaw, pitch and roll value
    
    Parameter ``input_in_degrees``:
        if true, yaw, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(YPR: list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]], input_in_degrees: bool = True) -> list[..., ...]:
    """
    create an eigen quaternion by rotating yaw (z axis), pitch (y axis)
    and roll (x axis)
    
    Template parameter ``t_float``:
        $Parameter ``ypr``:
    
    array that contains yaw, pitch and roll value
    
    Parameter ``input_in_degrees``:
        if true, yaw, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def quaternion_from_ypr(yaw: list[float], pitch: list[float], roll: list[float], input_in_degrees: bool = True) -> list[..., ...]:
    """
    create an eigen quaternion by rotating yaw (z axis), pitch (y axis)
    and roll (x axis)
    
    Template parameter ``t_float``:
        $Parameter ``ypr``:
    
    array that contains yaw, pitch and roll value
    
    Parameter ``input_in_degrees``:
        if true, yaw, pitch and roll input values are in ° otherwise rad
    
    Returns:
        EigenQuaternion<t_float>
    """
@typing.overload
def rotateXYZ(*args, **kwargs) -> numpy.ndarray[numpy.float32[3, 1]]:
    """
    OVERLOADED rotateXYZ: rotates a x,y,z vector with the passed
    parameters roll, pitch, yaw as a Quaternion
    
    Parameter ``q:``:
        roll, pitch, yaw as Quaternion<t_float>
    
    Parameter ``x:``:
        x as double
    
    Parameter ``y:``:
        y as double
    
    Parameter ``z:``:
        z as double
    
    Returns:
        returns vector with rotated xyz
    """
@typing.overload
def rotateXYZ(*args, **kwargs) -> numpy.ndarray[numpy.float32[3, 1]]:
    """
    OVERLOADED rotateXYZ: rotates a x,y,z vector with the passed
    parameters roll, pitch, yaw as a Quaternion
    
    Parameter ``q:``:
        roll, pitch, yaw as Quaternion<t_float>
    
    Parameter ``x:``:
        x as double
    
    Parameter ``y:``:
        y as double
    
    Parameter ``z:``:
        z as double
    
    Returns:
        returns vector with rotated xyz
    """
@typing.overload
def rotateXYZ(*args, **kwargs) -> numpy.ndarray[numpy.float64[3, 1]]:
    """
    OVERLOADED rotateXYZ: rotates a x,y,z vector with the passed
    parameters roll, pitch, yaw as a Quaternion
    
    Parameter ``q:``:
        roll, pitch, yaw as Quaternion<t_float>
    
    Parameter ``x:``:
        x as double
    
    Parameter ``y:``:
        y as double
    
    Parameter ``z:``:
        z as double
    
    Returns:
        returns vector with rotated xyz
    """
@typing.overload
def rotateXYZ(*args, **kwargs) -> numpy.ndarray[numpy.float64[3, 1]]:
    """
    OVERLOADED rotateXYZ: rotates a x,y,z vector with the passed
    parameters roll, pitch, yaw as a Quaternion
    
    Parameter ``q:``:
        roll, pitch, yaw as Quaternion<t_float>
    
    Parameter ``x:``:
        x as double
    
    Parameter ``y:``:
        y as double
    
    Parameter ``z:``:
        z as double
    
    Returns:
        returns vector with rotated xyz
    """
@typing.overload
def rpy_from_quaternion(*args, **kwargs) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
    """
    Convert quaternion to roll, pitch and yaw
    
    Template parameter ``t_float``:
        $Parameter ``q``:
    
    quaternion
    
    Parameter ``output_to_degrees``:
        if true, roll, pitch and yaw input values are in ° otherwise rad
    
    Returns:
        std::array<t_float, 3> roll, pitch and yaw
    """
@typing.overload
def rpy_from_quaternion(Q: list[..., ...], output_to_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
    """
    Convert quaternion to roll, pitch and yaw
    
    Template parameter ``t_float``:
        $Parameter ``q``:
    
    quaternion
    
    Parameter ``output_to_degrees``:
        if true, roll, pitch and yaw input values are in ° otherwise rad
    
    Returns:
        std::array<t_float, 3> roll, pitch and yaw
    """
@typing.overload
def rpy_from_quaternion(*args, **kwargs) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
    """
    Convert quaternion to roll, pitch and yaw
    
    Template parameter ``t_float``:
        $Parameter ``q``:
    
    quaternion
    
    Parameter ``output_to_degrees``:
        if true, roll, pitch and yaw input values are in ° otherwise rad
    
    Returns:
        std::array<t_float, 3> roll, pitch and yaw
    """
@typing.overload
def rpy_from_quaternion(Q: list[..., ...], output_to_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
    """
    Convert quaternion to roll, pitch and yaw
    
    Template parameter ``t_float``:
        $Parameter ``q``:
    
    quaternion
    
    Parameter ``output_to_degrees``:
        if true, roll, pitch and yaw input values are in ° otherwise rad
    
    Returns:
        std::array<t_float, 3> roll, pitch and yaw
    """
@typing.overload
def ypr_from_quaternion(*args, **kwargs) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
    """
    Convert quaternion to yaw, pitch and roll
    
    Template parameter ``t_float``:
        $Parameter ``q``:
    
    quaternion
    
    Parameter ``output_to_degrees``:
        if true, yaw, pitch and roll input values are in ° otherwise rad
    
    Returns:
        std::array<t_float, 3> yaw, pitch and roll
    """
@typing.overload
def ypr_from_quaternion(Q: list[..., ...], output_to_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
    """
    Convert quaternion to yaw, pitch and roll
    
    Template parameter ``t_float``:
        $Parameter ``q``:
    
    quaternion
    
    Parameter ``output_to_degrees``:
        if true, yaw, pitch and roll input values are in ° otherwise rad
    
    Returns:
        std::array<t_float, 3> yaw, pitch and roll
    """
@typing.overload
def ypr_from_quaternion(*args, **kwargs) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
    """
    Convert quaternion to yaw, pitch and roll
    
    Template parameter ``t_float``:
        $Parameter ``q``:
    
    quaternion
    
    Parameter ``output_to_degrees``:
        if true, yaw, pitch and roll input values are in ° otherwise rad
    
    Returns:
        std::array<t_float, 3> yaw, pitch and roll
    """
@typing.overload
def ypr_from_quaternion(Q: list[..., ...], output_to_degrees: bool = True) -> list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]]:
    """
    Convert quaternion to yaw, pitch and roll
    
    Template parameter ``t_float``:
        $Parameter ``q``:
    
    quaternion
    
    Parameter ``output_to_degrees``:
        if true, yaw, pitch and roll input values are in ° otherwise rad
    
    Returns:
        std::array<t_float, 3> yaw, pitch and roll
    """
