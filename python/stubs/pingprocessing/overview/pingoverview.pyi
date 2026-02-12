from typing import List, Union

from themachinethatgoesping.navigation_nanopy.navtools import (
    cumulative_latlon_distances_m as cumulative_latlon_distances_m
)
from themachinethatgoesping.pingprocessing.core.progress import (
    get_progress_iterator as get_progress_iterator
)
import themachinethatgoesping.pingprocessing.overview.nav_plot as nav_plot


class PingOverview:
    """
    A class to represent an overview of ping statistics.

    Attributes
    ----------
    variables : defaultdict
        A dictionary containing lists of variables.
    stats : defaultdict
        A dictionary containing statistics for each variable.

    Methods
    -------
    __init__(self, ping_list=None, progress=False)
        Constructs a PingOverview object.
    add_ping_list(self, ping_list, progress=False)
        Adds a list of pings to the overview.
    add_ping(self, ping)
        Adds a single ping to the overview.
    get_stat_keys(self)
        Returns the keys of the statistics dictionary.
    get_min(self, key)
        Returns the minimum value of a variable.
    get_max(self, key)
        Returns the maximum value of a variable.
    get_minmax(self, key)
        Returns the minimum and maximum values of a variable.
    get_mean(self, key)
        Returns the mean value of a variable.
    get_median(self, key)
        Returns the median value of a variable.
    """

    def __init__(self, ping_list: List = None, progress: bool = False) -> None:
        """
        Constructs a PingOverview object.

        Parameters
        ----------
        ping_list : List, optional
            A list of pings to add to the overview, by default None
        progress : bool, optional
            Whether to show a progress bar, by default False
        """

    def plot_navigation(self, ax, label='survey', annotate=True, max_points=100000, **kwargs):
        """
        Plot latitude and longitude coordinates on a given axis.

        Parameters:
            ax (matplotlib.axes.Axes): The axis on which to plot the coordinates.
            label (str, optional): Name of the survey. Defaults to 'survey'.
            annotate (bool, optional): Whether to annotate the plot with the survey name. Defaults to True.
            max_points (int, optional): Maximum number of points to plot. Defaults to 100000.
            **kwargs: Additional keyword arguments to be passed to the plot function.

        Returns:
            None
        """

    def get_speed_in_knots(self): ...

    def plot_speed_in_knots(self, ax, **kwargs):
        """
        Plot speed in knots over time on a given axis.

        Parameters:
            ax (matplotlib.axes.Axes): The axis on which to plot the speed.
            **kwargs: Additional keyword arguments to be passed to the plot function.
        Returns:
            None
        """

    def get_ping_rate_hz(self):
        """
        Compute the ping rate in Hz (pings per second).

        Returns:
            np.ndarray: Array of ping rates in Hz for each ping interval.
        """

    def plot_ping_rate_hz(self, ax, **kwargs):
        """
        Plot ping rate in Hz over time on a given axis.

        Parameters:
            ax (matplotlib.axes.Axes): The axis on which to plot the ping rate.
            **kwargs: Additional keyword arguments to be passed to the plot function.
        Returns:
            None
        """

    def get_course_over_ground(self):
        """
        Compute course-over-ground (COG) in degrees for each ping.

        COG is the bearing from each ping to the next (north = 0°,
        east = 90°).  The last ping gets the same COG as the
        second-to-last.

        Returns:
            np.ndarray: COG in degrees [0, 360) per ping.
        """

    def plot_heading_vs_course(self, ax, heading_offset=0.0, **kwargs):
        """
        Plot true heading (yaw) and course-over-ground on the same axis.

        Useful for visually checking whether the vessel heading agrees
        with the actual track direction.

        Parameters:
            ax (matplotlib.axes.Axes): Target axis.
            heading_offset (float): Offset added to yaw before plotting
                (same convention as ``split_pings.by_course``).
            **kwargs: Forwarded to both ``ax.plot`` calls.
        """

    def add_ping_list(self, ping_list: List, progress: bool = False) -> None:
        """
        Adds a list of pings to the overview.

        Parameters
        ----------
        ping_list : List
            A list of pings to add to the overview.
        progress : bool, optional
            Whether to show a progress bar, by default False
        """

    def add_ping(self, ping) -> None:
        """
        Adds a single ping to the overview.

        Parameters
        ----------
        ping : Ping
            A ping to add to the overview.
        """

    def get_stat_keys(self) -> List:
        """
        Returns the keys of the statistics dictionary.

        Returns
        -------
        List
            The keys of the statistics dictionary.
        """

    def get_min(self, key: str) -> float:
        """
        Returns the minimum value of a variable.

        Parameters
        ----------
        key : str
            The name of the variable.

        Returns
        -------
        float
            The minimum value of the variable.
        """

    def get_max(self, key: str) -> float:
        """
        Returns the maximum value of a variable.

        Parameters
        ----------
        key : str
            The name of the variable.

        Returns
        -------
        float
            The maximum value of the variable.
        """

    def get_minmax(self, key: str) -> tuple:
        """
        Returns the minimum and maximum values of a variable.

        Parameters
        ----------
        key : str
            The name of the variable.

        Returns
        -------
        tuple
            The minimum and maximum values of the variable.
        """

    def get_mean(self, key: str) -> float:
        """
        Returns the mean value of a variable.

        Parameters
        ----------
        key : str
            The name of the variable.

        Returns
        -------
        float
            The mean value of the variable.
        """

    def get_median(self, key: str) -> float:
        """
        Returns the median value of a variable.

        Parameters
        ----------
        key : str
            The name of the variable.

        Returns
        -------
        float
            The median value of the variable.
        """

    def get_primary_file_paths(self) -> list[str]:
        """
        Return the list of unique primary file paths.

        Returns
        -------
        List[str]
            Unique primary file paths referenced by pings in this overview.
        """

    def get_file_paths(self) -> list[str]:
        """
        Return all unique file paths (primary and secondary).

        Returns
        -------
        List[str]
            All unique file paths referenced by pings in this overview.
        """

    def get_primary_file_path(self, ping_index: int) -> str:
        """
        Return the primary file path for a specific ping by its index.

        Parameters
        ----------
        ping_index : int
            Index of the ping in this overview.

        Returns
        -------
        str
            The primary file path of the ping.
        """

    def get_file_paths_for_ping(self, ping_index: int) -> list[str]:
        """
        Return all file paths for a specific ping.

        Parameters
        ----------
        ping_index : int
            Index of the ping in this overview.

        Returns
        -------
        List[str]
            All file paths associated with the ping.
        """

    def get_pings_per_primary_file_path(self) -> dict:
        """
        Return a mapping from primary file path to list of ping indices.

        Returns
        -------
        dict
            Dictionary mapping primary_file_path → list of ping indices.
        """

    def get_pings_per_file_path(self) -> dict:
        """
        Return a mapping from file path (any) to list of ping indices.

        Returns
        -------
        dict
            Dictionary mapping file_path → list of ping indices.
        """

    def get_timestamp_range_per_file(self) -> dict:
        """
        Return min/max timestamp per file path.

        Returns
        -------
        dict
            ``{file_path: (min_timestamp, max_timestamp), …}``
        """

    def get_datetime_range_per_file(self) -> dict:
        """
        Return min/max datetime per file path.

        Returns
        -------
        dict
            ``{file_path: (min_datetime, max_datetime), …}``
        """

    def get_latitude_range_per_file(self) -> dict:
        """
        Return min/max latitude per file path.

        Returns
        -------
        dict
            ``{file_path: (min_latitude, max_latitude), …}``
        """

    def get_longitude_range_per_file(self) -> dict:
        """
        Return min/max longitude per file path.

        Returns
        -------
        dict
            ``{file_path: (min_longitude, max_longitude), …}``
        """

    def to_ping_proxies(self) -> List:
        """
        Create lightweight proxy objects that duck-type ``I_Ping``.

        Each proxy implements the methods used by
        :mod:`~themachinethatgoesping.pingprocessing.filter_pings` and
        :mod:`~themachinethatgoesping.pingprocessing.split_pings`, so you
        can pass the returned list directly to any of those functions.

        To convert the result back, simply pass the (filtered/split)
        proxy list to ``PingOverview(proxy_list)`` — the constructor
        accepts proxies since they implement the same interface as
        real pings.

        Returns
        -------
        list of PingProxy
            One proxy per ping in this overview, in order.  Each proxy
            has an ``overview_index`` attribute recording its position
            in this overview.
        """

    def get_track_data(self, min_lat: float = None, max_lat: float = None, min_lon: float = None, max_lon: float = None, max_points: int = 50000, context_fraction: float = 0.2):
        """
        Return downsampled track coordinates for the given view.

        The algorithm splits the point budget between **viewport** and
        **context** (outside-viewport backbone):

        * **Viewport** (``1 - context_fraction`` of *max_points*):  A
          grid-based density filter keeps the first point per cell so
          that dense areas are thinned while sparse outliers survive.
        * **Context** (``context_fraction`` of *max_points*): Points
          outside the viewport are uniformly sub-sampled to preserve
          the overall track shape, survey-line starts/ends, and line
          continuity when panning.

        The first and last point of the *entire* track are always
        included.

        Parameters
        ----------
        min_lat, max_lat, min_lon, max_lon : float, optional
            View bounding box in degrees.  ``None`` → full extent.
        max_points : int
            Total point budget (default 50 000).
        context_fraction : float
            Fraction of *max_points* reserved for the out-of-viewport
            backbone (default 0.2 = 20 %).

        Returns
        -------
        latitudes : np.ndarray
        longitudes : np.ndarray
        indices : np.ndarray of int
            Indices into the overview arrays (sorted, temporal order).
        """

def get_ping_overview(ping_list: Union[dict[str, list[float]], list[float]], progress: bool = False) -> Union[dict[str, dict[str, Union[float, int]]], 'PingOverview']:
    """
    Returns a summary of ping statistics for a list of pings.

    If the input is a dictionary, the function will return a dictionary with the same keys and a summary of the pings for each key.
    If the input is a list, the function will return a PingOverview object with a summary of the pings.

    Parameters
    ----------
    ping_list : Union[Dict[str, List[float]], List[float]]
        A dictionary or list of pings to summarize.
    progress : bool, optional
        Whether to display a progress bar while processing, by default False.

    Returns
    -------
    Union[Dict[str, Dict[str, Union[float, int]]], 'PingOverview']
        A dictionary or PingOverview object with a summary of the pings.
    """
