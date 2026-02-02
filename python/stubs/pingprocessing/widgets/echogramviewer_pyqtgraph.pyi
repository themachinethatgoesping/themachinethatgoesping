"""
PyQtGraph-based echogram viewer that streams via pyqtgraph's Jupyter widgets.
"""

import themachinethatgoesping as theping
import themachinethatgoesping.pingprocessing.widgets.pyqtgraph_helpers as pgh


class EchogramViewerPyQtGraph:
    """Replacement for Matplotlib-based EchogramViewer using PyQtGraph."""

    def __init__(self, echogramdata: Sequence[Any], name: str = 'Echogram', names: Optional[Sequence[Optional[str]]] = None, progress: Optional[Any] = None, show: bool = True, voffsets: Optional[Sequence[float]] = None, cmap: str = 'Greys_r', cmap_layer: str = 'YlGnBu_r', fps: int = 25, widget_height_px: Optional[int] = None, widget_width_px: int = 900, auto_update: bool = True, auto_update_delay_ms: int = 300, **kwargs: Any) -> None: ...

    def cleanup(self) -> None:
        """Clean up resources (call when done with the viewer)."""

    def __del__(self) -> None:
        """Destructor to ensure cleanup when viewer is garbage collected."""

    def show(self) -> None: ...

    def init_ax(self, adapt_axis_names: bool = True) -> None: ...

    def show_background_echogram(self) -> None: ...

    def clear_output(self, _event: Any = None) -> None: ...

    def show_background_zoom(self, _event: Any = None) -> None:
        """
        Trigger a background load for the current zoom level.

        This method is non-blocking: it starts loading in a background thread
        and updates the view when complete.
        """

    def pan_view(self, direction: str, fraction: float = 0.25) -> None:
        """
        Pan the view in the specified direction.

        Args:
            direction: One of 'left', 'right', 'up', 'down'
            fraction: Fraction of the current view width/height to pan (default 25%)
        """

    def set_nav_fraction(self, fraction: float = 0.25) -> None:
        """
        Set the fraction of view to pan per button click.

        Args:
            fraction: Fraction of view to pan (default 25%)
        """

    def update_view(self, _widget: Any = None, reset: bool = False) -> None: ...

    def invert_y_axis(self) -> None: ...

    def callback_view(self) -> None: ...

    def update_ping_line(self, _event: Any = None) -> None: ...

    def disconnect_pingviewer(self) -> None: ...

    def connect_pingviewer(self, pingviewer: Any) -> None: ...

    def set_widget_height(self, height_px: int) -> None:
        """Adjust the CSS height of the embedded GraphicsLayoutWidget."""
