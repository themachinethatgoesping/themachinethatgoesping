import datetime
from typing import Union

import numpy

from themachinethatgoesping.pingprocessing.core.asserts import (
    assert_length as assert_length
)
import themachinethatgoesping.tools as tools


TYPE_CHECKING: bool = False

class EchoLayer:
    """
    Represents a region of interest within an echogram.

    A layer defines upper and lower bounds in Y coordinates that can vary
    across pings (X axis). This is useful for isolating specific water column
    regions like the bottom layer, surface layer, or acoustic layers.

    Attributes:
        echodata: Reference to the parent EchogramBuilder.
        i0: Array of start sample indices per ping.
        i1: Array of end sample indices per ping (exclusive).
        y0: Array of start grid indices per ping.
        y1: Array of end grid indices per ping.
        vec_min_y: Array of minimum Y coordinates per ping.
        vec_max_y: Array of maximum Y coordinates per ping.
    """

    def __init__(self, echodata: EchogramBuilder, vec_x_val, vec_min_y, vec_max_y):
        """
        Create a layer with explicit boundaries.

        Args:
            echodata: Parent EchogramBuilder instance.
            vec_x_val: X values (timestamps, indices, or datetimes) for boundary points.
            vec_min_y: Minimum Y values (depths, ranges, etc.) at each X point.
            vec_max_y: Maximum Y values at each X point.
        """

    def set_indices(self, i0, i1, vec_min_y, vec_max_y):
        """
        Set layer sample indices and update grid indices.

        Args:
            i0: Start sample indices per ping.
            i1: End sample indices per ping (exclusive).
            vec_min_y: Minimum Y coordinates per ping.
            vec_max_y: Maximum Y coordinates per ping.
        """

    def update_y_gridder(self):
        """Update grid indices after coordinate system change."""

    @classmethod
    def from_static_layer(cls, echodata: EchogramBuilder, min_y: float, max_y: float) -> EchoLayer:
        """
        Create a layer with static (constant) boundaries.

        Args:
            echodata: Parent EchogramBuilder instance.
            min_y: Constant minimum Y value across all pings.
            max_y: Constant maximum Y value across all pings.

        Returns:
            New EchoLayer instance.
        """

    @classmethod
    def from_ping_param_offsets_absolute(cls, echodata: EchogramBuilder, ping_param_name: str, offset_0: Union[float, None], offset_1: Union[float, None]) -> EchoLayer:
        """
        Create a layer based on absolute offsets from a ping parameter.

        Args:
            echodata: Parent EchogramBuilder instance.
            ping_param_name: Name of the ping parameter (e.g., 'bottom').
            offset_0: Absolute offset for upper bound (added to param).
            offset_1: Absolute offset for lower bound (added to param).

        Returns:
            New EchoLayer instance.
        """

    @classmethod
    def from_ping_param_offsets_relative(cls, echodata: EchogramBuilder, ping_param_name: str, offset_0: Union[float, None], offset_1: Union[float, None]) -> EchoLayer:
        """
        Create a layer based on relative offsets from a ping parameter.

        Args:
            echodata: Parent EchogramBuilder instance.
            ping_param_name: Name of the ping parameter (e.g., 'bottom').
            offset_0: Relative multiplier for upper bound.
            offset_1: Relative multiplier for lower bound.

        Returns:
            New EchoLayer instance.
        """

    def get_y_indices(self, wci_nr: int) -> tuple[Union[numpy.ndarray, None], Union[numpy.ndarray, None]]:
        """
        Get Y indices constrained to layer bounds.

        Uses precomputed affine coefficients for speed.

        Args:
            wci_nr: Ping/column number.

        Returns:
            Tuple of (image_indices, data_indices) arrays, or (None, None) if no valid range.
        """

    def combine(self, other: EchoLayer):
        """
        Combine this layer with another by taking the intersection.

        The resulting layer will have the more restrictive bounds from both layers.

        Args:
            other: Another EchoLayer to combine with.
        """

class PingData:
    """
    Wrapper for accessing per-ping data from an EchogramBuilder.

    Provides convenient access to water column data and layer extractions
    for a specific ping.

    Attributes:
        echodata: Reference to the parent EchogramBuilder.
        nr: Ping index.
    """

    def __init__(self, echodata: EchogramBuilder, nr: int):
        """
        Initialize PingData for a specific ping.

        Args:
            echodata: Parent EchogramBuilder instance.
            nr: Ping index.
        """

    def get_wci(self) -> numpy.ndarray:
        """Get water column image data for this ping."""

    def get_wci_layers(self) -> dict[str, numpy.ndarray]:
        """Get water column data split by layers."""

    def get_extent_layers(self, axis_name: Union[str, None] = None) -> dict[str, tuple[float, float]]:
        """Get layer extents in specified coordinate system."""

    def get_limits_layers(self, axis_name: Union[str, None] = None) -> dict[str, tuple[float, float]]:
        """Get layer limits in specified coordinate system."""

    def get_ping_time(self) -> float:
        """Get ping timestamp."""

    def get_datetime(self) -> datetime.datetime:
        """Get ping datetime."""
