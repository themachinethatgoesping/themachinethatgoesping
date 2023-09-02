"""
Convenient functions for converting latlon and utm strings.
"""
from __future__ import annotations
import typing
__all__ = ['degrees', 'latitude_to_string', 'latlon_to_utm', 'longitude_to_string', 'minutes', 'seconds', 't_latlon_format', 'utm_to_latlon']
class t_latlon_format:
    """
    lat/lon format specifications
    
    Members:
    
      degrees
    
      minutes
    
      seconds
    """
    __members__: typing.ClassVar[dict[str, t_latlon_format]]  # value = {'degrees': <t_latlon_format.degrees: 0>, 'minutes': <t_latlon_format.minutes: 1>, 'seconds': <t_latlon_format.seconds: 2>}
    degrees: typing.ClassVar[t_latlon_format]  # value = <t_latlon_format.degrees: 0>
    minutes: typing.ClassVar[t_latlon_format]  # value = <t_latlon_format.minutes: 1>
    seconds: typing.ClassVar[t_latlon_format]  # value = <t_latlon_format.seconds: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    @typing.overload
    def __init__(self, value: int) -> None:
        ...
    @typing.overload
    def __init__(self, str: str) -> None:
        """
        Construct this enum type from string
        """
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def str(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
@typing.overload
def latitude_to_string(latitude: float, format: t_latlon_format = ..., precision: int = ...) -> str:
    """
    convert a latitude value to a string
    
    Parameter ``latitude``:
        value to be converted
    
    Parameter ``precision``:
        number of digits behind the .
    
    Parameter ``format``:
        latlon format (degrees°N/S, degrees°minutes'N/S or
        degrees°minutes'seconds''N/S)
    
    Returns:
        converted latitude string
    """
@typing.overload
def latitude_to_string(latitude: list[float], format: t_latlon_format = ..., precision: int = ...) -> list[str]:
    """
    convert a latitude value to a string
    
    Parameter ``latitude``:
        value to be converted
    
    Parameter ``precision``:
        number of digits behind the .
    
    Parameter ``format``:
        latlon format (degrees°N/S, degrees°minutes'N/S or
        degrees°minutes'seconds''N/S)
    
    Returns:
        converted latitude string
    """
def latlon_to_utm(latitude: list[float], longitude: list[float], setzone: int) -> tuple[list[float], list[float], int, bool]:
    ...
@typing.overload
def longitude_to_string(longitude: float, format: t_latlon_format = ..., precision: int = ...) -> str:
    """
    convert a latitude value to a string
    
    Parameter ``latitude``:
        value to be converted
    
    Parameter ``precision``:
        number of digits behind the .
    
    Parameter ``format``:
        latlon format (degrees°N/S, degrees°minutes'N/S or
        degrees°minutes'seconds''N/S)
    
    Returns:
        converted latitude string
    """
@typing.overload
def longitude_to_string(longitude: list[float], format: t_latlon_format = ..., precision: int = ...) -> list[str]:
    """
    convert a latitude value to a string
    
    Parameter ``latitude``:
        value to be converted
    
    Parameter ``precision``:
        number of digits behind the .
    
    Parameter ``format``:
        latlon format (degrees°N/S, degrees°minutes'N/S or
        degrees°minutes'seconds''N/S)
    
    Returns:
        converted latitude string
    """
@typing.overload
def utm_to_latlon(northing: list[float], easting: list[float], zone: int, northern_hemisphere: bool) -> tuple[list[float], list[float]]:
    ...
@typing.overload
def utm_to_latlon(northing: list[float], easting: list[float], zone: list[int], northern_hemisphere: list[bool]) -> tuple[list[float], list[float]]:
    ...
degrees: t_latlon_format  # value = <t_latlon_format.degrees: 0>
minutes: t_latlon_format  # value = <t_latlon_format.minutes: 1>
seconds: t_latlon_format  # value = <t_latlon_format.seconds: 2>
