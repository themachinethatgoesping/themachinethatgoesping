"""
PyQtGraph-based map viewer widget for Jupyter notebooks.

Provides interactive visualization of map layers with pan/zoom,
track overlays, and integration with echogram/WCI viewers.

The viewer handles:
- Colorscale, opacity, blending per data layer
- Background tiles from web sources (OSM, ESRI, CartoDB, etc.)
- Auto-update with debouncing on pan/zoom
- Track overlays with direct lat/lon coordinates
- Ping position markers from connected viewers

Example with data layers:
    from themachinethatgoesping.pingprocessing.widgets import MapViewerPyQtGraph
    from themachinethatgoesping.pingprocessing.overview.map_builder import MapBuilder

    builder = MapBuilder()
    builder.add_geotiff('map/BPNS_latlon.tiff')

    # Auto-displays in Jupyter (like EchogramViewer)
    viewer = MapViewerPyQtGraph(builder)

Example with background tiles:
    from themachinethatgoesping.pingprocessing.widgets import MapViewerPyQtGraph
    from themachinethatgoesping.pingprocessing.overview.map_builder import MapBuilder, TileBuilder

    # Data layer
    builder = MapBuilder()
    builder.add_geotiff('map/BPNS_latlon.tiff')

    # Background tiles
    tiles = TileBuilder()
    tiles.add_osm()  # or add_esri_worldimagery(), add_cartodb_positron(), etc.

    viewer = MapViewerPyQtGraph(builder, tile_builder=tiles)

    # Or change tile source programmatically
    viewer.set_tile_source('esri_worldimagery')  # Switch to satellite
    viewer.set_tile_visible(False)  # Hide tiles

Example tiles-only (no data layers):
    from themachinethatgoesping.pingprocessing.widgets import MapViewerPyQtGraph
    from themachinethatgoesping.pingprocessing.overview.map_builder import TileBuilder

    tiles = TileBuilder()
    tiles.add_osm()

    viewer = MapViewerPyQtGraph(tile_builder=tiles)
    viewer.connect_echogram_viewer(echogram_viewer)  # Just show tracks on tiles
"""

import dataclasses

import np
import pg

import themachinethatgoesping.pingprocessing.widgets.pyqtgraph_helpers as pgh


HAS_MATPLOTLIB: bool = True

class LayerRenderSettings:
    """
    Viewer-side rendering settings for a layer.

    These settings are controlled by the viewer, not the builder.
    """

    colormap: str = 'viridis'

    opacity: float = 1.0

    vmin: None = None

    vmax: None = None

    blend_mode: str = 'alpha'

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, colormap: str = 'viridis', opacity: float = 1.0, vmin: Optional[float] = None, vmax: Optional[float] = None, blend_mode: str = 'alpha') -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

class TrackInfo:
    """Track display information."""

    line_width: float = 2.0

    is_active: bool = False

    visible: bool = True

    slot_idx: None = None

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, latitudes: np.ndarray, longitudes: np.ndarray, color: str, line_width: float = 2.0, is_active: bool = False, visible: bool = True, slot_idx: Optional[int] = None) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

class OverviewTrackInfo:
    """
    Track backed by a PingOverview with zoom-adaptive downsampling.

    Instead of static lat/lon arrays the track is refreshed from
    ``overview.get_track_data()`` on every zoom change so that only a
    bounded number of points are sent to the renderer.
    """

    max_points: int = 50000

    line_width: float = 2.0

    is_active: bool = False

    visible: bool = True

    slot_idx: None = None

    show_points: bool = False

    point_size: float = 5.0

    point_symbol: str = 'o'

    point_outline: bool = True

    latitudes: None = None

    longitudes: None = None

    indices: None = None

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, overview: Any, color: str, max_points: int = 50000, line_width: float = 2.0, is_active: bool = False, visible: bool = True, slot_idx: Optional[int] = None, show_points: bool = False, point_size: float = 5.0, point_symbol: str = 'o', point_outline: bool = True, latitudes: Optional[np.ndarray] = None, longitudes: Optional[np.ndarray] = None, indices: Optional[np.ndarray] = None) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

