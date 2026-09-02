---
name: tmtgp-cpp-nanobind-style
description: 'Coding style & conventions for themachinethatgoesping (C++20 + nanobind monorepo): file headers, naming, comments/docstrings, ObjectPrinter, stream/binary helpers, enums (OptionFrozen), libraries, performance idioms, catch2 tests, and how classes are exposed to Python with nanobind. USE when writing or reviewing C++ or nanobind code anywhere in themachinethatgoesping (echosounders, tools, navigation, gridding, pingprocessing, widgets, algorithms). Reference implementations: kongsbergall and kmall (most complete).'
---

# themachinethatgoesping C++ / nanobind style

Study `subprojects/echosounders/.../kongsbergall` and `.../kmall` as canonical examples.
Match the surrounding file; the notes below are the defaults.

## File layout
- **SPDX header** on every file. Code = `MPL-2.0`; tests / meson.build / generated = `CC0-1.0`.
  Copyright line: `// SPDX-FileCopyrightText: 2022 - 2025 Peter Urban, Ghent University`.
- Header: `#pragma once`, then `/* generated doc strings */ #include ".docstrings/<name>.doc.hpp"`.
- Include order: docstrings → `std` → external (`fmt`, `magic_enum`, `frozen`, `boost`, `nanobind`)
  → `themachinethatgoesping/...` → local `"..."`.
- Namespaces (no indent inside): `themachinethatgoesping::echosounders::<format>[::datagrams|::filedatainterfaces]`.
  Close with `// namespace x` comments.

## Naming
- Types/classes `PascalCase`; functions & variables `snake_case`; **members `_snake_case`** (leading underscore).
- `t_` prefix = enum / template type params (`t_KMALLDatagramIdentifier`, `t_ifstream`).
- `o_` prefix = `OptionFrozen`/`Option` wrapper around an enum (`o_KMALLDatagramIdentifier`).
- Getters/setters: `get_x()` / `set_x(v)`. Static factory: `from_stream`, `from_binary`.
- nanobind files: `c_<class>.cpp` (bind one class), `module.cpp`/`module.hpp` per submodule,
  namespaces `pymodule::py_<format>`, init fns `init_c_<class>` / `init_m_<format>`.

## Comments & docstrings (feed pybind11_mkdoc)
- Members: trailing `///< short description`.
- Classes/functions: `/** @brief ... @param ... @return ... */` (extracted into Python docstrings).
- Section separators inside classes: `// ----- section name -----`.
- Suppress a generated docstring with a line `// IGNORE_DOC:mkd_doc_...` before the entity.
- Keep comments to what code cannot show; do not restate the next line.
- **Trivial passthrough `get_x`/`set_x` have an empty generated doc** (mkdoc emits `R"doc()doc"` for
  an undocumented one-line accessor) while the *variable it returns* is documented — so in the `.def`
  point the docstring at that variable's doc (for **both** getter and setter), not the empty accessor:
    - direct member `_x` (body `return _x;` / `_x = v;`) → `DOC(<pfx>, <Class>, x)` — mkdoc **strips the
      leading `_`** (e.g. `DOC_S7KDatagram(device_identifier)`, *not* `(get_device_identifier)`).
    - packed `Content`-struct field `_content.x` → `DOC(<pfx>, <Class>, Content, x)`; make the per-file
      shortcut **variadic** so it can carry the path:
      `#define DOC_C(CLASS, ...) DOC(<pfx>, CLASS, __VA_ARGS__)` → `DOC_C(ReferencePoint, Content, offset_x)`.
- **If `get_x`/`set_x` processes the value** (cast, scale, flag/bit decode, unit conversion, compute)
  it needs its *own* doc: put a `///`/`/** @brief ... */` comment on the C++ accessor (mkdoc extracts
  it — keep `DOC(...,get_x)`) or pass an inline string literal to `.def`. Never leave a processing
  accessor pointing at an empty doc.

## Datagram / value classes (pattern)
- `using t_DatagramIdentifier = ...;` **and `using o_DatagramIdentifier = o_<Fmt>DatagramIdentifier;`**
  (the `OptionFrozen` wrapper); `static constexpr size_t __size = <header bytes>;`
  (note: real `sizeof` is larger because of the vtable).
- Store the record-type member and take identifier params as **`o_DatagramIdentifier`**, not the raw
  enum (member `_..._identifier`, `get/set_datagram_identifier`, `from_stream(is, o_DatagramIdentifier)`,
  `__check_datagram_identifier__(o_..., o_...)`). `OptionFrozen` is a thin single-`value` wrapper (no
  vtable, same size/layout as the enum) so the member stays inside the one-shot
  `is.read(&_first_member, __size)` header read, and it converts implicitly to/from the enum, the
  underlying int and the name/alt-name string.
- `virtual double get_timestamp() const` (NaN if none); `skip(std::istream&)`; `from_stream(...)`.
- `bool operator==(const T&) const = default;`.
- Printing: implement `tools::classhelper::ObjectPrinter __printer__(unsigned int float_precision,
  bool superscript_exponents) const` using `register_value / register_string / register_section /
  append`; then add macro `__CLASSHELPER_DEFAULT_PRINTING_FUNCTIONS__` (gives `info_string()`,
  `print()`, `__repr__`).
