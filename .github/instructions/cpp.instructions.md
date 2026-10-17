---
applyTo: "**/*.{hpp,cpp,h,c,cc,cxx}"
---

# C++ style for *themachinethatgoesping*

Apply these rules to all C++ code. They reflect the existing conventions — match
them instead of introducing new patterns.

## Formatting
- Formatting is defined by the repository `.clang-format` (custom, Mozilla-based).
  Always run clang-format; never hand-format against it.
- 4-space indentation, no tabs, 100-column limit.
- Braces on their own line for functions, classes, structs, enums and control
  statements (custom `BreakBeforeBraces: Custom`).
- Pointer/reference bind to the type (`int* p`, not `int *p`).
- One parameter/argument per line when they don't fit (`BinPack*: false`).

## Language & layout
- Standard is **C++23** (`cpp_std=c++23`); requires gcc ≥ 14 or clang ≥ 18.
- Start every file with the correct SPDX header (`MPL-2.0` for source).
- Headers use `#pragma once`.
- Immediately after the SPDX header (in headers), include generated docstrings:
  `#include ".docstrings/<name>.doc.hpp"`. Do not hand-edit files under
  `.docstrings/` — they are generated.
- Namespaces follow the directory: `themachinethatgoesping::<module>::<submodule>`.
- File names are lowercase, matching the primary type/topic (`i_interpolator.hpp`).

## Naming
- Classes: `PascalCase`. Interface/abstract classes are prefixed `I_`
  (e.g. `I_Interpolator`).
- Enums: prefixed `t_` (e.g. `t_extr_mode`); their option-wrapper aliases use
  `o_` (e.g. `using o_extr_mode = classhelper::Option<t_extr_mode>;`).
- Template parameters: descriptive with `t_` prefix (`t_float`) or short
  capitalized names (`XType`, `YType`).
- Private/protected members: leading underscore (`_extr_mode`).

## Documentation
- Use Doxygen block comments with `@brief`, `@param`, `@tparam`, `@return`, and
  `@authors` where appropriate — see existing headers for the exact form.

## Class conventions
- Printable/serializable classes provide
  `classhelper::ObjectPrinter __printer__(unsigned int float_precision, bool superscript_exponents) const;`
  and use the `__CLASSHELPER_DEFAULT_PRINTING_FUNCTIONS__` macro to generate
  `info_string`, `print`, `to_binary`, `from_binary`, `copy`, and comparison.
  Keep this pattern when adding new value/data classes.

## Python bindings
- Bindings live under `src/nanomodule/**` (nanobind; some legacy pybind11 under
  `*_pybind`). Register submodules with the `init_m_<name>(module_& m)` /
  `init_c_<name>(module_& m)` pattern already used in the `module.cpp` files.

## Testing
- C++ tests use **Catch2** (`TEST_CASE` / `TEMPLATE_TEST_CASE`) and live in each
  submodule's `src/tests/`. Define a `TESTTAG` and tag test cases with it, as in
  the existing tests. Build/run with `meson test -C builddir/`.
