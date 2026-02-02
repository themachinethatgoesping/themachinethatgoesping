"""Simple helper functions"""

import numba.core.registry


__conditional_annotations__: set = ...

M_PI: float = 3.141592653589793

M_PI_2: float = 1.5707963267948966

M_2_PI: float = 6.283185307179586

M_PI_180: float = 0.017453292519943295

MIN_DB_VALUE: float = -50.0

round_int: numba.core.registry.CPUDispatcher = ...
