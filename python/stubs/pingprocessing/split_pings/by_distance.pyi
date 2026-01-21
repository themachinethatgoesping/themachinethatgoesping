import themachinethatgoesping.echosounders_nanopy.filetemplates as filetemplates
import themachinethatgoesping.echosounders_nanopy.filetemplates
from themachinethatgoesping.echosounders_nanopy.filetemplates import (
    I_Ping as I_Ping
)
import themachinethatgoesping.navigation as nav
from themachinethatgoesping.pingprocessing.core.progress import (
    get_progress_iterator as get_progress_iterator
)


def by_distance_difference(pings: list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping], meters: float, progress: bool = False) -> dict[int, list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping]]:
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
