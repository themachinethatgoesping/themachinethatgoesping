"""
Backend for gridded echogram data on a regular grid using memory-mapped files.

Gridded mmap stores data downsampled onto a regular (x, y) grid where:
- Y-axis (depth/range) has fixed step size, with 0 as a cell center
- X-axis is sparse: only occupied bins are stored (empty bins omitted)
- All rows have the same number of y cells (no padding)

Grid alignment: cell i has center at i * step.  Edges at (i - 0.5) * step
to (i + 0.5) * step.  This makes grids from different time ranges combinable.

Trade-offs vs regular mmap:
- Smaller files (downsampled)
- Faster get_image (uniform y → single index computation)
- Loss of original resolution
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


GRIDDED_MMAP_FORMAT_VERSION: str = '1.0'

AVERAGING_MODES: dict = ...

class GriddedMmapBackend(themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base.EchogramDataBackend):
    """
    Backend for gridded echogram data stored as memory-mapped files.

    All rows share the same y-grid (uniform depth/range bins), enabling a
    simplified and faster ``get_image`` implementation that computes the
    y-index mapping only once.

    Store layout::

        store_dir/
            wci_data.bin            # (n_x_bins, n_y_cells) float32
            metadata.json
            bin_x_coordinates.npy   # (n_x_bins,) float64
            ping_times.npy          # alias for bin_x_coordinates when x=time
            ping_counts.npy         # (n_x_bins,) int32  source pings per bin
            [latitudes.npy]
            [longitudes.npy]
            [ping_param_{name}_times.npy]
            [ping_param_{name}_values.npy]
    """

    def __init__(self, store_path: str, wci_mmap: numpy.memmap, metadata: Dict): ...

    @classmethod
    def from_path(cls, path: str) -> GriddedMmapBackend:
        """Load a GriddedMmapBackend from a store directory."""

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
    def latitudes(self) -> Union[numpy.ndarray, None]: ...

    @property
    def longitudes(self) -> Union[numpy.ndarray, None]: ...

    @property
    def wci_value(self) -> str: ...

    @property
    def linear_mean(self) -> bool: ...

    @property
    def storage_mode(self) -> themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.storage_mode.StorageAxisMode: ...

    @property
    def store_path(self) -> str: ...

    @property
    def x_step(self) -> float: ...

    @property
    def y_step(self) -> float: ...

    @property
    def y_origin(self) -> float: ...

    @property
    def n_y_cells(self) -> int: ...

    @property
    def bin_x_coordinates(self) -> numpy.ndarray: ...

    @property
    def ping_counts(self) -> Union[numpy.ndarray, None]: ...

    @property
    def averaging(self) -> str: ...

    def get_ping_params(self) -> dict[str, tuple[str, tuple[numpy.ndarray, numpy.ndarray]]]: ...

    def get_column(self, ping_index: int) -> numpy.ndarray: ...

    def get_raw_column(self, ping_index: int) -> numpy.ndarray: ...

    def get_chunk(self, start_ping: int, end_ping: int) -> numpy.ndarray: ...

    def get_image(self, request: themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers.EchogramImageRequest) -> numpy.ndarray:
        """
        Build echogram image exploiting the uniform y-grid.

        Since all rows share the same y-extent, the sample-index mapping is
        computed once and reused for every x-column.
        """

    __abstractmethods__: frozenset = ...
