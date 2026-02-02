"""
Coordinate system management for map data.

Provides CRS transformations, affine coordinate mapping, and extent handling
for geospatial data visualization.
"""

import dataclasses
from typing import Union

import numpy


HAS_PYPROJ: bool = True

HAS_AFFINE: bool = True

class BoundingBox:
    """
    Bounding box in world coordinates.

    Attributes:
        xmin: Minimum x coordinate (west).
        ymin: Minimum y coordinate (south).
        xmax: Maximum x coordinate (east).
        ymax: Maximum y coordinate (north).
    """

    @property
    def width(self) -> float:
        """Width of the bounding box."""

    @property
    def height(self) -> float:
        """Height of the bounding box."""

    @property
    def center(self) -> tuple[float, float]:
        """Center point (x, y) of the bounding box."""

    def contains(self, x: float, y: float) -> bool:
        """Check if a point is within the bounding box."""

    def intersects(self, other: BoundingBox) -> bool:
        """Check if this bounding box intersects another."""

    def intersection(self, other: BoundingBox) -> Union['BoundingBox', None]:
        """
        Return the intersection of two bounding boxes, or None if no intersection.
        """

    def union(self, other: BoundingBox) -> BoundingBox:
        """Return the union (combined extent) of two bounding boxes."""

    def expand(self, factor: float) -> BoundingBox:
        """Return a new bounding box expanded by a factor around center."""

    def as_tuple(self) -> tuple[float, float, float, float]:
        """Return as (xmin, ymin, xmax, ymax) tuple."""

    @classmethod
    def from_points(cls, x: numpy.ndarray, y: numpy.ndarray) -> BoundingBox:
        """Create a bounding box from arrays of x and y coordinates."""

    __dataclass_params__: dataclasses._DataclassParams = ...

    __annotations_cache__: dict = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, xmin: float, ymin: float, xmax: float, ymax: float) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ('xmin', 'ymin', 'xmax', 'ymax')

