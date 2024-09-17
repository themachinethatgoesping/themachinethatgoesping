"""
Python module process ping data, e.g. apply absorption, spreading loss, compute range/depth, raytrace ...
"""
from __future__ import annotations
from . import geoprocessing
from . import signalprocessing
__all__ = ['geoprocessing', 'ostream_redirect', 'signalprocessing']
class ostream_redirect:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __enter__(self) -> None:
        ...
    def __exit__(self, *args) -> None:
        ...
    def __init__(self, stdout: bool = True, stderr: bool = True) -> None:
        ...
__version__: str = '0.8.1'
