"""
Backend for concatenating multiple echograms along the time/ping axis.

This backend provides a virtual view over multiple backends, allowing them
to be treated as a single continuous echogram. Useful for combining data
from multiple files or acquisition sessions.
"""

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


class ConcatBackend(themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base.EchogramDataBackend):
    """
    Virtual backend that concatenates multiple backends along X (ping) axis.

    This backend does not store any data itself - it delegates to sub-backends
    and combines their results. It provides:

    - Lazy access: data is only loaded from sub-backends when requested
    - O(log n) lookup for mapping global ping index to sub-backend
    - Efficient image generation that only queries relevant sub-backends
    - Support for both "preserve" (real time gaps) and "continuous" (no gaps) modes

    Example usage:
        >>> backends = [backend1, backend2, backend3]  # From different files
        >>> concat = ConcatBackend(backends)
        >>> builder = EchogramBuilder(concat)
        >>> image, extent = builder.build_image()
    """

    def __init__(self, backends: list[themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base.EchogramDataBackend], gap_handling: str = 'preserve'):
        """
        Initialize ConcatBackend.

        Args:
            backends: List of backends to concatenate, in temporal order.
                      Must have compatible metadata (same wci_value, etc.).
            gap_handling: How to handle gaps between backends:
                - "preserve": Keep real time gaps (x-axis shows true times)
                - "continuous": Virtual continuous (ignore gaps between files)

        Raises:
            ValueError: If backends list is empty or has incompatible metadata.
        """

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
    def gap_handling(self) -> str:
        """Gap handling mode: 'preserve' or 'continuous'."""

    @property
    def num_backends(self) -> int:
        """Number of sub-backends."""

    def get_backend(self, index: int) -> themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base.EchogramDataBackend:
        """Get a specific sub-backend by index."""

    def get_ping_params(self) -> dict[str, tuple[str, tuple[numpy.ndarray, numpy.ndarray]]]: ...

    def get_column(self, ping_index: int) -> numpy.ndarray:
        """
        Get column data for a ping by delegating to the appropriate sub-backend.
        """

    def get_raw_column(self, ping_index: int) -> numpy.ndarray:
        """Get raw column data for a ping."""

    def get_chunk(self, start_ping: int, end_ping: int) -> numpy.ndarray:
        """Get a chunk of WCI data spanning potentially multiple backends."""

    def get_image(self, request: themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers.EchogramImageRequest) -> numpy.ndarray:
        """
        Build image by delegating to sub-backends.

        Efficiently determines which backends have data in the requested range
        and only queries those backends. When in depth mode, computes proper
        affine parameters for each backend.
        """

    def __repr__(self) -> str: ...

    __abstractmethods__: frozenset = ...
