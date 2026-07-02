"""
Core WCI viewer logic independent of the UI toolkit.

Manages pyqtgraph scene-graph items (PlotItem, ImageItem, ColorBarItem, …)
and reads / writes control state through a :class:`ControlPanel` abstraction.
Adapters (``wciviewer_jupyter``, ``wciviewer_qt``) create the concrete
controls and wire up observers.
"""

import QtCore
import QtWidgets
import mi
import pg

import themachinethatgoesping.echosounders as echosounders
import themachinethatgoesping.pingprocessing.watercolumn.image as mi
from themachinethatgoesping.widgets.control_spec import (
    ControlPanel as ControlPanel
)
import themachinethatgoesping.widgets.pyqtgraph_helpers as pgh
from themachinethatgoesping.widgets.videoframes import (
    VideoFrames as VideoFrames
)


def normalise_channels(channels: Union[Dict[str, Sequence[Any]], Sequence[Sequence[Any]]], names: Optional[Sequence[Optional[str]]]) -> Tuple[Dict[str, Sequence[Any]], List[str]]:
    """Normalise various channel input formats to ``(dict, names_list)``."""

def auto_select_grid(initial_grid: Tuple[int, int], n_channels: int) -> Tuple[int, int]:
    """
    Choose an appropriate grid size based on the number of channels.

    Only overrides when the caller passes the default ``(2, 2)``.
    """

class WCISlot:
    """
    Manages a single WCI display slot with per-slot ping and colour levels.
    """

    def __init__(self, slot_idx: int, channels: Dict[str, Sequence[Any]], args_imagebuilder: Dict[str, Any], progress: Any) -> None: ...

    def set_visible(self, visible: bool) -> None: ...

    def assign_channel(self, channel_key: Optional[str]) -> None: ...

    def get_pings(self) -> Optional[Sequence[Any]]: ...

    def get_ping(self, index: Optional[int] = None) -> Optional[Any]: ...

    def get_timestamp(self, index: Optional[int] = None) -> Optional[float]: ...

    def find_closest_ping_index(self, target_timestamp: float) -> int: ...

class WCICore:
    """
    Backend-agnostic WCI viewer core.

    Parameters
    ----------
    channels : dict
        ``{name: ping_sequence}``
    channel_names : list[str]
        Ordered channel names.
    panel : ControlPanel
        Provides named :class:`ControlHandle` objects for reading / writing
        UI state.  Must already contain all controls listed in
        ``control_spec.WCI_*`` plus per-slot controls registered as
        ``"slot_selector__i"`` and ``"ping_slider__i"``.
    graphics : pg.GraphicsLayoutWidget
        The pyqtgraph widget (jupyter-rfb or native).
    progress : any
        Progress bar object (TqdmWidget or similar).
    cmap : str
        Matplotlib / pyqtgraph colourmap name.
    initial_grid : tuple[int, int]
        ``(rows, cols)``
    time_sync_enabled : bool
    time_warning_threshold : float
    """

    MAX_SLOTS: int = 8

    def __init__(self, channels: Dict[str, Sequence[Any]], channel_names: List[str], panel: ControlPanel, graphics: pg.GraphicsLayoutWidget, progress: Any, cmap: str = 'YlGnBu_r', initial_grid: Tuple[int, int] = (2, 2), time_sync_enabled: bool = True, time_warning_threshold: float = 5.0, **kwargs: Any) -> None: ...

    def wire_observers(self, *, play_callback: Optional[Callable[[], Any]] = None, layout_callback: Optional[Callable[[], Any]] = None) -> None:
        """
        Connect panel controls to core methods.

        Parameters
        ----------
        play_callback
            Called when the play button is clicked.
            Defaults to :meth:`toggle_autoplay` (async, for Jupyter).
        layout_callback
            Called (with no args) **after** the grid layout change has been
            processed.  Use for adapter-specific UI updates such as
            refreshing slot-selector visibility in Jupyter.
        """

    def update_grid_layout(self) -> None:
        """(Re-)create PlotItems / ImageItems for the current grid size."""

    def on_layout_change(self, new_rows: int, new_cols: int) -> None: ...

    def on_slot_change(self, slot_idx: int, new_channel: Optional[str]) -> None: ...

    def on_ping_change(self, slot_idx: int, new_ping: int) -> None:
        """
        Handle a *manual or external* ping change for ``slot_idx``.

        This slot becomes the synchronisation master: its timestamp becomes the
        reference and all other slots are aligned to it.  Changes that originate
        from the internal synchronisation itself are flagged by ``_syncing`` and
        ignored here so they can never become a competing master (which caused
        the back-and-forth oscillation between channels).
        """

    def on_global_color_change(self) -> None: ...

    def on_global_param_change(self) -> None: ...

    def on_video_format_change(self, fmt: str) -> None: ...

    def on_ping_step_change(self, new_step: int) -> None: ...

    def fix_xy(self) -> None: ...

    def unfix_xy(self) -> None: ...

    def step_prev(self) -> None: ...

    def step_next(self) -> None: ...

    def toggle_autoplay(self) -> None: ...

    def start_autoplay(self) -> None: ...

    def stop_autoplay(self) -> None: ...

    def export_video(self) -> None: ...

    def toggle_continuous_capture(self) -> None:
        """
        Toggle infinite capture mode.

        While active, every ping change grabs a frame.  When toggled off,
        the captured frames are exported with the current video settings.
        """

    def show_single(self, channel_name: str) -> None: ...

    def handle_scene_move(self, pos: QtCore.QPointF) -> None: ...

    def register_depth_change_callback(self, callback: Any) -> None: ...

    def unregister_depth_change_callback(self, callback: Any) -> None: ...

    def set_external_crosshair_depth(self, depth: Optional[float]) -> None:
        """
        Set the horizontal crosshair from an external viewer (no callback fired).
        """

    def register_ping_change_callback(self, callback: Any) -> None: ...

    def unregister_ping_change_callback(self, callback: Any) -> None: ...

    def register_view_change_callback(self, callback: Any) -> None:
        """
        Register a callback fired when a display parameter (e.g. the stack
        size/step) changes.  Connected viewers use this to keep overlays such
        as the echogram stack region in sync.
        """

    def unregister_view_change_callback(self, callback: Any) -> None: ...

    @property
    def w_index(self):
        """Compatibility: ping slider handle for first visible slot."""

    @property
    def imagebuilder(self) -> Optional[mi.ImageBuilder]: ...

    def get_scene(self) -> QtWidgets.QGraphicsScene: ...

    def save_scene(self, filename: str = 'scene.svg') -> None: ...

    def get_matplotlib(self, dpi: int = 150): ...
