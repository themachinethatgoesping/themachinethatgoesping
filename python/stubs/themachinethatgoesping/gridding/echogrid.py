from __future__ import annotations
import collections.abc
from collections.abc import MutableMapping
from numba.core.decorators import njit
import numpy as np
from themachinethatgoesping.gridding.forwardgridder import ForwardGridder
from themachinethatgoesping.gridding.functions import gridfunctions as gf
import typing
import warnings as warnings
__all__ = ['EchoGrid', 'EchoGridDict', 'ForwardGridder', 'MutableMapping', 'gf', 'njit', 'np', 'static_get_target_pos', 'warnings']
class EchoGrid:
    __firstlineno__: typing.ClassVar[int] = 47
    __static_attributes__: typing.ClassVar[tuple] = ('ExtentX', 'ExtentY', 'ExtentZ', 'ImageAvg', 'ImageNums', 'ImageSums', 'MaxX', 'MaxY', 'MaxZ', 'MinX', 'MinY', 'MinZ', 'ResX', 'ResY', 'ResZ', 'TotalValue', 'TotalValueLayer', 'ZDiff')
    @classmethod
    def from_data(cls, res, sx, sy, sz, sv, blockmean = False):
        ...
    def __init__(self, imagesums, imagenums, gridder):
        ...
    def cutDepthLayer(self, layer_z, layer_size):
        ...
    def getDepthMeanImage(self, layer_z, layer_size):
        ...
    def getGridExtents(self):
        ...
    def getGridder(self):
        ...
    def getTotalvalue(self, min_val):
        ...
    def getTotalvalueLayer(self, min_val):
        ...
    def get_3DImage(self, toDb = True, minDbVal = -50):
        ...
    def get_target_pos(self, min_val = ...):
        ...
    def plot(self, figure, targets_color = None, target_size = 1, show_wci = True, show_echo = True, show_map = True, show_colorbar = True, toDb = True, minDbVal = -50, minDbReplace = None, xindex = None, yindex = None, zindex = None, zindeces = None, kwargs = None, colorbar_kwargs = None):
        ...
    def print(self, methodName, minMethodNameSize, TrueValue):
        ...
    def toString(self, TrueValue, methodName = None, minMethodNameSize = None):
        ...
class EchoGridDict(collections.abc.MutableMapping):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    __firstlineno__: typing.ClassVar[int] = 429
    __static_attributes__: typing.ClassVar[tuple] = ('store')
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __delitem__(self, key):
        ...
    def __getitem__(self, key):
        ...
    def __init__(self, *args, **kwargs):
        ...
    def __iter__(self):
        ...
    def __len__(self):
        ...
    def __setitem__(self, key, value):
        ...
    def cutDepthLayer(self, layer_z, layer_size):
        ...
    def print(self, TrueValue):
        ...
def static_get_target_pos(*args, **kwargs):
    ...
