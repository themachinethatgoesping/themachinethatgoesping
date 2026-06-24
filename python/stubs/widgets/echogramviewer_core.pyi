"""
Core echogram viewer logic independent of the UI toolkit.

Manages pyqtgraph scene-graph items (PlotItem, ImageItem, ColorBarItem, …)
and reads / writes control state through a :class:`ControlPanel` abstraction.
Adapters (``echogramviewer_jupyter``, ``echogramviewer_qt``) create the
concrete controls and wire up observers.
"""

import PySide6.QtCore
import QtCore
import QtWidgets
import pg
import pyqtgraph.graphicsItems.GraphicsObject
import pyqtgraph.graphicsItems.ROI
import pyqtgraph.graphicsItems.ScatterPlotItem

import themachinethatgoesping as theping
from themachinethatgoesping.widgets.control_spec import (
    ControlPanel as ControlPanel
)
import themachinethatgoesping.widgets.pyqtgraph_helpers as pgh


GRID_LAYOUTS: list = ...

def timestamp_to_axis_coordinate(cs, x_axis_name, timestamp):
    """
    Map a real Unix timestamp to a non-time x-axis coordinate.

    Handles the ping-index/number axis (via a binary search on the per-ping
    times) and custom axes such as ``"Distance"`` (by interpolating the
    timestamp against the per-ping custom coordinates). Time axes
    (``"Date time"`` / ``"Ping time"``) are handled by the caller because they
    may apply gap-compression.

    Args:
        cs: An ``EchogramCoordinateSystem`` (must expose ``ping_times``;
            optionally ``ping_numbers``, ``_custom_x_per_ping`` and
            ``_custom_x_axis_name``).
        x_axis_name: The current x-axis name.
        timestamp: Real Unix timestamp in seconds.

    Returns:
        The x-axis coordinate (float) or ``None`` when it cannot be resolved.
    """

def normalise_echograms(echogramdata: Union[Dict[str, Any], Sequence[Any], Any], names: Optional[Sequence[Optional[str]]]) -> Tuple[Dict[str, Any], List[str]]:
    """Normalise echogram input to ``(dict, names_list)``."""

def auto_select_grid(initial_grid: Tuple[int, int], n_items: int) -> Tuple[int, int]:
    """Choose an appropriate grid size based on the number of items."""

class DraggableScatterPlotItem(pyqtgraph.graphicsItems.ScatterPlotItem.ScatterPlotItem):
    """
    ScatterPlotItem whose individual points can be dragged.

    This uses pyqtgraph's ``mouseDragEvent`` abstraction — the same mechanism
    :class:`pyqtgraph.TargetItem` and the ROI classes use — instead of raw Qt
    mouse events.  That guarantees correct arbitration with the ViewBox:

    * a drag that *starts on a point* moves only that point, while
    * a drag that starts on empty space is left unaccepted and falls through to
      the ViewBox, so normal pan / zoom keeps working.

    Crucially this is **one** scene item for *all* points (pyqtgraph batches
    scatter rendering into a single item), so editing a curve with hundreds of
    control points no longer creates hundreds of hover-accepting handle /
    segment items the way :class:`pyqtgraph.PolyLineROI` does — which was the
    cause of the whole-viewer slowdown.  Hit-testing uses the vectorised
    :meth:`ScatterPlotItem.pointsAt`, so only the point under the cursor is
    grabbed regardless of the total number of points ("only points close to the
    mouse are selectable").

    The original index of every displayed point is carried in the spot ``data``
    field, so the emitted index stays correct even when the visible points are
    a downsampled subset of the full parameter array.
    """

    sigPointDragged: PySide6.QtCore.Signal = ...

    sigPointDragFinished: PySide6.QtCore.Signal = ...

    def __init__(self, *args, **kwargs): ...

    def setMovable(self, movable: bool) -> None: ...

    def mouseDragEvent(self, ev): ...

    staticMetaObject: PySide6.QtCore.QMetaObject = ...

class StationOverlayItem(pyqtgraph.graphicsItems.GraphicsObject.GraphicsObject):
    """
    Lightweight graphics item that draws station markers in one paint().

    Uses a *draw_mode* to control what is rendered:
      - ``'background'``: translucent region fills only (behind echogram).
      - ``'foreground'``: vertical lines and text labels (above echogram).
    """

    def __init__(self, draw_mode: str = 'foreground', parent=None): ...

    def add_station(self, name, start_x, end_x, pen, brush, label_color, font, label_position): ...

    def remove_station(self, name: str): ...

    def clear_stations(self): ...

    def station_names(self) -> List[str]: ...

    def stations_at_x(self, x: float) -> List[str]: ...

    def boundingRect(self): ...

    def paint(self, painter, option, widget=None): ...

    def viewRangeChanged(self): ...

    staticMetaObject: PySide6.QtCore.QMetaObject = ...

class SafePolyLineROI(pyqtgraph.graphicsItems.ROI.PolyLineROI):
    """
    PolyLineROI subclass that disables right-click context menu on handles.
    """

    def __init__(self, *args, **kwargs): ...

    def addHandle(self, *args, **kwargs): ...

    def setPoints(self, points, closed=None): ...

    staticMetaObject: PySide6.QtCore.QMetaObject = ...

class EchogramSlot:
    """Manages a single echogram display slot with lazy loading."""

    def __init__(self, slot_idx: int, echograms: Dict[str, Any], global_image_cache: Dict[str, Dict[str, Any]]) -> None: ...

    def mark_dirty(self): ...

    def set_visible(self, visible: bool): ...

    def assign_echogram(self, echogram_key: Optional[str]): ...

    def get_echogram(self) -> Optional[Any]: ...

    def clear_high_res(self): ...

