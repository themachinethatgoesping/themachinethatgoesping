"""
Tidy, on-disk cross-calibration dataset and its analysis API.

A cross-calibration dataset compares a *base* echogram (e.g. a vertical
single-beam echosounder) against many *beam* echograms (e.g. individual
multibeam beams) over fixed time blocks and named range layers. This module
stores that comparison in a compact, portable, **append-able** layout and
exposes a clean analysis API (per-range calibration with bootstrap CIs,
cross-plot data, and cheap splitting by station / environmental parameter).

On-disk layout (a directory, written incrementally so processing is resumable)::

    <root>/
        meta.json            # base name, deltaT, reference, layer config, ...
        params.parquet       # per-time-block params (temperature, station, ...)
        beams/
            manifest.json     # [{file, channel, angle}, ...]
            <channel>=<angle>.parquet   # one long table per (channel, angle)

Each beam table is long over ``(time, layer)`` with columns
``unixtime, layer, range_beam, range_base, depth,
base_value, base_count, beam_value, beam_count``.

The base/beam *values* are per-block reductions (median by default) of the
acoustic samples inside the layer; the *counts* are the number of contributing
samples and drive the fill-based filtering.
"""

import np
import pd


BEAM_COLUMNS: list = ...

def beam_filename(channel: str, angle: float) -> str:
    """Filesystem-safe ``<channel>=<angle>.parquet`` name for one beam."""

class CalibrationStore:
    """Read/write helper for the on-disk calibration directory layout."""

    def __init__(self, root): ...

    def init(self, meta: dict) -> None: ...

    def write_meta(self, meta: dict) -> None: ...

    def read_meta(self) -> dict: ...

    def write_params(self, df: pd.DataFrame) -> None: ...

    def read_params(self) -> Optional[pd.DataFrame]: ...

    def read_manifest(self) -> List[dict]: ...

    def write_beam(self, channel: str, angle: float, df: pd.DataFrame) -> None: ...

    def has_beam(self, channel: str, angle: float) -> bool: ...

    def read_beam(self, fname: str) -> pd.DataFrame: ...

class CalibrationData:
    """
    Analysis view over a cross-calibration dataset.

    Open an existing dataset with :meth:`open`. Splitting methods
    (:meth:`filter_time`, :meth:`split_by_param`, :meth:`split_by_label`)
    return lightweight views that share the underlying (cached) beam tables but
    restrict the time blocks considered -- so comparing e.g. per-station or
    per-temperature calibration is cheap and never copies the heavy data.
    """

    def __init__(self, store: CalibrationStore, meta: dict, params: Optional[pd.DataFrame], beams: Dict[Tuple[str, float], _Beam]): ...

    @classmethod
    def open(cls, path) -> 'CalibrationData':
        """
        Open a dataset directory written by :class:`~.builder.CalibrationBuilder`.
        """

    @property
    def base_name(self) -> str: ...

    @property
    def deltaT(self) -> str: ...

    @property
    def reference(self) -> str: ...

    @property
    def channels(self) -> List[str]: ...

    def angles(self, channel: str) -> np.ndarray: ...

    @property
    def beams(self) -> List[Tuple[str, float]]: ...

    @property
    def layers(self) -> List[str]: ...

    @property
    def params(self) -> pd.DataFrame: ...

    @property
    def time(self) -> pd.DatetimeIndex: ...

    def param(self, name: str) -> pd.Series: ...

    def beam(self, channel: str, angle: float) -> pd.DataFrame:
        """Long table for one beam, restricted to the current time mask."""

    def find_closest_angle(self, channel: str, angle: float) -> float: ...

    def find_closest_angles(self, channel: str, angles: Iterable[float]) -> List[float]: ...

    def filter_time(self, t0=None, t1=None) -> 'CalibrationData':
        """View restricted to ``t0 <= time <= t1`` (each bound optional)."""

    def split_by_param(self, name: str, ranges: Sequence[Tuple[str, float, float]]) -> Dict[str, 'CalibrationData']:
        """
        Split into views by value ranges of a numeric param.

        ``ranges`` is a list of ``(label, low, high)``; a block is included when
        ``low <= param <= high``.
        """

    def split_by_label(self, name: str) -> Dict[str, 'CalibrationData']:
        """Split into one view per distinct value of a categorical param."""

    def exclude_label(self, name: str, label) -> 'CalibrationData':
        """View with all blocks of ``param == label`` removed."""

    def calibration_per_range(self, channel: str, angle: float, *, min_count_fraction: float = 0.66, iqr_filter: bool = True, iqr_k: float = 1.5, bootstrap: int = 100, confidence_level: float = 0.95, random_state: Optional[int] = 42) -> pd.DataFrame:
        """
        Per-layer calibration offset ``C = base - beam`` for one beam.

        Pipeline (matching the validated notebook approach):

        1. **Fill filter** -- per side, drop blocks whose sample count is below
           ``min_count_fraction * median(positive counts)`` (computed on the
           full, unsplit beam so splits stay comparable).
        2. **Outlier filter** -- optional 1.5*IQR fence on the per-block
           difference ``C`` within each layer.
        3. **Reduce** -- median ``C`` per layer with a bootstrap CI.

        Returns a frame indexed by layer with ``range_beam, range_base, depth,
        csv`` (median offset), ``ci_low, ci_high, n``.
        """

    def cross_data(self, channel: str, angle: float, layer: str, *, min_count_fraction: float = 0.66, iqr_filter: bool = True, iqr_k: float = 1.5) -> pd.DataFrame:
        """
        Per-block ``base``/``beam`` values for one layer (for cross-plots).

        Returns a frame with ``base, beam, diff, inlier`` columns (fill-filtered;
        ``inlier`` marks the 1.5*IQR-accepted points used for the offset).
        """

    def series(self, channel: str, angle: float, layer: str) -> pd.DataFrame:
        """Raw per-block time series for one layer (base/beam value+count)."""

    def __repr__(self) -> str: ...
