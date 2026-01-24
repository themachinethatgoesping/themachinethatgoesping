from typing import Union

import matplotlib.axes._axes

from . import (
    ainslie_leighton as ainslie_leighton,
    anderson as anderson,
    bubble_dissolution as bubble_dissolution,
    li as li,
    medwin as medwin,
    parameters as parameters,
    thuraisingham as thuraisingham
)
from .parameters import (
    EnvironmentalParameters as EnvironmentalParameters
)


def plot_bs_comparison(frequency_hz: float = 300000.0, water_depth_m: float = 50.0, bubble_diameter_min_mm: float = 0.001, bubble_diameter_max_mm: float = 20.0, num_points: int = 50000, ax: Union[matplotlib.axes._axes.Axes, None] = None, models: Union[list[str], None] = None) -> matplotlib.axes._axes.Axes:
    """
    Plot backscattering strength from multiple models vs bubble diameter.

    Parameters
    ----------
    frequency_hz : float
        Acoustic frequency in Hz (default: 300 kHz)
    water_depth_m : float
        Water depth in meters (default: 50 m)
    bubble_diameter_min_mm : float
        Minimum bubble diameter in mm (default: 0.001 mm)
    bubble_diameter_max_mm : float
        Maximum bubble diameter in mm (default: 20 mm)
    num_points : int
        Number of points for the plot (default: 50000)
    ax : plt.Axes | None
        Matplotlib axes to plot on. If None, creates new figure.
    models : list[str] | None
        List of models to plot. Options: 'thuraisingham', 'li', 'medwin', 
        'anderson', 'ainslie_leighton'. If None, plots all models.

    Returns
    -------
    plt.Axes
        The matplotlib axes with the plot
    """

def main():
    """Main function to demonstrate bubble backscattering model comparison."""
