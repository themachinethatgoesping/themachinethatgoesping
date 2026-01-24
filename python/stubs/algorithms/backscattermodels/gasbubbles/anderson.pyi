import themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters
from themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters import (
    EnvironmentalParameters as EnvironmentalParameters
)


pi: float = 3.141592653589793

def calculate_scattering_coefficient(n: int, ka_outer: float, ka_inner: float, rho_ratio: float) -> complex:
    """
    Calculate the n-th partial wave scattering coefficient A_n.

    For a fluid sphere, the scattering coefficient involves matching
    boundary conditions at the sphere surface.

    Parameters
    ----------
    n : int
        Mode number (0 = monopole, 1 = dipole, etc.)
    ka_outer : float
        Wavenumber times radius in outer medium (water)
    ka_inner : float
        Wavenumber times radius in inner medium (gas)
    rho_ratio : float
        Density ratio (gas/water)

    Returns
    -------
    complex
        Scattering coefficient A_n
    """

def calculate_form_function(frequency: float, bubble_radius: float, waterdepth: float, n_modes: int = 10, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> complex:
    """
    Calculate the backscattering form function f_bs.

    The form function is the dimensionless scattering amplitude.

    Parameters
    ----------
    frequency : float
        Acoustic frequency (Hz)
    bubble_radius : float
        Bubble radius (m)
    waterdepth : float
        Water depth (m)
    n_modes : int, optional
        Number of partial wave modes to include (default: 10)
    params : EnvironmentalParameters, optional
        Environmental parameters.

    Returns
    -------
    complex
        Backscattering form function
    """

def calculate_sigma_bs(frequency: float, bubble_radius: float, waterdepth: float, n_modes: int = 10, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate backscattering cross-section using Anderson (1950) model.

    This is the full partial wave (modal) solution for a fluid sphere.
    No damping is included, so the model shows infinite scattering at
    exact resonance frequencies.

    Parameters
    ----------
    frequency : float
        Acoustic frequency (Hz)
    bubble_radius : float
        Bubble radius (m)
    waterdepth : float
        Water depth (m), positive downward or absolute value used
    n_modes : int, optional
        Number of partial wave modes to include (default: 10)
    params : EnvironmentalParameters, optional
        Environmental parameters. If None, uses default values.

    Returns
    -------
    float
        Backscattering cross-section (m²)

    Notes
    -----
    The backscattering cross-section is:

    σ_bs = (λ² / 4π) |Σ (-1)^n (2n+1) A_n|²

    where A_n are the partial wave scattering coefficients.

    For gas bubbles (large density contrast), the monopole term (n=0)
    dominates near resonance.

    References
    ----------
    Anderson, V.C. (1950). "Sound scattering from a fluid sphere."
    J. Acoust. Soc. Am., 22(4), 426–431.
    """

def calculate_sigma_bs_monopole(frequency: float, bubble_radius: float, waterdepth: float, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
    """
    Calculate backscattering cross-section using monopole approximation.

    This simplified version uses only the monopole (n=0) term, valid when
    ka << 1 (long wavelength approximation).

    This is the undamped resonant scatterer model:

    σ_bs = a² / (f_0²/f² - 1)²

    Note: This diverges at resonance (f = f_0) because no damping is included.
    Use the Medwin model or Ainslie-Leighton model for realistic results.

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
    """

def calculate_target_strength(frequency: float, bubble_radius: float, waterdepth: float, n_modes: int = 10, params: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.parameters.EnvironmentalParameters = None) -> float:
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
    n_modes : int, optional
        Number of partial wave modes
    params : EnvironmentalParameters, optional
        Environmental parameters.

    Returns
    -------
    float
        Target strength (dB re 1 m²)
    """
