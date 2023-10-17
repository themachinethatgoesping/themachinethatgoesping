"""

functions for making images from watercolumn data
"""
from __future__ import annotations
import numpy
import numpy as np
from themachinethatgoesping.algorithms import geoprocessing as gp
import themachinethatgoesping.algorithms.geoprocessing.datastructures
from themachinethatgoesping import echosounders as es
import themachinethatgoesping.echosounders_cppy.filetemplates
import themachinethatgoesping.echosounders_cppy.pingtools
__all__ = ['es', 'get_bottom_directions_bottom', 'get_bottom_directions_wci', 'gp', 'np']
def get_bottom_directions_bottom(ping):
    ...
def get_bottom_directions_wci(ping: themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, selection: themachinethatgoesping.echosounders_cppy.pingtools.BeamSelection = None) -> (themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1, themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_1, numpy.ndarray):
    """
    retrieve bottom positions/directions/sample numbers from a water column ping
        Note: this function is an approximation (for performance reasons). As such it 
        assumes a constant sound velocity profile
    
        Parameters
        ----------
        ping : es.filetemplates.I_Ping
            Ping to retrieve bottom positions/directions/sample numbers from
        selection : es.pingtools.BeamSelection, optional
            A beam selection to retreive the directions from, by default None
    
        Returns
        -------
        _type_
            _description_
        
    """
