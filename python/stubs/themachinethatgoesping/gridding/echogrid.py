from __future__ import annotations
from collections.abc import MutableMapping
from numba.core.decorators import njit
import numpy as np
from themachinethatgoesping.algorithms.gridding import ForwardGridder3D
from themachinethatgoesping.gridding.functions import gridfunctions as gf
import typing
import warnings as warnings
__all__ = ['EchoGrid', 'ForwardGridder3D', 'MutableMapping', 'gf', 'njit', 'np', 'static_get_target_pos', 'warnings']
class EchoGrid:
    __firstlineno__: typing.ClassVar[int] = 48
    __static_attributes__: typing.ClassVar[tuple] = ('ZDiff', 'extent_x', 'extent_y', 'extent_z', 'image_avg', 'image_nums', 'image_sums', 'max_x', 'max_y', 'max_z', 'min_x', 'min_y', 'min_z', 'res_x', 'res_y', 'res_z', 'total_value', 'total_value_layer')
    @classmethod
    def from_data(cls, res, sx, sy, sz, sv, blockmean = False):
        ...
    def __init__(self, image_sums, image_nums, gridder):
        ...
    def cut_by_layer_extent(self, min_z = None, max_z = None):
        ...
    def cut_by_layer_size(self, layer_z, layer_size):
        ...
    def get_depth_mean_image(self, layer_z, layer_size):
        ...
    def get_grid_extent(self, axis = 'xyz'):
        ...
    def get_gridder(self):
        ...
    def get_image(self, toDb = True, minDbVal = -50):
        ...
    def get_target_pos(self, min_val = ...):
        ...
    def get_total_value(self, min_val):
        ...
    def get_total_value_layer(self, min_val):
        ...
    def plot(self, figure, targets_color = None, target_size = 1, show_wci = True, show_echo = True, show_map = True, show_colorbar = True, toDb = True, minDbVal = -50, minDbReplace = None, xindex = None, yindex = None, zindex = None, zindeces = None, kwargs = None, colorbar_kwargs = None):
        ...
    def print(self, methodName, minMethodNameSize, TrueValue):
        ...
    def to_string(self, TrueValue, methodName = None, minMethodNameSize = None):
        ...
def static_get_target_pos(*args, **kwargs):
    ...
