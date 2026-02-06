"""Convenient functions for converting latlon and utm strings."""

from collections.abc import Sequence
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.navigation_nanopy.datastructures


@overload
def latitude_to_string(latitude: float, format: themachinethatgoesping.navigation_nanopy.o_latlon_format = themachinethatgoesping.navigation_nanopy.t_latlon_format.minutes, precision: int = 6) -> str:
    r"""
    convert a latitude value to a string

    Args:
        latitude: value to be converted
        precision: number of digits behind the .
        format: latlon format (degrees°N/S, degrees°minutes'N/S or
                degrees°minutes'seconds\'\'N/S)

    Returns:
        converted latitude string
    """

@overload
def latitude_to_string(latitude: Sequence[float], format: themachinethatgoesping.navigation_nanopy.o_latlon_format = themachinethatgoesping.navigation_nanopy.t_latlon_format.minutes, precision: int = 6) -> list[str]: ...

@overload
def longitude_to_string(longitude: float, format: themachinethatgoesping.navigation_nanopy.o_latlon_format = themachinethatgoesping.navigation_nanopy.t_latlon_format.minutes, precision: int = 6) -> str:
    r"""
    convert a latitude value to a string

    Args:
        latitude: value to be converted
        precision: number of digits behind the .
        format: latlon format (degrees°N/S, degrees°minutes'N/S or
                degrees°minutes'seconds\'\'N/S)

    Returns:
        converted latitude string
    """

@overload
def longitude_to_string(longitude: Sequence[float], format: themachinethatgoesping.navigation_nanopy.o_latlon_format = themachinethatgoesping.navigation_nanopy.t_latlon_format.minutes, precision: int = 6) -> list[str]: ...

@overload
def utm_to_latlon(northing: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], easting: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], zone: int, northern_hemisphere: bool, mp_cores: int = 1) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]]:
    """
    Convert utm coordinates to latitude longitude using Geographic lib

    Args:
        northing: northing in meters
        easting: easting in meters
        zone: utm zone number (1-60)
        northern_hemisphere: if true, northern hemisphere, else southern
                             hemisphere

    Returns:
        (list of latitude, list of longitudes)
    """

@overload
def utm_to_latlon(northing: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], easting: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], zone: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')], northern_hemisphere: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]]: ...

def latlon_to_utm(latitude: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], longitude: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], setzone: int = -1, mp_cores: int = 1) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], int, bool]: ...

@overload
def compute_latlon_distance_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Compute the distance in meters between two latitude-longitude
    coordinates using the WGS84 ellipsoid.

    Args:
        lat1: Latitude of the first coordinate.
        lon1: Longitude of the first coordinate.
        lat2: Latitude of the second coordinate.
        lon2: Longitude of the second coordinate.

    Template Args:
        T_float: Floating-point type for latitude and longitude values.

    Returns:
        Distance between the two coordinates in meters.
    """

@overload
def compute_latlon_distance_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float: ...

@overload
def compute_latlon_distance_m(geolocation_latlon_1: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLatLon, geolocation_latlon_2: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLatLon) -> float: ...

@overload
def compute_latlon_distance_m(geolocation_latlon_1: themachinethatgoesping.navigation_nanopy.datastructures.SensordataLatLon, geolocation_latlon_2: themachinethatgoesping.navigation_nanopy.datastructures.SensordataLatLon) -> float: ...

@overload
def compute_latlon_distance_m(geolocation_latlon_1: tuple[float, float], geolocation_latlon_2: tuple[float, float]) -> float: ...

@overload
def compute_latlon_distance_m(geolocation_latlon_1: tuple[float, float], geolocation_latlon_2: tuple[float, float]) -> float: ...

@overload
def compute_latlon_distances_m(latitudes: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], longitudes: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
    """
    Compute the distances in meters between consecutive latitude-longitude
    coordinates using the WGS84 ellipsoid.

    Args:
        latitudes: Vector of latitude values.
        longitudes: Vector of longitude values.

    Template Args:
        T_return_container: Type of container to store the distances.
        T_float_container: Type of container that holds latitude and
                           longitude values as floats.

    Returns:
        Vector of distances between consecutive coordinates in meters.
    """

@overload
def compute_latlon_distances_m(latitudes: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], longitudes: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def compute_latlon_distances_m(geolocations_latlon: Sequence[themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLatLon]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def compute_latlon_distances_m(geolocations_latlon: Sequence[themachinethatgoesping.navigation_nanopy.datastructures.SensordataLatLon]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def compute_latlon_distances_m(geolocations_latlon: Sequence[tuple[float, float]]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def compute_latlon_distances_m(geolocations_latlon: Sequence[tuple[float, float]]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def cumulative_latlon_distances_m(latitudes: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], longitudes: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
    """
    Compute the cumulative distances in meters between consecutive
    latitude-longitude coordinates using the WGS84 ellipsoid.

    Args:
        latitudes: Vector of latitude values.
        longitudes: Vector of longitude values.

    Template Args:
        T_return_container: Type of container to store the distances.
        T_float_container: Type of container that holds latitude and
                           longitude values as floats.

    Returns:
        Vector of cumulative distances between consecutive coordinates in
        meters.
    """

@overload
def cumulative_latlon_distances_m(latitudes: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], longitudes: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def cumulative_latlon_distances_m(geolocations_latlon: Sequence[themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLatLon]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def cumulative_latlon_distances_m(geolocations_latlon: Sequence[themachinethatgoesping.navigation_nanopy.datastructures.SensordataLatLon]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def cumulative_latlon_distances_m(geolocations_latlon: Sequence[tuple[float, float]]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def cumulative_latlon_distances_m(geolocations_latlon: Sequence[tuple[float, float]]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...
