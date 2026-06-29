"""
Plotting helpers for cross-calibration results.

These operate on the tidy frames returned by :class:`~.data.CalibrationData`
(``calibration_per_range`` and ``cross_data``) so notebooks stay short. Colour
schemes are Paul Tol's qualitative palettes (colour-blind friendly).
"""



TOL_MUTED: list = ...

TOL_LIGHT: list = ...

TOL_BRIGHT: list = ...

def plot_calibration(ax, table, *, y: str = 'depth', min_n: int = 20, color: str = 'black', color_excluded: str = 'grey', label: Optional[str] = None, lines: bool = False, plot_excluded: bool = True, zorder: int = 3, markersize: float = 3.0):
    """
    Plot ``csv`` vs ``y`` with bootstrap-CI error bars.

    ``table`` is the frame from :meth:`CalibrationData.calibration_per_range`.
    Points with fewer than ``min_n`` accepted blocks are drawn faded (or hidden
    when ``plot_excluded=False``).
    """

def plot_cross(ax, cross, *, voffset: float = 0.0, color: str = 'black', color_excluded: str = 'grey', s: float = 1.0, draw_offset: bool = True, label: Optional[str] = None):
    """
    Scatter base vs beam values for one layer (from ``cross_data``).

    ``voffset`` shifts the beam axis (useful to overlay the nominal offset).
    The dashed red line marks the median offset of the accepted (inlier) points.
    """
