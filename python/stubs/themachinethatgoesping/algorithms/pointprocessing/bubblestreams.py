"""
Submodule that holds classes related to bubblestream processing
"""
from __future__ import annotations
import numpy
import themachinethatgoesping.tools_cppy.vectorinterpolators
import typing
__all__ = ['ZSpine']
class ZSpine:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ZSpine:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    @typing.overload
    def from_point_cloud(x: numpy.ndarray[numpy.float64], y: numpy.ndarray[numpy.float64], z: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float64], n_quantiles: int, is_altitude: bool = False) -> ZSpine:
        ...
    @staticmethod
    @typing.overload
    def from_point_cloud(x: numpy.ndarray[numpy.float64], y: numpy.ndarray[numpy.float64], z: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float32], n_quantiles: int, is_altitude: bool = False) -> ZSpine:
        ...
    @staticmethod
    @typing.overload
    def from_point_cloud(x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float64], n_quantiles: int, is_altitude: bool = False) -> ZSpine:
        ...
    @staticmethod
    @typing.overload
    def from_point_cloud(x: numpy.ndarray[numpy.float32], y: numpy.ndarray[numpy.float32], z: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float32], n_quantiles: int, is_altitude: bool = False) -> ZSpine:
        ...
    def __copy__(self) -> ZSpine:
        ...
    def __deepcopy__(self, arg0: dict) -> ZSpine:
        ...
    def __eq__(self, other: ZSpine) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, is_altitude: bool = False) -> None:
        ...
    @typing.overload
    def __init__(self, x: list[float], y: list[float], z: list[float], is_altitude: bool = False) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def add_point(self, x: float, y: float, z: float) -> None:
        ...
    def add_points(self, x: list[float], y: list[float], z: list[float]) -> None:
        ...
    def copy(self) -> ZSpine:
        """
        return a copy using the c++ default copy constructor
        """
    def estimate_origin(self, bottom_z: float, slope_modifier: float = 1.0) -> None:
        ...
    def get_is_altitude(self) -> bool:
        ...
    def get_origin(self) -> tuple[float, float, float] | None:
        ...
    def get_spine(self, n_points: int, with_origin: bool = True) -> numpy.ndarray[numpy.float64]:
        ...
    def get_spine_points(self, with_origin: bool = True) -> tuple[list[float], list[float], list[float]]:
        ...
    def get_x_interpolator(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator:
        ...
    def get_xy(self, z: float) -> tuple[float, float]:
        ...
    @typing.overload
    def get_xy_vec(self, z: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.float64]:
        ...
    @typing.overload
    def get_xy_vec(self, z: numpy.ndarray[numpy.float32]) -> numpy.ndarray[numpy.float32]:
        ...
    def get_y_interpolator(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator:
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
