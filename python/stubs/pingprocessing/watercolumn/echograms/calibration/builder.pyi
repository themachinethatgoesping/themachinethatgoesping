"""
Build a cross-calibration dataset from a base + many beam echograms.

:class:`CalibrationBuilder` takes one *base* echogram (the reference, e.g. a
vertical single-beam echosounder) and lets you add *beam* echograms one at a
time (e.g. individual multibeam beams). For each beam it:

1. defines the range-band layers on the beam echogram (intersected with the
   beam's ``valid`` mask),
2. transfers each band to the base echogram through a shared physical
   reference (depth) so the base measures the *same physical extent*
   (intersected with the base's ``valid`` mask),
3. pools both echograms' layer samples into shared time blocks (fast), and
4. writes that beam's long table to disk immediately.

Because every beam is written as soon as it is computed, the process is
**resumable**: stop any time and re-run later with more (or finer) beam angles;
already-computed beams are skipped. Shared per-block parameters (temperature,
focus range, station label, ...) are written once and reused by every beam.
"""

from themachinethatgoesping.pingprocessing.watercolumn.echograms.calibration.data import (
    CalibrationData as CalibrationData,
    CalibrationStore as CalibrationStore
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.layers.layer import (
    Layer as Layer
)
from themachinethatgoesping.pingprocessing.watercolumn.echograms.layers.transfer import (
    transfer_layer as transfer_layer
)


class CalibrationBuilder:
    """
    Incrementally build a cross-calibration dataset on disk.

    Parameters
    ----------
    path:
        Output directory (created/extended). Re-opening an existing directory
        resumes it.
    base_echogram:
        The reference echogram, shared by every beam comparison.
    base_name:
        Display name for the base channel (stored in metadata).
    ranges:
        Range-band centres (m) on the beam echogram, e.g. ``np.arange(1, 31)``.
    layer_size:
        Range-band thickness (m); each band is ``r +/- layer_size/2``.
    deltaT:
        Time-block size (``'1min'`` or seconds).
    base_mask, beam_mask:
        Layer names of the per-echogram ``valid`` masks to intersect into every
        band (``None`` to skip).
    layer_reference:
        Reference the range bands are defined in on the *beam* echogram
        (``'Range (m)'`` by default -- multibeam beams are banded in slant
        range; use ``'Depth (m)'`` for vertical setups).
    reference:
        Physical reference used to transfer bands base_-beam (depth).
    step:
        Ping stride for pooling (``1`` = every ping).
    reduce:
        Block reducer for pooled samples (default median).
    """

    def __init__(self, path, base_echogram, *, base_name: str = 'base', ranges: Sequence[float] = ..., layer_size: float = 1.0, deltaT: Union[str, float] = '1min', base_mask: Optional[str] = 'valid', beam_mask: Optional[str] = 'valid', layer_reference: str = 'Range (m)', reference: str = 'Depth (m)', step: int = 1, reduce=..., time_extent: Optional[Tuple[float, float]] = None, show_progress: bool = True): ...

    def has_beam(self, channel: str, angle: float) -> bool: ...

    def add_beam(self, channel: str, angle: float, beam_echogram, *, overwrite: bool = False, show_progress: Union[bool, object, None] = None) -> None:
        """Extract and store one beam comparison (skipped if already present)."""

    def add_beams(self, channel: str, beam_echograms: Dict[float, object], *, overwrite: bool = False, show_progress: Optional[bool] = None) -> None:
        """Convenience: add several ``{angle: echogram}`` beams of one channel."""

    def add_param(self, name: str, times, values, *, reduce=None, interpolate: bool = True) -> None:
        """
        Pool an external ``(times, values)`` series into the block grid.

        Parameters are first binned by time block (using ``reduce`` for blocks
        with multiple samples) and then linearly interpolated across block
        centers by default.
        """

    def add_intervals(self, name: str, intervals: Iterable[Tuple[str, object, object]]) -> None:
        """
        Label each block by the first ``(label, t0, t1)`` interval it falls in.
        """

    def result(self) -> CalibrationData:
        """Open the (current) on-disk dataset as a :class:`CalibrationData`."""

    def add_calibration_layers(self, beam_echogram, *, base_echogram=None, ranges: Optional[Sequence[float]] = None, apply_masks: bool = True):
        """
        Add the calibration range bands as named layers for verification.

        Adds exactly the layers ``add_beam`` pools (same band + transfer code) to
        both echograms and returns ``(beam, base)`` so values can be checked with
        the normal layer mechanism (``get_wci_layers``, ``build_image_and_layer_images``,
        ``get_layer_bounds``). The pooled calibration medians equal the per-block
        medians of these layers.

        Parameters
        ----------
        beam_echogram:
            The beam echogram to band (e.g. one MBES beam).
        base_echogram:
            Base echogram to add the matching transferred bands to (defaults to
            the builder's base).
        ranges:
            Which bands to add (e.g. ``[1, 5, 10]``); ``None`` uses all builder ranges.
        apply_masks:
            Intersect the configured ``valid`` masks (matches ``add_beam``).

        Returns
        -------
        (beam, base):
            The two echograms with bands ``"1m"``, ``"5m"``, ... added. The
            analytic geometry per band is also stored in ``last_layer_geometry``.

        Example::

            beam, sbes = builder.add_calibration_layers(mbes_beam, ranges=[1, 5, 10])
            beam.get_wci_layers(0)["5m"]   # samples used for the 5 m band, ping 0
        """

    def __repr__(self) -> str: ...
