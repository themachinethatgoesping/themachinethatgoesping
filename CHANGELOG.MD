# Changelog

Ping is still in the bootstrapping phase, thus changes will be frequent and not always documented. 
Once the project is more stable, this changelog will be updated more frequently.

Versioning scheme is currently based on my mood, but will be changed to [Semantic Versioning](https://semver.org/) once the project is more stable. I do not create tags for the versions as none of them are stable enough to be considered a release.

---
## [0.23.1] - 18-06-2024

- tools -> 0.24.1
- echosounders -> 0.39.1

### Maintenance (breaking)

- adapted flat_map library because there seems to be a flat_map bug in boost 1.83

## [0.23.0] - 17-06-2024

- tools -> 0.24.0
- navigation -> 0.16.0
- algorithms -> 0.8.0
- echosounders -> 0.39.0
- pingprocessing -> 0.8.0
- gridding -> 0.2.0

### Maintenance (breaking)

- minimum numpy version is now 2.0

### Fixed

- echosounders:
  - SeabedImageData: comparison operator did not handle nan/inf values


## [0.22.2] - 17-06-2024

- minor updates and fixes to tests

## [0.22.0] - 17-05-2024

- pingprocessing -> 0.7.0
- echosounders -> 0.38.1
- tools -> 0.23.1

### Added

- pingprocessing:
  - echogrambuilderclass
  - echogramsection: added plotting function
  - echogramdata class that can convert pings to images
  - Added ImageBuilder class to conviniently handle different cases for plotting watercolumn images
  - make_wci_stack: support different progressbars using make_iterator function
  - add wciviewer widget
  - add sv/av plotting option
- tools:
  - float_equal comparison function that allows for a relative tolerance and nan/inf handling

### Changed

- echosounders:
  - do not use lat/lon as depth sensor offsets anymore

### Fixed

- echosounders (flickery tests):
  - extradetections datagram: operater== handle nan/inf values
  - xyzdatagram: operater== handle nan/inf values
  - RAW3 flickery test: init float array to avoid nan/inf value comparison

### Maintenance

- tools:
  - update xsimd: 12.1.1 -> 13.0.0
  - update catch2: 3.5.4 -> 3.6.0

### [0.21.0] - 23-04-2024

- tools -> 0.23.0
- echosounders -> 0.38.0
- navigation -> 0.15.3
- pingprocessing -> 0.6.0
- algorithms -> 0.7.0

## Changed

- tools:
  - vectorinterpolators now support float and double
- algorithms:
  - changed backtracer interface to support multithreading and simpler initialization

## Added

- tools:
  - py_NearestInterpolator: also support int py object
  - get_y_const: interpolation function to allow usage of interpolators in multithreaded environments
- echosounders:
  - WaterColumnCalibration structure
  - conversion to sv (kongsberg all)
  - available_features() and available_feature_groups() function for i_pingcommon
- pingprocessing:
  - make_wci: support av,sv and amp
  - make_wci_dual_head: now takes ping groups
  - make_wci: faster version (currently make_wci2)

## Fixed

- navigation
  - memory error when accessing empty mode for gll,rmc and vtg datagrams
- tools
  - vectorinterpolators::extent function did not check for nan/inf errors
  - binary/hashing stability for vectorinterpolators

## Maintenance

- tools:
  - update fast_float: 6.1.0 -> 6.1.1
  - pybind11 2.11.1 -> 2.12.0
  - Catch2 3.5.3 -> 3.5.4
  - xxhash_cpp -> git/master branch hopefully fixes arm/neon builds (e.g. macos)

## [0.20.1] - 2024-03-07

- tools -> 0.22.4
- echosounders -> 0.37.1
- navigation -> 0.15.2
- pingprocessing -> 0.5.5

### Added

- pingprocessing
  - echogramsection: get_downsampled function to reduce number of samples per beam (for plotting)

### Fixed

- tools
  - ObjectPrinter: Do not print empty line if no value_infos are to be printed
- echosounders
  - renamed bottomrange sample to bottomrange samples
  - throw warning instead of error if sensor configuration could not be read from file
  - printing ping in case geolocation is not available
  - update sensor configuration after reading navigation interpolator from file to avoid configuration missmatch after caching
- navigation
  - indicate that Geolocation, Positional offsets and SensorLocation are structs when printing
- pingprocessing
  - fixed get_ping_times_datetimes function in echogram section

### Maintenance

- tools
  - updated Catch2 -> 3.5.2 -> 3.5.3

## [0.20.0] - 2024-02-29

- echosounders -> 0.37.0
- algorithms -> 0.6.0
- tools -> 0.22.3
- pingprocessing -> 0.5.4

### Added

- pingprocessing
  - create echogram groups functions
- tools
  - add rpy to/from quaternion (as alternative to ypr to/from quaternion)

### Changed

- echosounders
  - MemoryMapped IO is now the default, iostream is available via FileHandler_stream
  - Restructure PingFeatures into features and feature groups
  - Improve printing for PingFeatures
- algorithms
  - TXSignalParameters are now classes with getters and setters instead of structures
- tools
  - ObjectPrinter: put value info in the next line if line with value info is > 150 characters

### Internal

- echosounders
  - Reworked pingfeatures: use enum instead of std::string
  - Reworked pingfeatures: do not safe features twice
  - Reworked pingfeatures: replace unordered_map with flat_map to safe memory

## [0.19.0] - 2024-02-22

- echosounders -> 0.36.0
- navigation -> 0.15.1
- algorithms -> 0.5.9

### Changed

- echosounders:
  - Throw error when trying to initialize handler with empty list of files
  - tx_signal_parameters and number_of_tx_sectors features are now exclusively features of ping.bottom and ping.watercolumn
  - FileHandler.pings() method is renamed to FileHandler.get_pings()
  - FileHandler.channel_ids() method is renamed to FileHandler.get_channel_ids()
  - Ping: timestamp, channel_id, geolocation, sensor_data, datetime and sensor configuration are now features
  - NavigationDataInterface: has_sensor_data function (to check if sensor data is available for a specific SensorConfiguration)

### Added
- echosounders:
  - Ping: set_geolocation function (not sure if this method will remain like this)
- navigation:
  - SensorConfiguration has_target function to check if a target_id has been added
  - valid() function for navigationinterpolators (latlon and local)

### Fixed
- navigation:
  SensorConfiguration hash changed when writing/reading to binary because the order of the targets is not guaranteed
- echosounders:
  - avoid duplicate sensor configuration hashing in ping initialization
  - avoid duplicate sensor configuration hashing in navigation interpolation
  - check navigation validity before trying to access it
  - reading error for sensorconfiguration cache
- algorithms:
  - reading error for sensorconfiguration cache


## [0.18.2] - 2024-02-22

- echosounders -> 0.35.2
- tools -> 0.22.2
- algorithms -> 0.5.8
- pingprocessing -> 0.5.3

### Changed

- pingprocessing:
  - plot_navigation: argument survey_name -> label
  - nav_plot: create_figure add capability to plot background image
- echosounders:
  - KongsbergAllPingWatercolumn: get_av do not correct for pulse length if transmit Pulse is Generic or FM
    - Note: Generic happens if RawRangeAndAngle datagram is not available

### Added

- algorithms:
  - signalprocessing::datastructures::TxSignalParameters: add comparison operator that accounts for nan
- pingprocessing:
  - filter_pings.by_files, by_folders
  - plot_navigation for pingoverview

### Performance

- speed up to/from binary functions using isviewstream (istringstream that adapts a string_view)

### Maintainance

- tools:
  - deactive openmp for windows clang-cl for now

### Fixed

- echosounders:
  - KongsbergAllPingWatercolumn: report correctly if av feature is available
  - I_Ping::print, explicitly print if features belong to bottom or watercolumn

### Internal

- echosounders
  - extra files for _wciinfos and _sysinfos
  - _sysinfos substructure is not used at the moment
- tools
  - add visit_variant_no_return visitor function
  - from_binary replaced const std::string& with std::string_view

## [0.18.1] - 2024-02-15

- echosounders -> 0.35.1

### Added

- echosounders:
  - pingbottom and pingwatercolumn structures for simradraw ping
  - XML_Environment to pingdatainterface and ping
  - basic support fro retreiving echograms from simradraw
  - index_functions: print_cache_files_statistics function
  - FileCache: function to remove variable from cache
  - FileCache: function to load from file directly

### Changed

- echosounders:
  - I_Ping: make channel_id flyweight and remove geolocation to reduce ping memory consumption
  - renamed variable: replaced cached_paths_per_file_path with file_cache_paths
  - full ping caching for KongsbergAll
  - PackageCache now stores the package as unique pointer to allow caching packages without default constructor
  - removed TuplePackage in favor of StructPackge

### Fixed
- echosounders:
  - FileCache: did not remove lower priority caches when adding a new cache
  - I_Ping: did not copy sensor configuration when copying ping
- require meson >= 1.3.2 for clang-cl openmp support

### Internal

- echosounders:
  - many shared pointers are now weak pointers, this means that resources will be unavailable if the file is closed
  - fixed common test error with extra detections datagram

## [0.18.0] - 2024-02-08

- pingprocessing -> 0.5.2
- echosounders -> 0.35.0
- tools -> 0.22.1

### Changed

- echosounders
 - reworked caching for package index, navigation and ping data

### Added

- pingprocessing:
  - tests for importing EchogramSection
- echosounders:
  - more import tests
  - FilePackageCache with python bindings for the required datagrams
  - FileCache that supports caching of index, navigation and ping data and partial cache reading
  - get_file_name and get_file_size for FileDataInterfacesPerFile
  - filepackagecache: get_subpackage_count, get_packages and has_package functions
  - complete cachinf for SimradRaw
  - simpel TuplePackage class for FilePackageCache
- tools:
  - register_value_bytes function for object printer (converts bytes to KB,MB or GB)
  - exceptions for version missmatch during reading and writing of binary files

### Internal

- tools:
 - add get_from_map_with_default function to tools::helper

### Maintenance

- Removed python 3.8 and 3.9 support and builds from CI

## [0.17.0] - 2024-02-01

- tools -> 0.22.0
- pingprocessing -> 0.5.1
- echosounders -> 0.34
- navigation -> 0.15.1

### Changed

- echosounders:
  - pingsampleselector: apply selection now explicitly needs IPingWatercolumn or I_PingBottom
  - simradrawping: restructure to using pingcommon, pingbottom and pingwatercolumn substructures
  - changed function names 'initialized' to 'is_initialized'
  - automatic initialization of preceding interfaces to navigation and ping data interfaces
  - simrad XML_ParameterChannel and KongsbergAll RuntimeParameters now supports boost hash (and thus the flyweight pattern)
  - replaced deduplicate buffer by flyweights
- navigation:
  - Internal change: class name is now a function and not a property anymore
- tools:
  - changed function names 'initialized' to 'is_initialized'

### Added

- pingprocessing:
  - EchogramSection class
- echosounders:
  - Added SimradRawDatagramDataInterface and SimradRawDatagramDatainterfacePerFile
  - Caching for NavigationDataInterface
  - towards package caching for pingdata

### Fixed

- pingprocessing
  - pass through mp_cores to backtrace image

### Maintenance

- tools
  - Catch2 3.5.0 -> 3.5.2
  - fmt 10.1.1 -> 10.2.1
  - xtl 0.7.6 -> 0.7.7
  - xtensor 0.24.7 -> 0.25.0
  - xtensor-python 0.26.1 -> 0.27.0
  - fast_float 6.0.0 -> 6.1.0

## [0.16.1] - 2023-12-21

- tools -> 0.21.8
- echosounders -> 0.33.1

### Added

- themachinethatgoesping:
  - bindings for python 3.12
- tools:
  - unixtime_to_datetime
  - datetime_to_unixtime
- echosounders:
  - get_datetime and set_datetime for datagrams and pings

### Fixed

- tools:
  - datestring_to_datetime: now explicitly utc
  - datetime_to_datestring: now explicitly utc

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