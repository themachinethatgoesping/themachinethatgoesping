"""
Fast web-map tiles for the map viewer.

Thin wrapper around two maintained packages:

* **contextily** – parallel tile download (``n_connections``), on-disk caching and
  Web-Mercator → lat/lon reprojection (``warp_tiles``).
* **xyzservices** – maintained catalogue of XYZ tile providers (OSM, Esri, CartoDB, …).

The builder returns RGBA images already reprojected to linear lat/lon (WGS84) so they
line up with the map viewer's lat/lon axes.

Sources cover street/imagery maps, hybrids (imagery + labels/seamarks, alpha-composited),
ocean/bathymetry (GEBCO, EMODnet, Esri Ocean), near-real-time satellite and science layers
(NASA GIBS VIIRS/MODIS true colour, sea-surface temperature, chlorophyll, night lights) and
cloud-free Sentinel-2. See :data:`TILE_SOURCES` for the full list.

Example::

    from themachinethatgoesping.pingprocessing.overview.map_builder import TileBuilder
    tiles = TileBuilder()
    tiles.set_source("imagery_seamarks")  # or "esri_hybrid", "gebco",
                                          # "nasa_viirs_truecolor" (near-real-time), "nasa_sst", ...
    image, bounds = tiles.get_image_with_bounds(bbox, target_size=(1200, 900))
"""

import dataclasses

import numpy

from themachinethatgoesping.pingprocessing.overview.map_builder.coordinate_system import (
    BoundingBox as BoundingBox
)


__conditional_annotations__: set = ...

HAS_TILES: bool = True

DEFAULT_N_CONNECTIONS: int = 16

TILE_SOURCES: dict = ...

OVERLAY_SOURCES: dict = ...

def list_available_sources() -> List[str]:
    """List the names of the available pre-defined (base) tile sources."""

def list_overlay_sources() -> List[str]:
    """List the names of the available transparent overlay sources."""

class TileSource:
    """
    Lightweight description of a custom XYZ tile source.

    Kept for backwards compatibility; :meth:`TileBuilder.add_source` also accepts an
    :class:`xyzservices.TileProvider` directly.
    """

    attribution: str = ''

    max_zoom: int = 19

    min_zoom: int = 0

    tile_size: int = 256

    def to_provider(self):
        """Convert to an :class:`xyzservices.TileProvider`."""

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, url_template: str, attribution: str = '', max_zoom: int = 19, min_zoom: int = 0, tile_size: int = 256, headers: Dict[str, str] = ...) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

