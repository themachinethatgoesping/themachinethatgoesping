"""SIMD math functions for performance testing"""

from typing import Annotated, overload

import numpy
from numpy.typing import NDArray


def fma_dispatch_arch() -> str:
    """
    Return the SIMD architecture name selected by fma_dispatch (e.g. 'avx2', 'sse2')
    """

@overload
def fma_dispatch(x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], slope: float, base: float) -> None:
    """Compute x[:] = x * slope + base in-place using runtime SIMD dispatch"""

@overload
def fma_dispatch(x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], slope: float, base: float) -> None: ...

@overload
def fma_xtensor(x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], slope: float, base: float) -> None:
    """
    Compute x[:] = x * slope + base in-place using xt::fma (compile-time SIMD)
    """

@overload
def fma_xtensor(x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], slope: float, base: float) -> None: ...
