"""
Backend for pre-built echogram images with extent metadata.

Wraps a 2D numpy array (in-memory or memory-mapped) together with
matplotlib-style extent metadata so it can be used as an EchogramBuilder
backend.  This replaces the old ``EchoData`` helper.

Typical usage::

    # In-memory
    backend = ImageBackend.from_image(image, ping_times, y_min, y_max,
                                      y_axis="depth")

    # Memory-mapped file
    backend = ImageBackend.from_mmap(path, ping_times, y_min, y_max,
                                     y_axis="range")

    builder = EchogramBuilder.from_backend(backend)
"""

import np
import numpy

import themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base import (
    EchogramDataBackend as EchogramDataBackend
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.storage_mode import (
    StorageAxisMode as StorageAxisMode
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.indexers import (
    EchogramImageRequest as EchogramImageRequest
)


class ImageBackend(themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base.EchogramDataBackend):
    """
    Backend for a pre-built 2D echogram image with uniform y-axis.

    The image has shape ``(n_pings, n_samples)`` and a regular y-axis
    grid defined by per-ping ``(y_min, y_max)`` arrays (range or depth
    in metres, or plain sample numbers).

    Supports both in-memory ``ndarray`` and on-disk ``memmap`` arrays.
    """

    def __init__(self, image: np.ndarray, ping_times: np.ndarray, y_min: np.ndarray, y_max: np.ndarray, *, y_axis: str = 'range', wci_value: str = 'sv', linear_mean: bool = True, latitudes: Optional[np.ndarray] = None, longitudes: Optional[np.ndarray] = None, ping_params: Optional[Dict[str, Tuple[str, Tuple[np.ndarray, np.ndarray]]]] = None):
        """
        Initialise the backend.

        Prefer the factory methods ``from_image`` / ``from_mmap``.

        Parameters
        ----------
        image : ndarray or memmap, shape (n_pings, n_samples)
            Echogram data.  May be float32/float64.
        ping_times : ndarray, shape (n_pings,)
            Unix timestamps per ping.
        y_min, y_max : ndarray, shape (n_pings,)
            Y-axis (range/depth) extents per ping.  Scalars are broadcast.
        y_axis : str
            One of ``"range"``, ``"depth"``, ``"sample_index"``.
        wci_value : str
            Label for the stored quantity (e.g. ``"sv"``).
        linear_mean : bool
            Whether beam averaging was done in linear domain.
        latitudes, longitudes : ndarray, optional
            Per-ping coordinates.
        ping_params : dict, optional
            Pre-computed ping parameters, same format as other backends:
            ``{name: (y_reference, (timestamps, values))}``.
        """

    @classmethod
    def from_image(cls, image: np.ndarray, ping_times: np.ndarray, y_min: Union[float, np.ndarray], y_max: Union[float, np.ndarray], *, y_axis: str = 'range', wci_value: str = 'sv', linear_mean: bool = True, latitudes: Optional[np.ndarray] = None, longitudes: Optional[np.ndarray] = None, ping_params: Optional[Dict] = None) -> 'ImageBackend':
        """
        Create a backend from an in-memory numpy array.

        Parameters
        ----------
        image : ndarray (n_pings, n_samples)
            Echogram image data.
        ping_times : ndarray (n_pings,)
            Unix timestamps.
        y_min, y_max : float or ndarray (n_pings,)
            Per-ping y-axis extents.  Scalars are broadcast.
        y_axis : str
            ``"range"``, ``"depth"`` or ``"sample_index"``.
        wci_value, linear_mean, latitudes, longitudes, ping_params
            See ``__init__``.
        """

    @classmethod
    def from_mmap(cls, path: Union[str, Path], ping_times: np.ndarray, y_min: Union[float, np.ndarray], y_max: Union[float, np.ndarray], *, shape: Optional[Tuple[int, int]] = None, dtype: np.dtype = numpy.float32, y_axis: str = 'range', wci_value: str = 'sv', linear_mean: bool = True, latitudes: Optional[np.ndarray] = None, longitudes: Optional[np.ndarray] = None, ping_params: Optional[Dict] = None) -> 'ImageBackend':
        """
        Create a backend from a memory-mapped binary file.

        Parameters
        ----------
        path : str or Path
            Path to the raw binary file (flat float32 by default).
        ping_times : ndarray (n_pings,)
            Unix timestamps.
        y_min, y_max : float or ndarray
            Per-ping y-axis extents.
        shape : (n_pings, n_samples), optional
            If *None*, inferred from ``len(ping_times)`` and file size.
        dtype : numpy dtype
            Element type of the binary file (default ``float32``).
        y_axis, wci_value, linear_mean, latitudes, longitudes, ping_params
            See ``__init__``.
        """

    @property
    def n_pings(self) -> int: ...

    @property
    def ping_times(self) -> np.ndarray: ...

    @property
    def max_sample_counts(self) -> np.ndarray: ...

    @property
    def sample_nr_extents(self) -> Tuple[np.ndarray, np.ndarray]: ...

    @property
    def range_extents(self) -> Optional[Tuple[np.ndarray, np.ndarray]]: ...

    @property
    def depth_extents(self) -> Optional[Tuple[np.ndarray, np.ndarray]]: ...

    @property
    def has_navigation(self) -> bool: ...

    @property
    def latitudes(self) -> Optional[np.ndarray]: ...

    @property
    def longitudes(self) -> Optional[np.ndarray]: ...

    @property
    def wci_value(self) -> str: ...

    @property
    def linear_mean(self) -> bool: ...

    @property
    def storage_mode(self) -> StorageAxisMode: ...

    def get_ping_params(self) -> Dict[str, Tuple[str, Tuple[np.ndarray, np.ndarray]]]: ...

    def get_ping_metainfo(self) -> Dict[str, Tuple[str, Tuple[np.ndarray, np.ndarray]]]:
        """Per-ping metadata. ImageBackend does not provide metainfo."""

    def get_column(self, ping_index: int) -> np.ndarray: ...

    def get_raw_column(self, ping_index: int) -> np.ndarray: ...

    def get_chunk(self, start_ping: int, end_ping: int) -> np.ndarray: ...

    def get_image(self, request: EchogramImageRequest) -> np.ndarray: ...

    def __repr__(self) -> str: ...

    __abstractmethods__: frozenset = ...
