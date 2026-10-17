---
name: tmtgp-echosounders-lessons-learned
description: 'Hard-won, echosounder-specific gotchas and techniques for implementing or extending a file-format reader in themachinethatgoesping/echosounders (s7k, kmall, kongsbergall, simradraw, gsf): datagram header/identifier indexing & UTF-8-safe identifier printing, file-data interface init-order traps, on-disk binary record layout (packing, the Windows/MSVC bind_vector operator== SIMD rule, the fast substruct+container read pattern, skip_data), navigation unit/sign-convention conversion & record preference, ping grouping and the raw-detection (I_MBESRawDetectionInfos) interface, water-column/bottom/calibration pitfalls (strictly-increasing beam angles, zero-range-beam WCI crash), and debugging the WCI/Echogram viewers. USE when writing or debugging any echosounder format reader. For the layered architecture + build order see tmtgp-echosounders-add-format; for class/binding/build mechanics see tmtgp-cpp-class-style, tmtgp-cpp-nanobind-style, tmtgp-build-and-test. Reference implementations: kmall / kongsbergall (complete), s7k (recent), gsf (minimal).'
---

# echosounders: lessons learned (gotchas that cost real debugging time)

Companion to **tmtgp-echosounders-add-format** (architecture + build order). Everything below is a
fact that was learned the hard way; **mirror kmall/kongsbergall** for the surrounding boilerplate and
only reach for these when the thing they warn about bites. Validate every claim on **real data** in a
**fresh python process** (a rebuilt C++/nanobind module is NOT picked up by a running Jupyter kernel —
see tmtgp-ping-jupyter).

## 1. Datagram header + identifier indexing
- **Fixed headers rely on no struct padding.** Order members so every field is naturally aligned and
  read the whole header in one `is.read(reinterpret_cast<char*>(&first), size)`; add a parse test that
  asserts real field values to catch layout mistakes. `skip()` / raw-content length must use the
  header's own total-size field consistently so the scan lands exactly on the next datagram (a wrong
  offset surfaces as a "read incompletely" warning).
- **Keep the `I_DatagramInterface` map key + the virtual `datagram_identifier_*` signature the plain
  enum** so unknown record types still index. Use the `o_<Fmt>DatagramIdentifier` `OptionFrozen`
  wrapper only as the *working* identifier (members, `from_stream` params, the Python `datagrams(...)`
  argument). `o_...(id).name()/.alt_name()` **throw on unknown values** → keep the enum exhaustive or
  guard with `enum_contains()`.
- **Identifier→string conversions must emit valid UTF-8 and never throw** — they run over EVERY
  datagram, including record types not in the enum. There are **TWO** paths and a passing interface
  print does **not** prove the container print works: the *interface* printer uses the virtual member
  `datagram_identifier_to_string`/`_info`; the *container* printer
  (`fh.datagram_interface.datagrams().print()`) uses the free
  `echosounders::datagram_identifier_to_string(<fmt>::t_...)` in `types.hpp`. **Fix BOTH.** For a
  **numeric-id** format return the DECIMAL string (`std::to_string(uint32_t(id))`); `int_as_string`
  (correct only for 4-char-code formats like kmall/kongsbergall) reinterprets the number's raw bytes →
  invalid UTF-8 → Python `print()`/`info_string()` raise `UnicodeDecodeError` /
  `nanobind::str(): conversion error!`.
- Also provide **plural** `datagram_identifiers_to_string` (a `std::vector<...>` **and** a
  `std::set<...>` overload) in the `echosounders` namespace in `types.hpp` — the base
  `I_FileDataInterfacePerFile::__printer__` calls it via ADL for the linked-file extension sets.
  Missing it fails to compile ("no declarations found by ADL") **only when a PerFile interface printer
  is instantiated**, so the indexing step won't catch it.

