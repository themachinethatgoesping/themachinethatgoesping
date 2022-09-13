from __future__ import annotations
import themachinethatgoesping.gridding.echogrid
import typing
from themachinethatgoesping.gridding.forwardgridder import ForwardGridder
from collections.abc import MutableMapping
import _abc
import collections.abc
import numba.core.registry
import numpy
import themachinethatgoesping.gridding.functions.gridfunctions
import warnings
_Shape = typing.Tuple[int, ...]

__all__ = [
    "EchoGrid",
    "EchoGridDict",
    "ForwardGridder",
    "MutableMapping",
    "gf",
    "njit",
    "np",
    "static_get_target_pos",
    "warnings"
]


class EchoGrid():
    pass
class EchoGridDict(collections.abc.MutableMapping, collections.abc.Mapping, collections.abc.Collection, collections.abc.Sized, collections.abc.Iterable, collections.abc.Container):
    __abstractmethods__: frozenset # value = frozenset()
    _abc_impl: _abc._abc_data
    pass
static_get_target_pos: numba.core.registry.CPUDispatcher # value = CPUDispatcher(<function static_get_target_pos>)
