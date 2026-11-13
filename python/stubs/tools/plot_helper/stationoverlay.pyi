from typing import Any, Union

import matplotlib.axes._axes


class StationOverlay:
    """Draws and manages station time markers on a single matplotlib Axes."""

    def __init__(self, ax: matplotlib.axes._axes.Axes): ...

    def add_station_times(self, stations: dict[str, tuple[Any, Any]], line_color: str = '#424242', line_width: float = 2, line_style: str = 'dash', region_color: Union[str, None] = None, region_alpha: float = 0.15, label_color: Union[str, None] = None, label_size: Any = 10, label_position: str = 'top', label_rotation: float = 0, zorder: float = 10) -> None:
        """
        Add station time markers (lines + optional region + label) to `self.ax`.

        Parameters
        ----------
        stations : dict mapping station name -> (start_time, end_time)
        line_color, line_width, line_style : style of the start/end vertical lines.
            line_style accepts Qt names ('solid', 'dash', 'dot', 'dashdot')
            or matplotlib names ('-', '--', ':', '-.').
        region_color, region_alpha : optional shaded axvspan between the lines.
        label_color : defaults to line_color if None.
        label_size : float (points) or a string like '10pt'.
        label_position : 'top' or 'bottom' (axes-fraction height of the label).
        label_rotation : rotation of the label text in degrees.
        zorder : drawn above typical data (images are ~zorder 0, lines ~2).
        """

    def clear_station_times(self, station_name: Union[str, None] = None) -> None:
        """Remove one station's artists, or all stations if name is None."""

    def get_station_names(self):
        """Names currently overlaid (useful for mirroring _station_data_list)."""

def add_station_times(ax: matplotlib.axes._axes.Axes, stations: dict[str, tuple[Any, Any]], **kwargs) -> StationOverlay:
    """
    One-shot convenience wrapper: creates an overlay, adds stations, returns it
    (keep the returned object if you ever want to clear/remove markers).
    """
