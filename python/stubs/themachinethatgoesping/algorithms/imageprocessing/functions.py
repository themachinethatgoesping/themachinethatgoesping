"""
M that holds functions used for amplitude corrections
"""
from __future__ import annotations
import numpy
import typing
__all__ = ['find_local_maxima']
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