class TileBuilder:
    """
    Fetch and composite web-map tiles for a lat/lon view.

    Sources are :class:`xyzservices.TileProvider` objects (see :data:`TILE_SOURCES` for the
    presets). Tiles are downloaded in parallel and cached on disk by contextily; the returned
    images are reprojected to linear lat/lon (WGS84).
    """

    def __init__(self, cache_dir: Optional[Path] = None, n_connections: int = 16, max_pixels: Tuple[int, int] = (2000, 2000)) -> None: ...

    @property
    def source_names(self) -> List[str]: ...

    @property
    def sources(self) -> List[object]: ...

    @property
    def visible_sources(self) -> List[object]: ...

    @property
    def active_source_name(self) -> Optional[str]:
        """Name of the first visible source, or ``None`` if no source is active."""

    def add_source(self, source, name: Optional[str] = None, visible: bool = True) -> 'TileBuilder':
        """
        Add a tile source.

        *source* may be an :class:`xyzservices.TileProvider`, a :class:`TileSource`, or a list of
        providers (base first) that are alpha-composited into a hybrid.
        """

    def add_preset(self, name: str) -> 'TileBuilder':
        """Add a pre-defined source (or overlay) from the catalogue by name."""

    def add_xyz(self, name: str, url_template: str, attribution: str = '', max_zoom: int = 19, **kwargs) -> 'TileBuilder':
        """Add a custom XYZ source from a ``{z}/{x}/{y}`` URL template."""

    def set_source(self, name: str) -> 'TileBuilder':
        """Use a single preset source (clears any others)."""

    def add_osm(self) -> 'TileBuilder': ...

    def add_esri_worldimagery(self) -> 'TileBuilder': ...

    def add_esri_ocean(self) -> 'TileBuilder': ...

    def add_cartodb_positron(self) -> 'TileBuilder': ...

    def add_cartodb_darkmatter(self) -> 'TileBuilder': ...

    def add_opentopomap(self) -> 'TileBuilder': ...

    def set_source_visible(self, name: str, visible: bool) -> 'TileBuilder': ...

    def set_source_opacity(self, name: str, opacity: float) -> 'TileBuilder': ...

    def remove_source(self, name: str) -> 'TileBuilder': ...

    def clear_sources(self) -> 'TileBuilder': ...

    def set_layers(self, names: List[Optional[str]]) -> 'TileBuilder':
        """
        Set the ordered composite stack of active sources (base first).

        Each name is a key in :data:`TILE_SOURCES`; ``None`` / ``"None"`` entries are ignored.
        Replaces any previously active sources (used for the GUI base + overlay selection).
        """

    @property
    def active_layer_names(self) -> List[str]:
        """Names of the active (visible) sources, base first."""

    def is_time_dependent(self, name: Optional[str] = None) -> bool:
        """
        Whether *name* (or any active source, if None) depends on an acquisition date.
        """

    def set_axis_latlon(self, min_lat: float = float('nan'), max_lat: float = float('nan'), min_lon: float = float('nan'), max_lon: float = float('nan'), max_pixels: Optional[Tuple[int, int]] = None) -> 'TileBuilder':
        """Set the view extent in lat/lon (``np.nan`` = full extent)."""

    def set_bounds(self, bounds: BoundingBox) -> 'TileBuilder':
        """Set the current view bounds (lon as x, lat as y)."""

    def set_max_pixels(self, max_pixels: Tuple[int, int]) -> 'TileBuilder': ...

    def reset_bounds(self) -> 'TileBuilder': ...

    @property
    def max_pixels(self) -> Tuple[int, int]: ...

    @property
    def current_bounds(self) -> Optional[BoundingBox]: ...

    def set_time(self, time) -> 'TileBuilder':
        """
        Set the acquisition date for time-dependent layers.

        *time* may be a ``datetime`` / ``date``, an ISO ``"YYYY-MM-DD"`` string, or ``None`` for the
        latest available imagery. Non-time-dependent layers ignore it.
        """

    def get_time(self) -> Optional[str]: ...

    @property
    def time(self) -> Optional[str]: ...

    def get_image_with_bounds(self, bounds: BoundingBox, target_size: Tuple[int, int] = (800, 600), source_name: Optional[str] = None) -> Tuple[Optional[numpy.ndarray], BoundingBox]:
        """Return ``(rgba_image, actual_bounds)`` reprojected to linear lat/lon."""

    def get_image(self, bounds: BoundingBox, target_size: Tuple[int, int] = (800, 600), source_name: Optional[str] = None) -> Tuple[Optional[numpy.ndarray], BoundingBox]:
        """
        Return ``(rgba_image, bounds)`` (alias of :meth:`get_image_with_bounds`).
        """

    def build_image(self, source_name: Optional[str] = None) -> Tuple[Optional[numpy.ndarray], Optional[Tuple[float, float, float, float]]]:
        """
        Build a tile image for the current axis settings (EchogramBuilder-style).

        Returns ``(rgba_image, extent)`` with ``extent = (lon_min, lon_max, lat_min, lat_max)``,
        or ``(None, None)`` if no bounds are set or no tiles could be loaded.
        """

    def export_geotiff(self, path, bounds: BoundingBox, target_size: Tuple[int, int] = (4000, 4000), source_name: Optional[str] = None) -> Optional[str]:
        """
        Fetch *bounds* at *target_size* and save a georeferenced GeoTIFF (EPSG:4326).

        Returns the written path, or ``None`` if no tiles could be loaded.
        """

    @staticmethod
    def save_geotiff(path, image: numpy.ndarray, bounds: BoundingBox) -> str:
        """
        Write an RGBA lat/lon *image* (row 0 = north) to a georeferenced GeoTIFF (EPSG:4326).
        """

    def clear_cache(self) -> None:
        """Delete the on-disk tile cache."""
