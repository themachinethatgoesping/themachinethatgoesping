"""
Convenient functions for converting latlon and utm strings.
"""
from __future__ import annotations
import collections.abc
import numpy
import themachinethatgoesping.navigation.datastructures
import typing
__all__: list[str] = ['compute_latlon_distance_m', 'compute_latlon_distances_m', 'cumulative_latlon_distances_m', 'degrees', 'inplace_1', 'latitude_to_string', 'latlon_to_utm', 'longitude_to_string', 'minutes', 'o_latlon_format', 'seconds', 't_latlon_format', 'utm_to_latlon']
class o_latlon_format:
    """
    Helper class to convert between strings and enum values of type 't_latlon_format'
    """
    __default_value__: typing.ClassVar[t_latlon_format]  # value = <t_latlon_format.degrees: 0>
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_latlon_format:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> o_latlon_format:
        ...
    def __deepcopy__(self, arg0: dict) -> o_latlon_format:
        ...
    @typing.overload
    def __eq__(self, arg0: o_latlon_format) -> bool:
        ...
    @typing.overload
    def __eq__(self, arg0: t_latlon_format) -> bool:
        ...
    @typing.overload
    def __eq__(self, arg0: typing.SupportsInt) -> bool:
        ...
    @typing.overload
    def __eq__(self, arg0: str) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, value: t_latlon_format = ...) -> None:
        """
        Construct from enum value
        """
    @typing.overload
    def __init__(self, value: str) -> None:
        """
        Construct from string
        """
    @typing.overload
    def __init__(self, value: typing.SupportsInt) -> None:
        """
        Construct from string
        """
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __repr__(self) -> None:
        ...
    def __setstate__(self, arg0: bytes) -> None:
        ...
    @typing.overload
    def __str__(self) -> str:
        ...
    @typing.overload
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> o_latlon_format:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def value(self) -> t_latlon_format:
        """
        enum value
        """
    @value.setter
    def value(self, arg0: t_latlon_format) -> None:
        ...
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
    def __init__(self, value: typing.SupportsInt) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
@typing.overload
def compute_latlon_distance_m(lat1: typing.SupportsFloat, lon1: typing.SupportsFloat, lat2: typing.SupportsFloat, lon2: typing.SupportsFloat) -> float:
    """
    Compute the distance in meters between two latitude-longitude
    coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_float``:
        Floating-point type for latitude and longitude values.
    
    Parameter ``lat1``:
        Latitude of the first coordinate.
    
    Parameter ``lon1``:
        Longitude of the first coordinate.
    
    Parameter ``lat2``:
        Latitude of the second coordinate.
    
    Parameter ``lon2``:
        Longitude of the second coordinate.
    
    Returns:
        Distance between the two coordinates in meters.
    """
@typing.overload
def compute_latlon_distance_m(lat1: typing.SupportsFloat, lon1: typing.SupportsFloat, lat2: typing.SupportsFloat, lon2: typing.SupportsFloat) -> float:
    """
    Compute the distance in meters between two latitude-longitude
    coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_float``:
        Floating-point type for latitude and longitude values.
    
    Parameter ``lat1``:
        Latitude of the first coordinate.
    
    Parameter ``lon1``:
        Longitude of the first coordinate.
    
    Parameter ``lat2``:
        Latitude of the second coordinate.
    
    Parameter ``lon2``:
        Longitude of the second coordinate.
    
    Returns:
        Distance between the two coordinates in meters.
    """
@typing.overload
def compute_latlon_distance_m(geolocation_latlon_1: themachinethatgoesping.navigation.datastructures.GeolocationLatLon, geolocation_latlon_2: themachinethatgoesping.navigation.datastructures.GeolocationLatLon) -> float:
    """
    Compute the distance in meters between two latitude-longitude
    coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_float``:
        Floating-point type for latitude and longitude values.
    
    Parameter ``lat1``:
        Latitude of the first coordinate.
    
    Parameter ``lon1``:
        Longitude of the first coordinate.
    
    Parameter ``lat2``:
        Latitude of the second coordinate.
    
    Parameter ``lon2``:
        Longitude of the second coordinate.
    
    Returns:
        Distance between the two coordinates in meters.
    """
