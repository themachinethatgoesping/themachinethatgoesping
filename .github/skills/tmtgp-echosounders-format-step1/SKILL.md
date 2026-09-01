---
name: tmtgp-echosounders-format-step1
description: 'Concrete recipe for the FIRST implementation step of a new echosounder file format in themachinethatgoesping/echosounders: read/parse the datagram (record) header, index all datagrams, display them via print(file_handler), and iterate raw datagrams from Python. Produces a working vertical slice (C++ core + catch2 tests + nanobind bindings) before any per-record parsing. Worked example: the s7k format (src/.../echosounders/s7k). USE this to bootstrap a new format; then add per-record datagram classes. See also tmtgp-echosounders-add-format, tmtgp-cpp-nanobind-style, tmtgp-build-and-test.'
---

# Step 1: datagram headers + display + raw iteration

Goal: `fh = theping.echosounders.<fmt>.<Fmt>FileHandler(files, index); print(fh)` shows every
datagram type + count, and `fh.datagram_interface.datagrams_raw()` iterates raw datagrams.
Reference implementation: **s7k** (mirror gsf, the minimal complete format).

## 0. Research the header first
Get the **datagram/record header** byte layout (offsets, types, endianness), the **record-type id**
list, and how to compute the **timestamp**. Cross-check ≥2 sources (official spec + a C reader like
MB-System). Store a research doc + spec next to the format (see `s7k/../docs/s7k_format/`).

## 1. C++ core files (under `src/themachinethatgoesping/echosounders/<fmt>/`)
- **`types.hpp` (+ `types.cpp`)** — `enum class t_<Fmt>DatagramIdentifier : uintN` with the record
  ids. Sparse/large ids → `OptionFrozen` (arrays `_values/_names/_alt_names` + `extern template` in
  hpp, `template struct ...` in cpp). Keep the plain enum as the interface identifier so **unknown
  record types don't throw** (a scoped enum can hold any value). Add
  `datagram_type_to_string`/`_from_string` and echosounders-namespace `datagram_identifier_to_string`
  /`_info`. (75-entry enums: generate hpp with a throwaway script to keep arrays consistent.)
- **`datagrams/<fmt>datagram.{hpp,cpp}`** — the header class:
  - members in exact on-disk order, default-initialized (`= 0`) so a default object is well-defined,
    laid out so they are naturally aligned → read all at once:
    `is.read(reinterpret_cast<char*>(&_first_member), __size);` (`static constexpr size_t __size`).
  - `static <Fmt>Datagram from_stream(istream&)` (+ an overload checking an expected identifier),
    `void to_stream(ostream&) const`, `void skip(istream&) const` (seek by `size - __size`),
    `virtual double get_timestamp() const` (NaN if none), `get_datagram_identifier()`, getters,
    `bool operator==(...) const = default`, `__printer__`, macros
    `__CLASSHELPER_DEFAULT_PRINTING_FUNCTIONS__` + `__STREAM_DEFAULT_TOFROM_BINARY_FUNCTIONS__(T)`.
- **`datagrams/<fmt>unknown.{hpp,cpp}`** — subclass with a `std::string _raw_content`;
  `from_stream(is, header)` resizes to `compute_size_content()` and reads the rest. Uses
  `__STREAM_DEFAULT_TOFROM_BINARY_FUNCTIONS_NOT_CONST__`.
- **`datagrams.hpp` (+ `.cpp`)** — include the two datagram headers, a `std::variant`, and a
  `<Fmt>DatagramVariant::from_stream(is, type, skip)` that `default:`-returns `<Fmt>Unknown`.
- **`filedatainterfaces/<fmt>datagraminterface.hpp`** — extend
  `I_DatagramInterface<t_<Fmt>DatagramIdentifier, t_ifstream>`; implement `datagram_identifier_to_string`
  (e.g. the numeric id) + `datagram_identifier_info` (the name, "unknown" fallback) + `per_file()`.
- **`<fmt>filehandler.{hpp,cpp}`** — extend
  `I_InputFileHandler<datagrams::<Fmt>Datagram, filedatainterfaces::<Fmt>DatagramInterface<t_ifstream>>`;
  4 constructors (single/multi × bool/progressbar), empty `setup_interfaces()` + `init_interfaces()`,
  `__printer__` that appends the base printer. (Copy gsffilehandler.hpp and strip the commented parts.)
- Create placeholder `<dir>/.docstrings/<name>.doc.hpp` for each header (boilerplate + `//sourcehash: 0`).

## 2. nanobind bindings (under `src/nanomodule/py_<fmt>/`)
- `module.hpp` (declares `init_m_<fmt>`), `module.cpp` (submodule + enum `.value(...)` + option class
  + `init_c_*` calls).
- `c_<fmt>datagrams.cpp` — bind `<Fmt>Datagram` and `<Fmt>Unknown`.
- `c_<fmt>datagramcontainer.cpp` — `py_datagramcontainer::create_DatagramContainerTypes<<Fmt>Datagram,
  t_id>(m,"..._Header")` and `<<Fmt>Unknown,...>("..._Unknown")` (these are the return types of the
  iterators — must be registered).
- `c_<fmt>datagraminterface.cpp` — bind the interface for both stream types; add
  `py_i_datagraminterface::add_InterfaceFunctions`, then `datagrams_raw()` →
  `self.datagrams<<Fmt>Unknown>()` and `datagram_headers()` → `self.datagrams<<Fmt>Datagram>()`
  (each with a no-arg and a `(t_id type)` overload), plus `per_file`.
- `c_<fmt>filehandler.cpp` — bind for both stream types with
  `py_i_inputfilehandler::add_default_constructors / add_open_file_interface / add_default_containers`
  (the last adds the `datagram_interface` property). Names `"<Fmt>FileHandler"` (mapped) and `..._stream`.

## 3. Register + test + build
- Register sources/headers/tests in the three `meson.build`s and wire `init_m_<fmt>` into
  `src/nanomodule/module.cpp` (see tmtgp-echosounders-add-format).
- Add catch2 tests `src/tests/<fmt>/datagrams/<fmt>datagram.test.cpp` (build a raw header buffer,
  assert decoded fields + the timestamp date string) and `<fmt>unknown.test.cpp` (round trips).
- Build/test/install with **tmtgp-build-and-test**. Then a Python smoke test:
  ```python
  files, index = theping.echosounders.index_functions.find_files_and_index(folder, ['.<ext>'])
  fh = theping.echosounders.<fmt>.<Fmt>FileHandler(files, index)
  print(fh)                                  # all datagram types + counts
  raw = fh.datagram_interface.datagrams_raw(); print(len(raw), raw[0])
  ```

## Pitfalls
- Header read relies on **no struct padding** — order members so every field is naturally aligned;
  add a parse test that asserts real field values to catch layout mistakes.
- Keep the interface identifier a **plain enum** (not the throwing OptionFrozen) so unknown record
  types index & print gracefully.
- `skip()`/raw-content length must use the header's total-size field, consistently, so the scan lands
  exactly on the next datagram (a wrong offset shows up as a "read incompletely" warning).
