---
name: tmtgp-echosounders-interfaces
description: 'Recipe for the THIRD implementation step of an echosounder file format in themachinethatgoesping/echosounders: create the six file-data INTERFACES (datagramdata, configuration, navigation, environment, otherfiledata, ping) as structural shells (top-level + PerFile each), the minimal ping TYPE infrastructure (ping/common/filedata/bottom/watercolumn + container) needed for the ping interface to compile, sort the indexed datagrams into the interfaces in the file handler (callback_scan_packet), and expose everything via nanobind — WITHOUT yet implementing the read_* processing functions (read_sensor_configuration/read_navigation_data/read_pings). Follows tmtgp-echosounders-record-parsers. Worked example: the s7k interfaces (src/.../echosounders/s7k/filedatainterfaces, filedatatypes, filedatacontainers). USE when a bootstrapped+parsed format needs its interface layer scaffolded so the interfaces can be implemented one-by-one next (starting with configuration). See tmtgp-echosounders-add-format, tmtgp-cpp-class-style, tmtgp-cpp-nanobind-style, tmtgp-build-and-test. Reference: kmall (most complete), kongsbergall, simradraw.'
---

# File-data interfaces + minimal ping types + datagram sorting (format step 3 of N)

Goal: after this step `fh = <Fmt>FileHandler(files)` builds, exposes `fh.configuration_interface`,
`fh.navigation_interface`, `fh.environment_interface`, `fh.ping_interface`,
`fh.datagramdata_interface`, `fh.otherfiledata_interface`, and **every indexed datagram is sorted
into exactly one specialized interface** (inspect via `itf.per_file(i).datagram_headers()`).
The `read_*` processing (sensor config, navigation, pings) is **not** implemented yet, so
`init_interfaces` only inits the generic datagram-data interface and `get_pings()` returns empty.
Reference implementation: **s7k**; mirror **kmall** (most complete). Build/validate with
tmtgp-build-and-test after each wave.

## Layer overview (mirror kmall exactly, strip the processing)
Six interfaces, each a **top-level** (`<Fmt>XDataInterface`, over multiple files) + a **PerFile**
(`<Fmt>XDataInterfacePerFile`, one file). All derive from the generic base templates in
`filetemplates/datainterfaces/` and are templated on `t_ifstream`.

| interface | base (top / perfile) | ctor dependency |
|-----------|----------------------|-----------------|
| DatagramData | `I_FileDataInterface` / `I_FileDataInterfacePerFile<<Fmt>DatagramInterface>` | none |
| OtherFileData | same as DatagramData | none |
| Configuration | `I_ConfigurationDataInterface` / `...PerFile<<Fmt>DatagramInterface>` | none |
| Navigation | `I_NavigationDataInterface` / `...PerFile<<Fmt>ConfigurationDataInterface>` | shared_ptr\<Config\> |
| Environment | `I_EnvironmentDataInterface` / `...PerFile<<Fmt>NavigationDataInterface>` | shared_ptr\<Nav\> |
| Ping | `I_PingDataInterface` / `...PerFile<<Fmt>EnvironmentDataInterface, <Fmt>PingContainer>` | shared_ptr\<Env\> |

- **PerFile** interfaces additionally re-expose the raw datagram accessors — bind them in nanobind
  with `<Fmt>DatagramInterface_add_interface_functions<T>(cls)` (see below).
- **Nav/Env/Ping PerFile need TWO constructors**: a default one (delegates to the base name-ctor,
  which *throws* — it is never actually called because the top-level interface **overrides
  `add_file_interface`** to `make_shared<PerFile>(dependency)`) **and** one taking the
  `shared_ptr<dependency>`. Config/DatagramData/OtherFile PerFile only need the default ctor.
- Each `__printer__` just `append`s the base printer + a `register_section("<Class>")` marker.

## Minimal ping TYPE infrastructure (needed only so the ping interface compiles)
The ping interface PerFile is templated on `<Fmt>PingContainer` = `PingContainer<<Fmt>Ping>`, so a
ping type must exist. Create **stubs** under `filedatatypes/` (mirror kmall, drop all data logic):
- `<Fmt>PingCommon<t_ifstream>` — holds `shared_ptr<<Fmt>PingFileData> _file_data`; `file_data()`
  get/set; `t_rawdata` alias. (copy kmallpingcommon verbatim, rename.)
- `<Fmt>PingFileData<t_ifstream>` — derives `I_PingFileData` **and**
  `filedatainterfaces::<Fmt>DatagramInterface<t_ifstream>` (so a ping owns its datagram index);
  `class_name()`, `__printer__` appends both base printers, `__CLASSHELPER_DEFAULT_PRINTING_FUNCTIONS__`.
