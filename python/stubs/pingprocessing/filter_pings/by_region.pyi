import themachinethatgoesping.echosounders_nanopy.filetemplates as filetemplates
import themachinethatgoesping.echosounders_nanopy.filetemplates
from themachinethatgoesping.echosounders_nanopy.filetemplates import (
    I_Ping as I_Ping
)
from themachinethatgoesping.pingprocessing.core.progress import (
    get_progress_iterator as get_progress_iterator
)


def by_latlon(pings: list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping], min_lat: float = float('nan'), max_lat: float = float('nan'), min_lon: float = float('nan'), max_lon: float = float('nan'), progress: bool = False) -> list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping]:
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
