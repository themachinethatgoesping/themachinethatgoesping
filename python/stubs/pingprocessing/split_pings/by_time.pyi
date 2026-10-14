from themachinethatgoesping.pingprocessing.core.progress import (
    get_progress_iterator as get_progress_iterator
)
from themachinethatgoesping.pingprocessing_nanopy import (
    datatypes as datatypes
)
import themachinethatgoesping.pingprocessing_nanopy.datatypes
from themachinethatgoesping.pingprocessing_nanopy.datatypes import (
    I_Ping as I_Ping
)


def by_time_difference(pings: list[themachinethatgoesping.pingprocessing_nanopy.datatypes.I_Ping], seconds: float, progress: bool = False) -> dict[int, list[themachinethatgoesping.pingprocessing_nanopy.datatypes.I_Ping]]:
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
