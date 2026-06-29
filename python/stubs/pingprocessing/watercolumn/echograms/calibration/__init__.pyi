"""
Cross-calibration of echograms: build, analyse, model.

This subpackage replaces the old ``LayerProcessor`` workflow with a clean,
fast, resumable pipeline:

* :class:`CalibrationBuilder` -- extract a base-vs-beam comparison from
  echograms into a compact, append-able on-disk dataset (Parquet).
* :class:`CalibrationData` -- open such a dataset and analyse it (per-range
  calibration with bootstrap CIs, cross-plot data, cheap splitting by station
  or environmental parameter).
* :class:`CalibrationPattern` -- fit a per-channel ``offset(angle, range)``
  surface and apply it back onto multibeam pings.
* :mod:`models` / :mod:`plotting` -- curve-fit models and plotting helpers.

Quick start
-----------
::

    from themachinethatgoesping.pingprocessing.watercolumn.echograms.calibration import (
        CalibrationBuilder, CalibrationData, CalibrationPattern)

    b = CalibrationBuilder('calib.dir', sbes_echo, base_name='EK80',
                           ranges=range(1, 31), deltaT='1min')
    b.add_beam('TRX-2004', 0.0, mbes_beam_echo)
    b.add_param('temperature', times, temps)

    data = CalibrationData.open('calib.dir')
    table = data.calibration_per_range('TRX-2004', 0.0)

    pattern = CalibrationPattern().fit(data)
"""

from . import (
    builder as builder,
    data as data,
    models as models,
    pattern as pattern,
    plotting as plotting
)
from .builder import CalibrationBuilder as CalibrationBuilder
from .data import (
    CalibrationData as CalibrationData,
    CalibrationStore as CalibrationStore
)
from .models import (
    CalibrationModel as CalibrationModel,
    LogisticSTR as LogisticSTR,
    PchipBlendChangePoint as PchipBlendChangePoint
)
from .pattern import CalibrationPattern as CalibrationPattern


__all__: list = ['CalibrationBuilder', 'CalibrationData', 'CalibrationStore', 'CalibrationPattern', 'CalibrationModel', 'PchipBlendChangePoint', 'LogisticSTR', 'plotting']
