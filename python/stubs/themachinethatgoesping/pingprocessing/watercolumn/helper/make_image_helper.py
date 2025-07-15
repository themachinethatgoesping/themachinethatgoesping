from __future__ import annotations
import numpy
import numpy as np
from themachinethatgoesping.algorithms import geoprocessing
import themachinethatgoesping.algorithms.geoprocessing.datastructures
from themachinethatgoesping import echosounders
import themachinethatgoesping.echosounders_cppy.filetemplates
import themachinethatgoesping.echosounders_cppy.pingtools
from themachinethatgoesping import navigation
__all__ = ['echosounders', 'geoprocessing', 'get_bottom_directions_bottom', 'get_bottom_directions_wci', 'navigation', 'np']
def get_bottom_directions_bottom(ping: themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping) -> (themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1, themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_1, numpy.ndarray):
    """
    
    Retrieve bottom positions/directions/sample numbers from a bottom ping.
    
    Parameters
    ----------
    ping : echosounders.filetemplates.I_Ping
        Ping to retrieve bottom positions/directions/sample numbers from.
    
    Returns
    -------
    Tuple[geoprocessing.datastructures.XYZ_1, geoprocessing.datastructures.SampleDirectionsRange_1, np.ndarray]
        A tuple containing the bottom positions, directions, and sample numbers.
    """
def get_bottom_directions_wci(ping: themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, selection: themachinethatgoesping.echosounders_cppy.pingtools.BeamSelection = None) -> (themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1, themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_1, numpy.ndarray):
    """
    
    Retrieve bottom positions/directions/sample numbers from a water column ping.
    Note: this function is an approximation (for performance reasons). As such, it 
    assumes a constant sound velocity profile.
    
    Parameters
    ----------
    ping : echosounders.filetemplates.I_Ping
        Ping to retrieve bottom positions/directions/sample numbers from.
    selection : echosounders.pingtools.BeamSelection, optional
        A beam selection to retrieve the directions from, by default None.
    
    Returns
    -------
    Tuple[geoprocessing.datastructures.XYZ_1, geoprocessing.datastructures.SampleDirectionsRange_1, np.ndarray]
        A tuple containing the bottom positions, directions, and sample numbers.
    """
