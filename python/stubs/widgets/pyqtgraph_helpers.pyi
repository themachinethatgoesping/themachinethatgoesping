"""Utility helpers shared by PyQtGraph-based widget viewers."""

import PySide6.QtCore
import ipywidgets
import pg
import pyqtgraph.graphicsItems.AxisItem


__all__: list = ['MatplotlibDateAxis', 'TimedeltaAxis', 'DistanceAxis', 'ensure_qapp', 'resolve_colormap', 'list_colormaps', 'apply_widget_layout']

class MatplotlibDateAxis(pyqtgraph.graphicsItems.AxisItem.AxisItem):
    """AxisItem that formats matplotlib-style ordinal dates."""

    def __init__(self, converter: Callable[[float], datetime], orientation: str = 'bottom') -> None: ...

    def tickStrings(self, values: List[float], scale: float, spacing: float) -> List[str]: ...

    staticMetaObject: PySide6.QtCore.QMetaObject = ...

class TimedeltaAxis(pyqtgraph.graphicsItems.AxisItem.AxisItem):
    """
    AxisItem that formats seconds as human-readable time strings.

    The format is chosen once based on *max_seconds* (the overall data range)
    and stays fixed regardless of zoom level:

    - < 1 s:  "0.123 s"
    - < 60 s: "12.3 s"
    - < 1 h:  "05:23"  (mm:ss)
    - < 24 h: "1:05:23" (h:mm:ss)
    - >= 24 h: "2d 03:15" (Nd hh:mm)
    """

    def __init__(self, max_seconds: float = 60.0, orientation: str = 'bottom') -> None: ...

    def tickStrings(self, values: List[float], scale: float, spacing: float) -> List[str]: ...

    staticMetaObject: PySide6.QtCore.QMetaObject = ...

class DistanceAxis(pyqtgraph.graphicsItems.AxisItem.AxisItem):
    """
    AxisItem for along-track distance that switches between m and km by zoom.

    When the visible span is below ``km_threshold_m`` meters the ticks and the
    axis label use meters; otherwise kilometers. The unit therefore adapts to
    the current zoom level (e.g. it shows meters once zoomed in below 5 km even
    if the full survey spans tens of kilometers).
    """

    def __init__(self, km_threshold_m: float = 10000.0, show_unit_label: bool = True, orientation: str = 'bottom') -> None: ...

    def setRange(self, mn: float, mx: float) -> None: ...

    def tickValues(self, minVal: float, maxVal: float, size: int):
        """
        Ensure a fixed left-edge anchor tick in mixed mode.

        This guarantees that the absolute km label is always rendered on the
        left edge, independent of pyqtgraph's automatic tick placement.
        """

    def tickStrings(self, values: List[float], scale: float, spacing: float) -> List[str]: ...

    staticMetaObject: PySide6.QtCore.QMetaObject = ...

def ensure_qapp() -> None:
    """Ensure a QApplication exists for PyQtGraph widgets."""

def resolve_colormap(cmap) -> pg.ColorMap:
    """
    Return a PyQtGraph ColorMap from a name, pg.ColorMap, or matplotlib Colormap.

    Parameters
    ----------
    cmap : str, pg.ColorMap, or matplotlib.colors.Colormap
        Colormap name (pyqtgraph or matplotlib), a PyQtGraph ColorMap
        instance, or a matplotlib Colormap (e.g. ``colorcet.cm.CET_L20``).

    Returns
    -------
    pg.ColorMap
        Resolved colormap. Falls back to 'viridis' if not found.
    """

def list_colormaps(source: Optional[str] = None) -> List[str]:
    """
    List available colormap names.

    Parameters
    ----------
    source : str, optional
        Filter by source: 'pyqtgraph', 'matplotlib', or None for all.

    Returns
    -------
    List[str]
        Sorted list of colormap names that can be passed to :func:`resolve_colormap`.

    Examples
    --------
    >>> list_colormaps()                    # All colormaps
    >>> list_colormaps('matplotlib')        # Only matplotlib colormaps
    >>> list_colormaps('pyqtgraph')         # Only pyqtgraph colormaps
    """

def apply_widget_layout(widget: ipywidgets.Widget, width_px: int, height_px: int) -> None:
    """Attach a resizable layout to the GraphicsLayoutWidget wrapper."""
