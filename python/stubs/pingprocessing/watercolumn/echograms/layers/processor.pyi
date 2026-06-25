"""
Aggregate layer acoustic values over time blocks across echograms.

This is a clean redesign of the old ``LayerProcessor``. Given one or more
echograms that share named layers, it pools the acoustic samples that fall
inside each layer into fixed-length time blocks and reduces them (median by
default) to a tidy :class:`pandas.DataFrame`. Typical use is inter-echosounder
comparison / calibration, where one echogram is the reference and others are
compared against it per layer (e.g. per range band).

Design notes
------------
* Echograms are passed as ``{name: echogram}``; nothing is mutated on them.
* Layers are referenced by name and resolved per echogram (so the same layer
  name may cover a different physical band on each echogram -- which is exactly
  what you want after transferring a layer between echograms).
* The per-ping sample extraction loop is unavoidable (data is read per ping),
  but layer sample-index resolution and block assignment are vectorized.
"""

import pd


class LayerProcessor:
    """
    Pool layer samples into time blocks and reduce them per echogram.

    Parameters
    ----------
    echograms:
        ``{name: echogram}`` mapping (or a single echogram). All echograms must
        expose the requested layer names.
    layers:
        Layer names to process. ``None`` uses the layers common to every
        echogram.
    deltaT:
        Time-block size (e.g. ``'1min'``, ``'30s'``) or seconds as a number.
    step:
        Ping stride for extraction (``1`` = every ping).
    reduce:
        Block reducer applied to the pooled samples: a name
        (``'median'``/``'mean'``/...) or a callable ``f(values)->scalar``.
    min_count:
        Blocks with fewer than this many finite samples are set to NaN.
    show_progress:
        ``True``/``False`` or an existing tqdm instance.
    """

    def __init__(self, echograms: Union[Dict[str, object], Sequence, object], *, layers: Optional[Sequence[str]] = None, deltaT: Union[str, float] = '1min', step: int = 1, reduce: Union[str, Callable] = 'median', min_count: int = 1, show_progress: Union[bool, object] = True): ...

    @property
    def data(self) -> pd.DataFrame:
        """The tidy result frame (one row per time block)."""

    @property
    def layers(self) -> List[str]: ...

    @property
    def names(self) -> List[str]: ...

    @property
    def times(self) -> pd.DatetimeIndex: ...

    def value(self, layer: str, name: str) -> pd.Series:
        """Reduced layer value series for ``layer`` on echogram ``name``."""

    def count(self, layer: str, name: str) -> pd.Series:
        """Sample-count series for ``layer`` on echogram ``name``."""

    def difference(self, layer: str, name_a: str, name_b: str) -> pd.Series:
        """``value(layer, name_a) - value(layer, name_b)`` (e.g. calibration)."""

    def calibration_per_range(self, name_a: str, name_b: str, *, layers: Optional[Iterable[str]] = None, bootstrap_resamples: int = 100, confidence_level: float = 0.95, min_count: Optional[int] = None, show_progress: bool = True) -> pd.DataFrame:
        """
        Median difference (``name_a - name_b``) per range-band layer.

        Layers are interpreted by parsing a leading number from their name
        (``'12.0m'`` -> range 12.0 m). Returns a frame indexed by range with
        the median difference and a bootstrap confidence interval.
        """

    def __repr__(self) -> str: ...
