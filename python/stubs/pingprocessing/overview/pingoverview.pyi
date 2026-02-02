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
