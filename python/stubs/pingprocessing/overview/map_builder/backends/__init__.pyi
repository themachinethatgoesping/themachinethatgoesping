"""MapDataBackend implementations for various geospatial data sources."""

from themachinethatgoesping.pingprocessing.overview.map_builder.backends import (
    base as base,
    geotiff_backend as geotiff_backend
)
from themachinethatgoesping.pingprocessing.overview.map_builder.backends.base import (
    MapDataBackend as MapDataBackend
)
from themachinethatgoesping.pingprocessing.overview.map_builder.backends.geotiff_backend import (
    GeoTiffBackend as GeoTiffBackend
)


__all__: list = ['MapDataBackend', 'GeoTiffBackend']
