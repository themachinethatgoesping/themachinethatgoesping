---
name: tmtgp-echosounders-navigation
description: 'Recipe for the FOURTH implementation step of an echosounder file format in themachinethatgoesping/echosounders: implement the navigation data interface, i.e. the per-file read_navigation_data() that turns the indexed position/attitude/heading/heave records into a navigation::NavigationInterpolatorLatLon, and enable its init in the file handler. Covers the ONE function you must write (the base I_NavigationDataInterface caches the interpolators automatically, per sensor-configuration hash, via a boost flyweight), the CRITICAL unit + sign-convention checks against the format spec (interpolator wants degrees / seconds / meters; roll +port up, pitch +bow up, heave +up, heading true north=0), a modern-vs-legacy record preference with toggle flags (mirroring kmall SPO/CPO + SKM/CHE), the sort_and_deduplicate helper, treating an empty sensor configuration as a real one, and validation on real data. Follows tmtgp-echosounders-interfaces (the shells already exist). Worked example: s7k (Navigation 1015 / Attitude 1016 preferred over Position 1003 / RollPitchHeave 1012 / Heading 1013). Reference: kmall (SKM), kongsbergall (add_attitudes). See tmtgp-cpp-class-style, tmtgp-cpp-nanobind-style, tmtgp-build-and-test.'
---

# Navigation data interface: read_navigation_data + interpolator caching (format step 4 of N)

Goal: after this step `fh = <Fmt>FileHandler(files)` builds and caches the navigation interpolators,
so `fh.navigation_interface.get_navigation_interpolator_keys()` returns a hash per unique sensor
configuration and `get_navigation_interpolator(hash)` returns a
`navigation::NavigationInterpolatorLatLon` whose `get_sensor_data(t)` yields sane
lat/lon/heading/pitch/roll/heave. Follows **tmtgp-echosounders-interfaces** (the six interface shells
already exist; here you fill in the navigation one). Reference: **kmall** (`read_attitude_from_skm`,
SPO/CPO + SKM/CHE preferences) and **kongsbergall** (`add_attitudes`). Worked example: **s7k**.

## The ONLY function you implement: `read_navigation_data()`
The base `filetemplates::datainterfaces::I_NavigationDataInterface::init_from_file` does everything
else: it initializes the configuration interface first, calls your per-file
`read_navigation_data()` (through a file-cache wrapper), re-applies the sensor configuration, then
**caches one interpolator per `sensor_configuration.binary_hash()` in a
`std::unordered_map<uint64_t, boost::flyweights::flyweight<NavigationInterpolatorLatLon>>` and
merges/`finalize()`s them**. You do NOT write any caching, merging or interpolator-storage code —
just return a fully populated `NavigationInterpolatorLatLon` for one file.

Override in `<fmt>navigationdatainterfaceperfile.hpp`:
```cpp
navigation::NavigationInterpolatorLatLon read_navigation_data() const final
{
    // Treat the sensor configuration as a real one even if the file has no offsets: an empty
    // SensorConfiguration means zero offsets, which is a valid configuration (it still provides a
    // default target "0", so get_sensor_data / get_navigation_data work).
    navigation::NavigationInterpolatorLatLon navi(
        this->configuration_data_interface_const().get_sensor_configuration(this->get_file_nr()));

    // ... fill the vectors below from the indexed records ...

    sort_and_deduplicate_time_series(times_pos,        latitudes, longitudes);
    sort_and_deduplicate_time_series(times_pitch_roll, pitchs, rolls);
    sort_and_deduplicate_time_series(times_heading,    headings);
    sort_and_deduplicate_time_series(times_heave,      heaves);

    navi.set_data_attitude(std::move(times_pitch_roll), std::move(pitchs), std::move(rolls));
    navi.set_data_heading (std::move(times_heading),    std::move(headings));
    navi.set_data_heave   (std::move(times_heave),      std::move(heaves));
    navi.set_data_position(std::move(times_pos),        std::move(latitudes), std::move(longitudes));
    return navi;
}
```
Read each record with `packet->template read_datagram_from_file<datagrams::<Rec>>()` over
`this->_datagram_infos_by_type.at_const(t_<Fmt>DatagramIdentifier::<Rec>)` (guard with a
`has_datagrams(id)` = `contains(id) && !at_const(id).empty()` helper). `read_navigation_data()` is
`const`; the loop variable is a `const shared_ptr&` but `read_datagram_from_file` mutates the pointee
(the stream), which is allowed — mirror kmall.

