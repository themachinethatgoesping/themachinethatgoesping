"""
Convenient functions for converting latlon and utm strings.
"""
from __future__ import annotations
import numpy
import themachinethatgoesping.navigation.datastructures
import typing
__all__: list[str] = ['compute_latlon_distance_m', 'compute_latlon_distances_m', 'cumulative_latlon_distances_m', 'degrees', 'latitude_to_string', 'latlon_to_utm', 'longitude_to_string', 'minutes', 'seconds', 't_latlon_format', 'utm_to_latlon']
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
def compute_latlon_distance_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
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
def compute_latlon_distance_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
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
def compute_latlon_distance_m(geolocation_latlon_1: tuple[float, float], geolocation_latlon_2: tuple[float, float]) -> float:
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
def compute_latlon_distance_m(geolocation_latlon_1: tuple[float, float], geolocation_latlon_2: tuple[float, float]) -> float:
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
def compute_latlon_distances_m(geolocations_latlon: list[themachinethatgoesping.navigation.datastructures.GeolocationLatLon]) -> numpy.ndarray[numpy.float64]:
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
def compute_latlon_distances_m(geolocations_latlon: list[themachinethatgoesping.navigation.datastructures.SensordataLatLon]) -> numpy.ndarray[numpy.float64]:
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
def compute_latlon_distances_m(geolocations_latlon: list[tuple[float, float]]) -> numpy.ndarray[numpy.float64]:
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
def compute_latlon_distances_m(geolocations_latlon: list[tuple[float, float]]) -> numpy.ndarray[numpy.float64]:
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
def cumulative_latlon_distances_m(geolocations_latlon: list[themachinethatgoesping.navigation.datastructures.GeolocationLatLon]) -> numpy.ndarray[numpy.float64]:
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
def cumulative_latlon_distances_m(geolocations_latlon: list[themachinethatgoesping.navigation.datastructures.SensordataLatLon]) -> numpy.ndarray[numpy.float64]:
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
def cumulative_latlon_distances_m(geolocations_latlon: list[tuple[float, float]]) -> numpy.ndarray[numpy.float64]:
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
def cumulative_latlon_distances_m(geolocations_latlon: list[tuple[float, float]]) -> numpy.ndarray[numpy.float64]:
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
def latitude_to_string(latitude: float, format: t_latlon_format = ..., precision: int = 6) -> str:
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
def latitude_to_string(latitude: list[float], format: t_latlon_format = ..., precision: int = 6) -> list[str]:
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
def latlon_to_utm(latitude: numpy.ndarray[numpy.float64], longitude: numpy.ndarray[numpy.float64], setzone: int = -1, mp_cores: int = 1) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64], int, bool]:
    ...
@typing.overload
def longitude_to_string(longitude: float, format: t_latlon_format = ..., precision: int = 6) -> str:
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
def longitude_to_string(longitude: list[float], format: t_latlon_format = ..., precision: int = 6) -> list[str]:
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
def utm_to_latlon(northing: numpy.ndarray[numpy.float64], easting: numpy.ndarray[numpy.float64], zone: int, northern_hemisphere: bool, mp_cores: int = 1) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
    ...
@typing.overload
def utm_to_latlon(northing: numpy.ndarray[numpy.float64], easting: numpy.ndarray[numpy.float64], zone: numpy.ndarray[numpy.int32], northern_hemisphere: numpy.ndarray[numpy.int32], mp_cores: int = 1) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
    ...
degrees: t_latlon_format  # value = <t_latlon_format.degrees: 0>
minutes: t_latlon_format  # value = <t_latlon_format.minutes: 1>
seconds: t_latlon_format  # value = <t_latlon_format.seconds: 2>
