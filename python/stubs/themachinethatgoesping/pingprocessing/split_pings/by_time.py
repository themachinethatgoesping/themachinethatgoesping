from __future__ import annotations
from collections import defaultdict
import numpy as np
from themachinethatgoesping.echosounders_cppy import filetemplates
from themachinethatgoesping.echosounders_cppy.filetemplates import I_Ping
from themachinethatgoesping.pingprocessing.core.progress import get_progress_iterator
__all__: list[str] = ['I_Ping', 'by_time_difference', 'defaultdict', 'filetemplates', 'get_progress_iterator', 'np']
def by_time_difference(pings: typing.List[themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping], seconds: float, progress: bool = False) -> typing.Dict[int, typing.List[themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping]]:
    """
    Split pings into groups based on the time difference between them.
    
    Parameters
    ----------
    pings : List[I_Ping]
        List of pings to be split.
    seconds : float
        Time difference in seconds to split the pings.
    progress : bool, optional
        Flag to show progress bar, by default False.
    
    Returns
    -------
    Dict[int, List[I_Ping]]
        Dictionary containing the split pings.
    """
