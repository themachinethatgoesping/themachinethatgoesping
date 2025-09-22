"""
Submodule for geoprocessing functions
"""
from __future__ import annotations
import numpy
import typing
__all__: list[str] = ['to_raypoints']
@typing.overload
def to_raypoints(base_location: typing.SupportsFloat, end_locations: numpy.ndarray[numpy.float64], base_scale_value: typing.SupportsFloat, end_scale_values: numpy.ndarray[numpy.float64], ray_scale_values: numpy.ndarray[numpy.float64], mp_cores: typing.SupportsInt = 1) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def to_raypoints(base_location: typing.SupportsFloat, end_locations: numpy.ndarray[numpy.float32], base_scale_value: typing.SupportsFloat, end_scale_values: numpy.ndarray[numpy.float32], ray_scale_values: numpy.ndarray[numpy.float32], mp_cores: typing.SupportsInt = 1) -> numpy.ndarray[numpy.float32]:
    ...
