---
name: tmtgp-cpp-class-style
description: 'General C++ class style for themachinethatgoesping (C++20 monorepo): file layout, naming (types/members/t_/o_ prefixes), class structure of a value/datagram class, getter/setter conventions, comments & pybind11_mkdoc docstrings, ObjectPrinter printing rules (print-name = getter name, processed sections, substruct container "(.accessor)" pattern), processed-member & physical-unit conventions (degrees/meters/seconds/dB, lat/lon, UTM), enums (OptionFrozen), and checksum/debug fields. USE when writing or reviewing ANY C++ class in themachinethatgoesping (echosounders, tools, navigation, gridding, pingprocessing, widgets, algorithms). For exposing the class to Python see tmtgp-cpp-nanobind-style; to build/test see tmtgp-build-and-test. Reference implementations: echosounders kongsbergall / kmall / s7k.'
---

# themachinethatgoesping C++ class style

The general (non-nanobind) conventions for every class in the monorepo. Match the surrounding file;
the notes below are the defaults. For the nanobind bindings see **tmtgp-cpp-nanobind-style**; to
build/test/install see **tmtgp-build-and-test**. Canonical examples: `subprojects/echosounders/.../s7k`,
`.../kmall`, `.../kongsbergall`.

## File layout
- **SPDX header** on every file. Code = `MPL-2.0`; tests / meson.build / generated = `CC0-1.0`.
  Copyright line: `// SPDX-FileCopyrightText: 2022 - 2025 Peter Urban, Ghent University`.
- Header: `#pragma once`, then `/* generated doc strings */ #include ".docstrings/<name>.doc.hpp"`.
- Include order: docstrings → `std` → external (`fmt`, `magic_enum`, `frozen`, `boost`, `xtensor`,
  `nanobind`) → `themachinethatgoesping/...` → local `"..."`.
- Namespaces (no indent inside), closed with `// namespace x` comments, e.g.
  `themachinethatgoesping::echosounders::<format>[::datagrams[::substructs]|::filedatainterfaces]`.

## Naming
- Types/classes `PascalCase`; functions & variables `snake_case`; **data members `_snake_case`**
  (leading underscore). This is **ping-wide** and applies to **every** private/protected member,
  **including the fields of a packed `#pragma pack` `Content`/record-type-header struct** (e.g.
  `struct Content { uint32_t _ping_number; ... } _content;`, accessed as `_content._ping_number`).
  mkdoc strips the leading `_`, so `_ping_number` still resolves via `DOC(...,Content,ping_number)`.
- `t_` prefix = enum / template type params (`t_S7KDatagramIdentifier`, `t_ifstream`).
- `o_` prefix = `OptionFrozen`/`Option` wrapper around an enum (`o_S7KDatagramIdentifier`).
- Getters/setters: `get_x()` / `set_x(v)`. Static factory: `from_stream`, `from_binary`.
- Prefer `o_X` (not the raw enum) as the working identifier type everywhere (auto str↔number↔enum).

## Class structure (value / datagram / record class)
- Members in a private/protected block; a fixed on-disk header/record goes in a `#pragma pack(push,1)`
  `struct Content { ... } _content;` (packed so `sizeof` == on-disk size). Value-init in the ctor
  (`: _content{}`) so an unset packed float never round-trips a NaN bit pattern.
- Public: clean `get_x()/set_x(v)` per field; `bool operator==(const T&) const = default;`;
  `from_stream(...)` / `to_stream(std::ostream&) const`; an `__printer__` (below); the macros
  `__CLASSHELPER_DEFAULT_PRINTING_FUNCTIONS__` and `__STREAM_DEFAULT_TOFROM_BINARY_FUNCTIONS__(T)`
  (`..._NOT_CONST__(T)` if `to_stream` is non-const).
- Read a fixed header in **one** `is.read(reinterpret_cast<char*>(&_first_member), __size)` — order
  members to match the on-disk byte order with natural alignment (no padding). Verify offsets.

## Comments & docstrings (feed pybind11_mkdoc)
- Members: trailing `///< short description` (on the **same line** as the whole declaration — a `///<`
  on the line after an initializer yields an EMPTY generated doc var).
