from __future__ import annotations
import themachinethatgoesping as Ping
from themachinethatgoesping.pingprocessing.core.progress import get_progress_iterator
from themachinethatgoesping.pingprocessing.watercolumn.image.make_wci import make_wci
from themachinethatgoesping.pingprocessing.watercolumn.image.make_wci import make_wci_dual_head
from themachinethatgoesping.pingprocessing.watercolumn.image.make_wci import make_wci_stack
__all__ = ['ImageBuilder', 'Ping', 'get_progress_iterator', 'make_wci', 'make_wci_dual_head', 'make_wci_stack']
class ImageBuilder:
    def __init__(self, pings, horizontal_pixels, use_beam_sample_view = False, progress = False, **kwargs):
        ...
    def build(self, index, stack = 1, stack_step = 1, **kwargs):
        ...
    def update_args(self, **kwargs):
        ...
