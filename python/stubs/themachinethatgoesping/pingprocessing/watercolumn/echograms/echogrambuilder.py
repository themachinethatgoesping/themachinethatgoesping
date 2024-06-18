from __future__ import annotations
from collections import defaultdict
import datetime as dt
import matplotlib as mpl
from matplotlib import dates as mdates
import numpy as np
from themachinethatgoesping import echosounders
from themachinethatgoesping import pingprocessing
from themachinethatgoesping.pingprocessing.watercolumn.echograms.echoimagebuilders.timeimagebuilder import TimeImageBuilder
from tqdm.asyncio import tqdm_asyncio as tqdm
__all__ = ['EchogramBuilder', 'TimeImageBuilder', 'defaultdict', 'dt', 'echosounders', 'mdates', 'mpl', 'np', 'pingprocessing', 'tqdm']
class EchogramBuilder:
    def __init__(self, pings, pingsampleselector = ..., apply_pss_to_bottom = False):
        ...
    def build_time_echogram(self, max_pings = 10000, max_samples = None, max_image_size = 30000000, min_time = ..., max_time = ..., min_depth = ..., max_depth = ..., min_delta_t = ..., min_delta_t_quantile = 0.05, pss = None, linear_mean = True, use_range = False, verbose = True):
        ...
