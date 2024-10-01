from __future__ import annotations
import numpy as np
import numpy
import themachinethatgoesping as Ping
from themachinethatgoesping.algorithms import geoprocessing as gp
import themachinethatgoesping.algorithms.geoprocessing.datastructures
from themachinethatgoesping import echosounders as es
import themachinethatgoesping.echosounders_cppy.filetemplates
import themachinethatgoesping.echosounders_cppy.pingtools
__all__ = ['Ping', 'es', 'get_bottom_directions_bottom', 'get_bottom_directions_wci', 'gp', 'np']
def get_bottom_directions_bottom(ping: themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping) -> (themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1, themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_1, numpy.ndarray):
    """
    
        Retrieve bottom positions/directions/sample numbers from a bottom ping.
    
        Parameters
        ----------
        ping : es.filetemplates.I_Ping
            Ping to retrieve bottom positions/directions/sample numbers from.
    
        Returns
        -------
        Tuple[gp.datastructures.XYZ_1, gp.datastructures.SampleDirectionsRange_1, np.ndarray]
            A tuple containing the bottom positions, directions, and sample numbers.
        
    """
def get_bottom_directions_wci(ping: themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, selection: themachinethatgoesping.echosounders_cppy.pingtools.BeamSelection = None) -> (themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1, themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleDirectionsRange_1, numpy.ndarray):
    """
    
        Retrieve bottom positions/directions/sample numbers from a water column ping.
        Note: this function is an approximation (for performance reasons). As such, it 
        assumes a constant sound velocity profile.
    
        Parameters
        ----------
        ping : es.filetemplates.I_Ping
            Ping to retrieve bottom positions/directions/sample numbers from.
        selection : es.pingtools.BeamSelection, optional
            A beam selection to retrieve the directions from, by default None.
    
        Returns
        -------
        Tuple[gp.datastructures.XYZ_1, gp.datastructures.SampleDirectionsRange_1, np.ndarray]
            A tuple containing the bottom positions, directions, and sample numbers.
        
    """
