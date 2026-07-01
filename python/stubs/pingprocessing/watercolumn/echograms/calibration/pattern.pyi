"""
Beam-pattern modelling from a cross-calibration dataset.

:class:`CalibrationPattern` turns a :class:`~.data.CalibrationData` into a
per-channel 2-D calibration surface ``offset(beam_angle, range)``. For each beam
angle it fits a 1-D :mod:`.models` curve to the per-range offset, then stacks
those curves (one row per angle) into a bivariate Akima interpolator. The
result can be evaluated anywhere, plotted as a far-field pattern, and applied
back onto multibeam pings as an Sv calibration offset.
"""

import np

from themachinethatgoesping.pingprocessing.watercolumn.echograms.calibration.data import (
    CalibrationData as CalibrationData
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.calibration.models import (
    PchipBlendChangePoint as PchipBlendChangePoint
)


class CalibrationPattern:
    """
    Fit and evaluate a per-channel ``offset(angle, range)`` calibration surface.

    Parameters
    ----------
    x:
        Which range column to model against -- ``'depth'`` (default),
        ``'range_beam'`` or ``'range_base'``.
    model_factory:
        Zero-arg callable returning a fresh model with ``fit``/``get_fit``
        (default :class:`PchipBlendChangePoint`).
    min_n:
        Minimum accepted blocks for a range point to be used.
    min_points:
        Minimum range points required to fit a beam.
    range_grid:
        ``(r0, r1, n)`` grid the fitted curve is sampled on before stacking.
    """

    def __init__(self, *, x: str = 'depth', model_factory: Callable[[], object] = ..., min_n: int = 20, min_points: int = 4, range_grid=(0.0, 30.0, 31)): ...

    def fit(self, data: CalibrationData, *, channels: Optional[Sequence[str]] = None, show_progress: bool = True, **calib_kwargs) -> 'CalibrationPattern':
        """Fit a model per beam angle and build the per-channel interpolators."""

    def channels(self) -> List[str]: ...

    def interpolator(self, channel: str):
        """The bivariate ``offset(angle, range)`` interpolator for a channel."""

    def angles(self, channel: str) -> np.ndarray: ...

    def evaluate(self, channel: str, angles, ranges) -> np.ndarray:
        """Offset surface for ``angles`` x ``ranges`` (2-D)."""

    def far_field(self, channel: str, far_range: float = 5000.0):
        """``(angles, offset)`` at a large (far-field) range for one channel."""

    def apply_to_pings(self, pings, *, show_progress: bool = True) -> dict:
        """Apply the pattern as an Sv calibration onto ``pings`` (in place)."""
