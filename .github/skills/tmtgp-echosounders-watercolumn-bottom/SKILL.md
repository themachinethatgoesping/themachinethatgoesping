---
name: tmtgp-echosounders-watercolumn-bottom
description: 'Recipe for the SIXTH implementation step of an echosounder file format in themachinethatgoesping/echosounders: implement the ping WATER COLUMN + BOTTOM accessors (I_PingWatercolumn / I_PingBottom overrides), a <Fmt>WaterColumnCalibration (+ MultiSector) so raw amplitudes AND converted amplitudes (av/pv/rv, i.e. uncalibrated Sv) are available, substruct caching of the per-ping records (lazy load/release + flyweight calibration), so pingprocessing EchogramBuilder.from_pings + widgets WCIViewerQt / EchogramViewerQt can display the pings. Follows tmtgp-echosounders-ping-interface (pings + file_data grouping already work). Worked example: s7k (7042 CompressedWaterColumn amplitudes, 7027 RawDetection angles/bottom, 7000 SonarSettings sample rate / sound speed / TVG). Reference: kmall (KMALLPingWatercolumn / KMALLPingBottom / KMALLWaterColumnCalibration / _sub/WaterColumnInformation). See tmtgp-cpp-class-style, tmtgp-cpp-nanobind-style, tmtgp-build-and-test, tmtgp-ping-jupyter.'
---

# Ping water column + bottom + calibration (format step 6 of N)

