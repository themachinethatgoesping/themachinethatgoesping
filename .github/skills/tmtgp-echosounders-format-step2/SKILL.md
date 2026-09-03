---
name: tmtgp-echosounders-format-step2
description: 'Recipe for the SECOND implementation step of an echosounder file format in themachinethatgoesping/echosounders: implement the individual per-record (datagram) classes that parse each record type into typed fields, with nanobind bindings, per-type containers and typed datagram_interface.datagrams(type) access (kmall parity). Follows step1 (header + indexing). Worked example: the s7k records (src/.../echosounders/s7k/datagrams). Covers fixed-header records (pragma-pack block read) and, for fast reading, per-beam/per-sample records via packed substruct + container classes (bulk read, arrays converted on access) and variant sample containers (simradraw RAW3 parity), with skip=store-file-position+lazy re-read. USE when adding record parsers to a bootstrapped format. See tmtgp-echosounders-format-step1, tmtgp-cpp-nanobind-style, tmtgp-build-and-test.'
---

# Step 2: per-record datagram classes

Each record type becomes a class deriving `<Fmt>Datagram` (the header). Reference: s7k `datagrams/`
(SonarSettings = fixed; RawDetection/Snippet/CompressedWaterColumn = per-beam arrays). Mirror kmall
(SPosition fixed; MWCRxBeamData water column). Build/validate after every wave (tmtgp-build-and-test).

## Class pattern
```cpp
class <Rec> : public <Fmt>Datagram {
  public:
    static constexpr auto DatagramIdentifier = t_<Fmt>DatagramIdentifier::<ENUM>;
  protected:
#pragma pack(push, 1)                 // records are PACKED (fields often mis-aligned)
    struct Content { <RTH fields in on-disk order>; bool operator==(const Content&) const = default; } _content;
#pragma pack(pop)
    static constexpr size_t __content_size = sizeof(Content);
    // per-beam / per-sample data: hold a substructs::<Rec>...Container member (bulk read, arrays
    // converted on access) -- see "Fast per-beam / per-sample records" below. Do NOT keep parallel
    // xt::xtensor arrays filled with an element-by-element loop.
  public:
    <Rec>() : _content{} { set_datagram_identifier(DatagramIdentifier); } // fixed records
    // getters get_x() -> _content.x; array getters return const xt::xtensor&
    bool operator==(const <Rec>&) const = default;
    static <Rec> from_stream(std::istream&, <Fmt>Datagram header);   // + (is) and (is, o_DatagramIdentifier id) overloads
    static <Rec> from_stream(std::istream& is) { return from_stream(is, <Fmt>Datagram::from_stream(is)); }
    void to_stream(std::ostream&) const;
    tools::classhelper::ObjectPrinter __printer__(unsigned int, bool) const;
    __CLASSHELPER_DEFAULT_PRINTING_FUNCTIONS__
    __STREAM_DEFAULT_TOFROM_BINARY_FUNCTIONS__(<Rec>)   // const to_stream
  private:
    explicit <Rec>(<Fmt>Datagram header) : <Fmt>Datagram(std::move(header)) {}
    void __read__(std::istream& is);   // reads _content then arrays
};
```
- Fixed-RTH read: `is.read(reinterpret_cast<char*>(&_content), __content_size);`.
- Array read: `arr.resize({N}); is.read(arr.data(), N*sizeof(T));` (contiguous), or a per-element loop
  using a `#pragma pack(1)` element struct then `arr.unchecked(i) = ...`.
- Printer: `register_value(name,val,unit)` for scalars; `register_container(name, tensor, unit)` for arrays.
- Include `<xtensor/containers/xtensor.hpp>` in the header.
- **Generate the repetitive fixed-RTH classes** from a compact field spec (see the s7k throwaway
  generator `/tmp/gen_s7k_records.py`): emits hpp+cpp+binding consistently for many records at once.

