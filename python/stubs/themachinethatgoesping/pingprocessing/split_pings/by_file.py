from __future__ import annotations
from collections import defaultdict
import math as math
import numpy as np
from themachinethatgoesping.echosounders_cppy import filetemplates
from themachinethatgoesping.echosounders_cppy.filetemplates import I_Ping
from themachinethatgoesping import navigation as nav
from themachinethatgoesping.pingprocessing.core.progress import get_progress_iterator
__all__ = ['I_Ping', 'by_file_nr', 'by_file_path', 'defaultdict', 'filetemplates', 'get_progress_iterator', 'math', 'nav', 'np']
def by_file_nr(pings: typing.List[themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping], progress: bool = True) -> typing.Dict[int, typing.List[themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping]]:
    """
    
    Splits a list of pings by the associated file number.
    
    Args:
        pings (List[I_Ping]): A list of pings to be split.
        progress (bool, optional): Whether to show a progress bar. Defaults to False.
    
    Returns:
        Dict[int, List[I_Ping]]: A dictionary where the keys are channel ids and the values are lists of pings.
    """
def by_file_path(pings: typing.List[themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping], progress: bool = True) -> typing.Dict[str, typing.List[themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping]]:
    """
    
    Splits a list of pings by the associated file path.
    
    Args:
        pings (List[I_Ping]): A list of pings to be split.
        progress (bool, optional): Whether to show a progress bar. Defaults to False.
    
    Returns:
        Dict[str, List[I_Ping]]: A dictionary where the keys are channel ids and the values are lists of pings.
    """
