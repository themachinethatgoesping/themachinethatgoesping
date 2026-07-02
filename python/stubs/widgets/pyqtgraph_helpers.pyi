"""Utility helpers shared by PyQtGraph-based widget viewers."""

import PySide6.QtCore
import ipywidgets
import pg
import pyqtgraph.graphicsItems.AxisItem


__all__: list = ['MatplotlibDateAxis', 'TimedeltaAxis', 'DistanceAxis', 'ensure_qapp', 'resolve_colormap', 'list_colormaps', 'apply_widget_layout', 'responsive_row']

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
    """
    Configure a ``jupyter_rfb`` graphics widget to fill its container width
    and resize like a native Qt widget.

    ``pyqtgraph.jupyter.GraphicsLayoutWidget`` is a subclass of
    :class:`jupyter_rfb.RemoteFrameBuffer`, which already provides everything we
    need for Qt-like resizing:

    * a ``resizable`` trait (native drag handle in the bottom-right corner), and
    * a ``ResizeObserver`` on the canvas that re-renders the Qt scene whenever
      the canvas size changes — so it adapts to the notebook/window width
      automatically.

    The previous implementation *fought* this by imposing an ipywidgets
    ``layout.resize`` handle plus ``overflow='auto'`` and a fixed pixel
    ``layout.width``.  That produced (a) two competing resize mechanisms,
    (b) scrollbars, (c) a host element with a fixed height while the inner RFB
    wrapper shrank — leaving a large empty gap under the plot — and (d) controls
    that never reflowed.  In addition, when the RFB frontend has no explicit
    width it clamps itself to ``max-width: 90vmin`` (the "weird maximum width").

    Here we instead cooperate with ``jupyter_rfb``:

    * ``css_width='100%'``  → wrapper fills the available width (removes the
      ``90vmin`` clamp and makes the plot follow the window/output width),
    * ``css_height='<px>'`` → a definite starting height that is still
      drag-resizable via the native handle,
    * ``resizable=True``    → native RFB resize handle on both axes,
    * the ipywidgets host ``layout`` only fills the width and gets out of the
      way (``height='auto'``, ``overflow='visible'``, no resize handle).

    Note
    ----
    ``GraphicsView.__init__`` parses ``css_width``/``css_height`` as pixels
    (``int(css_width[:-2])``), so the widget must be *constructed* with a
    ``"<n>px"`` string.  This helper is always called *after* construction, so
    it is safe to switch ``css_width`` to ``"100%"`` here.
    """

def responsive_row(children, *, align_items: str = 'center', justify_content: Optional[str] = None) -> 'ipywidgets.HBox':
    """
    Return an :class:`ipywidgets.HBox` that reflows when space runs out.

    Unlike a plain ``HBox`` (which keeps all children on a single, non-shrinking
    row), this container fills the available width and wraps its children onto
    new lines as the viewer/window gets narrower — so control rows behave like
    the freely re-flowing panels of the native Qt viewers.
    """
