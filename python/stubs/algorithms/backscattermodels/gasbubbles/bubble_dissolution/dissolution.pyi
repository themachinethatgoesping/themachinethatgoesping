import dataclasses
from typing import Union

import numpy

import themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment
from themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment import (
    BubbleEnvironment as BubbleEnvironment,
    GasProperties as GasProperties
)
from themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.rise_velocity import (
    bubble_rise_velocity_clift as bubble_rise_velocity_clift,
    get_rise_velocity_model as get_rise_velocity_model
)


class BubbleDissolutionResult:
    """
    Results from bubble dissolution simulation.

    Contains the bubble state at each depth step during rise.

    Attributes
    ----------
    depths : np.ndarray
        Depth values (m), decreasing from initial depth to surface
    radii : np.ndarray
        Bubble equivalent radius (m) at each depth
    rise_velocities : np.ndarray
        Rise velocity (m/s) at each depth
    gas_fractions : dict[str, np.ndarray]
        Mole fraction of each gas species at each depth
    times : np.ndarray
        Time since release (s) at each depth
    dissolved_mass : np.ndarray
        Cumulative mass dissolved (kg) at each depth
    initial_radius : float
        Initial bubble radius (m)
    initial_depth : float
        Initial (release) depth (m)
    final_radius : float
        Final radius at surface or dissolution (m)
    dissolution_depth : float
        Depth at which bubble fully dissolved (m), or 0 if reached surface
    reached_surface : bool
        True if bubble reached surface with remaining gas
    """

    final_radius: float = 0.0

    dissolution_depth: float = 0.0

    reached_surface: bool = True

    __dataclass_params__: dataclasses._DataclassParams = ...

    __annotations_cache__: dict = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, depths: numpy.ndarray, radii: numpy.ndarray, rise_velocities: numpy.ndarray, gas_fractions: dict, times: numpy.ndarray, dissolved_mass: numpy.ndarray, initial_radius: float, initial_depth: float, final_radius: float = 0.0, dissolution_depth: float = 0.0, reached_surface: bool = True) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

def sherwood_number(radius: float, rise_velocity: float, depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment, gas: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.GasProperties) -> float:
    """
    Calculate Sherwood number for mass transfer.

    The Sherwood number relates convective to diffusive mass transport.
    Uses correlations from Clift et al. (1978) for bubbles.

    Parameters
    ----------
    radius : float
        Bubble radius (m)
    rise_velocity : float
        Rise velocity (m/s)
    depth : float
        Water depth (m)
    env : BubbleEnvironment
        Environmental conditions
    gas : GasProperties
        Properties of the dissolving gas

    Returns
    -------
    float
        Sherwood number (dimensionless)

    Notes
    -----
    Sh = k_L * d / D, where:
    - k_L: mass transfer coefficient (m/s)
    - d: bubble diameter (m)
    - D: molecular diffusivity (m²/s)

    For clean bubbles (mobile interface):
        Sh = 1.13 * Pe^0.5 for Pe > 100 (Levich, 1962)

    For dirty bubbles (rigid interface):
        Sh = 2 + 0.6 * Re^0.5 * Sc^0.33 (Ranz-Marshall)
    """

def mass_transfer_coefficient(radius: float, rise_velocity: float, depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment, gas: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.GasProperties) -> float:
    """
    Calculate mass transfer coefficient k_L.

    Parameters
    ----------
    radius : float
        Bubble radius (m)
    rise_velocity : float
        Rise velocity (m/s)
    depth : float
        Water depth (m)
    env : BubbleEnvironment
        Environmental conditions
    gas : GasProperties
        Gas properties

    Returns
    -------
    float
        Mass transfer coefficient k_L (m/s)
    """

