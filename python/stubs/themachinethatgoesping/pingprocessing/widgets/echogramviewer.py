from IPython.core.display_functions import display
from __future__ import annotations
import asyncio as asyncio
import ipywidgets as ipywidgets
from matplotlib import dates as mdates
from matplotlib import pyplot as plt
import numpy as np
import themachinethatgoesping as theping
from themachinethatgoesping.pingprocessing.watercolumn import echograms
from time import time
import types as types
import typing
__all__ = ['EchogramViewer', 'asyncio', 'display', 'echograms', 'ipywidgets', 'mdates', 'np', 'plt', 'theping', 'time', 'types']
class EchogramViewer:
    __firstlineno__: typing.ClassVar[int] = 15
    __static_attributes__: typing.ClassVar[tuple] = ('args_plot', 'axes', 'box_buttons', 'box_sliders', 'clear_button', 'cmap', 'colorbar', 'display_progress', 'echogram_axes', 'echogramdata', 'extents_background', 'fig', 'fig_events', 'high_res_extents', 'high_res_images', 'images_background', 'loop', 'mapables', 'names', 'nechograms', 'output', 'pingline', 'pingviewer', 'progress', 'task', 'update_button', 'w_interpolation', 'w_vmax', 'w_vmin', 'x_axis_name', 'xlim', 'y_axis_name', 'ylim')
    def __init__(self, echogramdata, name = 'Echogram', names = None, figure = None, progress = None, show = True, cmap = 'YlGnBu_r', **kwargs):
        ...
    def clear_output(self, event = 0):
        ...
    def click_echogram(self, event):
        ...
    def connect_pingviewer(self, pingviewer):
        ...
    def event_loop(self):
        ...
    def init_ax(self, adapt_axis_names = True):
        ...
    def invert_y_axis(self):
        ...
    def show(self):
        ...
    def show_background_echogram(self):
        ...
    def show_background_zoom(self, event = 0):
        ...
    def update_ping_line(self):
        ...
    def update_view(self, w = None, reset = False):
        ...
