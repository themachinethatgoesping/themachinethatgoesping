"""Module that holds functions used for amplitude corrections"""
import typing

from typing import Annotated, overload

import numpy
from numpy.typing import NDArray


@overload
def weighted_median(values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.

    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight.
    Note: Edge case with inbalanced partial weights is handled by
          returning the weighted mean of the
    two closest values.

    Args:
        values: 1D xtensor of numerical values.
        weights: 1D xtensor of corresponding weights (same shape as
                 values). Weights must be positive!

    Template Args:
        t_xtensor_val: The type of the 1D xtensor for values.
        t_xtensor_weight: The type of the 1D xtensor for weights.

    Returns:
        The weighted median as a single scalar value.
    """

@overload
def weighted_median(values_x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values_y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> typing.Any: ...

@overload
def weighted_median(values_x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values_y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values_z: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> tuple[float, float, float]: ...

@overload
def weighted_median(values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.

    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight.
    Note: Edge case with inbalanced partial weights is handled by
          returning the weighted mean of the
    two closest values.

    Args:
        values: 1D xtensor of numerical values.
        weights: 1D xtensor of corresponding weights (same shape as
                 values). Weights must be positive!

    Template Args:
        t_xtensor_val: The type of the 1D xtensor for values.
        t_xtensor_weight: The type of the 1D xtensor for weights.

    Returns:
        The weighted median as a single scalar value.
    """

@overload
def weighted_median(values_x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values_y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> typing.Any: ...

@overload
def weighted_median(values_x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values_y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values_z: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> tuple[float, float, float]: ...

@overload
def weighted_median(values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.

    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight.
    Note: Edge case with inbalanced partial weights is handled by
          returning the weighted mean of the
    two closest values.

    Args:
        values: 1D xtensor of numerical values.
        weights: 1D xtensor of corresponding weights (same shape as
                 values). Weights must be positive!

    Template Args:
        t_xtensor_val: The type of the 1D xtensor for values.
        t_xtensor_weight: The type of the 1D xtensor for weights.

    Returns:
        The weighted median as a single scalar value.
    """

@overload
def weighted_median(values_x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values_y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> typing.Any: ...

@overload
def weighted_median(values_x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values_y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values_z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> tuple[float, float, float]: ...

@overload
def weighted_median(values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> float:
    """
    Computes the weighted median of a 1D xtensor without using Boost.

    The weighted median is defined as the smallest value for which the
    cumulative weight is >= 50% of the total weight.
    Note: Edge case with inbalanced partial weights is handled by
          returning the weighted mean of the
    two closest values.

    Args:
        values: 1D xtensor of numerical values.
        weights: 1D xtensor of corresponding weights (same shape as
                 values). Weights must be positive!

    Template Args:
        t_xtensor_val: The type of the 1D xtensor for values.
        t_xtensor_weight: The type of the 1D xtensor for weights.

    Returns:
        The weighted median as a single scalar value.
    """

@overload
def weighted_median(values_x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values_y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> typing.Any: ...

@overload
def weighted_median(values_x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values_y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values_z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> tuple[float, float, float]: ...

@overload
def segment_in_weighted_quantiles(values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], n_quantiles: int, return_empty_segments: bool = False) -> list["xt::xarray_container_xt_uvector<unsignedlong_xsimd_aligned_allocator<unsignedlong_16ul >, (xt::layout_type)0, xt::svector_unsignedlong_4ul_std_allocator<unsignedlong, true>, xt::xtensor_expression_tag>"]: ...

@overload
def segment_in_weighted_quantiles(values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], n_quantiles: int, return_empty_segments: bool = False) -> list["xt::xarray_container_xt_uvector<unsignedlong_xsimd_aligned_allocator<unsignedlong_16ul >, (xt::layout_type)0, xt::svector_unsignedlong_4ul_std_allocator<unsignedlong, true>, xt::xtensor_expression_tag>"]: ...

@overload
def segment_in_weighted_quantiles(values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], n_quantiles: int, return_empty_segments: bool = False) -> list["xt::xarray_container_xt_uvector<unsignedlong_xsimd_aligned_allocator<unsignedlong_16ul >, (xt::layout_type)0, xt::svector_unsignedlong_4ul_std_allocator<unsignedlong, true>, xt::xtensor_expression_tag>"]: ...

@overload
def segment_in_weighted_quantiles(values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], n_quantiles: int, return_empty_segments: bool = False) -> list["xt::xarray_container_xt_uvector<unsignedlong_xsimd_aligned_allocator<unsignedlong_16ul >, (xt::layout_type)0, xt::svector_unsignedlong_4ul_std_allocator<unsignedlong, true>, xt::xtensor_expression_tag>"]: ...
