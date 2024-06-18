from __future__ import annotations
from matplotlib import dates as mdates
from matplotlib import pyplot as plt
__all__ = ['clear_memory', 'close_plots', 'create_figure', 'mdates', 'plt', 'set_ax_timeformat']
def clear_memory():
    ...
def create_figure(name: str, return_ax: bool = True):
    """
    Helper function to create a figure with a given name that returns the figure and axis
        
    """
def set_ax_timeformat(ax, timeformat = '%d-%m-%Y %H:%M:%S', rotation = 10):
    ...
close_plots: bool = True
