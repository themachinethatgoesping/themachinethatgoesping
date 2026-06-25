"""
Echogram layer system: portable region-of-interest specs and aggregation.

Public API
----------
* :class:`Layer` / :class:`Boundary` -- portable, echogram-independent layer specs.
* :class:`LayerStore` / :class:`ResolvedBand` -- per-echogram resolution + caching.
* :class:`PingData` -- lightweight per-ping accessor.
* :func:`transfer_layer` / :func:`transfer_layers` -- move layers between echograms
  through a shared physical reference (depth by default).
* :class:`LayerProcessor` -- pool layer samples into time blocks for comparison /
  calibration across echograms.
"""

from . import (
    layer as layer,
    pingdata as pingdata,
    processor as processor,
    store as store,
    transfer as transfer
)
from .layer import Boundary as Boundary, Layer as Layer
from .pingdata import PingData as PingData
from .processor import LayerProcessor as LayerProcessor
from .store import (
    LayerStore as LayerStore,
    ResolvedBand as ResolvedBand
)
from .transfer import (
    transfer_layer as transfer_layer,
    transfer_layers as transfer_layers
)


REFERENCES: tuple = ...

__all__: list = ['Boundary', 'Layer', 'REFERENCES', 'LayerStore', 'ResolvedBand', 'PingData', 'transfer_layer', 'transfer_layers', 'LayerProcessor']
