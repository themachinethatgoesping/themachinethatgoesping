"""
MapBuilder class for managing multiple map layers.

Provides a unified interface for loading, combining, and displaying
multiple geospatial data layers. Acts as a data provider with axis/resolution
control, similar to EchogramBuilder.

The MapBuilder controls:
- Layer management (add, remove, visibility, ordering)
- Axis/resolution settings for data retrieval
- Coordinate system handling

Rendering properties (colormap, opacity, blending) are handled by the viewer.
"""

import dataclasses
from typing import Union

import numpy

import themachinethatgoesping.pingprocessing.overview.map_builder.backends.base
from themachinethatgoesping.pingprocessing.overview.map_builder.backends.base import (
    MapDataBackend as MapDataBackend
)
from themachinethatgoesping.pingprocessing.overview.map_builder.backends.geotiff_backend import (
    GeoTiffBackend as GeoTiffBackend
)
import themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system
from themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system import (
    BoundingBox as BoundingBox,
    MapCoordinateSystem as MapCoordinateSystem
)


class MapLayer:
    """
    Configuration for a single map layer.

    Attributes:
        backend: The data backend for this layer.
        name: Display name for the layer.
        visible: Whether the layer is currently visible.
        z_order: Rendering order (higher = on top).
    """

    visible: bool = True

    z_order: int = 0

    __dataclass_params__: dataclasses._DataclassParams = ...

    __annotations_cache__: dict = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, backend: themachinethatgoesping.pingprocessing.overview.map_builder.backends.base.MapDataBackend, name: str, visible: bool = True, z_order: int = 0) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ('backend', 'name', 'visible', 'z_order')

