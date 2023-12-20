# Changelog

Ping is still in the bootstrapping phase, thus changes will be frequent and not always documented. 
Once the project is more stable, this changelog will be updated more frequently.

Versioning scheme is currently based on my mood, but will be changed to [Semantic Versioning](https://semver.org/) once the project is more stable. I do not create tags for the versions as none of them are stable enough to be considered a release.


---


## [0.16.0] - 2023-12-20

- echosounders -> 0.33.0
- pingprocessing -> 0.5.0
- tool -> 0.21.7
- navigation -> 0.15.0
- algorithms -> 0.6.0

### Added

- pingprocessing:
  - split_pings.by_time_blocks function
- navigation:
  - compute_latlon_distance_m between lat lon points function
  - compute_latlon_distances_m between lat lon points (vectors)
  - cumulative_latlon_distances_m of lat lon vectors
  - above functions for GeolocationLatLon and SensordataLatLon

### Changed

- echosounders:
  safe sample_interval instead of sampling_frequency
  pingtools: allow explicit casting from beamsampleslection to beamselection
- navigation:
  Renamed GeoLocation -> Geolocation
  Renamed Sensordata -> Sensordata

### Fixed

- echosounders:
  - Do not crash when trying to open empty file
  - get_sample_interval only available for water column data (means something different for bottom data)
  - kongsbergallping.bottom.get_xyz(selection) : incorrect memory access error
- adapted to navigation 0.15.0
  - algorithm
  - echosounders
  - pingprocessing
  

### Updated

- tools:
  - xsimd 12.1.0 -> 12.1.1
  - xtl 0.7.5 -> 0.7.6
  - fast_float 5.3.0 -> 6.0.0

## [0.15.1] - 2023-12-12

- algorithms -> 0.5.5
- pingprocessing -> 0.4.1
- echosounders -> 0.32.1
- tool -> 0.21.6

### Added

- algorithms:
  - signalprocessing::datastructures::CWSignalParameters
  - signalprocessing::datastructures::FMSignalParameters
  - add hash tests
- echosounders:
  - rawrangeandangletransmitsector: get_transmit_signal_type
  - kongsbergall: add systeminformation structure
  - load_sys to file_data and to kongsbergallbottom
  - add tx_signal_parameters accessor ti I_PingCommon
  - add get transmit sector information to kongsbergallpings
  - has_any_of and all_of_features to i_pingcommon
  - kongsbergallampltiudeconverter class
  - beamsampleselection::get_sample_numbers_as_vector and get_sample_numbers_ensemble
  - i_pingwatercolumn: get_soundspeed_at_transducer
  - kongsbergallpingwatercolumn: get_tvg_offset, get_tvg_factor
  - get_av function for kongsbergallpingwatercolumn
- pingprocessing
  - add split_ping by_function_return function

### Fixed

- pingprocessing: 
  - nav_plot for >100.000 elements

### Changed

- echosounders
  - rework watercolumninformation structure
  - consistently use center_frequency instead of centre_frequency
  - reduce i_ping printing verbosity
  - specialized structure for interesting water column datagram information that can be deduplicated
- tools
  - updated xsimd 0.12.0 -> 0.12.1
  - updated catch2 3.4.0 -> 3.5.0

## [0.15.0] - 2023-12-01

- pingprocessing -> 0.4.0
- echosounders -> 0.32.0
- tools -> 0.21.5
- navigation -> 0.14.2
- algorithms -> 0.5.4

### Added

- pingprocessing: group_pings.by_dual_head() function
- pinggrocessing: split_pings.by_file_path function
- echosounders: add index_functions.find_folders_with_files function

### Changed

- echosounders: index_functions.find_files
  - Path folders can now be string, path or list of strings or paths
  - File extensions can now be string or list of strings
  - add followlinks argument to follow symbolic links
  - find_files: delay for progressbar is now 3 seconds
  - distinguish between main and normal features
- updated xsimd 0.11.2 -> 0.12.0
  - This fixes a lot of compiler warnings for gcc 13.2

### Breaking

- echosounders
  - breaking: removed get_file_path and get_file_number to ping raw_data
  - added get_file_paths and get_file_numbers to ping raw_data
  - added get_primary_file_path and get_primary_file_number to ping raw_data
  - renamed RawData and raw_data to FileData and file_data
- pingprocessing
  - adapted to echosounders v.0.32 changes

### Performance

- echosounders
  - removed unnecessary strings from ping classes to reduce memory usage

### Fixed

- echosounders: circular shared_ptr memory leak in KongsbergAllFileHandler

### internal

- renamed get_name() to class_name()

## [0.14.1] - 2023-11-16

- pingprocessing -> 0.3.4

### Added

- pingprocessing: filter.by_features() function
- pingprocessing: split.by_channel_id() function

### Fixed

- added comments for pingprocessing functions

## [0.14.0] - 2023-11-16

### Modules

- echosounders -> 0.31.0
- pingsprocessing -> 0.3.3
- tools -> 0.21.4
- navigation -> 0.14.1

### Breaking

- echosounders: reworked pings() function
  - pings() now returns pings sorted by time by default
  - removed pings('channel_id') functions

### Added

- pingprocessing:
  - functions to filter pings by time and region
  - functions to calculate ping statistics
  - functions to split pings by time or distance difference
  - navigation plotting functions

### Fixed

- navigation: wrong argument name for initializing GeolocationUTM

### Update subproject wraps

- tools:[magic_enum] -> 0.9.5

## [0.13.0] - 2023-11-15

### Modules

- echosounders -> 0.30.0

### Breaking

- echosounders: Namespace and file renaming
  - em3000 -> kongsbergall
  - simrad -> simradraw
  - InputFile -> InputFileHandler
  - FileEm3000 -> KongsbergAllFileHandler
  - FileSimradRaw -> SimradRawFileHandler
  - simradraw_datagrams.hpp -> datagrams.hpp
  - simradraw_types.hpp -> types.hpp
  - kongsbergall_datagrams.hpp -> datagrams.hpp
  - kongsbergall_types.hpp -> types.hpp


### Update subproject wraps

- tools:[fast_float] -> 0.5.3
- tools:[magic_enum] -> 0.9.4
- tools:[xsimd]      -> 0.11.2


## [0.12.4] - 2023-11-15

- started change log


---


# Notes

The datum format used is [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD).

We use the following tags based on [keepachangelog.com](https://keepachangelog.com/en/1.1.0/):

### Breaking
- `Breaking` for changes that will break existing functionality.

### Added
- `Added` for new features.

### Changed
- `Changed` for changes in existing functionality.

### Deprecated
- `Deprecated` for soon-to-be removed features.

### Removed
- `Removed` for now removed features.

### Fixed
- `Fixed` for any bug fixes.

### Security
- `Security` in case of vulnerabilities.

Additionally, we use the following tags:

### Breaking
- `Breaking` for changes that will break existing functionality and thus require a major version change.