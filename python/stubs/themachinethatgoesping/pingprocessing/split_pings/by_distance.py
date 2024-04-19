from __future__ import annotations
from collections import defaultdict
import math as math
import numpy as np
from themachinethatgoesping.echosounders_cppy import filetemplates
from themachinethatgoesping.echosounders_cppy.filetemplates import I_Ping
from themachinethatgoesping import navigation as nav
from themachinethatgoesping.pingprocessing.core.progress import get_progress_iterator
__all__ = ['I_Ping', 'by_distance_difference', 'defaultdict', 'filetemplates', 'get_progress_iterator', 'math', 'nav', 'np']
def by_distance_difference(pings: typing.List[themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping], meters: float, progress: bool = False) -> typing.Dict[int, typing.List[themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping]]:
    """
    
        Split pings into groups based on the distance between consecutive pings.
    
        Parameters
        ----------
        pings : List[I_Ping]
            List of pings to be split.
        meters : float
            Distance threshold in meters.
        progress : bool, optional
            If True, show progress bar, by default False.
    
        Returns
        -------
        Dict[int, List[I_Ping]]]
            A dictionary with keys as group numbers and values as lists of pings belonging to that group.
        
    """
