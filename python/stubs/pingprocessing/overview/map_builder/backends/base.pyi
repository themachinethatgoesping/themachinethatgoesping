"""
Abstract base class for map data backends.

Defines the interface that all map data sources must implement,
including coordinate system access, data retrieval, and downsampling.
"""

import abc
from typing import Any, Union

import numpy

import themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system
from themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system import (
    BoundingBox as BoundingBox,
    MapCoordinateSystem as MapCoordinateSystem
)


class MapDataBackend(abc.ABC):
    """
    Abstract base class for map data sources.

    Backends handle loading and accessing geospatial raster data from
    various sources (GeoTiff, NetCDF, Zarr, etc.). They provide:

    - Coordinate system information (CRS, transform, bounds)
    - Feature/variable names for colormap selection
    - Data retrieval with optional downsampling
    - Memory-efficient access for large-than-memory datasets

    Each backend manages its own memory (caching, lazy loading, etc.)
    and must handle data retrieval efficiently for interactive visualization.
    """

    @property
    def coordinate_system(self) -> themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.MapCoordinateSystem:
        """
        Get the coordinate system for this data.

        Returns:
            MapCoordinateSystem with CRS, transform, and bounds.
        """

    @property
    def feature_name(self) -> str:
        """
        Get the feature/variable name (e.g., 'bathymetry', 'backscatter').

        Used for automatic colormap selection and display labeling.

        Returns:
            String identifier for the data type.
        """

    @property
    def bounds(self) -> themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox:
        """
        Get the bounding box in world coordinates.

        Returns:
            BoundingBox with (xmin, ymin, xmax, ymax) in native CRS.
        """

    @property
    def shape(self) -> tuple[int, int]:
        """
        Get the raster shape (height, width) in pixels.

        Returns:
            Tuple of (height, width).
        """

    @property
    def nodata(self) -> Union[float, None]:
        """
        Get the nodata value, or None if not defined.

        Returns:
            Nodata value used to mark invalid/missing pixels.
        """

    @property
    def dtype(self) -> numpy.dtype:
        """
        Get the data type of raster values.

        Returns:
            NumPy dtype of the data.
        """

    @property
    def units(self) -> Union[str, None]:
        """
        Get the units of the data values (e.g., 'm', 'dB').

        Returns:
            Unit string or None if not defined.
        """

    @property
    def min_value(self) -> Union[float, None]:
        """
        Get the minimum data value (for colormap scaling).

        Returns:
            Minimum value or None if not known.
        """

    @property
    def max_value(self) -> Union[float, None]:
        """
        Get the maximum data value (for colormap scaling).

        Returns:
            Maximum value or None if not known.
        """

    @property
    def metadata(self) -> dict[str, Any]:
        """
        Get additional metadata as a dictionary.

        Returns:
            Dictionary of metadata (empty by default).
        """

    def get_data(self, bounds: Union[themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, None] = None, max_size: Union[tuple[int, int], None] = None) -> tuple[numpy.ndarray, themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.MapCoordinateSystem]:
        """
        Get raster data for a region with optional downsampling.

        This is the primary data retrieval method. Backends should:
        - Return only the requested region (or full extent if bounds=None)
        - Downsample if the region is larger than max_size
        - Handle memory efficiently (don't load entire file if not needed)
        - Replace nodata values with NaN for float output

        Args:
            bounds: Bounding box in world coordinates. If None, return full extent.
            max_size: Maximum output size as (height, width). If the requested
                     region is larger, downsample to fit. If None, return at
                     full resolution.

        Returns:
            Tuple of:
            - 2D NumPy array with data values (NaN for nodata)
            - MapCoordinateSystem for the returned data (may differ from original
              if subregion or downsampled)
        """

    def get_value_at(self, x: float, y: float) -> Union[float, None]:
        """
        Get the data value at a world coordinate.

        Args:
            x: X coordinate in world CRS.
            y: Y coordinate in world CRS.

        Returns:
            Data value at the point, or None if outside bounds or nodata.
        """

    def get_data_at_latlon(self, lat: float, lon: float) -> Union[float, None]:
        """
        Get the data value at a lat/lon coordinate.

        Args:
            lat: Latitude in degrees.
            lon: Longitude in degrees.

        Returns:
            Data value at the point, or None if outside bounds or nodata.
        """

    def get_overview(self, max_size: tuple[int, int] = (1000, 1000)) -> tuple[numpy.ndarray, themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.MapCoordinateSystem]:
        """
        Get a downsampled overview of the entire dataset.

        Useful for initial display before zooming to regions of interest.

        Args:
            max_size: Maximum size as (height, width).

        Returns:
            Tuple of (data array, coordinate system).
        """

    def close(self) -> None:
        """
        Release any resources held by the backend.

        Override this if your backend holds open file handles or connections.
        Default implementation does nothing.
        """

    def __enter__(self):
        """Context manager entry."""

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - closes the backend."""

    def compute_downsample_factor(self, bounds: themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, max_size: tuple[int, int]) -> int:
        """
        Compute the downsample factor needed to fit bounds within max_size.

        Args:
            bounds: Requested region bounds.
            max_size: Maximum output size (height, width).

        Returns:
            Downsample factor (1 = no downsampling, 2 = half resolution, etc.)
        """

    def __repr__(self) -> str: ...

    __abstractmethods__: frozenset = ...
