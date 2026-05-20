"""
Native Qt echogram viewer using pyqtgraph DockArea + extracted EchogramCore.

This module provides a standalone Qt application for viewing echograms
without Jupyter.  The layout uses ``pyqtgraph.dockarea`` so the user can
drag, float, and rearrange panels.

Usage::

    from themachinethatgoesping.widgets.echogramviewer_qt import EchogramViewerQt
    viewer = EchogramViewerQt(echogramdata)
    viewer.show()
    viewer.run()   # blocks in QApplication.exec()
"""

import PySide6.QtCore
import PySide6.QtWidgets
import QtWidgets

from themachinethatgoesping.widgets.control_qt import (
    QtControlHandle as QtControlHandle,
    QtControlPanel as QtControlPanel,
    create_qt_control as create_qt_control
)
from themachinethatgoesping.widgets.control_spec import (
    DropdownSpec as DropdownSpec
)
from themachinethatgoesping.widgets.echogramviewer_core import (
    EchogramCore as EchogramCore,
    auto_select_grid as auto_select_grid,
    normalise_echograms as normalise_echograms
)
import themachinethatgoesping.widgets.pyqtgraph_helpers as pgh
from themachinethatgoesping.widgets.wciviewer_qt import (
    _QtProgressBar as _QtProgressBar
)


GRID_LAYOUTS: list = ...

ECHO_RENDER_SPECS: list = ...

ECHO_NAV_SPECS: list = ...

ECHO_MISC_SPECS: list = ...

ECHO_PARAM_SPECS: list = ...

ECHO_PARAM_DISPLAY_SPECS: list = ...

ECHO_TAB_LAYOUT: dict = ...

class EchogramViewerQt(PySide6.QtWidgets.QMainWindow):
    """
    Standalone native Qt echogram viewer window.

    Parameters match :class:`echogramviewer_jupyter.EchogramViewerJupyter`
    so the two viewers are interchangeable at construction time.
    """

    def __init__(self, echogramdata: Union[Dict[str, Any], Sequence[Any], Any], name: str = 'Multi-Echogram Viewer', names: Optional[Sequence[Optional[str]]] = None, progress: Optional[Any] = None, cmap: str = 'Greys_r', cmap_layer: str = 'YlGnBu_r', show: bool = True, embedded: bool = False, voffsets: Optional[Dict[str, float]] = None, widget_height_px: int = 800, widget_width_px: int = 1200, auto_update: bool = True, auto_update_delay_ms: int = 300, initial_grid: Tuple[int, int] = (2, 2), parent: Optional[QtWidgets.QWidget] = None, **kwargs: Any) -> None: ...

    def eventFilter(self, obj, event): ...

    def build_control_widget(self) -> QtWidgets.QWidget:
        """Return all controls as a single embeddable QWidget."""

    def run(self) -> None:
        """Enter the Qt event loop (blocking)."""

    @property
    def slots(self): ...

    @property
    def slot_selectors(self): ...

    def get_scene(self): ...

    def save_scene(self, filename: str = 'scene.svg') -> None: ...

    def get_matplotlib(self, dpi: int = 150): ...

    def get_xlim(self): ...

    def get_ylim(self): ...

    def pan_view(self, direction: str, fraction: float = 0.25) -> None: ...

    def connect_pingviewer(self, pingviewer: Any, **kwargs) -> None: ...

    def disconnect_pingviewer(self) -> None: ...

    def update_ping_lines(self) -> None: ...

    def show_single(self, echogram_name: str) -> None: ...

    def add_station_times(self, stations, **kwargs) -> None: ...

    def clear_station_times(self, station_name=None) -> None: ...

    def reset_view(self) -> None: ...

    def cleanup(self) -> None: ...

    def closeEvent(self, event) -> None: ...

    def __del__(self) -> None: ...

    staticMetaObject: PySide6.QtCore.QMetaObject = ...