- Classes/functions: `/** @brief ... @param ... @return ... */` (extracted into Python docstrings).
- Section separators inside a class: `// ----- section name -----`.
- Suppress a generated docstring with a line `// IGNORE_DOC:mkd_doc_...` before the entity.
- Keep comments to what the code cannot show; do not restate the next line.
- **Trivial passthrough `get_x`/`set_x` have an empty generated doc** — in the `.def` point the doc at
  the *variable* it returns (both getter and setter): direct member `_x` → `DOC(...,<Class>,x)` (mkdoc
  strips the `_`); packed field `_content.x` → `DOC(...,<Class>,Content,x)` (make the per-file `DOC_C`
  shortcut variadic). **A getter that PROCESSES the value (cast/scale/flag/unit) needs its own
  `/** @brief */` doc** and keeps `DOC(...,get_x)` — never point a processing accessor at an empty doc.

## Getters / setters & processed members (units)
Keep each raw on-disk field with a plain `get_x`/`set_x` in the raw unit. Then, in a
`// ----- processed data access -----` section, add **derived** getters that convert to physical /
engineering units. **Whenever a value carries a physical quantity there must be a member (raw or
processed) that exposes it in the canonical unit:**

| quantity | canonical unit | type | processed getter |
|----------|----------------|------|------------------|
| angle / beam width / steering | degrees | `float` | `get_<x>_in_degrees()` (rad→deg via `std::numbers::pi`, `#include <numbers>`) |
| distance / range / depth / offset | meters | `float` | `get_<x>_in_meters()` |
| time / duration / delay | seconds | `double` | `get_<x>_in_seconds()` |
| amplitude / magnitude / intensity | dB | `float` | `get_<x>_in_db()` |
| latitude / longitude | degrees | `double` | `get_<x>_in_degrees()` |
| UTM northing / easting | meters | `double` | (keep `double`) |

Rules:
- **If the raw field is already in the canonical unit, do NOT convert** — even if the on-disk dtype is
  "wrong" (e.g. a time already in seconds stored as `float` stays `float`; do not add a
  `_in_seconds` copy). Only add a processed getter when a **conversion** is needed.
- Values in **samples / counts / indices / flags** are not a physical unit → leave raw (converting
  samples→seconds needs a sample rate the object may not hold). If a unit is genuinely unclear
  (e.g. a bare "signal strength"), leave it raw and ask.
- **Per-element structs stay raw; the owning container provides the processed tensors.** A single
  `AttitudeSample` exposes only `get_roll()` (rad); its `AttitudeSampleContainer` exposes
  `get_roll_tensor()` (rad) **and** `get_roll_in_degrees_tensor()` (deg).

## ObjectPrinter printing (`__printer__`)
Implement `tools::classhelper::ObjectPrinter __printer__(unsigned int float_precision, bool
superscript_exponents) const` and register fields with `register_value / register_string /
register_container / register_section / append`.

**The printed field name MUST equal the getter name with the `get_` prefix removed** (keep every
other part, including a `_tensor` / `_in_degrees` / `_in_db` suffix). This lets a reader map a printed
line straight back to the accessor. Examples:

| getter | printed name |
|--------|--------------|
| `get_roll()` | `roll` |
| `get_roll_in_degrees()` | `roll_in_degrees` |
| `get_roll_tensor()` | `roll_tensor` |
| `get_roll_in_degrees_tensor()` | `roll_in_degrees_tensor` |
| `get_latitude_in_degrees()` | `latitude_in_degrees` |

- Only exception: the date/time block emitted from the shared datagram-header printer.
- **Never print a processed value under the raw field's name** (e.g. do not print
  `get_heading_in_degrees()` as `heading` next to the raw `heading` — it must be `heading_in_degrees`).
- Put raw fields in the record's content section; put all derived values in a
  `printer.register_section("processed")` block.
