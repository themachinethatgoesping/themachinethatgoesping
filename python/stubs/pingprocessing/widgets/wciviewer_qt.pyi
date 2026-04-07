r"""
Native Qt WCI viewer using pyqtgraph DockArea + extracted WCICore.

This module provides a standalone Qt application for viewing water-column
images without Jupyter.  The layout uses ``pyqtgraph.dockarea`` so the
user can drag, float, and rearrange panels.

Usage (standalone)::

    python -m themachinethatgoesping.pingprocessing.widgets.wciviewer_qt \
        --help

Or programmatically::

    from themachinethatgoesping.pingprocessing.widgets.wciviewer_qt import WCIViewerQt
    viewer = WCIViewerQt(channels)
    viewer.show()
    viewer.run()   # blocks in QApplication.exec()
"""

import PySide6.QtCore
import PySide6.QtWidgets
import QtWidgets

from themachinethatgoesping.pingprocessing.widgets.control_qt import (
    QtControlHandle as QtControlHandle,
    QtControlPanel as QtControlPanel,
    create_qt_control as create_qt_control
)
from themachinethatgoesping.pingprocessing.widgets.control_spec import (
    DropdownSpec as DropdownSpec,
    IntSliderSpec as IntSliderSpec
)
import themachinethatgoesping.pingprocessing.widgets.pyqtgraph_helpers as pgh
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

class WCIViewerQt(PySide6.QtWidgets.QMainWindow):
    """
    Standalone native Qt WCI viewer window.

    Parameters match :class:`wciviewer_jupyter.WCIViewerJupyter` so the
    two viewers are interchangeable at construction time.
    """

    def __init__(self, channels: Union[Dict[str, Sequence[Any]], Sequence[Sequence[Any]]], name: str = 'Multi-Channel WCI', names: Optional[Sequence[Optional[str]]] = None, horizontal_pixels: int = 1024, progress: Optional[Any] = None, cmap: str = 'YlGnBu_r', show: bool = True, embedded: bool = False, widget_height_px: int = 800, widget_width_px: int = 1200, initial_grid: Tuple[int, int] = (2, 2), time_sync_enabled: bool = True, time_warning_threshold: float = 5.0, parent: Optional[QtWidgets.QWidget] = None, **kwargs: Any) -> None: ...

    def build_control_widget(self) -> QtWidgets.QWidget:
        """
        Return all controls as a single embeddable QWidget.

        Used by the combined viewer to embed this viewer's controls in a
        shared tab widget.  The viewer must have been created with
        ``show=False`` (or ``embedded=True``).
        """

    def run(self) -> None:
        """Enter the Qt event loop (blocking).  Call after ``.show()``."""

    def register_ping_change_callback(self, callback: Any) -> None: ...

    def unregister_ping_change_callback(self, callback: Any) -> None: ...

    @property
    def slots(self): ...

    @property
    def imagebuilder(self): ...

    staticMetaObject: PySide6.QtCore.QMetaObject = ...
