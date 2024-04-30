from __future__ import annotations
from collections import defaultdict
import datetime as dt
import matplotlib as mpl
from matplotlib import dates as mdates
import numpy as np
import themachinethatgoesping as Ping
from themachinethatgoesping import echosounders
from themachinethatgoesping import pingprocessing
from tqdm.asyncio import tqdm_asyncio as tqdm
__all__ = ['Ping', 'TimeImageBuilder', 'defaultdict', 'dt', 'echosounders', 'mdates', 'mpl', 'np', 'pingprocessing', 'tqdm']
class TimeImageBuilder:
    @staticmethod
    def sample_image_depths(min_d, max_d, res_r, min_depth, max_depth, max_samples = 5000):
        ...
    @staticmethod
    def sample_ping_times(pings, max_pings = 10000, min_time = ..., max_time = ..., min_delta_t = ..., min_delta_t_quantile = 0.05, verbose = True):
        ...
    def __init__(self, pings, max_pings = 10000, max_samples = None, max_image_size = 30000000, min_time = ..., max_time = ..., min_depth = ..., max_depth = ..., min_delta_t = ..., min_delta_t_quantile = 0.05, pss = ..., linear_mean = True, apply_pss_to_bottom = False, verbose = True):
        ...
    def build_image(self, use_range = False, use_datetime = True):
        ...
