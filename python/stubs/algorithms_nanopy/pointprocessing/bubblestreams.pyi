from collections.abc import Sequence
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

import themachinethatgoesping.tools_nanopy.vectorinterpolators


class ZSpine:
    @overload
    def __init__(self, is_altitude: bool = False) -> None: ...

    @overload
    def __init__(self, x: Sequence[float], y: Sequence[float], z: Sequence[float], is_altitude: bool = False) -> None: ...

    def __eq__(self, other: ZSpine) -> bool: ...

    def add_point(self, x: float, y: float, z: float) -> None: ...

    def add_points(self, x: Sequence[float], y: Sequence[float], z: Sequence[float]) -> None: ...

    def reset_origin(self) -> None: ...

    def set_origin(self, x: float, y: float, z: float) -> None: ...

    def estimate_origin(self, bottom_z: float, slope_modifier: float = 1.0) -> None: ...

    def get_spine_points(self, with_origin: bool = True) -> tuple[list[float], list[float], list[float]]: ...

    def get_spine(self, n_points: int, with_origin: bool = True) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    def get_origin(self) -> tuple[float, float, float] | None: ...

    def get_is_altitude(self) -> bool: ...

    def get_xy(self, z: float) -> tuple[float, float]: ...

    def get_x_interpolator(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator: ...

    def get_y_interpolator(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator: ...

    def copy(self) -> ZSpine:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ZSpine: ...

    def __deepcopy__(self, arg: dict, /) -> ZSpine: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ZSpine:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    @overload
    @staticmethod
    def from_point_cloud(x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], z: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], n_quantiles: int, is_altitude: bool = False) -> ZSpine: ...

    @overload
    @staticmethod
    def from_point_cloud(x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], z: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], n_quantiles: int, is_altitude: bool = False) -> ZSpine: ...

    @overload
    @staticmethod
    def from_point_cloud(x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], n_quantiles: int, is_altitude: bool = False) -> ZSpine: ...

    @overload
    @staticmethod
    def from_point_cloud(x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], n_quantiles: int, is_altitude: bool = False) -> ZSpine: ...

    @overload
    def get_xy_vec(self, z: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def get_xy_vec(self, z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def displace_points_inplace(self, x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], z: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> None: ...

    @overload
    def displace_points_inplace(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> None: ...

    @overload
    def displace_points(self, x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], z: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]]: ...

    @overload
    def displace_points(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> tuple[Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]]: ...

    @overload
    def displace_points_x(self, x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], z: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]: ...

    @overload
    def displace_points_x(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]: ...

    @overload
    def displace_points_y(self, y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], z: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]: ...

    @overload
    def displace_points_y(self, y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]: ...
