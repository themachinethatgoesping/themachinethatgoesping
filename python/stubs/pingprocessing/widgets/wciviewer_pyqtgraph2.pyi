"""
PyQtGraph-based Multi-Channel Water Column Image (WCI) viewer.

Features:
- Grid layout selector (1, 2, 2x2, 3x2, 4x2)
- Per-slot ping number selection with time synchronization
- Global controls except per-slot ping selection and color levels
- Time difference display for synchronized pings
- Per-slot interactive colorbars with global override
- Smooth view transitions when switching slots
"""

import ipywidgets
import mi

import themachinethatgoesping.echosounders as echosounders
import themachinethatgoesping.pingprocessing.watercolumn.image as mi
import themachinethatgoesping.pingprocessing.widgets.pyqtgraph_helpers as pgh
from themachinethatgoesping.pingprocessing.widgets.tqdmwidget import (
    TqdmWidget as TqdmWidget
)


WCI_VALUE_CHOICES: list = ...

class WCISlot:
    """Manages a single WCI display slot with per-slot ping and color levels."""

    def __init__(self, slot_idx: int, parent: 'WCIViewerMultiChannel'): ...

    def set_visible(self, visible: bool):
        """Set visibility."""

    def assign_channel(self, channel_key: Optional[str]):
        """Assign a channel (ping source) to this slot."""

    def get_pings(self) -> Optional[Sequence[Any]]:
        """Get the pings assigned to this slot."""

    def get_ping(self, index: Optional[int] = None) -> Optional[Any]:
        """Get a specific ping from this slot's channel."""

    def get_timestamp(self, index: Optional[int] = None) -> Optional[float]:
        """Get timestamp of a ping (unix time)."""

    def find_closest_ping_index(self, target_timestamp: float) -> int:
        """Find the ping index closest to the target timestamp."""

class WCIViewerMultiChannel:
    """
    Multi-channel Water Column Image viewer with time synchronization.

    Features:
    - Multiple WCI channels displayed in a grid layout
    - Per-slot ping number selection
    - Time synchronization across channels
    - Per-slot color scales with global override
    - Smooth view transitions
    """

    GRID_LAYOUTS: list = ...

    def __init__(self, channels: Union[Dict[str, Sequence[Any]], Sequence[Sequence[Any]]], name: str = 'Multi-Channel WCI', names: Optional[Sequence[Optional[str]]] = None, horizontal_pixels: int = 1024, progress: Optional[Any] = None, show: bool = True, cmap: str = 'YlGnBu_r', widget_height_px: int = 600, widget_width_px: int = 1000, initial_grid: Tuple[int, int] = (2, 2), time_sync_enabled: bool = True, time_warning_threshold: float = 5.0, **kwargs: Any) -> None:
        """
        Initialize the multi-channel WCI viewer.

        Parameters
        ----------
        channels : dict or sequence
            Either a dict mapping channel names to ping sequences,
            or a sequence of ping sequences.
        name : str
            Viewer name/title.
        names : sequence, optional
            Names for each channel if channels is a sequence.
        horizontal_pixels : int
            Horizontal resolution for WCI images.
        progress : widget, optional
            Progress widget for loading feedback.
        show : bool
            If True, display immediately.
        cmap : str
            Colormap name.
        widget_height_px : int
            Widget height in pixels.
        widget_width_px : int
            Widget width in pixels.
        initial_grid : tuple
            Initial grid layout (rows, cols).
        time_sync_enabled : bool
            If True, synchronize ping times across channels.
        time_warning_threshold : float
            Time difference (seconds) above which to show red warning text.
        **kwargs
            Additional arguments passed to image builder.
        """

    def process_events(self) -> None:
        """Process pending Qt events for responsiveness."""

    def redraw(self, force: bool = True) -> None:
        """Force a redraw of the widget."""

    def set_widget_height(self, height_px: int) -> None:
        """Set the widget height."""

    def register_ping_change_callback(self, callback: Any) -> None:
        """
        Register a callback to be called when ping changes.

        The callback should be a callable with no arguments.
        Useful for connecting echogram viewers to update their pinglines.

        Args:
            callback: A callable to be invoked on ping change.
        """

    def unregister_ping_change_callback(self, callback: Any) -> None:
        """
        Unregister a previously registered ping change callback.

        Args:
            callback: The callback to remove.
        """

    @property
    def w_index(self) -> ipywidgets.IntSlider:
        """
        Return ping slider for first visible slot (compatibility with single-channel viewer).
        """

    @property
    def imagebuilder(self) -> Optional[mi.ImageBuilder]:
        """
        Return imagebuilder for first visible slot (compatibility with single-channel viewer).
        """
