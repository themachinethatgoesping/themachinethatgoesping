"""
Coordinate system management for echograms.

This module provides the EchogramCoordinateSystem class which handles all
coordinate transformations between different axis types (ping index, time,
datetime for X; sample index, sample number, depth, range for Y).
"""

from collections.abc import Callable as _Callable
import datetime
from typing import Union

import numpy

import themachinethatgoesping as theping
from themachinethatgoesping.algorithms_nanopy.featuremapping import (
    NearestFeatureMapper as NearestFeatureMapper
)
from themachinethatgoesping.algorithms_nanopy.gridding import (
    ForwardGridder1D as ForwardGridder1D
)
from themachinethatgoesping.pingprocessing.core.asserts import (
    assert_valid_argument as assert_valid_argument
)
import themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers
from themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers import (
    EchogramImageRequest as EchogramImageRequest
)
import themachinethatgoesping.tools as tools


class EchogramCoordinateSystem:
    """
    Manages coordinate systems and transformations for echogram display.

    This class handles:
    - X-axis systems (ping index, ping time, datetime)
    - Y-axis systems (sample index, sample number, depth, range)
    - Interpolators for converting between coordinate systems
    - Extent management (min/max for each axis type)
    - Ping parameters (additional per-ping data like bottom depth)

    The coordinate system is independent of data storage, allowing it to be
    reused across different data sources.
    """

    def __init__(self, n_pings: int, max_number_of_samples: numpy.ndarray, ping_times: numpy.ndarray, ping_numbers: Union[numpy.ndarray, None] = None, time_zone: datetime.timezone = ...):
        """
        Initialize coordinate system.

        Args:
            n_pings: Number of pings.
            max_number_of_samples: Array of max sample counts per ping.
            ping_times: Array of ping timestamps.
            ping_numbers: Optional array of ping numbers. If None, uses 0..n_pings-1.
            time_zone: Timezone for datetime display.
        """

    @property
    def n_pings(self) -> int:
        """Number of pings."""

    @property
    def initialized(self) -> bool:
        """Whether coordinate system is fully initialized."""

    def set_ping_numbers(self, ping_numbers: numpy.ndarray):
        """Set ping numbers for x-axis indexing."""

    def set_ping_times(self, ping_times: numpy.ndarray, time_zone: Union[datetime.timezone, None] = None):
        """Set ping times for x-axis time display."""

    def set_range_extent(self, min_ranges: numpy.ndarray, max_ranges: numpy.ndarray):
        """Set range extents (per-ping min/max range in meters)."""

    def set_depth_extent(self, min_depths: numpy.ndarray, max_depths: numpy.ndarray):
        """Set depth extents (per-ping min/max depth in meters)."""

    def set_sample_nr_extent(self, min_sample_nrs: numpy.ndarray, max_sample_nrs: numpy.ndarray):
        """Set sample number extents (per-ping min/max sample numbers)."""

    def add_ping_param(self, name: str, x_reference: str, y_reference: str, vec_x_val: numpy.ndarray, vec_y_val: numpy.ndarray):
        """
        Add a ping parameter (e.g., bottom depth, layer boundary).

        Args:
            name: Parameter name (e.g., 'bottom', 'minslant').
            x_reference: X reference type ('Ping index', 'Ping time', 'Date time').
            y_reference: Y reference type ('Y indice', 'Sample number', 'Depth (m)', 'Range (m)').
            vec_x_val: X values (timestamps or indices).
            vec_y_val: Y values (depths, ranges, etc.).
        """

    def get_ping_param(self, name: str, use_x_coordinates: bool = False) -> tuple[numpy.ndarray, numpy.ndarray]:
        """
        Get a ping parameter's values in current coordinate system.

        Uses vectorized affine transforms for speed.
        Handles both dense format (one value per ping) and sparse format (control points).

        Args:
            name: Parameter name.
            use_x_coordinates: If True, use current x coordinates instead of all pings.

        Returns:
            Tuple of (x_coordinates, y_values).
        """

    def reinit(self):
        """Reinitialize coordinate systems if needed."""

    def get_x_kwargs(self) -> dict:
        """Get current X-axis configuration."""

    def get_y_kwargs(self) -> dict:
        """Get current Y-axis configuration."""

    def set_y_axis_y_indice(self, min_sample_nr: float = 0, max_sample_nr: float = float('nan'), max_steps: int = 1024, layer_update_callback: Union[_Callable, None] = None, **kwargs):
        """
        Set Y axis to sample indices.

        Args:
            min_sample_nr: Minimum sample index to display.
            max_sample_nr: Maximum sample index to display (nan = auto).
            max_steps: Maximum number of Y pixels.
            layer_update_callback: Callback to update layers after axis change.
        """

    def set_y_axis_depth(self, min_depth: float = float('nan'), max_depth: float = float('nan'), max_steps: int = 1024, layer_update_callback: Union[_Callable, None] = None, **kwargs):
        """
        Set Y axis to depth in meters.

        Args:
            min_depth: Minimum depth to display (nan = auto).
            max_depth: Maximum depth to display (nan = auto).
            max_steps: Maximum number of Y pixels.
            layer_update_callback: Callback to update layers after axis change.
        """

    def set_y_axis_range(self, min_range: float = float('nan'), max_range: float = float('nan'), max_steps: int = 1024, layer_update_callback: Union[_Callable, None] = None, **kwargs):
        """
        Set Y axis to range in meters.

        Args:
            min_range: Minimum range to display (nan = auto).
            max_range: Maximum range to display (nan = auto).
            max_steps: Maximum number of Y pixels.
            layer_update_callback: Callback to update layers after axis change.
        """

    def set_y_axis_sample_nr(self, min_sample_nr: float = 0, max_sample_nr: float = float('nan'), max_steps: int = 1024, layer_update_callback: Union[_Callable, None] = None, **kwargs):
        """
        Set Y axis to sample numbers.

        Args:
            min_sample_nr: Minimum sample number to display.
            max_sample_nr: Maximum sample number to display (nan = auto).
            max_steps: Maximum number of Y pixels.
            layer_update_callback: Callback to update layers after axis change.
        """

    def set_x_axis_ping_index(self, min_ping_index: float = 0, max_ping_index: float = float('nan'), max_steps: int = 4096, **kwargs):
        """
        Set X axis to ping index.

        Args:
            min_ping_index: Minimum ping index to display.
            max_ping_index: Maximum ping index to display (nan = auto).
            max_steps: Maximum number of X pixels.
        """

    def set_x_axis_ping_time(self, min_timestamp: float = float('nan'), max_timestamp: float = float('nan'), time_resolution: float = float('nan'), time_interpolation_limit: float = float('nan'), max_steps: int = 4096, **kwargs):
        """
        Set X axis to ping time (Unix timestamp).

        Args:
            min_timestamp: Minimum timestamp to display (nan = auto).
            max_timestamp: Maximum timestamp to display (nan = auto).
            time_resolution: Time resolution in seconds (nan = auto).
            time_interpolation_limit: Max time gap for interpolation (nan = auto).
            max_steps: Maximum number of X pixels.
        """

    def set_x_axis_date_time(self, min_ping_time: float = float('nan'), max_ping_time: float = float('nan'), time_resolution: float = float('nan'), time_interpolation_limit: float = float('nan'), max_steps: int = 4096, **kwargs):
        """
        Set X axis to datetime.

        Args:
            min_ping_time: Minimum time (timestamp or datetime, nan = auto).
            max_ping_time: Maximum time (timestamp or datetime, nan = auto).
            time_resolution: Time resolution (seconds or timedelta, nan = auto).
            time_interpolation_limit: Max time gap (seconds or timedelta, nan = auto).
            max_steps: Maximum number of X pixels.
        """

    def get_y_indices(self, wci_nr: int) -> tuple[numpy.ndarray, numpy.ndarray]:
        """
        Get Y indices mapping image coordinates to data indices.

        Uses precomputed affine coefficients for speed.

        Args:
            wci_nr: Ping/column number.

        Returns:
            Tuple of (image_indices, data_indices) arrays.
        """

    def get_x_indices(self) -> tuple[numpy.ndarray, numpy.ndarray]:
        """
        Get X indices mapping image coordinates to ping indices.

        Returns:
            Tuple of (image_indices, ping_indices) arrays.
        """

    def copy_xy_axis_to(self, other: EchogramCoordinateSystem):
        """
        Copy X/Y axis settings to another coordinate system.

        Args:
            other: Target coordinate system.
        """

    def make_image_request(self) -> themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers.EchogramImageRequest:
        """
        Create a backend-ready request for building the current image.

        This method generates all the indexing information needed for a backend
        to produce a downsampled (nx, ny) echogram image without needing to
        know about the coordinate system internals.

        The request includes:
        - ping_indexer: which ping to use for each output x column
        - affine params (a, b): for computing sample indices from y coordinates
        - max_sample_indices: for bounds checking

        Returns:
            EchogramImageRequest with all necessary indexing information.
        """

    def make_oversampled_image_request(self, x_oversampling: int = 1, y_oversampling: int = 1) -> EchogramImageRequest:
        """
        Create an oversampled image request for anti-aliased downsampling.

        Generates a request with x_oversampling × y_oversampling more pixels
        than the current coordinate system grid. The oversampled grid spans
        the same physical extent, so block-averaging the result back to the
        original resolution produces anti-aliased output.

        The oversampled Y coordinates are computed by subdividing each original
        Y pixel into y_oversampling sub-pixels. Similarly for X.

        Args:
            x_oversampling: Integer factor for X axis oversampling.
            y_oversampling: Integer factor for Y axis oversampling.

        Returns:
            EchogramImageRequest with oversampled dimensions.
        """
