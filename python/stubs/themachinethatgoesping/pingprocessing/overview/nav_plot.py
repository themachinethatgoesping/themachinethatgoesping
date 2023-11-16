from __future__ import annotations
from collections import defaultdict
from matplotlib import pyplot as plt
import numpy as np
from themachinethatgoesping.pingprocessing.core.progress import get_progress_iterator
from themachinethatgoesping.pingprocessing.overview.pingoverview import get_ping_overview
__all__ = ['create_figure', 'defaultdict', 'get_ping_overview', 'get_progress_iterator', 'np', 'plot_latlon', 'plt']
def create_figure(name, aspect = 'equal', close_plots = True):
    ...
def plot_latlon(lat, lon, ax, survey_name = 'survey', annotate = True, max_points = 100000, **kwargs):
    ...
