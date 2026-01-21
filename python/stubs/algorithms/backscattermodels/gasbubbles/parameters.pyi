import dataclasses


class EnvironmentalParameters:
    """
    Parameters for gas bubble backscatter models.

    Default values are typical for methane (CH4) bubbles in seawater.
    """

    T: float = 281.29

    tau: float = 0.0745

    pv: float = 872.0

    eta_s: float = 0.0015

    K_gas: float = 0.08

    Cp: float = 2191.0

    g: float = 9.81

    rho_liq: float = 1025.0

    P_atm: float = 101000.0

    cw: float = 1485.0

    gamma: float = 1.299

    Mm: float = 0.016

    R: float = 8.31

    __dataclass_params__: dataclasses._DataclassParams = ...

    __annotations_cache__: dict = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, T: float = 281.29, tau: float = 0.0745, pv: float = 872.0, eta_s: float = 0.0015, K_gas: float = 0.08, Cp: float = 2191.0, g: float = 9.81, rho_liq: float = 1025.0, P_atm: float = 101000.0, cw: float = 1485.0, gamma: float = 1.299, Mm: float = 0.016, R: float = 8.31) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...
