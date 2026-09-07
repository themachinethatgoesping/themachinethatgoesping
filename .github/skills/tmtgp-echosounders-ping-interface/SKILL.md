---
name: tmtgp-echosounders-ping-interface
description: 'Recipe for the FIFTH implementation step of an echosounder file format in themachinethatgoesping/echosounders: implement read_pings() so the ping interface groups a file''s ping datagrams into pings and fills each ping''s file_data datagram index — WITHOUT yet decoding water column or bottom data. After this step fh.get_pings() returns pings and ping.file_data.datagrams() lists every datagram of that ping. Also enables ALL file-data interface inits in the file handler (environment/other/ping init empty/basic). Follows tmtgp-echosounders-navigation (the interface shells + navigation already exist). Worked example: s7k (group on 7000 SonarSettings). Reference: kmall (group MRZ/MWC by ping_counter). See tmtgp-echosounders-interfaces, tmtgp-cpp-class-style, tmtgp-cpp-nanobind-style, tmtgp-build-and-test.'
---

# Ping interface: read_pings + per-ping file_data (format step 5 of N)

Goal: after this step `fh = <Fmt>FileHandler(files)` builds with **all** file-data interfaces
initialized, `fh.get_pings()` returns one `<Fmt>Ping` per ping, and
`ping.file_data.datagrams()` (or `.datagrams("<Type>")`, `.datagrams_raw()`) lists every datagram
that belongs to that ping. Water column and bottom decoding are **not** done yet — this step only
assembles the per-ping datagram index so a user can *see* which datagrams make up a ping. Follows
**tmtgp-echosounders-navigation** (the six interface shells + minimal ping types already exist from
tmtgp-echosounders-interfaces, and navigation is implemented). Worked example: **s7k**; reference:
**kmall** (`read_pings` grouping `#MRZ`/`#MWC` by ping counter). Build/validate with
tmtgp-build-and-test.

## The ONE function you implement: `read_pings()`
The base `I_PingDataInterface::init_from_file` does everything else: for each primary file it calls
the per-file `init_from_file` + `init_file_interface_data()` (default no-op) + your
`read_pings(index_paths)`, then merges the per-file containers into `_ping_container` and **groups
the pings by `ping->get_channel_id()`** into `_ping_container_by_channel` (an auto-creating map, so
any non-empty channel id works). You only return a fully populated `<Fmt>PingContainer` for one file.

Override in `<fmt>pingdatainterfaceperfile.hpp` (replace the "not implemented" TODO):
```cpp
filedatacontainers::<Fmt>PingContainer<t_ifstream> read_pings(
    [[maybe_unused]] const std::unordered_map<std::string, std::string>& index_paths = {}) override
{
    using t_pingcontainer = filedatacontainers::<Fmt>PingContainer<t_ifstream>;
    using t_ping          = filedatatypes::<Fmt>Ping<t_ifstream>;
    using t_ping_ptr      = std::shared_ptr<t_ping>;

    // process this file's ping datagrams in file order (sort a COPY so grouping is robust to
    // whatever order _datagram_infos_all happens to be in).
    auto datagram_infos = this->_datagram_infos_all;              // vector<DatagramInfo_ptr>
    std::sort(datagram_infos.begin(), datagram_infos.end(), [](const auto& a, const auto& b) {
        if (a->get_file_nr() != b->get_file_nr()) return a->get_file_nr() < b->get_file_nr();
        return a->get_file_pos() < b->get_file_pos();
    });

    t_pingcontainer pings;
    t_ping_ptr      current_ping = nullptr;

    for (const auto& datagram_info : datagram_infos)
    {
        const bool starts_new_ping =
            datagram_info->get_datagram_identifier() == t_<Fmt>DatagramIdentifier::<PingAnchor>;

        if (starts_new_ping || current_ping == nullptr)   // also make the leading records a ping
        {
            current_ping = std::make_shared<t_ping>();
            current_ping->set_channel_id("0");            // single channel for now (config not read)
            current_ping->file_data().set_primary_file_nr(this->get_file_nr());
            pings.add_ping_no_reindex(current_ping);      // store the ptr, keep adding to it
        }
        current_ping->add_datagram_info(datagram_info);   // <-- populates ping.file_data index
    }

    pings.reindex();
    return pings;
}
```
Add `#include <algorithm>`. `read_pings` runs **before** the water column / bottom decoding, and this
version does **no file I/O at all** — it only regroups the already-indexed `DatagramInfo`s, so it is
fast and thread-safe (`init_from_file(..., mp_cores)` can process files in parallel).

## Why this works (the pieces already exist from step 3)
- `<Fmt>Ping::add_datagram_info(di)` (in `filedatatypes/<fmt>ping.hpp`) updates the ping timestamp and
  calls `_file_data->add_datagram_info(di)`. `<Fmt>PingCommon` initializes `_file_data =
  make_shared<<Fmt>PingFileData>()` inline, so a default-constructed ping already has a valid
  file_data. `<Fmt>PingFileData` **derives `<Fmt>DatagramInterface`**, so it *is* a datagram index and
  gets `datagrams()/datagrams_raw()/datagram_headers()` for free.
- `set_channel_id` (public on `I_Ping`) is **required**: the base groups pings by channel id, so it
  must be non-empty. Use `"0"` until the configuration interface provides real transducer ids.
- `PingContainer::add_ping_no_reindex(ptr)` + `reindex()` is the batch-add idiom (mirror kmall).

