"""
Resolution and caching of :class:`Layer` specifications for one echogram.

The :class:`LayerStore` owns the named layers attached to an echogram's
coordinate system and turns the portable :class:`Layer` specs into concrete
per-ping sample-index bands (and, on demand, display-grid bands).

Caching strategy
----------------
* Sample-index bands depend only on the per-ping geometry, tracked by
  ``coordinate_system.geometry_version``. They are cached and only recomputed
  when that version changes (e.g. new extents / ping times). Crucially they do
  **not** depend on the display y-axis, so switching axes is free.
* Display-grid bands additionally depend on ``coordinate_system.display_version``
  and are recomputed lazily when the display axis changes.

A *named* layer is a list of one or more :class:`Layer` specs that are combined
by **intersection** in sample space. This makes the common "valid mask = several
constraints" pattern natural and supports mixing references (e.g. a depth band
intersected with a bottom-relative band).
"""

import types

import np

from themachinethatgoesping.pingprocessing.watercolumn.echograms.layers.layer import (
    Layer as Layer
)


class ResolvedBand:
    """
    A resolved per-ping sample-index band, with lazy display-grid projection.

    Attributes
    ----------
    i0, i1:
        Per-ping sample-index bounds (``i0`` inclusive, ``i1`` exclusive).
    y0, y1:
        Per-ping display-grid index bounds for the *current* y-axis, computed
        lazily and refreshed when the display axis changes.
    """

    __slots__: tuple = ...

    def __init__(self, cs, i0: np.ndarray, i1: np.ndarray): ...

    @property
    def y0(self) -> np.ndarray: ...

    @property
    def y1(self) -> np.ndarray: ...

    def bounds(self, reference: str) -> Tuple[np.ndarray, np.ndarray]:
        """Return per-ping ``(lower, upper)`` values in ``reference`` units."""

    i0: types.MemberDescriptorType = ...

    i1: types.MemberDescriptorType = ...

class LayerStore:
    """Manages named layers for one echogram coordinate system."""

    def __init__(self, cs): ...

    def add(self, name: str, layer, *, combine: bool = True) -> None:
        """
        Add a layer spec under ``name``.

        If ``name`` already exists and ``combine`` is True, the new spec is
        intersected with the existing ones; otherwise it replaces them. A list
        of specs may be passed to set several intersected constraints at once.
        """

    def remove(self, name: str) -> None: ...

    def clear(self) -> None: ...

    def rename(self, old: str, new: str) -> None: ...

    def names(self) -> List[str]: ...

    def keys(self): ...

    def values(self): ...

    def specs(self, name: str) -> List[Layer]: ...

    def __contains__(self, name: str) -> bool: ...

    def __len__(self) -> int: ...

    def __iter__(self): ...

    def __getitem__(self, name: str) -> ResolvedBand: ...

    def get(self, name: str) -> Optional[ResolvedBand]: ...

    def items(self): ...

    def resolve(self, name: str) -> ResolvedBand:
        """Resolve ``name`` to a :class:`ResolvedBand` (cached by geometry)."""

    def sample_indices(self, name: str) -> Tuple[np.ndarray, np.ndarray]: ...

    def grid_indices(self, name: str) -> Tuple[np.ndarray, np.ndarray]: ...

    def bounds(self, name: str, reference: str) -> Tuple[np.ndarray, np.ndarray]: ...