## CRITICAL: verify units and sign conventions against the spec
`NavigationInterpolatorLatLon` fixes the units/frame; you must convert each record into them. Getting
this wrong yields a plausible-looking but silently wrong georeference. **The setters (see
`navigation/i_navigationinterpolator.hpp` + `navigationinterpolatorlatlon.hpp`) expect:**

| setter | args (unit) | sign convention |
|--------|-------------|-----------------|
| `set_data_position(t[s], lat[°], lon[°])` | `double`, degrees | WGS84 lat/lon |
| `set_data_attitude(t[s], pitch[°], roll[°])` | `float`, **degrees** | pitch **+ bow up**, roll **+ port up** |
| `set_data_heading(t[s], heading[°])` | `float`, degrees | **+ clockwise, north = 0°** |
| `set_data_heave(t[s], heave[m])` | `double`, meters | **+ upwards** |

Steps before writing conversions:
1. Open the format spec's **sign-convention / coordinate table** and read the sign for roll, pitch,
   heave, heading, and the unit for angles and lat/lon. (s7k: 7k DFD *Table 2 Sign Conventions* —
   Roll +Port Up, Pitch +Bow up, **Heave +Up**, Heading true 0..359.99 north=0; angles in **radians**,
   lat/lon in **radians**.)
2. Map each to the table above. Only apply a conversion where they differ:
   - **radians → degrees**: `value * 180/π` (`#include <numbers>`, `rad_to_deg = 180.0/std::numbers::pi`).
     Prefer the record's own `get_x_in_degrees()` accessor if it exists.
   - **heave sign**: this is the field most likely to differ **between formats**. Kongsberg **kmall**
     `#SKM`/`#CHE` heave is **+down** → kmall negates (`-heave_m`). **s7k** heave is **+up** (Table 2)
     → **matches ours, NO flip**. Never copy the sign from another format's reader — confirm per spec.
3. Roll/pitch/heading sign conventions are the same across Kongsberg and s7k (all +port-up / +bow-up /
   true-north); still confirm, and add a one-line comment citing the spec table next to any (non-)flip.
4. The format's **X/Y/Z axis naming** (e.g. s7k X=starboard Y=forward Z=up vs our X=forward
   Y=starboard Z=down) matters ONLY for the offset vectors in the **configuration** interface (which
   converts them); the roll/pitch/heave/heading **values** are frame-independent physical rotations
   and use the table above directly.

## Record preference (modern fused vs legacy single-quantity)
Most formats store each quantity twice: a modern fused record and a legacy per-quantity record.
Prefer the modern one, but fall back when it is absent. Expose the choice with `bool _prefer_*`
members + `get_/set_` (mirror kmall `_prefer_spo_over_cpo`, `_prefer_skm_over_che`). Selection idiom
(kmall): `bool use_A = _prefer_A; if (use_A && !hasA && hasB) use_A=false; if (!use_A && !hasB &&
hasA) use_A=true; if (use_A && hasA) read_A(); else if (hasB) read_B();`.

s7k mapping (user rule "prefer navigation + attitude over rollpitchheave, heading, position"):
- **position**: 1015 Navigation ▸ 1003 Position (`_prefer_navigation_over_position`, skip grid-coord
  1003 records).
- **roll/pitch + heave**: 1016 Attitude ▸ 1012 RollPitchHeave (`_prefer_attitude_over_rollpitchheave`).
  1016 Attitude holds **many samples per record**, each with a `delta_time` offset (ms) →
  `sample_time = record.get_timestamp() + delta_time * 0.001` (mirror kmall SKM). Read
  roll/pitch/heave **and heading** in one pass over 1016 (it carries heading too, like `#SKM`).
- **heading**: when 1016 is used, take heading from it (consistent, same sensor/timestamps); else
  prefer the fused Navigation (1015) heading, then the dedicated Heading (1013) record, then 1016 as a
  last resort. Guard `if (times_heading.empty())` for the fallback so you never read a record twice.

## `sort_and_deduplicate_time_series` (copy verbatim from kmall/kongsbergall)
A variadic helper `void sort_and_deduplicate_time_series(std::vector<double>& times,
ValueVectors&... values) const`: stable-sort an index permutation by time (invalid = non-finite or
≤0 sorted last), drop invalid timestamps and **keep the first sample of each duplicate timestamp**,
then rebuild `times` and every value vector in lock-step. Prefer this over kmall's
`packet_timestamp_in_range` (which throws on out-of-order) — it is robust to unsorted/duplicated
records and each format's per-record timestamps.

