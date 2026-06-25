"""
Lightweight per-ping accessor used by :meth:`EchogramBuilder.iterate_ping_data`.

``PingData`` is a thin, transient view onto one ping of an echogram. Unlike the
old implementation it carries no coordinate state of its own -- it simply
delegates to the echogram, so it can never go out of sync with the echogram's
current axes or layers.
"""

import types

import dt
import np


class PingData:
    """Accessor for a single ping's water-column data and layer slices."""

    __slots__: tuple = ('echogram', 'nr')

    def __init__(self, echogram, nr: int): ...

    def get_wci(self) -> np.ndarray:
        """Full processed water-column column for this ping."""

    def get_wci_layers(self) -> Dict[str, np.ndarray]:
        """Water-column data split by named layer."""

    def get_extent_layers(self, axis_name: Optional[str] = None) -> Dict[str, Tuple[float, float]]:
        """Per-layer outer extents in ``axis_name`` (defaults to current y-axis)."""

    def get_limits_layers(self, axis_name: Optional[str] = None) -> Dict[str, Tuple[float, float]]:
        """Per-layer inner limits in ``axis_name`` (defaults to current y-axis)."""

    def get_ping_time(self) -> float:
        """Ping timestamp (Unix seconds)."""

    def get_datetime(self) -> dt.datetime:
        """Ping time as a timezone-aware datetime."""

    echogram: types.MemberDescriptorType = ...

    nr: types.MemberDescriptorType = ...