- Stream/binary: `void to_stream(std::ostream&) const;` `static T from_stream(std::istream&);`
  plus macro `__STREAM_DEFAULT_TOFROM_BINARY_FUNCTIONS__(T)` (or `..._NOT_CONST__(T)` if
  `to_stream` is non-const).

## Enums
- Small, contiguous values → plain `enum class : uintN_t` + `magic_enum` for name<->value.
- Large/sparse values (record numbers, 4-char codes) → **`OptionFrozen`**: declare the enum plus
  three `inline constexpr std::array`s `_values` / `_names` / `_alt_names`, then
  `using o_X = tools::classhelper::OptionFrozen<t_X, _values.size(), _values, _names, _alt_names>;`
  and an `extern template struct OptionFrozen<...>;` in the header with the matching
  `template struct OptionFrozen<...>;` instantiation in the `.cpp`. `o_X.name()` throws on unknown
  values → guard with `enum_contains()` or keep the raw enum for graceful "unknown" handling.
- **Prefer `o_X` (not the raw enum) as the working identifier type** — datagram members,
  `from_stream`/check params, and the Python `datagrams(...)` argument — so str↔number↔enum conversion
  is automatic. `name()` (descriptive) / `alt_name()` (short code / record number) throw on unknown, so
  keep the identifier enum exhaustive; the `I_DatagramInterface` map key + virtual `datagram_identifier_*`
  signature stay the **plain enum** so unrecognised records still index.

## Libraries / performance
- `fmt` for formatting, `magic_enum`, `frozen` (constexpr maps), `boost::endian` (byte-swap for
  big-endian formats like gsf), `nanobind`, `xtensor`/`xsimd` for numerics, `catch2` for tests.
- Read a fixed header in **one** `is.read(reinterpret_cast<char*>(&_first_member), __size)` — lay
  members out to match the on-disk byte order with natural alignment (no padding). Verify offsets.
- Datagrams are indexed first (position + timestamp + type), then read **lazily** through
  `DatagramContainer`. Everything is templated on `t_ifstream` and instantiated for both
  `std::ifstream` and `datastreams::MappedFileStream`.

## C++ tests (catch2)
- File `src/tests/<format>/.../<name>.test.cpp`; `#define TESTTAG "[<format>]"`.
- `TEST_CASE("...", TESTTAG)`; use `REQUIRE` / `CHECK`, `Catch::Approx` for floats.
- Standard checks: copy `x == T(x)`, binary `x == T(x.from_binary(x.to_binary()))`, stream round
  trip, `x.info_string().size() != 0`. For parsers, build a byte buffer and assert decoded fields.
- Register the file in `src/tests/meson.build` `sources`.

## Exposing to Python (nanobind)
- **Module layout (mirror `py_kmall`)**: split a format's bindings into submodules, each with its own
  `module.{hpp,cpp}` that `def_submodule(...)`s and calls per-class `init_c_*`: `py_<fmt>/` (top: enum
  + `make_option_class` + filehandler) → `py_datagrams/` (**one `c_<datagram>.cpp` per datagram**,
  `substructs/` if any → Python `<fmt>.datagrams.<Class>`), `py_filedatacontainers/`,
  `py_filedatainterfaces/` (interface template in a `c_<fmt>datagraminterface.hpp`, class + `init_c_*`
  in the `.cpp`), later `py_filedatatypes/`. Don't lump many classes in one file. Include C++ headers
  as `<themachinethatgoesping/echosounders/<fmt>/…>` (angle brackets).
- One template function `py_create_class_<x><T_FileStream>(module&, name)`; register for both stream
  types with names `"<Class>"` (MappedFileStream) and `"<Class>_stream"` (`std::ifstream`).
- Reuse helpers: `py_filetemplates::py_i_inputfilehandler::add_default_constructors /
  add_open_file_interface / add_default_containers` (adds the `datagram_interface` property);
  `py_i_datagraminterface::add_InterfaceFunctions`; `py_datagramcontainer::create_DatagramContainerTypes`.
- Docstrings via `DOC(themachinethatgoesping, echosounders, <format>, <Class>, <member>)`
  (define a `#define DOC_<Class>(ARG) DOC(..., <Class>, ARG)` shortcut). Trailing macros
  `__PYCLASS_DEFAULT_COPY__/BINARY/PRINTING__(Class)`.
- Enums exposed with `nb::enum_<t_X>(subm,"t_X",DOC(...)).value("NAME", t_X::NAME, "doc")...`; option
  wrappers with `tools::nanobind_helper::make_option_class<o_X>(subm, "o_X")` — this registers the
  implicit `str`/`int`/enum→`o_X` constructors (a plain `nb::enum_` argument only accepts int + enum
  member, **never a string**). Python methods that take an identifier (e.g. `datagrams(type)`) should
  take **`o_X` and `switch (type.value)`**, so callers pass the enum, the record number, the name or the
  alt-name string interchangeably; pass `type` straight to the C++ `datagrams<T>(id)` (implicit convert).
- Docstrings are generated by `python make_pybind_doc.py` (walks the tree, writes
  `.docstrings/*.doc.hpp`); every public method gets an (empty) doc var so `DOC(...)` always resolves.
