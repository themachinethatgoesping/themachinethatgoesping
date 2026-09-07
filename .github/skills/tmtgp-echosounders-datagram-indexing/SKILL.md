---
name: tmtgp-echosounders-datagram-indexing
description: 'Concrete recipe for the FIRST implementation step (bootstrap) of a new echosounder file format in themachinethatgoesping/echosounders: read/parse the datagram (record) header, index all datagrams, display them via print(file_handler), and iterate raw datagrams from Python. Produces a working vertical slice (C++ core + catch2 tests + nanobind bindings) before any per-record parsing. Worked example: the s7k format (src/.../echosounders/s7k). USE this to bootstrap a new format; then add per-record datagram classes with tmtgp-echosounders-record-parsers. See also tmtgp-echosounders-add-format, tmtgp-cpp-class-style, tmtgp-cpp-nanobind-style, tmtgp-build-and-test.'
---

# Datagram header + indexing + display + raw iteration (format bootstrap, step 1 of 2)

Goal: `fh = theping.echosounders.<fmt>.<Fmt>FileHandler(files, index); print(fh)` shows every
datagram type + count, and `fh.datagram_interface.datagrams_raw()` iterates raw datagrams.
Reference implementation: **s7k** (mirror gsf, the minimal complete format). Next, add per-record
parsers with **tmtgp-echosounders-record-parsers**.

## 0. Research the header first
Get the **datagram/record header** byte layout (offsets, types, endianness), the **record-type id**
list, and how to compute the **timestamp**. Cross-check ≥2 sources (official spec + a C reader like
MB-System). Store a research doc + spec next to the format (see `s7k/../docs/s7k_format/`).

## 1. C++ core files (under `src/themachinethatgoesping/echosounders/<fmt>/`)
- **`types.hpp` (+ `types.cpp`)** — `enum class t_<Fmt>DatagramIdentifier : uintN` with the record
  ids **plus the `o_<Fmt>DatagramIdentifier` `OptionFrozen` wrapper** (arrays `_values/_names/_alt_names`
  + `extern template` in hpp, `template struct ...` in cpp). `o_...` is the working identifier type
  everywhere below (it converts str↔number↔enum automatically); the plain enum stays the interface
  **map key + virtual-signature type so unknown record types still index** (a scoped enum can hold any
  value). Add `datagram_type_to_string`/`_from_string` and echosounders-namespace
  `datagram_identifier_to_string`/`_info`. (75-entry enums: generate hpp with a throwaway script to
  keep arrays consistent.)
- **`datagrams/<fmt>datagram.{hpp,cpp}`** — the header class:
  - `using t_DatagramIdentifier = t_<Fmt>DatagramIdentifier;` **and `using o_DatagramIdentifier =
    o_<Fmt>DatagramIdentifier;`**; type the record-type member as `o_DatagramIdentifier` (default-init
    to `t_...::unspecified`) — a thin single-`value` wrapper (same size/layout as the enum) so it stays
    inside the one-shot header read.
  - members in exact on-disk order, default-initialized (`= 0`) so a default object is well-defined,
    laid out so they are naturally aligned → read all at once:
    `is.read(reinterpret_cast<char*>(&_first_member), __size);` (`static constexpr size_t __size`).
  - `static <Fmt>Datagram from_stream(istream&)` (+ an overload taking an expected `o_DatagramIdentifier`),
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
  `I_DatagramInterface<t_<Fmt>DatagramIdentifier, t_ifstream>` (the virtual `datagram_identifier_*` still
  take the **plain enum**); implement `datagram_identifier_to_string` (the **short identifier**: a
  numeric-id format → `std::to_string(uint32_t(id))`; a 4-char-code format → `int_as_string(id)`) and
  `datagram_identifier_info` (descriptive name → `<fmt>::datagram_type_to_string(id)`), then
  `per_file()`. **Both must be graceful for unknown record types — do NOT use `o_...(id).alt_name()` /
  `.name()` here** (those throw via the frozen-map `.at()` on any value not in the enum, and a real
  file WILL contain proprietary/unnamed records). `std::to_string` never throws; `datagram_type_to_string`
  returns `"unknown"`.
- **`<fmt>filehandler.{hpp,cpp}`** — extend
  `I_InputFileHandler<datagrams::<Fmt>Datagram, filedatainterfaces::<Fmt>DatagramInterface<t_ifstream>>`;
  4 constructors (single/multi × bool/progressbar), empty `setup_interfaces()` + `init_interfaces()`,
  `__printer__` that appends the base printer. (Copy gsffilehandler.hpp and strip the commented parts.)
- Create placeholder `<dir>/.docstrings/<name>.doc.hpp` for each header (boilerplate + `//sourcehash: 0`).