@typing.overload
def compute_latlon_distance_m(geolocation_latlon_1: themachinethatgoesping.navigation.datastructures.SensordataLatLon, geolocation_latlon_2: themachinethatgoesping.navigation.datastructures.SensordataLatLon) -> float:
    """
    Compute the distance in meters between two latitude-longitude
    coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_float``:
        Floating-point type for latitude and longitude values.
    
    Parameter ``lat1``:
        Latitude of the first coordinate.
    
    Parameter ``lon1``:
        Longitude of the first coordinate.
    
    Parameter ``lat2``:
        Latitude of the second coordinate.
    
    Parameter ``lon2``:
        Longitude of the second coordinate.
    
    Returns:
        Distance between the two coordinates in meters.
    """
@typing.overload
def compute_latlon_distance_m(geolocation_latlon_1: tuple[typing.SupportsFloat, typing.SupportsFloat], geolocation_latlon_2: tuple[typing.SupportsFloat, typing.SupportsFloat]) -> float:
    """
    Compute the distance in meters between two latitude-longitude
    coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_float``:
        Floating-point type for latitude and longitude values.
    
    Parameter ``lat1``:
        Latitude of the first coordinate.
    
    Parameter ``lon1``:
        Longitude of the first coordinate.
    
    Parameter ``lat2``:
        Latitude of the second coordinate.
    
    Parameter ``lon2``:
        Longitude of the second coordinate.
    
    Returns:
        Distance between the two coordinates in meters.
    """
@typing.overload
def compute_latlon_distance_m(geolocation_latlon_1: tuple[typing.SupportsFloat, typing.SupportsFloat], geolocation_latlon_2: tuple[typing.SupportsFloat, typing.SupportsFloat]) -> float:
    """
    Compute the distance in meters between two latitude-longitude
    coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_float``:
        Floating-point type for latitude and longitude values.
    
    Parameter ``lat1``:
        Latitude of the first coordinate.
    
    Parameter ``lon1``:
        Longitude of the first coordinate.
    
    Parameter ``lat2``:
        Latitude of the second coordinate.
    
    Parameter ``lon2``:
        Longitude of the second coordinate.
    
    Returns:
        Distance between the two coordinates in meters.
    """
@typing.overload
def compute_latlon_distances_m(latitudes: numpy.ndarray[numpy.float32], longitudes: numpy.ndarray[numpy.float32]) -> numpy.ndarray[numpy.float64]:
    """
    Compute the distances in meters between consecutive latitude-longitude
    coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_return_container``:
        Type of container to store the distances.
    
    Template parameter ``T_float_container``:
        Type of container that holds latitude and longitude values as
        floats.
    
    Parameter ``latitudes``:
        Vector of latitude values.
    
    Parameter ``longitudes``:
        Vector of longitude values.
    
    Returns:
        Vector of distances between consecutive coordinates in meters.
    """
@typing.overload
def compute_latlon_distances_m(latitudes: numpy.ndarray[numpy.float64], longitudes: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.float64]:
    """
    Compute the distances in meters between consecutive latitude-longitude
    coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_return_container``:
        Type of container to store the distances.
    
    Template parameter ``T_float_container``:
        Type of container that holds latitude and longitude values as
        floats.
    
    Parameter ``latitudes``:
        Vector of latitude values.
    
    Parameter ``longitudes``:
        Vector of longitude values.
    
    Returns:
        Vector of distances between consecutive coordinates in meters.
    """
@typing.overload
def compute_latlon_distances_m(geolocations_latlon: collections.abc.Sequence[themachinethatgoesping.navigation.datastructures.GeolocationLatLon]) -> numpy.ndarray[numpy.float64]:
    """
    Compute the distances in meters between consecutive latitude-longitude
    coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_return_container``:
        Type of container to store the distances.
    
    Template parameter ``T_float_container``:
        Type of container that holds latitude and longitude values as
        floats.
    
    Parameter ``latitudes``:
        Vector of latitude values.
    
    Parameter ``longitudes``:
        Vector of longitude values.
    
    Returns:
        Vector of distances between consecutive coordinates in meters.
    """
