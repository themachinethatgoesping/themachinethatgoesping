import themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters
from themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters import (
    EnvironmentalParameters as EnvironmentalParameters
)


pi: float = 3.141592653589793

def calculate_sigma_bs(frequency: float, bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate backscattering cross-section using Thuraisingham (1997) model.

    Parameters
    ----------
    frequency : float
        Acoustic frequency (Hz)
    bubble_radius : float
        Bubble radius (m)
    waterdepth : float
        Water depth (m), positive downward or absolute value used
    params : EnvironmentalParameters, optional
        Environmental parameters. If None, uses default values.

    Returns
    -------
    float
        Backscattering cross-section (m²)
    """
