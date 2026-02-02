"""Utility helpers shared by PyQtGraph-based widget viewers."""

import PySide6.QtCore
import ipywidgets
import pg
import pyqtgraph.graphicsItems.AxisItem


__all__: list = ['MatplotlibDateAxis', 'ensure_qapp', 'resolve_colormap', 'list_colormaps', 'apply_widget_layout']

class MatplotlibDateAxis(pyqtgraph.graphicsItems.AxisItem.AxisItem):
    """AxisItem that formats matplotlib-style ordinal dates."""

    def __init__(self, converter: Callable[[float], datetime], orientation: str = 'bottom') -> None: ...

    def tickStrings(self, values: List[float], scale: float, spacing: float) -> List[str]: ...

    staticMetaObject: PySide6.QtCore.QMetaObject = ...

def ensure_qapp() -> None:
    """Ensure a QApplication exists for PyQtGraph widgets."""

def resolve_colormap(cmap: Union[str, pg.ColorMap]) -> pg.ColorMap:
    """
    Return a PyQtGraph ColorMap from either a name or a ColorMap instance.

    Parameters
    ----------
    cmap : str or pg.ColorMap
        Colormap name (pyqtgraph or matplotlib) or ColorMap instance.
        Use :func:`list_colormaps` to see all available names.

    Returns
    -------
    pg.ColorMap
        Resolved colormap. Falls back to 'viridis' if not found.

    Examples
    --------
    >>> cmap = resolve_colormap('cubehelix_r')  # matplotlib colormap
    >>> cmap = resolve_colormap('viridis')      # pyqtgraph colormap
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
