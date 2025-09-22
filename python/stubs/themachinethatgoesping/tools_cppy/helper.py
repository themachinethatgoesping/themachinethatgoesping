"""
Small helper functions
"""
from __future__ import annotations
import typing
__all__: list[str] = ['int_as_string_4b', 'int_as_string_8b', 'string_as_int_4b', 'string_as_int_8b', 'superscript']
def int_as_string_4b(value: typing.SupportsInt) -> str:
    """
    Interprete an integer to a 4 byte string
    """
def int_as_string_8b(value: typing.SupportsInt) -> str:
    """
    Interprete an integer to a 8 byte string
    """
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
