import themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters
from themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters import (
    EnvironmentalParameters as EnvironmentalParameters
)


pi: float = 3.141592653589793

def calculate_gas_properties(bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters) -> tuple[float, float, float]:
    """
    Calculate gas pressure, density, and thermal diffusivity.

    Parameters
    ----------
    bubble_radius : float
        Bubble radius (m)
    waterdepth : float
        Water depth (m)
    params : EnvironmentalParameters
        Environmental parameters

    Returns
    -------
    tuple[float, float, float]
        Gas pressure (Pa), gas density (kg/m³), thermal diffusivity (m²/s)
    """

def calculate_complex_polytropic_index(frequency: float, bubble_radius: float, thermal_diffusivity: float, gamma: float) -> complex:
    """
    Calculate the complex polytropic index Γ.

    The complex polytropic index accounts for the transition between
    isothermal (Γ = 1) and adiabatic (Γ = γ) behavior depending on
    the thermal penetration depth relative to bubble size.

    Parameters
    ----------
    frequency : float
        Acoustic frequency (Hz)
    bubble_radius : float
        Bubble radius (m)
    thermal_diffusivity : float
        Thermal diffusivity of gas (m²/s)
    gamma : float
        Ratio of specific heats

    Returns
    -------
    complex
        Complex polytropic index Γ

    Notes
    -----
    Following Prosperetti (1977):

    Γ = γ / [1 - (1+i)X/2 / tanh((1+i)X/2) × 6i(γ-1)/X²]

    where X = a × sqrt(2ω/D_g) is the dimensionless thermal parameter.

    - For X >> 1 (high frequency or large bubble): Γ → γ (adiabatic)
    - For X << 1 (low frequency or small bubble): Γ → 1 (isothermal)
    """

def calculate_complex_stiffness(bubble_radius: float, gas_pressure: float, polytropic_index: complex, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters) -> complex:
    """
    Calculate the complex stiffness parameter Ω².

    Parameters
    ----------
    bubble_radius : float
        Bubble radius (m)
    gas_pressure : float
        Gas pressure inside bubble (Pa)
    polytropic_index : complex
        Complex polytropic index Γ
    params : EnvironmentalParameters
        Environmental parameters

    Returns
    -------
    complex
        Complex stiffness parameter Ω² (rad²/s²)

    Notes
    -----
    Ω² = (1 / ρa²) × (3ΓP_g - 2τ/a)

    The real part gives the resonance frequency squared.
    The imaginary part contributes to thermal damping.
    """

def calculate_resonance_frequency(bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate the resonance frequency including thermal and surface tension effects.

    Parameters
    ----------
    bubble_radius : float
        Bubble radius (m)
    waterdepth : float
        Water depth (m)
    params : EnvironmentalParameters, optional
        Environmental parameters

    Returns
    -------
    float
        Resonance frequency (Hz)

    Notes
    -----
    ω_0 = sqrt(Re{Ω²})
    f_0 = ω_0 / (2π)

    This differs from the simple Minnaert frequency by including:
    1. Surface tension correction (significant for small bubbles)
    2. Thermal effects via the polytropic index
    """

def calculate_damping_coefficients(frequency: float, bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters) -> tuple[float, float, float]:
    """
    Calculate thermal, viscous, and combined damping coefficients.

    Parameters
    ----------
    frequency : float
        Acoustic frequency (Hz)
    bubble_radius : float
        Bubble radius (m)
    waterdepth : float
        Water depth (m)
    params : EnvironmentalParameters
        Environmental parameters

    Returns
    -------
    tuple[float, float, float]
        Thermal damping β_th, viscous damping β_vis, total damping β_0 (all in rad/s)

    Notes
    -----
    β_th = Im{Ω²} / (2ω)    (thermal damping)
    β_vis = 2η_s / (ρa²)    (viscous damping)
    β_0 = β_th + β_vis       (total damping)
    """

def calculate_sigma_bs(frequency: float, bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate backscattering cross-section using Ainslie & Leighton model.

    This comprehensive model includes:
    - Complex polytropic exponent for thermal effects
    - Surface tension corrections
    - Thermal and viscous damping
    - Near-resonant corrections for finite ka

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
    The backscattering cross-section (Eq. 14 from Ainslie & Leighton 2011):

    σ_bs = a² / [((ω_0/ω)² - 1 - (2β_0/ω)ka)² + ((2β_0/ω) + (ω_0/ω)²ka)²]

    where:
    - a = bubble radius
    - ω = angular frequency
    - ω_0 = resonance angular frequency (from Re{Ω²})
    - β_0 = combined thermal and viscous damping coefficient
    - k = wavenumber in water

    The terms involving ka provide near-resonant corrections that account
    for radiation damping and finite-wavelength effects.

    References
    ----------
    Ainslie, M.A. & Leighton, T.G. (2011). JASA 130(5), 3184–3208.
    """

def calculate_sigma_bs_with_thuraisingham(frequency: float, bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate backscattering cross-section with Thuraisingham correction.

    This adds the Thuraisingham (1997) correction factor for cases where
    ka is not much smaller than 1, which is common for high-frequency
    echosounders imaging larger bubbles.

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
        Backscattering cross-section (m²)

    Notes
    -----
    The Thuraisingham correction factor is:

    T(ka) = [sin(ka)/(ka)]² / [1 + (ka)²]

    This accounts for the breakdown of the monopole approximation
    when the bubble is not small compared to the wavelength.

    References
    ----------
    Thuraisingham, R.A. (1997). Ultrasonics 35, 357–366.
    """

def calculate_extinction_cross_section(frequency: float, bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate extinction cross-section σ_e.

    The extinction cross-section represents the total power removed
    from the incident wave (scattering + absorption).

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
        Extinction cross-section (m²)

    Notes
    -----
    σ_e = 4π Im{f_s} / k

    where f_s is the forward scattering amplitude.

    For a monopole scatterer:
    σ_e = (4πa² / [(ω_0/ω)² - 1]² + δ²) × δ

    where δ is the total damping.
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
