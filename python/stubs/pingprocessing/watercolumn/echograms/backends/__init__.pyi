"""Echogram data backends for different data sources."""

from . import (
    base as base,
    combine_backend as combine_backend,
    concat_backend as concat_backend,
    gridded_mmap_backend as gridded_mmap_backend,
    image_backend as image_backend,
    mmap_backend as mmap_backend,
    ping_backend as ping_backend,
    storage_mode as storage_mode,
    zarr_backend as zarr_backend
)
from .base import EchogramDataBackend as EchogramDataBackend
from .combine_backend import CombineBackend as CombineBackend
from .concat_backend import ConcatBackend as ConcatBackend
from .gridded_mmap_backend import (
    GriddedMmapBackend as GriddedMmapBackend
)
from .image_backend import ImageBackend as ImageBackend
from .mmap_backend import MmapDataBackend as MmapDataBackend
from .ping_backend import PingDataBackend as PingDataBackend
from .storage_mode import (
    ResolutionStrategy as ResolutionStrategy,
    StorageAxisMode as StorageAxisMode,
    XAxisType as XAxisType,
    YAxisType as YAxisType,
    compute_resolution_from_backends as compute_resolution_from_backends
)
from .zarr_backend import ZarrDataBackend as ZarrDataBackend


AVERAGING_MODES: dict = ...

COMBINE_FUNCTIONS: dict = ...

__all__: list = ['EchogramDataBackend', 'PingDataBackend', 'ZarrDataBackend', 'MmapDataBackend', 'GriddedMmapBackend', 'AVERAGING_MODES', 'ConcatBackend', 'CombineBackend', 'COMBINE_FUNCTIONS', 'ImageBackend', 'StorageAxisMode', 'XAxisType', 'YAxisType', 'ResolutionStrategy', 'compute_resolution_from_backends']
