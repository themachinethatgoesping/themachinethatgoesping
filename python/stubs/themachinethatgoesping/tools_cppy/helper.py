"""
Small helper functions
"""
from __future__ import annotations
import numpy
import typing
__all__: list[str] = ['int_as_string_4b', 'int_as_string_8b', 'pytensor_const_load_ref', 'pytensor_load_copy', 'pytensor_load_ref', 'pytensor_loop_ref', 'pytensor_loop_ref2', 'pytensor_make', 'pytensor_make_xtensor', 'pytensor_sum_const_ref', 'pytensor_sum_const_ref2', 'pytensor_sum_const_ref3', 'pytensor_sum_ref', 'pytensor_view_ref', 'string_as_int_4b', 'string_as_int_8b', 'superscript']
def int_as_string_4b(value: typing.SupportsInt) -> str:
    """
    Interprete an integer to a 4 byte string
    """
def int_as_string_8b(value: typing.SupportsInt) -> str:
    """
    Interprete an integer to a 8 byte string
    """
def pytensor_const_load_ref(arg0: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.float64]:
    ...
def pytensor_load_copy(arg0: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.float64]:
    ...
def pytensor_load_ref(arg0: numpy.ndarray[numpy.float64]) -> None:
    ...
def pytensor_loop_ref(arg0: numpy.ndarray[numpy.float64]) -> None:
    ...
def pytensor_loop_ref2(arg0: numpy.ndarray[numpy.float64]) -> None:
    ...
def pytensor_make(arg0: typing.SupportsInt, arg1: typing.SupportsInt) -> numpy.ndarray[numpy.float64]:
    ...
def pytensor_make_xtensor(arg0: typing.SupportsInt, arg1: typing.SupportsInt) -> numpy.ndarray[numpy.float64]:
    ...
def pytensor_sum_const_ref(arg0: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.float64]:
    ...
def pytensor_sum_const_ref2(arg0: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.float64]:
    ...
def pytensor_sum_const_ref3(arg0: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.float64]:
    ...
def pytensor_sum_ref(arg0: numpy.ndarray[numpy.float64]) -> None:
    ...
def pytensor_view_ref(arg0: numpy.ndarray[numpy.float64]) -> None:
    ...
def string_as_int_4b(value: str) -> int:
    """
    Interprete a 4 byte string to an integer
    """
def string_as_int_8b(value: str) -> int:
    """
    Interprete a 8 byte string to an integer
    """
def superscript(exponent: typing.SupportsInt) -> str:
    """
    convert integer number to superscript
    """
