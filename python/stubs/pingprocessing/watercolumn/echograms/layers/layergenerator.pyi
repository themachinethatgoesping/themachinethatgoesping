from themachinethatgoesping.pingprocessing.core.asserts import (
    assert_length as assert_length
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.layers.echolayer import (
    EchoLayer as EchoLayer
)


class LayerGenerator:
    """
    Generate processing layers on a base echogram and copy them to a second echogram.

    Designed for the new EchogramBuilder (backend-based).
    Layers are created in range (or depth) space on ``echogram_base`` and then
    converted to depth coordinates on ``echogram_second``.
    """

    def __init__(self, echogram_base, echogram_second, cut_in_range=True, minslant_relative=0.95, minslant_absolute=-0.5): ...

    def add_layer(self, layer_range, layer_size=1): ...

    def __make_layer__(self, layer_range, layer_size=1): ...

    def __copy_layer__(self, echogram2, layer_name):
        """
        Copy a layer from echogram_base to echogram2, converting to depth coordinates.

        Uses the base echogram's affine transforms to convert sample indices
        to depth values, then adds the layer to echogram2 in depth space.
        """
