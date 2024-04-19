from __future__ import annotations
from collections import defaultdict
import datetime as dt
import matplotlib as mpl
from matplotlib import dates as mdates
import numpy as np
from themachinethatgoesping import tools as ptools
__all__ = ['EchogramSection', 'defaultdict', 'dt', 'mdates', 'mpl', 'np', 'ptools']
class EchogramSection:
    def __init__(self, data):
        ...
    def bottom_depth_per_ping_distance(self, ping_distance):
        ...
    def bottom_depth_per_ping_index(self, ping_index):
        ...
    def bottom_depth_per_ping_number(self, ping_number):
        ...
    def bottom_depth_per_ping_time(self, ping_time):
        ...
    def echosounder_depth_per_ping_distance(self, ping_distance):
        ...
    def echosounder_depth_per_ping_index(self, ping_index):
        ...
    def echosounder_depth_per_ping_number(self, ping_number):
        ...
    def echosounder_depth_per_ping_time(self, ping_time):
        ...
    def get_data(self):
        ...
    def get_downsampled(self, downsample_factor):
        ...
    def get_echogram(self, ping_numbers = None, ping_axis = 'index', sample_axis = 'index'):
        ...
    def get_echogram_layer(self, upper_depth, lower_depth, depth_times = None, ping_indices = None, ping_axis = 'index', sample_axis = 'index'):
        ...
    def get_extent(self, ping_axis = 'index', sample_axis = 'index', min_ping_index = 0, max_ping_index = -1, min_sample_index = 0, max_sample_index = -1):
        ...
    def get_ping_distances(self):
        ...
    def get_ping_indices(self):
        ...
    def get_ping_numbers(self):
        ...
    def get_ping_parameters(self):
        ...
    def get_ping_times_datetimes(self):
        ...
    def get_ping_times_mdates(self):
        ...
    def get_ping_times_unixtimes(self):
        ...
    def get_sample_depths(self):
        ...
    def get_sample_indices(self):
        ...
    def get_sample_numbers(self):
        ...
    def ping_distance_to_ping_index(self, ping_distance):
        ...
    def ping_distance_to_ping_number(self, ping_distance):
        ...
    def ping_distance_to_ping_time(self, ping_distance):
        ...
    def ping_index_to_ping_distance(self, ping_index):
        ...
    def ping_index_to_ping_number(self, ping_index):
        ...
    def ping_index_to_ping_time(self, ping_index):
        ...
    def ping_number_to_ping_distance(self, ping_number):
        ...
    def ping_number_to_ping_index(self, ping_number):
        ...
    def ping_number_to_ping_time(self, ping_number):
        ...
    def ping_time_to_ping_distance(self, ping_time):
        ...
    def ping_time_to_ping_index(self, ping_time):
        ...
    def ping_time_to_ping_number(self, ping_time):
        ...
    def sample_depth_to_sample_index(self, sample_depth):
        ...
    def sample_depth_to_sample_number(self, sample_depth):
        ...
    def sample_index_to_sample_depth(self, sample_index):
        ...
    def sample_index_to_sample_number(self, sample_index):
        ...
    def sample_number_sample_index(self, sample_number):
        ...
    def sample_number_to_sample_depth(self, sample_number):
        ...
    def set_bottom_depths(self, bottom_depths, bottom_depth_times):
        ...
    def set_echosounder_depths(self, echosounder_depths, echosounder_depth_times):
        ...
    def set_ping_distances(self, ping_distances):
        ...
    def set_ping_numbers(self, ping_numbers):
        ...
    def set_ping_parameters(self, parameter_key, parameters):
        ...
    def set_ping_times(self, ping_unixtimes):
        ...
    def set_sample_depths(self, sample_depths):
        ...
    def set_sample_numbers(self, sample_numbers):
        ...
    @property
    def shape(self):
        ...
