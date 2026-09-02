---
name: tmtgp-echosounders-add-format
description: 'Architecture of a file-format reader in themachinethatgoesping/echosounders and how to add a new one (e.g. s7k, gsf, kmall, kongsbergall, simradraw). Explains the layering: datagrams (headers/records), types (identifier enum), datagram interface, file handler (indexing via I_InputFileHandler), file-data interfaces (configuration/navigation/environment/ping), ping data types, and the nanobind bindings. USE when planning or extending an echosounder format reader. For the concrete first coding step use the tmtgp-echosounders-format-step1 skill; for exposing to Python and building use the style and build-and-test skills.'
---

# echosounders format architecture

Formats live in `subprojects/echosounders/src/themachinethatgoesping/echosounders/<format>/`.
Study **kongsbergall** and **kmall** (most complete) and **gsf** (minimal). All classes are
templated on `t_ifstream` and instantiated for `std::ifstream` and `datastreams::MappedFileStream`.

## Layers (bottom → top)
1. **`types.hpp`** — `t_<FMT>DatagramIdentifier` enum (record/datagram type) + the
   `o_<FMT>DatagramIdentifier` `OptionFrozen` wrapper (`_values/_names/_alt_names`). Small contiguous →
   plain enum + magic_enum; large/sparse (record numbers, 4-char codes) → `OptionFrozen`. The `o_`
   wrapper is the working identifier type (auto str↔number↔enum); the plain enum stays the interface map
   key so unknown records still index. Free helpers `datagram_type_to_string` / `_from_string` and
   `datagram_identifier_to_string` / `_info` (used by the generic interface).
2. **`datagrams/<fmt>datagram.{hpp,cpp}`** — the **datagram header** (the fixed record header). Must
   provide `from_stream`, `skip`, `get_timestamp`, `get_datagram_identifier`, `__printer__`.
3. **`datagrams/<fmt>unknown.{hpp,cpp}`** — subclass storing the raw record bytes; used for any
   record type not yet parsed. Later, one class per record type (e.g. `mrangeanddepth.hpp`).
4. **`datagrams.hpp/.cpp`** — aggregates the datagram headers + a `std::variant` of all record
   types + a `from_stream` dispatch (`<FMT>DatagramVariant`).
5. **`filedatainterfaces/<fmt>datagraminterface.hpp`** — extends
   `filetemplates::datainterfaces::I_DatagramInterface<t_identifier, t_ifstream>`; implements the
   virtual `datagram_identifier_to_string` (`o_...(id).alt_name()`) / `_info` (`o_...(id).name()`);
   holds the datagram index and offers `datagrams<T>()`, `per_file()`. Reached via
   `file_handler.datagram_interface`; its Python `datagrams(...)` takes the `o_` wrapper so it accepts
   enum / number / name / alt-name.
6. **`<fmt>filehandler.{hpp,cpp}`** — extends
   `filetemplates::I_InputFileHandler<<Fmt>Datagram, <Fmt>DatagramInterface<t_ifstream>>`. The base
   **scans** each file (`scan_for_datagrams` loops `header = <Fmt>Datagram::from_stream(ifs);
   header.skip(ifs);` → builds a `DatagramInfo` with file-nr/position/timestamp/identifier),
   caches the index, and exposes `datagram_interface()` + a combined `__printer__`.
7. **(later) higher file-data interfaces** — `configuration` / `navigation` / `environment` / `ping`
   `DataInterface` + `...PerFile`, plus `filedatatypes` (ping objects), `filedatacontainers`
   (ping/datagram containers). These turn indexed datagrams into pings, navigation, calibration,
   water-column images. Mirror `kongsbergall`/`kmall`.

## Key base classes (in `filetemplates/`)
- `I_InputFileHandler<t_DatagramBase, t_DatagramInterface>` — indexing, caching, `append_file(s)`,
  `datagram_interface()`, printing. The **only** requirements on `t_DatagramBase` are
  `from_stream(istream&)`, `skip(istream&)`, `get_timestamp()`, `get_datagram_identifier()`.
- `I_DatagramInterface<t_identifier, t_ifstream>` — datagram index, `datagrams<T>()` →
  `DatagramContainer<T,...>` (lazy reader), `size()`, `keys()`, timestamps, printing.
- `DatagramContainer` — lazily reads datagrams on `[]`/iteration from the stored `DatagramInfo`.

## Python entry points (already generic — no per-format wiring needed)
- `index_functions.find_files_and_index(folder, ['.<ext>'])` → `(files, index)`.
- `theping.echosounders.<format>.<Fmt>FileHandler(files, index)` (filehandler stays at the format
  top level); `print(fh)`; `fh.datagram_interface.datagrams_raw()` / `.datagram_headers()` /
  `.datagrams()` (whole-file variant) / `.datagrams(type[, skip_data])`.
- Datagram classes live at `<format>.datagrams.<Class>`; containers at
  `<format>.filedatacontainers.*`; the interface at `<format>.filedatainterfaces.<Fmt>DatagramInterface`.

## Binding module layout (`src/nanomodule/py_<fmt>/`, mirror py_kmall)
Split into submodules, each with `module.{hpp,cpp}` (`def_submodule` + per-class `init_c_*`):
`py_<fmt>/` (enum + option + `c_<fmt>filehandler.cpp`) → `py_datagrams/` (one `c_<datagram>.cpp` each,
`substructs/` if any) → `py_filedatacontainers/` → `py_filedatainterfaces/` (interface template in a
`.hpp` + class/init in the `.cpp`) → later `py_filedatatypes/`. See tmtgp-echosounders-format-step1 §2.

## Registration checklist (for every new file)
- Sources + headers + `.docstrings/*.doc.hpp` → `src/themachinethatgoesping/echosounders/meson.build`.
- Binding `c_*.cpp` / `module.cpp` (each under its `py_<fmt>/py_*/` submodule dir) →
  `src/nanomodule/meson.build`, and `#include "py_<fmt>/module.hpp"` + `py_<fmt>::init_m_<fmt>(m);`
  in `src/nanomodule/module.cpp`.
- Tests → `src/tests/meson.build`.

Build/test/install with the **tmtgp-build-and-test** skill; follow **tmtgp-cpp-nanobind-style**.