class EchogramCore:
    """
    Backend-agnostic echogram viewer core.

    Parameters
    ----------
    echograms : dict
        ``{name: echogram_object}``
    echogram_names : list[str]
        Ordered echogram names.
    panel : ControlPanel
        Named control handles (must already contain all echogram specs
        plus per-slot controls ``"slot_selector__i"``).
    graphics : pg.GraphicsLayoutWidget
        The pyqtgraph widget (jupyter-rfb or native).
    progress : any
        Progress bar (TqdmWidget or similar).
    """

    MAX_SLOTS: int = 8

    def __init__(self, echograms: Dict[str, Any], echogram_names: List[str], panel: ControlPanel, graphics: pg.GraphicsLayoutWidget, progress: Any, cmap: str = 'Greys_r', cmap_layer: str = 'YlGnBu_r', initial_grid: Tuple[int, int] = (2, 2), voffsets: Optional[Dict[str, float]] = None, **kwargs: Any) -> None: ...

    def wire_observers(self, *, layout_callback: Optional[Callable[[], None]] = None) -> None:
        """
        Connect panel controls to core methods.

        Parameters
        ----------
        layout_callback
            Called after grid layout change (e.g. to refresh UI selectors).
        """

    def update_grid_layout(self) -> None:
        """(Re-)create PlotItems / ImageItems for the current grid size."""

    def on_layout_change(self, new_rows: int, new_cols: int) -> None: ...

    def on_slot_change(self, slot_idx: int, new_key: Optional[str]) -> None: ...

    def on_global_color_change(self) -> None: ...

    def on_colorbar_layer_change(self, new_layer: str) -> None: ...

    def show_single(self, echogram_name: str) -> None: ...

    def handle_key_down(self, key: str, modifiers: tuple = ()) -> None:
        """Handle keyboard events for parameter editing."""

    def load_all_backgrounds(self) -> None:
        """Load background images for all echograms (synchronous)."""

    def build_high_res_sync(self, view_params: Dict[int, Dict[str, float]], cancel_flag=None) -> Optional[Dict[int, Dict[str, Any]]]:
        """
        Build high-res images for visible slots (synchronous).

        Run in a background thread/executor.  Returns results dict or None
        if cancelled.
        """

    def apply_high_res_results(self, results: Dict[int, Dict[str, Any]]) -> None:
        """Apply loaded high-res results to slots and refresh display."""

    def get_xlim(self) -> Optional[Tuple[float, float]]: ...

    def get_ylim(self) -> Optional[Tuple[float, float]]: ...

    def reset_view(self) -> None:
        """Reset view to show full extent of all visible echograms."""

    def capture_view_params(self) -> Dict[int, Dict[str, float]]:
        """
        Capture current view parameters for visible slots (for high-res loading).
        """

    def pan_view(self, direction: str, fraction: float = 0.25) -> None: ...

    def autoscale_y(self) -> None:
        """
        Scale Y axis to fit the visible data range in the current X view.

        Uses the per-ping vec_min_y / vec_max_y from the echogrambuilder's
        coordinate system rather than scanning rendered pixels.

        If an echogram defines a main layer, autoscaling is constrained to that
        layer's visible Y limits for the current X window.
        """

    def set_x_interval_from_panel(self) -> None:
        """
        Set X axis width from the x_interval panel text field.

        Supported formats:
        - ``"2 min"`` or ``"2min"`` — 2 minutes (datetime axis only)
        - ``"30 s"`` or ``"30s"`` — 30 seconds (datetime axis only)
        - ``"1 h"`` or ``"1h"`` — 1 hour (datetime axis only)
        - ``"500"`` — 500 in native x-axis units (ping number, etc.)
        """

    def set_x_interval(self, width: float) -> None:
        """Set X axis to a given width, centered on the current view center."""

    def handle_scene_click(self, event: Any) -> None: ...

    def handle_scene_move(self, pos: QtCore.QPointF) -> None: ...

    def register_depth_change_callback(self, callback: Any) -> None: ...

    def unregister_depth_change_callback(self, callback: Any) -> None: ...

    def set_external_crosshair_depth(self, depth: Optional[float]) -> None:
        """
        Set the horizontal crosshair from an external viewer (no callback fired).
        """

    def set_slot_interactive(self, slot_idx: int, enabled: bool) -> None:
        """
        Enable / disable interactive parameter editing for one echogram view.

        When disabled the view still *shows* the parameter (curve + points) but
        the points are not draggable, so left-drag pans the view as usual.
        Rebuilds the visualization so the change takes effect immediately.
        """

    def connect_pingviewer(self, pingviewer: Any, progress: bool = False) -> None: ...

    def disconnect_pingviewer(self) -> None: ...

    def set_depth_sync_enabled(self, enabled: bool) -> None:
        """Enable or disable depth crosshair sync without disconnecting."""

    def update_ping_lines(self) -> None: ...

    def goto_pingline(self) -> None:
        """Center the view on the current pingline position."""

    def add_station_times(self, stations: Dict[str, Tuple[Any, Any]], line_color: str = '#424242', line_width: int = 2, line_style: str = 'dash', region_color: Optional[str] = None, region_alpha: float = 0.15, label_color: Optional[str] = None, label_size: str = '10pt', label_position: str = 'top') -> None:
        """Add station time markers to all visible echograms."""

    def clear_station_times(self, station_name: Optional[str] = None) -> None: ...

    def get_scene(self) -> QtWidgets.QGraphicsScene: ...

    def save_scene(self, filename: str = 'scene.svg') -> None: ...

    def get_matplotlib(self, dpi: int = 150): ...

    def register_ping_change_callback(self, callback: Any) -> None: ...

    def unregister_ping_change_callback(self, callback: Any) -> None: ...