@typing.overload
def compute_latlon_distances_m(geolocations_latlon: collections.abc.Sequence[themachinethatgoesping.navigation.datastructures.SensordataLatLon]) -> numpy.ndarray[numpy.float64]:
    """
    Compute the distances in meters between consecutive latitude-longitude
    coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_return_container``:
        Type of container to store the distances.
    
    Template parameter ``T_float_container``:
        Type of container that holds latitude and longitude values as
        floats.
    
    Parameter ``latitudes``:
        Vector of latitude values.
    
    Parameter ``longitudes``:
        Vector of longitude values.
    
    Returns:
        Vector of distances between consecutive coordinates in meters.
    """
@typing.overload
def compute_latlon_distances_m(geolocations_latlon: collections.abc.Sequence[tuple[typing.SupportsFloat, typing.SupportsFloat]]) -> numpy.ndarray[numpy.float64]:
    """
    Compute the distances in meters between consecutive latitude-longitude
    coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_return_container``:
        Type of container to store the distances.
    
    Template parameter ``T_float_container``:
        Type of container that holds latitude and longitude values as
        floats.
    
    Parameter ``latitudes``:
        Vector of latitude values.
    
    Parameter ``longitudes``:
        Vector of longitude values.
    
    Returns:
        Vector of distances between consecutive coordinates in meters.
    """
@typing.overload
def compute_latlon_distances_m(geolocations_latlon: collections.abc.Sequence[tuple[typing.SupportsFloat, typing.SupportsFloat]]) -> numpy.ndarray[numpy.float64]:
    """
    Compute the distances in meters between consecutive latitude-longitude
    coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_return_container``:
        Type of container to store the distances.
    
    Template parameter ``T_float_container``:
        Type of container that holds latitude and longitude values as
        floats.
    
    Parameter ``latitudes``:
        Vector of latitude values.
    
    Parameter ``longitudes``:
        Vector of longitude values.
    
    Returns:
        Vector of distances between consecutive coordinates in meters.
    """
@typing.overload
def cumulative_latlon_distances_m(latitudes: numpy.ndarray[numpy.float32], longitudes: numpy.ndarray[numpy.float32]) -> numpy.ndarray[numpy.float64]:
    """
    Compute the cumulative distances in meters between consecutive
    latitude-longitude coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_return_container``:
        Type of container to store the distances.
    
    Template parameter ``T_float_container``:
        Type of container that holds latitude and longitude values as
        floats.
    
    Parameter ``latitudes``:
        Vector of latitude values.
    
    Parameter ``longitudes``:
        Vector of longitude values.
    
    Returns:
        Vector of cumulative distances between consecutive coordinates in
        meters.
    """
@typing.overload
def cumulative_latlon_distances_m(latitudes: numpy.ndarray[numpy.float64], longitudes: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.float64]:
    """
    Compute the cumulative distances in meters between consecutive
    latitude-longitude coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_return_container``:
        Type of container to store the distances.
    
    Template parameter ``T_float_container``:
        Type of container that holds latitude and longitude values as
        floats.
    
    Parameter ``latitudes``:
        Vector of latitude values.
    
    Parameter ``longitudes``:
        Vector of longitude values.
    
    Returns:
        Vector of cumulative distances between consecutive coordinates in
        meters.
    """
@typing.overload
def cumulative_latlon_distances_m(geolocations_latlon: collections.abc.Sequence[themachinethatgoesping.navigation.datastructures.GeolocationLatLon]) -> numpy.ndarray[numpy.float64]:
    """
    Compute the cumulative distances in meters between consecutive
    latitude-longitude coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_return_container``:
        Type of container to store the distances.
    
    Template parameter ``T_float_container``:
        Type of container that holds latitude and longitude values as
        floats.
    
    Parameter ``latitudes``:
        Vector of latitude values.
    
    Parameter ``longitudes``:
        Vector of longitude values.
    
    Returns:
        Vector of cumulative distances between consecutive coordinates in
        meters.
    """
