"""
Range-dependent calibration-offset models.

These 1-D models describe how the cross-calibration offset ``C`` (dB) varies
with range/depth for a single beam. They share a tiny common interface so the
:class:`~.pattern.CalibrationPattern` can fit and evaluate them
interchangeably:

* ``fit(x, y)`` where ``x`` is range/depth and ``y`` is the offset ``C`` --
  returns ``self``.
* ``__call__(x)`` -> predicted offset at ``x``.
* ``get_fit(x0, x1, n)`` -> ``(x_grid, y_grid)`` for plotting.

Two models are provided:

* :class:`PchipBlendChangePoint` -- a shape-preserving PCHIP spline blended
  into a constant (or linear) tail beyond a detected change point ``xc``. This
  is the model used to build the beam pattern (the near-field rolls off, the
  far field is ~constant).
* :class:`LogisticSTR` -- a smooth-transition regression with a logistic gate
  between a linear near-field trend and a constant/linear far-field trend.
"""

import np


class CalibrationModel:
    """Common interface for 1-D calibration-offset models."""

    def fit(self, x, y) -> 'CalibrationModel': ...

    def __call__(self, x): ...

    def get_fit(self, x0: float, x1: float, n: int = 200) -> Tuple[np.ndarray, np.ndarray]: ...

class PchipBlendChangePoint(CalibrationModel):
    """
    PCHIP spline blended into a constant/linear tail past a change point.

    The near field is interpolated by a shape-preserving PCHIP spline; beyond a
    detected change point ``xc`` the model blends (via a logistic weight of
    width ``blend_width``) into a constant (mean of the tail) or a linear tail.

    Parameters
    ----------
    mode:
        ``'auto'`` (decide constant vs linear from the tail slope),
        ``'constant'`` or ``'linear'``.
    blend_width:
        Width of the logistic blend between spline and tail (same units as x).
    window_frac:
        Fraction of points in the sliding window used to locate the change
        point from local linear-fit residuals.
    """

    def __init__(self, mode: str = 'auto', blend_width: float = 5.0, window_frac: float = 0.15): ...

    def fit(self, x, y) -> 'PchipBlendChangePoint': ...

    def __call__(self, x): ...

class LogisticSTR(CalibrationModel):
    """
    Smooth-transition regression with a logistic gate between two regimes.

    Near field: linear trend ``b0 + b1*x``. Far field: constant ``a0`` (or
    linear ``a0 + a1*x``). The transition is a logistic gate centred at
    ``transition_center`` with steepness ``gamma``.
    """

    def __init__(self, tail: str = 'constant'): ...

    def fit(self, x, y) -> 'LogisticSTR': ...

    def __call__(self, x): ...
