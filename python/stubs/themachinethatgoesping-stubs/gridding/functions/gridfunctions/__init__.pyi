"""
Helper functions for the gridder class, implemented using numba
"""
from __future__ import annotations
import themachinethatgoesping.gridding.functions.gridfunctions
import typing
import math
import numba.core.registry
import numpy
import themachinethatgoesping.gridding.functions.helperfunctions
_Shape = typing.Tuple[int, ...]

__all__ = [
    "get_grd_value",
    "get_index",
    "get_index_fraction",
    "get_index_weights",
    "get_minmax",
    "get_value",
    "grd_block_mean",
    "grd_weighted_mean",
    "hlp",
    "math",
    "njit",
    "np"
]


get_grd_value: numba.core.registry.CPUDispatcher # value = CPUDispatcher(<function get_grd_value>)
get_index: numba.core.registry.CPUDispatcher # value = CPUDispatcher(<function get_index>)
get_index_fraction: numba.core.registry.CPUDispatcher # value = CPUDispatcher(<function get_index_fraction>)
get_index_weights: numba.core.registry.CPUDispatcher # value = CPUDispatcher(<function get_index_weights>)
get_minmax: numba.core.registry.CPUDispatcher # value = CPUDispatcher(<function get_minmax>)
get_value: numba.core.registry.CPUDispatcher # value = CPUDispatcher(<function get_value>)
grd_block_mean: numba.core.registry.CPUDispatcher # value = CPUDispatcher(<function grd_block_mean>)
grd_weighted_mean: numba.core.registry.CPUDispatcher # value = CPUDispatcher(<function grd_weighted_mean>)