@typing.overload
def cumulative_latlon_distances_m(geolocations_latlon: collections.abc.Sequence[themachinethatgoesping.navigation.datastructures.SensordataLatLon]) -> numpy.ndarray[numpy.float64]:
    """
    Compute the cumulative distances in meters between consecutive
    latitude-longitude coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_return_container``:
        Type of container to store the distances.
    
    Template parameter ``T_float_container``:
        Type of container that holds latitude and longitude values as
        floats.
    
    Parameter ``latitudes``:
        Vector of latitude values.
    
    Parameter ``longitudes``:
        Vector of longitude values.
    
    Returns:
        Vector of cumulative distances between consecutive coordinates in
        meters.
    """
@typing.overload
def cumulative_latlon_distances_m(geolocations_latlon: collections.abc.Sequence[tuple[typing.SupportsFloat, typing.SupportsFloat]]) -> numpy.ndarray[numpy.float64]:
    """
    Compute the cumulative distances in meters between consecutive
    latitude-longitude coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_return_container``:
        Type of container to store the distances.
    
    Template parameter ``T_float_container``:
        Type of container that holds latitude and longitude values as
        floats.
    
    Parameter ``latitudes``:
        Vector of latitude values.
    
    Parameter ``longitudes``:
        Vector of longitude values.
    
    Returns:
        Vector of cumulative distances between consecutive coordinates in
        meters.
    """
@typing.overload
def cumulative_latlon_distances_m(geolocations_latlon: collections.abc.Sequence[tuple[typing.SupportsFloat, typing.SupportsFloat]]) -> numpy.ndarray[numpy.float64]:
    """
    Compute the cumulative distances in meters between consecutive
    latitude-longitude coordinates using the WGS84 ellipsoid.
    
    Template parameter ``T_return_container``:
        Type of container to store the distances.
    
    Template parameter ``T_float_container``:
        Type of container that holds latitude and longitude values as
        floats.
    
    Parameter ``latitudes``:
        Vector of latitude values.
    
    Parameter ``longitudes``:
        Vector of longitude values.
    
    Returns:
        Vector of cumulative distances between consecutive coordinates in
        meters.
    """
def inplace_1(arg0: numpy.ndarray[numpy.float64]) -> None:
    ...
@typing.overload
def latitude_to_string(latitude: typing.SupportsFloat, format: o_latlon_format = ..., precision: typing.SupportsInt = 6) -> str:
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
def latitude_to_string(latitude: collections.abc.Sequence[typing.SupportsFloat], format: o_latlon_format = ..., precision: typing.SupportsInt = 6) -> list[str]:
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
def latlon_to_utm(latitude: numpy.ndarray[numpy.float64], longitude: numpy.ndarray[numpy.float64], setzone: typing.SupportsInt = -1, mp_cores: typing.SupportsInt = 1) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64], int, bool]:
    ...
@typing.overload
def longitude_to_string(longitude: typing.SupportsFloat, format: o_latlon_format = ..., precision: typing.SupportsInt = 6) -> str:
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
def longitude_to_string(longitude: collections.abc.Sequence[typing.SupportsFloat], format: o_latlon_format = ..., precision: typing.SupportsInt = 6) -> list[str]:
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
def utm_to_latlon(northing: numpy.ndarray[numpy.float64], easting: numpy.ndarray[numpy.float64], zone: typing.SupportsInt, northern_hemisphere: bool, mp_cores: typing.SupportsInt = 1) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
    ...
@typing.overload
def utm_to_latlon(northing: numpy.ndarray[numpy.float64], easting: numpy.ndarray[numpy.float64], zone: numpy.ndarray[numpy.int32], northern_hemisphere: numpy.ndarray[numpy.int32], mp_cores: typing.SupportsInt = 1) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
    ...
degrees: t_latlon_format  # value = <t_latlon_format.degrees: 0>
minutes: t_latlon_format  # value = <t_latlon_format.minutes: 1>
seconds: t_latlon_format  # value = <t_latlon_format.seconds: 2>
