"""
Native Qt combined viewer using pyqtgraph DockArea.

Thin wrapper that hosts existing viewer instances (created with
``embedded=True``) in a shared :class:`QMainWindow` with dockable
graphics panels and a dockable control sidebar.

All docks (graphics **and** controls) are movable and can optionally
be floated to a second monitor.

Usage::

    from themachinethatgoesping.pingprocessing.widgets import (
        CombinedViewerQt, WCIViewerQt, EchogramViewerQt, MapViewerQt,
    )

    wci = WCIViewerQt(channels, embedded=True, show=False)
    echo = EchogramViewerQt(echogramdata, embedded=True, show=False)
    map_ = MapViewerQt(builder=builder, tile_builder=tb, embedded=True, show=False)

    cv = CombinedViewerQt()
    cv.add(wci, name="WCI")
    cv.add(echo, name="Echogram")
    cv.add(map_, name="Map")

    # manual cross-wiring
    echo.core.connect_pingviewer(wci.core)
    map_.core.connect_echogram_viewer(echo.core)
    map_.core.connect_wci_viewer(wci.core)

    cv.show()
"""

import PySide6.QtCore
import PySide6.QtWidgets
import QtWidgets

from themachinethatgoesping.pingprocessing.widgets.combinedviewer_core import (
    CombinedViewerCore as CombinedViewerCore,
    ViewerEntry as ViewerEntry
)
import themachinethatgoesping.pingprocessing.widgets.pyqtgraph_helpers as pgh


class CombinedViewerQt(PySide6.QtWidgets.QMainWindow):
    """
    QMainWindow hosting multiple embedded viewer instances.

    Every panel — graphics *and* the shared controls tab — lives in a
    pyqtgraph :class:`Dock` so it can be dragged, re-arranged, or
    floated to a secondary screen.
    """

    def __init__(self, title: str = 'Combined Viewer', width: int = 1600, height: int = 900, parent: Optional[QtWidgets.QWidget] = None, settings_key: str = 'CombinedViewerQt') -> None: ...

    @property
    def core(self) -> CombinedViewerCore: ...

    @property
    def entries(self): ...

    def add(self, viewer: Any, name: str = '', position: str = 'auto') -> ViewerEntry:
        """
        Add an existing viewer instance (created with ``embedded=True``).

        Parameters
        ----------
        viewer
            A viewer instance with ``.graphics`` and ``.build_control_widget()``
            attributes.
        name
            Dock / tab label.
        position
            Dock position hint: ``"top"``, ``"bottom"``, ``"left"``,
            ``"right"``, or ``"auto"`` (stacks below existing graphics docks).
        """

    def remove(self, entry: ViewerEntry) -> None:
        """Remove a viewer from the combined window."""

    def show(self) -> None:
        """Show the window and restore saved dock arrangement."""

    def closeEvent(self, event) -> None:
        """Auto-save window geometry and dock arrangement on close."""

    def save_state(self) -> None:
        """Explicitly save window geometry and dock arrangement."""

    def restore_state(self) -> None:
        """Explicitly restore window geometry and dock arrangement."""

    def run(self) -> None:
        """Start the Qt event loop (convenience for scripts)."""

    staticMetaObject: PySide6.QtCore.QMetaObject = ...
