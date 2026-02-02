"""
Backend for ultra-fast echogram data access using memory-mapped files.

Memory-mapped files provide near-instantaneous random access by letting the
OS handle paging. This is ideal for interactive visualization where scattered
ping access patterns are common.

Trade-off vs Zarr:
- Mmap: Uncompressed (larger files), but 10-100x faster random access
- Zarr: Compressed (smaller files), but slower due to decompression

Memory efficiency:
- WCI data is truly lazy-loaded via OS page cache
- get_image processes in chunks to avoid loading entire dataset
- Only the requested pages are loaded from disk
"""

from typing import Dict, Union

import numpy

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


MMAP_FORMAT_VERSION: str = '3.0'

class MmapDataBackend(themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base.EchogramDataBackend):
    """
    Backend using memory-mapped files for ultra-fast random access.

    This backend stores data in a simple directory structure:
    - wci_data.bin: Raw float32 array (n_pings × max_samples)
    - metadata.json: All metadata and ping parameters

    Memory-mapped access means:
    - Zero decompression overhead
    - OS handles caching via page cache (truly lazy loading)
    - Instant random access (10-100x faster than Zarr for scattered reads)
    - File size = raw data size (no compression)
    - Supports larger-than-memory files (only accessed pages are loaded)
    """

    def __init__(self, store_path: str, wci_mmap: numpy.memmap, metadata: Dict):
        """
        Initialize MmapDataBackend.

        Prefer using the `from_path` factory method or `EchogramBuilder.from_mmap()`.

        Args:
            store_path: Path to the mmap store directory.
            wci_mmap: Memory-mapped WCI data array (lazy-loaded by OS).
            metadata: Dictionary containing all metadata.
        """

    @classmethod
    def from_path(cls, path: str) -> MmapDataBackend:
        """
        Load a MmapDataBackend from a store directory.

        The WCI data is memory-mapped with mode='r' (read-only), meaning:
        - No data is loaded into memory until accessed
        - OS page cache handles all caching efficiently
        - Supports files larger than available RAM

        Args:
            path: Path to the mmap store directory.

        Returns:
            MmapDataBackend instance with lazy-loaded data.
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

    def get_ping_params(self) -> dict[str, tuple[str, tuple[numpy.ndarray, numpy.ndarray]]]:
        """
        Return pre-computed ping parameters.

        Returns:
            Dict mapping param name to (y_reference, (timestamps, values)).
        """

    def get_column(self, ping_index: int) -> numpy.ndarray:
        """Get beam-averaged water column data for a single ping."""

    def get_raw_column(self, ping_index: int) -> numpy.ndarray:
        """Get raw water column data (same as get_column for mmap)."""

    def get_chunk(self, start_ping: int, end_ping: int) -> numpy.ndarray:
        """
        Get a chunk of WCI data for multiple consecutive pings.

        Optimized for MmapDataBackend - direct slice from memory-mapped file.

        Args:
            start_ping: First ping index (inclusive).
            end_ping: Last ping index (exclusive).

        Returns:
            2D array of shape (end_ping - start_ping, n_samples).
        """

    def get_image(self, request: themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers.EchogramImageRequest) -> numpy.ndarray:
        """
        Build a complete echogram image from a request.

        Uses memory-mapped scattered access for ultra-fast loading.
        Processes in chunks to limit memory usage for large datasets.

        Memory usage: O(chunk_size * ny) + O(nx * ny) for output

        Args:
            request: Image request with ping mapping and affine parameters.

        Returns:
            2D array of shape (nx, ny) with echogram data (ping, sample).
        """

    @property
    def store_path(self) -> str:
        """Path to the mmap store directory."""

    def __repr__(self) -> str: ...

    __abstractmethods__: frozenset = ...
