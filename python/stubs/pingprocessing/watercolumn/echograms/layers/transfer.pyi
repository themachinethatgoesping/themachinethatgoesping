"""
Transfer layers between echograms through a shared physical reference.

This replaces the old ``LayerGenerator``. The idea is simple: a layer resolved
on a *source* echogram is read back as per-ping ``(lower, upper)`` values in a
shared reference (depth by default), then re-created on a *destination*
echogram as a time-referenced :class:`Layer`. Because the destination resolves
the band against its own geometry, a band defined in one echogram (e.g. a range
band on a slanted MBES beam) is reproduced at the *same physical extent* (e.g.
the same depths) on another echogram with different geometry.

Example
-------
::

    # range band on a slanted MBES beam, restricted to a 'valid' mask
    mbes.add_layer('10m', Layer.range(9.0, 11.0))
    mbes.add_layer('10m', mbes.layers.specs('valid'))  # intersect

    # reproduce the same depth coverage on the downward-looking echosounder
    transfer_layer(mbes, sbes, '10m', reference='Depth (m)', mask='valid')
"""

from themachinethatgoesping.pingprocessing.watercolumn.echograms.layers.layer import (
    Boundary as Boundary,
    Layer as Layer
)


def transfer_layer(src, dst, name: str, *, reference: str = 'Depth (m)', new_name: Optional[str] = None, mask: Optional[str] = None, combine: bool = False) -> Layer:
    """
    Transfer one layer from ``src`` to ``dst`` via ``reference``.

    Args:
        src: Source echogram (must contain layer ``name``).
        dst: Destination echogram.
        name: Layer name on ``src``.
        reference: Shared physical reference used to carry the band across
            (``'Depth (m)'`` by default; any reference both echograms support).
        new_name: Name to use on ``dst`` (defaults to ``name``).
        mask: Optional layer name on ``dst`` whose constraints are intersected
            into the transferred band (e.g. a per-echogram 'valid' mask).
        combine: If ``True``, intersect with an existing ``dst`` layer of the
            same name instead of replacing it.

    Returns:
        The :class:`Layer` created on ``dst``.
    """

def transfer_layers(src, dst, names: Optional[Iterable[str]] = None, *, reference: str = 'Depth (m)', mask: Optional[str] = None, combine: bool = False) -> List[Layer]:
    """
    Transfer several (or all) named layers from ``src`` to ``dst``.

    Args:
        src: Source echogram.
        dst: Destination echogram.
        names: Layer names to transfer. ``None`` transfers all named layers.
        reference: Shared physical reference (default depth).
        mask: Optional ``dst`` layer name to intersect into each transferred band.
        combine: If ``True``, intersect with existing same-named ``dst`` layers.

    Returns:
        The list of created layers.
    """
