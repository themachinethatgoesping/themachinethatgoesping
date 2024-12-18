from __future__ import annotations
from collections import defaultdict
from copy import copy
from copy import deepcopy
import datetime as datetime
import numpy as np
import pandas as pd
import pytimeparse2 as pytimeparse2
from scipy import stats
import themachinethatgoesping as theping
from tqdm.asyncio import tqdm_asyncio as tqdm
import warnings as warnings
__all__ = ['LayerProcessor', 'copy', 'datetime', 'deepcopy', 'defaultdict', 'np', 'pd', 'pytimeparse2', 'stats', 'theping', 'tqdm', 'warnings']
class LayerProcessor:
    @staticmethod
    def __filter_by_layer_size__(data, layers, names = ['mbes', 'sbes']):
        ...
    @staticmethod
    def __filter_by_min_values__(data, layers, names = ['mbes', 'sbes'], qmin = 0.02, dmin = 3):
        ...
    @staticmethod
    def __make_timeblocks_dataframe__(echograms, deltaT = '1min'):
        ...
    @staticmethod
    def split_per_station(data, pm):
        ...
    def __add_layer_vals__(self, name, echogram, step = 1, progress = None):
        ...
    def __init__(self, echograms, names, base_name = None, layers = None, deltaT = '1min', step = 1, min_val_qmin = 0.02, min_val_dmin = 3, only_process_visible = False):
        ...
    def __mark_outliers__(self):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def add_param(self, name, times, param, step = 1):
        ...
    def get_base_name(self):
        ...
    def get_base_num(self, layer):
        ...
    def get_base_num_all(self, layer):
        ...
    def get_base_num_outliers(self, layer):
        ...
    def get_base_val(self, layer):
        ...
    def get_base_val_all(self, layer):
        ...
    def get_base_val_outliers(self, layer):
        ...
    def get_c(self, layer, name = None):
        ...
    def get_c_all(self, layer, name = None):
        ...
    def get_c_outliers(self, layer, name = None):
        ...
    def get_calibration_per_range(self, data = None, layers = None, name = None, bootstrap_resamples = 100, show_progress = True, min_n = None):
        ...
    def get_data(self):
        ...
    def get_deltaT(self):
        ...
    def get_echograms(self):
        ...
    def get_layers(self):
        ...
    def get_names(self):
        ...
    def get_num(self, layer, name = None):
        ...
    def get_num_all(self, layer, name = None):
        ...
    def get_num_outliers(self, layer, name = None):
        ...
    def get_t(self):
        ...
    def get_val(self, layer, name = None):
        ...
    def get_val_all(self, layer, name = None):
        ...
    def get_val_outliers(self, layer, name = None):
        ...
    def get_valid_indices(self, layer, name = None):
        ...
    def get_valid_indices_all(self, layer, name = None):
        ...
    def get_valid_indices_outliers(self, layer, name = None):
        ...
    def reset_filters(self, min_val_qmin = 0.02, min_val_dmin = 3):
        ...
    def split_per_param(self, param_name, param_ranges):
        ...