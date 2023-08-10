"""Python module process ping data, e.g. apply absorption, spreading loss, compute range/depth, raytrace ..."""
from __future__ import annotations
import themachinethatgoesping.algorithms
import typing

__all__ = [
    "geoprocessing",
    "ostream_redirect"
]


class ostream_redirect():
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...
    def __init__(self, stdout: bool = True, stderr: bool = True) -> None: ...
    pass
__version__ = '0.1.1'
