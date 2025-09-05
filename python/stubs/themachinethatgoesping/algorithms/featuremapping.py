"""
Functions and classes for featuremapping and interpolation
"""
from __future__ import annotations
import numpy
import typing
__all__: list[str] = ['NearestFeatureMapper']
class NearestFeatureMapper:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestFeatureMapper:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> NearestFeatureMapper:
        ...
    def __deepcopy__(self, arg0: dict) -> NearestFeatureMapper:
        ...
    def __eq__(self, other: NearestFeatureMapper) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, features: dict[str, list[float]] = {}) -> None:
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
    def clear_features(self) -> None:
        ...
    def copy(self) -> NearestFeatureMapper:
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def feature_to_feature(self, feature_from: str, feature_to: str, value: float) -> float:
        ...
    @typing.overload
    def feature_to_feature(self, feature_from: str, feature_to: str, values: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
        ...
    @typing.overload
    def feature_to_index(self, feature: str, value: float) -> int:
        ...
    @typing.overload
    def feature_to_index(self, feature: str, values: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> numpy.ndarray[numpy.uint64]:
        ...
    def get_feature_values(self, feature: str) -> list[float] | None:
        ...
    def has_feature(self, feature: str) -> bool:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def index_to_feature(self, feature: str, index: int) -> float:
        ...
    @typing.overload
    def index_to_feature(self, feature: str, indices: numpy.ndarray[numpy.uint64], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def keys(self) -> list[str]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def remove_feature(self, feature: str) -> None:
        ...
    def set_feature(self, feature: str, values: list[float]) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
