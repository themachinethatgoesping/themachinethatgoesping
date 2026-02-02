"""
Builder for echogram images with coordinate system and layer management.

This module provides the EchogramBuilder class which handles:
- Image building from data backends
- Layer management for region selection
- Coordinate system delegation to EchogramCoordinateSystem
"""

from typing import Union

import numpy

import themachinethatgoesping.echosounders as echosounders
from themachinethatgoesping.pingprocessing.core.progress import (
    get_progress_iterator as get_progress_iterator
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base import (
    EchogramDataBackend as EchogramDataBackend
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.ping_backend import (
    PingDataBackend as PingDataBackend
)
import themachinethatgoesping.pingprocessing.watercolumn.echograms.coordinate_system
from themachinethatgoesping.pingprocessing.watercolumn.echograms.coordinate_system import (
    EchogramCoordinateSystem as EchogramCoordinateSystem
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.layers.echolayer import (
    EchoLayer as EchoLayer,
    PingData as PingData
)


class EchogramBuilder:
    """
    Builder for echogram images with coordinate system and layer management.

    The EchogramBuilder controls:
    - Image building using data from a backend
    - Layer management for region selection

    Coordinate systems are delegated to an EchogramCoordinateSystem instance.
    Data access is delegated to an EchogramDataBackend.
    """

    def __init__(self, backend: EchogramDataBackend, ping_numbers: Union[numpy.ndarray, None] = None):
        """
        Initialize EchogramBuilder with a data backend.

        Args:
            backend: Data backend providing access to echogram data.
            ping_numbers: Optional array of ping numbers. If None, uses 0..n_pings-1.
        """

    @classmethod
    def from_pings(cls, pings, pss=None, wci_value: str = 'sv/av/pv/rv', linear_mean: bool = True, no_navigation: bool = False, apply_pss_to_bottom: bool = False, force_angle: Union[float, None] = None, depth_stack: bool = False, verbose: bool = True, mp_cores: int = 1) -> EchogramBuilder:
        """
        Create an EchogramBuilder from a list of pings.

        Args:
            pings: List of ping objects.
            pss: PingSampleSelector for beam/sample selection. If None, uses default.
            wci_value: Water column image value type (e.g., 'sv', 'av', 'sv/av/pv/rv').
            linear_mean: Whether to use linear mean for beam averaging.
            no_navigation: If True, skip depth calculations.
            apply_pss_to_bottom: Whether to apply PSS to bottom detection.
            force_angle: Force a specific angle for depth projection (degrees).
            depth_stack: If True, use depth stacking mode (requires navigation).
            verbose: Whether to show progress bar.
            mp_cores: Number of cores for parallel processing.

        Returns:
            EchogramBuilder instance.
        """

    @classmethod
    def from_backend(cls, backend: EchogramDataBackend) -> EchogramBuilder:
        """
        Create an EchogramBuilder from an existing backend.

        Args:
            backend: Data backend instance.

        Returns:
            EchogramBuilder instance.
        """

    @classmethod
    def from_pings_dict(cls, pings_dict: dict, progress: bool = True, **kwargs) -> dict:
        """
        Create multiple EchogramBuilders from a dictionary of ping lists.

        Convenience method for creating multiple echograms at once, e.g., from
        pings grouped by frequency or channel.

        Args:
            pings_dict: Dictionary mapping keys (e.g., frequency) to ping lists.
            progress: Show progress bar for each echogram. Default True.
            **kwargs: Additional arguments passed to from_pings() for each echogram.
                Common kwargs: pss, wci_value, linear_mean, depth_stack, mp_cores.

        Returns:
            Dictionary mapping the same keys to EchogramBuilder instances.

        Examples:
            >>> pings_by_freq = {18000: pings_18k, 38000: pings_38k, 120000: pings_120k}
            >>> echograms = EchogramBuilder.from_pings_dict(
            ...     pings_by_freq,
            ...     pss=pss,
            ...     depth_stack=True,
            ...     progress=True
            ... )
            >>> # echograms = {18000: EchogramBuilder, 38000: EchogramBuilder, ...}
            >>> 
            >>> # Access individual echograms
            >>> echogram_38k = echograms[38000]
        """

    @classmethod
    def concat(cls, builders_or_backends: list, gap_handling: str = 'preserve') -> EchogramBuilder:
        """
        Concatenate multiple echograms along the time/ping axis.

        Creates a virtual echogram that spans all input echograms. Data is
        loaded lazily from the original backends as needed.

        Args:
            builders_or_backends: List of EchogramBuilder or EchogramDataBackend instances.
                Must be in temporal order.
            gap_handling: How to handle gaps between echograms:
                - "preserve": Keep real time gaps (x-axis shows true times)
                - "continuous": Virtual continuous (ignore gaps between files)

        Returns:
            EchogramBuilder with ConcatBackend.

        Examples:
            >>> # Concatenate echograms from multiple files
            >>> echograms = [EchogramBuilder.from_zarr(f) for f in file_list]
            >>> combined = EchogramBuilder.concat(echograms)
            >>> 
            >>> # Build full timeline image
            >>> image, extent = combined.build_image()
        """

    @classmethod
    def combine(cls, builders_or_backends, combine_func: str = 'nanmean', name: str = 'combined', linear: bool = True) -> EchogramBuilder:
        """
        Combine multiple echograms with a mathematical operation.

        Creates a virtual echogram that combines all input echograms using
        the specified function (mean, median, sum, etc.). Useful for combining
        different frequencies or averaging multiple acquisitions.

        Combination happens AFTER downsampling for efficiency - each backend
        produces its downsampled image, then they are combined.

        The view settings (x_axis, y_axis) from the first EchogramBuilder are
        preserved in the combined result.

        Args:
            builders_or_backends: List or dict of EchogramBuilder or EchogramDataBackend
                instances. If a dict, uses dict.values(). Should have overlapping 
                time ranges.
            combine_func: Function to combine images, either:
                - String name: "nanmean", "nanmedian", "nansum", "nanmax", 
                  "nanmin", "nanstd", "mean", "first_valid"
                - Callable with signature (stack, axis) -> result
                  Stack has shape (n_backends, nx, ny), reduce along axis=0.
            name: Name for the combined echogram.
            linear: If True (default), convert dB data to linear domain before
                combining, then convert back to dB. This gives acoustically
                correct averaging of intensities. Set to False to combine
                directly in dB domain.

        Returns:
            EchogramBuilder with CombineBackend.

        Examples:
            >>> # Combine different frequencies with mean (linear domain)
            >>> echograms = {18000: echo_18k, 38000: echo_38k, 120000: echo_120k}
            >>> combined = EchogramBuilder.combine(echograms)  # dict works directly
            >>> 
            >>> # Use median instead of mean
            >>> combined = EchogramBuilder.combine(echograms, combine_func="nanmedian")
            >>> 
            >>> # Combine directly in dB domain (not acoustically correct)
            >>> combined = EchogramBuilder.combine(echograms, linear=False)
            >>> 
            >>> # Custom RMS combination
            >>> def rms(stack, axis):
            ...     return np.sqrt(np.nanmean(stack**2, axis=axis))
            >>> combined = EchogramBuilder.combine(echograms, combine_func=rms, linear=False)
        """

    @property
    def coord_system(self) -> themachinethatgoesping.pingprocessing.watercolumn.echograms.coordinate_system.EchogramCoordinateSystem:
        """
        Access the coordinate system.

        All coordinate-related properties are available through this object:
        - x_axis_name, y_axis_name: Current axis names
        - x_extent, y_extent: Data extents
        - y_coordinates, y_resolution, y_gridder: Y-axis grid info
        - feature_mapper: X-axis mapping
        - ping_times, ping_numbers: Ping information
        - time_zone: Timezone for datetime conversions
        - max_number_of_samples: Per-ping sample counts
        - has_depths, has_ranges, has_sample_nrs: Available coordinate types
        - Various interpolators for coordinate transformations
        """

    @property
    def backend(self) -> EchogramDataBackend:
        """Access the data backend."""

    @property
    def pings(self):
        """
        Direct access to pings (for backward compatibility).

        Only works with PingDataBackend.
        """

    @property
    def beam_sample_selections(self):
        """
        Direct access to beam sample selections (for backward compatibility).

        Only works with PingDataBackend.
        """

    @property
    def wci_value(self) -> str:
        """Water column image value type from backend."""

    @property
    def linear_mean(self) -> bool:
        """Whether linear mean is used for beam averaging."""

    @property
    def offset(self) -> float:
        """
        Value offset applied to all data.

        This offset is added to all echogram values when building images
        (build_image, build_image_and_layer_image, build_image_and_layer_images)
        and permanently applied when saving (to_mmap, to_zarr).

        Returns:
            Current offset value (default 0.0).
        """

    @offset.setter
    def offset(self, value: float):
        """
        Set the value offset applied to all data.

        Args:
            value: Offset to add to all echogram values (e.g., calibration correction).
        """

    def get_track(self, start_ping: Union[int, None] = None, end_ping: Union[int, None] = None) -> Union[tuple[numpy.ndarray, numpy.ndarray], None]:
        """
        Get the navigation track (latitudes, longitudes) for this echogram.

        Returns the lat/lon coordinates stored in the backend, which represent
        the ship position for each ping.

        Args:
            start_ping: Optional start ping index. Default: 0.
            end_ping: Optional end ping index (exclusive). Default: n_pings.

        Returns:
            Tuple of (latitudes, longitudes) arrays in degrees, or None if
            navigation data is not available.

        Example:
            >>> lats, lons = echogram.get_track()
            >>> # Get track for visible range
            >>> lats_visible, lons_visible = echogram.get_track(100, 500)
        """

    @property
    def has_track(self) -> bool:
        """Check if navigation track data is available."""

    def reinit(self):
        """Reinitialize coordinate systems if needed."""

    def get_x_kwargs(self): ...

    def get_y_kwargs(self): ...

    def set_y_axis_y_indice(self, min_sample_nr=0, max_sample_nr=float('nan'), max_steps=1024, **kwargs):
        """Set Y axis to sample indices."""

    def set_y_axis_depth(self, min_depth=float('nan'), max_depth=float('nan'), max_steps=1024, **kwargs):
        """Set Y axis to depth in meters."""

    def set_y_axis_range(self, min_range=float('nan'), max_range=float('nan'), max_steps=1024, **kwargs):
        """Set Y axis to range in meters."""

    def set_y_axis_sample_nr(self, min_sample_nr=0, max_sample_nr=float('nan'), max_steps=1024, **kwargs):
        """Set Y axis to sample numbers."""

    def set_x_axis_ping_index(self, min_ping_index=0, max_ping_index=float('nan'), max_steps=4096, **kwargs):
        """Set X axis to ping index."""

    def set_x_axis_ping_time(self, min_timestamp=float('nan'), max_timestamp=float('nan'), time_resolution=float('nan'), time_interpolation_limit=float('nan'), max_steps=4096, **kwargs):
        """Set X axis to ping time (Unix timestamp)."""

    def set_x_axis_date_time(self, min_ping_time=float('nan'), max_ping_time=float('nan'), time_resolution=float('nan'), time_interpolation_limit=float('nan'), max_steps=4096, **kwargs):
        """Set X axis to datetime."""

    def copy_xy_axis(self, other: EchogramBuilder):
        """Copy X/Y axis settings to another EchogramBuilder."""

    def set_ping_numbers(self, ping_numbers):
        """Set ping numbers for x-axis indexing."""

    def set_ping_times(self, ping_times, time_zone=...):
        """Set ping times for x-axis time display."""

    def set_range_extent(self, min_ranges, max_ranges):
        """Set range extents."""

    def set_depth_extent(self, min_depths, max_depths):
        """Set depth extents."""

    def set_sample_nr_extent(self, min_sample_nrs, max_sample_nrs):
        """Set sample number extents."""

    def add_ping_param(self, name, x_reference, y_reference, vec_x_val, vec_y_val):
        """Add a ping parameter (e.g., bottom depth, layer boundary)."""

    def get_ping_param(self, name, use_x_coordinates=False):
        """Get a ping parameter's values in current coordinate system."""

    def get_y_indices(self, wci_nr):
        """Get Y indices mapping image coordinates to data indices."""

    def get_x_indices(self):
        """Get X indices mapping image coordinates to ping indices."""

    def get_column(self, nr):
        """Get column data for a ping from backend."""

    def build_image(self, progress=None):
        """
        Build the echogram image.

        Uses the backend's get_image() method with affine indexing for efficiency.
        Backends can override get_image() for vectorized implementations (e.g., Zarr/Dask).

        Args:
            progress: Optional progress bar or None (not currently used).

        Returns:
            Tuple of (image, extent) where image is a 2D numpy array of shape (nx, ny)
            and extent is [x_min, x_max, y_max, y_min].
        """

    def build_image_and_layer_image(self, progress=None):
        """
        Build echogram image and combined layer image.

        Uses fast vectorized get_image() for the main echogram when no main_layer
        is set. Falls back to per-column iteration only for layer processing.

        Returns:
            Tuple of (image, layer_image, extent).
        """

    def build_image_and_layer_images(self, progress=None):
        """
        Build echogram image and individual layer images.

        Uses fast vectorized get_image() for the main echogram when no main_layer
        is set. Falls back to per-column iteration only for layer processing.

        Returns:
            Tuple of (image, layer_images_dict, extent).
        """

    def get_wci_layers(self, nr):
        """Get WCI data split by layers."""

    def get_extent_layers(self, nr, axis_name=None):
        """Get extents for each layer at a given ping."""

    def get_limits_layers(self, nr, axis_name=None):
        """Get limits for each layer at a given ping."""

    __set_layer__ = _set_layer

    def add_layer(self, name, vec_x_val, vec_min_y, vec_max_y):
        """Add a layer with explicit boundaries."""

    def add_layer_from_static_layer(self, name, min_y, max_y):
        """Add a layer with static boundaries."""

    def add_layer_from_ping_param_offsets_absolute(self, name, ping_param_name, offset_0, offset_1):
        """Add a layer based on absolute offsets from a ping parameter."""

    def add_layer_from_ping_param_offsets_relative(self, name, ping_param_name, offset_0, offset_1):
        """Add a layer based on relative offsets from a ping parameter."""

    def remove_layer(self, name):
        """Remove a layer by name."""

    def clear_layers(self):
        """Remove all layers except main."""

    def clear_main_layer(self):
        """Remove the main layer."""

    def iterate_ping_data(self, keep_to_xlimits=True):
        """Iterate over ping data objects."""

    def get_raw_layer_data(self, layer_name, ping_indices=None):
        """
        Get raw (non-downsampled) data for a specific layer.

        Args:
            layer_name: Name of the layer to extract data from.
            ping_indices: Optional list of ping indices. If None, uses visible x range.

        Yields:
            Tuples of (ping_index, raw_data, (sample_start, sample_end)).
        """

    def get_raw_data_at_coordinates(self, x_coord, y_start, y_end):
        """
        Get raw (non-downsampled) data at specific coordinates.

        Args:
            x_coord: X coordinate (ping time, index, or datetime).
            y_start: Start Y coordinate (depth, range, or sample number).
            y_end: End Y coordinate.

        Returns:
            Tuple of (raw_data, (sample_start, sample_end)) or None if not found.
        """

    def to_zarr(self, path: str, mode: str = 'native', chunks: tuple = (64, -1), compressor: str = 'zstd', compression_level: int = 3, progress: bool = True, resolution: float = None, interpolation: str = 'nearest') -> str:
        """
        Export echogram data to a Zarr store for fast lazy loading.

        Reads and writes data in chunks for memory efficiency and speed.
        Each chunk of pings is read, assembled in memory, and written at once.

        Args:
            path: Path for the Zarr store (directory, will be created).
            mode: Storage mode:
                - "native": Store raw sample indices (fastest, smallest overhead)
                - "view": Transform to match current axis settings (depth/range)
            chunks: Chunk sizes as (ping_chunk, sample_chunk). 
                    Use -1 for full dimension. Default (64, -1) = 64 pings per chunk.
            compressor: Compression algorithm ('zstd', 'lz4', 'zlib', 'none').
            compression_level: Compression level (1-22 for zstd, higher = smaller/slower).
            progress: Whether to show progress bar.
            resolution: Y-axis resolution in meters (auto-detected if None).
                        Only used when mode="view" with depth/range axis.
            interpolation: Resampling method ("nearest" or "linear").

        Returns:
            Path to the created Zarr store.

        Examples:
            >>> # Default: store in native sample indices
            >>> builder.to_zarr("output.zarr")
            >>> 
            >>> # First set view to depth mode, then save in those coordinates
            >>> builder.set_y_axis_depth()
            >>> builder.to_zarr("output.zarr", mode="view")
        """

    @classmethod
    def from_zarr(cls, path: str, chunks: dict = None) -> EchogramBuilder:
        """
        Load an EchogramBuilder from a Zarr store.

        The axis type settings (e.g., "Date time", "Depth (m)") are restored
        from the saved metadata, but zoom levels are not preserved.

        Args:
            path: Path to the Zarr store (directory).
            chunks: Optional chunk sizes for Dask loading.

        Returns:
            EchogramBuilder with ZarrDataBackend.
        """

    def to_mmap(self, path: str, mode: str = 'native', progress: bool = True, chunk_mb: float = 10.0, resolution: float = None, interpolation: str = 'nearest') -> str:
        """
        Export echogram data to a memory-mapped store for ultra-fast access.

        Memory-mapped files provide near-instantaneous random access, making
        them ideal for interactive visualization (zooming, panning). Trade-off:
        files are uncompressed and larger than Zarr stores.

        Args:
            path: Path for the mmap store (directory, will be created).
            mode: Storage mode:
                - "native": Store raw sample indices (fastest, smallest overhead)
                - "view": Transform to match current axis settings (depth/range)
            progress: Whether to show progress bar.
            chunk_mb: Chunk size in megabytes for writing (default 10MB).
            resolution: Y-axis resolution in meters (auto-detected if None).
                        Only used when mode="view" with depth/range axis.
            interpolation: Resampling method ("nearest" or "linear").

        Returns:
            Path to the created mmap store.

        Examples:
            >>> # Default: store in native sample indices (fastest)
            >>> builder.to_mmap("output.mmap")
            >>> 
            >>> # First set view to depth mode, then save in those coordinates
            >>> builder.set_y_axis_depth()
            >>> builder.to_mmap("output.mmap", mode="view")
            >>> 
            >>> # Store with specific resolution
            >>> builder.set_y_axis_depth()
            >>> builder.to_mmap("output.mmap", mode="view", resolution=0.1)
        """

    @classmethod
    def from_mmap(cls, path: str) -> EchogramBuilder:
        """
        Load an EchogramBuilder from a mmap store.

        The WCI data is memory-mapped and lazy-loaded:
        - No data loaded into memory until accessed
        - OS page cache handles caching efficiently
        - Supports files larger than available RAM

        The axis type settings (e.g., "Date time", "Depth (m)") are restored
        from the saved metadata, but zoom levels are not preserved.

        Args:
            path: Path to the mmap store (directory).

        Returns:
            EchogramBuilder with MmapDataBackend.
        """
