"""
M that holds functions used for amplitude corrections
"""
from __future__ import annotations
import numpy
import typing
__all__ = ['segment_in_weighted_quantiles', 'weighted_median']
@typing.overload
def segment_in_weighted_quantiles(values: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float32], n_quantiles: int, return_empty_segments: bool = False) -> list[numpy.ndarray[numpy.uint64]]:
    ...
@typing.overload
def segment_in_weighted_quantiles(values: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float64], n_quantiles: int, return_empty_segments: bool = False) -> list[numpy.ndarray[numpy.uint64]]:
    ...
@typing.overload
def segment_in_weighted_quantiles(values: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float64], n_quantiles: int, return_empty_segments: bool = False) -> list[numpy.ndarray[numpy.uint64]]:
    ...
@typing.overload
def segment_in_weighted_quantiles(values: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float32], n_quantiles: int, return_empty_segments: bool = False) -> list[numpy.ndarray[numpy.uint64]]:
    ...
@typing.overload
def weighted_median(values: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float32]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.
    
    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight. Note: Edge case with
    inbalanced partial weights is handled by returning the weighted mean
    of the two closest values.
    
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
def weighted_median(values: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float32]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.
    
    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight. Note: Edge case with
    inbalanced partial weights is handled by returning the weighted mean
    of the two closest values.
    
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
def weighted_median(values: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float64]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.
    
    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight. Note: Edge case with
    inbalanced partial weights is handled by returning the weighted mean
    of the two closest values.
    
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
def weighted_median(values: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float64]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.
    
    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight. Note: Edge case with
    inbalanced partial weights is handled by returning the weighted mean
    of the two closest values.
    
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
def weighted_median(values: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float64]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.
    
    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight. Note: Edge case with
    inbalanced partial weights is handled by returning the weighted mean
    of the two closest values.
    
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
def weighted_median(values: numpy.ndarray[numpy.float32], weights: numpy.ndarray[numpy.float64]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.
    
    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight. Note: Edge case with
    inbalanced partial weights is handled by returning the weighted mean
    of the two closest values.
    
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
def weighted_median(values: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float32]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.
    
    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight. Note: Edge case with
    inbalanced partial weights is handled by returning the weighted mean
    of the two closest values.
    
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
@typing.overload
def weighted_median(values: numpy.ndarray[numpy.float64], weights: numpy.ndarray[numpy.float32]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.
    
    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight. Note: Edge case with
    inbalanced partial weights is handled by returning the weighted mean
    of the two closest values.
    
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
