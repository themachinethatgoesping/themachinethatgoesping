from typing import Any, Union

import numpy

import themachinethatgoesping.pingprocessing.overview.map_builder.backends.base
from themachinethatgoesping.pingprocessing.overview.map_builder.backends.base import (
    MapDataBackend as MapDataBackend
)
import themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system
from themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system import (
    BoundingBox as BoundingBox,
    MapCoordinateSystem as MapCoordinateSystem
)


HAS_RASTERIO: bool = True

class GeoTiffBackend(themachinethatgoesping.pingprocessing.overview.map_builder.backends.base.MapDataBackend):
    """
    Backend for loading data from GeoTiff files.

    Features:
    - Memory-efficient windowed reading (only loads requested regions)
    - Automatic use of internal overviews for downsampling
    - Support for multi-band files (reads first band by default)
    - Automatic nodata handling and NaN conversion

    Requires: rasterio (pip install rasterio)
    """

    def __init__(self, path: str, feature_name: Union[str, None] = None, band: int = 1, preload_stats: bool = True):
        """
        Open a GeoTiff file.

        Args:
            path: Path to the GeoTiff file.
            feature_name: Name of the feature/variable. If None, infers from
                         filename or defaults to 'raster'.
            band: Band number to read (1-indexed). Default is 1.
            preload_stats: If True, compute min/max from overviews or sampling.
        """

    @property
    def coordinate_system(self) -> themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.MapCoordinateSystem: ...

    @property
    def feature_name(self) -> str: ...

    @property
    def bounds(self) -> themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox: ...

    @property
    def shape(self) -> tuple[int, int]: ...

    @property
    def nodata(self) -> Union[float, None]: ...

    @property
    def dtype(self) -> numpy.dtype: ...

    @property
    def min_value(self) -> Union[float, None]: ...

    @property
    def max_value(self) -> Union[float, None]: ...

    @property
    def metadata(self) -> dict[str, Any]: ...

    def get_data(self, bounds: Union[themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, None] = None, max_size: Union[tuple[int, int], None] = None) -> tuple[numpy.ndarray, themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.MapCoordinateSystem]:
        """
        Get raster data for a region with optional downsampling.

        Uses rasterio's windowed reading for memory efficiency and
        built-in overview levels for fast downsampling.

        Args:
            bounds: Bounding box in world coordinates. If None, full extent.
            max_size: Maximum output size (height, width). Downsamples if needed.

        Returns:
            Tuple of (data array with NaN for nodata, coordinate system).
        """

    def get_value_at(self, x: float, y: float) -> Union[float, None]:
        """
        Get the data value at a world coordinate.

        Args:
            x: X coordinate in world CRS.
            y: Y coordinate in world CRS.

        Returns:
            Data value or None if outside bounds or nodata.
        """

    def get_data_along_track(self, x: numpy.ndarray, y: numpy.ndarray, interpolation: str = 'nearest') -> numpy.ndarray:
        """
        Get data values along a track (e.g., ship navigation).

        Efficiently samples data at multiple points, useful for
        extracting values along a navigation track.

        Args:
            x: Array of X coordinates in world CRS.
            y: Array of Y coordinates in world CRS.
            interpolation: 'nearest' or 'bilinear'.

        Returns:
            Array of data values (NaN for nodata/out-of-bounds).
        """

    def close(self) -> None:
        """Close the rasterio dataset."""

    def __del__(self):
        """Ensure dataset is closed on garbage collection."""

    @classmethod
    def from_path(cls, path: str, feature_name: Union[str, None] = None, band: int = 1) -> GeoTiffBackend:
        """
        Create a GeoTiffBackend from a file path.

        This is the recommended way to create a GeoTiffBackend.

        Args:
            path: Path to the GeoTiff file.
            feature_name: Optional feature name override.
            band: Band number (1-indexed).

        Returns:
            GeoTiffBackend instance.
        """

    __abstractmethods__: frozenset = ...