class MapViewerPyQtGraph:
    """
    PyQtGraph-based map viewer for geospatial data.

    Features:
    - Interactive pan/zoom with mouse
    - Layer management with visibility/opacity/colorscale controls (viewer-side)
    - Auto-update with debouncing on pan/zoom (like EchogramViewer)
    - Track overlays showing navigation paths from echograms
    - Current ping position marker (larger points from WCI viewer)
    - Integration with EchogramViewerMultiChannel and WCIViewerMultiChannel
    - Coordinate display (lat/lon)

    The MapBuilder provides data; the viewer controls all rendering properties.

    Example:
        from themachinethatgoesping.pingprocessing.widgets import MapViewerPyQtGraph
        from themachinethatgoesping.pingprocessing.overview.map_builder import MapBuilder

        builder = MapBuilder()
        builder.add_geotiff('map/BPNS_latlon.tiff')

        # Auto-displays in Jupyter (like EchogramViewer)
        viewer = MapViewerPyQtGraph(builder)

        # Control rendering from viewer
        viewer.set_layer_colormap("BPNS_latlon", "terrain")
        viewer.set_layer_opacity("BPNS_latlon", 0.8)

        # Connect to echogram viewer - tracks are loaded automatically
        viewer.connect_echogram_viewer(echogram_viewer)
    """

    TRACK_COLORS: list = ...

    def __init__(self, builder: Any = None, tile_builder: Any = None, width: int = 800, height: int = 600, show_controls: bool = True, max_render_size: Tuple[int, int] = (2000, 2000), auto_update: bool = True, auto_update_delay_ms: int = 300, show: bool = True):
        """
        Initialize the map viewer.

        Args:
            builder: MapBuilder with data layers to display (optional).
            tile_builder: TileBuilder for background tiles (optional).
            width: Widget width in pixels.
            height: Widget height in pixels.
            show_controls: Whether to show layer control widgets.
            max_render_size: Maximum size for rendered layers (for performance).
            auto_update: Whether to auto-update on pan/zoom.
            auto_update_delay_ms: Delay before auto-update (debounce).
            show: Whether to display immediately. Default True.
        """

    def show(self) -> None:
        """Display the viewer widget."""

    def set_layer_colormap(self, layer_name: str, colormap: str) -> 'MapViewerPyQtGraph':
        """Set colormap for a layer (viewer-controlled)."""

    def set_layer_opacity(self, layer_name: str, opacity: float) -> 'MapViewerPyQtGraph':
        """Set opacity for a layer (viewer-controlled)."""

    def set_layer_range(self, layer_name: str, vmin: float, vmax: float) -> 'MapViewerPyQtGraph':
        """Set value range for a layer (viewer-controlled)."""

    def set_layer_blend_mode(self, layer_name: str, blend_mode: str) -> 'MapViewerPyQtGraph':
        """
        Set blend mode for a layer (viewer-controlled).

        Args:
            layer_name: Layer name.
            blend_mode: One of "alpha", "additive", "overlay".
        """

    def set_tile_source(self, source_name: str) -> 'MapViewerPyQtGraph':
        """
        Set the background tile source.

        Args:
            source_name: Name of tile source (e.g., 'osm', 'esri_worldimagery').
                        Use 'None' to disable tiles.

        Available sources:
            - osm: OpenStreetMap
            - esri_worldimagery: ESRI World Imagery (satellite)
            - esri_ocean: ESRI Ocean Basemap
            - esri_natgeo: ESRI National Geographic
            - cartodb_positron: CartoDB Positron (light theme)
            - cartodb_darkmatter: CartoDB Dark Matter (dark theme)
            - cartodb_voyager: CartoDB Voyager
            - stadia_terrain: Stadia Terrain
            - stadia_toner: Stadia Toner (B&W)
            - stadia_watercolor: Stadia Watercolor
            - opentopomap: OpenTopoMap (topographic)
        """

    def set_tile_visible(self, visible: bool) -> 'MapViewerPyQtGraph':
        """
        Set tile layer visibility.

        Args:
            visible: Whether to show background tiles.
        """

    @property
    def tile_builder(self):
        """Access the TileBuilder instance."""

    @tile_builder.setter
    def tile_builder(self, builder):
        """Set a new TileBuilder instance."""

    def list_tile_sources(self) -> List[str]:
        """List available tile source names."""

    def zoom_to_fit(self):
        """Zoom to fit all visible layers."""

    def zoom_to_track(self):
        """Zoom to fit all navigation tracks (regular and overview)."""

    def zoom_to_position(self, lat: float, lon: float, radius_deg: float = 0.01):
        """
        Zoom to center on a lat/lon position.

        Args:
            lat: Latitude in degrees.
            lon: Longitude in degrees.
            radius_deg: View radius in degrees.
        """

    def pan_to_wci_position(self):
        """Pan to center on the current WCI ping position without changing zoom."""

    def pan_to_position(self, lat: float, lon: float):
        """
        Pan to center on a position without changing zoom level.

        Args:
            lat: Latitude in degrees.
            lon: Longitude in degrees.
        """

    def is_position_near_edge(self, lat: float, lon: float, edge_fraction: float = 0.2) -> bool:
        """
        Check if a position is near the edge of the current view.

        Args:
            lat: Latitude in degrees.
            lon: Longitude in degrees.
            edge_fraction: Fraction of view to consider as 'edge' (0.2 = 20%).

        Returns:
            True if position is in the outer edge_fraction of the view.
        """

    def pan_to_position_if_near_edge(self, lat: float, lon: float, edge_fraction: float = 0.2):
        """
        Pan to center on position only if it's near the edge of the view.

        Args:
            lat: Latitude in degrees.
            lon: Longitude in degrees.
            edge_fraction: Fraction of view to consider as 'edge' (0.2 = 20%).
        """

    def add_markers(self, latitudes, longitudes, name: str = 'markers', labels: Optional[List[str]] = None, color: str = 'white', edge_color: str = 'black', size: float = 10, symbol: str = 'o', edge_width: float = 1.5, z_value: float = 100, label_color: str = 'black', label_size: str = '9pt') -> pg.ScatterPlotItem:
        """
        Add persistent marker points that stay above tracks.

        Args:
            latitudes: Array of latitudes.
            longitudes: Array of longitudes.
            name: Unique key (replaces existing markers with same name).
            labels: Optional list of per-point labels displayed next
                    to each marker on the map.
            color: Fill colour.
            edge_color: Border colour.
            size: Marker size in pixels.
            symbol: PyQtGraph symbol ('o', 's', 't', 'd', '+', 'x', …).
            edge_width: Border width.
            z_value: Draw order (higher = on top). Default 100 is
                     well above tracks.
            label_color: Text colour for labels.
            label_size: Font size for labels (e.g. '9pt').

        Returns:
            The ``ScatterPlotItem`` – can be used for further styling.
        """

    def add_markers_tuples(self, positions, name: str = 'markers', **kwargs) -> pg.ScatterPlotItem:
        """
        Add markers from ``(lat, lon)`` tuples.

        Args:
            positions: Iterable of ``(lat, lon)`` pairs.
            name: Unique key (replaces existing markers with same name).
            **kwargs: Forwarded to :meth:`add_markers` (color,
                      edge_color, size, symbol, edge_width, z_value).

        Returns:
            The ``ScatterPlotItem``.
        """

    def remove_markers(self, name: str):
        """Remove a named marker overlay (including labels)."""

    def clear_markers(self):
        """Remove all user marker overlays."""

    def add_track(self, latitudes: np.ndarray, longitudes: np.ndarray, name: str = 'Track', color: Optional[str] = None, line_width: float = 2.0, is_active: bool = False, slot_idx: Optional[int] = None):
        """
        Add a navigation track overlay.

        Args:
            latitudes: Array of latitudes in degrees.
            longitudes: Array of longitudes in degrees.
            name: Track name (used as key).
            color: Track color. If None, auto-assigned.
            line_width: Line width.
            is_active: Whether this is the active/selected track.
            slot_idx: Echogram viewer slot index (for visible range highlighting).
        """

    def add_overview_track(self, overview, name: str = 'Overview', color: Optional[str] = None, line_width: float = 2.0, max_points: int = 50000, is_active: bool = False, slot_idx: Optional[int] = None, show_points: bool = False, point_size: float = 5.0, point_symbol: str = 'o', point_outline: bool = True):
        """
        Add a navigation track backed by a :class:`PingOverview`.

        Unlike :meth:`add_track`, the track data is **resampled on every
        zoom change** via ``overview.get_track_data()`` so that only up
        to *max_points* are rendered regardless of dataset size.

        Args:
            overview: A ``PingOverview`` instance with latitude/longitude.
            name: Track name (used as key; must be unique across both
                  regular and overview tracks).
            color: Track colour.  If *None*, auto-assigned.
            line_width: Base line width.
            max_points: Maximum rendered points (default 50 000).
            is_active: Whether this is the active/highlighted track.
            slot_idx: Echogram viewer slot index for visible-range
                      highlighting.
            show_points: If *True*, draw a marker at every downsampled
                         track point.
            point_size: Marker diameter in pixels (default 5).
            point_symbol: PyQtGraph symbol string (default ``'o'``).
            point_outline: If *True* (default), markers get a white
                           outline; set *False* for no outline.
        """

    def set_active_track(self, name: str):
        """
        Set which track is the active/highlighted one.

        Args:
            name: Name of the track to make active.
        """

    def clear_tracks(self):
        """Remove all tracks (regular and overview)."""

    def set_track_color(self, name: str, color: str):
        """
        Change the colour of a track.

        Args:
            name: Track name.
            color: New CSS colour (hex or named).
        """

    def update_ping_position(self, lat: float, lon: float):
        """
        Update the current ping position marker.

        Args:
            lat: Latitude in degrees.
            lon: Longitude in degrees.
        """

    def connect_echogram_viewer(self, echogram_viewer):
        """
        Connect to an EchogramViewerMultiChannel to show tracks and ping positions.

        This will:
        - Add tracks for each visible channel (from echogram builders with get_track())
        - Sync track visibility with echogramviewer slot visibility
        - Highlight the track for the currently active slot
        - Update ping position when the ping changes

        Args:
            echogram_viewer: EchogramViewerMultiChannel instance.
        """

    def connect_wci_viewer(self, wci_viewer):
        """
        Connect to a WCIViewerMultiChannel to show tracks and ping positions.

        This will:
        - Add tracks for each channel (if echogram data is available)
        - Update ping position when the ping changes

        Args:
            wci_viewer: WCIViewerMultiChannel instance.
        """

    def refresh_tracks(self):
        """Refresh tracks from connected viewers, preserving visibility state."""

    def register_click_callback(self, callback: Callable[[float, float], None]):
        """
        Register a callback for map clicks.

        Callback receives (lat, lon) of clicked position.

        Args:
            callback: Function to call on click.
        """

    def register_view_change_callback(self, callback: Callable):
        """
        Register a callback for view changes.

        Callback receives new view bounds.

        Args:
            callback: Function to call on view change.
        """
