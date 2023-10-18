"""
Trampoline classes for abstract file template classes
"""
from __future__ import annotations
import numpy
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import themachinethatgoesping.navigation
import themachinethatgoesping.navigation.datastructures
import typing
__all__ = ['I_Ping', 'I_PingBottom', 'I_PingCommon', 'I_PingWatercolumn']
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
    def get_file_nr(self) -> int:
        ...
    def get_file_path(self) -> str:
        ...
    def get_file_ping_counter(self) -> int:
        ...
    def get_geolocation(self, target_id: str = 'Transducer') -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon:
        """
        Get the geolocation of the transducer.
        
        Returns:
            const navigation::datastructures::GeoLocationLatLon&
        """
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration:
        ...
    def get_sensor_data_latlon(self) -> themachinethatgoesping.navigation.datastructures.SensorDataLatLon:
        ...
    def get_timestamp(self) -> float:
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    def has_bottom(self) -> bool:
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
    def set_file_ping_counter(self, file_ping_counter: int) -> None:
        ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None:
        ...
    def set_sensor_data_latlon(self, sensor_data_latlon: themachinethatgoesping.navigation.datastructures.SensorDataLatLon) -> None:
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
    def feature_string(self, available: bool = True) -> str:
        """
        Get a string of all registered features that are available or not
        available
        
        Parameter ``available``:
            if True (default) return available features, else return not
            available features
        
        Returns:
            std::string
        """
    def has_feature(self, feature_name: str) -> bool:
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def load(self, force: bool = False) -> None:
        ...
    def loaded(self) -> bool:
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
class I_PingWatercolumn(I_PingCommon):
    """
    Interface for all ping watercolumn functions
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
    def get_sample_interval(self) -> float:
        """
        Get the sample interval in seconds
        
        Returns:
            float
        """
    def has_amplitudes(self) -> bool:
        """
        Check this pings supports AMPLITUDES data
        
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
