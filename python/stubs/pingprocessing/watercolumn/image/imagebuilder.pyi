from themachinethatgoesping.pingprocessing.core.progress import (
    get_progress_iterator as get_progress_iterator
)
from themachinethatgoesping.pingprocessing.watercolumn.image.make_wci import (
    downsample_wci as downsample_wci,
    make_beam_sample_image as make_beam_sample_image,
    make_wci as make_wci,
    make_wci_dual_head as make_wci_dual_head,
    make_wci_stack as make_wci_stack
)


class ImageBuilder:
    def __init__(self, pings, horizontal_pixels, wci_render='linear', progress=False, oversampling=1, oversampling_mode='linear_mean', **kwargs): ...

    def update_args(self, wci_render='linear', oversampling=None, oversampling_mode=None, **kwargs): ...

    def build(self, index, stack=1, stack_step=1, **kwargs): ...
