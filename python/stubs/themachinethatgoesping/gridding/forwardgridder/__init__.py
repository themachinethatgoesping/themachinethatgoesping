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
ArrayLike: typing._UnionGenericAlias # value = typing.Union[numpy._typing._array_like._SupportsArray[numpy.dtype], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[typing.Union[bool, int, float, complex, str, bytes]]]
