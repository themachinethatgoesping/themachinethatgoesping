"""
Echogram layer system: portable region-of-interest specs and aggregation.

Public API
----------
* :class:`Layer` / :class:`Boundary` -- portable, echogram-independent layer specs.
* :class:`LayerStore` / :class:`ResolvedBand` -- per-echogram resolution + caching.
* :class:`PingData` -- lightweight per-ping accessor.
* :func:`transfer_layer` / :func:`transfer_layers` -- move layers between echograms
  through a shared physical reference (depth by default).

For pooling layer samples into time blocks and cross-calibrating echograms, see
the sibling :mod:`..calibration` subpackage.
"""

from themachinethatgoesping.pingprocessing.watercolumn.echograms.layers import (
    layer as layer,
    pingdata as pingdata,
    store as store,
    transfer as transfer
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.layers.layer import (
    Boundary as Boundary,
    Layer as Layer
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.layers.pingdata import (
    PingData as PingData
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.layers.store import (
    LayerStore as LayerStore,
    ResolvedBand as ResolvedBand
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.layers.transfer import (
    transfer_layer as transfer_layer,
    transfer_layers as transfer_layers
)


REFERENCES: tuple = ...

__all__: list = ['Boundary', 'Layer', 'REFERENCES', 'LayerStore', 'ResolvedBand', 'PingData', 'transfer_layer', 'transfer_layers']
