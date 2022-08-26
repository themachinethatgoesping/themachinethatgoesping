"""
Simple gridder class that can create quantitative 3D images from x,z,y,val from some custom data.
"""
from __future__ import annotations
import themachinethatgoesping.gridding.forwardgridder
import typing
import numpy
import themachinethatgoesping.gridding.functions.gridfunctions
_Shape = typing.Tuple[int, ...]

__all__ = [
    "ArrayLike",
    "ForwardGridder",
    "grdf",
    "np"
]


class ForwardGridder():
    """
    Simple class to generate 3D grids (images) and interpolate xyz data onto a grid using simple forward mapping algorithms.
        (e.g. block mean, weighted mean interpolation)
        
    """
    pass
ArrayLike: typing._UnionGenericAlias # value = typing.Union[typing.Sequence[typing.Sequence[typing.Sequence[typing.Sequence[typing.Sequence[typing.Any]]]]], numpy.typing._array_like._SupportsArray[numpy.dtype], typing.Sequence[numpy.typing._array_like._SupportsArray[numpy.dtype]], typing.Sequence[typing.Sequence[numpy.typing._array_like._SupportsArray[numpy.dtype]]], typing.Sequence[typing.Sequence[typing.Sequence[numpy.typing._array_like._SupportsArray[numpy.dtype]]]], typing.Sequence[typing.Sequence[typing.Sequence[typing.Sequence[numpy.typing._array_like._SupportsArray[numpy.dtype]]]]], bool, int, float, complex, str, bytes, typing.Sequence[typing.Union[bool, int, float, complex, str, bytes]], typing.Sequence[typing.Sequence[typing.Union[bool, int, float, complex, str, bytes]]], typing.Sequence[typing.Sequence[typing.Sequence[typing.Union[bool, int, float, complex, str, bytes]]]], typing.Sequence[typing.Sequence[typing.Sequence[typing.Sequence[typing.Union[bool, int, float, complex, str, bytes]]]]]]
