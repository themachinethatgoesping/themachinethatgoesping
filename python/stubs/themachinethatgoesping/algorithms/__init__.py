"""
Python module process ping data, e.g. apply absorption, spreading loss, compute range/depth, raytrace ...
"""
from __future__ import annotations
from . import amplitudecorrection
from . import geoprocessing
from . import gridding
from . import imageprocessing
from . import pointprocessing
from . import signalprocessing
__all__ = ['amplitudecorrection', 'geoprocessing', 'gridding', 'imageprocessing', 'ostream_redirect', 'pointprocessing', 'signalprocessing']
class ostream_redirect:
    def __enter__(self) -> None:
        ...
    def __exit__(self, *args) -> None:
        ...
    def __init__(self, stdout: bool = True, stderr: bool = True) -> None:
        ...
__version__: str = '0.9.3'