- **Printer title MUST use the `DatagramIdentifier` constant, not `get_datagram_identifier()`** — a
  default-constructed record has an `unspecified` id and `o_...(unspecified).name()` throws
  `"unknown key"` (the `info_string()` test then fails intermittently under Catch2's random order).

### Substruct containers print their fields (the `(.accessor)` pattern)
A per-beam/per-sample **container** (`std::vector<Row>` + `get_<field>_tensor()`; see
tmtgp-echosounders-record-parsers) prints **all of its tensors**, so a reader sees the data — do NOT
reduce a container's `__printer__` to a bare `number_of_x` count. Follow `AttitudeSampleContainer`:

```cpp
printer.register_section("Attitudes (.attitudes)");   // "<Plural> (.<vector accessor>)"
printer.register_value("attitudes (vector)", fmt::format("size={}", get_number_of_attitudes()),
                       "attitudes");
printer.register_container("delta_time_tensor", get_delta_time_tensor(), "ms");   // raw tensors
printer.register_container("roll_tensor",       get_roll_tensor(),       "rad");
// ...
printer.register_section("processed");                                            // processed tensors
printer.register_container("delta_time_in_seconds_tensor", get_delta_time_in_seconds_tensor(), "s");
printer.register_container("roll_in_degrees_tensor",       get_roll_in_degrees_tensor(),       "deg");
```

- The leading `register_section("<Plural> (.<accessor>)")` documents how the container is reached
  (e.g. `.attitudes`, `.beams`, `.devices`); it is printed both standalone and when the owning
  datagram `append`s the container's printer, which helps the user find the accessor.
- The owning datagram keeps its short grouping section (`register_section("beams")`) and then
  `printer.append(_beams.__printer__(...))`; the container supplies the detailed `(.beams)` section.
- Containers whose payload is variable-length / not a simple tensor (e.g. water-column amplitudes)
  still open with `register_section("<Plural> (.<accessor>)")` and then a short summary
  (`register_value` counts/flags) instead of tensors.

## Enums
- Small, contiguous values → plain `enum class : uintN_t` + `magic_enum` for name<->value.
- Large/sparse values (record numbers, 4-char codes) or **coded fields** (a field whose spec defines a
  small named set) → **`OptionFrozen`**: the enum plus three `inline constexpr std::array`s
  `_values`/`_names`/`_alt_names`, `using o_X = OptionFrozen<t_X, _values.size(), _values, _names,
  _alt_names>;`, and `extern template struct OptionFrozen<...>;` in the header with the matching
  `template struct ...;` in the `.cpp`. For a coded field store `o_x` **inside the packed struct** with
  the enum's underlying type matching the on-disk width (`enum class t_x : uint8_t` for a `u8`). Print
  with `register_string("x", _content._x.name(), _content._x.alt_name())`. `_names` (snake_case) and
  `_alt_names` (Capitalised / spec text) **must all be byte-distinct** (frozen-map keys).
- `o_X.name()`/`.alt_name()` **throw on an unknown value** → keep an identifier enum exhaustive, guard
  with `enum_contains()`, or keep the plain enum for graceful "unknown" handling (an interface map key
  / virtual signature stays the plain enum so unrecognised records still index).
- **Bit-field** flags (many independent bits) stay a raw `u32`; expose useful bits as `bool
  get_<flag>()` and print the raw value as `fmt::format("0b{:032b}", _content._flags)`.

## Checksum / debug-only integrity fields
Store a trailing integrity word (so `len(to_binary()) == size`) and **round-trip the stored value** —
never (re)compute it during normal read/write. Provide compute/read/compare as `static` helpers that
take the serialized buffer (`std::string_view`).

## C++ tests (catch2)
- `src/tests/<area>/.../<name>.test.cpp`; `#define TESTTAG "[<area>]"`; `TEST_CASE("...", TESTTAG)`
  with `REQUIRE`/`CHECK` (`Catch::Approx` for floats). Standard checks: copy `x == T(x)`, binary
  `x == T::from_binary(x.to_binary())`, stream round-trip, `x.info_string().size() != 0`; for parsers
  build a byte buffer and assert decoded fields. Register the file in `src/tests/meson.build`.
