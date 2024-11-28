from __future__ import annotations
import themachinethatgoesping as theping
from themachinethatgoesping.pingprocessing.core.progress import get_progress_iterator
from themachinethatgoesping.pingprocessing.watercolumn.image.make_wci import make_beam_sample_image
from themachinethatgoesping.pingprocessing.watercolumn.image.make_wci import make_wci
from themachinethatgoesping.pingprocessing.watercolumn.image.make_wci import make_wci_dual_head
from themachinethatgoesping.pingprocessing.watercolumn.image.make_wci import make_wci_stack
import typing
__all__ = ['ImageBuilder', 'get_progress_iterator', 'make_beam_sample_image', 'make_wci', 'make_wci_dual_head', 'make_wci_stack', 'theping']
class ImageBuilder:
    __firstlineno__: typing.ClassVar[int] = 6
    __static_attributes__: typing.ClassVar[tuple] = ('beam_sample_view', 'default_args', 'pings', 'progress')
    def __init__(self, pings, horizontal_pixels, wci_render = 'linear', progress = False, **kwargs):
        ...
    def build(self, index, stack = 1, stack_step = 1, **kwargs):
        ...
    def update_args(self, wci_render = 'linear', **kwargs):
        ...