Goal: after this step `fh.get_pings()` pings expose a working `ping.watercolumn` and `ping.bottom`,
so `theping.pingprocessing.watercolumn.echograms.EchogramBuilder.from_pings(pings)` +
`set_x_axis_date_time()` + `set_y_axis_depth()` + `build_image()` produces an echogram, and
`pingprocessing.watercolumn.image.make_wci.make_wci(ping, px)` produces a water-column image (the
`widgets.EchogramViewerQt` / `WCIViewerQt` inputs). Raw amplitudes **and** converted amplitudes
(av/pv/rv) are available. Follows **tmtgp-echosounders-ping-interface**. Reference: **kmall**
(`KMALLPingWatercolumn`, `KMALLPingBottom`, `filedatatypes/calibration/kmallwatercolumncalibration`,
`_sub/watercolumninformation`). Worked example: **s7k**. Build/validate with tmtgp-build-and-test;
run/verify in a fresh `mamba run python` (see tmtgp-ping-jupyter — the notebook kernel won't reload).

## The minimal set the builders call (implement these)
`EchogramBuilder.from_pings` / `make_wci` (via `make_image_helper.get_bottom_directions_wci`,
`ping_backend`, `select_get_wci_image`) call, on `ping.watercolumn`:
`has_amplitudes`, `get_number_of_beams`, `get_beam_crosstrack_angles(sel)`,
`get_beam_alongtrack_angles(sel)`, `get_sample_interval`, `get_number_of_samples_per_beam(sel)`,
`get_first_sample_offset_per_beam`, `get_sound_speed_at_transducer`, `get_amplitudes(sel,mp)`,
`get_bottom_range_samples(sel)`, `get_tx_signal_parameters` (+ `get_tx_sector_per_beam`),
`get_number_of_tx_sectors`, `has_av/has_rv/...` + `get_wci(sel, o_calibration_type)`; the base
`get_beam_sample_selection_all()` is computed from the geometry getters. On `ping.bottom` (only for
`apply_pss_to_bottom` / a bottom overlay): `has_xyz`, `has_beam_crosstrack_angles`,
`get_number_of_beams`, `get_beam_crosstrack_angles(sel)`, `get_two_way_travel_times(sel)`,
`get_xyz(sel)`. **These overrides are virtual on the bound base `I_PingWatercolumn`/`I_PingBottom` —
no new nanobind bindings are needed** (the `nb::class_<<Fmt>PingWatercolumn, I_PingWatercolumn>`
from step 3 inherits them and dispatches to your C++).

## Where the data comes from (s7k example)
- **amplitudes**: 7042 CompressedWaterColumn. Keep the samples in their **native integer type** (a
  per-encoding `std::variant`, see tmtgp-echosounders-record-parsers) and assemble the *selected*
  beams/samples into a 2D ensemble with a templated helper (mirror kmall `get_raw_amplitudes`'s
  `rsr = selection.get_read_sample_range(out_bn, first_sample, n_samples)` loop; per-beam
  `xt::view(out,bn,range) = xt::view(native_samples, sample_range)` casts on assignment). Then do the
  **dB conversion once, deferred and vectorized** on the assembled 2D array (`container.
  convert_magnitude_to_db(raw_float_2d)` — 16-bit `20*log10(mag/65535)`, 8-bit already-dB pass through)
  so only used samples are converted (xsimd). **Sanitize** `20*log10(0) = -inf` to NaN via
  `xt::where(xt::isfinite(x), x, NaN)` or the echogram min/max break. Expose the s7k-specific
  `get_raw_amplitudes()` (native uint), `get_raw_phase()` (int16) and `get_phase()` (float degrees)
  overloads (no-arg + `(BeamSampleSelection)`) alongside the base `get_amplitudes` override.
- **sample interval** = `1 / 7042.get_sample_rate()`; **sound speed** = `7000.get_sound_velocity()`;
  **first sample offset** = `7042.get_first_sample()` (record-wide, broadcast); **samples per beam**
  = the 7042 container `get_sample_count_tensor()`.
- **beam crosstrack angles** + **bottom range samples**: 7027 RawDetection (`get_rx_angle_in_degrees`,
  `get_detection_point`). s7k has **no clean beam-geometry record** here, so the detection angles are
  the angle source. **alongtrack angle**: broadcast the tx steering (`7027.get_tx_angle_in_degrees`).
- **bottom** (7027): `get_number_of_beams`, `get_beam_crosstrack_angles` = rx angle,
  `get_two_way_travel_times` = `detection_point / sampling_rate`. **`has_xyz()` = false** (s7k raw
  detections carry no ready-made XYZ — provide angles + travel times as best guesses; raytracing later).

## Calibration: raw + converted amplitudes (av = uncalibrated Sv)
Build `<Fmt>WaterColumnCalibration : filetemplates::datatypes::calibration::WaterColumnCalibration`
(mirror `KMALLWaterColumnCalibration`) + `using <Fmt>MultiSectorWaterColumnCalibration =
T_MultiSectorCalibration<<Fmt>WaterColumnCalibration>;`. `setup_<fmt>_calibrations()` builds
`_power_calibration`/`_ap_calibration`/`_av_calibration` as `AmplitudeCalibration(-system_gain_offset)`
(+ av gets `-10*log10(effective_pulse_duration * sound_velocity / 2)`, the volume factor). Serialize
the 3 extra floats (`sound_velocity`, `effective_pulse_duration`, `system_gain_offset`) after
`WaterColumnCalibration::to_stream`. The ping's `<Fmt>PingFileData::init_watercolumn_calibration()`
builds one calibration per sector into a `boost::flyweight<<Fmt>MultiSectorWaterColumnCalibration>`.

The base `get_wci(sel, o_calibration_type)` / `get_av` etc. dispatch to `get_calibrated_wci<type>`
which, for **one sector**, calls `get_watercolumn_calibration().apply_beam_sample_correction<type>(
get_amplitudes, get_beam_crosstrack_angles, get_approximate_ranges, mp_cores)`. So expose (single
sector): `get_number_of_tx_sectors()==1`, `get_watercolumn_calibration()` (sector 0),
`get_multisectorwatercolumn_calibration()`, and `has_watercolumn_calibration()`.

### The calibration availability rules (cost real debugging time)
- `get_wci(sel, value)` only accepts the **9 calibration types** `power/rp/rv/pp/pv/ap/av/sp/sv` —
  there is **NO `"amp"`** (it throws "Invalid calibration type"). The echogram default
  `wci_value="sv/av/pv/rv"` picks the first *available* one, so you must make **≥1** of them available.
- `has_av/ap/sp/sv/pv/pp` additionally require **`has_valid_absorption_db_m()`** → you MUST
  `cal.set_absorption_db_m(absorption)` for `av` to be available. `has_rv/rp/power` need **no**
  absorption (only `has_power_calibration()`), so `rv` is the easiest converted output to light up.
- **TVG that is already applied to the recorded data** goes into the ctor's `tvg_absorption_db_m` +
  `tvg_factor`; the *target* correction is chosen by the calibration type (20 log r for volume
  av/sv/pv/rv, 40 for point). s7k stores the applied log-range factor in
  `7000.get_spreading()` (e.g. 40 or 0) → `tvg_factor = get_spreading()`; absorption
  `7000.get_absorption()` is **dB/km → *0.001** for dB/m. Setting applied == to-apply makes absorption
  a no-op change and av just corrects the (20 − spreading)·log r difference — a sane first guess.
- **Sv semantics**: `sv` = calibrated volume backscattering strength (needs a real system/beam
  calibration → leave it unavailable). `av` = amplitude-derived, *uncalibrated* Sv — the "best guess
  of Sv with no calibration". `power/rv/pv` = power-derived. Document that `av` is the uncalibrated Sv.

## Substruct caching (mirror kmall)
`<Fmt>PingFileData` lazily caches the per-ping records so the many geometry/amplitude calls don't
re-read: `std::unique_ptr<...> _sonar_settings/_raw_detection/_water_column` +
`get_sonar_settings()/get_raw_detection()/get_water_column()` (build on first access);
`load_wci()/release_wci()/wci_loaded()` for the large water-column record (the ping `load()/release()`
manage it so the echogram over all pings stays bounded); `boost::flyweight<...MultiSectorCalibration>`
for the calibration. **unique_ptr members are not copyable → add a copy constructor** that deep-copies
each cached pointer (mirror `KMALLPingFileData`). A `read_first_datagram<t_datagram>()` helper
(`this->get_datagram_infos_by_type(t::DatagramIdentifier).at(0)->read_datagram_from_file<t>()`) reads
the ping's first record of a type.

## Gotchas that cost real debugging time
1. **`using t_base1::get_x;` for every selection-taking override** (`get_beam_crosstrack_angles`,
   `get_number_of_samples_per_beam`, `get_tx_sector_per_beam`, `get_bottom_range_samples`, …) — the
   selection overload otherwise **hides** the base no-arg convenience overload and code that calls
   `watercolumn().get_number_of_samples_per_beam()` (0-arg, e.g. pingcontainer) fails to compile.
2. **Fully qualify base calibration return types in overrides**:
   `const filetemplates::datatypes::calibration::WaterColumnCalibration&` /
   `...::I_MultiSectorCalibration&` — inside `<fmt>::filedatatypes` an unqualified `calibration::` binds
   to *your* `<fmt>::filedatatypes::calibration` namespace.
3. **Multi-detect records**: a bottom-detection record may hold **several detections per beam** (s7k
   7027: 571 rows for 512 beams, keyed by a per-row `beam_descriptor`). Reduce to **one value per beam
   number** (first detection) before indexing by beam number, or angles/ranges are misaligned.
4. **The WCI interpolator needs STRICTLY increasing beam angles.** Quantized receive angles repeat for
   adjacent (outer) beams → the interpolator's `_check_XY` throws
   `"X list contains XType x values!"` (= duplicate X). If the angles are sorted-non-decreasing with
   duplicates, **nudge duplicates by a tiny epsilon** (e.g. `+1e-3°`, drift < 0.1°) so they are strictly
   increasing. (A non-monotonic set, not just duplicates, means the beam numbering is not angular and
   needs a real beam-geometry source — flag it.)
5. **`get_tx_signal_parameters()` is required by the echogram backend** (`main_frequency` /
   `main_pulse_duration`). Return one `CWSignalParameters(center_freq, bandwidth, pulse_width)` per
   sector from the settings record; also implement `has_tx_signal_parameters`.
6. **A ping missing a record must not throw from a `has_*`/getter used by the builder.** Guard the
   calibration/sound-speed on a missing settings record (return NaN / build a power-only calibration),
   and in `read_pings` **drop records before the first sonar-settings record** (an incomplete leading
   ping otherwise lacks the settings/detection records and crashes beam-angle selection).
7. **Lazy-init the calibration in the `get_[multisector]watercolumn_calibration()` overrides**
   (`_file_data->init_watercolumn_calibration()`), because the builder calls `has_av`/`get_wci` without
   calling `ping.load()` first.

## Validate on real data (fresh process, NOT the notebook kernel)
```python
pings = theping.pingprocessing.filter_pings.by_features(fh.get_pings(), ['watercolumn.amplitudes'])
p = pings[len(pings)//2]
wc = p.watercolumn
assert wc.has_amplitudes() and wc.has_av() and wc.has_rv()
sel = wc.get_beam_sample_selection_all()
amp = np.asarray(wc.get_amplitudes(sel));  av = np.asarray(wc.get_av(sel))   # dB, sane range
from themachinethatgoesping.pingprocessing.watercolumn.image.make_wci import make_wci
wci, extent = make_wci(p, 600)                                              # WCIViewer image
eg = theping.pingprocessing.watercolumn.echograms.EchogramBuilder.from_pings(pings, verbose=False)
eg.set_x_axis_date_time(max_steps=400); eg.set_y_axis_depth(max_steps=400)
image, ext = eg.build_image()                                              # (image, extent) tuple!
```
Sanity: amplitudes/av finite fraction high, dB ranges sane; `make_wci` finite ≳ 0.5; the echogram
depth rows mostly filled (time columns can be sparse if the pings span time-separated files). The Qt
`WCIViewerQt`/`EchogramViewerQt` consume exactly these (make_wci + the echogram builder), so they will
display; they need `%gui qt6` and cannot be tested headless.

## Next steps
Set a real system/beam calibration so `sv`/`sp` become available; multi-sector tx; a proper
beam-geometry source (real beamforming angles instead of nudged detection angles); bottom XYZ via
raytracing.
