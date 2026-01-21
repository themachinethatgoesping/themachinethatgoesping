from collections.abc import Callable as _Callable
import dataclasses
import enum
from typing import Union

import themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment
from themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment import (
    BubbleEnvironment as BubbleEnvironment
)


class BubbleShape(enum.Enum):
    """Bubble shape regime based on size and Reynolds number."""

    SPHERICAL = spherical
    """Bubble shape regime based on size and Reynolds number."""

    ELLIPSOIDAL = ellipsoidal
    """Bubble shape regime based on size and Reynolds number."""

    SPHERICAL_CAP = spherical_cap
    """Bubble shape regime based on size and Reynolds number."""

class BubbleRiseModel:
    """
    Configuration for bubble rise velocity calculation.

    Parameters
    ----------
    model_name : str
        Name of the model (e.g., "clift", "leifer", "mendelson")
    clean_bubble : bool
        True for clean (mobile interface), False for dirty (rigid interface)
    shape_dependent : bool
        Whether to account for shape transitions
    compute_velocity : Callable
        Function: (radius_m, depth_m, env) -> velocity_m_s
    """

    clean_bubble: bool = False

    shape_dependent: bool = True

    compute_velocity: None = None

    __dataclass_params__: dataclasses._DataclassParams = ...

    __annotations_cache__: dict = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, model_name: str, clean_bubble: bool = False, shape_dependent: bool = True, compute_velocity: Union[_Callable[[float, float, themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment], float], None] = None) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

def bubble_shape_regime(radius: float, depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment) -> BubbleShape:
    """
    Determine bubble shape regime based on size and fluid properties.

    Uses Morton number (M) and Eötvös number (Eo) to classify regime.

    Parameters
    ----------
    radius : float
        Bubble equivalent spherical radius in meters
    depth : float  
        Water depth in meters
    env : BubbleEnvironment
        Environmental conditions

    Returns
    -------
    BubbleShape
        Shape regime classification
    """

def bubble_rise_velocity_clift(radius: float, depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment, clean: bool = False) -> float:
    """
    Calculate bubble rise velocity using Clift et al. (1978) correlations.

    This function accounts for different shape regimes and clean/dirty
    bubble surfaces. The correlations are valid for air bubbles in water
    and similar systems.

    Parameters
    ----------
    radius : float
        Bubble equivalent spherical radius in meters
    depth : float
        Water depth in meters (positive downward)
    env : BubbleEnvironment
        Environmental conditions
    clean : bool
        True for clean bubbles (mobile interface), False for dirty
        (contaminated, rigid interface)

    Returns
    -------
    float
        Terminal rise velocity in m/s

    Notes
    -----
    Clean bubbles: surface-active materials absent, internal circulation.
    Dirty bubbles: surfactants present, rigid interface like solid sphere.

    For most natural conditions, "dirty" is appropriate.

    References
    ----------
    Clift, R., Grace, J.R., Weber, M.E. (1978) "Bubbles, Drops, and Particles"
    """

def bubble_rise_velocity_leifer(radius: float, depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment, clean: bool = False) -> float:
    """
    Calculate bubble rise velocity using Leifer et al. (2000) method.

    This parameterization is specifically developed for methane seep bubbles
    and distinguishes between clean and dirty bubbles based on surfactant
    loading.

    Parameters
    ----------
    radius : float
        Bubble equivalent spherical radius in meters
    depth : float  
        Water depth in meters
    env : BubbleEnvironment
        Environmental conditions
    clean : bool
        True for clean bubbles, False for dirty (default)

    Returns
    -------
    float
        Terminal rise velocity in m/s

    References
    ----------
    Leifer, I., Patro, R.K., Bowyer, P. (2000) "A study on the temperature
    variation of rise velocity for large clean bubbles" J. Atmos. Oceanic
    Technol., 17, 1392-1402.
    """

def bubble_rise_velocity_woolf(radius: float, depth: float, env: themachinethatgoesping.algorithms.backscattermodels.gasbubbles.bubble_dissolution.environment.BubbleEnvironment, clean: bool = False) -> float:
    """
    Calculate bubble rise velocity using Woolf & Thorpe (1991) method.

    Simple parameterization suitable for bubble plume modeling.

    Parameters
    ----------
    radius : float
        Bubble radius in meters
    depth : float
        Water depth in meters  
    env : BubbleEnvironment
        Environmental conditions
    clean : bool
        True for clean, False for dirty bubbles

    Returns
    -------
    float
        Rise velocity in m/s

    References
    ----------
    Woolf, D.K., Thorpe, S.A. (1991) "Bubbles and the air-sea exchange
    of gases in near-saturation conditions" J. Mar. Res., 49, 435-466.
    """

def get_rise_velocity_model(model_name: str = 'clift') -> BubbleRiseModel:
    """
    Get a configured rise velocity model by name.

    Parameters
    ----------
    model_name : str
        Model name: "clift", "leifer", or "woolf"

    Returns
    -------
    BubbleRiseModel
        Configured model object

    Examples
    --------
    >>> model = get_rise_velocity_model("leifer")
    >>> env = BubbleEnvironment()
    >>> velocity = model.compute_velocity(0.002, 100, env)  # 2mm bubble at 100m
    """
