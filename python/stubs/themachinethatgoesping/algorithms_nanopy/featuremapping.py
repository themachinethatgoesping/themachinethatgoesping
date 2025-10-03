"""
Functions and classes for featuremapping and interpolation
"""
from __future__ import annotations
import collections.abc
import typing
__all__: list[str] = ['NearestFeatureMapper']
class NearestFeatureMapper:
    """
    A feature mapper that enables conversion between different feature
    spaces using nearest neighbor interpolation
    
    This class manages multiple named features and provides functionality
    to map values between different feature spaces or convert feature
    values to/from indices. It's particularly useful for coordinate
    transformations and feature space conversions in data processing
    pipelines.
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> NearestFeatureMapper:
        ...
    def __deepcopy__(self, arg: dict) -> NearestFeatureMapper:
        ...
    def __eq__(self, other: NearestFeatureMapper) -> bool:
        """
        Equality comparison operator
        
        Parameter ``other``:
            Another NearestFeatureMapper to compare with
        
        Returns:
            true if both mappers have the same features and values, false
            otherwise
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, features: collections.abc.Mapping[str, collections.abc.Sequence[float]] = {}) -> None:
        """
        Constructor with optional initial features
        
        Parameter ``features``:
            Map of feature names to their corresponding value vectors
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
    def clear_features(self) -> None:
        """
        Clear all features from the mapper
        """
    def copy(self) -> NearestFeatureMapper:
        """
        return a copy using the c++ default copy constructor
        """
    def feature_to_feature(self, feature_from: str, feature_to: str, value: float) -> float:
        """
        feature_to_feature(self, feature_from: str, feature_to: str, values: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        
        Overloaded function.
        
        1. ``feature_to_feature(self, feature_from: str, feature_to: str, value: float) -> float``
        
        Convert a value from one feature space to another
        
        Parameter ``feature_from``:
            Name of the source feature
        
        Parameter ``feature_to``:
            Name of the target feature
        
        Parameter ``value``:
            The value in the source feature space
        
        Returns:
            The corresponding value in the target feature space
        
        Throws:
            std::runtime_error if either feature is not found
        
        2. ``feature_to_feature(self, feature_from: str, feature_to: str, values: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*), order='A']``
        
        Convert multiple values from one feature space to another (vectorized)
        
        Template parameter ``t_values``:
            Type of the values container (must be xtensor compatible)
        
        Parameter ``feature_from``:
            Name of the source feature
        
        Parameter ``feature_to``:
            Name of the target feature
        
        Parameter ``values``:
            Container of values in the source feature space
        
        Parameter ``mp_cores``:
            Number of cores to use for parallel processing (default: 1)
        
        Returns:
            Container of corresponding values in the target feature space
        
        Throws:
            std::runtime_error if either feature is not found
        """
    def feature_to_index(self, feature: str, value: float) -> int:
        """
        feature_to_index(self, feature: str, values: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=uint64, shape=(*), order='A']
        
        Overloaded function.
        
        1. ``feature_to_index(self, feature: str, value: float) -> int``
        
        Convert a feature value to its corresponding index
        
        Parameter ``feature``:
            Name of the feature
        
        Parameter ``value``:
            The value to convert to an index
        
        Returns:
            The index of the nearest value in the feature
        
        Throws:
            std::runtime_error if the feature is not found
        
        2. ``feature_to_index(self, feature: str, values: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=uint64, shape=(*), order='A']``
        
        Convert multiple feature values to their corresponding indices
        (vectorized)
        
        Template parameter ``t_index``:
            Type of the output index container (must be xtensor compatible)
        
        Template parameter ``t_values``:
            Type of the input values container (must be xtensor compatible)
        
        Parameter ``feature``:
            Name of the feature
        
        Parameter ``values``:
            Container of values to convert to indices
        
        Parameter ``mp_cores``:
            Number of cores to use for parallel processing (default: 1)
        
        Returns:
            Container of indices corresponding to the nearest values
        
        Throws:
            std::runtime_error if the feature is not found
        """
    def get_feature_indices(self, feature: str) -> list[int] | None:
        """
        Get the indices for a specific feature
        
        Parameter ``feature``:
            Name of the feature
        
        Returns:
            Optional vector of feature indices, nullopt if feature doesn't
            exist
        """
    def get_feature_values(self, feature: str) -> list[float] | None:
        """
        Get the values for a specific feature
        
        Parameter ``feature``:
            Name of the feature
        
        Returns:
            Optional vector of feature values, nullopt if feature doesn't
            exist
        """
    def has_feature(self, feature: str) -> bool:
        """
        Check if a feature exists in the mapper
        
        Parameter ``feature``:
            Name of the feature to check
        
        Returns:
            true if the feature exists, false otherwise
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def index_to_feature(self, feature: str, index: int) -> float:
        """
        index_to_feature(self, feature: str, indices: numpy.ndarray[dtype=uint64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        
        Overloaded function.
        
        1. ``index_to_feature(self, feature: str, index: int) -> float``
        
        Convert an index to its corresponding feature value
        
        Parameter ``feature``:
            Name of the feature
        
        Parameter ``index``:
            The index to convert to a value
        
        Returns:
            The interpolated value at the given index
        
        Throws:
            std::runtime_error if the feature is not found
        
        2. ``index_to_feature(self, feature: str, indices: numpy.ndarray[dtype=uint64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*), order='A']``
        
        Convert multiple indices to their corresponding feature values
        (vectorized)
        
        Template parameter ``t_values``:
            Type of the output values container (must be xtensor compatible)
        
        Template parameter ``t_index``:
            Type of the input index container (must be xtensor compatible)
        
        Parameter ``feature``:
            Name of the feature
        
        Parameter ``indices``:
            Container of indices to convert to values
        
        Parameter ``mp_cores``:
            Number of cores to use for parallel processing (default: 1)
        
        Returns:
            Container of interpolated values at the given indices
        
        Throws:
            std::runtime_error if the feature is not found
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def keys(self) -> list[str]:
        """
        Get all feature names
        
        Returns:
            Vector of all feature names currently stored in the mapper
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def remove_feature(self, feature: str) -> None:
        """
        Remove a feature from the mapper
        
        Parameter ``feature``:
            Name of the feature to remove
        """
    def set_feature(self, feature: str, values: collections.abc.Sequence[float]) -> None:
        """
        Add or update a feature with the given values
        
        Parameter ``feature``:
            Name of the feature to set
        
        Parameter ``values``:
            Vector of values for the feature
        
        Throws:
            std::invalid_argument if values has less than 2 elements
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
