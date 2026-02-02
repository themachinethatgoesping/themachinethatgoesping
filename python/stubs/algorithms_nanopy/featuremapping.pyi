"""Functions and classes for featuremapping and interpolation"""

from collections.abc import Mapping, Sequence
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray


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

    def __init__(self, features: Mapping[str, Sequence[float]] = {}) -> None:
        """
        Constructor with optional initial features
        Args:
            features: Map of feature names to their corresponding value
                      vectors
        """

    def set_feature(self, feature: str, values: Sequence[float]) -> None:
        """
        Add or update a feature with the given values
        Args:
            feature: Name of the feature to set
            values: Vector of values for the feature

        Raises:
            std::invalid_argument: if values has less than 2 elements
        """

    def remove_feature(self, feature: str) -> None:
        """
        Remove a feature from the mapper
        Args:
            feature: Name of the feature to remove
        """

    def clear_features(self) -> None:
        """Clear all features from the mapper"""

    def has_feature(self, feature: str) -> bool:
        """
        Check if a feature exists in the mapper
        Args:
            feature: Name of the feature to check

        Returns:
            true if the feature exists, false otherwise
        """

    @overload
    def feature_to_index(self, feature: str, value: float) -> int:
        """
        Convert a feature value to its corresponding index
        Args:
            feature: Name of the feature
            value: The value to convert to an index

        Returns:
            The index of the nearest value in the feature

        Raises:
            std::runtime_error: if the feature is not found
        """

    @overload
    def feature_to_index(self, feature: str, values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.uint64], dict(shape=(None,), order='A')]:
        """
        Convert multiple feature values to their corresponding indices
        (vectorized)
        Args:
            feature: Name of the feature
            values: Container of values to convert to indices
            mp_cores: Number of cores to use for parallel processing (default:
                      1)

        Template Args:
            t_index: Type of the output index container (must be xtensor
                     compatible)
            t_values: Type of the input values container (must be xtensor
                      compatible)

        Returns:
            Container of indices corresponding to the nearest values

        Raises:
            std::runtime_error: if the feature is not found
        """

    @overload
    def index_to_feature(self, feature: str, index: int) -> float:
        """
        Convert an index to its corresponding feature value
        Args:
            feature: Name of the feature
            index: The index to convert to a value

        Returns:
            The interpolated value at the given index

        Raises:
            std::runtime_error: if the feature is not found
        """

    @overload
    def index_to_feature(self, feature: str, indices: Annotated[NDArray[numpy.uint64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]:
        """
        Convert multiple indices to their corresponding feature values
        (vectorized)
        Args:
            feature: Name of the feature
            indices: Container of indices to convert to values
            mp_cores: Number of cores to use for parallel processing (default:
                      1)

        Template Args:
            t_values: Type of the output values container (must be xtensor
                      compatible)
            t_index: Type of the input index container (must be xtensor
                     compatible)

        Returns:
            Container of interpolated values at the given indices

        Raises:
            std::runtime_error: if the feature is not found
        """

    @overload
    def feature_to_feature(self, feature_from: str, feature_to: str, value: float) -> float:
        """
        Convert a value from one feature space to another
        Args:
            feature_from: Name of the source feature
            feature_to: Name of the target feature
            value: The value in the source feature space

        Returns:
            The corresponding value in the target feature space

        Raises:
            std::runtime_error: if either feature is not found
        """

    @overload
    def feature_to_feature(self, feature_from: str, feature_to: str, values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]:
        """
        Convert multiple values from one feature space to another (vectorized)
        Args:
            feature_from: Name of the source feature
            feature_to: Name of the target feature
            values: Container of values in the source feature space
            mp_cores: Number of cores to use for parallel processing (default:
                      1)

        Template Args:
            t_values: Type of the values container (must be xtensor
                      compatible)

        Returns:
            Container of corresponding values in the target feature space

        Raises:
            std::runtime_error: if either feature is not found
        """

    def get_feature_values(self, feature: str) -> list[float] | None:
        """
        Get the values for a specific feature
        Args:
            feature: Name of the feature

        Returns:
            Optional vector of feature values, nullopt if feature doesn't
            exist
        """

    def get_feature_indices(self, feature: str) -> list[int] | None:
        """
        Get the indices for a specific feature
        Args:
            feature: Name of the feature

        Returns:
            Optional vector of feature indices, nullopt if feature doesn't
            exist
        """

    def keys(self) -> list[str]:
        """
        Get all feature names
        Returns:
            Vector of all feature names currently stored in the mapper
        """

    def __eq__(self, other: NearestFeatureMapper) -> bool:
        """
        Equality comparison operator
        Args:
            other: Another NearestFeatureMapper to compare with

        Returns:
            true if both mappers have the same features and values, false
            otherwise
        """

    def copy(self) -> NearestFeatureMapper:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NearestFeatureMapper: ...

    def __deepcopy__(self, arg: dict, /) -> NearestFeatureMapper: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NearestFeatureMapper:
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
