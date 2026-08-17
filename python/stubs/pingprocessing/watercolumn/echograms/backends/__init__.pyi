"""Echogram data backends for different data sources."""

from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends import (
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
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.base import (
    EchogramDataBackend as EchogramDataBackend
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.combine_backend import (
    CombineBackend as CombineBackend
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.concat_backend import (
    ConcatBackend as ConcatBackend
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.gridded_mmap_backend import (
    GriddedMmapBackend as GriddedMmapBackend
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.image_backend import (
    ImageBackend as ImageBackend
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.mmap_backend import (
    MmapDataBackend as MmapDataBackend
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.ping_backend import (
    PingDataBackend as PingDataBackend
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.storage_mode import (
    ResolutionStrategy as ResolutionStrategy,
    StorageAxisMode as StorageAxisMode,
    XAxisType as XAxisType,
    YAxisType as YAxisType,
    compute_resolution_from_backends as compute_resolution_from_backends
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.backends.zarr_backend import (
    ZarrDataBackend as ZarrDataBackend
)


AVERAGING_MODES: dict = ...

COMBINE_FUNCTIONS: dict = ...

__all__: list = ['EchogramDataBackend', 'PingDataBackend', 'ZarrDataBackend', 'MmapDataBackend', 'GriddedMmapBackend', 'AVERAGING_MODES', 'ConcatBackend', 'CombineBackend', 'COMBINE_FUNCTIONS', 'ImageBackend', 'StorageAxisMode', 'XAxisType', 'YAxisType', 'ResolutionStrategy', 'compute_resolution_from_backends']
