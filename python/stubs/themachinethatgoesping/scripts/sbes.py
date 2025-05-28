from __future__ import annotations
from copy import deepcopy
from math import radians
from math import tan
from matplotlib import pyplot as plt
from themachinethatgoesping.scripts.oceanographic import knots_to_ms
from themachinethatgoesping.scripts.plot_tools import prepare_plt
import typing
__all__ = ['SBES', 'deepcopy', 'knots_to_ms', 'plt', 'prepare_plt', 'radians', 'tan']
class SBES:
    plt_aspect: typing.ClassVar[bool] = False
    plt_grid: typing.ClassVar[bool] = True
    plt_title: typing.ClassVar[str] = 'SBES overlap'
    plt_xlabel: typing.ClassVar[str] = 'Alongtrack (m)'
    plt_ylabel: typing.ClassVar[str] = 'Depth (m)'
    @staticmethod
    def calc_pingdistance(speed, pingrate):
        ...
    @staticmethod
    def show():
        ...
    def __init__(self, beamopening_angle, x = 0, z = 0):
        ...
    def calc_footprint(self, depth: float, beamopening_angle: float = None) -> float:
        """
        
        
        :rtype: float
        """
    def calc_overlap_depth(self, delta_x):
        ...
    def calc_overlap_depth_for_pingrate(self, speed, pingrate):
        ...
    def calc_overlap_pingrate(self, speed: float, depth: float, beamopening_angle: float = None) -> float:
        ...
    def get_beam_limits(self, depth: float) -> tuple:
        ...
    def get_beam_xmax(self, depth: float) -> float:
        ...
    def get_beam_xmin(self, depth: float) -> float:
        ...
    def get_horizontal_line(self, depth: float) -> tuple:
        ...
    def make_figure(self, title = None, xlabel = None, ylabel = None, aspect = None, grid = None):
        ...
    def plot(self, depth, color, aspect = True, add_bottom = True, axes = None):
        ...
    def plot_pingoverlap_at_overlapdepth(self, depth, speed, overlapdepth, color1 = 'r', color2 = 'b', print_vars = True, add_bottom = True, axes = None, make_figure = True):
        ...
    def plot_pingoverlap_at_pingrate(self, depth, speed, pingrate, color1 = 'r', color2 = 'b', print_vars = True, add_bottom = True, axes = None, make_figure = True):
        ...