## Choosing the ping anchor (grouping key)
A "ping" is the set of records the sonar emits per transmit cycle. Group them by the record that
**starts each ping cycle** and is always present:
- **s7k**: `SonarSettings` (7000) — one per ping, first record of the cycle. Records without a
  ping_number (e.g. 7004 BeamGeometry, 7010 TVG) attach to the current ping by file order; records
  that *do* carry a ping_number (7000/7002/7027/7028/7042/7058, all with `u64 serial_number` @0 +
  `u32 ping_number` @8 in the RTH) also attach in file order — no parsing needed.
- **kmall**: `#MRZ` / `#MWC`, grouped by a `ping_counter` read cheaply from a **precomputed
  DatagramInfo "extra info"** (`get_extra_info<uint16_t>(0)`), not by file order. Use this pattern if
  the format stores an extra info during indexing.

Pick the anchor from the routing you already set in `callback_scan_packet` (the record types sent to
`_ping_interface`). Prefer **file-order anchoring on the ping-start record** (no I/O) over parsing a
ping_number out of every record. It is correct for single-head, sequentially-written files (the
common case) and needs zero datagram reads.

## Enable ALL interface inits in the file handler
Now that `read_pings` no longer throws, turn on every interface in `<fmt>filehandler.hpp`
`init_interfaces` (environment + other-file-data init "empty" via the generic
`I_FileDataInterface::init_from_file`, which only tracks datagrams and never throws; ping init groups
the pings). Mirror the navigation step's progress-bar accounting:
```cpp
auto n = _datagramdata_interface->per_primary_file().size();
progress_bar.init(0., double(2 * n + 4), "Initializing file interfaces");   // 4 manual + nav(n) + ping(n)
_datagramdata_interface->init_from_file(paths, force, progress_bar);  progress_bar.tick();
_configuration_interface->init_from_file(paths, force, progress_bar);  progress_bar.tick();
_navigation_interface->init_from_file(paths, force, progress_bar, true);          // ticks per file
_environment_interface->init_from_file(paths, force, progress_bar);   progress_bar.tick();
_otherfiledata_interface->init_from_file(paths, force, progress_bar);  progress_bar.tick();
_ping_interface->init_from_file(paths, force, progress_bar, true, mp_cores);      // ticks per file
progress_bar.close("Done");
```
Drop the `[[maybe_unused]]` on `force`/`progress_bar`/`mp_cores` now that they are used.

## nanobind (nothing new if step 3 is done)
The ping-type bindings from tmtgp-echosounders-interfaces already expose what you need:
`<Fmt>Ping.file_data` (`def_prop_ro` on `<Fmt>PingCommon::file_data`) and, on `<Fmt>PingFileData`,
`<Fmt>DatagramInterface_add_interface_functions<...>(cls)` (gives `datagrams()`, `datagrams("<Type>")`,
`datagrams_raw()`). The file handler already binds `get_pings` + `get_channel_ids`. So `read_pings`
lights up `fh.get_pings()[i].file_data.datagrams()` with no binding changes.

## Validate on real data
```python
fh = theping.echosounders.<fmt>.<Fmt>FileHandler(files, show_progress=False, mp_cores=4)
pings = fh.get_pings();  print(len(pings), fh.get_channel_ids())
p = pings[len(pings)//2]
print(p.get_timestamp(), p.get_datetime())
print(p.file_data.datagrams().count_datagrams_per_type())   # e.g. s7k {'7000':1,'7004':1,'7027':1,...}
```
Sanity: the per-ping type counts should be ~1 of each per-ping record (a clean 1:1 means the anchor
grouped correctly); `len(pings)` ≈ the count of the anchor record; timestamps increase monotonically.
s7k datasets: `kh1908` (7000/7004/7027/7028/7058 per ping), `thomaslake`/`ultfarms`
(7000/7027/7028/7042 per ping). Ignore any `index/` subfolder.

## Gotchas
- **`init_interfaces` could NOT call ping init before this step** (I_PingDataInterface::init_from_file
  processes file 0 outside try/catch → the old "not implemented" `read_pings` threw → the handler
  ctor threw). Implementing `read_pings` is exactly what unblocks enabling the ping init.
- **channel id must be non-empty** or the base's `_ping_container_by_channel.at(get_channel_id())`
  keys on `""` (works, but is meaningless). Use `"0"` for the first version.
- **Do not parse datagrams to group them.** The `DatagramInfo` already has type + position +
  timestamp; grouping only needs those. Parsing (especially water-column records) is slow and
  unnecessary here.
- **Stub bottom/watercolumn stay untouched.** `read_pings` must not call `ping.bottom()` /
  `ping.watercolumn()` getters (they still throw "not implemented"); it only fills the datagram index.
  `<Fmt>Ping::__printer__` (appends only `I_Ping::__printer__`) is safe; `ping.get_geolocation()` will
  throw until you set navigation/sensor-configuration on each ping (a later step).
- **File-order anchoring assumes each ping starts with the anchor record and is written
  contiguously.** Multi-head / multi-ping (interleaved anchors) or files lacking the anchor are not
  grouped precisely yet — acceptable for a first version; refine later by grouping on the record
  `ping_number` (+ serial/multiping) instead of pure file order.

## Next step
Fill each ping's data: set the sensor configuration + navigation interpolator on every ping (so
`get_geolocation()` works, mirror kmall), then implement the real `<Fmt>PingBottom` /
`<Fmt>PingWatercolumn` accessors (`read_pings` reading bottom detections / water-column images from
the grouped datagrams).
