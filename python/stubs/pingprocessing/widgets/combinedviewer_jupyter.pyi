"""
Jupyter notebook combined viewer using ipywidgets layout.

Thin wrapper that hosts existing viewer instances (created with
``embedded=True``) in a shared layout with a tabbed control panel.

Usage::

    from themachinethatgoesping.pingprocessing.widgets import (
        CombinedViewerJupyter, WCIViewerJupyter, EchogramViewerJupyter,
        MapViewerJupyter,
    )

    wci = WCIViewerJupyter(channels, embedded=True, show=False)
    echo = EchogramViewerJupyter(echogramdata, embedded=True, show=False)
    map_ = MapViewerJupyter(builder=builder, tile_builder=tb, embedded=True, show=False)

    cv = CombinedViewerJupyter()
    cv.add(wci, name="WCI")
    cv.add(echo, name="Echogram")
    cv.add(map_, name="Map")

    # manual cross-wiring
    echo.core.connect_pingviewer(wci.core)
    map_.core.connect_echogram_viewer(echo.core)
    map_.core.connect_wci_viewer(wci.core)

    cv.show()
"""

from themachinethatgoesping.pingprocessing.widgets.combinedviewer_core import (
    CombinedViewerCore as CombinedViewerCore,
    ViewerEntry as ViewerEntry
)


class CombinedViewerJupyter:
    """Jupyter combined viewer hosting multiple embedded viewer instances."""

    def __init__(self) -> None: ...

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
            Tab label for controls.
        position
            Unused for now; reserved for future grid layout control.
        """

    def remove(self, entry: ViewerEntry) -> None:
        """Remove a viewer from the combined widget."""

    def show(self) -> None:
        """Display the combined viewer widget."""