class MapCoordinateSystem:
    """
    Coordinate system for map data with CRS transformations.

    Handles conversions between:
    - Pixel coordinates (row, col in raster)
    - World coordinates (in native CRS, e.g., UTM meters)
    - Geographic coordinates (latitude, longitude in WGS84)

    Attributes:
        crs: Coordinate Reference System (pyproj.CRS or EPSG code).
        transform: Affine transform from pixel to world coordinates.
        bounds: Bounding box in world coordinates.
    """

    def __init__(self, crs: Union[str, int, 'CRS'], transform: Affine, width: int, height: int):
        """
        Initialize coordinate system.

        Args:
            crs: Coordinate Reference System (EPSG code, WKT, or pyproj.CRS).
            transform: Affine transform from pixel to world coordinates.
                      Maps (col, row) to (x, y) in world coordinates.
            width: Raster width in pixels.
            height: Raster height in pixels.
        """

    @property
    def crs(self) -> CRS:
        """Coordinate Reference System."""

    @property
    def transform(self) -> Affine:
        """Affine transform from pixel to world coordinates."""

    @property
    def bounds(self) -> BoundingBox:
        """Bounding box in world coordinates."""

    @property
    def width(self) -> int:
        """Raster width in pixels."""

    @property
    def height(self) -> int:
        """Raster height in pixels."""

    @property
    def resolution(self) -> tuple[float, float]:
        """Pixel resolution (dx, dy) in world coordinate units."""

    @property
    def is_geographic(self) -> bool:
        """True if CRS uses geographic (lat/lon) coordinates."""

    @property
    def epsg(self) -> Union[int, None]:
        """EPSG code of the CRS, or None if not available."""

    def pixel_to_world(self, col: Union[float, numpy.ndarray], row: Union[float, numpy.ndarray]) -> tuple[Union[float, numpy.ndarray], Union[float, numpy.ndarray]]:
        """
        Convert pixel coordinates to world coordinates.

        Args:
            col: Column index (x in pixel space).
            row: Row index (y in pixel space).

        Returns:
            Tuple of (x, y) in world coordinates.
        """

    def world_to_pixel(self, x: Union[float, numpy.ndarray], y: Union[float, numpy.ndarray]) -> tuple[Union[float, numpy.ndarray], Union[float, numpy.ndarray]]:
        """
        Convert world coordinates to pixel coordinates.

        Args:
            x: X coordinate in world CRS.
            y: Y coordinate in world CRS.

        Returns:
            Tuple of (col, row) in pixel coordinates (float, may need rounding).
        """

    def world_to_latlon(self, x: Union[float, numpy.ndarray], y: Union[float, numpy.ndarray]) -> tuple[Union[float, numpy.ndarray], Union[float, numpy.ndarray]]:
        """
        Convert world coordinates to WGS84 lat/lon.

        Args:
            x: X coordinate in native CRS.
            y: Y coordinate in native CRS.

        Returns:
            Tuple of (latitude, longitude) in degrees.
        """

    def latlon_to_world(self, lat: Union[float, numpy.ndarray], lon: Union[float, numpy.ndarray]) -> tuple[Union[float, numpy.ndarray], Union[float, numpy.ndarray]]:
        """
        Convert WGS84 lat/lon to world coordinates.

        Args:
            lat: Latitude in degrees.
            lon: Longitude in degrees.

        Returns:
            Tuple of (x, y) in native CRS coordinates.
        """

    def latlon_to_pixel(self, lat: Union[float, numpy.ndarray], lon: Union[float, numpy.ndarray]) -> tuple[Union[float, numpy.ndarray], Union[float, numpy.ndarray]]:
        """
        Convert WGS84 lat/lon directly to pixel coordinates.

        Args:
            lat: Latitude in degrees.
            lon: Longitude in degrees.

        Returns:
            Tuple of (col, row) in pixel coordinates.
        """

    def pixel_to_latlon(self, col: Union[float, numpy.ndarray], row: Union[float, numpy.ndarray]) -> tuple[Union[float, numpy.ndarray], Union[float, numpy.ndarray]]:
        """
        Convert pixel coordinates to WGS84 lat/lon.

        Args:
            col: Column index.
            row: Row index.

        Returns:
            Tuple of (latitude, longitude) in degrees.
        """

    def get_pixel_bounds_for_world_extent(self, world_bounds: BoundingBox) -> tuple[int, int, int, int]:
        """
        Get pixel bounds (col_min, row_min, col_max, row_max) for a world extent.

        Args:
            world_bounds: Bounding box in world coordinates.

        Returns:
            Tuple of (col_min, row_min, col_max, row_max) clipped to raster extent.
        """

    def create_subregion(self, col_min: int, row_min: int, col_max: int, row_max: int) -> MapCoordinateSystem:
        """
        Create a new coordinate system for a subregion.

        Args:
            col_min: Minimum column index.
            row_min: Minimum row index.
            col_max: Maximum column index.
            row_max: Maximum row index.

        Returns:
            New MapCoordinateSystem for the subregion.
        """

    def create_downsampled(self, factor: int) -> MapCoordinateSystem:
        """
        Create a coordinate system for a downsampled version.

        Args:
            factor: Downsampling factor (e.g., 2 = half resolution).

        Returns:
            New MapCoordinateSystem with scaled transform.
        """

    def create_rotated_view(self, center_x: float, center_y: float, heading: float, view_width: int, view_height: int, resolution: float) -> tuple['MapCoordinateSystem', BoundingBox]:
        """
        Create a rotated coordinate system for track-up display.

        Creates a new coordinate system rotated around a center point,
        useful for displaying maps in ship-relative (track-up) orientation.

        Args:
            center_x: X coordinate of rotation center (world coords).
            center_y: Y coordinate of rotation center (world coords).
            heading: Heading in degrees (0=north, clockwise).
            view_width: Output view width in pixels.
            view_height: Output view height in pixels.
            resolution: Desired pixel resolution in world units.

        Returns:
            Tuple of (rotated coordinate system, source bounds needed).
        """

    def __repr__(self) -> str: ...
