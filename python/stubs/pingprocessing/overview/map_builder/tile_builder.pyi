import dataclasses
import pathlib
from typing import Union

import numpy

import themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system
from themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system import (
    BoundingBox as BoundingBox
)


HAS_REQUESTS: bool = True

HAS_PIL: bool = True

class TileSource:
    """
    Configuration for a tile source.

    Attributes:
        name: Display name of the source.
        url_template: URL template with {z}, {x}, {y} placeholders.
        attribution: Attribution text (required by most providers).
        max_zoom: Maximum zoom level (typically 18-19).
        min_zoom: Minimum zoom level (typically 0).
        tile_size: Tile size in pixels (typically 256).
        headers: Optional HTTP headers for requests.
    """

    attribution: str = ''

    max_zoom: int = 19

    min_zoom: int = 0

    tile_size: int = 256

    visible: bool = True

    opacity: float = 1.0

    __dataclass_params__: dataclasses._DataclassParams = ...

    __annotations_cache__: dict = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, url_template: str, attribution: str = '', max_zoom: int = 19, min_zoom: int = 0, tile_size: int = 256, headers: dict[str, str] = ..., visible: bool = True, opacity: float = 1.0) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

TILE_SOURCES: dict = ...

def list_available_sources() -> list[str]:
    """List available pre-defined tile sources."""

class TileCache:
    """Simple disk-based tile cache."""

    def __init__(self, cache_dir: Union[pathlib.Path, None] = None):
        """
        Initialize tile cache.

        Args:
            cache_dir: Directory for cached tiles. If None, uses ~/.cache/pingprocessing/tiles
        """

    def get(self, source_name: str, z: int, x: int, y: int) -> Union[numpy.ndarray, None]:
        """Get tile from cache (memory or disk)."""

    def put(self, source_name: str, z: int, x: int, y: int, data: numpy.ndarray) -> None:
        """Store tile in cache (memory and disk)."""

    def clear_memory(self) -> None:
        """Clear memory cache."""

    def clear_disk(self, source_name: Union[str, None] = None) -> None:
        """Clear disk cache for a source or all sources."""

def latlon_to_tile(lat: float, lon: float, zoom: int) -> tuple[int, int]:
    """
    Convert lat/lon to tile coordinates at given zoom level.

    Uses Web Mercator (EPSG:3857) tile scheme.
    """

def tile_to_latlon(x: int, y: int, zoom: int) -> tuple[float, float]:
    """Convert tile coordinates to lat/lon (top-left corner)."""

def tile_bounds_latlon(x: int, y: int, zoom: int) -> themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox:
    """Get bounding box of a tile in lat/lon."""

def lat_to_mercator_y(lat: float) -> float:
    """
    Convert latitude to Web Mercator y coordinate (in degrees equivalent).

    Web Mercator uses the Spherical Mercator projection where:
    y = R * ln(tan(pi/4 + lat/2))

    We express this in "degree equivalents" so it can be compared with longitude.
    """

def mercator_y_to_lat(y: float) -> float:
    """Convert Web Mercator y coordinate back to latitude."""

def reproject_mercator_to_latlon(image: numpy.ndarray, merc_bounds: themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, target_bounds: themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, target_size: tuple[int, int]) -> numpy.ndarray:
    """
    Reproject a Web Mercator image to linear lat/lon coordinates.

    Web Mercator tiles have pixels uniformly spaced in Mercator y-coordinate,
    not in latitude. This function resamples the image so pixels are uniformly
    spaced in latitude, allowing correct display with linear lat/lon axes.

    Args:
        image: Input RGBA image in Web Mercator projection.
        merc_bounds: Bounds in lat/lon of the Mercator image.
        target_bounds: Desired output bounds in lat/lon.
        target_size: Output size as (width, height).

    Returns:
        Reprojected RGBA image with pixels uniformly spaced in lat/lon.
    """

def choose_zoom_level(bounds: themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, target_size: tuple[int, int], tile_size: int = 256) -> int:
    """Choose appropriate zoom level for given bounds and target size."""

