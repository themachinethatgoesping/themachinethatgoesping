import themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters
from themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters import (
    EnvironmentalParameters as EnvironmentalParameters
)


pi: float = 3.141592653589793

def calculate_resonance_frequency(bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate Minnaert resonance frequency of a bubble.

    The Minnaert (1933) frequency represents the natural pulsation frequency
    of a spherical gas bubble in a liquid.

    Parameters
    ----------
    bubble_radius : float
        Bubble radius (m)
    waterdepth : float
        Water depth (m)
    params : EnvironmentalParameters, optional
        Environmental parameters. If None, uses default values.

    Returns
    -------
    float
        Resonance frequency (Hz)

    Notes
    -----
    The Minnaert frequency is given by:

    f_0 = (1 / 2πa) * sqrt(3γP_0 / ρ)

    where:
    - a = bubble radius
    - γ = polytropic exponent (ratio of specific heats)
    - P_0 = ambient static pressure
    - ρ = liquid density

    References
    ----------
    Minnaert, M. (1933). "On musical air-bubbles and the sound of running water."
    Philosophical Magazine, 16(104), 235–248.
    """

def calculate_damping_radiation(frequency: float, bubble_radius: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate radiation damping coefficient (dimensionless).

    Radiation damping arises from the re-radiation of acoustic energy
    by the pulsating bubble.

    Parameters
    ----------
    frequency : float
        Acoustic frequency (Hz)
    bubble_radius : float
        Bubble radius (m)
    params : EnvironmentalParameters, optional
        Environmental parameters.

    Returns
    -------
    float
        Radiation damping coefficient (dimensionless)

    Notes
    -----
    δ_rad = ka = ωa/c = 2πfa/c

    At resonance, this equals the bubble radius divided by the wavelength.
    """

def calculate_damping_thermal(frequency: float, bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate thermal damping coefficient (dimensionless).

    Thermal damping arises from heat conduction between the compressed/expanded
    gas and the surrounding liquid during bubble oscillation.

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
        Thermal damping coefficient (dimensionless)

    Notes
    -----
    Following Devin (1959):

    δ_th = 3(γ-1) / a * sqrt(D_g / 2ω)

    where D_g is the thermal diffusivity of the gas.
    """

def calculate_damping_viscous(frequency: float, bubble_radius: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate viscous damping coefficient (dimensionless).

    Viscous damping arises from the oscillatory boundary layer at the
    bubble surface.

    Parameters
    ----------
    frequency : float
        Acoustic frequency (Hz)
    bubble_radius : float
        Bubble radius (m)
    params : EnvironmentalParameters, optional
        Environmental parameters.

    Returns
    -------
    float
        Viscous damping coefficient (dimensionless)

    Notes
    -----
    δ_vis = 4η / (ρωa²)

    where η is the dynamic viscosity of the liquid.
    """

def calculate_total_damping(frequency: float, bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate total damping coefficient (dimensionless).

    The total damping is the sum of radiation, thermal, and viscous components.

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
        Total damping coefficient (dimensionless)
    """

def calculate_sigma_bs(frequency: float, bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate backscattering cross-section using Medwin (1977) model.

    The classic damped resonant bubble model, treating the bubble as a
    simple harmonic oscillator.

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
    The Medwin model is:

    σ_bs = a² / [(f_0²/f² - 1)² + δ²]

    where:
    - a = bubble radius
    - f_0 = Minnaert resonance frequency
    - f = acoustic frequency
    - δ = total damping coefficient (radiation + thermal + viscous)

    This model assumes ka << 1 (long wavelength approximation).
    At resonance (f = f_0), σ_bs = a²/δ² which is finite due to damping.

    References
    ----------
    Medwin, H. (1977). "Counting bubbles acoustically: A review." Ultrasonics, 15, 7–13.
    Clay, C.S. & Medwin, H. (1998). Fundamentals of Acoustical Oceanography.
    """

def calculate_target_strength(frequency: float, bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate target strength in dB from the backscattering cross-section.

    TS = 10 * log10(σ_bs)

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

def calculate_quality_factor(bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate the quality factor Q of the bubble resonator.

    The quality factor describes the sharpness of the resonance peak.
    Higher Q means sharper resonance.

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
        Quality factor (dimensionless)

    Notes
    -----
    Q = 1 / δ_total

    where δ_total is evaluated at the resonance frequency.
    """
