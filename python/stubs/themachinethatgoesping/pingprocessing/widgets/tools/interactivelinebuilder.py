from __future__ import annotations
import datetime as datetime
from matplotlib import dates as mdates
from matplotlib import pyplot as plt
import numpy as np
import os as os
__all__: list[str] = ['InteractiveLineBuilder', 'datetime', 'find_closest_index', 'mdates', 'np', 'os', 'plt']
class InteractiveLineBuilder:
    def __del__(self):
        ...
    def __init__(self, echoviewer, filepath = None, axnr = -1):
        ...
    def on_click(self, event):
        ...
    def on_draw(self, event = 0):
        ...
    def on_key_press(self, event):
        ...
    def on_motion(self, event):
        ...
    def on_release(self, event):
        ...
    def redraw_line(self):
        ...
    def reinit_xs(self):
        ...
    def to_file(self, filepath = None):
        ...
    def update_line(self):
        ...
def find_closest_index(sorted_array, target):
    """
    
    Find the index of the closest number in a sorted array using NumPy.
    
    Parameters:
        sorted_array (np.ndarray): A sorted NumPy array of numbers.
        target (float): The target number to find the closest to.
    
    Returns:
        int: The index of the closest number in the sorted array.
    """
