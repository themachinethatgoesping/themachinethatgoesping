"""
Submodule for echogram processing (e.g. bottom detection on Sv echograms)
"""

from typing import Annotated, overload

import numpy
from numpy.typing import NDArray


class BottomDetector:
    """
    Robust echogram bottom detector (ESP3 detec_bottom_algo_v4 port). Set the threshold/option fields (or pass them to the constructor as keyword arguments), add pings with add_ping, then read the detected track with get_bottom / get_bottom_backscatter.
    """

    def __init__(self, thr_bottom: float = -35.0, thr_echo: float = -35.0, thr_backstep: float = -1.0, thr_cum_percent: float = 1.0, r_min: float = 0.0, r_max: float = float('inf'), shift_bot_m: float = 0.0, denoised: bool = True, incidence_angle_deg: float = 10.0, n_ping_smoothing: int = 5, mask_fill_fraction: float = 0.7, remove_outliers: bool = False, outlier_window: int = 7, outlier_threshold: float = 3.0, interpolate_gaps: bool = False, max_interpolation_gap: int = 10, mp_cores: int = 1) -> None:
        """
        Construct a BottomDetector. All parameters are keyword arguments with ESP3 defaults.
        """

    @property
    def thr_bottom(self) -> float:
        """Absolute floor (dB) on the strongest surface backscatter per ping."""

    @thr_bottom.setter
    def thr_bottom(self, arg: float, /) -> None: ...

    @property
    def thr_echo(self) -> float:
        """Candidate offset (dB) below the per-ping maximum backscatter."""

    @thr_echo.setter
    def thr_echo(self, arg: float, /) -> None: ...

    @property
    def thr_backstep(self) -> float:
        """Back-step threshold (dB) for walking up the leading edge."""

    @thr_backstep.setter
    def thr_backstep(self, arg: float, /) -> None: ...

    @property
    def thr_cum_percent(self) -> float:
        """Cumulative-energy threshold (percent, 0..100)."""

    @thr_cum_percent.setter
    def thr_cum_percent(self, arg: float, /) -> None: ...

    @property
    def r_min(self) -> float:
        """Minimum range (m)."""

    @r_min.setter
    def r_min(self, arg: float, /) -> None: ...

    @property
    def r_max(self) -> float:
        """Maximum range (m)."""

    @r_max.setter
    def r_max(self, arg: float, /) -> None: ...

    @property
    def shift_bot_m(self) -> float:
        """Vertical shift of the detected bottom (m, positive = up)."""

    @shift_bot_m.setter
    def shift_bot_m(self, arg: float, /) -> None: ...

    @property
    def denoised(self) -> bool:
        """Whether the input Sv is denoised."""

    @denoised.setter
    def denoised(self, arg: bool, /) -> None: ...

    @property
    def incidence_angle_deg(self) -> float:
        """Incidence angle (deg) for the echo-length filter."""

    @incidence_angle_deg.setter
    def incidence_angle_deg(self, arg: float, /) -> None: ...

    @property
    def n_ping_smoothing(self) -> int:
        """Neighbouring pings used for cross-ping mask smoothing (1 = off)."""

    @n_ping_smoothing.setter
    def n_ping_smoothing(self, arg: int, /) -> None: ...

    @property
    def mask_fill_fraction(self) -> float:
        """Majority-filter fill fraction (0..1)."""

    @mask_fill_fraction.setter
    def mask_fill_fraction(self, arg: float, /) -> None: ...

    @property
    def remove_outliers(self) -> bool:
        """Reject cross-ping outliers (robust MAD)."""

    @remove_outliers.setter
    def remove_outliers(self, arg: bool, /) -> None: ...

    @property
    def outlier_window(self) -> int:
        """Half-width (pings) of the outlier median window."""

    @outlier_window.setter
    def outlier_window(self, arg: int, /) -> None: ...

    @property
    def outlier_threshold(self) -> float:
        """Outlier threshold in multiples of the MAD."""

    @outlier_threshold.setter
    def outlier_threshold(self, arg: float, /) -> None: ...

    @property
    def interpolate_gaps(self) -> bool:
        """Interpolate the bottom across short invalid gaps."""

    @interpolate_gaps.setter
    def interpolate_gaps(self, arg: bool, /) -> None: ...

    @property
    def max_interpolation_gap(self) -> int:
        """Maximum interpolated gap length (pings)."""

    @max_interpolation_gap.setter
    def max_interpolation_gap(self, arg: int, /) -> None: ...

    def __eq__(self, other: BottomDetector) -> bool: ...

    def get_bottom(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """Detected bottom sample index per added ping (NaN where no bottom)."""

    def get_bottom_backscatter(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        Surface backscatter (dB) at the detected bottom per added ping (NaN where none).
        """

    def reset(self) -> None:
        """Clear all accumulated state so a new ping sequence can be started."""

    def __len__(self) -> int: ...

    def copy(self) -> BottomDetector:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BottomDetector: ...

    def __deepcopy__(self, arg: dict, /) -> BottomDetector: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    @overload
    def add_ping(self, sv_db: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], range_offset: float, range_resolution: float, pulse_nsamples: float, beamwidth_deg: float) -> None: ...

    @overload
    def add_ping(self, sv_db: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], range_offset: float, range_resolution: float, pulse_nsamples: float, beamwidth_deg: float) -> None:
        """
        Add one ping of Sv data (dB) to the detector.

        Range geometry is the affine range = range_offset + range_resolution * sample. Call get_bottom() / get_bottom_backscatter() afterwards to run the cross-ping detection and read the detected track.
        """
