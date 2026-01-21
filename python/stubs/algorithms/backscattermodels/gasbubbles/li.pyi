import themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters
from themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters import (
    EnvironmentalParameters as EnvironmentalParameters
)


pi: float = 3.141592653589793

def calculate_sigma_bs(frequency: float, bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate backscattering cross-section using Li et al. (2020) model.

    This model is adapted from Ainslie & Leighton (2009, 2011) and includes
    Thuraisingham's (1997) correction factor for finite kr effects. It properly
    handles the case when kr is not much smaller than 1, which is common when
    using high-frequency echo sounders to image large bubbles.

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

    Notes
    -----
        The model uses equation (5) from Li et al. (2020):

        σ_bs = r² / [((ω₀²/ω²) - 1 - (2β₀/ω)kr)² + ((2β₀/ω) + (ω₀²/ω²)kr)²]
            × [sin(kr)/(kr)]² / [1 + (kr)²]

    where:
    - r is the bubble radius
    - ω is the angular frequency of the incident sound
    - ω₀ is the resonance angular frequency (from Eq. 6)
    - β₀ is the combined thermal and viscous damping coefficient
    - c_w is the sound speed in water
    - k is the wave number

    The final factor [sin(kr)/(kr)]² / [1 + (kr)²] is Thuraisingham's correction
    which accounts for finite kr effects when the long-wavelength assumption breaks down.
    """

def calculate_target_strength(frequency: float, bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate target strength in dB from the backscattering cross-section.

    TS = 10 * log10(sigma_bs / (4 * pi))

    Parameters
    ----------
    frequency : float
        Acoustic frequency (Hz)
    bubble_radius : float
        Bubble radius (m)
    waterdepth : float
        Water depth (m)
    params : EnvironmentalParameters, optional
        Environmental parameters.

    Returns
    -------
    float
        Target strength (dB re 1 m²)
    """

def calculate_resonance_frequency(bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate the resonance frequency of a bubble.

    Parameters
    ----------
    bubble_radius : float
        Bubble radius (m)
    waterdepth : float
        Water depth (m)
    params : EnvironmentalParameters, optional
        Environmental parameters.

    Returns
    -------
    float
        Resonance frequency (Hz)
    """