class MapBuilder:
    """
    Builder for managing multiple map layers.

    MapBuilder provides:
    - Layer management (add, remove, reorder, visibility)
    - Axis/resolution control for data retrieval
    - Coordinate system handling

    Similar to EchogramBuilder, it acts as a data provider.
    Rendering properties are controlled by the viewer.

    Example usage:
        from themachinethatgoesping.pingprocessing.overview.map_builder import MapBuilder
        from themachinethatgoesping.pingprocessing.widgets import MapViewerPyQtGraph

        # Create builder and add layers
        builder = MapBuilder()
        builder.add_geotiff('map/BPNS_latlon.tiff', name="Bathymetry")

        # Set axis/resolution
        builder.set_axis(max_pixels=(1000, 1000))

        # Create viewer (handles colorscale, opacity, blending)
        viewer = MapViewerPyQtGraph(builder)
    """

    def __init__(self):
        """Initialize an empty MapBuilder."""

    def set_axis_latlon(self, min_lat: float = float('nan'), max_lat: float = float('nan'), min_lon: float = float('nan'), max_lon: float = float('nan'), max_pixels: tuple[int, int] = (2000, 2000)) -> MapBuilder:
        """
        Set axis extent in lat/lon coordinates.

        Similar to EchogramBuilder's set_x_axis_date_time pattern.
        Use np.nan for auto-detection from data bounds.

        Args:
            min_lat: Minimum latitude (nan = auto from data).
            max_lat: Maximum latitude (nan = auto from data).
            min_lon: Minimum longitude (nan = auto from data).
            max_lon: Maximum longitude (nan = auto from data).
            max_pixels: Maximum output size (height, width).

        Returns:
            Self for method chaining.
        """

    def set_axis_utm(self, min_easting: float = float('nan'), max_easting: float = float('nan'), min_northing: float = float('nan'), max_northing: float = float('nan'), max_pixels: tuple[int, int] = (2000, 2000)) -> MapBuilder:
        """
        Set axis extent in UTM/projected coordinates.

        Similar to EchogramBuilder's axis-setting pattern.
        Use np.nan for auto-detection from data bounds.

        Args:
            min_easting: Minimum easting (nan = auto from data).
            max_easting: Maximum easting (nan = auto from data).
            min_northing: Minimum northing (nan = auto from data).
            max_northing: Maximum northing (nan = auto from data).
            max_pixels: Maximum output size (height, width).

        Returns:
            Self for method chaining.
        """

    def set_axis(self, bounds: Union[themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, None] = None, max_pixels: Union[tuple[int, int], None] = None) -> MapBuilder:
        """
        Set axis extent and resolution for data retrieval (legacy method).

        For more explicit control, use set_axis_latlon() or set_axis_utm().

        Args:
            bounds: Bounding box in world coordinates (None = full extent).
            max_pixels: Maximum output size (height, width) for downsampling.

        Returns:
            Self for method chaining.
        """

    def set_bounds(self, bounds: themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox) -> MapBuilder:
        """Set the current view bounds."""

    def set_max_pixels(self, max_pixels: tuple[int, int]) -> MapBuilder:
        """Set maximum output resolution."""

    def reset_bounds(self) -> MapBuilder:
        """Reset bounds to full extent."""

    @property
    def max_pixels(self) -> tuple[int, int]:
        """Current max pixels setting."""

    @property
    def current_bounds(self) -> Union[themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, None]:
        """Current view bounds (None = full extent)."""

    def add_layer(self, backend: themachinethatgoesping.pingprocessing.overview.map_builder.backends.base.MapDataBackend, name: Union[str, None] = None, visible: bool = True, z_order: Union[int, None] = None) -> MapBuilder:
        """
        Add a data layer.

        Args:
            backend: The data backend for this layer.
            name: Display name (default: backend feature name).
            visible: Whether layer is initially visible.
            z_order: Render order (default: next available).

        Returns:
            Self for method chaining.
        """

    def add_geotiff(self, path: str, name: Union[str, None] = None, band: int = 1, **kwargs) -> MapBuilder:
        """
        Add a GeoTiff layer.

        Convenience method that creates a GeoTiffBackend and adds it.

        Args:
            path: Path to the GeoTiff file.
            name: Display name (default: inferred from file).
            band: Band number to read (1-indexed).
            **kwargs: Additional arguments for add_layer().

        Returns:
            Self for method chaining.
        """

    def remove_layer(self, name: str) -> MapBuilder:
        """Remove a layer by name."""

    def get_layer(self, name: str) -> Union[MapLayer, None]:
        """Get a layer by name."""

    def set_layer_visibility(self, name: str, visible: bool) -> MapBuilder:
        """Set visibility of a layer."""

    def set_layer_order(self, name: str, z_order: int) -> MapBuilder:
        """Set rendering order of a layer."""

    @property
    def layers(self) -> list[MapLayer]:
        """List of all layers (sorted by z-order)."""

    @property
    def visible_layers(self) -> list[MapLayer]:
        """List of visible layers (sorted by z-order)."""

    @property
    def combined_bounds(self) -> Union[themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, None]:
        """Get combined bounding box of all visible layers."""

    @property
    def primary_coordinate_system(self) -> Union[themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.MapCoordinateSystem, None]:
        """Get coordinate system from the first layer."""

    def get_layer_data(self, layer_name: str, bounds: Union[themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, None] = None, max_size: Union[tuple[int, int], None] = None) -> Union[tuple[numpy.ndarray, themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.MapCoordinateSystem], None]:
        """
        Get data for a single layer.

        Args:
            layer_name: Name of the layer.
            bounds: Bounding box (None = use current_bounds or full extent).
            max_size: Maximum output size (None = use max_pixels setting).

        Returns:
            Tuple of (data array, coordinate system) or None if layer not found.
        """

    def get_all_layer_data(self, bounds: Union[themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, None] = None, max_size: Union[tuple[int, int], None] = None) -> list[tuple[MapLayer, numpy.ndarray, themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.MapCoordinateSystem]]:
        """
        Get data for all visible layers.

        Args:
            bounds: Bounding box (None = use current_bounds or full extent).
            max_size: Maximum output size (None = use max_pixels setting).

        Returns:
            List of (layer, data array, coordinate system) tuples.
        """

    def get_value_at_position(self, lat: float, lon: float) -> dict[str, Union[float, None]]:
        """Get values from all layers at a lat/lon position."""

    def close(self) -> None:
        """Close all backends and release resources."""

    def __enter__(self): ...

    def __exit__(self, exc_type, exc_val, exc_tb): ...

    def __repr__(self) -> str: ...
