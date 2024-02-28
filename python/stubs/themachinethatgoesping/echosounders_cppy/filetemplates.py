"""
Trampoline classes for abstract file template classes
"""
from __future__ import annotations
import numpy
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import themachinethatgoesping.algorithms.signalprocessing.datastructures
import themachinethatgoesping.navigation
import themachinethatgoesping.navigation.datastructures
import typing
__all__ = ['FileCache', 'I_Ping', 'I_PingBottom', 'I_PingCommon', 'I_PingFileData', 'I_PingWatercolumn', 'amplitudes', 'av', 'beam_crosstrack_angles', 'bottom', 'bottom_range_sample', 'channel_id', 'datetime', 'geolocation', 'number_of_tx_sectors', 'sensor_configuration', 'sensor_data_latlon', 't_pingfeature', 'timestamp', 'two_way_travel_times', 'tx_signal_parameters', 'watercolumn', 'xyz']
class FileCache:
    """
    """
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def remove_from_cache(self, name: str) -> None:
        ...
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    def update_file(self, cache_path: str, emulate_only: bool = False) -> None:
        ...
class I_Ping(I_PingCommon):
    """
    """
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
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
            uint16_t
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def load(self, force: bool = False) -> None:
        ...
    def loaded(self) -> bool:
        ...
    def primary_features(self) -> str:
        ...
    def print(self, float_precision: int = 2) -> None:
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
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
    def get_av(self) -> numpy.ndarray[numpy.float32]:
        """
        Get tha amplitude data converted to AV (uncalibrated volume
        scattering)
        
        Returns:
            xt::xtensor<float,2>
        """
    @typing.overload
    def get_av(self, beam_selection: ...) -> numpy.ndarray[numpy.float32]:
        """
        Get tha amplitude data converted to AV (uncalibrated volume
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
    def get_beam_numbers_per_tx_sector(self) -> list[list[int]]:
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
    def get_bottom_range_samples(self) -> numpy.ndarray[numpy.uint16]:
        """
        Get the sample number of the bottom detection for each beam
        
        Returns:
            xt::xtensor<uint16_t, 1>
        """
    @typing.overload
    def get_bottom_range_samples(self, beam_selection: ...) -> numpy.ndarray[numpy.uint16]:
        """
        Get the sample number of the bottom detection for each beam
        
        Returns:
            xt::xtensor<uint16_t, 1>
        """
    def get_first_sample_offset_per_beam(self) -> numpy.ndarray[numpy.uint16]:
        ...
    def get_number_of_beams(self) -> int:
        """
        Get the number of beams for this ping
        
        Returns:
            uint16_t
        """
    @typing.overload
    def get_number_of_samples_per_beam(self) -> numpy.ndarray[numpy.uint16]:
        ...
    @typing.overload
    def get_number_of_samples_per_beam(self, arg0: ...) -> numpy.ndarray[numpy.uint16]:
        ...
    def get_number_of_tx_sectors(self) -> int:
        """
        Get the number of transmission sectors.
        
        This function returns the number of transmission sectors for the
        echosounder.
        
        Returns:
            The number of transmission sectors.
        """
    def get_sample_interval(self) -> float:
        """
        Get the sample interval in seconds
        
        Returns:
            float
        """
    def get_sound_speed_at_transducer(self) -> float:
        ...
    def get_tx_sector_per_beam(self) -> numpy.ndarray[numpy.uint64]:
        ...
    def get_tx_signal_parameters(self) -> list[themachinethatgoesping.algorithms.signalprocessing.datastructures.CWSignalParameters | themachinethatgoesping.algorithms.signalprocessing.datastructures.FMSignalParameters | themachinethatgoesping.algorithms.signalprocessing.datastructures.GenericSignalParameters]:
        """
        Get the transmission signal parameters per sector.
        
        Returns:
            const std::vector<algorithms::signalprocessing::datastructures::Tx
            SignalParameters>&
        """
    def has_amplitudes(self) -> bool:
        """
        Check this pings supports AMPLITUDES data
        
        Returns:
            true
        
        Returns:
            false
        """
    def has_av(self) -> bool:
        """
        Check this pings supports AV data
        
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
    def has_tx_sector_information(self) -> bool:
        ...
    def has_tx_signal_parameters(self) -> bool:
        ...
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
    
      amplitudes
    
      av
    
      bottom_range_sample
    """
    __members__: typing.ClassVar[dict[str, t_pingfeature]]  # value = {'timestamp': <t_pingfeature.timestamp: 0>, 'datetime': <t_pingfeature.datetime: 1>, 'channel_id': <t_pingfeature.channel_id: 2>, 'sensor_configuration': <t_pingfeature.sensor_configuration: 3>, 'sensor_data_latlon': <t_pingfeature.sensor_data_latlon: 4>, 'geolocation': <t_pingfeature.geolocation: 5>, 'bottom': <t_pingfeature.bottom: 7>, 'watercolumn': <t_pingfeature.watercolumn: 8>, 'tx_signal_parameters': <t_pingfeature.tx_signal_parameters: 9>, 'number_of_tx_sectors': <t_pingfeature.number_of_tx_sectors: 10>, 'beam_crosstrack_angles': <t_pingfeature.beam_crosstrack_angles: 11>, 'two_way_travel_times': <t_pingfeature.two_way_travel_times: 12>, 'xyz': <t_pingfeature.xyz: 13>, 'amplitudes': <t_pingfeature.amplitudes: 14>, 'av': <t_pingfeature.av: 15>, 'bottom_range_sample': <t_pingfeature.bottom_range_sample: 16>}
    amplitudes: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.amplitudes: 14>
    av: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.av: 15>
    beam_crosstrack_angles: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.beam_crosstrack_angles: 11>
    bottom: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.bottom: 7>
    bottom_range_sample: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.bottom_range_sample: 16>
    channel_id: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.channel_id: 2>
    datetime: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.datetime: 1>
    geolocation: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.geolocation: 5>
    number_of_tx_sectors: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.number_of_tx_sectors: 10>
    sensor_configuration: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.sensor_configuration: 3>
    sensor_data_latlon: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.sensor_data_latlon: 4>
    timestamp: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.timestamp: 0>
    two_way_travel_times: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.two_way_travel_times: 12>
    tx_signal_parameters: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.tx_signal_parameters: 9>
    watercolumn: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.watercolumn: 8>
    xyz: typing.ClassVar[t_pingfeature]  # value = <t_pingfeature.xyz: 13>
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
amplitudes: t_pingfeature  # value = <t_pingfeature.amplitudes: 14>
av: t_pingfeature  # value = <t_pingfeature.av: 15>
beam_crosstrack_angles: t_pingfeature  # value = <t_pingfeature.beam_crosstrack_angles: 11>
bottom: t_pingfeature  # value = <t_pingfeature.bottom: 7>
bottom_range_sample: t_pingfeature  # value = <t_pingfeature.bottom_range_sample: 16>
channel_id: t_pingfeature  # value = <t_pingfeature.channel_id: 2>
datetime: t_pingfeature  # value = <t_pingfeature.datetime: 1>
geolocation: t_pingfeature  # value = <t_pingfeature.geolocation: 5>
number_of_tx_sectors: t_pingfeature  # value = <t_pingfeature.number_of_tx_sectors: 10>
sensor_configuration: t_pingfeature  # value = <t_pingfeature.sensor_configuration: 3>
sensor_data_latlon: t_pingfeature  # value = <t_pingfeature.sensor_data_latlon: 4>
timestamp: t_pingfeature  # value = <t_pingfeature.timestamp: 0>
two_way_travel_times: t_pingfeature  # value = <t_pingfeature.two_way_travel_times: 12>
tx_signal_parameters: t_pingfeature  # value = <t_pingfeature.tx_signal_parameters: 9>
watercolumn: t_pingfeature  # value = <t_pingfeature.watercolumn: 8>
xyz: t_pingfeature  # value = <t_pingfeature.xyz: 13>