## File handler: enable the init (mirror kmall, but NOT ping)
In `<fmt>filehandler.hpp` `init_interfaces`, add the configuration + navigation inits (leave
environment/other/ping commented until implemented). Navigation's `init_from_file` auto-initializes
the configuration interface, but init it explicitly for the progress bar:
```cpp
progress_bar.init(0., double(number_of_primary_files + 2), "Initializing file interfaces");
_datagramdata_interface->init_from_file(this->get_index_paths(), force, progress_bar);   progress_bar.tick();
_configuration_interface->init_from_file(this->get_index_paths(), force, progress_bar);   progress_bar.tick();
_navigation_interface->init_from_file(this->get_index_paths(), force, progress_bar, true); // external_progress_tick=true → ticks per file
progress_bar.close("Done");
```
Total = `number_of_primary_files + 2` (2 manual ticks + one per-file tick from navigation).

## Empty sensor configuration
If the configuration interface is not implemented yet its `read_sensor_configuration` throws; the
base config `init_from_file` **catches it and falls back to `SensorConfiguration()`** (one-time
warning). That empty config is valid: zero offsets, a default target `"0"`. Pass it straight into the
interpolator (`navi(get_sensor_configuration(file_nr))`) — do NOT special-case it. The navigation is
still fully usable (`get_sensor_data(t)` = vessel reference point; `get_navigation_data()` /
`compute_target_position("0", t)` work).

## nanobind
The generic helpers already expose the interface (`NavigationDataInterface_add_interface` →
`get_navigation_interpolator[_keys]`, `get_navigation_data`, `get_channel_ids`, `is_initialized`;
`NavigationDataInterfacePerFile_add_interface` + `<Fmt>DatagramInterface_add_interface_functions`).
Only add the new `_prefer_*` getters/setters to the **perfile** binding
(`c_<fmt>navigationdatainterfaceperfile.cpp`), chained onto the `nb::class_` with
`DOC(LOCAL_DOC_PREFIX, get_prefer_...)` (re-run `make_pybind_doc.py`). The `.def`s go **before** the
`..._add_interface<T>(cls)` calls.

## Validate on real data (both paths)
Use datasets that exercise the modern AND the legacy path (s7k: `kh1908` has all of 1003/1012/1013/
1015/1016 → preferred path; `thomaslake`, `ultfarms` only 1003/1012/1013 → fallback). Ignore any
`index/` subfolder.
```python
fh = theping.echosounders.<fmt>.<Fmt>FileHandler(files, show_progress=False)
nav = fh.navigation_interface
assert nav.is_initialized()
for k in nav.get_navigation_interpolator_keys():
    ip = nav.get_navigation_interpolator(k)
    ts = np.array(ip.get_sampled_timestamps(1.0))          # common lat/lon timestamps
    sd = ip.get_sensor_data(list(np.linspace(ts[0], ts[-1], 5)))
    # sanity: lat/lon in the survey area, heading 0..360, roll/pitch small°, heave small m
    print(sd.get_latitudes(), sd.get_longitudes(), sd.get_headings(),
          sd.get_pitches(), sd.get_rolls(), sd.get_heaves())
```
Cross-check against the raw records (`di = nav.per_file(0); di.datagrams('<Rec>')[i].get_x_in_degrees()`).
**A value that is exactly 0 for a whole file is usually real** (e.g. a system that logs 0 heave in the
legacy record), not a bug — confirm by reading the raw field, don't "fix" it. Toggle a preference
(`nav.per_file(0).set_prefer_*(False)` then `nav.init_from_file(fh.get_index_paths(), True,
tools_nanopy.progressbars.NoIndicator())`) and re-check to prove both sources decode.

## Gotchas
- `get_sensor_data(...)` returns a `SensordataLatLonVector` with `get_latitudes()/get_longitudes()/
  get_headings()/get_pitches()/get_rolls()/get_heaves()` (NOT `.latitude`).
- The per-file preference members live on the **perfile** interface; changing them needs a forced
  `init_from_file(..., force=true)` to rebuild the cached interpolators.
- Add a synthetic C++ test (no data file): construct the perfile with a config interface, assert the
  `_prefer_*` defaults + toggling + `__printer__().create_str().size() != 0`. Data-driven navigation
  checks are done in Python, not C++.
- Register nothing new in the C++ `meson.build` (you only edited existing headers); the binding
  `.cpp`s are already registered. Re-run `make_pybind_doc.py` so the new `DOC(...)` refs resolve.
