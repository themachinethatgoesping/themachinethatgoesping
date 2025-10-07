"""
Module that holds functions used for image processing functions
"""
from __future__ import annotations
__all__: list[str] = ['UniformAxis', 'backward_map_bilinear', 'backward_map_bilinear_add', 'backward_map_nearest', 'backward_map_nearest_add', 'find_local_maxima', 'find_local_maxima2', 'grow_regions']
class UniformAxis:
    """
    """
    origin: float
    size: int
    spacing: float
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __init__(self, origin: float, spacing: float, size: int) -> None:
        """
        __init__(self, coordinates: numpy.ndarray[dtype=float64, shape=(*), order='A'], tolerance: float = 1e-09) -> None
        __init__(self, coordinates: numpy.ndarray[dtype=float32, shape=(*), order='A'], tolerance: float = 1e-09) -> None
        """
backward_map_bilinear: nanobind.nb_func  # value = <nanobind.nb_func object>
backward_map_bilinear_add: nanobind.nb_func  # value = <nanobind.nb_func object>
backward_map_nearest: nanobind.nb_func  # value = <nanobind.nb_func object>
backward_map_nearest_add: nanobind.nb_func  # value = <nanobind.nb_func object>
find_local_maxima: nanobind.nb_func  # value = <nanobind.nb_func object>
find_local_maxima2: nanobind.nb_func  # value = <nanobind.nb_func object>
grow_regions: nanobind.nb_func  # value = <nanobind.nb_func object>