class TileBuilder:
    """
    Builder for fetching and compositing web map tiles.

    TileBuilder handles:
    - Multiple tile sources (OSM, ESRI, etc.)
    - Tile fetching with disk caching
    - Compositing tiles for arbitrary view bounds

    Unlike MapBuilder's numerical data, tiles are pre-rendered RGBA images.
    No colormap/colorbar is needed.

    Example:
        tiles = TileBuilder()
        tiles.add_osm()  # Add OpenStreetMap tiles

        # Get composited image for a region
        image = tiles.get_image(bounds, target_size=(800, 600))
    """

    def __init__(self, cache_dir: Union[pathlib.Path, None] = None):
        """
        Initialize TileBuilder.

        Args:
            cache_dir: Directory for tile cache. Default: ~/.cache/pingprocessing/tiles
        """

    def set_axis_latlon(self, min_lat: float = float('nan'), max_lat: float = float('nan'), min_lon: float = float('nan'), max_lon: float = float('nan'), max_pixels: Union[tuple[int, int], None] = None) -> TileBuilder:
        """
        Set axis extent in lat/lon coordinates.

        Similar to MapBuilder/EchogramBuilder pattern.
        Use np.nan for auto-detection (full world).

        Args:
            min_lat: Minimum latitude (-85.05 = Web Mercator limit).
            max_lat: Maximum latitude (85.05 = Web Mercator limit).
            min_lon: Minimum longitude (-180).
            max_lon: Maximum longitude (180).
            max_pixels: Maximum output size (height, width).

        Returns:
            Self for method chaining.
        """

    def set_bounds(self, bounds: themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox) -> TileBuilder:
        """
        Set the current view bounds (in lat/lon).

        Args:
            bounds: BoundingBox with lon as x, lat as y.

        Returns:
            Self for method chaining.
        """

    def set_max_pixels(self, max_pixels: tuple[int, int]) -> TileBuilder:
        """
        Set maximum output resolution (height, width).

        Args:
            max_pixels: Maximum size as (height, width) tuple.

        Returns:
            Self for method chaining.
        """

    def reset_bounds(self) -> TileBuilder:
        """Reset bounds to full Web Mercator extent."""

    @property
    def max_pixels(self) -> tuple[int, int]:
        """Current max pixels setting (height, width)."""

    @property
    def current_bounds(self) -> Union[themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, None]:
        """Current view bounds in lat/lon (None = not set)."""

    def add_source(self, source: TileSource) -> TileBuilder:
        """
        Add a tile source.

        Args:
            source: TileSource configuration.
        """

    def add_xyz(self, name: str, url_template: str, attribution: str = '', max_zoom: int = 19, **kwargs) -> TileBuilder:
        """
        Add a custom XYZ tile source.

        Args:
            name: Display name.
            url_template: URL with {z}, {x}, {y} placeholders.
            attribution: Attribution text.
            max_zoom: Maximum zoom level.
        """

    def add_preset(self, preset_name: str) -> TileBuilder:
        """
        Add a pre-defined tile source.

        Args:
            preset_name: Name from TILE_SOURCES (e.g., 'osm', 'esri_worldimagery').
        """

    def add_osm(self) -> TileBuilder:
        """Add OpenStreetMap tiles."""

    def add_esri_worldimagery(self) -> TileBuilder:
        """Add ESRI World Imagery (satellite)."""

    def add_esri_ocean(self) -> TileBuilder:
        """Add ESRI Ocean Basemap."""

    def add_esri_natgeo(self) -> TileBuilder:
        """Add ESRI National Geographic."""

    def add_cartodb_positron(self) -> TileBuilder:
        """Add CartoDB Positron (light theme)."""

    def add_cartodb_darkmatter(self) -> TileBuilder:
        """Add CartoDB Dark Matter (dark theme)."""

    def add_opentopomap(self) -> TileBuilder:
        """Add OpenTopoMap (topographic)."""

    @property
    def sources(self) -> list[TileSource]:
        """List of all tile sources."""

    @property
    def source_names(self) -> list[str]:
        """List of source names."""

    @property
    def visible_sources(self) -> list[TileSource]:
        """List of visible tile sources."""

    def set_source_visible(self, name: str, visible: bool) -> TileBuilder:
        """Set visibility of a source."""

    def set_source_opacity(self, name: str, opacity: float) -> TileBuilder:
        """Set opacity of a source (0.0 - 1.0)."""

    def remove_source(self, name: str) -> TileBuilder:
        """Remove a tile source."""

    def clear_sources(self) -> TileBuilder:
        """Remove all tile sources."""

    def set_source(self, preset_name: str) -> TileBuilder:
        """
        Set a single tile source (clears others and adds this one).

        Convenience method for simple single-source usage.

        Args:
            preset_name: Name from TILE_SOURCES (e.g., 'osm', 'esri_worldimagery').
        """

    def get_image(self, bounds: themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, target_size: tuple[int, int] = (800, 600), source_name: Union[str, None] = None) -> tuple[Union[numpy.ndarray, None], themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox]:
        """
        Get composited tile image for given bounds.

        Args:
            bounds: Bounding box in lat/lon (WGS84).
            target_size: Desired output size (width, height) in pixels.
            source_name: Specific source to use, or None for first visible.

        Returns:
            Tuple of (RGBA image array, actual bounds covered).
            Returns (None, bounds) if no tiles could be loaded.
        """

    def get_image_with_bounds(self, bounds: themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox, target_size: tuple[int, int] = (800, 600), source_name: Union[str, None] = None) -> tuple[Union[numpy.ndarray, None], themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system.BoundingBox]:
        """
        Get composited tile image reprojected to linear lat/lon coordinates.

        Web Mercator tiles have non-linear latitude spacing. This method 
        reprojects the tiles to have uniform lat/lon pixel spacing, allowing
        correct display with simple setRect positioning.

        Args:
            bounds: Bounding box in lat/lon (WGS84) - the requested area.
            target_size: Desired output size (width, height) in pixels.
            source_name: Specific source to use, or None for first visible.

        Returns:
            Tuple of (RGBA image array, bounds).
            The image is reprojected to linear lat/lon matching the returned bounds.
            Returns (None, bounds) if no tiles could be loaded.
        """

    def build_image(self, source_name: Union[str, None] = None) -> tuple[Union[numpy.ndarray, None], Union[tuple[float, float, float, float], None]]:
        """
        Build a tile image for the current axis settings.

        This is the main interface following the EchogramBuilder pattern.
        Call set_axis_latlon() or set_bounds() + set_max_pixels() first.

        The returned extent tuple is (xmin, xmax, ymin, ymax) for use with
        PyQtGraph's ImageItem.setRect() (like EchogramBuilder).

        Args:
            source_name: Specific source to use, or None for first visible.

        Returns:
            Tuple of (RGBA image array, extent).
            extent is (lon_min, lon_max, lat_min, lat_max) in lat/lon coordinates.
            Returns (None, None) if no bounds set or no tiles could be loaded.

        Example:
            tiles = TileBuilder()
            tiles.add_osm()

            # Set view region
            tiles.set_axis_latlon(min_lat=51.0, max_lat=52.0,
                                  min_lon=2.5, max_lon=3.5,
                                  max_pixels=(800, 600))

            # Build image
            image, extent = tiles.build_image()
            # extent = (lon_min, lon_max, lat_min, lat_max)
        """