- `<Fmt>PingBottom<t_ifstream>` / `<Fmt>PingWatercolumn<t_ifstream>` — derive
  `I_PingBottom`/`I_PingWatercolumn` + `<Fmt>PingCommon`; **ctor + `class_name()` + a MINIMAL
  `__printer__` only** (no getter overrides — they inherit the base "not implemented" throwers).
- `<Fmt>Ping<t_ifstream>` — derives `I_Ping` + `<Fmt>PingCommon`; holds `_bottom`/`_watercolumn`
  members; `deep_copy()`, `add_datagram_info()`, `bottom()`/`watercolumn()` overrides, `__printer__`
  (append `I_Ping::__printer__` only). `type_DatagramInfo_ptr = <Fmt>PingFileData::type_DatagramInfo_ptr`.
- `filedatacontainers/<Fmt>pingcontainer.hpp` — `using <Fmt>PingContainer = PingContainer<<Fmt>Ping<t_ifstream>>;`.

## File handler wiring (mirror kmall `<Fmt>filehandler.hpp`)
- Members: `shared_ptr` for each interface; build the **dependency chain**:
  `config`, `nav(config)`, `env(nav)`, `ping(env)`, plus standalone `datagramdata`, `otherfile`.
- `callback_scan_new_file_begin`: call `add_file_information(this->_input_file_manager->get_file_paths())`
  on **all six** interfaces.
- `callback_scan_packet(datagram_info)`: `_datagramdata_interface->add_datagram_info(di)` **always**
  (it tracks *all* datagrams), then `switch (di->get_datagram_identifier())` routing each record type
  to `_configuration_/_navigation_/_environment_/_ping_interface->add_datagram_info(di)`; **`default:`
  → `_otherfiledata_interface`**. Guess placement from record semantics; when unsure, leave it in
  the default (other). (s7k map: nav=position/attitude/heading/heave/depth/altitude; env=SVP/CTD/
  soundspeed/absorption; config=installation/config; ping=sonar-settings/beam-geometry/detection/
  water-column/snippets; everything else → other.)
- `init_interfaces`: **only** `_datagramdata_interface->init_from_file(...)` for now. Add the
  config/nav/env/other/ping inits as **commented TODOs** — see the gotcha below for why the ping
  init must stay off. `setup_interfaces()` stays empty (unless the format has split file pairs like
  kmall .kmall/.kmwcd → `link_all_and_wcd_files`).
- Accessors `configuration_interface()`…`ping_interface()`; `get_pings(sorted_by_time=true)` →
  `_ping_interface->get_pings()`; `get_channel_ids()`.

## nanobind bindings (under `src/nanomodule/py_<fmt>/`, mirror py_kmall)
- `py_filedatainterfaces/` — one `c_<fmt>XdatainterfacePerFile.cpp` + `c_<fmt>Xdatainterface.cpp`
  per interface. Top-level uses helper `py_i_<x>datainterface::<X>DataInterface_add_interface<T>(cls)`;
  **PerFile** uses `py_i_<x>datainterface::<X>DataInterfacePerFile_add_interface<T>(cls)` **plus**
  `<Fmt>DatagramInterface_add_interface_functions<T>(cls)` (from `c_<fmt>datagraminterface.hpp`).
  Helper namespaces are **all** `py_i_<x>datainterface` (perfile helper lives there too), e.g.
  `py_i_filedatainterface::FileDataInterfacePerFile_add_interface`,
  `py_i_configurationdatainterface::ConfigurationDataInterfacePerFile_add_interface`. Register every
  `init_c_*` in `py_filedatainterfaces/module.cpp` (PerFile before top-level).
- `py_filedatatypes/` (NEW) — `module.{hpp,cpp}` + `c_<fmt>ping{common,filedata,bottom,watercolumn}.cpp`
  + `c_<fmt>ping.cpp`. `nb::class_<t_X, datatypes::I_PingBottom>` (etc.) for the sub-types;
  filedata gets `<Fmt>DatagramInterface_add_interface_functions`; ping/common expose `file_data`
  via `def_prop_ro(..., nb::rv_policy::reference_internal)`; end each with `__PYCLASS_DEFAULT_COPY__`.
- `py_filedatacontainers/` — add `c_<fmt>pingcontainer.cpp`:
  `py_pingcontainer::create_PingContainerType<<Fmt>Ping<Stream>>(m, name)`.
- filehandler `c_<fmt>filehandler.cpp` — add `def_prop_ro` for the six interfaces + `get_pings`
  (`nb::overload_cast<bool>(&...::get_pings, nb::const_)`) + `get_channel_ids`.
- top `py_<fmt>/module.cpp` — `#include "py_filedatatypes/module.hpp"` and call
  `py_filedatatypes::init_m_<fmt>filedatatypes(subm)` **before** filedatacontainers (container
  references the ping type).
