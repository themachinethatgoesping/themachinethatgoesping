"""Backend for reading echogram data from ping objects."""

from typing import List, Tuple, Union

import numpy

from themachinethatgoesping.algorithms_nanopy.geoprocessing.functions import (
    to_raypoints as to_raypoints
)
from themachinethatgoesping.algorithms_nanopy.gridding import (
    ForwardGridder1D as ForwardGridder1D
)
import themachinethatgoesping.echosounders as echosounders
import themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base import (
    EchogramDataBackend as EchogramDataBackend
)
import themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers
from themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers import (
    EchogramImageRequest as EchogramImageRequest
)
import themachinethatgoesping.pingprocessing.watercolumn.helper.make_image_helper as make_image_helper
from themachinethatgoesping.pingprocessing.watercolumn.helper.select_get_wci_image import (
    apply_pss as apply_pss,
    select_get_wci_image as select_get_wci_image
)


class PingDataBackend(themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base.EchogramDataBackend):
    """
    Backend that reads data from echosounders ping objects.

    This backend wraps ping objects and provides access to water column data
    through the EchogramDataBackend interface.
    """

    def __init__(self, pings: List, beam_sample_selections: List, ping_times: numpy.ndarray, wci_value: str, linear_mean: bool, max_sample_counts: numpy.ndarray, sample_nr_extents: tuple[numpy.ndarray, numpy.ndarray], range_extents: Union[tuple[numpy.ndarray, numpy.ndarray], None], depth_extents: Union[tuple[numpy.ndarray, numpy.ndarray], None], ping_params: dict[str, tuple[str, numpy.ndarray]], latitudes: Union[numpy.ndarray, None] = None, longitudes: Union[numpy.ndarray, None] = None, depth_stack: bool = False, mp_cores: int = 1):
        """
        Initialize PingDataBackend.

        Prefer using the `from_pings` factory method instead of this constructor.

        Args:
            pings: List of ping objects.
            beam_sample_selections: List of BeamSampleSelection objects, one per ping.
            ping_times: Array of ping timestamps.
            wci_value: Water column image value type (e.g., 'sv', 'av').
            linear_mean: Whether to use linear mean for beam averaging.
            max_sample_counts: Maximum sample count per ping.
            sample_nr_extents: Tuple of (min_sample_nrs, max_sample_nrs) arrays.
            range_extents: Tuple of (min_ranges, max_ranges) arrays, or None.
            depth_extents: Tuple of (min_depths, max_depths) arrays, or None.
            ping_params: Dictionary of pre-computed ping parameters.
            latitudes: Array of latitudes (degrees) per ping, or None.
            longitudes: Array of longitudes (degrees) per ping, or None.
            depth_stack: If True, use depth stacking mode (requires navigation).
            mp_cores: Number of cores for parallel processing.
        """

    @classmethod
    def from_pings(cls, pings, pss=None, wci_value: str = 'sv/av/pv/rv', linear_mean: bool = True, no_navigation: bool = False, apply_pss_to_bottom: bool = False, force_angle: Union[float, None] = None, depth_stack: bool = False, verbose: bool = True, mp_cores: int = 1) -> PingDataBackend:
        """
        Create a PingDataBackend from a list of pings.

        Args:
            pings: List of ping objects.
            pss: PingSampleSelector for beam/sample selection. If None, uses default.
            wci_value: Water column image value type (e.g., 'sv', 'av', 'sv/av/pv/rv').
            linear_mean: Whether to use linear mean for beam averaging.
            no_navigation: If True, skip depth calculations (useful for data without nav).
            apply_pss_to_bottom: Whether to apply PSS to bottom detection.
            force_angle: Force a specific angle for depth projection (radians).
            depth_stack: If True, use depth stacking mode (requires navigation).
            verbose: Whether to show progress bar.
            mp_cores: Number of cores for parallel processing.

        Returns:
            PingDataBackend instance.
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
    def latitudes(self) -> Union[numpy.ndarray, None]:
        """Latitude for each ping in degrees, or None if not available."""

    @property
    def longitudes(self) -> Union[numpy.ndarray, None]:
        """Longitude for each ping in degrees, or None if not available."""

    @property
    def wci_value(self) -> str: ...

    @property
    def linear_mean(self) -> bool: ...

    def get_ping_params(self) -> dict[str, tuple[str, Tuple]]:
        """
        Return pre-computed ping parameters.

        Returns:
            Dictionary mapping parameter names to (y_reference, (times, values)) tuples.
        """

    def get_column(self, ping_index: int) -> numpy.ndarray:
        """
        Get column data for a ping.

        Returns beam-averaged water column data. If depth_stack mode is enabled,
        the data is transformed via raypoints and re-gridded to depth coordinates
        with the same number of samples.

        Args:
            ping_index: Index of the ping to retrieve.

        Returns:
            1D array of shape (n_samples,) with processed values.
        """

    def get_raw_column(self, ping_index: int) -> numpy.ndarray:
        """
        Get full-resolution beam-averaged column data for a ping.

        Always returns range-stacked data regardless of depth_stack mode.
        """

    def get_beam_sample_selection(self, ping_index: int):
        """Get the beam sample selection for a ping."""

    def get_ping(self, ping_index: int):
        """
        Get the raw ping object at the given index.

        This provides direct access to the underlying ping for advanced use cases
        that need functionality not exposed through the backend interface.
        """

    @property
    def pings(self):
        """Direct access to the ping list (for backward compatibility)."""

    @property
    def beam_sample_selections(self):
        """Direct access to beam sample selections (for backward compatibility)."""

    def get_image(self, request: themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers.EchogramImageRequest) -> numpy.ndarray:
        """
        Build a complete echogram image from a request.

        Loops over x columns using get_column() to build the image.

        Args:
            request: Image request with ping mapping and affine parameters.

        Returns:
            2D array of shape (nx, ny) with echogram data (ping, sample).
        """

    __abstractmethods__: frozenset = ...
