import themachinethatgoesping.echosounders_nanopy.filetemplates as filetemplates
import themachinethatgoesping.echosounders_nanopy.filetemplates
from themachinethatgoesping.echosounders_nanopy.filetemplates import (
    I_Ping as I_Ping
)
from themachinethatgoesping.pingprocessing.core.progress import (
    get_progress_iterator as get_progress_iterator
)


def by_time_difference(pings: list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping], seconds: float, progress: bool = False) -> dict[int, list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping]]:
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
