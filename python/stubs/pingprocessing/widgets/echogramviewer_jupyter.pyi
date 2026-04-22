"""
Jupyter notebook echogram viewer using the extracted core + ipywidgets controls.

Drop-in replacement for ``EchogramViewerMultiChannel`` in
``echogramviewer_pyqtgraph2.py`` — same constructor signature, same public API
— but built on top of :class:`echogramviewer_core.EchogramCore` and
:class:`control_jupyter.JupyterControlPanel`.
"""

import ipywidgets

from themachinethatgoesping.pingprocessing.widgets.control_jupyter import (
    JupyterControlHandle as JupyterControlHandle,
    JupyterControlPanel as JupyterControlPanel,
    create_jupyter_control as create_jupyter_control
)
from themachinethatgoesping.pingprocessing.widgets.control_spec import (
    DropdownSpec as DropdownSpec
)
from themachinethatgoesping.pingprocessing.widgets.echogramviewer_core import (
    EchogramCore as EchogramCore,
    auto_select_grid as auto_select_grid,
    normalise_echograms as normalise_echograms
)
import themachinethatgoesping.pingprocessing.widgets.pyqtgraph_helpers as pgh
from themachinethatgoesping.pingprocessing.widgets.tqdmwidget import (
    TqdmWidget as TqdmWidget
)


GRID_LAYOUTS: list = ...

ECHO_RENDER_SPECS: list = ...

ECHO_NAV_SPECS: list = ...

ECHO_MISC_SPECS: list = ...

ECHO_PARAM_SPECS: list = ...

ECHO_PARAM_DISPLAY_SPECS: list = ...

class EchogramViewerJupyter:
    """
    Multi-echogram viewer for Jupyter notebooks.

    This viewer renders echogram images via pyqtgraph (``jupyter_rfb``)
    and exposes ipywidget controls. Internally all heavy lifting is
    delegated to :class:`echogramviewer_core.EchogramCore`.

    The constructor signature is intentionally compatible with
    ``EchogramViewerMultiChannel`` so you can swap them in notebooks.
    """

    def __init__(self, echogramdata: Union[Dict[str, Any], Sequence[Any], Any], name: str = 'Multi-Echogram Viewer', names: Optional[Sequence[Optional[str]]] = None, progress: Optional[Any] = None, show: bool = True, voffsets: Optional[Dict[str, float]] = None, cmap: str = 'Greys_r', cmap_layer: str = 'YlGnBu_r', fps: int = 25, widget_height_px: int = 600, widget_width_px: int = 1000, auto_update: bool = True, auto_update_delay_ms: int = 300, initial_grid: Tuple[int, int] = (2, 2), embedded: bool = False, **kwargs: Any) -> None: ...

    def build_control_widget(self) -> ipywidgets.Widget:
        """Return all controls as a single embeddable ipywidget."""

    @property
    def slots(self): ...

    @property
    def slot_selectors(self): ...

    def get_scene(self): ...

    def save_scene(self, filename: str = 'scene.svg') -> None: ...

    def get_matplotlib(self, dpi: int = 150): ...

    def get_xlim(self): ...

    def get_ylim(self): ...

    def set_widget_size(self, width_px: int, height_px: int) -> None: ...

    def pan_view(self, direction: str, fraction: float = 0.25) -> None: ...

    def connect_pingviewer(self, pingviewer: Any, **kwargs) -> None: ...

    def disconnect_pingviewer(self) -> None: ...

    def update_ping_lines(self) -> None: ...

    def show_single(self, echogram_name: str) -> None: ...

    def add_station_times(self, stations, **kwargs) -> None: ...

    def clear_station_times(self, station_name=None) -> None: ...

    def show(self) -> None: ...

    def redraw(self, force: bool = True) -> None: ...

    def process_events(self) -> None: ...

    def cleanup(self) -> None: ...

    def __del__(self) -> None: ...
