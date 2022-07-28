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
    "ForwardGridder",
    "grdf",
    "np"
]


class ForwardGridder():
    """
    Simple class to generate 3D grids (images) and interpolate xyz data ontothem using simple forwardmapping algorithms.
       (e.g. block mean, weighted mean interpolation)
       
    """
    pass
