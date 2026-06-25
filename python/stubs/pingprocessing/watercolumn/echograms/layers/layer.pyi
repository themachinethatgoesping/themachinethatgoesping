"""
Portable, echogram-independent layer (region-of-interest) specifications.

A :class:`Layer` describes a vertical band (a region of interest) per ping by a
*lower* and an *upper* boundary curve expressed in a fixed **reference frame**
(``'Depth (m)'``, ``'Range (m)'``, ``'Sample number'`` or ``'Y indice'``).

Key design properties
----------------------
* A layer owns **no** echogram. It is a lightweight, reusable spec.
* Binding a layer to an echogram resolves the boundaries to **sample indices**
  (the data-anchored canonical representation) using that echogram's per-ping
  geometry. This is independent of the current display y-axis, so changing the
  display axis never invalidates a layer.
* Because resolution goes through a physical reference, the same layer can be
  applied to *different* echograms, and a band resolved on one echogram can be
  read back in any reference (e.g. depth) and transferred to another echogram.

Boundaries
----------
Each boundary (lower/upper) is one of:

* a constant value (in the layer's reference units),
* a per-ping array (already aligned to the echogram's pings),
* a time series ``(timestamps, values)`` interpolated onto the ping times,
* a ping-parameter reference (e.g. ``'bottom'``) with ``scale``/``offset``,
* ``None`` meaning "open" (the top resp. bottom of the data).
"""

from collections.abc import Sequence as _Sequence
import types
from typing import TypeAlias, Union

import np
import numpy


REFERENCES: tuple = ...

BoundaryLike: TypeAlias = Union[float, int, _Sequence[float], numpy.ndarray, 'Boundary', None]

class Boundary:
    """
    One boundary curve (lower or upper) of a :class:`Layer`.

    Resolves, against an ``EchogramCoordinateSystem``, to a per-ping float array
    (length ``n_pings``) expressed in the layer's reference units. ``None``
    values mark an *open* boundary that the layer maps to the data extent.
    """

    __slots__: tuple = ...

    def __init__(self, kind, *, value=None, values=None, timestamps=None, series=None, param=None, scale=1.0, offset=0.0): ...

    @classmethod
    def const(cls, value: float) -> 'Boundary': ...

    @classmethod
    def open(cls) -> 'Boundary': ...

    @classmethod
    def per_ping(cls, values: Sequence[float]) -> 'Boundary': ...

    @classmethod
    def time_series(cls, timestamps, values, *, scale=1.0, offset=0.0) -> 'Boundary': ...

    @classmethod
    def from_param(cls, param: str, *, scale=1.0, offset=0.0) -> 'Boundary': ...

    @classmethod
    def coerce(cls, obj: BoundaryLike) -> 'Boundary':
        """
        Turn a user value into a :class:`Boundary`.

        * ``None`` -> open boundary
        * scalar -> constant
        * array-like -> per-ping
        * :class:`Boundary` -> returned unchanged
        """

    def resolve(self, cs, reference: str) -> np.ndarray:
        """Resolve to a per-ping array in ``reference`` units (NaN where open)."""

    def is_open(self) -> bool: ...

    kind: types.MemberDescriptorType = ...

    offset: types.MemberDescriptorType = ...

    param: types.MemberDescriptorType = ...

    scale: types.MemberDescriptorType = ...

    series: types.MemberDescriptorType = ...

    timestamps: types.MemberDescriptorType = ...

    value: types.MemberDescriptorType = ...

    values: types.MemberDescriptorType = ...

class Layer:
    """
    A region of interest defined by lower/upper boundaries in a reference frame.

    Parameters
    ----------
    reference:
        One of ``'Depth (m)'``, ``'Range (m)'``, ``'Sample number'``,
        ``'Y indice'`` -- the units the boundaries are expressed in.
    lower, upper:
        Boundary specifications. Each accepts a scalar, a per-ping array, a
        :class:`Boundary`, or ``None`` (open). ``lower`` is the shallower /
        smaller-value edge, ``upper`` the deeper / larger-value edge.
    name:
        Optional layer name (informational; the echogram stores layers by name).
    """

    def __init__(self, reference: str, lower: BoundaryLike, upper: BoundaryLike, name: Optional[str] = None): ...

    def __repr__(self) -> str: ...

    @classmethod
    def depth(cls, lower: BoundaryLike, upper: BoundaryLike, name=None) -> 'Layer':
        """A band between two depths (meters)."""

    @classmethod
    def range(cls, lower: BoundaryLike, upper: BoundaryLike, name=None) -> 'Layer':
        """A band between two ranges (meters)."""

    @classmethod
    def sample_number(cls, lower: BoundaryLike, upper: BoundaryLike, name=None) -> 'Layer':
        """A band between two sample numbers."""

    @classmethod
    def y_indice(cls, lower: BoundaryLike, upper: BoundaryLike, name=None) -> 'Layer':
        """A band between two raw sample indices."""

    @classmethod
    def from_param_absolute(cls, param: str, offset_lower: Optional[float], offset_upper: Optional[float], *, reference: str = 'Depth (m)', name=None) -> 'Layer':
        """
        Band at ``param + offset`` for each edge (``None`` -> open).

        Example: ``Layer.from_param_absolute('bottom', -1.0, +1.0)`` is the
        1 m band straddling the bottom.
        """

    @classmethod
    def from_param_relative(cls, param: str, scale_lower: Optional[float], scale_upper: Optional[float], *, reference: str = 'Depth (m)', name=None) -> 'Layer':
        """
        Band at ``param * scale`` for each edge (``None`` -> open).

        Example: ``Layer.from_param_relative('bottom', 0.0, 1.2)`` covers from
        the surface to 1.2x the bottom value.
        """

    @classmethod
    def from_param(cls, param: str, *, scale_lower=1.0, offset_lower=0.0, scale_upper=1.0, offset_upper=0.0, reference: str = 'Depth (m)', name=None) -> 'Layer':
        """General param band: ``param*scale + offset`` for each edge."""

    @classmethod
    def from_time_series(cls, reference: str, timestamps, values, *, offset_lower: float = 0.0, offset_upper: float = 0.0, name=None) -> 'Layer':
        """
        Band straddling a time-referenced value series (e.g. a sensor depth).

        Example (sensor depth +/- 1 m)::

            Layer.from_time_series('Depth (m)', times, depths,
                                   offset_lower=-1.0, offset_upper=+1.0)
        """

    @classmethod
    def from_sample_indices(cls, i0, i1, name=None) -> 'Layer':
        """
        Build a layer that resolves to exact per-ping sample-index bounds.

        Mainly used for persistence (exact round-trips). The bounds are tied to
        a specific ping count, so such a layer is not portable across echograms
        with a different number of pings.
        """

    def resolve_bounds(self, cs) -> Tuple[np.ndarray, np.ndarray]:
        """
        Resolve to per-ping ``(lower_value, upper_value)`` in reference units.

        Open boundaries are returned as the data extent (sample 0 resp. the last
        sample mapped into the reference), so the result always spans the full
        available band where a boundary is open.
        """

    def resolve_sample_indices(self, cs) -> Tuple[np.ndarray, np.ndarray]:
        """
        Resolve to per-ping ``(i0, i1)`` sample-index bounds (i1 exclusive).

        ``i0`` is inclusive, ``i1`` exclusive. Degenerate / undefined pings map
        to ``i0 == i1 == 0`` (empty band).
        """
