import abc
from collections.abc import (
    Iterable as _Iterable,
    Iterator as _Iterator
)
from typing import Union

import numpy


TYPE_CHECKING: bool = False

class EchogramDataBackend(abc.ABC):
    """
    Abstract base class for echogram data sources.

    Backends are responsible for:
    - Providing metadata about the data (ping times, extents, etc.)
    - Reading water column data for individual pings
    - Managing data caching if needed

    Backends receive sample indices from the EchogramBuilder and return
    the corresponding data. Coordinate conversion is handled by EchogramBuilder.
    """

    @property
    def n_pings(self) -> int:
        """Number of pings in the dataset."""

    @property
    def ping_times(self) -> numpy.ndarray:
        """Timestamps for each ping (Unix timestamps as float64)."""

    @property
    def max_sample_counts(self) -> numpy.ndarray:
        """Maximum number of samples for each ping (int array)."""

    @property
    def sample_nr_extents(self) -> tuple[numpy.ndarray, numpy.ndarray]:
        """Sample number extents as (min_sample_nrs, max_sample_nrs) arrays."""

    @property
    def range_extents(self) -> Union[tuple[numpy.ndarray, numpy.ndarray], None]:
        """
        Range extents as (min_ranges, max_ranges) arrays, or None if not available.
        """

    @property
    def depth_extents(self) -> Union[tuple[numpy.ndarray, numpy.ndarray], None]:
        """
        Depth extents as (min_depths, max_depths) arrays, or None if no navigation.
        """

    @property
    def has_navigation(self) -> bool:
        """Whether depth information is available (requires navigation data)."""

    @property
    def latitudes(self) -> Union[numpy.ndarray, None]:
        """
        Latitude for each ping in degrees, or None if not available.

        Default implementation returns None. Override in backends that support it.
        """

    @property
    def longitudes(self) -> Union[numpy.ndarray, None]:
        """
        Longitude for each ping in degrees, or None if not available.

        Default implementation returns None. Override in backends that support it.
        """

    @property
    def has_latlon(self) -> bool:
        """Whether latitude/longitude information is available."""

    @property
    def wci_value(self) -> str:
        """The water column image value type (e.g., 'sv', 'av', 'pv')."""

    @property
    def linear_mean(self) -> bool:
        """Whether to use linear mean for beam averaging."""

    def get_ping_params(self) -> dict[str, tuple[str, numpy.ndarray]]:
        """
        Return pre-computed ping parameters.

        Returns:
            Dictionary mapping parameter names (e.g., 'bottom', 'minslant', 'echosounder')
            to tuples of (y_reference, values) where y_reference is one of
            'Depth (m)', 'Range (m)', 'Sample number', 'Y indice'.
        """

    def get_column(self, ping_index: int) -> numpy.ndarray:
        """
        Get column data for a ping.

        Returns beam-averaged water column data. The processing method
        (range stack vs depth stack) is determined by the backend's configuration.
        Both modes return data of the same shape (n_samples for the ping).

        Args:
            ping_index: Index of the ping to retrieve.

        Returns:
            1D array of shape (n_samples,) with processed values.
        """

    def get_raw_column(self, ping_index: int) -> numpy.ndarray:
        """
        Get full-resolution beam-averaged column data for a ping.

        Unlike get_column, this always returns range-stacked data regardless
        of the backend's stacking mode. Used for layer extraction where
        sample indices need to be preserved.

        Args:
            ping_index: Index of the ping to retrieve.

        Returns:
            1D array with all samples for the ping.
        """

    def iterate_raw_columns(self, ping_indices: _Iterable[int]) -> _Iterator[tuple[int, numpy.ndarray]]:
        """
        Iterate over raw columns for given ping indices.

        Args:
            ping_indices: Indices of pings to iterate over.

        Yields:
            Tuples of (ping_index, raw_column_data).
        """

    def get_chunk(self, start_ping: int, end_ping: int) -> numpy.ndarray:
        """
        Get a chunk of WCI data for multiple consecutive pings.

        Returns a 2D array of shape (n_pings, max_samples) where n_pings
        is end_ping - start_ping. Backends can override this for faster
        bulk access.

        Default implementation uses get_column for each ping.

        Args:
            start_ping: First ping index (inclusive).
            end_ping: Last ping index (exclusive).

        Returns:
            2D array of shape (end_ping - start_ping, max_samples).
        """

    def get_beam_sample_selection(self, ping_index: int):
        """
        Get the beam sample selection for a ping, if available.

        Not all backends support this. Override in subclasses that do.

        Args:
            ping_index: Index of the ping.

        Returns:
            BeamSampleSelection object or None if not supported.
        """

    def clear_cache(self) -> None:
        """Clear any cached data. Override in subclasses that implement caching."""

    def get_image(self, request: EchogramImageRequest) -> numpy.ndarray:
        """
        Build a complete echogram image from a request.

        Each backend implements this differently based on its data storage format.

        Args:
            request: Image request with ping mapping and affine parameters.

        Returns:
            2D array of shape (nx, ny) with echogram data (ping, sample).
        """

    __abstractmethods__: frozenset = ...
