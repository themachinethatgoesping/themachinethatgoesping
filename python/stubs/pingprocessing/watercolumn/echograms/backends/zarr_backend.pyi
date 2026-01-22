from typing import Union

import numpy
import xr

import themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base import (
    EchogramDataBackend as EchogramDataBackend
)
import themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.storage_mode
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.storage_mode import (
    StorageAxisMode as StorageAxisMode
)
import themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers
from themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers import (
    EchogramImageRequest as EchogramImageRequest
)


HAS_ZARR: bool = True

ZARR_FORMAT_VERSION: str = '2.0'

class ZarrDataBackend(themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base.EchogramDataBackend):
    """
    Backend that reads data from Zarr arrays with lazy loading.

    Zarr arrays provide efficient chunked storage and lazy loading via Dask,
    making them suitable for large datasets that don't fit in memory.

    The Zarr store contains:
    - wci_data: 2D array (n_pings, max_samples) of beam-averaged water column data
    - ping_times: 1D array of timestamps
    - max_sample_counts: 1D array of sample counts per ping
    - sample_nr_min/max: 1D arrays of sample number extents
    - range_min/max: 1D arrays of range extents (optional)
    - depth_min/max: 1D arrays of depth extents (optional)
    - ping_params/*: Ping parameter arrays (bottom, echosounder depth, etc.)
    - Attributes: wci_value, linear_mean, has_navigation, format_version, storage_mode
    """

    def __init__(self, ds: xr.Dataset, store_path: Union[str, None] = None, max_chunk_mb: float = 100.0):
        """
        Initialize ZarrDataBackend from an xarray Dataset.

        Prefer using the `from_zarr` factory method instead of this constructor.

        Args:
            ds: xarray Dataset backed by Dask arrays.
            store_path: Path to the Zarr store (for reference).
            max_chunk_mb: Maximum memory (MB) per contiguous load chunk.
                         Larger = faster I/O, smaller = less memory.
                         Default 100 MB is a good balance.
        """

    @classmethod
    def from_zarr(cls, path: str, chunks: Union[dict[str, int], None] = None, max_chunk_mb: float = 100.0) -> ZarrDataBackend:
        """
        Create a ZarrDataBackend from a Zarr store.

        Args:
            path: Path to the Zarr store (directory).
            chunks: Optional chunk sizes for loading. Default uses stored chunks.
                    Pass chunks={} to use stored chunking (lazy), or
                    chunks=None to load eagerly as numpy arrays.
            max_chunk_mb: Maximum memory (MB) per contiguous load chunk in get_image().
                         Larger = faster I/O, smaller = less memory.
                         Default 100 MB is a good balance for most systems.

        Returns:
            ZarrDataBackend instance with lazy-loaded data.
        """

    @property
    def n_pings(self) -> int: ...

    @property
    def ping_times(self) -> numpy.ndarray: ...

    @property
    def max_sample_counts(self) -> numpy.ndarray: ...

    @property
    def sample_nr_extents(self) -> tuple[numpy.ndarray, numpy.ndarray]: ...

    @property
    def range_extents(self) -> Union[tuple[numpy.ndarray, numpy.ndarray], None]: ...

    @property
    def depth_extents(self) -> Union[tuple[numpy.ndarray, numpy.ndarray], None]: ...

    @property
    def has_navigation(self) -> bool: ...

    @property
    def latitudes(self) -> Union[numpy.ndarray, None]:
        """Latitude for each ping in degrees, or None if not available."""

    @property
    def longitudes(self) -> Union[numpy.ndarray, None]:
        """Longitude for each ping in degrees, or None if not available."""

    @property
    def wci_value(self) -> str: ...

    @property
    def linear_mean(self) -> bool: ...

    @property
    def storage_mode(self) -> themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.storage_mode.StorageAxisMode:
        """Storage coordinate system for this backend."""

    def get_ping_params(self) -> dict[str, tuple[str, tuple[numpy.ndarray, numpy.ndarray]]]: ...

    def get_column(self, ping_index: int) -> numpy.ndarray:
        """
        Get column data for a ping.

        Uses chunk caching for fast consecutive reads. When a column is 
        requested, the entire zarr chunk containing it is loaded and cached.
        Subsequent requests for columns in the same chunk are instant.

        Args:
            ping_index: Index of the ping to retrieve.

        Returns:
            1D array of shape (n_samples,) with processed values.
        """

    def get_raw_column(self, ping_index: int) -> numpy.ndarray:
        """
        Get full-resolution column data for a ping.

        For ZarrDataBackend, this is the same as get_column since
        we store beam-averaged data.
        """

    def get_chunk(self, start_ping: int, end_ping: int) -> numpy.ndarray:
        """
        Get a chunk of WCI data for multiple consecutive pings.

        Optimized for ZarrDataBackend using direct zarr array access.

        Args:
            start_ping: First ping index (inclusive).
            end_ping: Last ping index (exclusive).

        Returns:
            2D array of shape (end_ping - start_ping, n_samples).
        """

    def get_image(self, request: themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers.EchogramImageRequest) -> numpy.ndarray:
        """
        Build a complete echogram image from a request.

        Uses direct zarr access with scattered (fancy) indexing to load only
        the unique pings needed. This is memory-efficient and fast for all
        access patterns.

        Args:
            request: Image request with ping mapping and affine parameters.

        Returns:
            2D array of shape (nx, ny) with echogram data (ping, sample).
        """

    @property
    def store_path(self) -> Union[str, None]:
        """Path to the Zarr store, if available."""

    def __repr__(self) -> str: ...

    __abstractmethods__: frozenset = ...