## Fast per-beam / per-sample records: substruct + container (PREFERRED over parallel arrays)
For records with per-beam or per-sample data, do **NOT** resort the on-disk records into several
parallel `xt::xtensor` members with an element-by-element loop (slow: it reads/copies field by
field). Keep the in-memory layout **as close to the on-disk layout as possible** and convert to
arrays only on access. Reference: kmall `datagrams/substructs/` (`MRZSoundings` +
`MRZSoundingsContainer`, `MWCRxBeamData`), simradraw `raw3datatypes/` (variant sample types); s7k
`datagrams/substructs/` is the worked example (7027/7028/7042/7004/1016/7200). Put substructs in
`datagrams/substructs/`; each substruct **and** each container gets its own `.hpp` (+ `.cpp` for the
container's out-of-line tensor accessors).

- **Row substruct** (AoS on disk): `#pragma pack(push,1)` class, private members in on-disk order,
  `get_/set_` accessors, inline `__printer__`, `operator==(...) = default`,
  `__CLASSHELPER_DEFAULT_PRINTING_FUNCTIONS__`. `static_assert`/comment its `sizeof` == on-disk
  stride so the bulk read is correct.
- **Container**: holds `std::vector<Row>`; `get_<rows>()/rows()/set_<rows>()` for raw struct access
  **plus** `get_<field>_tensor()` built on demand via a private `build_tensor<ValueType>(getter)`
  template (`xt::xtensor<V,1>::from_shape({n})` + `unchecked` loop). The datagram holds the container
  and exposes it via `def_prop_rw` — no flat arrays on the datagram.
- **Bulk read** (in the datagram `__read__`): read straight into the final storage, no intermediate
  buffer/`memcpy`. Full-width AoS: `vec.resize(n); is.read(reinterpret_cast<char*>(vec.data()),
  n*sizeof(Row));`. Variable per-record stride (e.g. s7k 7027 `data_field_size`, made `const` before
  the loop): if `dfs == sizeof(Row)` do the single bulk read above; **else** loop and read each beam
  directly into `&vec[i]` (`is.read(&vec[i], min(dfs,sizeof(Row)))`, seek the extra bytes if
  `dfs>sizeof(Row)`, set version-dependent missing fields to NaN). Never read the whole block into a
  scratch `std::vector<char>` and `memcpy` it out.
- **SoA on disk** (per-field arrays already contiguous, e.g. s7k 7004 BeamGeometry): the data is
  *already* in the array form we want, so keep the `xt::xtensor<..,1>` members **directly on the
  datagram** and bulk-read each array (`arr.resize({n}); is.read(arr.data(), n*sizeof(T))`). Do NOT
  wrap SoA arrays in a container/substruct — it adds indirection and zero read-speed benefit.
- **Variable-length samples / water column**: **read directly into the final per-beam storage** —
  do NOT read the whole record into a scratch buffer and `substr`/`memcpy` it out. Two styles:
  (a) samples contiguous with a fixed datagram-wide dtype (s7k 7028): store a flat
  `std::variant<xt::xtensor<u16,1>, xt::xtensor<u32,1>>` + `xt::xtensor<uint64_t,1>` beam offsets,
  read the header block and the sample block each in one `is.read`; per-beam / list / dB conversions
  computed on demand (like simradraw RAW3's variant). (b) interleaved per-beam blocks with
  flag-driven dtype (s7k 7042): loop over beams and let **each beam read itself** from the stream
  (`beam.read(is, has_segment, stride)` reads its header fields + `is.read` of its raw sample block
  straight into `beam._raw_samples`). Store the record-wide sample **encoding once on the container**
  (`set_magnitude_bytes/has_phase/...`), NOT on every beam — the beam should reflect only the binary
  (beam number, count, raw bytes); the container decodes magnitude/phase from the raw bytes on demand.
- **skip_data = store file position + lazy re-read** (kmall `MWCRxBeamData` style): on skip, record
  `is.tellg()` in the container (`set_skipped(pos)`), seek past the samples, leave the sample arrays
  empty; expose `get_samples_are_skipped()/get_sample_position()` and a `read_samples(std::istream&)`
  that seeks back and parses. `datagrams(type, skip_data=true)` uses the skip factory.
- **Bindings**: one file per substruct + per container under `py_<fmt>/py_datagrams/substructs/`.
  Substruct file: `NB_MAKE_OPAQUE(std::vector<Row>)` + bind all `get_/set_` + end with
  `nb::bind_vector<std::vector<Row>>(m, "<Row>s_vector")`. Container file: `def_prop_rw` for the raw
  vector (`nb::rv_policy::reference_internal`) + one `.def` per `get_<field>_tensor` (needs
  `<xtensor-python/nanobind/pytensor.hpp>`; variant returns need `<nanobind/stl/variant.h>`).
  Register every `init_c_<sub>` in `py_datagrams/module.cpp` **before** the datagrams that expose them.

### Gotchas that cost real debugging time
- **Printer title MUST use the `DatagramIdentifier` constant, not `get_datagram_identifier()`.** A
  default-constructed record (array records use `= default`, so no `set_datagram_identifier`) has an
  `unspecified` id; `o_<Fmt>DatagramIdentifier(unspecified).name()` throws `"unknown key"`, and the
  `info_string()` test then fails (intermittently, because Catch2 randomizes case order).
- **mkdoc cannot parse `std::vector<xt::xtensor<...>>`-returning getters** → no doc symbol is
  generated and `DOC(...)` fails to compile. Give those `.def`s a plain string-literal docstring.
  Single `xt::xtensor<..>` returns are fine.
- **NaN-filled version-dependent fields break `operator==` round-trip** (`NaN != NaN`). Test the
  round trip at the byte level (`to_binary()` bytes equal) or construct with the full field size.
- Keep container/substruct `__printer__` to `register_value` summaries (counts, flags); don't dump
  every array with `register_container` there.

## Critical correctness rules (learned the hard way)
1. **Per-beam stride = the on-disk *_field_size / data_field_size field, NOT the MB-System struct
   sizeof.** Read exactly that many bytes per beam into a buffer and memcpy fields at fixed offsets;
   fill trailing (version-dependent) fields with NaN when the stride is short. (s7k 7027 is 26 bytes
   in the field, not the 34 the MB-System struct suggests.)
2. **`nalloc` in MB-System structs is an in-memory allocation counter — it is NOT on disk.** Do not
   read it.
3. **Water-column ordering differs per record.** s7k 7028: all N beam-headers first, then the
   concatenated per-beam samples. s7k 7042: per-beam interleaved (header then that beam's samples),
   with the sample dtype (mag/phase bit depth) selected by the flags bit field. Always confirm the
   on-disk layout against the spec, not just a C struct.
4. Records are **packed** — use `#pragma pack(push,1)` on the `Content` struct so `sizeof` == on-disk
   size (unlike the naturally-aligned DRF header).

## Wiring each record (checklist)
- `datagrams.hpp`: `#include "datagrams/<rec>.hpp"` + add `<Rec>` to `t_<Fmt>DatagramVariant`.
- `datagrams.cpp`: add a `case <ENUM>: return t_<Fmt>DatagramVariant(<Rec>::from_stream(is, type));`.
- **class binding = its own file** `py_<fmt>/py_datagrams/c_<rec>.cpp` (one per datagram, like kmall);
  declare + call `init_c_<rec>` in `py_datagrams/module.cpp`:
  `nb::class_<<Rec>, <Fmt>Datagram>(m,"<Rec>",DOC(...)).def("get_x",&<Rec>::get_x,DOC_C(<Rec>,get_x))...`
  `__PYCLASS_DEFAULT_COPY__/BINARY/PRINTING__(<Rec>)`. For xtensor getters `#include
  <xtensor-python/nanobind/pytensor.hpp>`; for `std::vector<xtensor>` getters `#include
  <nanobind/stl/vector.h>`. (`DOC_C(CLASS,ARG) = DOC(...,<fmt>,datagrams,CLASS,ARG)` is the per-format shortcut.)
- container binding (`py_<fmt>/py_filedatacontainers/c_<fmt>datagramcontainer.cpp`):
  `create_DatagramContainerTypes<datagrams::<Rec>, t_<Fmt>DatagramIdentifier>(m, "<Fmt>DatagramContainer_<Rec>");`.
- interface binding (in the `py_<fmt>/py_filedatainterfaces/c_<fmt>datagraminterface.hpp` template): the
  `datagrams(type, skip_data=false)` argument is **`o_<Fmt>DatagramIdentifier`** with `switch (type.value)`;
  add `case <ENUM>: return nb::cast(self.template datagrams<datagrams::<Rec>>(type));`
  (so `datagrams(t_id.<ENUM>)`, `datagrams(<number>)`, `datagrams("<ENUM>")` and `datagrams("<number>")`
  all return typed objects; `type` passes straight to the C++ `datagrams<T>(id)` via implicit conversion).
- meson: register the binding `.cpp` (under its `py_<fmt>/py_*/` submodule dir) in the nanomodule
  meson.build; register the C++ `.cpp`/`.hpp` + `.docstrings/<rec>.doc.hpp` (placeholder) in the src meson.build.
- test: `src/tests/<fmt>/datagrams/<fmt>records.test.cpp` — default-construct, set fields, assert
  copy/binary/stream round trips and `info_string().size() != 0`.

## skip_data for water-column records (kmall parity)
Large water-column records get a fast metadata-only read path (like kmall's `MWaterColumn`):
- Add `<Fmt>SkipDataFactory<t_datagram>` + `<Fmt>SkipDataVariantFactory` to `datagrams.hpp` (mirror
  `KMALLSkipDataFactory`): each forwards to `t_datagram::from_stream(is[, type], true)`.
- Every WC-record `from_stream` overload gets a trailing `bool skip_data = false` (replace the plain
  `from_stream(is)` with `from_stream(is, bool skip_data = false)` to avoid ambiguity), forwarded to
  `__read__(is, skip_data)`. In `__read__`, when `skip_data`: read the RTH `_content`, then
  `is.seekg(std::streamoff(compute_size_content()) - std::streamoff(__content_size), std::ios::cur)`
  to land at the record end, leaving the sample arrays empty (RTH metadata stays available). Simpler
  than kmall's lazy-load-on-demand — a skipped record can't be re-serialised.
- `datagrams.cpp` variant dispatch: forward `skip_data` to the WC cases only.
- container: also register `..._<Rec>_SkippedData` (`<Rec>` + `<Fmt>SkipDataFactory<<Rec>>`) and
  `..._Variant_SkippedData` (`<Fmt>SkipDataVariantFactory`).
- interface template: the no-arg `datagrams(skip_data=false)` picks the variant vs skip-variant factory;
  the typed `datagrams(type, skip_data=false)` WC cases branch `if (skip_data)` to the skip factory.

## Docstring pitfall
`pybind11_mkdoc` (libclang) **cannot parse getters that return `std::vector<xt::xtensor<...>>`** — it
aborts the class parse, so `DOC()` vars are missing for that getter and every method declared after
it. Use a plain string literal docstring for those getters (and keep them last in the class if possible).

## Validate on real data
Parse a real file and sanity-check physical values (frequency in Hz, lat/lon in radians → sensible
degrees, angles in radians, sample counts). Wrong byte offsets show up as NaN/inf/garbage.
