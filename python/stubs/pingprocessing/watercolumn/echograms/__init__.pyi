from . import (
    backends as backends,
    coordinate_system as coordinate_system,
    echodata as echodata,
    echogrambuilder as echogrambuilder,
    echogrambuilder_new as echogrambuilder_new,
    indexers as indexers,
    layers as layers
)
from .backends.base import EchogramDataBackend as EchogramDataBackend
from .backends.ping_backend import PingDataBackend as PingDataBackend
from .backends.zarr_backend import ZarrDataBackend as ZarrDataBackend
from .coordinate_system import (
    EchogramCoordinateSystem as EchogramCoordinateSystem
)
from .echodata import EchoData as EchoData
from .echogrambuilder import EchogramBuilder as EchogramBuilder
from .echogrambuilder_new import (
    EchogramBuilder as EchogramBuilderNew
)
from .indexers import EchogramImageRequest as EchogramImageRequest


def is_new_builder(echogram) -> bool:
    """
    Check if an echogram instance is the new EchogramBuilderNew with LayerManager.

    Args:
        echogram: An EchogramBuilder or EchogramBuilderNew instance.

    Returns:
        True if using EchogramBuilderNew (with LayerManager), False otherwise.
    """

def is_refactored_builder(echogram) -> bool:
    """
    Check if an echogram instance uses the refactored builder with separate coordinate system.

    Args:
        echogram: An EchogramBuilder instance.

    Returns:
        True if using EchogramBuilderRefactored (with separate coord_system), False otherwise.
    """

def has_layers(echogram) -> bool:
    """
    Check if an echogram has any layers (works with both builder types).

    Args:
        echogram: An EchogramBuilder or EchogramBuilderNew instance.

    Returns:
        True if there are named layers or a main layer.
    """
