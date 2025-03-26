from IPython.core.display_functions import display
from __future__ import annotations
import ipywidgets as ipywidgets
from matplotlib import pyplot as plt
import numpy as np
from themachinethatgoesping import echosounders
from themachinethatgoesping.pingprocessing.watercolumn.helper import make_image_helper as mi_hlp
from themachinethatgoesping.pingprocessing.watercolumn import image as mi
from themachinethatgoesping.pingprocessing.widgets.tqdmwidget import TqdmWidget
from time import time
import types as types
import typing
__all__ = ['TqdmWidget', 'WCIViewer', 'display', 'echosounders', 'ipywidgets', 'mi', 'mi_hlp', 'np', 'plt', 'time', 'types']
class WCIViewer:
    __firstlineno__: typing.ClassVar[int] = 16
    __static_attributes__: typing.ClassVar[tuple] = ('args_imagebuilder', 'args_plot', 'ax', 'background', 'cmap', 'colorbar', 'display_progress', 'extent', 'fig', 'first_blit', 'imagebuilder', 'layout', 'mapable', 'output', 'progress', 'w_aspect', 'w_date', 'w_fix_xy', 'w_horizontal_pixels', 'w_index', 'w_interpolation', 'w_mp_cores', 'w_procrate', 'w_proctime', 'w_stack', 'w_stack_linear', 'w_stack_step', 'w_time', 'w_unfix_xy', 'w_vmax', 'w_vmin', 'w_wci_render', 'w_wci_value', 'wci', 'wci_value', 'xmax', 'xmin', 'ymax', 'ymin')
    def __init__(self, pings, horizontal_pixels = 1024, name = 'WCI', figure = None, progress = None, show = True, cmap = 'YlGnBu_r', **kwargs):
        ...
    def callback_data(self):
        ...
    def callback_view(self):
        ...
    def fix_xy(self, w):
        ...
    def save_background(self):
        ...
    def set_ping_sample_selector(self, ping_sample_selector, apply_pss_to_bottom = False):
        ...
    def unfix_xy(self, w):
        ...
    def update_data(self, w = None):
        ...
    def update_view(self, w = None):
        ...
