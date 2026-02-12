"""
Enhanced PyQtGraph-based multi-echogram viewer with grid layout and lazy updates.

Features:
- Grid layout selector (1, 2, 2x2, 3x2, 4x2)
- Per-slot dropdown to select which echogram/frequency to display
- Visibility-based updates (inactive echograms don't update until shown)
- Synchronized crosshair for target investigation across frequencies
- Tab-based quick access for single echogram view
- Lazy loading pattern for performance
- Interactive parameter editing (add, move, delete points)
"""

import PySide6.QtCore
import QtGui
import pyqtgraph.graphicsItems.ROI
import pyqtgraph.graphicsItems.ScatterPlotItem

import themachinethatgoesping as theping
import themachinethatgoesping.pingprocessing.widgets.pyqtgraph_helpers as pgh


class DraggableScatterPlotItem(pyqtgraph.graphicsItems.ScatterPlotItem.ScatterPlotItem):
    """ScatterPlotItem that supports dragging individual points."""

    sigPointDragged: PySide6.QtCore.Signal = ...

    def __init__(self, *args, **kwargs): ...

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        """Handle mouse press - start drag if on a point."""

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        """Handle mouse move - drag point if dragging."""

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        """Handle mouse release - end drag."""

    staticMetaObject: PySide6.QtCore.QMetaObject = ...

class SafePolyLineROI(pyqtgraph.graphicsItems.ROI.PolyLineROI):
    """
    PolyLineROI subclass that disables right-click context menu on handles.

    The default PolyLineROI handles can crash when right-clicked due to
    internal state issues. This subclass intercepts and ignores right-click
    events to prevent crashes.
    """

    def __init__(self, *args, **kwargs): ...

    def addHandle(self, *args, **kwargs):
        """Override to disable context menu on newly added handles."""

    def setPoints(self, points, closed=None):
        """Override to disable context menu on handles after setting points."""

    staticMetaObject: PySide6.QtCore.QMetaObject = ...

class EchogramSlot:
    """Manages a single echogram display slot with lazy loading."""

    def __init__(self, slot_idx: int, parent: 'EchogramViewerMultiChannel'): ...

    def mark_dirty(self):
        """Mark that data needs refresh when shown."""

    def set_visible(self, visible: bool):
        """Set visibility and trigger update if needed."""

    def assign_echogram(self, echogram_key: Optional[str]):
        """Assign an echogram to this slot."""

    def get_echogram(self) -> Optional[Any]:
        """Get the echogram assigned to this slot."""

    def clear_high_res(self):
        """Clear high-res data (keeps background)."""

class EchogramViewerMultiChannel:
    """Enhanced multi-echogram viewer with grid layout and lazy updates."""

    GRID_LAYOUTS: list = ...

    def __init__(self, echogramdata: Union[Dict[str, Any], Sequence[Any]], name: str = 'Multi-Echogram Viewer', names: Optional[Sequence[Optional[str]]] = None, progress: Optional[Any] = None, show: bool = True, voffsets: Optional[Dict[str, float]] = None, cmap: str = 'Greys_r', cmap_layer: str = 'YlGnBu_r', fps: int = 25, widget_height_px: int = 600, widget_width_px: int = 1000, auto_update: bool = True, auto_update_delay_ms: int = 300, initial_grid: Tuple[int, int] = (2, 2), **kwargs: Any) -> None: ...

    def get_xlim(self) -> Optional[Tuple[float, float]]:
        """
        Get the current visible X-axis limits of the viewport.

        Returns:
            Tuple of (xmin, xmax) or None if no plot is available.
        """

    def get_ylim(self) -> Optional[Tuple[float, float]]:
        """
        Get the current visible Y-axis limits of the viewport.

        Returns:
            Tuple of (ymin, ymax) or None if no plot is available.
        """

    def pan_view(self, direction: str, fraction: float = 0.25) -> None:
        """Pan the view in a direction."""

    def connect_pingviewer(self, pingviewer: Any) -> None:
        """
        Connect to a pingviewer for synchronized display.

        If the pingviewer supports ping change callbacks (e.g., WCIViewerMultiChannel),
        automatically registers to update pinglines when the ping changes.
        """

    def disconnect_pingviewer(self) -> None:
        """Disconnect from pingviewer."""

    def update_ping_lines(self) -> None:
        """Public method to update ping lines from connected pingviewer."""

    def show(self) -> None:
        """Display the viewer widget."""

    def set_widget_size(self, width_px: int, height_px: int) -> None:
        """Set widget dimensions."""

    def add_station_times(self, stations: Dict[str, Tuple[Any, Any]], line_color: str = '#424242', line_width: int = 2, line_style: str = 'dash', region_color: Optional[str] = None, region_alpha: float = 0.15, label_color: Optional[str] = None, label_size: str = '10pt', label_position: str = 'top') -> None:
        """
        Add station time markers to all visible echograms.

        Draws vertical lines at station start/end times with a semi-transparent
        region between them and a label showing the station name.

        Args:
            stations: Dict mapping station names to (start_time, end_time) tuples.
                      Times can be datetime objects or unix timestamps (float/int).
            line_color: Color for the vertical lines (hex or named color).
            line_width: Width of the vertical lines in pixels.
            line_style: Line style - 'solid', 'dash', 'dot', or 'dashdot'.
            region_color: Fill color for the region between lines. If None,
                         uses line_color with region_alpha transparency.
            region_alpha: Alpha (0-1) for the region fill color.
            label_color: Color for the station label text. If None, uses line_color.
            label_size: Font size for labels (e.g., '10pt', '12pt').
            label_position: Where to place the label - 'top' or 'bottom'.

        Example:
            >>> viewer.add_station_times({
            ...     'Station A': (datetime(2024, 1, 1, 10, 0), datetime(2024, 1, 1, 10, 30)),
            ...     'Station B': (1704110400.0, 1704112200.0),  # unix timestamps
            ... })
        """

    def clear_station_times(self, station_name: Optional[str] = None) -> None:
        """
        Remove station time markers.

        Args:
            station_name: If specified, remove only this station's markers.
                         If None, remove all station markers.
        """

    def cleanup(self) -> None:
        """Clean up resources."""

    def __del__(self) -> None: ...
