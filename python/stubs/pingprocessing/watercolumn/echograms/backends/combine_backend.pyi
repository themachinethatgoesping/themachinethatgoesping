from collections.abc import Callable as _Callable
from typing import Union

import numpy

import themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base import (
    EchogramDataBackend as EchogramDataBackend
)
import themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.storage_mode
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.storage_mode import (
    StorageAxisMode as StorageAxisMode
)
import themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers
from themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers import (
    EchogramImageRequest as EchogramImageRequest
)


def nanmean(stack: numpy.ndarray, axis: int) -> numpy.ndarray:
    """Mean ignoring NaN values."""

def nanmedian(stack: numpy.ndarray, axis: int) -> numpy.ndarray:
    """Median ignoring NaN values."""

def nansum(stack: numpy.ndarray, axis: int) -> numpy.ndarray:
    """Sum ignoring NaN values."""

def nanmax(stack: numpy.ndarray, axis: int) -> numpy.ndarray:
    """Maximum ignoring NaN values."""

def nanmin(stack: numpy.ndarray, axis: int) -> numpy.ndarray:
    """Minimum ignoring NaN values."""

def nanstd(stack: numpy.ndarray, axis: int) -> numpy.ndarray:
    """Standard deviation ignoring NaN values."""

def mean(stack: numpy.ndarray, axis: int) -> numpy.ndarray:
    """Mean (NaN propagates)."""

def first_valid(stack: numpy.ndarray, axis: int) -> numpy.ndarray:
    """Return first non-NaN value along axis (priority order)."""

COMBINE_FUNCTIONS: dict = ...

