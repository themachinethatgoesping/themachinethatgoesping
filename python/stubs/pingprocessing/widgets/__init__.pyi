from . import (
    echogramviewer as echogramviewer,
    echogramviewer_pyqtgraph as echogramviewer_pyqtgraph,
    echogramviewer_pyqtgraph2 as echogramviewer_pyqtgraph2,
    mapviewer_pyqtgraph as mapviewer_pyqtgraph,
    pyqtgraph_helpers as pyqtgraph_helpers,
    tools as tools,
    tqdmwidget as tqdmwidget,
    wciviewer as wciviewer,
    wciviewer_pyqtgraph as wciviewer_pyqtgraph,
    wciviewer_pyqtgraph2 as wciviewer_pyqtgraph2
)
from .echogramviewer import EchogramViewer as EchogramViewer
from .echogramviewer_pyqtgraph import (
    EchogramViewerPyQtGraph as EchogramViewerPyQtGraph
)
from .echogramviewer_pyqtgraph2 import (
    EchogramViewerMultiChannel as EchogramViewerMultiChannel
)
from .mapviewer_pyqtgraph import (
    MapViewerPyQtGraph as MapViewerPyQtGraph
)
from .tqdmwidget import TqdmWidget as TqdmWidget
from .wciviewer import WCIViewer as WCIViewer
from .wciviewer_pyqtgraph import (
    WCIViewerPyQtGraph as WCIViewerPyQtGraph
)
from .wciviewer_pyqtgraph2 import (
    WCIViewerMultiChannel as WCIViewerMultiChannel
)
import themachinethatgoesping as theping
import themachinethatgoesping.echosounders as echosounders
import themachinethatgoesping.pingprocessing.watercolumn.echograms as echograms
import themachinethatgoesping.pingprocessing.watercolumn.helper.make_image_helper as mi_hlp
import themachinethatgoesping.pingprocessing.watercolumn.image as mi


WCI_VALUE_CHOICES: list = ...
