"""
Core map viewer logic independent of the UI toolkit.

Manages pyqtgraph scene-graph items (PlotItem, ImageItem, ScatterPlotItem, …)
and reads / writes control state through a :class:`ControlPanel` abstraction.
Adapters (``mapviewer_jupyter``, ``mapviewer_qt``) create the concrete
controls and wire up display / async loading.
"""

import dataclasses

import np
import pg

from themachinethatgoesping.pingprocessing.widgets.control_spec import (
    ControlPanel as ControlPanel
)
import themachinethatgoesping.pingprocessing.widgets.pyqtgraph_helpers as pgh


MAP_COLORMAPS: list = ...

HAS_MATPLOTLIB: bool = True

class LayerRenderSettings:
    """Viewer-side rendering settings for a layer."""

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
    """Track backed by a PingOverview with zoom-adaptive downsampling."""

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

class MapCore:
    """
    Backend-agnostic map viewer core.

    Parameters
    ----------
    builder : any, optional
        MapBuilder with data layers to display.
    tile_builder : any, optional
        TileBuilder for background tiles.
    panel : ControlPanel
        Named :class:`ControlHandle` objects for reading / writing UI state.
    graphics : pg.GraphicsLayoutWidget
        The pyqtgraph widget (jupyter-rfb or native).
    max_render_size : tuple[int, int]
        Maximum size for rendered layers.
    """

    TRACK_COLORS: list = ...

    def __init__(self, builder: Any = None, tile_builder: Any = None, panel: Optional[ControlPanel] = None, graphics: Any = None, max_render_size: Tuple[int, int] = (2000, 2000)) -> None: ...

    def create_colorbar(self) -> None:
        """Create an interactive colorbar for the selected layer."""

    def on_colorbar_layer_change(self, layer_name: Optional[str]) -> None:
        """Handle colorbar layer selection change."""

    def set_layer_colormap(self, layer_name: str, colormap: str) -> None: ...

    def set_layer_opacity(self, layer_name: str, opacity: float) -> None: ...

    def set_layer_range(self, layer_name: str, vmin: float, vmax: float) -> None: ...

    def set_layer_blend_mode(self, layer_name: str, blend_mode: str) -> None: ...

    @property
    def tile_visible(self) -> bool: ...

    @tile_visible.setter
    def tile_visible(self, visible: bool) -> None: ...

    @property
    def tile_builder(self): ...

    @tile_builder.setter
    def tile_builder(self, builder) -> None: ...

    def change_tile_source(self, source_name: str) -> None:
        """Change the tile source by name."""

    def list_tile_sources(self) -> List[str]: ...

    def update_view(self) -> None:
        """Update the displayed layers based on current view bounds."""

    def render_tiles(self) -> None:
        """Trigger background tile loading via the adapter callback."""

    def apply_tile_result(self, result: Dict[str, Any]) -> None:
        """Apply a tile loading result (called from adapter after async load)."""

    def set_layer_visibility(self, layer_name: str, visible: bool) -> None:
        """Set visibility for a data layer."""

    def set_layer_opacity_image(self, layer_name: str, opacity: float) -> None:
        """Set opacity and re-render a layer."""

    def set_layer_colormap_image(self, layer_name: str, colormap: str) -> None:
        """Set colormap and re-render a layer."""

    def add_geotiff(self, path: str, name: Optional[str] = None, band: int = 1, **kwargs) -> None: ...

    def add_layer(self, backend: Any, name: Optional[str] = None, visible: bool = True, z_order: Optional[int] = None) -> None: ...

    @property
    def layer_names(self) -> List[str]:
        """Get names of all data layers."""

    def add_track(self, latitudes: np.ndarray, longitudes: np.ndarray, name: str = 'Track', color: Optional[str] = None, line_width: float = 2.0, is_active: bool = False, slot_idx: Optional[int] = None) -> None: ...

    def add_overview_track(self, overview, name: str = 'Overview', color: Optional[str] = None, line_width: float = 2.0, max_points: int = 50000, is_active: bool = False, slot_idx: Optional[int] = None, show_points: bool = False, point_size: float = 5.0, point_symbol: str = 'o', point_outline: bool = True) -> None: ...

    def set_active_track(self, name: str) -> None: ...

    def clear_tracks(self) -> None: ...

    def set_track_color(self, name: str, color: str) -> None: ...

    def set_track_visibility(self, track_name: str, visible: bool) -> None: ...

    def add_markers(self, latitudes, longitudes, name: str = 'markers', labels: Optional[List[str]] = None, color: str = 'white', edge_color: str = 'black', size: float = 10, symbol: str = 'o', edge_width: float = 1.5, z_value: float = 100, label_color: str = 'black', label_size: str = '9pt') -> pg.ScatterPlotItem: ...

    def add_markers_tuples(self, positions, name: str = 'markers', **kwargs) -> pg.ScatterPlotItem: ...

    def remove_markers(self, name: str) -> None: ...

    def clear_markers(self) -> None: ...

    def update_ping_position(self, lat: float, lon: float) -> None:
        """Update the current ping position marker."""

    def zoom_to_fit(self) -> None: ...

    def zoom_to_track(self) -> None: ...

    def zoom_to_position(self, lat: float, lon: float, radius_deg: float = 0.01) -> None: ...

    def pan_to_wci_position(self) -> None: ...

    def pan_to_position(self, lat: float, lon: float) -> None: ...

    def is_position_near_edge(self, lat: float, lon: float, edge_fraction: float = 0.2) -> bool: ...

    def pan_to_position_if_near_edge(self, lat: float, lon: float, edge_fraction: float = 0.2) -> None: ...

    def set_scale_bar_visible(self, visible: bool) -> None: ...

    def set_measure_active(self, active: bool) -> None:
        """Enable or disable the measurement tool (left-click to place)."""

    def set_measure_unit(self, unit: str) -> None:
        """Set the measurement display unit ('m', 'km', or 'nm')."""

    def clear_measurement(self) -> None:
        """Remove all measurement points and overlays."""

    def connect_echogram_viewer(self, echogram_viewer) -> None: ...

    def connect_wci_viewer(self, wci_viewer) -> None: ...

    def refresh_tracks(self) -> None: ...

    def register_click_callback(self, callback: Callable[[float, float], None]) -> None: ...

    def register_view_change_callback(self, callback: Callable) -> None: ...

    def build_high_res_sync(self, cancel_flag) -> Optional[Dict[str, Any]]:
        """Load all visible layer data synchronously (for background thread)."""

    def apply_high_res_results(self, results: Dict[str, Any]) -> None:
        """Apply preloaded layer data from background thread."""

    def wire_observers(self) -> None:
        """Wire control panel observers to core actions."""

    @property
    def plot(self):
        """Access the main PlotItem."""