- Every class is registered for **both** stream types: `datastreams::MappedFileStream` → name
  `"<Class>"`, `std::ifstream` → `"<Class>_stream"`.

## Gotchas that cost real debugging time
1. **`datagram_identifiers_to_string` (plural) must exist in the `echosounders` namespace in
   `<fmt>/types.hpp`** — the base `I_FileDataInterfacePerFile::__printer__` calls it (found via
   enclosing-namespace/ADL) for the linked-file extension sets. Provide **both** a
   `std::vector<t_<Fmt>Identifier>` and a `std::set<...>` overload (inline, next to
   `datagram_identifier_to_string`). Missing it → "declared later in the translation unit" /
   "no declarations found by ADL" **only when a PerFile interface printer is instantiated** (so the
   datagram-indexing step didn't catch it).
2. **`init_interfaces` must NOT call the ping interface init yet.** `I_PingDataInterface::init_from_file`
   processes file 0 (`_ping_container = process_file(0)`) **outside** its try/catch, and `process_file`
   calls the not-implemented `read_pings` → the exception propagates → constructing the handler with
   `init=true` (the default) throws. Navigation/configuration init *are* exception-safe (config's base
   `init_from_file` catches and falls back to an empty config; nav catches per-file), but keep them off
   too until implemented to avoid noisy warnings.
3. **Stub `<Fmt>PingBottom`/`Watercolumn` `__printer__` must NOT append the `I_PingBottom`/
   `I_PingWatercolumn` base printer** — the base printer queries `get_number_of_beams` /
   `get_number_of_tx_sectors` etc., which are virtual-with-default *throwers* in the stub, so it throws.
   Print a minimal `register_string("status", "not implemented yet")` instead. (`I_Ping::__printer__`
   is safe — it does not recurse into the sub-object printers.)
4. **The `read_*` virtuals are virtual-with-default (throw), not pure** → you do NOT override them in
   the shells; the class still instantiates. Likewise the `I_PingBottom`/`Watercolumn` getters, so the
   bottom/watercolumn stubs need no getter overrides.
5. **C++ test include depth**: tests resolve `#include "../themachinethatgoesping/..."` via an
   `-I src/tests/` dir, so use **one** `../` regardless of the test's subdirectory depth.
6. **Ping-type / container bindings need an explicit
   `#include <.../filetemplates/datastreams/mappedfilestream.hpp>`** (the s7k headers don't pull it
   in transitively) or `datastreams::MappedFileStream` is "not declared".

## Registration checklist (three meson.build files)
- C++ headers + `.docstrings/*.doc.hpp` for every new interface/type/container →
  `src/themachinethatgoesping/echosounders/meson.build` (`headers = [...]`). Run
  `python make_pybind_doc.py` first — it walks the tree and generates the `.doc.hpp` placeholders.
- Binding `.cpp` (all interface/type/container files + the new `py_filedatatypes/module.cpp`) →
  `src/nanomodule/meson.build`.
- C++ test → `src/tests/meson.build`.

## Tests & validation
- **C++**: a synthetic instantiation smoke test (no data file needed) — construct the
  config←nav←env←ping chain + datagramdata/other, `CHECK(itf->__printer__(2,false).create_str().size()
  != 0)`; construct `<Fmt>Ping`, check `__printer__`/`bottom()`/`watercolumn()`/`deep_copy()` and an
  empty `<Fmt>PingContainer`. (No format has data-driven interface C++ tests — they're synthetic.)
- **Python** (real data, e.g. s7k at `/home/data/test_data/s7k/<subfolder>/`, ignore `index/`):
  ```python
  fh = theping.echosounders.<fmt>.<Fmt>FileHandler(files, show_progress=False)
  # every datagram sorted exactly once:
  total = len(fh.datagramdata_interface.per_file(0).datagram_headers())
  spec  = sum(len(getattr(fh,n).per_file(0).datagram_headers())
              for n in ['configuration_interface','navigation_interface','environment_interface',
                        'otherfiledata_interface','ping_interface'])
  assert spec == total           # sorting covers everything, no double-counting
  fh.filedatatypes.<Fmt>Ping; fh.filedatacontainers.<Fmt>PingContainer   # importable
  assert len(fh.get_pings()) == 0  # processing not implemented yet
  ```
  `keys()` on an interface can raise `ValueError: <n> is not a valid t_<Fmt>DatagramIdentifier` for
  proprietary/unnamed record numbers in a real file — that is a pre-existing enum-binding limitation,
  not a sorting bug; use `datagram_headers()` counts (or raw record numbers) to inspect instead.

Next step: implement the interfaces one by one, starting with the **configuration** data interface
(`read_sensor_configuration`), then navigation, environment, ping (`read_pings` + the real
bottom/watercolumn accessors) — flipping on each `init_from_file` in `init_interfaces` as it lands.
