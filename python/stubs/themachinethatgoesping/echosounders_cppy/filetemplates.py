"""
Trampoline classes for abstract file template classes
"""
from __future__ import annotations
import numpy
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import themachinethatgoesping.algorithms.signalprocessing.datastructures
import themachinethatgoesping.navigation
import themachinethatgoesping.navigation.datastructures
import themachinethatgoesping.tools_cppy.vectorinterpolators
import typing
__all__ = ['AmplitudeCalibration', 'FileCache', 'I_Ping', 'I_PingBottom', 'I_PingCommon', 'I_PingFileData', 'I_PingWatercolumn', 'WaterColumnCalibration', 'amplitudes', 'ap', 'av', 'beam_crosstrack_angles', 'bottom', 'bottom_range_samples', 'channel_id', 'datetime', 'geolocation', 'number_of_tx_sectors', 'power', 'power_calibration', 'sensor_configuration', 'sensor_data_latlon', 'sp', 'sp_calibration', 'sv', 'sv_calibration', 't_pingfeature', 'timestamp', 'two_way_travel_times', 'tx_signal_parameters', 'watercolumn', 'xyz']
class AmplitudeCalibration:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> AmplitudeCalibration:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> AmplitudeCalibration:
        ...
    def __deepcopy__(self, arg0: dict) -> AmplitudeCalibration:
        ...
    def __eq__(self, other: AmplitudeCalibration) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    @typing.overload
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __hash__(self) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, system_offset: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: AmplitudeCalibration) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def apply_beam_sample_correction(self, wci: numpy.ndarray[numpy.float32], beam_angles: numpy.ndarray[numpy.float32], ranges: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
        ...
    @typing.overload
    def apply_beam_sample_correction(self, wci: numpy.ndarray[numpy.float32], beam_angles: numpy.ndarray[numpy.float32], ranges: numpy.ndarray[numpy.float32], absorption_db_m: float, tvg_factor: float, mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
        ...
    def cached_hash(self) -> int:
        ...
    def copy(self) -> AmplitudeCalibration:
        """
        return a copy using the c++ default copy constructor
        """
    def get_interpolator_offset_per_beamangle(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolatorFF:
        ...
    def get_interpolator_offset_per_range(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolatorFF:
        ...
    @typing.overload
    def get_offset_per_beamangle(self, beamangle: list[float]) -> list[float]:
        ...
    @typing.overload
    def get_offset_per_beamangle(self, beamangle: float) -> float:
        ...
    @typing.overload
    def get_offset_per_range(self, range: list[float]) -> list[float]:
        ...
    @typing.overload
    def get_offset_per_range(self, range: float) -> float:
        ...
    def get_per_beam_offsets(self, beamangles: numpy.ndarray[numpy.float32]) -> numpy.ndarray[numpy.float32]:
        ...
    def get_per_sample_offsets(self, ranges: numpy.ndarray[numpy.float32]) -> numpy.ndarray[numpy.float32]:
        ...
    def get_system_offset(self) -> float:
        ...
    def has_offset_per_beamangle(self) -> bool:
        ...
    def has_offset_per_range(self) -> bool:
        ...
    def has_system_offset(self) -> bool:
        ...
    @typing.overload
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def hash(self) -> int:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def initialized(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_offset_per_beamangle(self, beamangle: list[float], offset: list[float]) -> None:
        ...
    def set_offset_per_range(self, range: list[float], offset: list[float]) -> None:
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
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FileCache:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def from_file(cache_path: str) -> FileCache:
        ...
    def __copy__(self) -> FileCache:
        ...
    def __deepcopy__(self, arg0: dict) -> FileCache:
        ...
    def __eq__(self, other: FileCache) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, file_name: str, file_size: int) -> None:
        ...
    @typing.overload
    def __init__(self, cache_path: str, file_name: str, file_size: int, cache_keys: list[str] = []) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> FileCache:
        """
        return a copy using the c++ default copy constructor
        """
    def get_cache_buffer(self) -> dict[str, str]:
        ...
    def get_cache_buffer_header(self) -> list[tuple[str, int, int]]:
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
    def remove_from_cache(self, name: str) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    def update_file(self, cache_path: str, emulate_only: bool = False) -> None:
        ...
class I_Ping(I_PingCommon):
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __copy__(self) -> I_Ping:
        ...
    def __deepcopy__(self, arg0: dict) -> I_Ping:
        ...
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> I_Ping:
        """
        return a copy using the c++ default copy constructor
        """
    def get_channel_id(self) -> str:
        """
        < channel id of the transducer
        """
    def get_datetime(self, timezone_offset_hours: float = 0.0) -> typing.Any:
        """
        Return the timestamp as datetime object
        """
    def get_geolocation(self, target_id: str = 'Transducer') -> themachinethatgoesping.navigation.datastructures.GeolocationLatLon:
        ...
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration:
        ...
    def get_sensor_data_latlon(self) -> themachinethatgoesping.navigation.datastructures.SensordataLatLon:
        ...
    def get_timestamp(self) -> float:
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    def has_bottom(self) -> bool:
        ...
    def has_channel_id(self) -> bool:
        ...
    def has_geolocation(self) -> bool:
        ...
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
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_channel_id(self, channel_id: str) -> None:
        """
        < channel id of the transducer
        """
    def set_datetime(self, datetime: typing.Any) -> None:
        """
        Set the timestamp using a datetime object
        """
    def set_geolocation(self, geolocation: themachinethatgoesping.navigation.datastructures.GeolocationLatLon) -> None:
        ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None:
        ...
    def set_sensor_data_latlon(self, sensor_data_latlon: themachinethatgoesping.navigation.datastructures.SensordataLatLon) -> None:
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
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __copy__(self) -> I_PingBottom:
        ...
    def __deepcopy__(self, arg0: dict) -> I_PingBottom:
        ...
    def copy(self) -> I_PingBottom:
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def get_beam_crosstrack_angles(self) -> numpy.ndarray[numpy.float32]:
        """
        Get the beam crosstrack angles for this ping in °
        
        Returns:
            xt::xtensor<float, 1>
        """
    @typing.overload
    def get_beam_crosstrack_angles(self, beam_selection: ...) -> numpy.ndarray[numpy.float32]:
        """
        Get the beam crosstrack angles for this ping in °
        
        Returns:
            xt::xtensor<float, 1>
        """
    def get_beam_numbers_per_tx_sector(self) -> list[list[int]]:
        ...
    def get_beam_selection_all(self) -> ...:
        """
        Get a beam selection object that selects all beams
        
        Returns:
            pingtools::BeamSelection
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
    @typing.overload
    def get_two_way_travel_times(self) -> numpy.ndarray[numpy.float32]:
        """
        Get the two way travel times of the bottom detection samples
        
        Returns:
            xt::xtensor<float, 1>
        """
    @typing.overload
    def get_two_way_travel_times(self, beam_selection: ...) -> numpy.ndarray[numpy.float32]:
        """
        Get the two way travel times of the bottom detection samples
        
        Returns:
            xt::xtensor<float, 1>
        """
    def get_tx_sector_per_beam(self) -> numpy.ndarray[numpy.uint64]:
        ...
    def get_tx_signal_parameters(self) -> list[themachinethatgoesping.algorithms.signalprocessing.datastructures.CWSignalParameters | themachinethatgoesping.algorithms.signalprocessing.datastructures.FMSignalParameters | themachinethatgoesping.algorithms.signalprocessing.datastructures.GenericSignalParameters]:
        """
        Get the transmission signal parameters per sector.
        
        Returns:
            const std::vector<algorithms::signalprocessing::datastructures::Tx
            SignalParameters>&
        """
    @typing.overload
    def get_xyz(self) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1:
        """
        Get an XYZ object containing the XYZ position of the bottom detection
        Note: XYZ is in the local coordinate system of the ping! To convert it
        use algorithms::geoprocessing::georeferencer class or - Use
        get_xyz_utm() to get the bottom detection in UTM coordinates - Use
        get_xyz_latlon() to get the bottom detection in Latitude/Longitude
        coordinates
        
        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>
        """
    @typing.overload
    def get_xyz(self, beam_selection: ...) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1:
        """
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
    def has_beam_crosstrack_angles(self) -> bool:
        """
        Check this pings supports the extraction of beam_crosstrack_angles
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_two_way_travel_times(self) -> bool:
        """
        Check this pings supports the extraction of two_way_travel_times
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_tx_sector_information(self) -> bool:
        ...
    def has_tx_signal_parameters(self) -> bool:
        ...
    def has_xyz(self) -> bool:
        """
        Check this pings supports XYZ data
        
        Returns:
            true
        
        Returns:
            false
        """
class I_PingCommon:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __copy__(self) -> I_PingCommon:
        ...
    def __deepcopy__(self, arg0: dict) -> I_PingCommon:
        ...
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
    def copy(self) -> I_PingCommon:
        """
        return a copy using the c++ default copy constructor
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
    def has_all_of_features(self, feature_names: list[t_pingfeature]) -> bool:
        """
        Check if all of the specified features are available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_any_of_features(self, feature_names: list[t_pingfeature]) -> bool:
        """
        Check if any of the specified features is available
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_feature(self, feature_name: t_pingfeature) -> bool:
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
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __copy__(self) -> I_PingFileData:
        ...
    def __deepcopy__(self, arg0: dict) -> I_PingFileData:
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
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __copy__(self) -> I_PingWatercolumn:
        ...
    def __deepcopy__(self, arg0: dict) -> I_PingWatercolumn:
        ...
    def copy(self) -> I_PingWatercolumn:
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def get_amplitudes(self) -> numpy.ndarray[numpy.float32]:
        """
        Get tha raw water amplitude data converted to float(32bit)
        
        Returns:
            xt::xtensor<float,2>
        """
    @typing.overload
    def get_amplitudes(self, beam_selection: ...) -> numpy.ndarray[numpy.float32]:
        """
        Get tha raw water amplitude data converted to float(32bit)
        
        Returns:
            xt::xtensor<float,2>
        """
    @typing.overload
    def get_ap(self) -> numpy.ndarray[numpy.float32]:
        """
        Get the amplitude data converted to AP (uncalibrated point scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    @typing.overload
    def get_ap(self, beam_selection: ...) -> numpy.ndarray[numpy.float32]:
        """
        Get the amplitude data converted to AP (uncalibrated point scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    @typing.overload
    def get_av(self) -> numpy.ndarray[numpy.float32]:
        """
        Get the amplitude data converted to AV (uncalibrated volume
        scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    @typing.overload
    def get_av(self, beam_selection: ...) -> numpy.ndarray[numpy.float32]:
        """
        Get the amplitude data converted to AV (uncalibrated volume
        scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    @typing.overload
    def get_beam_alongtrack_angles(self) -> numpy.ndarray[numpy.float32]:
        """
        Get the beam alongtrack angles for this ping in °
        
        Returns:
            xt::xtensor<float, 1>
        """
    @typing.overload
    def get_beam_alongtrack_angles(self, beam_selection: ...) -> numpy.ndarray[numpy.float32]:
        """
        Get the beam alongtrack angles for this ping in °
        
        Returns:
            xt::xtensor<float, 1>
        """
    @typing.overload
    def get_beam_crosstrack_angles(self) -> numpy.ndarray[numpy.float32]:
        """
        Get the beam crosstrack angles for this ping in °
        
        Returns:
            xt::xtensor<float, 1>
        """
    @typing.overload
    def get_beam_crosstrack_angles(self, beam_selection: ...) -> numpy.ndarray[numpy.float32]:
        """
        Get the beam crosstrack angles for this ping in °
        
        Returns:
            xt::xtensor<float, 1>
        """
    @typing.overload
    def get_beam_numbers_per_tx_sector(self) -> list[list[int]]:
        ...
    @typing.overload
    def get_beam_numbers_per_tx_sector(self, beam_selection: ...) -> list[list[int]]:
        ...
    def get_beam_sample_selection_all(self) -> ...:
        """
        Get beam sample selection that selects all beams and samples
        
        Returns:
            pingtools::BeamSampleSelection
        """
    def get_beam_selection_all(self) -> ...:
        """
        Get a beam selection object that selects all beams
        
        Returns:
            pingtools::BeamSelection
        """
    @typing.overload
    def get_bottom_range_samples(self) -> numpy.ndarray[numpy.uint32]:
        """
        Get the sample number of the bottom detection for each beam
        
        Returns:
            xt::xtensor<uint32_t, 1>
        """
    @typing.overload
    def get_bottom_range_samples(self, beam_selection: ...) -> numpy.ndarray[numpy.uint32]:
        """
        Get the sample number of the bottom detection for each beam
        
        Returns:
            xt::xtensor<uint32_t, 1>
        """
    def get_first_sample_offset_per_beam(self) -> numpy.ndarray[numpy.uint32]:
        ...
    def get_number_of_beams(self) -> int:
        """
        Get the number of beams for this ping
        
        Returns:
            uint32_t
        """
    @typing.overload
    def get_number_of_samples_per_beam(self) -> numpy.ndarray[numpy.uint32]:
        ...
    @typing.overload
    def get_number_of_samples_per_beam(self, arg0: ...) -> numpy.ndarray[numpy.uint32]:
        ...
    def get_number_of_tx_sectors(self) -> int:
        """
        Get the number of transmission sectors.
        
        This function returns the number of transmission sectors for the
        echosounder.
        
        Returns:
            The number of transmission sectors.
        """
    @typing.overload
    def get_power(self) -> numpy.ndarray[numpy.float32]:
        """
        Get the amplitude data converted to power
        
        Returns:
            xt::xtensor<float,2>
        """
    @typing.overload
    def get_power(self, beam_selection: ...) -> numpy.ndarray[numpy.float32]:
        """
        Get the amplitude data converted to power
        
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
    @typing.overload
    def get_sp(self) -> numpy.ndarray[numpy.float32]:
        """
        Get the amplitude data converted to SP (calibrated point scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    @typing.overload
    def get_sp(self, beam_selection: ...) -> numpy.ndarray[numpy.float32]:
        """
        Get the amplitude data converted to SP (calibrated point scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    @typing.overload
    def get_sv(self) -> numpy.ndarray[numpy.float32]:
        """
        Get the amplitude data converted to SV (calibrated volume scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    @typing.overload
    def get_sv(self, beam_selection: ...) -> numpy.ndarray[numpy.float32]:
        """
        Get the amplitude data converted to SV (calibrated volume scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    @typing.overload
    def get_tx_sector_per_beam(self) -> numpy.ndarray[numpy.uint64]:
        ...
    @typing.overload
    def get_tx_sector_per_beam(self, beam_selection: ...) -> numpy.ndarray[numpy.uint64]:
        ...
    def get_tx_signal_parameters(self) -> list[themachinethatgoesping.algorithms.signalprocessing.datastructures.CWSignalParameters | themachinethatgoesping.algorithms.signalprocessing.datastructures.FMSignalParameters | themachinethatgoesping.algorithms.signalprocessing.datastructures.GenericSignalParameters]:
        """
        Get the transmission signal parameters per sector.
        
        Returns:
            const std::vector<algorithms::signalprocessing::datastructures::Tx
            SignalParameters>&
        """
    def get_watercolumn_calibration(self) -> WaterColumnCalibration:
        ...
    def has_amplitudes(self) -> bool:
        """
        Check this pings supports AMPLITUDES data
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_ap(self) -> bool:
        """
        Check this pings supports AP data (uncalibrated point scattering)
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_av(self) -> bool:
        """
        Check this pings supports AV data (uncalibrated volume scattering)
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_bottom_range_samples(self) -> bool:
        """
        Check this pings supports bottom range samples
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_power(self) -> bool:
        """
        Check this pings supports calibrated power data
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_sp(self) -> bool:
        """
        Check this pings supports calibrated SV data
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_sv(self) -> bool:
        """
        Check this pings supports calibrated SV data
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_tx_sector_information(self) -> bool:
        ...
    def has_tx_signal_parameters(self) -> bool:
        ...
    def has_watercolumn_calibration(self) -> bool:
        """
        Check this pings has valid power calibration data
        
        Returns:
            true
        
        Returns:
            false
        """
    def set_watercolumn_calibration(self, calibration: WaterColumnCalibration) -> None:
        ...
class WaterColumnCalibration:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> WaterColumnCalibration:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> WaterColumnCalibration:
        ...
    def __deepcopy__(self, arg0: dict) -> WaterColumnCalibration:
        ...
    def __eq__(self, other: WaterColumnCalibration) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    @typing.overload
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __hash__(self) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, power_calibration: AmplitudeCalibration = ..., ap_calibration: AmplitudeCalibration = ..., av_calibration: AmplitudeCalibration = ...) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: WaterColumnCalibration) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def cached_hash(self) -> int:
        ...
    def copy(self) -> WaterColumnCalibration:
        """
        return a copy using the c++ default copy constructor
        """
    def get_absorption_db_m(self) -> float:
        ...
    def get_power_calibration(self) -> AmplitudeCalibration:
        ...
    def get_tvg_absorption_db_m(self) -> float:
        ...
    def get_tvg_factor(self) -> float:
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
    @typing.overload
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def hash(self) -> int:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def initialized(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
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
class t_pingfeature:
    """
    
    
    Members:
    
      timestamp
    
      datetime
    
      channel_id
    
      sensor_configuration
    
      sensor_data_latlon
    
      geolocation
    
      bottom
    
      watercolumn
    
      tx_signal_parameters
    
      number_of_tx_sectors
    
      beam_crosstrack_angles
    
      two_way_travel_times
    
      xyz
    
      bottom_range_samples
    
      amplitudes
    
      ap
    
      av
    
      power
    
      sp
    
      sv
    
      power_calibration
    
      sp_calibration
    
      sv_calibration
    """
    __members__: typing.ClassVar[dict[str, t_pingfeature]]  # value = {'timestamp': <t_pingfeature.timestamp: 0>, 'datetime': <t_pingfeature.datetime: 1>, 'channel_id': <t_pingfeature.channel_id: 2>, 'sensor_configuration': <t_pingfeature.sensor_configuration: 3>, 'sensor_data_latlon': <t_pingfeature.sensor_data_latlon: 4>, 'geolocation': <t_pingfeature.geolocation: 5>, 'bottom': <t_pingfeature.bottom: 7>, 'watercolumn': <t_pingfeature.watercolumn: 8>, 'tx_signal_parameters': <t_pingfeature.tx_signal_parameters: 9>, 'number_of_tx_sectors': <t_pingfeature.number_of_tx_sectors: 10>, 'beam_crosstrack_angles': <t_pingfeature.beam_crosstrack_angles: 11>, 'two_way_travel_times': <t_pingfeature.two_way_travel_times: 12>, 'xyz': <t_pingfeature.xyz: 13>, 'bottom_range_samples': <t_pingfeature.bottom_range_samples: 15>, 'amplitudes': <t_pingfeature.amplitudes: 16>, 'ap': <t_pingfeature.ap: 17>, 'av': <t_pingfeature.av: 18>, 'power': <t_pingfeature.power: 19>, 'sp': <t_pingfeature.sp: 20>, 'sv': <t_pingfeature.sv: 21>, 'power_calibration': <t_pingfeature.power_calibration: 22>, 'sp_calibration': <t_pingfeature.sp_calibration: 23>, 'sv_calibration': <t_pingfeature.sv_calibration: 24>}
    amplitudes: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.amplitudes: 16>
    ap: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.ap: 17>
    av: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.av: 18>
    beam_crosstrack_angles: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.beam_crosstrack_angles: 11>
    bottom: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.bottom: 7>
    bottom_range_samples: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.bottom_range_samples: 15>
    channel_id: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.channel_id: 2>
    datetime: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.datetime: 1>
    geolocation: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.geolocation: 5>
    number_of_tx_sectors: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.number_of_tx_sectors: 10>
    power: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.power: 19>
    power_calibration: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.power_calibration: 22>
    sensor_configuration: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.sensor_configuration: 3>
    sensor_data_latlon: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.sensor_data_latlon: 4>
    sp: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.sp: 20>
    sp_calibration: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.sp_calibration: 23>
    sv: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.sv: 21>
    sv_calibration: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.sv_calibration: 24>
    timestamp: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.timestamp: 0>
    two_way_travel_times: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.two_way_travel_times: 12>
    tx_signal_parameters: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.tx_signal_parameters: 9>
    watercolumn: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.watercolumn: 8>
    xyz: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.xyz: 13>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    @typing.overload
    def __init__(self, value: int) -> None:
        ...
    @typing.overload
    def __init__(self, str: str) -> None:
        """
        Construct this enum type from string
        """
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def str(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
amplitudes: t_pingfeature  # value = <t_pingfeature.amplitudes: 16>
ap: t_pingfeature  # value = <t_pingfeature.ap: 17>
av: t_pingfeature  # value = <t_pingfeature.av: 18>
beam_crosstrack_angles: t_pingfeature  # value = <t_pingfeature.beam_crosstrack_angles: 11>
bottom: t_pingfeature  # value = <t_pingfeature.bottom: 7>
bottom_range_samples: t_pingfeature  # value = <t_pingfeature.bottom_range_samples: 15>
channel_id: t_pingfeature  # value = <t_pingfeature.channel_id: 2>
datetime: t_pingfeature  # value = <t_pingfeature.datetime: 1>
geolocation: t_pingfeature  # value = <t_pingfeature.geolocation: 5>
number_of_tx_sectors: t_pingfeature  # value = <t_pingfeature.number_of_tx_sectors: 10>
power: t_pingfeature  # value = <t_pingfeature.power: 19>
power_calibration: t_pingfeature  # value = <t_pingfeature.power_calibration: 22>
sensor_configuration: t_pingfeature  # value = <t_pingfeature.sensor_configuration: 3>
sensor_data_latlon: t_pingfeature  # value = <t_pingfeature.sensor_data_latlon: 4>
sp: t_pingfeature  # value = <t_pingfeature.sp: 20>
sp_calibration: t_pingfeature  # value = <t_pingfeature.sp_calibration: 23>
sv: t_pingfeature  # value = <t_pingfeature.sv: 21>
sv_calibration: t_pingfeature  # value = <t_pingfeature.sv_calibration: 24>
timestamp: t_pingfeature  # value = <t_pingfeature.timestamp: 0>
two_way_travel_times: t_pingfeature  # value = <t_pingfeature.two_way_travel_times: 12>
tx_signal_parameters: t_pingfeature  # value = <t_pingfeature.tx_signal_parameters: 9>
watercolumn: t_pingfeature  # value = <t_pingfeature.watercolumn: 8>
xyz: t_pingfeature  # value = <t_pingfeature.xyz: 13>
