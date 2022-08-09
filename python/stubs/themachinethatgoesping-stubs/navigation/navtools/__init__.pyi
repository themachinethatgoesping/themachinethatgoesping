"""Convenient functions for converting latlon and utm strings."""
from __future__ import annotations
import themachinethatgoesping.navigation.navtools
import typing

__all__ = [
    "degrees",
    "latitude_to_string",
    "latlon_to_utm",
    "longitude_to_string",
    "minutes",
    "seconds",
    "t_latlon_format",
    "utm_to_latlon"
]


class t_latlon_format():
    """
    lat/lon format specifications

    Members:

      degrees

      minutes

      seconds
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    @typing.overload
    def __init__(self, str: str) -> None: 
        """
        Construct this enum type from string
        """
    @typing.overload
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'degrees': <t_latlon_format.degrees: 0>, 'minutes': <t_latlon_format.minutes: 1>, 'seconds': <t_latlon_format.seconds: 2>}
    degrees: themachinethatgoesping.navigation.navtools.t_latlon_format # value = <t_latlon_format.degrees: 0>
    minutes: themachinethatgoesping.navigation.navtools.t_latlon_format # value = <t_latlon_format.minutes: 1>
    seconds: themachinethatgoesping.navigation.navtools.t_latlon_format # value = <t_latlon_format.seconds: 2>
    pass
@typing.overload
def latitude_to_string(latitude: float, format: t_latlon_format = t_latlon_format.minutes, precision: int = 6) -> str:
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
        converteds latitude string

    convert a latitude value to a string

    Parameter ``latitude``:
        value to be converted

    Parameter ``precision``:
        number of digits behind the .

    Parameter ``format``:
        latlon format (degrees°N/S, degrees°minutes'N/S or
        degrees°minutes'seconds''N/S)

    Returns:
        converteds latitude string
    """
@typing.overload
def latitude_to_string(latitude: typing.List[float], format: t_latlon_format = t_latlon_format.minutes, precision: int = 6) -> typing.List[str]:
    pass
def latlon_to_utm(latitude: typing.List[float], longitude: typing.List[float], setzone: int) -> typing.Tuple[typing.List[float], typing.List[float], int, bool]:
    pass
@typing.overload
def longitude_to_string(longitude: float, format: t_latlon_format = t_latlon_format.minutes, precision: int = 6) -> str:
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
def longitude_to_string(longitude: typing.List[float], format: t_latlon_format = t_latlon_format.minutes, precision: int = 6) -> typing.List[str]:
    pass
@typing.overload
def utm_to_latlon(northing: typing.List[float], easting: typing.List[float], zone: int, northern_hemisphere: bool) -> typing.Tuple[typing.List[float], typing.List[float]]:
    pass
@typing.overload
def utm_to_latlon(northing: typing.List[float], easting: typing.List[float], zone: typing.List[int], northern_hemisphere: typing.List[bool]) -> typing.Tuple[typing.List[float], typing.List[float]]:
    pass
degrees: themachinethatgoesping.navigation.navtools.t_latlon_format # value = <t_latlon_format.degrees: 0>
minutes: themachinethatgoesping.navigation.navtools.t_latlon_format # value = <t_latlon_format.minutes: 1>
seconds: themachinethatgoesping.navigation.navtools.t_latlon_format # value = <t_latlon_format.seconds: 2>
