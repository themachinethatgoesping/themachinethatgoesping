"""
M that holds functions used for amplitude corrections
"""
from __future__ import annotations
import numpy
import typing
__all__ = ['find_local_maxima', 'weighted_median']
@typing.overload
def find_local_maxima(data: numpy.ndarray[numpy.float32], threshold: float | None = None, accept_nans: bool = True, mp_cores: int = 1) -> tuple[list[int], list[int], list[int], list[float]]:
    ...
@typing.overload
def find_local_maxima(data: numpy.ndarray[numpy.float32], threshold: float | None = None, accept_nans: bool = True, mp_cores: int = 1) -> tuple[list[int], list[int], list[float]]:
    ...
@typing.overload
def find_local_maxima(data: numpy.ndarray[numpy.float32], threshold: float | None = None, accept_nans: bool = True, mp_cores: int = 1) -> tuple[list[int], list[float]]:
    ...
@typing.overload
def find_local_maxima(data: numpy.ndarray[numpy.float64], threshold: float | None = None, accept_nans: bool = True, mp_cores: int = 1) -> tuple[list[int], list[int], list[int], list[float]]:
    ...
@typing.overload
def find_local_maxima(data: numpy.ndarray[numpy.float64], threshold: float | None = None, accept_nans: bool = True, mp_cores: int = 1) -> tuple[list[int], list[int], list[float]]:
    ...
@typing.overload
def find_local_maxima(data: numpy.ndarray[numpy.float64], threshold: float | None = None, accept_nans: bool = True, mp_cores: int = 1) -> tuple[list[int], list[float]]:
    ...
@typing.overload
def weighted_median(values: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float32]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.
    
    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight.
    
    Template parameter ``t_xtensor_val``:
        The type of the 1D xtensor for values.
    
    Template parameter ``t_xtensor_weight``:
        The type of the 1D xtensor for weights.
    
    Parameter ``values``:
        1D xtensor of numerical values.
    
    Parameter ``weights``:
        1D xtensor of corresponding weights (same shape as values).
        Weights must be positive!
    
    Returns:
        The weighted median as a single scalar value.
    """
@typing.overload
def weighted_median(values_x: numpy.ndarray[numpy.float32], values_y: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float32]) -> tuple[float, float]:
    ...
@typing.overload
def weighted_median(values_x: numpy.ndarray[numpy.float32], values_y: numpy.ndarray[numpy.float32], values_z: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float32]) -> tuple[float, float, float]:
    ...
@typing.overload
def weighted_median(values: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float64]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.
    
    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight.
    
    Template parameter ``t_xtensor_val``:
        The type of the 1D xtensor for values.
    
    Template parameter ``t_xtensor_weight``:
        The type of the 1D xtensor for weights.
    
    Parameter ``values``:
        1D xtensor of numerical values.
    
    Parameter ``weights``:
        1D xtensor of corresponding weights (same shape as values).
        Weights must be positive!
    
    Returns:
        The weighted median as a single scalar value.
    """
@typing.overload
def weighted_median(values_x: numpy.ndarray[numpy.float64], values_y: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float64]) -> tuple[float, float]:
    ...
@typing.overload
def weighted_median(values_x: numpy.ndarray[numpy.float64], values_y: numpy.ndarray[numpy.float64], values_z: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float64]) -> tuple[float, float, float]:
    ...
@typing.overload
def weighted_median(values: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float64]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.
    
    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight.
    
    Template parameter ``t_xtensor_val``:
        The type of the 1D xtensor for values.
    
    Template parameter ``t_xtensor_weight``:
        The type of the 1D xtensor for weights.
    
    Parameter ``values``:
        1D xtensor of numerical values.
    
    Parameter ``weights``:
        1D xtensor of corresponding weights (same shape as values).
        Weights must be positive!
    
    Returns:
        The weighted median as a single scalar value.
    """
@typing.overload
def weighted_median(values_x: numpy.ndarray[numpy.float32], values_y: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float64]) -> tuple[float, float]:
    ...
@typing.overload
def weighted_median(values_x: numpy.ndarray[numpy.float32], values_y: numpy.ndarray[numpy.float32], values_z: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float64]) -> tuple[float, float, float]:
    ...
@typing.overload
def weighted_median(values: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float32]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.
    
    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight.
    
    Template parameter ``t_xtensor_val``:
        The type of the 1D xtensor for values.
    
    Template parameter ``t_xtensor_weight``:
        The type of the 1D xtensor for weights.
    
    Parameter ``values``:
        1D xtensor of numerical values.
    
    Parameter ``weights``:
        1D xtensor of corresponding weights (same shape as values).
        Weights must be positive!
    
    Returns:
        The weighted median as a single scalar value.
    """
@typing.overload
def weighted_median(values_x: numpy.ndarray[numpy.float64], values_y: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float32]) -> tuple[float, float]:
    ...
@typing.overload
def weighted_median(values_x: numpy.ndarray[numpy.float64], values_y: numpy.ndarray[numpy.float64], values_z: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float32]) -> tuple[float, float, float]:
    ...
