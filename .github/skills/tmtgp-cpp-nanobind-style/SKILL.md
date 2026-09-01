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

## Datagram / value classes (pattern)
- `using t_DatagramIdentifier = ...;` and `static constexpr size_t __size = <header bytes>;`
  (note: real `sizeof` is larger because of the vtable).
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
- One template function `py_create_class_<x><T_FileStream>(module&, name)`; register for both stream
  types with names `"<Class>"` (MappedFileStream) and `"<Class>_stream"` (`std::ifstream`).
- Reuse helpers: `py_filetemplates::py_i_inputfilehandler::add_default_constructors /
  add_open_file_interface / add_default_containers` (adds the `datagram_interface` property);
  `py_i_datagraminterface::add_InterfaceFunctions`; `py_datagramcontainer::create_DatagramContainerTypes`.
- Docstrings via `DOC(themachinethatgoesping, echosounders, <format>, <Class>, <member>)`
  (define a `#define DOC_<Class>(ARG) DOC(..., <Class>, ARG)` shortcut). Trailing macros
  `__PYCLASS_DEFAULT_COPY__/BINARY/PRINTING__(Class)`.
- Enums exposed with `nb::enum_<t_X>(subm,"t_X",DOC(...)).value("NAME", t_X::NAME, "doc")...`; option
  wrappers with `tools::nanobind_helper::make_option_class<o_X>(subm, "o_X")`.
- Docstrings are generated by `python make_pybind_doc.py` (walks the tree, writes
  `.docstrings/*.doc.hpp`); every public method gets an (empty) doc var so `DOC(...)` always resolves.
