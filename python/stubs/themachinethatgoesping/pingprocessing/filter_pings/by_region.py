from __future__ import annotations
import numpy as np
from themachinethatgoesping.echosounders_cppy import filetemplates
from themachinethatgoesping.echosounders_cppy.filetemplates import I_Ping
from themachinethatgoesping.pingprocessing.core.progress import get_progress_iterator
__all__: list[str] = ['I_Ping', 'by_latlon', 'filetemplates', 'get_progress_iterator', 'np']
def by_latlon(pings: list[themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping], min_lat: float = ..., max_lat: float = ..., min_lon: float = ..., max_lon: float = ..., progress: bool = False) -> list[themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping]:
    """
    
    Filter pings by latitude and longitude region.
    
    Parameters
    ----------
    pings : list
        List of pings to filter.
    min_lat : float, optional
        Minimum latitude value, by default np.nan.
    max_lat : float, optional
        Maximum latitude value, by default np.nan.
    min_lon : float, optional
        Minimum longitude value, by default np.nan.
    max_lon : float, optional
        Maximum longitude value, by default np.nan.
    progress : bool, optional
        Whether to show progress bar, by default False.
    
    Returns
    -------
    list
        List of filtered pings.
    """