class CombineBackend(themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base.EchogramDataBackend):
    """
    Virtual backend that combines multiple backends with a reduce function.

    Combination happens AFTER downsampling for efficiency:
    1. Each sub-backend produces its downsampled image via get_image()
    2. Images are stacked (handling different extents)
    3. combine_func reduces the stack to a single image

    Alignment modes:
    - x_align="ping_index": Backends are aligned by ping index (ping N with ping N)
    - x_align="time": Backends are aligned by timestamp (find closest ping by time)
    - y_align="sample_index": Backends are aligned by sample index
    - y_align="depth": Backends are aligned by depth coordinates

    Linear mode (linear=True):
    - Data is assumed to be in dB (e.g., Sv values)
    - Before combining: converts from dB to linear using 10^(0.1 * dB)
    - Applies combine function (e.g., nanmean) in linear domain
    - After combining: converts back to dB using 10 * log10(linear)
    - This gives physically correct averaging of acoustic intensities

    Memory usage: O(n_backends * nx * ny) - all downsampled images must fit in RAM.
    This is typically fine since downsampled images are small (e.g., 4096 x 1024).

    Example usage:
        >>> backends = [backend_18khz, backend_38khz, backend_120khz]
        >>> combine = CombineBackend(backends, combine_func=np.nanmean)
        >>> builder = EchogramBuilder(combine)
        >>> image, extent = builder.build_image()
        >>>
        >>> # For acoustically correct averaging in linear domain:
        >>> combine = CombineBackend(backends, combine_func="nanmean", linear=True)

    Custom combine functions must have signature:
        func(stack: np.ndarray, axis: int) -> np.ndarray
    where stack has shape (n_backends, nx, ny) and the function reduces along axis=0.
    """

    def __init__(self, backends: list[themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base.EchogramDataBackend], combine_func: Union[str, _Callable[[numpy.ndarray, int], numpy.ndarray]] = 'nanmean', name: str = 'combined', x_align: str = 'ping_index', y_align: str = 'sample_index', linear: bool = True):
        """
        Initialize CombineBackend.

        Args:
            backends: List of backends to combine. Should have overlapping time ranges.
            combine_func: Function to combine stacked images, either:
                - String name of built-in: "nanmean", "nanmedian", "nansum", 
                  "nanmax", "nanmin", "nanstd", "mean", "first_valid"
                - Callable with signature (stack, axis) -> result
                  Stack has shape (n_backends, nx, ny), reduce along axis=0.
            name: Name for the combined echogram (used in repr).
            x_align: How to align backends on x-axis:
                - "ping_index": Align by ping index (ping N with ping N)
                - "time": Align by timestamp (find closest ping by time)
            y_align: How to align backends on y-axis:
                - "sample_index": Align by sample index
                - "depth": Align by depth coordinates (requires depth extents)
                - "range": Align by range coordinates (requires range extents)
            linear: If True (default), convert dB data to linear domain before
                combining, then convert back to dB. This gives acoustically
                correct averaging of intensities. Set to False to combine
                directly in dB domain.

        Raises:
            ValueError: If backends list is empty or invalid align mode.
        """

    @property
    def x_align(self) -> str:
        """X-axis alignment mode."""

    @x_align.setter
    def x_align(self, value: str):
        """Set X-axis alignment mode."""

    @property
    def y_align(self) -> str:
        """Y-axis alignment mode."""

    @y_align.setter
    def y_align(self, value: str):
        """Set Y-axis alignment mode."""

    @property
    def linear(self) -> bool:
        """Whether to combine in linear domain."""

    @linear.setter
    def linear(self, value: bool):
        """Set whether to combine in linear domain."""

    @property
    def n_pings(self) -> int: ...

    @property
    def ping_times(self) -> numpy.ndarray: ...

    @property
    def max_sample_counts(self) -> numpy.ndarray: ...

    @property
    def sample_nr_extents(self) -> tuple[numpy.ndarray, numpy.ndarray]: ...

    @property
    def range_extents(self) -> Union[tuple[numpy.ndarray, numpy.ndarray], None]: ...

    @property
    def depth_extents(self) -> Union[tuple[numpy.ndarray, numpy.ndarray], None]: ...

    @property
    def has_navigation(self) -> bool: ...

    @property
    def latitudes(self) -> Union[numpy.ndarray, None]: ...

    @property
    def longitudes(self) -> Union[numpy.ndarray, None]: ...

    @property
    def wci_value(self) -> str: ...

    @property
    def linear_mean(self) -> bool: ...

    @property
    def storage_mode(self) -> themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.storage_mode.StorageAxisMode:
        """Return storage mode from first backend."""

    @property
    def combine_func_name(self) -> str:
        """Name of the combine function."""

    @property
    def num_backends(self) -> int:
        """Number of sub-backends."""

    def get_backend(self, index: int) -> themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base.EchogramDataBackend:
        """Get a specific sub-backend by index."""

    def get_ping_params(self) -> dict[str, tuple[str, tuple[numpy.ndarray, numpy.ndarray]]]: ...

    def get_column(self, ping_index: int) -> numpy.ndarray:
        """
        Get combined column data for a ping.

        Fetches data from all backends, aligns by sample index, and combines.
        Note: This is slower than get_image() due to per-column overhead.
        For building full images, get_image() is preferred.
        """

    def get_raw_column(self, ping_index: int) -> numpy.ndarray:
        """Get combined raw column data."""

    def get_image(self, request: themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers.EchogramImageRequest) -> numpy.ndarray:
        """
        Build combined image by getting from each backend and combining.

        This is the main entry point for efficient image generation.
        Each backend produces its own downsampled image using its own
        depth-to-sample mapping, then images are stacked and combined.

        IMPORTANT: When combining echograms in depth mode, each backend
        may have different sample-to-depth relationships. This method
        computes the correct affine parameters for each backend.

        IMPORTANT: Backends are aligned by TIME, not by ping index. This is
        critical when combining different frequencies that may have different
        ping rates or timing.

        Handles backends with different coverage (different number of pings)
        by masking out-of-range pings as invalid for each backend.
        """

    def __repr__(self) -> str: ...

    __abstractmethods__: frozenset = ...
