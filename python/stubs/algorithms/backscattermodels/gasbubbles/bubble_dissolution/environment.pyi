from collections.abc import Callable as _Callable
import dataclasses


class GasProperties:
    """
    Properties of a gas species for dissolution modeling.

    Parameters
    ----------
    name : str
        Gas name (e.g., "CH4", "CO2", "N2", "O2")
    molar_mass : float
        Molar mass in kg/mol
    diffusivity_water : float
        Molecular diffusion coefficient in water at 20°C (m²/s)
    henry_constant_25C : float
        Henry's law constant at 25°C (mol/(m³·Pa)) - dimensionless form
    solubility_temperature_coeff : float
        Temperature coefficient for solubility adjustment (K⁻¹)

    Notes
    -----
    Default values are for methane (CH4) in seawater.
    """

    name: str = 'CH4'

    molar_mass: float = 0.01604

    diffusivity_water: float = 1.49e-09

    henry_constant_25C: float = 1.4e-05

    solubility_temperature_coeff: float = -0.0295

    def diffusivity_at_temperature(self, T: float) -> float:
        """
        Calculate diffusivity adjusted for temperature.

        Uses Stokes-Einstein relation: D ∝ T/μ where μ is viscosity.

        Parameters
        ----------
        T : float
            Temperature in Kelvin

        Returns
        -------
        float
            Diffusivity in m²/s
        """

    def henry_constant_at_temperature(self, T: float) -> float:
        """
        Calculate Henry's constant at given temperature.

        Uses van't Hoff equation for temperature dependence.

        Parameters
        ----------
        T : float
            Temperature in Kelvin

        Returns
        -------
        float
            Henry's constant in mol/(m³·Pa)
        """

    __dataclass_params__: dataclasses._DataclassParams = ...

    __annotations_cache__: dict = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str = 'CH4', molar_mass: float = 0.01604, diffusivity_water: float = 1.49e-09, henry_constant_25C: float = 1.4e-05, solubility_temperature_coeff: float = -0.0295) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

METHANE: GasProperties = ...

CO2: GasProperties = ...

NITROGEN: GasProperties = ...

OXYGEN: GasProperties = ...

class BubbleEnvironment:
    """
    Environmental conditions for bubble dissolution simulation.

    This class defines the water column properties that affect bubble behavior:
    temperature profile, salinity, dissolved gas concentrations, and current.

    Parameters
    ----------
    temperature_profile : Callable[[float], float]
        Function returning temperature (K) at given depth (m).
        Default: constant 281.29 K (8.14°C, typical deep ocean)
    salinity : float
        Salinity in PSU (default: 35.0)
    surface_pressure : float
        Atmospheric pressure at surface in Pa (default: 101325 Pa)
    water_density : float  
        Seawater density in kg/m³ (default: 1027)
    gravity : float
        Gravitational acceleration in m/s² (default: 9.81)
    gas_composition : dict[str, float]
        Gas mole fractions in bubble (should sum to 1.0)
        Default: 100% methane {"CH4": 1.0}
    dissolved_gas_saturation : dict[str, float]
        Saturation level of each gas in surrounding water (0-1 range)
        Default: {"CH4": 0.0} (no methane dissolved)
    gas_properties : dict[str, GasProperties]
        Properties for each gas species.
    bubble_surface_condition : str
        "clean" or "dirty" - affects mass transfer coefficient.
        Clean bubbles have mobile surface, dirty have immobile (surfactants).

    Examples
    --------
    >>> env = BubbleEnvironment()  # Default: 100% CH4, constant temperature
    >>> env = BubbleEnvironment(
    ...     temperature_profile=lambda z: 280 + 0.02*z,  # Thermocline
    ...     gas_composition={"CH4": 0.95, "N2": 0.05}
    ... )
    """

    salinity: float = 35.0

    surface_pressure: float = 101325.0

    water_density: float = 1027.0

    gravity: float = 9.81

    bubble_surface_condition: str = 'dirty'

    def pressure_at_depth(self, depth: float) -> float:
        """
        Calculate total pressure at given depth.

        Parameters
        ----------
        depth : float
            Water depth in meters (positive downward)

        Returns
        -------
        float
            Total pressure in Pa
        """

    def gas_density_at_depth(self, depth: float) -> float:
        """
        Calculate gas density inside bubble at depth using ideal gas law.

        Parameters
        ----------
        depth : float
            Water depth in meters

        Returns
        -------
        float
            Gas density in kg/m³
        """

    def kinematic_viscosity(self, depth: float) -> float:
        """
        Calculate seawater kinematic viscosity.

        Simplified Sharqawy et al. (2010) correlation.

        Parameters
        ----------
        depth : float
            Water depth in meters

        Returns
        -------
        float
            Kinematic viscosity in m²/s
        """

    def surface_tension(self, depth: float) -> float:
        """
        Calculate water-gas surface tension.

        Parameters
        ----------
        depth : float
            Water depth in meters

        Returns
        -------
        float
            Surface tension in N/m
        """

    __dataclass_params__: dataclasses._DataclassParams = ...

    __annotations_cache__: dict = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, temperature_profile: _Callable[[float], float] = ..., salinity: float = 35.0, surface_pressure: float = 101325.0, water_density: float = 1027.0, gravity: float = 9.81, gas_composition: dict[str, float] = ..., dissolved_gas_saturation: dict[str, float] = ..., gas_properties: dict[str, GasProperties] = ..., bubble_surface_condition: str = 'dirty') -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...
