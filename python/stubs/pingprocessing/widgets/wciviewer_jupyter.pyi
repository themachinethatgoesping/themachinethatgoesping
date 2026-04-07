"""
Jupyter notebook WCI viewer using the extracted core + ipywidgets controls.

Drop-in replacement for ``WCIViewerMultiChannel`` in
``wciviewer_pyqtgraph2.py`` — same constructor signature, same public API
— but built on top of :class:`wciviewer_core.WCICore` and
:class:`control_jupyter.JupyterControlPanel`.
"""

import ipywidgets

from themachinethatgoesping.pingprocessing.widgets.control_jupyter import (
    JupyterControlPanel as JupyterControlPanel,
    create_jupyter_control as create_jupyter_control
)
from themachinethatgoesping.pingprocessing.widgets.control_spec import (
    DropdownSpec as DropdownSpec,
    IntSliderSpec as IntSliderSpec
)
import themachinethatgoesping.pingprocessing.widgets.pyqtgraph_helpers as pgh
from themachinethatgoesping.pingprocessing.widgets.tqdmwidget import (
    TqdmWidget as TqdmWidget
)
from themachinethatgoesping.pingprocessing.widgets.videoframes import (
    VideoFrames as VideoFrames
)
from themachinethatgoesping.pingprocessing.widgets.wciviewer_core import (
    WCICore as WCICore,
    auto_select_grid as auto_select_grid,
    normalise_channels as normalise_channels
)


GRID_LAYOUTS: list = ...

WCI_MISC_SPECS: list = ...

WCI_RENDER_SPECS: list = ...

WCI_STACK_SPECS: list = ...

WCI_TIMING_SPECS: list = ...

WCI_PLAYBACK_SPECS: list = ...

WCI_VIDEO_SPECS: list = ...

WCI_TAB_LAYOUT: dict = ...

class WCIViewerJupyter:
    """
    Multi-channel WCI viewer for Jupyter notebooks.

    This viewer renders water-column images using pyqtgraph (via
    ``jupyter_rfb``) and provides ipywidget controls.  Internally all
    heavy lifting is delegated to :class:`wciviewer_core.WCICore`.

    The constructor signature is intentionally compatible with
    ``WCIViewerMultiChannel`` so you can swap them in notebooks.
    """

    def __init__(self, channels: Union[Dict[str, Sequence[Any]], Sequence[Sequence[Any]]], name: str = 'Multi-Channel WCI', names: Optional[Sequence[Optional[str]]] = None, horizontal_pixels: int = 1024, progress: Optional[Any] = None, show: bool = True, cmap: str = 'YlGnBu_r', widget_height_px: int = 600, widget_width_px: int = 1000, initial_grid: Tuple[int, int] = (2, 2), time_sync_enabled: bool = True, time_warning_threshold: float = 5.0, embedded: bool = False, **kwargs: Any) -> None: ...

    def build_control_widget(self) -> ipywidgets.Widget:
        """Return all controls as a single embeddable ipywidget."""

    def register_ping_change_callback(self, callback: Any) -> None: ...

    def unregister_ping_change_callback(self, callback: Any) -> None: ...

    @property
    def w_index(self): ...

    @property
    def imagebuilder(self): ...

    @property
    def slots(self): ...

    def get_scene(self): ...

    def save_scene(self, filename: str = 'scene.svg') -> None: ...

    def get_matplotlib(self, dpi: int = 150): ...

    def set_widget_height(self, height_px: int) -> None: ...

    def redraw(self, force: bool = True) -> None: ...

    def process_events(self) -> None: ...
