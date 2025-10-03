"""
Submodule that holds classes related to bubblestream processing
"""
from __future__ import annotations
import collections.abc
import numpy
import themachinethatgoesping.tools_nanopy.vectorinterpolators
import typing
__all__: list[str] = ['ZSpine']
class ZSpine:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_point_cloud: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> ZSpine:
        ...
    def __deepcopy__(self, arg: dict) -> ZSpine:
        ...
    def __eq__(self, other: ZSpine) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, is_altitude: bool = False) -> None:
        """
        __init__(self, x: collections.abc.Sequence[float], y: collections.abc.Sequence[float], z: collections.abc.Sequence[float], is_altitude: bool = False) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def add_point(self, x: float, y: float, z: float) -> None:
        ...
    def add_points(self, x: collections.abc.Sequence[float], y: collections.abc.Sequence[float], z: collections.abc.Sequence[float]) -> None:
        ...
    def copy(self) -> ZSpine:
        """
        return a copy using the c++ default copy constructor
        """
    def displace_points(self, x: numpy.ndarray[dtype=float64, ..., order='A'], y: numpy.ndarray[dtype=float64, ..., order='A'], z: numpy.ndarray[dtype=float64, ..., order='A'], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> ...:
        """
        displace_points(self, x: numpy.ndarray[dtype=float32, shape=(*), order='A'], y: numpy.ndarray[dtype=float32, shape=(*), order='A'], z: numpy.ndarray[dtype=float32, shape=(*), order='A'], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> std::pair<xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag> >
        """
    def displace_points_inplace(self, x: numpy.ndarray[dtype=float64, ..., order='A'], y: numpy.ndarray[dtype=float64, ..., order='A'], z: numpy.ndarray[dtype=float64, ..., order='A'], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> None:
        """
        displace_points_inplace(self, x: numpy.ndarray[dtype=float32, shape=(*), order='A'], y: numpy.ndarray[dtype=float32, shape=(*), order='A'], z: numpy.ndarray[dtype=float32, shape=(*), order='A'], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> None
        """
    def displace_points_x(self, x: numpy.ndarray[dtype=float64, ..., order='A'], z: numpy.ndarray[dtype=float64, ..., order='A'], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, ..., order='C']:
        """
        displace_points_x(self, x: numpy.ndarray[dtype=float32, shape=(*), order='A'], z: numpy.ndarray[dtype=float32, shape=(*), order='A'], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, shape=(*), order='C']
        """
    def displace_points_y(self, y: numpy.ndarray[dtype=float64, ..., order='A'], z: numpy.ndarray[dtype=float64, ..., order='A'], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, ..., order='C']:
        """
        displace_points_y(self, y: numpy.ndarray[dtype=float32, shape=(*), order='A'], z: numpy.ndarray[dtype=float32, shape=(*), order='A'], bottom_z: float | None = None, inverse: bool = False, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, shape=(*), order='C']
        """
    def estimate_origin(self, bottom_z: float, slope_modifier: float = 1.0) -> None:
        ...
    def get_is_altitude(self) -> bool:
        ...
    def get_origin(self) -> ... | None:
        ...
    def get_spine(self, n_points: int, with_origin: bool = True) -> numpy.ndarray[dtype=float64, ..., order='C']:
        ...
    def get_spine_points(self, with_origin: bool = True) -> ...:
        ...
    def get_x_interpolator(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator:
        ...
    def get_xy(self, z: float) -> ...:
        ...
    def get_xy_vec(self, z: numpy.ndarray[dtype=float64, ..., order='A']) -> numpy.ndarray[dtype=float64, ..., order='C']:
        """
        get_xy_vec(self, z: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*, *), order='C']
        """
    def get_y_interpolator(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def reset_origin(self) -> None:
        ...
    def set_origin(self, x: float, y: float, z: float) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
