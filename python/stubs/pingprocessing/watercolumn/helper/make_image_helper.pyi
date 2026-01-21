import numpy

import themachinethatgoesping.algorithms_nanopy.geoprocessing as geoprocessing
import themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures
import themachinethatgoesping.echosounders as echosounders
import themachinethatgoesping.echosounders_nanopy.filetemplates
import themachinethatgoesping.echosounders_nanopy.pingtools
import themachinethatgoesping.navigation as navigation


def get_bottom_directions_wci(ping: themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping, selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection = None) -> (themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1, themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_1, numpy.ndarray):
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

def get_bottom_directions_bottom(ping: themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping) -> (themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1, themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_1, numpy.ndarray):
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
