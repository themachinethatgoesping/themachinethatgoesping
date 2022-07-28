"""
Simple helper functions
"""
from __future__ import annotations
import themachinethatgoesping.gridding.functions.helperfunctions
import typing
import math
import numba.core.registry

__all__ = [
    "MIN_DB_VALUE",
    "M_2_PI",
    "M_PI",
    "M_PI_180",
    "M_PI_2",
    "math",
    "njit",
    "round_int"
]


MIN_DB_VALUE = -50.0
M_2_PI = 6.283185307179586
M_PI = 3.141592653589793
M_PI_180 = 0.017453292519943295
M_PI_2 = 1.5707963267948966
__annotations__: dict # value = {'MIN_DB_VALUE': <class 'float'>}
round_int: numba.core.registry.CPUDispatcher # value = CPUDispatcher(<function round_int>)
