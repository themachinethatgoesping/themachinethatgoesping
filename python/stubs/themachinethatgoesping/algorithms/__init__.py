"""
Python module process ping data, e.g. apply absorption, spreading loss, compute range/depth, raytrace ...
"""
from __future__ import annotations
from . import geoprocessing
__all__ = ['geoprocessing', 'ostream_redirect']
class ostream_redirect:
    def __enter__(self) -> None:
        ...
    def __exit__(self, *args) -> None:
        ...
    def __init__(self, stdout: bool = ..., stderr: bool = ...) -> None:
        ...
__version__: str = '0.4.0'
