"""Submodule that holds datastructures that hold the raytracing/georefrncing results"""
from __future__ import annotations
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import typing

__all__ = [
    "SamplelocationLocal"
]


class SamplelocationLocal():
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracing functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    def __copy__(self) -> SamplelocationLocal: ...
    def __deepcopy__(self, arg0: dict) -> SamplelocationLocal: ...
    def __eq__(self, other: SamplelocationLocal) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new sample location object (all values set to 0)

        Construct a new SamplelocationLocal object

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
    def copy(self) -> SamplelocationLocal: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SamplelocationLocal: 
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
