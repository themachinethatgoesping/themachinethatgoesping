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
    """
    
        Plot latitude and longitude coordinates on a given axis.
    
        Parameters:
            lat (list): List of latitude coordinates.
            lon (list): List of longitude coordinates.
            ax (matplotlib.axes.Axes): The axis on which to plot the coordinates.
            survey_name (str, optional): Name of the survey. Defaults to 'survey'.
            annotate (bool, optional): Whether to annotate the plot with the survey name. Defaults to True.
            max_points (int, optional): Maximum number of points to plot. Defaults to 100000.
            **kwargs: Additional keyword arguments to be passed to the plot function.
    
        Returns:
            None
        
    """