## 2. File-data interfaces & file-handler init order
- **Do NOT enable the ping interface init until `read_pings()` is implemented.**
  `I_PingDataInterface::init_from_file` processes file 0 (`_ping_container = process_file(0)`)
  **outside** its try/catch, so a not-implemented `read_pings` throws straight out of the handler
  constructor (which defaults to `init=true`). Navigation/configuration init *are* exception-safe
  (config falls back to an empty config, nav catches per-file) but keep them off too until implemented
  to avoid noisy warnings. Enabling ping init is exactly what implementing `read_pings` unblocks.
- **`read_*` virtuals are virtual-with-default (they throw), not pure** → do NOT override them in the
  interface/ping shells; the classes still instantiate. Same for the `I_PingBottom`/`I_PingWatercolumn`
  getters, so the stubs need no getter overrides.
- **Stub `<Fmt>PingBottom`/`Watercolumn` `__printer__` must NOT append the base
  `I_PingBottom`/`I_PingWatercolumn` printer** — the base queries `get_number_of_beams` /
  `get_number_of_tx_sectors` etc., which are the throwing defaults in a stub. Print a minimal
  `register_string("status", "not implemented yet")`. (`I_Ping::__printer__` is safe — it does not
  recurse into the sub-object printers.)
- **C++ test include depth**: tests resolve `#include "../themachinethatgoesping/..."` via an
  `-I src/tests/` dir → use **one** `../` regardless of the test file's subdirectory depth. Ping-type /
  container bindings need an explicit `#include <.../filetemplates/datastreams/mappedfilestream.hpp>`
  (the s7k headers don't pull it in transitively).

## 3. Per-record parsing & on-disk binary layout
- **Per-beam stride = the on-disk `*_field_size`/`data_field_size` field, NOT the MB-System struct
  `sizeof`.** Read exactly that many bytes per beam and memcpy fields at fixed offsets; fill trailing
  (version-dependent) fields with NaN when the stride is short. (s7k 7027 is 26 bytes on disk, not the
  34 the MB-System struct suggests.) **`nalloc` in MB-System structs is an in-memory counter — never on
  disk.** **Water-column ordering differs per record** (s7k 7028: all beam-headers then concatenated
  samples; 7042: per-beam interleaved, dtype chosen by a flags bit field) — confirm against the spec,
  not a C struct.
- **Pack a `Content`/row struct with `#pragma pack(push,1)` ONLY when its natural C++ layout ≠ the
  on-disk layout**, and always pin it with `static_assert(sizeof(X) == <N>)`. All-naturally-aligned
  records (all-4-byte, e.g. s7k 7610/1000/1012; the DRF header with every reserved field present) need
  **no** pragma — needless packing yields odd `sizeof`s that break MSVC SIMD (next bullet). If a record
  looks oddly sized, check the spec for a missing **reserved** field first.
- **Windows / MSVC-STL SIMD on `bind_vector` rows** (this also lives in tmtgp-cpp-class-style, because
  it is really an `operator==` rule): clang-cl & MSVC route the `std::find/count/remove` that
  `nb::bind_vector` emits (for `__contains__`/`count`/`remove`) through a vectorized path that only
  supports element sizes 1/2/4/8 bytes and `static_assert`-fails otherwise — **but only** for
  "trivially equality comparable" types (all-integer, no padding, *defaulted* `operator==`). So a
  packed all-integer row of size ∉ {1,2,4,8} (e.g. s7k 6-byte `FileHeaderDeviceInfo`, 14-byte
  `SnippetDataBeam`) fails to compile on Windows. Fix = give **just those rows** a *user-provided*
  memberwise `operator==` (not `= default`); this flips `__is_trivially_equality_comparable` to false →
  scalar path, keeps the exact layout, and does not disable SIMD elsewhere. Rows with any float/double
  are never affected.
- **Fast per-beam / per-sample records: substruct + container (PREFERRED over parallel-array loops).**
  Do not re-sort on-disk records into several parallel `xt::xtensor` members field-by-field. Keep the
  in-memory layout as close to on-disk as possible and convert to arrays only on access. Put substructs
  in `datagrams/substructs/` (each substruct and container its own `.hpp`, `.cpp` for the container's
  tensor accessors). Reference: kmall `MRZSoundings`/`MRZSoundingsContainer`, simradraw
  `raw3datatypes/` (variant sample types), s7k `datagrams/substructs/` (7027/7028/7042/7004/1016).
  - **Row substruct (AoS on disk)**: members in on-disk order, `get_/set_`, inline `__printer__`,
    `static_assert(sizeof(Row)==stride)`, `operator==` per the SIMD rule above.
  - **Container**: `std::vector<Row>` + `get_<field>_tensor()` built on demand via a private
    `build_tensor<V>(getter)` (`xt::xtensor<V,1>::from_shape({n})` + `unchecked` loop). The datagram
    holds the container via `def_prop_rw` — no flat arrays on the datagram.
  - **Bulk read straight into final storage, never a scratch buffer + memcpy.** Full-width AoS:
    `vec.resize(n); is.read(vec.data(), n*sizeof(Row))`. Variable stride (`dfs` made `const` before the
    loop): if `dfs==sizeof(Row)` one bulk read, else read each beam into `&vec[i]`
    (`is.read(&vec[i], min(dfs,sizeof(Row)))`, seek the extra when `dfs>sizeof(Row)`, NaN the missing
    version-dependent fields).
  - **SoA on disk** (per-field arrays already contiguous, e.g. s7k 7004): keep the `xt::xtensor<..,1>`
    members **directly on the datagram** and bulk-read each array — do NOT wrap in a container (zero
    read-speed benefit, adds indirection).
  - **Variable-length / water-column samples**: read directly into final per-beam storage. (a)
    contiguous with a datagram-wide dtype (s7k 7028): a flat `std::variant<xtensor<u16,1>,xtensor<u32,1>>`
    + `xtensor<u64,1>` beam offsets, header + sample blocks each one `is.read`. (b) interleaved per-beam
    with flag-driven dtype (s7k 7042): one class per sample encoding in a `std::variant` (mirror
    simradraw `raw3datatypes/`: an `I_<Rec>Data` interface + a concrete type per encoding + a `Skipped`
    default), each beam holds one variant.
- **`skip_data` for big water-column records (kmall parity)**: add `<Fmt>SkipDataFactory<t>` +
  `<Fmt>SkipDataVariantFactory` (mirror `KMALLSkipDataFactory`); give every WC `from_stream` a trailing
  `bool skip_data=false` forwarded to `__read__`, where on skip you read the RTH `_content` then
  `is.seekg(compute_size_content() - __content_size, cur)` to land at record end (sample arrays empty,
  RTH metadata kept — a skipped record cannot be re-serialised). Register `..._<Rec>_SkippedData` and
  `..._Variant_SkippedData` containers; the typed `datagrams(type, skip_data)` WC cases branch on it.
- **Docstring pitfall**: `pybind11_mkdoc` (libclang) **cannot parse getters returning
  `std::vector<xt::xtensor<...>>`** — it aborts the class parse, dropping `DOC()` for that getter and
  every method after it. Use a plain string-literal docstring for those getters and keep them last in
  the class. (General mkdoc mechanics: tmtgp-cpp-nanobind-style / tmtgp-build-and-test.)

## 4. Navigation (`read_navigation_data()` is the only function you implement)
- **`NavigationInterpolatorLatLon` fixes the units/frame — convert each record into them, and verify
  signs against the spec's sign-convention table.** Getting this wrong yields a plausible-but-silently
  wrong georeference. The setters expect:

  | setter | unit | sign |
  |--------|------|------|
  | `set_data_position(t[s], lat[°], lon[°])` | degrees | WGS84 |
  | `set_data_attitude(t[s], pitch[°], roll[°])` | **degrees** | pitch **+bow up**, roll **+port up** |
  | `set_data_heading(t[s], heading[°])` | degrees | **+clockwise, north=0°** |
  | `set_data_heave(t[s], heave[m])` | meters | **+up** |

  - radians→degrees: `value*180/π` (`#include <numbers>`); prefer the record's own `get_x_in_degrees()`.
  - **Heave sign is the field most likely to differ between formats — confirm per spec, never copy.**
    kmall `#SKM`/`#CHE` heave is +down → kmall negates; s7k heave is +up (7k DFD Table 2) → NO flip.
  - Axis naming (s7k X=starboard/Y=forward/Z=up vs ours X=forward/Y=starboard/Z=down) matters only for
    the **offset vectors** in the *configuration* interface; roll/pitch/heave/heading values are
    frame-independent and use the table directly.
- **Prefer the modern fused record, fall back to the legacy per-quantity one.** Expose the choice with
  `bool _prefer_*` members + `get_/set_` (mirror kmall `_prefer_spo_over_cpo`, `_prefer_skm_over_che`).
  s7k: 1015 Navigation ▸ 1003 Position; 1016 Attitude ▸ 1012 RollPitchHeave (1016 has many samples each
  with `delta_time` ms → `t = record_time + delta_time*1e-3`, and carries heading too, like `#SKM`);
  take heading from 1016 when used, else 1015 ▸ 1013 Heading ▸ 1016. Guard `if (times_heading.empty())`
  so you never read a record twice.
- **Copy `sort_and_deduplicate_time_series` verbatim from kmall/kongsbergall** (stable-sort by time,
  drop invalid/≤0, keep first of each duplicate timestamp, rebuild all value vectors in lock-step) —
  robust to unsorted/duplicated per-record timestamps; prefer it over the throw-on-out-of-order
  `packet_timestamp_in_range`.
- Minor: `get_sensor_data(...)` returns a `SensordataLatLonVector`
  (`get_latitudes()/...`, NOT `.latitude`); the `_prefer_*` members live on the **perfile** interface
  so changing them needs `init_from_file(..., force=true)` to rebuild cached interpolators. Add a
  synthetic C++ test (no data file) asserting the `_prefer_*` defaults + a non-empty `__printer__`;
  data-driven nav checks are done in Python.

## 5. Ping grouping + the raw-detection (MBES) interface
- **Group pings from the `DatagramInfo` index only — do NOT parse datagrams to group them** (type +
  position + timestamp are already there; parsing water-column records is slow and needless). File-order
  anchoring assumes each ping starts with its anchor record and is written contiguously; multi-head /
  interleaved-anchor files need grouping on the record `ping_number` (+serial/multiping) instead —
  acceptable to defer. **channel id must be non-empty** (use `"0"` for v1) or the base keys
  `_ping_container_by_channel` on `""`.
- `read_pings` must not call `ping.bottom()`/`watercolumn()` (still throwing) until those are
  implemented — it only fills each ping's datagram index; `ping.get_geolocation()` throws until you set
  navigation + sensor configuration on each ping.
- **`I_PingBottom` and `I_PingWatercolumn` publicly multiple-inherit
  `algorithms::geoprocessing::raytracers2::I_MBESRawDetectionInfos`** (I_PingCommon first in the base
  list) — the format-independent raw-detection view a raytracer consumes (per-transmission / per-sector
  / per-sounding getters, each with `has_*` and `__PING_REGISTER_FEATURE__`). Implement its getters per
  format in `<Fmt>PingBottom`/`Watercolumn` (override the `const BeamSelection&` virtual; add
  `using I_MBESRawDetectionInfos::get_soundings_…;` to un-hide the no-arg overload). The old per-ping
  getters it supersedes were renamed **`…_legacy`** (enum entries + bindings too).
  `ping.bottom.get_mbesrawdetectioninfos()` returns a zero-copy `I_MBESRawDetectionInfos&`;
  `get_mbesrawdetectiondata()` returns an owning snapshot (throws if a field is unimplemented). Expose
  via `py_i_mbesrawdetectioninfos::add_interface<T>(cls)` (nanobind has no multiple inheritance — see
  tmtgp-cpp-nanobind-style).

## 6. Water column + bottom + calibration
- **`using t_base::get_x;` for every selection-taking override** (`get_beam_crosstrack_angles`,
  `get_number_of_samples_per_beam`, `get_tx_sector_per_beam`, `get_bottom_range_samples`, …) or the
  selection overload **hides** the base no-arg overload and 0-arg callers (e.g. pingcontainer) fail to
  compile. **Fully qualify base calibration return types** in overrides
  (`const pingprocessing::datatypes::calibration::WaterColumnCalibration&` /
  `...::I_MultiSectorCalibration&`) — inside `<fmt>::filedatatypes` an unqualified `calibration::` binds
  to *your* namespace.
- **Multi-detect records** (s7k 7027: 571 rows for 512 beams, keyed by a per-row `beam_descriptor`):
  reduce to **one value per beam number** (first detection) before indexing by beam, or angles/ranges
  misalign.
- **The WCI interpolator needs STRICTLY increasing beam angles.** Quantized receive angles repeat for
  adjacent outer beams → `_check_XY` throws `"X list contains XType x values!"`. If the angles are
  sorted-non-decreasing with duplicates, **nudge duplicates by a tiny epsilon** (`+1e-3°`, drift
  <0.1°). A genuinely non-monotonic set means the beam numbering is not angular → needs a real
  beam-geometry source (flag it).
- **A beam with NO bottom detection (reference range 0) crashes `make_wci`** — a *different*
  interpolator than the angle one: the backtracer builds a per-beam range→sample interpolator from
  `{0, range}` (`algorithms/.../backtracers/backtracedwci.hpp` ctor); range `0`/non-finite makes `{0,0}`
  (duplicate X) and aborts the **entire** image. Bites the moment a `PingSampleSelector` limits the
  column to the bottom over the full swath (`select_max_bottom_range_percent(102)` +
  `select_beam_range_by_angles(-90,90,step)`): outer beams have no bottom → range 0. **Guard in both
  places** — clamp non-positive/non-finite ranges to a tiny positive in
  `make_image_helper.get_bottom_directions_wci/_bottom` (Python, live without a rebuild) **and** in the
  `BacktracedWCI` ctor (C++, covers every caller) → a no-bottom beam yields NaN samples instead of
  crashing. Only *some* pings throw, so it looks "chaotic".
- **Builders call `has_*`/getters without `ping.load()` first** → lazy-init the calibration inside the
  `get_[multisector]watercolumn_calibration()` overrides (`_file_data->init_watercolumn_calibration()`),
  guard a missing settings record (NaN / power-only calibration), implement
  `get_tx_signal_parameters()` + `has_tx_signal_parameters` (the echogram backend needs
  `main_frequency`/`main_pulse_duration`), and in `read_pings` **drop records before the first
  sonar-settings record** (an incomplete leading ping lacks settings/detection records and crashes beam
  selection).

## 7. Debugging the WCI / Echogram viewers ("it stops updating" is usually NOT a Qt/paint bug)
The viewers wrap `imagebuilder.build()` in `except Exception`; the autoplay path used to swallow it
silently, so a per-ping build crash (e.g. §6 zero-range beam) looked like a frozen GUI advancing the
ping index with the progress bar stuck "loading" (`WCICore._report_build_error` now surfaces it).
**Reproduce `make_wci_dual_head(ping, ...)` directly** with the user's exact `PingSampleSelector` /
`stack` / `mp_cores` and catch the exception, instead of chasing the GUI/paint/Wayland layer. Closing a
Qt viewer must stop its background work — `WCIViewerQt.cleanup()` (playback timer / autoplay / capture)
runs from `closeEvent`/`__del__`, and `CombinedViewerQt.closeEvent` calls `cleanup()` on every hosted
viewer (embedded viewers never get their own `closeEvent`). Bisect regressions by conda/pixi package
version and by diffing **submodule pointers** between working vs broken superproject commits
(`git diff <good> <bad> -- subprojects/<name>`).
