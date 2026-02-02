"""Submodule for geoprocessing functions"""

from typing import Annotated, overload

import numpy
from numpy.typing import NDArray


@overload
def to_raypoints(base_location: float, end_locations: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], base_scale_value: float, end_scale_values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ray_scale_values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

@overload
def to_raypoints(base_location: float, end_locations: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], base_scale_value: float, end_scale_values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ray_scale_values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...