## 2. nanobind bindings (under `src/nanomodule/py_<fmt>/`, submodules mirror kmall)
Mirror `py_kmall`'s layout — do **not** put everything flat. Each submodule has its own
`module.{hpp,cpp}` that `def_submodule(...)`s and calls the per-class `init_c_*`. Include the C++
headers as `<themachinethatgoesping/echosounders/<fmt>/…>` (angle brackets, like kmall).
- `py_<fmt>/module.{hpp,cpp}` — top: `def_submodule("<fmt>")`, register the enum `.value(...)` +
  `make_option_class<o_...>` + the free `datagram_type_to_string`/`_from_string`, then call the
  submodule inits (`py_datagrams::init_m_<fmt>datagrams`, `py_filedatacontainers::…`,
  `py_filedatainterfaces::…`) and `init_c_<fmt>filehandler`.
- `py_<fmt>/py_datagrams/` — **one `c_<datagram>.cpp` per datagram** (`c_<fmt>datagram.cpp` +
  `c_<fmt>unknown.cpp` first) + `module.{hpp,cpp}` (`init_m_<fmt>datagrams` →
  `def_submodule("datagrams")`). Classes land in Python at `<fmt>.datagrams.<Class>`. (Substructs, if
  any, go in `py_datagrams/substructs/` but register into the same `datagrams` submodule.)
- `py_<fmt>/py_filedatacontainers/` — `c_<fmt>datagramcontainer.cpp`
  (`create_DatagramContainerTypes<<Fmt>Datagram,t_id>(m,"..._Header")`, `<<Fmt>Unknown,…>("..._Unknown")`,
  and the whole-file variant `<t_<Fmt>DatagramVariant,t_id,<Fmt>DatagramVariant>("..._Variant")` — these
  are the iterator return types, must be registered) + `module.{hpp,cpp}` (`def_submodule("filedatacontainers")`).
- `py_<fmt>/py_filedatainterfaces/` — **split header + cpp**: `c_<fmt>datagraminterface.hpp` holds the
  template `<Fmt>DatagramInterface_add_interface_functions<T_BaseClass>(cls)`; `c_<fmt>datagraminterface.cpp`
  has `py_create_class_<Fmt>DatagramInterface<T_FileStream>` (both stream types) + `init_c_...`; plus
  `module.{hpp,cpp}` (`def_submodule("filedatainterfaces")`). In the template add
  `py_i_datagraminterface::add_InterfaceFunctions`, a **no-arg `datagrams(skip_data=false)`** →
  `self.datagrams<t_<Fmt>DatagramVariant,<Fmt>DatagramVariant>()` (whole-file variant iterator),
  `datagrams_raw()`→`self.datagrams<<Fmt>Unknown>()`, `datagram_headers()`→`self.datagrams<<Fmt>Datagram>()`,
  and `per_file`. Each typed iterator takes a **`(o_<Fmt>DatagramIdentifier type)`** arg (pass `type`
  straight through — it converts to the enum), so Python can call `datagrams_raw("<Name>")`/`("<number>")`/`(<number>)`.
- `py_<fmt>/c_<fmt>filehandler.cpp` (**stays top-level**) — bind for both stream types with
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
- The `I_DatagramInterface` map key + virtual `datagram_identifier_*` signature stay the **plain enum**
  so unknown record types still index. Use the `o_` wrapper for the *working* identifier (members,
  `from_stream` params, the Python `datagrams(...)` argument, `.name()`/`.alt_name()` lookups);
  `name()`/`alt_name()` **throw on unknown values** → keep the identifier enum exhaustive, or guard with
  `enum_contains()`.
- **The identifier→string conversions must emit valid UTF-8 and never throw** — they run over EVERY
  datagram, including record types not named in the enum. TWO code paths exist: the *interface*
  printer uses the virtual member `datagram_identifier_to_string`/`_info`; the *container* printer
  (`fh.datagram_interface.datagrams().print()`) uses the free `echosounders::datagram_identifier_to_string(<fmt>::t_...)`
  in `types.hpp`. **Fix BOTH — a passing interface print does NOT prove the container print works.**
  For a **numeric-id** format return the DECIMAL string (`std::to_string(uint32_t(id))`); `int_as_string`
  (correct only for 4-char-code formats like kmall/kongsbergall) reinterprets the number's raw bytes →
  **invalid UTF-8** → Python `print()`/`info_string()` raise `UnicodeDecodeError` /
  `nanobind::str(): conversion error!`. Never `o_...(id).name()/.alt_name()` in these (throws on unknown).
- `skip()`/raw-content length must use the header's total-size field, consistently, so the scan lands
  exactly on the next datagram (a wrong offset shows up as a "read incompletely" warning).
