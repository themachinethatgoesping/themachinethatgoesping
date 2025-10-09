"""
Trampoline classes for abstract file template classes
"""
from __future__ import annotations
import collections.abc
import enum
import numpy
import themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures
import themachinethatgoesping.echosounders_nanopy.pingtools
import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.navigation_nanopy.datastructures
import themachinethatgoesping.tools_nanopy.vectorinterpolators
import themachinethatgoesping.tools_nanopy.vectorinterpolators.bivectorinterpolators
import typing
__all__: list[str] = ['AmplitudeCalibration', 'FileCache', 'I_Ping', 'I_PingBottom', 'I_PingCommon', 'I_PingFileData', 'I_PingWatercolumn', 'KongsbergAllMultiSectorWaterColumnCalibration', 'MultiSectorWaterColumnCalibration', 'WaterColumnCalibration', 'o_pingfeature', 't_pingfeature']
class AmplitudeCalibration:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> AmplitudeCalibration:
        ...
    def __deepcopy__(self, arg: dict) -> AmplitudeCalibration:
        ...
    def __eq__(self, other: AmplitudeCalibration) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, system_offset: float) -> None
        __init__(self, arg: themachinethatgoesping.echosounders_nanopy.filetemplates.AmplitudeCalibration) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def apply_beam_sample_correction(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], absorption_db_m: float, tvg_factor: float, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        ...
    def copy(self) -> AmplitudeCalibration:
        """
        return a copy using the c++ default copy constructor
        """
    def get_interpolator_offset_per_beamangle(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolatorF:
        ...
    def get_interpolator_offset_per_beamangle_and_range(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.bivectorinterpolators.BiAkimaInterpolatorF:
        ...
    def get_interpolator_offset_per_range(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolatorF:
        ...
    def get_per_beam_offsets(self, beamangles: numpy.ndarray[dtype=float32, ..., order='A']) -> numpy.ndarray[dtype=float32, ..., order='A']:
        ...
    def get_per_sample_offsets(self, ranges: numpy.ndarray[dtype=float32, ..., order='A']) -> numpy.ndarray[dtype=float32, ..., order='A']:
        ...
    def get_system_offset(self) -> float:
        ...
    def has_offset_per_beamangle(self) -> bool:
        ...
    def has_offset_per_beamangle_and_range(self) -> bool:
        ...
    def has_offset_per_range(self) -> bool:
        ...
    def has_system_offset(self) -> bool:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def inplace_beam_sample_correction(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], absorption_db_m: float, tvg_factor: float, min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_offset_per_beamangle(self, beamangle: numpy.ndarray[dtype=float32, ..., order='A'], offset: numpy.ndarray[dtype=float32, ..., order='A']) -> None:
        ...
    def set_offset_per_beamangle_and_range(self, beamangles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], values: numpy.ndarray[dtype=float32, ..., order='A']) -> None:
        """
        set_offset_per_beamangle_and_range(self, offset_per_beamangle_and_range: themachinethatgoesping.tools_nanopy.vectorinterpolators.bivectorinterpolators.BiAkimaInterpolatorF) -> None
        """
    def set_offset_per_range(self, range: numpy.ndarray[dtype=float32, ..., order='A'], offset: numpy.ndarray[dtype=float32, ..., order='A']) -> None:
        ...
    def set_system_offset(self, value: float) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class FileCache:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_file: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> FileCache:
        ...
    def __deepcopy__(self, arg: dict) -> FileCache:
        ...
    def __eq__(self, other: FileCache) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, file_name: str, file_size: int) -> None:
        """
        __init__(self, index_path: str, file_name: str, file_size: int, cache_keys: collections.abc.Sequence[str] = []) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> FileCache:
        """
        return a copy using the c++ default copy constructor
        """
    def get_cache_buffer(self) -> ...:
        ...
    def get_cache_buffer_header(self) -> list[..., ..., ..., ..., ...]:
        ...
    def get_cache_names(self) -> list[str]:
        ...
    def get_file_name(self) -> str:
        ...
    def get_file_size(self) -> int:
        ...
    def get_loaded_cache_names(self) -> list[str]:
        ...
    def get_not_loaded_cache_names(self) -> list[str]:
        ...
    def has_cache(self, cache_name: str) -> bool:
        """
        Check if a cache entry with the given name exists
        
        Parameter ``name``:
            Name of the cache entry to check
        
        Returns:
            true if the cache entry exists
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def remove_from_cache(self, name: str) -> None:
        """
        Remove a cache entry and all entries added after it
        
        Parameter ``name``:
            Name of the cache entry to remove
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    def update_file(self, index_path: str, emulate_only: bool = False) -> None:
        """
        Update or create the cache file at the specified path
        
        Parameter ``index_path``:
            Path where to write the cache file
        
        Parameter ``emulate_only``:
            If true, only simulate the update without actually writing
        """
class I_Ping(I_PingCommon):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> I_Ping:
        """
        __copy__(self) -> themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping
        """
    def __deepcopy__(self, arg: dict) -> I_Ping:
        """
        __deepcopy__(self, arg: dict, /) -> themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping
        """
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        """
        __repr__(self) -> str
        
        Return object information as string
        """
    def __str__(self) -> str:
        """
        __str__(self) -> str
        
        Return object information as string
        """
    def available_feature_groups(self, available: bool = True) -> list[t_pingfeature]:
        ...
    def available_features(self, available_available: bool = True) -> list[t_pingfeature]:
        ...
    def copy(self) -> I_Ping:
        """
        copy(self) -> themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping
        
        return a copy using the c++ default copy constructor
        """
    def feature_groups_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered feature groups that are available or
        not available
        
        Parameter ``available``:
            if True (default) return available features, else return not
            available features
        
        Returns:
            std::string
        """
    def feature_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered features that are available or not
        available
        
        Parameter ``available``:
            if True (default) return available features, else return not
            available features
        
        Returns:
            std::string
        """
    def get_channel_id(self) -> str:
        """
        < channel id of the transducer
        """
    def get_datetime(self, timezone_offset_hours: float = 0.0) -> typing.Any:
        """
        Return the timestamp as datetime object
        """
    def get_geolocation(self, target_id: str = 'Transducer') -> themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLatLon:
        ...
    def get_navigation_interpolator_latlon(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon:
        ...
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration:
        ...
    def get_sensor_configuration_base_hash(self) -> int:
        """
        Returns the hash of the base sensor configuraiton. This is the sensor
        configuration with the "Transducer" target removed. This hash can be
        used to get the correct navigation interpolator from the
        navigation_data_interface Note: This function is for testing and
        finding errors. It is rather slow.
        
        Returns:
            uint64_t
        """
    def get_sensor_data_latlon(self) -> themachinethatgoesping.navigation_nanopy.datastructures.SensordataLatLon:
        ...
    def get_timestamp(self) -> float:
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    def has_all_of_features(self, feature_names: collections.abc.Sequence[o_pingfeature]) -> bool:
        """
        Check if all of the specified features are available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_any_of_features(self, feature_names: collections.abc.Sequence[o_pingfeature]) -> bool:
        """
        Check if any of the specified features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_bottom(self) -> bool:
        ...
    def has_channel_id(self) -> bool:
        ...
    def has_datetime(self) -> bool:
        """
        Return true if the timestamp is available that can be converted to a datetime
        """
    def has_feature(self, feature_name: o_pingfeature) -> bool:
        """
        Check if any of the registered features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_features(self) -> bool:
        """
        Check if any of the registered features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_geolocation(self) -> bool:
        ...
    def has_navigation_interpolator_latlon(self) -> bool:
        ...
    def has_primary_features(self) -> bool:
        """
        Check if any of the registered main features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_sensor_configuration(self) -> bool:
        ...
    def has_sensor_data_latlon(self) -> bool:
        ...
    def has_timestamp(self) -> bool:
        ...
    def has_watercolumn(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str
        
        Return object information as string
        """
    def load(self, force: bool = False) -> None:
        ...
    def loaded(self) -> bool:
        ...
    def possible_feature_groups(self) -> list[t_pingfeature]:
        ...
    def possible_features(self) -> list[t_pingfeature]:
        ...
    def primary_features(self) -> str:
        """
        Get a string of all registered primary features for this ping class
        
        Returns:
            std::string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None
        
        Print object information
        """
    def registered_features(self) -> str:
        """
        Get a string of all registered features for this ping class
        
        Returns:
            std::string
        """
    def release(self) -> None:
        ...
    def set_channel_id(self, channel_id: str) -> None:
        """
        < channel id of the transducer
        """
    def set_datetime(self, datetime: typing.Any) -> None:
        """
        Set the timestamp using a datetime object
        """
    def set_navigation_interpolator_latlon(self, nav_interpolator: themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon) -> None:
        ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation_nanopy.SensorConfiguration) -> None:
        ...
    def set_timestamp(self, timestamp: float) -> None:
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    @property
    def bottom(self) -> I_PingBottom:
        ...
    @property
    def watercolumn(self) -> I_PingWatercolumn:
        ...
class I_PingBottom(I_PingCommon):
    """
    Interface for all ping bottom detection functions
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> I_PingBottom:
        """
        __copy__(self) -> themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom
        """
    def __deepcopy__(self, arg: dict) -> I_PingBottom:
        """
        __deepcopy__(self, arg: dict, /) -> themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def available_feature_groups(self, available: bool = True) -> list[t_pingfeature]:
        ...
    def available_features(self, available_available: bool = True) -> list[t_pingfeature]:
        ...
    def copy(self) -> I_PingBottom:
        """
        copy(self) -> themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom
        
        return a copy using the c++ default copy constructor
        """
    def feature_groups_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered feature groups that are available or
        not available
        
        Parameter ``available``:
            if True (default) return available features, else return not
            available features
        
        Returns:
            std::string
        """
    def feature_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered features that are available or not
        available
        
        Parameter ``available``:
            if True (default) return available features, else return not
            available features
        
        Returns:
            std::string
        """
    def get_beam_crosstrack_angles(self) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_beam_crosstrack_angles(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> numpy.ndarray[dtype=float32, shape=(*), order='C']
        
        Get the beam crosstrack angles for this ping in °
        
        Returns:
            xt::xtensor<float, 1>
        """
    def get_beam_numbers_per_tx_sector(self) -> list[list[int]]:
        """
        get_beam_numbers_per_tx_sector(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> list[list[int]]
        """
    def get_beam_selection_all(self) -> themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection:
        """
        Get a beam selection object that selects all beams
        
        Returns:
            pingtools::BeamSelection
        """
    def get_bottom_z(self) -> float:
        """
        get_bottom_z(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> float
        
        Overloaded function.
        
        1. ``get_bottom_z(self) -> float``
        
        Computes closest bottom z value from all beams.
        
        This function retrieves the z-coordinates of the selected beams and
        performs outlier filtering to determine a valid bottom z value. If no
        valid bottom z value is found, an exception is thrown.
        
        Parameter ``selection``:
            The selection of beams from which to compute the bottom z value.
        
        Returns:
            The computed bottom z value.
        
        Throws:
            std::runtime_error If no valid bottom z value is found.
        
        2. ``get_bottom_z(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> float``
        
        Computes the closest z value from a given selection of beams.
        
        This function retrieves the z-coordinates of the selected beams and
        performs outlier filtering to determine a valid bottom z value. If no
        valid bottom z value is found, an exception is thrown.
        
        Parameter ``selection``:
            The selection of beams from which to compute the bottom z value.
        
        Returns:
            The computed bottom z value.
        
        Throws:
            std::runtime_error If no valid bottom z value is found.
        """
    def get_number_of_beams(self) -> int:
        """
        Get the number of beams for this ping
        
        Returns:
            uint32_t
        """
    def get_number_of_tx_sectors(self) -> int:
        """
        Get the number of transmission sectors.
        
        This function returns the number of transmission sectors for the
        echosounder.
        
        Returns:
            The number of transmission sectors.
        """
    def get_two_way_travel_times(self) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_two_way_travel_times(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> numpy.ndarray[dtype=float32, shape=(*), order='C']
        
        Get the two way travel times of the bottom detection samples
        
        Returns:
            xt::xtensor<float, 1>
        """
    def get_tx_sector_per_beam(self) -> numpy.ndarray[dtype=uint64, ..., order='C']:
        """
        get_tx_sector_per_beam(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> numpy.ndarray[dtype=uint64, shape=(*), order='C']
        """
    def get_tx_signal_parameters(self) -> list[..., ..., ...]:
        """
        Get the transmission signal parameters per sector.
        
        Returns:
            const std::vector<algorithms::signalprocessing::datastructures::Tx
            SignalParameters>&
        """
    def get_xyz(self) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1:
        """
        get_xyz(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1
        
        Overloaded function.
        
        1. ``get_xyz(self) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1``
        
        Get an XYZ object containing the XYZ position of the bottom detection
        Note: XYZ is in the local coordinate system of the ping! To convert it
        use algorithms::geoprocessing::georeferencer class or - Use
        get_xyz_utm() to get the bottom detection in UTM coordinates - Use
        get_xyz_latlon() to get the bottom detection in Latitude/Longitude
        coordinates
        
        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>
        
        2. ``get_xyz(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1``
        
        Get an XYZ object containing the XYZ position of the bottom detection
        Note: XYZ is in the local coordinate system of the ping! To convert it
        use algorithms::geoprocessing::georeferencer class or - Use
        get_xyz_utm() to get the bottom detection in UTM coordinates - Use
        get_xyz_latlon() to get the bottom detection in Latitude/Longitude
        coordinates
        
        Parameter ``selection``:
            structure with selected transducer_ids/beams/samples considered
            for this function
        
        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>
        """
    def has_all_of_features(self, feature_names: collections.abc.Sequence[o_pingfeature]) -> bool:
        """
        Check if all of the specified features are available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_any_of_features(self, feature_names: collections.abc.Sequence[o_pingfeature]) -> bool:
        """
        Check if any of the specified features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_beam_crosstrack_angles(self) -> bool:
        ...
    def has_beam_numbers_per_tx_sector(self) -> bool:
        ...
    def has_beam_selection_all(self) -> bool:
        ...
    def has_feature(self, feature_name: o_pingfeature) -> bool:
        """
        Check if any of the registered features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_features(self) -> bool:
        """
        Check if any of the registered features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_number_of_beams(self) -> bool:
        ...
    def has_number_of_tx_sectors(self) -> bool:
        ...
    def has_primary_features(self) -> bool:
        """
        Check if any of the registered main features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_two_way_travel_times(self) -> bool:
        ...
    def has_tx_sector_per_beam(self) -> bool:
        ...
    def has_tx_signal_parameters(self) -> bool:
        ...
    def has_xyz(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def load(self, force: bool = False) -> None:
        ...
    def loaded(self) -> bool:
        ...
    def possible_feature_groups(self) -> list[t_pingfeature]:
        ...
    def possible_features(self) -> list[t_pingfeature]:
        ...
    def primary_features(self) -> str:
        """
        Get a string of all registered primary features for this ping class
        
        Returns:
            std::string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def registered_features(self) -> str:
        """
        Get a string of all registered features for this ping class
        
        Returns:
            std::string
        """
    def release(self) -> None:
        ...
class I_PingCommon:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> I_PingCommon:
        """
        __copy__(self) -> themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingCommon
        """
    def __deepcopy__(self, arg: dict) -> I_PingCommon:
        """
        __deepcopy__(self, arg: dict, /) -> themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingCommon
        """
    def __repr__(self) -> str:
        """
        __repr__(self) -> str
        
        Return object information as string
        """
    def __str__(self) -> str:
        """
        __str__(self) -> str
        
        Return object information as string
        """
    def available_feature_groups(self, available: bool = True) -> list[t_pingfeature]:
        ...
    def available_features(self, available_available: bool = True) -> list[t_pingfeature]:
        ...
    def copy(self) -> I_PingCommon:
        """
        copy(self) -> themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingCommon
        
        return a copy using the c++ default copy constructor
        """
    def feature_groups_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered feature groups that are available or
        not available
        
        Parameter ``available``:
            if True (default) return available features, else return not
            available features
        
        Returns:
            std::string
        """
    def feature_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered features that are available or not
        available
        
        Parameter ``available``:
            if True (default) return available features, else return not
            available features
        
        Returns:
            std::string
        """
    def has_all_of_features(self, feature_names: collections.abc.Sequence[o_pingfeature]) -> bool:
        """
        Check if all of the specified features are available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_any_of_features(self, feature_names: collections.abc.Sequence[o_pingfeature]) -> bool:
        """
        Check if any of the specified features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_feature(self, feature_name: o_pingfeature) -> bool:
        """
        Check if any of the registered features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_features(self) -> bool:
        """
        Check if any of the registered features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_primary_features(self) -> bool:
        """
        Check if any of the registered main features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str
        
        Return object information as string
        """
    def load(self, force: bool = False) -> None:
        ...
    def loaded(self) -> bool:
        ...
    def possible_feature_groups(self) -> list[t_pingfeature]:
        ...
    def possible_features(self) -> list[t_pingfeature]:
        ...
    def primary_features(self) -> str:
        """
        Get a string of all registered primary features for this ping class
        
        Returns:
            std::string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None
        
        Print object information
        """
    def registered_features(self) -> str:
        """
        Get a string of all registered features for this ping class
        
        Returns:
            std::string
        """
    def release(self) -> None:
        ...
class I_PingFileData:
    """
    @class I_PingFileData Interface for raw ping data.
    
    This class defines an interface for raw ping data. It provides methods
    to access and manipulate the properties of the ping data, such as the
    name, file ping counter, primary file number, file numbers, primary
    file path, and file paths.
    
    The class also includes a nested exception class, `not_implemented`,
    which is thrown when a method is not implemented.
    
    The class provides a `__printer__` function for object printing, which
    can be used to print the properties of the ping data.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> I_PingFileData:
        ...
    def __deepcopy__(self, arg: dict) -> I_PingFileData:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> I_PingFileData:
        """
        return a copy using the c++ default copy constructor
        """
    def get_file_numbers(self) -> list[int]:
        """
        Get the file numbers of the contained datagrams.
        
        Returns:
            std::vector<size_t> The file numbers.
        
        Throws:
            not_implemented Exception if not implemented.
        """
    def get_file_paths(self) -> list[str]:
        """
        Get the file paths.
        
        Returns:
            std::vector<std::string> The file paths associated with the
            contained datagrams.
        
        Throws:
            not_implemented Exception if not implemented.
        """
    def get_file_ping_counter(self) -> int:
        """
        Get the file ping counter.
        
        Returns:
            size_t The file ping counter.
        """
    def get_primary_file_nr(self) -> int:
        """
        Get the primary file number of this ping.
        
        Returns:
            size_t The primary file number.
        """
    def get_primary_file_path(self) -> str:
        """
        Get the primary file path of this ping.
        
        Returns:
            std::string The primary file path of this ping.
        
        Throws:
            not_implemented Exception if not implemented.
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_file_ping_counter(self, file_ping_counter: int) -> None:
        """
        Set the file ping counter.
        
        Parameter ``file_ping_counter``:
            The file ping counter to set.
        """
    def set_primary_file_nr(self, file_nr: int) -> None:
        """
        Set the primary file number for this ping.
        
        Parameter ``primary_file_nr``:
            The primary file number to set.
        """
class I_PingWatercolumn(I_PingCommon):
    """
    Interface for all ping watercolumn functions
    
    @class I_PingWatercolumn Interface for watercolumn ping data.
    
    This class represents an interface for accessing watercolumn ping
    data. It inherits from the I_PingCommon class and provides additional
    functions and variables specific to watercolumn pings.
    """
    _test_mode: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> I_PingWatercolumn:
        """
        __copy__(self) -> themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn
        """
    def __deepcopy__(self, arg: dict) -> I_PingWatercolumn:
        """
        __deepcopy__(self, arg: dict, /) -> themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def available_feature_groups(self, available: bool = True) -> list[t_pingfeature]:
        ...
    def available_features(self, available_available: bool = True) -> list[t_pingfeature]:
        ...
    def copy(self) -> I_PingWatercolumn:
        """
        copy(self) -> themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn
        
        return a copy using the c++ default copy constructor
        """
    def feature_groups_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered feature groups that are available or
        not available
        
        Parameter ``available``:
            if True (default) return available features, else return not
            available features
        
        Returns:
            std::string
        """
    def feature_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered features that are available or not
        available
        
        Parameter ``available``:
            if True (default) return available features, else return not
            available features
        
        Returns:
            std::string
        """
    def get_amplitudes(self, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_amplitudes(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, shape=(*, *), order='C']
        
        Get tha raw water amplitude data converted to float(32bit)
        
        Returns:
            xt::xtensor<float,2>
        """
    def get_ap(self, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_ap(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, shape=(*, *), order='C']
        
        Get the amplitude data converted to AP (uncalibrated point scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    def get_approximate_ranges(self) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_approximate_ranges(self, beam_sample_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection) -> numpy.ndarray[dtype=float32, shape=(*), order='C']
        """
    def get_av(self, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_av(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, shape=(*, *), order='C']
        
        Get the amplitude data converted to AV (uncalibrated volume
        scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    def get_beam_alongtrack_angles(self) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_beam_alongtrack_angles(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> numpy.ndarray[dtype=float32, shape=(*), order='C']
        
        Get the beam alongtrack angles for this ping in °
        
        Returns:
            xt::xtensor<float, 1>
        """
    def get_beam_crosstrack_angles(self) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_beam_crosstrack_angles(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> numpy.ndarray[dtype=float32, shape=(*), order='C']
        
        Get the beam crosstrack angles for this ping in °
        
        Returns:
            xt::xtensor<float, 1>
        """
    def get_beam_numbers_per_tx_sector(self) -> list[list[int]]:
        """
        get_beam_numbers_per_tx_sector(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> list[list[int]]
        """
    def get_beam_sample_selection_all(self) -> themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection:
        """
        Get beam sample selection that selects all beams and samples
        
        Returns:
            pingtools::BeamSampleSelection
        """
    def get_beam_selection_all(self) -> themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection:
        """
        Get a beam selection object that selects all beams
        
        Returns:
            pingtools::BeamSelection
        """
    def get_bottom_range_samples(self) -> numpy.ndarray[dtype=uint32, ..., order='C']:
        """
        get_bottom_range_samples(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> numpy.ndarray[dtype=uint32, shape=(*), order='C']
        
        Get the sample number of the bottom detection for each beam
        
        Returns:
            xt::xtensor<uint32_t, 1>
        """
    def get_first_sample_offset_per_beam(self) -> numpy.ndarray[dtype=uint32, ..., order='C']:
        ...
    def get_minslant_sample_nr(self) -> int:
        """
        get_minslant_sample_nr(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> int
        
        Computes the minimum slant sample number from all beams.
        
        This function calculates the minimum slant sample number by first
        obtaining the bottom range samples from the provided beam selection.
        It then filters out outliers using the Interquartile Range (IQR)
        method and returns the smallest valid sample number.
        
        Returns:
            The minimum slant sample number.
        
        Throws:
            std::runtime_error If no valid bottom range sample is found.
        """
    def get_multisectorwatercolumn_calibration(self) -> ...:
        ...
    def get_number_of_beams(self) -> int:
        """
        Get the number of beams for this ping
        
        Returns:
            uint32_t
        """
    def get_number_of_samples_per_beam(self) -> numpy.ndarray[dtype=uint32, ..., order='C']:
        """
        get_number_of_samples_per_beam(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> numpy.ndarray[dtype=uint32, shape=(*), order='C']
        """
    def get_number_of_tx_sectors(self) -> int:
        """
        Get the number of transmission sectors.
        
        This function returns the number of transmission sectors for the
        echosounder.
        
        Returns:
            The number of transmission sectors.
        """
    def get_power(self, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_power(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, shape=(*, *), order='C']
        
        Get the amplitude data converted to power
        
        Returns:
            xt::xtensor<float,2>
        """
    def get_pp(self, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_pp(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, shape=(*, *), order='C']
        
        Get the power data converted to PP (power +2 alpha R + 40log(R))
        
        Returns:
            xt::xtensor<float,2>
        """
    def get_pv(self, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_pv(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, shape=(*, *), order='C']
        
        Get the power data converted to PV (power +2 alpha R + 20log(R))
        
        Returns:
            xt::xtensor<float,2>
        """
    def get_rp(self, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_rp(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, shape=(*, *), order='C']
        
        Get the power data converted to RP (power 40log(R))
        
        Returns:
            xt::xtensor<float,2>
        """
    def get_rv(self, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_rv(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, shape=(*, *), order='C']
        
        Get the power data converted to RV (power 20log(R))
        
        Returns:
            xt::xtensor<float,2>
        """
    def get_sample_interval(self) -> float:
        """
        Get the sample interval in seconds
        
        Returns:
            float
        """
    def get_sound_speed_at_transducer(self) -> float:
        ...
    def get_sp(self, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_sp(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, shape=(*, *), order='C']
        
        Get the amplitude data converted to SP (calibrated point scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    def get_sv(self, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get_sv(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, shape=(*, *), order='C']
        
        Get the amplitude data converted to SV (calibrated volume scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    def get_tx_sector_per_beam(self) -> numpy.ndarray[dtype=uint64, ..., order='C']:
        """
        get_tx_sector_per_beam(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> numpy.ndarray[dtype=uint64, shape=(*), order='C']
        """
    def get_tx_signal_parameters(self) -> list[..., ..., ...]:
        """
        Get the transmission signal parameters per sector.
        
        Returns:
            const std::vector<algorithms::signalprocessing::datastructures::Tx
            SignalParameters>&
        """
    def get_watercolumn_calibration(self) -> WaterColumnCalibration:
        """
        get_watercolumn_calibration(self, sector_nr: int) -> themachinethatgoesping.echosounders_nanopy.filetemplates.WaterColumnCalibration
        """
    def has_all_of_features(self, feature_names: collections.abc.Sequence[o_pingfeature]) -> bool:
        """
        Check if all of the specified features are available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_amplitudes(self) -> bool:
        ...
    def has_any_of_features(self, feature_names: collections.abc.Sequence[o_pingfeature]) -> bool:
        """
        Check if any of the specified features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_ap(self) -> bool:
        """
        Check this pings supports AP data (uncalibrated point scattering)
        """
    def has_av(self) -> bool:
        """
        Check this pings supports AV data (uncalibrated volume scattering)
        """
    def has_beam_numbers_per_tx_sector(self) -> bool:
        ...
    def has_beam_selection_all(self) -> bool:
        ...
    def has_bottom_range_samples(self) -> bool:
        """
        Check this pings supports bottom range samples
        """
    def has_feature(self, feature_name: o_pingfeature) -> bool:
        """
        Check if any of the registered features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_features(self) -> bool:
        """
        Check if any of the registered features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_multisectorwatercolumn_calibration(self) -> bool:
        """
        Check this pings has valid power calibration data
        """
    def has_number_of_beams(self) -> bool:
        ...
    def has_number_of_tx_sectors(self) -> bool:
        ...
    def has_power(self) -> bool:
        """
        Check this pings supports calibrated power data
        """
    def has_pp(self) -> bool:
        """
        Check this pings supports PP data
        """
    def has_primary_features(self) -> bool:
        """
        Check if any of the registered main features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_pv(self) -> bool:
        """
        Check this pings supports PV data
        """
    def has_rp(self) -> bool:
        """
        Check this pings supports RP data
        """
    def has_rv(self) -> bool:
        """
        Check this pings supports RV data
        """
    def has_sp(self) -> bool:
        """
        Check this pings supports calibrated SV data
        """
    def has_sv(self) -> bool:
        """
        Check this pings supports calibrated SV data
        """
    def has_tx_sector_per_beam(self) -> bool:
        ...
    def has_tx_signal_parameters(self) -> bool:
        ...
    def has_watercolumn_calibration(self) -> bool:
        """
        Check this pings has valid power calibration data
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def load(self, force: bool = False) -> None:
        ...
    def loaded(self) -> bool:
        ...
    def possible_feature_groups(self) -> list[t_pingfeature]:
        ...
    def possible_features(self) -> list[t_pingfeature]:
        ...
    def primary_features(self) -> str:
        """
        Get a string of all registered primary features for this ping class
        
        Returns:
            std::string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def registered_features(self) -> str:
        """
        Get a string of all registered features for this ping class
        
        Returns:
            std::string
        """
    def release(self) -> None:
        ...
class KongsbergAllMultiSectorWaterColumnCalibration:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> KongsbergAllMultiSectorWaterColumnCalibration:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllMultiSectorWaterColumnCalibration:
        ...
    def __eq__(self, other: KongsbergAllMultiSectorWaterColumnCalibration) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, calibration_per_sector: std::vector<themachinethatgoesping::echosounders::kongsbergall::filedatatypes::calibration::KongsbergAllWaterColumnCalibration, std::allocator<themachinethatgoesping::echosounders::kongsbergall::filedatatypes::calibration::KongsbergAllWaterColumnCalibration> >) -> None
        __init__(self, other: themachinethatgoesping.echosounders_nanopy.filetemplates.KongsbergAllMultiSectorWaterColumnCalibration) -> None
        """
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def apply_beam_sample_correction_ap(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_ap(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_av(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_av(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_power(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_power(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_pp(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_pp(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_pv(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_pv(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_sp(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_sp(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_sv(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_sv(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def copy(self) -> KongsbergAllMultiSectorWaterColumnCalibration:
        """
        return a copy using the c++ default copy constructor
        """
    def get_calibrations(self) -> ...:
        ...
    def get_number_of_sectors(self) -> int:
        ...
    def has_ap_calibration(self) -> bool:
        ...
    def has_av_calibration(self) -> bool:
        ...
    def has_power_calibration(self) -> bool:
        ...
    def has_sp_calibration(self) -> bool:
        ...
    def has_sv_calibration(self) -> bool:
        ...
    def has_valid_absorption_db_m(self) -> bool:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def inplace_beam_sample_correction_av(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> None:
        """
        inplace_beam_sample_correction_av(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> None
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class MultiSectorWaterColumnCalibration:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> MultiSectorWaterColumnCalibration:
        ...
    def __deepcopy__(self, arg: dict) -> MultiSectorWaterColumnCalibration:
        ...
    def __eq__(self, other: MultiSectorWaterColumnCalibration) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, calibration_per_sector: std::vector<themachinethatgoesping::echosounders::filetemplates::datatypes::calibration::WaterColumnCalibration, std::allocator<themachinethatgoesping::echosounders::filetemplates::datatypes::calibration::WaterColumnCalibration> >) -> None
        __init__(self, other: themachinethatgoesping.echosounders_nanopy.filetemplates.MultiSectorWaterColumnCalibration) -> None
        """
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def apply_beam_sample_correction_ap(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_ap(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_av(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_av(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_power(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_power(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_pp(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_pp(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_pv(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_pv(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_sp(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_sp(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_sv(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_sv(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def copy(self) -> MultiSectorWaterColumnCalibration:
        """
        return a copy using the c++ default copy constructor
        """
    def get_calibrations(self) -> ...:
        ...
    def get_number_of_sectors(self) -> int:
        ...
    def has_ap_calibration(self) -> bool:
        ...
    def has_av_calibration(self) -> bool:
        ...
    def has_power_calibration(self) -> bool:
        ...
    def has_sp_calibration(self) -> bool:
        ...
    def has_sv_calibration(self) -> bool:
        ...
    def has_valid_absorption_db_m(self) -> bool:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def inplace_beam_sample_correction_av(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], beam_numbers_per_tx_sector: ..., std: ..., std: ..., std: ..., mp_cores: int = 1) -> None:
        """
        inplace_beam_sample_correction_av(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], beam_numbers_per_tx_sector: std::vector<std::vector<unsigned long, std::allocator<unsigned long> >, std::allocator<std::vector<unsigned long, std::allocator<unsigned long> > > >, mp_cores: int = 1) -> None
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class WaterColumnCalibration:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> WaterColumnCalibration:
        ...
    def __deepcopy__(self, arg: dict) -> WaterColumnCalibration:
        ...
    def __eq__(self, other: WaterColumnCalibration) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, tvg_absorption_db_m: float = 0.0, tvg_factor: float = 0.0) -> None:
        """
        __init__(self, power_calibration: themachinethatgoesping.echosounders_nanopy.filetemplates.AmplitudeCalibration = AmplitudeCalibration, ap_calibration: themachinethatgoesping.echosounders_nanopy.filetemplates.AmplitudeCalibration = AmplitudeCalibration, av_calibration: themachinethatgoesping.echosounders_nanopy.filetemplates.AmplitudeCalibration = AmplitudeCalibration, tvg_absorption_db_m: float = 0.0, tvg_factor: float = 0.0) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def apply_beam_sample_correction_ap(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_ap(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_av(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_av(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_power(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_power(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_pp(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_pp(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_pv(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_pv(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_rp(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_rp(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_rv(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_rv(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_sp(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_sp(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def apply_beam_sample_correction_sv(self, wci: numpy.ndarray[dtype=float32, ..., order='A'], beam_angles: numpy.ndarray[dtype=float32, ..., order='A'], ranges: numpy.ndarray[dtype=float32, ..., order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='A']:
        """
        apply_beam_sample_correction_sv(self, wci: numpy.ndarray[dtype=float64, shape=(*, *), order='A'], beam_angles: numpy.ndarray[dtype=float64, shape=(*), order='A'], ranges: numpy.ndarray[dtype=float64, shape=(*), order='A'], mp_cores: int = 1) -> numpy.ndarray[dtype=float64, shape=(*, *), order='A']
        """
    def check_initialized(self) -> None:
        ...
    def check_modifying_base_calibration_allowed(self) -> None:
        ...
    def copy(self) -> WaterColumnCalibration:
        """
        return a copy using the c++ default copy constructor
        """
    def get_absorption_db_m(self) -> float:
        ...
    def get_absorption_to_apply(self, absorption_db_m: float | None = None) -> float | None:
        ...
    def get_ap_calibration(self) -> AmplitudeCalibration:
        ...
    def get_av_calibration(self) -> AmplitudeCalibration:
        ...
    def get_power_calibration(self) -> AmplitudeCalibration:
        ...
    def get_sp_calibration(self) -> AmplitudeCalibration:
        ...
    def get_sv_calibration(self) -> AmplitudeCalibration:
        ...
    def get_tvg_absorption_db_m(self) -> float:
        ...
    def get_tvg_factor(self) -> float:
        ...
    def get_tvg_factor_to_apply(self, tvg_factor: float) -> float | None:
        ...
    def has_ap_calibration(self) -> bool:
        ...
    def has_av_calibration(self) -> bool:
        ...
    def has_power_calibration(self) -> bool:
        ...
    def has_sp_calibration(self) -> bool:
        ...
    def has_sv_calibration(self) -> bool:
        ...
    def has_valid_absorption_db_m(self) -> bool:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_absorption_db_m(self, absorption_db_m: float) -> None:
        ...
    def set_ap_calibration(self, calibration: AmplitudeCalibration) -> None:
        ...
    def set_av_calibration(self, calibration: AmplitudeCalibration) -> None:
        ...
    def set_power_calibration(self, calibration: AmplitudeCalibration) -> None:
        ...
    def set_sp_calibration(self, calibration: AmplitudeCalibration) -> None:
        ...
    def set_sv_calibration(self, calibration: AmplitudeCalibration) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class o_pingfeature:
    """
    Helper class to convert between strings and enum values of type 't_pingfeature'
    """
    __default_value__: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.timestamp
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> o_pingfeature:
        ...
    def __deepcopy__(self, arg: dict) -> o_pingfeature:
        ...
    def __eq__(self, arg: o_pingfeature) -> bool:
        """
        __eq__(self, arg: themachinethatgoesping.echosounders_nanopy.filetemplates.t_pingfeature, /) -> bool
        __eq__(self, arg: int, /) -> bool
        __eq__(self, arg: str, /) -> bool
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, value: t_pingfeature = ...) -> None:
        """
        __init__(self, value: str) -> None
        __init__(self, value: int) -> None
        
        Overloaded function.
        
        1. ``__init__(self, value: themachinethatgoesping.echosounders_nanopy.filetemplates.t_pingfeature = t_pingfeature.timestamp) -> None``
        
        Construct from enum value
        
        2. ``__init__(self, value: str) -> None``
        
        Construct from string
        
        3. ``__init__(self, value: int) -> None``
        
        Construct from string
        """
    def __repr__(self) -> str:
        """
        __repr__(self) -> None
        
        Overloaded function.
        
        1. ``__repr__(self) -> str``
        
        Return object information as string
        
        2. ``__repr__(self) -> None``
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        __str__(self) -> str
        
        Overloaded function.
        
        1. ``__str__(self) -> str``
        
        
        2. ``__str__(self) -> str``
        
        Return object information as string
        """
    def copy(self) -> o_pingfeature:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def value(self) -> t_pingfeature:
        """
        enum value
        """
    @value.setter
    def value(self, arg: t_pingfeature) -> None:
        """
        enum value
        """
class t_pingfeature(enum.Enum):
    """
    """
    amplitudes: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.amplitudes
    ap: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.ap
    av: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.av
    beam_crosstrack_angles: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.beam_crosstrack_angles
    beam_numbers_per_tx_sector: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.beam_numbers_per_tx_sector
    beam_selection_all: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.beam_selection_all
    bottom: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.bottom
    bottom_range_samples: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.bottom_range_samples
    channel_id: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.channel_id
    datetime: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.datetime
    geolocation: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.geolocation
    multisectorwatercolumn_calibration: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.multisectorwatercolumn_calibration
    navigation_interpolator_latlon: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.navigation_interpolator_latlon
    number_of_beams: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.number_of_beams
    number_of_tx_sectors: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.number_of_tx_sectors
    power: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.power
    pp: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.pp
    pv: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.pv
    rp: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.rp
    rv: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.rv
    sensor_configuration: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.sensor_configuration
    sensor_data_latlon: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.sensor_data_latlon
    sp: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.sp
    sv: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.sv
    timestamp: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.timestamp
    two_way_travel_times: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.two_way_travel_times
    tx_sector_per_beam: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.tx_sector_per_beam
    tx_signal_parameters: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.tx_signal_parameters
    watercolumn: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.watercolumn
    watercolumn_calibration: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.watercolumn_calibration
    xyz: typing.ClassVar[t_pingfeature]  # value = t_pingfeature.xyz
