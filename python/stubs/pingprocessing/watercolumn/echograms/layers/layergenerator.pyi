from themachinethatgoesping.pingprocessing.core.asserts import (
    assert_length as assert_length
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.layers.echolayer import (
    EchoLayer as EchoLayer
)


class LayerGenerator:
    def __init__(self, echogram_base, echogram_second, cut_in_range=True, minslant_relative=0.95, minslant_absolute=-0.5): ...

    def add_layer(self, layer_range, layer_size=1): ...

    def __make_layer__(self, layer_range, layer_size=1): ...

    def __copy_layer__(self, echogram2, layer_name): ...
