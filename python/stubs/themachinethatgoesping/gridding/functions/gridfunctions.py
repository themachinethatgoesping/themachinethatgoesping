"""

Helper functions for the gridder class, implemented using numba
"""
from __future__ import annotations
import math as math
from numba.core.decorators import njit
import numpy as np
from themachinethatgoesping.gridding.functions import helperfunctions as hlp
__all__: list[str] = ['get_grd_value', 'get_index', 'get_index_fraction', 'get_index_weights', 'get_minmax', 'get_value', 'grd_block_mean', 'grd_weighted_mean', 'hlp', 'math', 'njit', 'np']
def get_grd_value(*args, **kwargs):
    ...
def get_index(*args, **kwargs):
    ...
def get_index_fraction(*args, **kwargs):
    ...
def get_index_weights(*args, **kwargs):
    """
    
    Return a vector with fraction and weights for the neighboring grid cells.
    """
def get_minmax(*args, **kwargs):
    """
    returns the min/max value of three lists (same size).
    Sometimes faster than separate numpy functions because it only loops once.
    
    Parameters
    ----------
    sx : np.array
        1D array with x positions (same size)
    sy : np.array
        1D array with x positions (same size)
    sz : np.array
        1D array with x positions (same size)
    
    Returns
    -------
    tuple
        with (xmin,xmax,ymin,ymax,zmin,zmax)
    """
def get_value(*args, **kwargs):
    ...
def grd_block_mean(*args, **kwargs):
    ...
def grd_weighted_mean(*args, **kwargs):
    ...