def bubble_dissolution_rate(radius: float, depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment, rise_velocity: float, gas_moles: Union[dict[str, float], None] = None) -> tuple[float, dict[str, float], dict[str, float]]:
    """
    Calculate the rate of bubble radius change due to gas exchange.

    This handles BOTH dissolution OUT (gas leaving bubble) AND dissolution IN
    (gas entering bubble from surrounding water). For a pure methane bubble:
    - CH4 leaves (high partial pressure in bubble vs low dissolved in water)
    - N2, O2 enter (saturated in seawater, zero/low in bubble)

    Parameters
    ----------
    radius : float
        Current bubble radius (m)
    depth : float
        Current depth (m)
    env : BubbleEnvironment
        Environmental conditions
    rise_velocity : float
        Current rise velocity (m/s)
    gas_moles : dict[str, float] | None
        Current moles of each gas in bubble. If None, uses env.gas_composition
        with ideal gas law to estimate initial moles.

    Returns
    -------
    tuple[float, dict[str, float], dict[str, float]]
        - dr/dt: Rate of radius change (m/s)
        - dn/dt per species: Molar flux rates (mol/s), positive = leaving bubble
        - Updated gas mole fractions

    Notes
    -----
    From Leifer & Patro (2002) / McGinnis et al. (2006):

    For each gas i:
        dn_i/dt = -k_L,i * A * (C_sat,i - C_ambient,i)

    where:
        C_sat,i = H_i * p_i  (Henry's law at bubble surface)
        C_ambient,i = H_i * p_ambient,i  (dissolved in water)

    Negative dn/dt means gas ENTERS the bubble.
    """

def simulate_bubble_rise(initial_radius: float, initial_depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment, depth_resolution: float = 1.0, rise_velocity_model: str = 'clift', min_radius: float = 1e-06, max_time: float = 7200.0) -> BubbleDissolutionResult:
    """
    Simulate bubble rise and dissolution through the water column.

    Integrates the coupled rise and dissolution equations from the initial
    depth to the surface (or until bubble completely dissolves). Tracks
    multi-gas exchange: CH4 dissolves out while N2/O2 dissolve into the bubble.

    Parameters
    ----------
    initial_radius : float
        Initial bubble equivalent spherical radius (m)
    initial_depth : float
        Initial (release) depth (m)
    env : BubbleEnvironment
        Environmental conditions including initial gas composition
    depth_resolution : float
        Approximate depth interval for output (m). Default: 1.0 m
    rise_velocity_model : str
        Rise velocity model name: "clift", "leifer", or "woolf"
    min_radius : float
        Minimum radius before bubble considered dissolved (m). Default: 1 μm
    max_time : float
        Maximum simulation time (s). Default: 7200 s (2 hours)

    Returns
    -------
    BubbleDissolutionResult
        Complete simulation results including:
        - depths, radii, rise_velocities arrays
        - gas_fractions: dict mapping gas name to array of mole fractions vs depth
        - This shows how e.g. a 100% CH4 bubble gains N2/O2 during rise

    Examples
    --------
    >>> env = BubbleEnvironment()  # Default: 100% CH4, 8°C, dirty bubbles
    >>> result = simulate_bubble_rise(
    ...     initial_radius=0.002,  # 2 mm
    ...     initial_depth=100.0,   # 100 m
    ...     env=env,
    ...     depth_resolution=5.0
    ... )
    >>> print(f"CH4 fraction at surface: {result.gas_fractions['CH4'][-1]:.1%}")
    >>> print(f"N2 fraction at surface: {result.gas_fractions['N2'][-1]:.1%}")
    """

def simulate_bubble_population(radii: numpy.ndarray, initial_depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment, depth_resolution: float = 5.0, rise_velocity_model: str = 'clift') -> dict:
    """
    Simulate dissolution for a population of bubbles with different sizes.

    Parameters
    ----------
    radii : np.ndarray
        Array of initial bubble radii (m)
    initial_depth : float
        Release depth (m)
    env : BubbleEnvironment
        Environmental conditions
    depth_resolution : float
        Output depth resolution (m)
    rise_velocity_model : str
        Rise velocity model name

    Returns
    -------
    dict
        Dictionary containing:
        - "depth_grid": common depth array
        - "radius_distribution": 2D array [n_bubbles, n_depths]
        - "velocity_distribution": 2D array
        - "fraction_surviving": fraction reaching each depth
        - "individual_results": list of BubbleDissolutionResult

    Examples
    --------
    >>> radii = np.linspace(0.0005, 0.005, 10)  # 0.5-5 mm
    >>> env = BubbleEnvironment()
    >>> pop_result = simulate_bubble_population(radii, 200.0, env)
    """
