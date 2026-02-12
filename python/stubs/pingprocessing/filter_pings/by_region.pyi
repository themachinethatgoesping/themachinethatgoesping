import themachinethatgoesping.echosounders_nanopy.filetemplates as filetemplates
import themachinethatgoesping.echosounders_nanopy.filetemplates
from themachinethatgoesping.echosounders_nanopy.filetemplates import (
    I_Ping as I_Ping
)
from themachinethatgoesping.navigation_nanopy.navtools import (
    compute_latlon_distance_m as compute_latlon_distance_m
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

def by_distance(pings: list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping], center_lat: float, center_lon: float, max_distance_m: float, progress: bool = False) -> list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping]:
    """
    Filter pings by distance from a center coordinate.

    Keeps only pings whose position is within *max_distance_m* metres
    of the given (latitude, longitude) center.

    Parameters
    ----------
    pings : list
        List of pings to filter.
    center_lat : float
        Center latitude in degrees.
    center_lon : float
        Center longitude in degrees.
    max_distance_m : float
        Maximum distance from the center in metres.
    progress : bool, optional
        Whether to show a progress bar, by default False.

    Returns
    -------
    list
        Pings within *max_distance_m* of the center.
    """
