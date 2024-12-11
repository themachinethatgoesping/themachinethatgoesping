"""

Simple helper functions
"""
from __future__ import annotations
import math as math
from numba.core.decorators import njit
__all__ = ['MIN_DB_VALUE', 'M_2_PI', 'M_PI', 'M_PI_180', 'M_PI_2', 'math', 'njit', 'round_int']
def round_int(*args, **kwargs):
    ...
MIN_DB_VALUE: float = -50.0
M_2_PI: float = 6.283185307179586
M_PI: float = 3.141592653589793
M_PI_180: float = 0.017453292519943295
M_PI_2: float = 1.5707963267948966
