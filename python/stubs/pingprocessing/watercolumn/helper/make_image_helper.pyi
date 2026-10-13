import numpy

from themachinethatgoesping import (
    algorithms as algorithms,
    echosounders as echosounders,
    navigation as navigation
)
from themachinethatgoesping.algorithms_nanopy import (
    geoprocessing as geoprocessing
)
import themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures
import themachinethatgoesping.algorithms_nanopy.pingtools
import themachinethatgoesping.echosounders_nanopy.filetemplates


def get_bottom_directions_wci(ping: themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping, selection: themachinethatgoesping.algorithms_nanopy.pingtools.BeamSelection = None) -> (themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1, themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_1, numpy.ndarray):
    """
    Retrieve bottom positions/directions/sample numbers from a water column ping.
    Note: this function is an approximation (for performance reasons). As such, it 
    assumes a constant sound velocity profile.

    Parameters
    ----------
    ping : echosounders.filetemplates.I_Ping
        Ping to retrieve bottom positions/directions/sample numbers from.
    selection : algorithms.pingtools.BeamSelection, optional
        A beam selection to retrieve the directions from, by default None.

    Returns
    -------
    Tuple[geoprocessing.datastructures.XYZ_1, geoprocessing.datastructures.SampleDirectionsRange_1, np.ndarray]
        A tuple containing the bottom positions, directions, and sample numbers.
    """

def get_bottom_directions_bottom(ping: themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping, selection: themachinethatgoesping.algorithms_nanopy.pingtools.BeamSelection = None) -> (themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1, themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_1, numpy.ndarray):
    """
    Retrieve bottom positions/directions/sample numbers from a bottom ping.

    Parameters
    ----------
    ping : echosounders.filetemplates.I_Ping
        Ping to retrieve bottom positions/directions/sample numbers from.
    selection : algorithms.pingtools.BeamSelection, optional
        A beam selection to filter beams, by default None (all beams).

    Returns
    -------
    Tuple[geoprocessing.datastructures.XYZ_1, geoprocessing.datastructures.SampleDirectionsRange_1, np.ndarray]
        A tuple containing the bottom positions, directions, and sample numbers.
    """
