from IPython.core.display_functions import display
from __future__ import annotations
import ipywidgets as ipywidgets
from matplotlib import pyplot as plt
import themachinethatgoesping as Ping
from themachinethatgoesping.pingprocessing.watercolumn.helper import make_image_helper as mi_hlp
from themachinethatgoesping.pingprocessing.watercolumn import image as mi
from time import time
__all__ = ['Ping', 'WCIViewer', 'display', 'ipywidgets', 'mi', 'mi_hlp', 'plt', 'time']
class WCIViewer:
    def __init__(self, pings, horizontal_pixels = 1024, name = 'WCI', figure = None, progress = None, show = True, **kwargs):
        ...
    def update_data(self, w):
        ...
    def update_view(self, w):
        ...
