# Changelog

Ping is still in the bootstrapping phase, thus changes will be frequent and not always documented. 
Once the project is more stable, this changelog will be updated more frequently.

Versioning scheme is currently based on my mood, but will be changed to [Semantic Versioning](https://semver.org/) once the project is more stable. I do not create tags for the versions as none of them are stable enough to be considered a release.

## [0.30.3] - 18-07-2025

- tools -> 0.29.0
- navigation -> 0.17.6
- algorithms -> 0.9.4
- echosounders -> 0.45.3

### Improvements
- algorithms:
  - added eat_neighbor_regions parameter to grow_regions function
  - vectorized functions for forward gridder transformation functions

### Maintenance
- tools: 
  - refractoring to move implementations to cpp files
  - update xtensor 0.27 -> 0.28
- all libraries:
  - activatiung unity builds for ci scripts
  - make builds compatible with fill unity builds
  - adapt new tools libray

## [0.30.2] - 17-06-2025

- algorithms -> 0.9.3
- tools -> 0.28.8
- navigation -> 0.17.4
- echosounders -> 0.45.2
- pingprocessing -> 0.11.5
- gridding -> 0.4.2

### Improvements

- echosounders
  - towards GSF raw file reading
  - use 'p' instead of middle mouse button to update echogramview
  - add InteractiveLineBuilder to pingprocessing/widgets/tools
- pingprocessing
  - echogramviewer: deal with echogramdata dictionaries

### Fixed

- pingprocessing
  - fixes to range/depth stack function names
- algorithms
  - fixed integer conversion for vectorized 1d gridder functions
- tools
  - require meson 1.8.1 (1.8.0 had a bug)
- gridding
  - fixed: echogrid failures using new ForwardGridder3D

### Maintenance

- update nlohmann/json 3.11.2 -> 3.11.3
- update xtensor custom -> 0.26
- update xtensor-python 0.27 -> 0.28
- update xtl 0.7.7 -> 0.8
- update fmt 11.1.4 -> 11.2.0


## [0.30.1] - 09-04-2025

- gridding -> 0.4.1

### Fixed

- gridding:
  - globbing error

## [0.30.0] - 09-04-2025
- pingprocessing -> 0.11.3
- tools -> 0.28.7
- algorithms -> 0.9.2
- gridding -> 0.4.0

### Changed
- gridding:
  - moved forward gridder and related functions to algorithms.gridding

### Improved
- tools
  - nearfield estimation scripts
- algorithms
  - added gridfunctions
  - added geoprocessing functions (to_raypoints)
- pingprocessing
  - adapting echogrambuilder to new gridder

### Fixed
- pingprocessing:
  - missing import for wciviewer

### Maintenance

- tools:
  - update Catch2 3.8.0 -> 3.8.1

---
## [0.29.1] - 26-03-2025
- pingprocessing -> 0.11.2

### Fixed
- fixed: windows circular imports error


## [0.29.0] - 26-03-2025

- tools -> 0.28.5
- navigation -> 17.4.0
- algorithms -> 0.9.1
- gridding -> 0.3.0

### Improvements

- themachinethatgoesping:
  - added bindings for python 3.13
- navigation:
  - multicoreprocessing for utm/latlon conversion
- algorithms:
  - added imageprocessing/find_local_maxima function
  - added imageprocessing/grow_regions function
  - added pointprocessing/weighted_mean function
  - added pointprocessing/segment_in_weighted_quantiles function
  - added pointprocessing/bubblestreams/zspine class
  - added pointprocessing/bubblestreams/zspine displace_points function
- tools:
  - add xtensor_3d concept
- gridding:
  - blockmean function for from_data method
  - improved get_extent and get_grd_extent functions

### Changed
- gridding:
  - refractoring names in echogrid class
  - removed unused class (EchoGridDict)

### Maintanances

- updated xsimd 13.0.0 -> 13.2.0
- updated fmt 11.1.3 -> 11.1.4
- updated fast_float 8.0.0 -> 8.0.2
- drop support for python 3.10

## [0.28.1] - 17-02-2025

- tools -> 0.28.4
- echosounders -> 0.45.1
- gridding -> 0.2.2

### Added

- tools:
  - BiVectorInterpolators
- gridding:
  - echogrid:
    - from_data method

### Maintanance

- updated sse2neon 1.7.0 -> 1.8.0
- update pugixml 1.14 -> 1.15
- fmt 11.1.1 -> 11.1.3
- fast_float 7.0.0 -> 8.0.0

## [0.28.1] - 06-02-2025

- pingprocessing -> 0.11.1

### Fixed

- pingprocessing:
  - import errors (make_wci)


## [0.28.0] - 06-02-2025

- pingprocessing -> 0.11.0
- echosounders -> 0.45.0
- navigation -> 0.17.3
- tools -> 0.28.3
- gridding -> 0.2.1

### Changed

- pingprocessing:
  - EchogramBuilder: renamed max_samples parameter -> max_steps to be more uniform with x_axis functions
- echosounders
  - Renamed:
    - file_cache_paths -> index_paths
    - cache_path -> index_path
    - cache_file_path -> index_path
    - cache_root -> index_root
    - cache_file -> index_file
    - update_cache -> update_index
    - .cache -> .index
    - clean_cache -> clean_index
    - remove_name_from_cache -> remove_name_from_index
    - filecache_functions -> index_file_functions

### Added

- pingprocessing:
  - EchogramViewer: voffsets option to set value offsets for layer colorbars
  - EchogramBuilder: separate clear_main_layer function
  - EchogramBuilder and ImageBuilder: use same apply_pss_to_bottom function
  - EchogramBuilder: do not rebuild axis if called with same parameters
  - EchogramBuilder: ignore additional kwargs in set_x and set_y axis functions
  - preview functions for echograms: LayerGenerator, LayerProcessor
- echosounders:
  - I_PingBottom: get_bottom_z function that returns the smallest (filtered) bottom z from a given selection
  - KongsbergAll sampleampltudestructure: get_sample_amplitudes_per_beam function to return 2d array of amplitudes
  - improved get sample_amplitudes function from sampleampltiudes structure (kongsberg)
- gridding:
  - removed limitation that value must be > 0

### Performance

- pingprocessing:
  - EchogramBuilder: do not rebuild axis if called with same parameters
  - EchogramBuilder: speed up echogram from_pings by using internal get_minslant_sample_nr function
  - EchogramBuilder: speed up echogram from_pings by using internal get_bottom_z function

### Fixed

- echosounders:
  - PingSampleSelector: accept optional/None arguments for all select functions
  - WCIViewer: added missing with self.output tags
  - do not expose get_index_path function (only used internally by get_index_paths)
- pingprocessing:
  - fixed ineffective assert
  - fixed invalid (negative) indices in echolayers
  - ignore errors when trying to find bottom layer in echogrambuilder
  - replace akkimainterpolator with linearinterpolator to avoid unexpected interpolation behavior
  - fix wrong has_rangess variable name

### Maintenance

- support for installing build-requirements using poetry
- pingprocessing: removed deprecated EchogramGroup class
- delete unused pybind11 doc files
- build with LinkTimeOptimization (LTO) for faster builds
- navigation:
  - updated geographiclib 2.4 -> 2.5
- tools:
  - updated fmt 11.0.2 -> 11.1.1
  - update Catch2 3.7.1 -> 3.8.0

## [0.27.1] - 09-12-2024

- pingprocessing -> 0.10.1

### Added

- pingprocessing:
  - improved navplotting
  - added option to filter main layer for echogrambuilder
  - improved pingviewer connection performance
  - removed async eventloop from pingviewer
  
### Fixed

- pingprocessing:
  - fixed: cmap_layer not actively applied in EchogramViewer

## [0.27.0] - 06-12-2024

- pingprocessing -> 0.10.0

### Added

- pingprocessing:
  - EchogramBuilder: basic selecting layer support
  - EchogramBuilder: add and create layers
  - EchogramViewer: callback_view function
  - EchogramViewer: show layers if they are available
  - renamed EchoProxy -> EchogramBuilder
  - echogramviewer: 
    - prepare posibility to add buttons

### Changed

- pingprocessing:
  - rename EchoProxy -> EchogramBuilder

### Fixed

- pingprocessing:
- incorrect ping reduction for filter_pings.by_ping_times

## [0.26.3] - 28-11-2024

- echosounders -> 0.44.2
- tools -> 0.28.2

### Added
- echosounders
  - decoding KongsbergAllRuntimeParameters: mode
  - decoding KongsbergAllRuntimeParameters: mode2
  - decoding KongsbergAllRuntimeParameters: filter_identifier
  - decoding KongsbergAllRuntimeParameters: filter_identifier2
  - decoding KongsbergAllRuntimeParameters: yaw_and_pitch_stabilization
  - decoding KongsbergAllRuntimeParameters: beam_spacing
  - decoding KongsbergAllRuntimeParameters: source_of_sound_speed_at_transducer_as_string
  - decode model number as string for all datagrams
- tools
  - objectprinter: register_string_with_delimiter function

## [0.26.2] - 26-11-2024

- echosounders -> 0.44.1
- pingprocessing -> 0.9.2

### Added
- echosounders
  - decode mode and mode2 for KongsbergAllRuntimeParameters
- pingprocessing -> 0.9.2
  - no_navigation mode for echodata and echogrambuilder from_pings functions
  - invert_y_axis for echogramviewer

## [0.26.1] - 25-11-2024

- echosounders -> 0.44.0
- pingprocessing -> 0.9.1

### Added
- pingprocessing:
  - new split_pings.into block functions
  - time parsing ability for time difference variables
  - new filter_pings.by time_lists function

### Changed
- echosounders -> renamed minslant_distance and bottom_distance to minslant_range and bottom_range

### Fixed
- colorbarwarning for empty pings in wciviewer
- pingprocessing
  - fix clear_output not working for echogramviewer
- echosounders:
  - some printing style changes for runtime parameters

## [0.26.0] - 22-11-2024

- echosounders -> 0.43.1
- tools -> 0.28.1
- algorithms -> 0.9.0
- pingprocessing -> 0.9.0

### Changed
- algorithms:
  - reworked backtracer to support downsampled wcis
  - removed legacy lookup_indices function
- pingprocessing:
  - removed legacy files (echogram builders)

### Added
- echosounders:
  - missing set_navigation_interpolator_latlon function for i_ping
  - set_navigation_interpolator_latlon function for navigation interpolator
  - Function to get incoherent sum from EK80 complex data
  - I_PingWaterColumn: get_minslant_sample_nr function
  - empty() function for beam- and beamsample-selection
  - allow for modifying KongsbergAllWaterColumnCalibration
- pingprocessing:
  - allow passing custom get_data function to make-wci and build echogram classes
  - wciviewer now supports minslant filtering (algorithm 0.9.0)
  - improved tqdmwidget progressbar for make-wci
  - added EchogramViewer widget
  - various improvements to echogram classes

### Fixed
- echosounders:
  - selection reports wron number of ensemple samples for empty selection
- pingprocessing:
  - make_image and echogram deal better with empty pings

### Maintanance
-tools:
  - update magic_enum -> 0.9.7
  - update fast_float -> 7.0.0
- echosounders:
  - adapted to tools 0.28.1
- algorithms:
  - adapted to tools 0.28.1
  - ignore pugixml warnings
- pingprocessing and tutorials
  - standard name for importing ping is now 'theping' (instead of 'Ping')

## [0.25.1] - 06-11-2024

- echosounders -> 0.43.0
- tools -> 0.28.0
- navigation -> 0.17.1
- algorithms -> 0.8.2
- pingprocessing -> 0.8.6
- navigation -> 0.17.2

### Changed
- echosounders:
  - reworked navigation handling for pings
- tools
  - removed non const functions from vector interpolators

### Added
- tools:
  - add python interface for roation functions (eigen/quaternions)
  - ypr_const functions for slerp_interpolator
- echosounders:
  - fallback to use navigation of inactive sensors if active sensor is not available

### Maintanance
-tools:
  - update hinnant-date git/master -> 3.0.2
- navigation:
  - fixed building problems
- algorithms:
  - fixed building problems
  - change GSW-C wrap to original repo (meson.build is now available)
  - adapted to tools 0.28.0
- navigation:
  - adapted to tools 0.28.0
- pingprocessing:
  - fixed building problems

## [0.25.0] - 18-10-2024

- pingprocessing -> 0.8.5
- echosounders -> 0.42.0

### Added
- pingprocessing:
  - correctly process variations of sv/av/rv/... in echograms and make_image
- echosounders:
  - PingSampleSelection:
    - select transmit_sectors by beam_angle or by number
  - KongsbergAllPingBottom:
    - implemented get_tx_sector_per_beam and get_beam_numbers_per_tx_sector

### Fixed
- pingprocessing:
  - echograms: fixed wrong range for get_filtered_by_y_extent
  - echograms: fixed crash if >75% of t data us iut of range
  - make_wci: include transducer position when determining hmin and hmax of the image
- echosounders"
  - AmplitudeCalibration: default extrapolation mode is now nearest instead of linear
  - RawRangeAndAngle: fixed wrong beam number sorting for get_beam_cross_track_angles

## [0.25.0] - 18-10-2024

- echosounders -> 0.42.0
- algorithms -> 0.8.2
- tools -> 0.27.0
- pingprocessing -> 0.8.4

### Changed
- echosounders:
  - rewamping calibration/tvg correction
  - do not cache runtime parameters for kongsbergall
  - renamed get_installation_parameters to read_installation_parameters to be more concise
- tools:
  - option to add or not add superscript to exponents when printing

### Added
- algorithms
  - absorption calculation
  - sound velocity calculation using gswteos-10
  - amplitude range correction functions
  - apply correction functions for wci
- tools:
  - xtensor concepts that work for xtensor and pytensor
  - improved printing of small and large floats
  - superscript helper function
  - minor updates and bugfixes
- echosounders:
  - tx_sector functions now take beam_selection as arguments
  - WatercolumnCalibration, MultisectorWatercolumnCalibration
  - KongsbergallWatercolumnCalibration, KongsbergallMultisectorWatercolumnCalibration
  - SimradRawWatercolumnCalibration

### Fixed
- echosounders::kongsbergall:
  - wrong runtime parameters for kongsbergall pings
- pingprocessing
  - fixed distortion for wci_viewer at short ranges (do not set x offset for backtracer)

## [0.24.2] - 23-09-2024

- echosounders -> 0.41.0
- pingprocessing -> 0.8.3
- tools -> 0.26.0
- algorithms -> 0.8.1
sta
### Changed

- echosounders:
  - reworked calibration classes
- tools:
  - removed slow_hash function
- pingprocessing:
  - adapt echosoudners 0.41.0

### Added

- EchogramBuilder class to pingprocessing
- tools:
  - substract_set_zero_if_negative helper function
- echosounders: 
  - simradraw ek80 corrected power computation from complex32 floats
  - create extra transceiverinformation namespace for simradraw ek80 filedata
  - simradraw ek80 xml_parameter_channel: get_pulse_duration and get_pulse_form_is_cw
  - kongsbergall: support PortableSingleHead configuration
- algorithms:
  - gswteos-10 dependency for sound speed and absorption calculation

### Fixed

- replaced str.split('/') with os.path.split() for cross-platform compatibility
- SimradRaw.watercolumn get_sound_speed_at_transducer now uses environment sound speed if parameter soundvelocity is not available
- echosounders:
  - SimradRaw: fixed wrong skip value for reading skipped sample data
  - unsigned int warning
- pingprocessing: wci_viewer

### Maintenance

- update pybind11 2.12.0 -> 2.13.6
- update Catch2 3.6.0 -> 3.7.1
- update fast_float 6.1.3 -> 6.1.6
- update fmt 10 -> 11
- geographiclib 2.3 -> 2.4
- removed unused flat_map dependency

## [0.24.1] - 02-08-2024

- pingprocessing -> 0.8.2

### Fixed

- pingprocessing:
  - echodata.from_pings: fixed crash for pings with same timestamp

## [0.24.0] - 02-08-2024

- tools -> 0.24.4
- pingprocessing -> 0.8.1
- navigation -> 0.17.0
- echosounders -> 0.40.0

### Changed

- navigation:
  - use more float in navigation interpolator (memory usage)
- echosounders:
  - changed sample nr and beam nr to uint32_t

### Added

- echosounders:
  - EK80:
    - add get_channel(channel_id) function to transceiver_channel

### Fixed

- pingprocessing:
  - overview.nav_plot.create_figure function: reproject background image to latlon by default (support for utm tiffs)
  - clear_memory function crashes on windows and macos
  - more specific error message for missing
- echosounders:
  - fixed typo in function name (get_environmnet)
  - fix filecache name mismatch for non-canonical paths
  - I_PingWaterColumn:
    - number of samples per beam uint16_t -> uint32_t
    - sample offset uint16_t -> int32_t

### Performance

- echosounders:
  - improved speed of get amplitude / get_sv / get_av functions by using eigen

### Maintenance

- tools
  - update fast_float: 6.1.1 -> 6.1.3
- echosounders
  - add test file that spawns get_amplitude error for EK80 data

### Internal
- tools
  - added classversion.hpp helper
- echosounders
  - add function to evaluate if all ping features that are specified as available can be called without causing an exception
  - evaluate unitest pings by calling all available features


## [0.23.4] - 08-07-2024

- tools -> 0.24.3
- echosounders -> 0.39.3

### Performance

- echosoudners
  - reviewed feature functions and significantly improved memory usage per ping

### Maintanance

  - tools:
    start generalizing functions to use an XContainer concept input rather than an xtensor
  - echosounders:
    - add tests that actually load data and loop through datagrams and pings
    - solved diamond inheritance mess
    - removed deprecated functions
  - set warning_level=2 to silence external warnings
  - fix missing override warning
  - cleaned numerous unused xtensor headers
  - finally fixed building for mac (intel only)

## [0.23.3] - 05-07-2024

- tools -> 0.24.2

### Maintanance

- tools
  - hold back pybind11 2.13.1 because there seems to be a problem with gcc 14.1 (keep 2.12.0)
  - update magic_enum -> 0.9.6
  - only require numpy >= 1.26.0 for tests and installing
  - working towards clang-cl openmp support (still not working)
- numerous small fixes while working on mac-os

## [0.23.2] - 20-06-2024

### Maintenance

- Do not require numpy >= 1.26.0 anymore (1.26 is enough)

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
  - AmplitudeCalibration structure
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