import dataclasses
import enum
from typing import Union

import themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment
from themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment import (
    BubbleEnvironment as BubbleEnvironment
)


class BubbleShapeRegime(enum.Enum):
    """Bubble shape regime classification."""

    SPHERICAL = spherical
    """Bubble shape regime classification."""

    ELLIPSOIDAL = ellipsoidal
    """Bubble shape regime classification."""

    WOBBLING = wobbling
    """Bubble shape regime classification."""

    SPHERICAL_CAP = spherical_cap
    """Bubble shape regime classification."""

class BubbleShapeResult:
    """
    Complete bubble shape characterization.

    Attributes
    ----------
    regime : BubbleShapeRegime
        Shape regime classification
    aspect_ratio : float
        E = minor axis / major axis (1.0 = sphere, <1 = oblate)
    equivalent_radius : float
        Radius of sphere with same volume (m)
    semi_major_axis : float
        Semi-major axis a (horizontal, m) for ellipsoid
    semi_minor_axis : float
        Semi-minor axis b (vertical, m) for ellipsoid
    eotvos_number : float
        Eo = Δρ g d² / σ
    morton_number : float
        Mo = g μ⁴ Δρ / (ρ² σ³)
    reynolds_number : float
        Re = ρ u d / μ (if velocity known)
    surface_area : float
        Bubble surface area (m²)
    cross_section_area : float
        Projected area normal to rise direction (m²)
    """

    reynolds_number: None = None

    surface_area: None = None

    cross_section_area: None = None

    __dataclass_params__: dataclasses._DataclassParams = ...

    __annotations_cache__: dict = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, regime: BubbleShapeRegime, aspect_ratio: float, equivalent_radius: float, semi_major_axis: float, semi_minor_axis: float, eotvos_number: float, morton_number: float, reynolds_number: Union[float, None] = None, surface_area: Union[float, None] = None, cross_section_area: Union[float, None] = None) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

def calculate_eotvos_number(radius: float, depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment) -> float:
    """
    Calculate Eötvös (Bond) number.

    Eo = Δρ g d² / σ

    Measures ratio of buoyancy to surface tension forces.

    Parameters
    ----------
    radius : float
        Bubble equivalent radius (m)
    depth : float
        Water depth (m)
    env : BubbleEnvironment
        Environmental conditions

    Returns
    -------
    float
        Eötvös number (dimensionless)
    """

def calculate_morton_number(depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment) -> float:
    """
    Calculate Morton number.

    Mo = g μ⁴ Δρ / (ρ² σ³)

    Fluid property group that characterizes the system.
    For water at ~20°C: Mo ≈ 2.5e-11

    Parameters
    ----------
    depth : float
        Water depth (m)
    env : BubbleEnvironment
        Environmental conditions

    Returns
    -------
    float
        Morton number (dimensionless)
    """

def calculate_aspect_ratio_wellek(eotvos: float) -> float:
    """
    Calculate bubble aspect ratio using Wellek et al. (1966) correlation.

    E = 1 / (1 + 0.163 * Eo^0.757)

    Valid for clean bubbles in the ellipsoidal regime.

    Parameters
    ----------
    eotvos : float
        Eötvös number

    Returns
    -------
    float
        Aspect ratio E = b/a (minor/major axis)
    """

def calculate_aspect_ratio_loth(eotvos: float, morton: float) -> float:
    """
    Calculate bubble aspect ratio using Loth (2008) correlation.

    More accurate for wider range of conditions than Wellek.
    Accounts for Morton number effects.

    Parameters
    ----------
    eotvos : float
        Eötvös number
    morton : float
        Morton number

    Returns
    -------
    float
        Aspect ratio E = b/a
    """

def calculate_aspect_ratio_myint(eotvos: float, weber: float = None) -> float:
    """
    Calculate aspect ratio using Myint et al. (2007) correlation.

    Based on experimental data for air bubbles in water.

    Parameters
    ----------
    eotvos : float
        Eötvös number
    weber : float, optional
        Weber number (if known)

    Returns
    -------
    float
        Aspect ratio E = b/a
    """

def predict_bubble_shape(radius: float, depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment, rise_velocity: float = None, aspect_ratio_model: str = 'loth') -> BubbleShapeResult:
    """
    Predict bubble shape and aspect ratio.

    Uses the Clift et al. (1978) regime diagram approach combined with
    empirical correlations for aspect ratio.

    Parameters
    ----------
    radius : float
        Bubble equivalent spherical radius (m)
    depth : float
        Water depth (m)
    env : BubbleEnvironment
        Environmental conditions
    rise_velocity : float, optional
        Rise velocity (m/s), used for Reynolds number calculation
    aspect_ratio_model : str
        Model for aspect ratio: "wellek", "loth", or "myint"

    Returns
    -------
    BubbleShapeResult
        Complete shape characterization

    Examples
    --------
    >>> env = BubbleEnvironment()
    >>> shape = predict_bubble_shape(0.002, 50.0, env)  # 2mm at 50m
    >>> print(f"Regime: {shape.regime.value}")
    >>> print(f"Aspect ratio: {shape.aspect_ratio:.2f}")
    """

def bubble_shape_vs_size(radius_range: tuple[float, float], depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment, n_points: int = 50, aspect_ratio_model: str = 'loth') -> dict:
    """
    Calculate bubble shape properties over a range of sizes.

    Parameters
    ----------
    radius_range : tuple[float, float]
        (min_radius, max_radius) in meters
    depth : float
        Water depth (m)
    env : BubbleEnvironment
        Environmental conditions
    n_points : int
        Number of points
    aspect_ratio_model : str
        Aspect ratio model name

    Returns
    -------
    dict
        Dictionary with arrays:
        - "radii": bubble radii (m)
        - "diameters_mm": bubble diameters (mm)
        - "aspect_ratios": E = b/a
        - "eotvos": Eo numbers
        - "regimes": shape regime strings
    """
