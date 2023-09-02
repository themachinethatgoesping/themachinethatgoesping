"""
Kongsberg EM3000 (.all/.wcd) EK80 datagram classes
"""
from __future__ import annotations
import numpy
import pybind11_stubgen.typing_ext
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import themachinethatgoesping.echosounders.em3000
import themachinethatgoesping.navigation.datastructures
import typing
from . import substructures
__all__ = ['AttitudeDatagram', 'Bscorr', 'CalibTxt', 'ClockDatagram', 'DepthOrHeightDatagram', 'EM3000Datagram', 'EM3000Unknown', 'ExtraDetections', 'ExtraParameters', 'ExtraParameters_t_ContentIdentifier', 'HeadingDatagram', 'InstallationParameters', 'LogAllHeights', 'MultiCastInputStatus', 'NetworkAttitudeVelocityDatagram', 'PUIDOutput', 'PUStatusOutput', 'PositionDatagram', 'QualityFactorDatagram', 'RawRangeAndAngle', 'RuntimeParameters', 'SeabedImageData', 'SingleBeamEchoSounderDepth', 'SoundSpeedProfileDatagram', 'SoundVelocityAtTransducer', 'SoundVelocityProfile', 'SurfaceSoundSpeedDatagram', 'WatercolumnDatagram', 'XYZDatagram', 'substructures']
class AttitudeDatagram(EM3000Datagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
    122, EM 302 and ME70BO. All receiver beams are included, check
    detection info and real time cleaning for beam status (note 4 and 5).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> AttitudeDatagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> AttitudeDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> AttitudeDatagram:
        ...
    def __eq__(self, other: AttitudeDatagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def attitudes(self) -> list[substructures.AttitudeDatagramAttitude]:
        """
        < N x Attitude data
        """
    def copy(self) -> AttitudeDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def get_attitude_counter(self) -> int:
        ...
    def get_attitude_sensor_number(self) -> int:
        """
        Get the number of attitude sensor from the sensor system descriptor
        field. xx00 xxxx – attitude sensor number 1 xx01 xxxx – attitude
        sensor number 2
        
        Returns:
            1 or 2
        """
    def get_attitudes(self) -> list[substructures.AttitudeDatagramAttitude]:
        """
        < N x Attitude data
        """
    def get_checksum(self) -> int:
        ...
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_heading_sensor_is_active(self) -> bool:
        """
        Evaluate if the heading sensor is active using sensor system
        descriptor field. 0bxxxxxxx1 : heading is active 0bxxxxxxx1 : heading
        is inactive
        
        Returns:
            bool
        """
    def get_heave_sensor_is_active(self) -> bool:
        """
        Evaluate if the heave sensor is active using sensor system descriptor
        field. 0bxxxx1xxx : heave is active 0bxxxx0xxx : heave is inactive
        
        Returns:
            bool
        """
    def get_number_of_entries(self) -> int:
        """
        < N
        """
    def get_pitch_sensor_is_active(self) -> bool:
        """
        Evaluate if the pitch sensor is active using sensor system descriptor
        field. 0bxxxxx1xx : pitch is active 0bxxxxx0xx : pitch is inactive
        
        Returns:
            bool
        """
    def get_roll_sensor_is_active(self) -> bool:
        """
        Evaluate if the roll sensor is active using sensor system descriptor
        field. 0bxxxxxx1x : roll is active 0bxxxxxx0x : roll is inactive
        
        Returns:
            bool
        """
    def get_sensor_system_descriptor(self) -> int:
        ...
    def get_system_serial_number(self) -> int:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_attitude_counter(self, arg0: int) -> None:
        ...
    def set_attitudes(self, arg0: list[substructures.AttitudeDatagramAttitude]) -> None:
        """
        < N x Attitude data
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_number_of_entries(self, arg0: int) -> None:
        """
        < N
        """
    def set_sensor_system_descriptor(self, arg0: int) -> None:
        ...
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class ClockDatagram(EM3000Datagram):
    """
    Clock datagrams
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> ClockDatagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> ClockDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> ClockDatagram:
        ...
    def __eq__(self, other: ClockDatagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> ClockDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def get_checksum(self) -> int:
        ...
    def get_clock_counter(self) -> int:
        """
        < sequential number
        """
    def get_date_external(self) -> int:
        """
        < from external clock input year*1000 + month*100 + day(Example:Jun <
        27, 2020 = 20200627)
        """
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_pps_active(self) -> int:
        """
        < 0 = inactive (Shows if the system clock is synchronized to an
        external < PPS signal or not)
        """
    def get_system_serial_number(self) -> int:
        ...
    def get_time_since_midnight_external(self) -> int:
        """
        < in ms from external clock datagram
        """
    def get_timestamp_external(self) -> float:
        """
        convert the date and time_since_midnight field to a unix timestamp
        
        Returns:
            unixtime as double
        """
    def get_timestamp_offset(self) -> float:
        """
        difference between timestamp and timestamp_external
        
        Returns:
            timestamp_external - timestamp
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_clock_counter(self, arg0: int) -> None:
        """
        < sequential number
        """
    def set_date_external(self, arg0: int) -> None:
        """
        < from external clock input year*1000 + month*100 + day(Example:Jun <
        27, 2020 = 20200627)
        """
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_pps_active(self, arg0: int) -> None:
        """
        < 0 = inactive (Shows if the system clock is synchronized to an
        external < PPS signal or not)
        """
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def set_time_since_midnight_external(self, arg0: int) -> None:
        """
        < in ms from external clock datagram
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class DepthOrHeightDatagram(EM3000Datagram):
    """
    Depth (pressure) or height datagrams
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> DepthOrHeightDatagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> DepthOrHeightDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> DepthOrHeightDatagram:
        ...
    def __eq__(self, other: DepthOrHeightDatagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> DepthOrHeightDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def get_checksum(self) -> int:
        ...
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_height(self) -> int:
        """
        < in cm
        """
    def get_height_counter(self) -> int:
        """
        < Sequential Number
        """
    def get_height_in_meters(self) -> float:
        """
        Get the height in meters
        
        Returns:
            _height * 0.01m (float)
        """
    def get_height_type(self) -> int:
        """
        < 0: derived from GGK or GGA, 1-99 ???, 100 depth is taken from the <
        DepthOrheight datagram, 200: Input from depth sensor
        """
    def get_height_type_explained(self) -> str:
        """
        Get a string description of the height_type
        
        Returns:
            std::string
        """
    def get_system_serial_number(self) -> int:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_height(self, arg0: int) -> None:
        """
        < in cm
        """
    def set_height_counter(self, arg0: int) -> None:
        """
        < Sequential Number
        """
    def set_height_type(self, arg0: int) -> None:
        """
        < 0: derived from GGK or GGA, 1-99 ???, 100 depth is taken from the <
        DepthOrheight datagram, 200: Input from depth sensor
        """
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class EM3000Datagram:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> EM3000Datagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> EM3000Datagram:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000Datagram:
        ...
    def __eq__(self, other: EM3000Datagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> EM3000Datagram:
        """
        return a copy using the c++ default copy constructor
        """
    def get_bytes(self) -> int:
        """
        < number of bytes in the datagram (not including the _bytes field
        itself)
        """
    def get_datagram_identifier(self) -> themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier:
        """
        < EM3000 datagram identifier
        """
    def get_date(self) -> int:
        """
        < year*1000 + month*100 + day(Example:Jun 27, 2020 = 20200627)
        """
    def get_date_string(self, fractional_seconds_digits: int = ..., format: str = ...) -> str:
        """
        Get the time as string
        
        Parameter ``fractionalSecondsDigits``:
            $Parameter ``format``:
        
        Returns:
            std::string
        """
    def get_model_number(self) -> int:
        """
        < EM3000 model number (example: EM 3002 = 3002)
        """
    def get_stx(self) -> int:
        """
        < (start identifier)
        """
    def get_time_since_midnight(self) -> int:
        ...
    def get_timestamp(self) -> float:
        """
        convert the date and time_since_midnight field to a unix timestamp
        
        Returns:
            unixtime as double
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_bytes(self, arg0: int) -> None:
        """
        < number of bytes in the datagram (not including the _bytes field
        itself)
        """
    def set_datagram_identifier(self, arg0: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> None:
        """
        < EM3000 datagram identifier
        """
    def set_date(self, arg0: int) -> None:
        """
        < year*1000 + month*100 + day(Example:Jun 27, 2020 = 20200627)
        """
    def set_model_number(self, arg0: int) -> None:
        """
        < EM3000 model number (example: EM 3002 = 3002)
        """
    def set_stx(self, arg0: int) -> None:
        """
        < (start identifier)
        """
    def set_time_since_midnight(self, arg0: int) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class EM3000Unknown(EM3000Datagram):
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> EM3000Unknown:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> EM3000Unknown:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000Unknown:
        ...
    def __eq__(self, other: EM3000Unknown) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> EM3000Unknown:
        """
        return a copy using the c++ default copy constructor
        """
    def get_checksum(self) -> int:
        ...
    def get_etx(self) -> int:
        ...
    def get_raw_content(self) -> str:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        ...
    def set_raw_content(self, arg0: str) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class ExtraDetections(EM3000Datagram):
    """
    This datagram is used for the models EM 2040 and EM 2040C with Slim
    Processing Unit.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> ExtraDetections:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> ExtraDetections:
        ...
    def __deepcopy__(self, arg0: dict) -> ExtraDetections:
        ...
    def __eq__(self, other: ExtraDetections) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> ExtraDetections:
        """
        return a copy using the c++ default copy constructor
        """
    def detection_classes(self) -> list[substructures.ExtraDetectionsDetectionClasses]:
        ...
    def extra_detections(self) -> list[substructures.ExtraDetectionsExtraDetections]:
        ...
    def get_checksum(self) -> int:
        ...
    def get_datagram_counter(self) -> int:
        """
        <
        """
    def get_datagram_version_id(self) -> int:
        """
        <
        """
    def get_depth_of_reference_point(self) -> float:
        """
        < m
        """
    def get_detection_classes(self) -> list[substructures.ExtraDetectionsDetectionClasses]:
        """
        < substructure 1
        """
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_extra_detections(self) -> list[substructures.ExtraDetectionsExtraDetections]:
        """
        < substructure 2
        """
    def get_heading(self) -> int:
        """
        < 0.01°
        """
    def get_heading_in_degrees(self) -> float:
        """
        Get heading in degrees
        
        Returns:
            _heading * 0.01° (double)
        """
    def get_number_of_alarm_flags(self) -> int:
        """
        <
        """
    def get_number_of_bytes_per_class(self) -> int:
        """
        <
        """
    def get_number_of_bytes_per_detection(self) -> int:
        """
        <
        """
    def get_number_of_detection_classes(self) -> int:
        """
        <
        """
    def get_number_of_extra_detections(self) -> int:
        """
        < Nd
        """
    def get_ping_counter(self) -> int:
        """
        <
        """
    def get_raw_amplitude_sample_rate(self) -> float:
        """
        < (SIsr)
        """
    def get_raw_amplitude_samples(self) -> substructures.SampleAmplitudesStructure_int16_t:
        """
        < 0.1 dB
        """
    def get_rx_transducer_index(self) -> int:
        """
        <
        """
    def get_sound_speed(self) -> int:
        """
        < dm/s
        """
    def get_sound_speed_in_m_per_s(self) -> float:
        """
        Get sound velocity in m/s
        
        Returns:
            _sound_speed * 0.1 m/s (double)
        """
    def get_swath_counter(self) -> int:
        """
        <
        """
    def get_swath_index(self) -> int:
        """
        <
        """
    def get_system_serial_number(self) -> int:
        """
        <
        """
    def get_water_column_sample_rate(self) -> float:
        """
        < (WCsr)
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def raw_amplitude_samples(self) -> substructures.SampleAmplitudesStructure_int16_t:
        ...
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_datagram_counter(self, arg0: int) -> None:
        """
        <
        """
    def set_datagram_version_id(self, arg0: int) -> None:
        """
        <
        """
    def set_depth_of_reference_point(self, arg0: float) -> None:
        """
        < m
        """
    def set_detection_classes(self, arg0: list[substructures.ExtraDetectionsDetectionClasses]) -> None:
        """
        < substructure 1
        """
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_extra_detections(self, arg0: list[substructures.ExtraDetectionsExtraDetections]) -> None:
        """
        < substructure 2
        """
    def set_heading(self, arg0: int) -> None:
        """
        < 0.01°
        """
    def set_number_of_alarm_flags(self, arg0: int) -> None:
        """
        <
        """
    def set_number_of_bytes_per_class(self, arg0: int) -> None:
        """
        <
        """
    def set_number_of_bytes_per_detection(self, arg0: int) -> None:
        """
        <
        """
    def set_number_of_detection_classes(self, arg0: int) -> None:
        """
        <
        """
    def set_number_of_extra_detections(self, arg0: int) -> None:
        """
        < Nd
        """
    def set_ping_counter(self, arg0: int) -> None:
        """
        <
        """
    def set_raw_amplitude_sample_rate(self, arg0: float) -> None:
        """
        < (SIsr)
        """
    def set_raw_amplitude_samples(self, arg0: substructures.SampleAmplitudesStructure_int16_t) -> None:
        """
        < 0.1 dB
        """
    def set_rx_transducer_index(self, arg0: int) -> None:
        """
        <
        """
    def set_sound_speed(self, arg0: int) -> None:
        """
        < dm/s
        """
    def set_swath_counter(self, arg0: int) -> None:
        """
        <
        """
    def set_swath_index(self, arg0: int) -> None:
        """
        <
        """
    def set_system_serial_number(self, arg0: int) -> None:
        """
        <
        """
    def set_water_column_sample_rate(self, arg0: float) -> None:
        """
        < (WCsr)
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class ExtraParameters(EM3000Datagram):
    """
    Clock datagrams
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> ExtraParameters:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> ExtraParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> ExtraParameters:
        ...
    def __eq__(self, other: ExtraParameters) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> ExtraParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def get_checksum(self) -> int:
        ...
    def get_content_identifier(self) -> ExtraParameters_t_ContentIdentifier:
        ...
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_ping_counter(self) -> int:
        ...
    def get_raw_content(self) -> str:
        """
        < depends on the content identifier
        """
    def get_spare(self) -> int:
        ...
    def get_system_serial_number(self) -> int:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_content_identifier(self, arg0: ExtraParameters_t_ContentIdentifier) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_ping_counter(self, arg0: int) -> None:
        ...
    def set_raw_content(self, arg0: str) -> None:
        """
        < depends on the content identifier
        """
    def set_spare(self, arg0: int) -> None:
        ...
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class ExtraParameters_t_ContentIdentifier:
    """
    
    
    Members:
    
      CalibTxt : < Calib.txt file for angle offset
    
      LogAllHeights : < Log of all heights
    
      SoundVelocityAtTransducer : < Sound velocity at transducer
    
      SoundVelocityProfile : < Sound velocity profile
    
      MultiCastInputStatus : < Multicast input status
    
      Bscorr : < Bscorr.txt file
    """
    Bscorr: typing.ClassVar[ExtraParameters_t_ContentIdentifier]  # value = <ExtraParameters_t_ContentIdentifier.Bscorr: 6>
    CalibTxt: typing.ClassVar[ExtraParameters_t_ContentIdentifier]  # value = <ExtraParameters_t_ContentIdentifier.CalibTxt: 1>
    LogAllHeights: typing.ClassVar[ExtraParameters_t_ContentIdentifier]  # value = <ExtraParameters_t_ContentIdentifier.LogAllHeights: 2>
    MultiCastInputStatus: typing.ClassVar[ExtraParameters_t_ContentIdentifier]  # value = <ExtraParameters_t_ContentIdentifier.MultiCastInputStatus: 5>
    SoundVelocityAtTransducer: typing.ClassVar[ExtraParameters_t_ContentIdentifier]  # value = <ExtraParameters_t_ContentIdentifier.SoundVelocityAtTransducer: 3>
    SoundVelocityProfile: typing.ClassVar[ExtraParameters_t_ContentIdentifier]  # value = <ExtraParameters_t_ContentIdentifier.SoundVelocityProfile: 4>
    __members__: typing.ClassVar[dict[str, ExtraParameters_t_ContentIdentifier]]  # value = {'CalibTxt': <ExtraParameters_t_ContentIdentifier.CalibTxt: 1>, 'LogAllHeights': <ExtraParameters_t_ContentIdentifier.LogAllHeights: 2>, 'SoundVelocityAtTransducer': <ExtraParameters_t_ContentIdentifier.SoundVelocityAtTransducer: 3>, 'SoundVelocityProfile': <ExtraParameters_t_ContentIdentifier.SoundVelocityProfile: 4>, 'MultiCastInputStatus': <ExtraParameters_t_ContentIdentifier.MultiCastInputStatus: 5>, 'Bscorr': <ExtraParameters_t_ContentIdentifier.Bscorr: 6>}
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
class HeadingDatagram(EM3000Datagram):
    """
    Heading datagrams
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> HeadingDatagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> HeadingDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> HeadingDatagram:
        ...
    def __eq__(self, other: HeadingDatagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> HeadingDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def get_checksum(self) -> int:
        ...
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_heading_counter(self) -> int:
        """
        < Sequential Number
        """
    def get_heading_indicator(self) -> int:
        """
        < 0 = inactive
        """
    def get_heading_timestamps(self) -> numpy.ndarray[numpy.float64]:
        """
        return the times converted to unix timestamps
        
        Returns:
            np.array([_number_of_entries], dtype = np.float64)
        """
    def get_headings_in_degrees(self) -> numpy.ndarray[numpy.float32]:
        """
        return headings in degrees by multiplying the heading by 0.01
        
        Returns:
            np.array([_number_of_entries], dtype = np.float32)
        """
    def get_number_of_entries(self) -> int:
        """
        < 0 = inactive
        """
    def get_system_serial_number(self) -> int:
        ...
    def get_times_and_headings(self) -> numpy.ndarray[numpy.uint16]:
        """
        < 2xN array of time in ms since record start and heading in 0.01°
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_heading_counter(self, arg0: int) -> None:
        """
        < Sequential Number
        """
    def set_heading_indicator(self, arg0: int) -> None:
        """
        < 0 = inactive
        """
    def set_number_of_entries(self, arg0: int) -> None:
        """
        < N
        """
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def set_times_and_headings(self, arg0: numpy.ndarray[numpy.uint16]) -> None:
        """
        < 2xN array of time in ms since record start and heading in 0.01°
        """
    def times_and_headings(self) -> numpy.ndarray[numpy.uint16]:
        """
        < 2xN array of time in ms since record start and heading in 0.01°
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class InstallationParameters(EM3000Datagram):
    """
    This datagram is an ASCII datagram except for the header which is
    formatted as in all other output datagrams. The datagram is issued as
    a start datagram when logging is switched on and as a stop datagram
    when logging is turned off, i.e. at the start and end of a survey
    line. It may also be sent to a remote port as an information datagram.
    It is usually followed by a sound speed profile datagram. In the
    datagram all ASCII fields start with a unique three character
    identifier followed by “=”. This should be used when searching for a
    specific field as the position of a field within the datagram is not
    guaranteed. The number or character part following is in a variable
    format with a minus sign and decimal point if needed, and with “,” as
    the field delimiter. The format may at any time later be expanded with
    the addition of new fields at any place in the datagram.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> InstallationParameters:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def merge(datagram_1: InstallationParameters, datagram_2: InstallationParameters) -> InstallationParameters:
        """
        Merge two InstallationParameters datagrams into one If the datagrams
        differ because an uncritical key does not exist in one of them, the
        uncritical key will be added to the resulting datagram.
        
        Parameter ``first``:
            $Parameter ``second``:
        
        Returns:
            InstallationParameters
        """
    def __copy__(self) -> InstallationParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> InstallationParameters:
        ...
    def __eq__(self, other: InstallationParameters) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def build_channel_id(self) -> str:
        ...
    def copy(self) -> InstallationParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def get_active_attitude_velocity_sensor(self) -> int:
        """
        Get the active attitude velocity sensor (not active, 1 or 2) 0: not
        used 1: Attitude Velocity Sensor 1 (assumed to be physical equal to
        Attitude sensor 1) 2: Attitude Velocity Sensor 2 (assumed to be
        physical equal to Attitude sensor 2)
        
        Returns:
            t_EM3000ActiveSensor
        """
    def get_active_heading_sensor(self) -> themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor:
        """
        Get the active heading sensor (0-9) here returned as an enum
        
        Returns:
            t_EM3000ActiveSensor
        """
    def get_active_heave_sensor(self) -> themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor:
        """
        Get the active heave sensor (2, 3, 8 or 9) here returned as an enum
        
        Returns:
            t_EM3000ActiveSensor
        """
    def get_active_pitch_roll_sensor(self) -> themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor:
        """
        Get the active roll pitch sensor (2, 3, 8 or 9) here returned as an
        enum
        
        Returns:
            t_EM3000ActiveSensor
        """
    def get_active_position_system_number(self) -> int:
        """
        Get the active position system number (APS + 1)
        
        Returns:
            uint8_t
        """
    @typing.overload
    def get_attitude_sensor_offsets(self, sensor_number: themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets:
        """
        Get the attitude sensor offsets of sensor 1 or 2
        
        Parameter ``sensor_number``:
            t_EM3000ActiveSensor (enum)
        
        Returns:
            navigation::datastructures::PositionalOffsets
        """
    @typing.overload
    def get_attitude_sensor_offsets(self, sensor: int) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets:
        """
        Get the attitude sensor offsets of sensor 1 or 2
        
        Parameter ``sensor_number``:
            t_EM3000ActiveSensor (enum)
        
        Returns:
            navigation::datastructures::PositionalOffsets
        """
    def get_checksum(self) -> int:
        ...
    def get_compass_offsets(self) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets:
        """
        Get the compass sensor offsets (Gyrocompass) Includes heading offset
        only
        
        Returns:
            navigation::datastructures::PositionalOffsets
        """
    def get_depth_sensor_offsets(self) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets:
        """
        Get the depth sensor offsets
        
        Returns:
            navigation::datastructures::PositionalOffsets
        """
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_installation_parameters(self) -> str:
        ...
    def get_installation_parameters_counter(self) -> int:
        """
        < Sequential Number
        """
    def get_installation_parameters_parsed(self) -> dict[str, str]:
        ...
    def get_position_system_offsets(self, position_system_number: int) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets:
        """
        Get the position system offsets of system 1, 2 or 3
        
        Parameter ``position_system_number``:
            must be 1, 2 or 3
        
        Returns:
            navigation::datastructures::PositionalOffsets
        """
    def get_rx1_serial_number(self) -> int:
        ...
    def get_rx2_serial_number(self) -> int:
        ...
    def get_rx_array_size(self) -> str:
        ...
    def get_secondary_system_serial_number(self) -> int:
        ...
    def get_sensor_offsets(self, sensor_name: str, sensor_prefix: str, has_xyz: bool = ..., has_ypr: bool = ...) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets:
        """
        Internal function to get the sensor offsets from the installation
        parameters. Possible sensor prefixes are: - MS for attitude sensor 1 -
        NS for attitude sensor 2 - P1 for position system 1 - P2 for position
        system 2 - P3 for position system 3 - S1 for transducer 1 - S2 for
        transducer 2 - S3 for transducer 3 - DS for depth (pressure) sensor
        
        Parameter ``sensor_name``:
            e.g. Attitude sensor 1
        
        Parameter ``sensor_prefix``:
            see above
        
        Parameter ``has_xyz``:
            sensor has xyz offsets
        
        Parameter ``has_ypr``:
            sensor has yaw pitch roll offsets
        
        Returns:
            PositionalOffsets
        """
    def get_system_main_head_serial_number(self) -> int:
        ...
    def get_system_serial_number(self) -> int:
        ...
    def get_system_transducer_configuration(self) -> themachinethatgoesping.echosounders.em3000.t_EM3000SystemTransducerConfiguration:
        ...
    def get_transducer_offsets(self, transducer_number: int, transducer_name: str = ...) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets:
        """
        Get the transducer offsets of transducer 0, 1, 2 or 3
        
        Parameter ``position_system_number``:
            must be 0, 1, 2 or 3
        
        Returns:
            navigation::datastructures::PositionalOffsets
        """
    def get_tx2_serial_number(self) -> int:
        ...
    def get_tx_array_size(self) -> str:
        ...
    def get_tx_serial_number(self) -> int:
        ...
    def get_water_line_vertical_location_in_meters(self) -> float:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def is_dual_rx(self) -> bool:
        ...
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def reparse_installation_parameters(self) -> None:
        """
        parse the installation parameters string into a map This happens when
        the datagram is read from a file, but must be called manually when the
        installation parameters string is changed manually.
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_installation_parameters(self, arg0: str) -> None:
        ...
    def set_installation_parameters_counter(self, arg0: int) -> None:
        """
        < Sequential Number
        """
    def set_secondary_system_serial_number(self, arg0: int) -> None:
        ...
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class NetworkAttitudeVelocityDatagram(EM3000Datagram):
    """
    Network attitude velocity datagram 110. This datagram is currently not
    used in the processing because the Attitude datagram already contains
    all necessary information.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> NetworkAttitudeVelocityDatagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> NetworkAttitudeVelocityDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> NetworkAttitudeVelocityDatagram:
        ...
    def __eq__(self, other: NetworkAttitudeVelocityDatagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def attitudes(self) -> list[substructures.NetworkAttitudeVelocityDatagramAttitude]:
        """
        < N x Attitude data
        """
    def copy(self) -> NetworkAttitudeVelocityDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def get_attitude_velocity_sensor_number(self) -> int:
        """
        Get the number of attitude sensor from the sensor system descriptor
        field. If this field is xx10 xxxx – attitude velocity sensor 1 (UDP5)
        xx11 xxxx – attitude velocity sensor 2 (UDP6)
        
        Returns:
            1 or 2
        """
    def get_attitudes(self) -> list[substructures.NetworkAttitudeVelocityDatagramAttitude]:
        """
        < N x Attitude data
        """
    def get_checksum(self) -> int:
        ...
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_function_is_used(self) -> bool:
        """
        Evaluate if the function is used. -1 : function is not used
        
        Returns:
            bool
        """
    def get_heading_sensor_is_active(self) -> bool:
        """
        Evaluate if the heading sensor is active using sensor system
        descriptor field. 0bxxxxxxx1 : heading is active 0bxxxxxxx1 : heading
        is inactive
        
        Returns:
            bool
        """
    def get_heave_sensor_is_active(self) -> bool:
        """
        Evaluate if the heave sensor is active using sensor system descriptor
        field. 0bxxxx1xxx : heave is active 0bxxxx0xxx : heave is inactive
        
        Returns:
            bool
        """
    def get_network_attitude_counter(self) -> int:
        ...
    def get_number_of_entries(self) -> int:
        """
        < N
        """
    def get_pitch_sensor_is_active(self) -> bool:
        """
        Evaluate if the pitch sensor is active using sensor system descriptor
        field. 0bxxxxx1xx : pitch is active 0bxxxxx0xx : pitch is inactive
        
        Returns:
            bool
        """
    def get_roll_sensor_is_active(self) -> bool:
        """
        Evaluate if the roll sensor is active using sensor system descriptor
        field. 0bxxxxxx1x : roll is active 0bxxxxxx0x : roll is inactive
        
        Returns:
            bool
        """
    def get_sensor_system_descriptor(self) -> int:
        ...
    def get_spare(self) -> int:
        ...
    def get_spare_align(self) -> int:
        ...
    def get_system_serial_number(self) -> int:
        ...
    def get_velocity_sensor_is_active(self) -> bool:
        """
        Evaluate if the velocity sensor is active using sensor system
        descriptor field. 0bxxxxxxx1 : velocity is active 0bxxxxxxx1 :
        velocity is inactive
        
        The exact meaning of this field is currently not clear to us. If this
        field is set to false, the attitude data seems to be exactly the same
        as in the attitude datagram. If it is set to true, the attitude data
        will be a little bit different.
        
        Returns:
            bool
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_attitudes(self, arg0: list[substructures.NetworkAttitudeVelocityDatagramAttitude]) -> None:
        """
        < N x Attitude data
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_network_attitude_counter(self, arg0: int) -> None:
        ...
    def set_number_of_entries(self, arg0: int) -> None:
        """
        < N
        """
    def set_sensor_system_descriptor(self, arg0: int) -> None:
        ...
    def set_spare(self, arg0: int) -> None:
        ...
    def set_spare_align(self, arg0: int) -> None:
        ...
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class PUIDOutput(EM3000Datagram):
    """
    The PU Status datagram is sent out every second if requested by the
    host processor. It has two functions, to indicate that the system is
    alive and receiving sensor data, and to give sensor data regularly for
    a potential screen update.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> PUIDOutput:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> PUIDOutput:
        ...
    def __deepcopy__(self, arg0: dict) -> PUIDOutput:
        ...
    def __eq__(self, other: PUIDOutput) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> PUIDOutput:
        """
        return a copy using the c++ default copy constructor
        """
    def get_bsp_software_date(self) -> str:
        ...
    def get_byte_order_flag(self) -> int:
        ...
    def get_checksum(self) -> int:
        ...
    def get_cpu_configuration(self) -> str:
        """
        Convert the system descriptor flag to a cpu configuration
        
        Returns:
            std::string
        """
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_has_bsp67B(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system is a
        BSP67B system
        
        This means it is not a CBMF system
        
        Returns:
            true
        
        Returns:
            false
        """
    def get_has_cbmf(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system is a
        CBMF system
        
        This means it is not a BSP67B system
        
        Returns:
            true
        
        Returns:
            false
        """
    def get_has_deep_water_sonar_head(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system has a
        deep water sonar head
        
        Returns:
            true (deep water sonar head)
        
        Returns:
            false (shallow water sonar head)s
        """
    def get_has_dual_head(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system is a
        dual head system
        
        Returns:
            true
        
        Returns:
            false
        """
    def get_has_dual_swath(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system is a
        dual swath system
        
        Returns:
            true
        
        Returns:
            false
        """
    def get_has_extra_detections_support(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system has
        extra detections support
        
        Returns:
            true
        
        Returns:
            false
        """
    def get_has_ptp_support(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system is a
        PTP (IEEE 1588 clock sync) support
        
        Returns:
            true
        
        Returns:
            false
        """
    def get_has_rs422_support(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system has
        RS422 serial lines support
        
        Returns:
            true
        
        Returns:
            false
        """
    def get_has_shallow_water_sonar_head(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system has a
        shallow water sonar head
        
        Returns:
            true (shallow water sonar head)
        
        Returns:
            false (deep water sonar head)
        """
    def get_host_ip_address(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(4)]:
        ...
    def get_host_ip_address_as_string(self) -> str:
        """
        Get the host ip address as string
        
        Returns:
            std::string
        """
    def get_pu_software_version(self) -> str:
        ...
    def get_rx_opening_angle(self) -> int:
        ...
    def get_sonar_transceiver_1_software_version(self) -> str:
        ...
    def get_sonar_transceiver_2_software_version(self) -> str:
        ...
    def get_spare(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(7)]:
        ...
    def get_system_descriptor(self) -> int:
        ...
    def get_system_serial_number(self) -> int:
        ...
    def get_tx_opening_angle(self) -> int:
        ...
    def get_udp_port_no_1(self) -> int:
        ...
    def get_udp_port_no_2(self) -> int:
        ...
    def get_udp_port_no_3(self) -> int:
        ...
    def get_udp_port_no_4(self) -> int:
        ...
    def get_which_em2040(self) -> str:
        """
        Evaluate the system_descriptor flag to determine the em2040 flag
        
        Returns:
            true
        
        Returns:
            false
        """
    def get_which_em710(self) -> str:
        """
        Evaluate the system_descriptor flag to determine the EM710 flag
        
        Returns:
            true
        
        Returns:
            false
        """
    def get_which_old_sounder(self) -> str:
        """
        Evaluate the system_descriptor flag to determine the old sounder flag
        
        Returns:
            true
        
        Returns:
            false
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_bsp_software_date(self, arg0: str) -> None:
        ...
    def set_byte_order_flag(self, arg0: int) -> None:
        ...
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_host_ip_address(self, arg0: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(4)]) -> None:
        ...
    def set_pu_software_version(self, arg0: str) -> None:
        ...
    def set_rx_opening_angle(self, arg0: int) -> None:
        ...
    def set_sonar_transceiver_1_software_version(self, arg0: str) -> None:
        ...
    def set_sonar_transceiver_2_software_version(self, arg0: str) -> None:
        ...
    def set_spare(self, arg0: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(7)]) -> None:
        ...
    def set_system_descriptor(self, arg0: int) -> None:
        ...
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def set_tx_opening_angle(self, arg0: int) -> None:
        ...
    def set_udp_port_no_1(self, arg0: int) -> None:
        ...
    def set_udp_port_no_2(self, arg0: int) -> None:
        ...
    def set_udp_port_no_3(self, arg0: int) -> None:
        ...
    def set_udp_port_no_4(self, arg0: int) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class PUStatusOutput(EM3000Datagram):
    """
    The PU Status datagram is sent out every second if requested by the
    host processor. It has two functions, to indicate that the system is
    alive and receiving sensor data, and to give sensor data regularly for
    a potential screen update.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> PUStatusOutput:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> PUStatusOutput:
        ...
    def __deepcopy__(self, arg0: dict) -> PUStatusOutput:
        ...
    def __eq__(self, other: PUStatusOutput) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> PUStatusOutput:
        """
        return a copy using the c++ default copy constructor
        """
    def get_across_ship_velocity(self) -> int:
        """
        < in cm/s (or port coverage or spare)
        """
    def get_across_ship_velocity_in_meters_per_second(self) -> float:
        """
        Get the across ship velocity in m/s
        
        Returns:
            _across_ship_velocity * 0.01f (float )
        """
    def get_along_ship_velocity(self) -> int:
        """
        < in cm/s
        """
    def get_along_ship_velocity_in_meters_per_second(self) -> float:
        """
        Get the along ship velocity in m/s
        
        Returns:
            _along_ship_velocity * 0.01f (float )
        """
    def get_attitude_status(self) -> int:
        """
        <
        """
    def get_attitude_velocity_sensor_status(self) -> int:
        """
        <
        """
    def get_backscatter_at_normal_incidence(self) -> int:
        """
        < in dB
        """
    def get_backscatter_at_oblique_angle(self) -> int:
        """
        < in dB
        """
    def get_checksum(self) -> int:
        ...
    def get_clock_status(self) -> int:
        """
        <
        """
    def get_depth_to_normal_incidence(self) -> int:
        """
        < in m
        """
    def get_distance_between_swath(self) -> int:
        """
        < in 10%
        """
    def get_distance_between_swath_in_percent(self) -> float:
        """
        Get the distance between swath in percent
        
        Returns:
            _distance_between_swath * 0.1f (float )
        """
    def get_downward_velocity(self) -> int:
        """
        < in cm/s (or starboard coverage or spare)
        """
    def get_downward_velocity_in_meters_per_second(self) -> float:
        """
        Get the downward velocity in m/s
        
        Returns:
            _downward_velocity * 0.01f (float )
        """
    def get_em2040_cpu_temperature(self) -> int:
        """
        < in degree Celsius (or spare)
        """
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_fixed_gain(self) -> int:
        """
        < in dB
        """
    def get_heading_status(self) -> int:
        """
        <
        """
    def get_last_received_depth(self) -> int:
        """
        < in cm
        """
    def get_last_received_depth_in_meters(self) -> float:
        """
        Get the last received depth in meters
        
        Returns:
            _last_received_depth * 0.01f (float )
        """
    def get_last_received_heading(self) -> int:
        """
        < in 0.01 degree
        """
    def get_last_received_heading_in_degrees(self) -> float:
        """
        Get the last received heading in degrees
        
        Returns:
            _last_received_heading * 0.01f (float )
        """
    def get_last_received_heave_at_sonar_head(self) -> int:
        """
        < in cm
        """
    def get_last_received_pitch(self) -> int:
        """
        < in 0.01 degree
        """
    def get_last_received_pitch_in_degrees(self) -> float:
        """
        Get the last received pitch in degrees
        
        Returns:
            _last_received_pitch * 0.01f (float )
        """
    def get_last_received_roll(self) -> int:
        """
        < in 0.01 degree
        """
    def get_last_received_roll_in_degrees(self) -> float:
        """
        Get the last received roll in degrees
        
        Returns:
            _last_received_roll * 0.01f (float )
        """
    def get_mammal_protection_ramp(self) -> int:
        """
        <
        """
    def get_ping_counter(self) -> int:
        """
        < of latest ping
        """
    def get_ping_rate(self) -> int:
        """
        < in 0.01 Hz
        """
    def get_ping_rate_hertz(self) -> float:
        """
        Get the ping rate in Hz
        
        Returns:
            _ping_rate * 0.01 Hz (float)
        """
    def get_port_coverage(self) -> int:
        """
        < in degrees
        """
    def get_position_status(self) -> int:
        """
        <
        """
    def get_pps_status(self) -> int:
        """
        <
        """
    def get_pu_status(self) -> int:
        """
        <
        """
    def get_range_to_normal_incidence(self) -> int:
        """
        < in m
        """
    def get_sensor_input_status_serial_port_1(self) -> int:
        """
        <
        """
    def get_sensor_input_status_serial_port_2(self) -> int:
        """
        <
        """
    def get_sensor_input_status_serial_port_3(self) -> int:
        """
        <
        """
    def get_sensor_input_status_serial_port_4(self) -> int:
        """
        <
        """
    def get_sensor_input_status_udp_port_2(self) -> int:
        """
        <
        """
    def get_sound_speed_at_transducer(self) -> int:
        """
        < in dm/s
        """
    def get_sound_speed_at_transducer_from_profile(self) -> int:
        """
        < in dm/s
        """
    def get_sound_speed_at_transducer_from_profile_in_meters_per_second(self) -> float:
        """
        Get the sound speed at transducer (derived from profile) in m/s
        
        Returns:
            _sound_speed_at_transducer_from_profile * 0.1f (float )
        """
    def get_sound_speed_at_transducer_in_meters_per_second(self) -> float:
        """
        Get the last received heave at sonar head in meters per second
        
        Returns:
            _sound_speed_at_transducer * 0.1f (float )
        """
    def get_starboard_coverage(self) -> int:
        """
        < in degrees
        """
    def get_status_datagram_counter(self) -> int:
        ...
    def get_system_serial_number(self) -> int:
        ...
    def get_yaw_stabilization_angle(self) -> int:
        """
        < in 0.01 degree, or tilt used at 3D scanning
        """
    def get_yaw_stabilization_angle_in_degrees(self) -> float:
        """
        Get the yaw stabilization angle in degrees
        
        Returns:
            _yaw_stabilization_angle * 0.01f (float )
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_across_ship_velocity(self, arg0: int) -> None:
        """
        < in cm/s (or port coverage or spare)
        """
    def set_along_ship_velocity(self, arg0: int) -> None:
        """
        < in cm/s
        """
    def set_attitude_status(self, arg0: int) -> None:
        """
        <
        """
    def set_attitude_velocity_sensor_status(self, arg0: int) -> None:
        """
        <
        """
    def set_backscatter_at_normal_incidence(self, arg0: int) -> None:
        """
        < in dB
        """
    def set_backscatter_at_oblique_angle(self, arg0: int) -> None:
        """
        < in dB
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_clock_status(self, arg0: int) -> None:
        """
        <
        """
    def set_depth_to_normal_incidence(self, arg0: int) -> None:
        """
        < in m
        """
    def set_distance_between_swath(self, arg0: int) -> None:
        """
        < in 10%
        """
    def set_downward_velocity(self, arg0: int) -> None:
        """
        < in cm/s (or starboard coverage or spare)
        """
    def set_em2040_cpu_temperature(self, arg0: int) -> None:
        """
        < in degree Celsius (or spare)
        """
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_fixed_gain(self, arg0: int) -> None:
        """
        < in dB
        """
    def set_heading_status(self, arg0: int) -> None:
        """
        <
        """
    def set_last_received_depth(self, arg0: int) -> None:
        """
        < in cm
        """
    def set_last_received_heading(self, arg0: int) -> None:
        """
        < in 0.01 degree
        """
    def set_last_received_heave_at_sonar_head(self, arg0: int) -> None:
        """
        < in cm
        """
    def set_last_received_pitch(self, arg0: int) -> None:
        """
        < in 0.01 degree
        """
    def set_last_received_roll(self, arg0: int) -> None:
        """
        < in 0.01 degree
        """
    def set_mammal_protection_ramp(self, arg0: int) -> None:
        """
        <
        """
    def set_ping_counter(self, arg0: int) -> None:
        """
        < of latest ping
        """
    def set_ping_rate(self, arg0: int) -> None:
        """
        < in 0.01 Hz
        """
    def set_port_coverage(self, arg0: int) -> None:
        """
        < in degrees
        """
    def set_position_status(self, arg0: int) -> None:
        """
        <
        """
    def set_pps_status(self, arg0: int) -> None:
        """
        <
        """
    def set_pu_status(self, arg0: int) -> None:
        """
        <
        """
    def set_range_to_normal_incidence(self, arg0: int) -> None:
        """
        < in m
        """
    def set_sensor_input_status_serial_port_1(self, arg0: int) -> None:
        """
        <
        """
    def set_sensor_input_status_serial_port_2(self, arg0: int) -> None:
        """
        <
        """
    def set_sensor_input_status_serial_port_3(self, arg0: int) -> None:
        """
        <
        """
    def set_sensor_input_status_serial_port_4(self, arg0: int) -> None:
        """
        <
        """
    def set_sensor_input_status_udp_port_2(self, arg0: int) -> None:
        """
        <
        """
    def set_sound_speed_at_transducer(self, arg0: int) -> None:
        """
        < in dm/s
        """
    def set_sound_speed_at_transducer_from_profile(self, arg0: int) -> None:
        """
        < in dm/s
        """
    def set_starboard_coverage(self, arg0: int) -> None:
        """
        < in degrees
        """
    def set_status_datagram_counter(self, arg0: int) -> None:
        ...
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def set_yaw_stabilization_angle(self, arg0: int) -> None:
        """
        < in 0.01 degree, or tilt used at 3D scanning
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class PositionDatagram(EM3000Datagram):
    """
    Depth (pressure) or height datagrams
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> PositionDatagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> PositionDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> PositionDatagram:
        ...
    def __eq__(self, other: PositionDatagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> PositionDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def get_checksum(self) -> int:
        ...
    def get_course(self) -> int:
        """
        < over ground in 0.01°
        """
    def get_course_in_degrees(self) -> float:
        """
        Get the course of vessel in degrees
        
        Returns:
            _course * 0.01° (float)
        """
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_heading(self) -> int:
        """
        < in 0.01°
        """
    def get_heading_in_degrees(self) -> float:
        """
        Get the heading of vessel in degrees
        
        Returns:
            _heading * 0.01° (float)
        """
    def get_latitude(self) -> int:
        """
        < latitude in 0.00000005° negative if southern hemishpere
        """
    def get_latitude_in_degrees(self) -> float:
        """
        Get the latitude in degrees
        
        Returns:
            _latitude * 0.00000005° (double)
        """
    def get_longitude(self) -> int:
        """
        < longitude in 0.0000001° negative if western hemishpere
        """
    def get_longitude_in_degrees(self) -> float:
        """
        Get the longitude in degrees
        
        Returns:
            _longitude * 0.0000001° (double)
        """
    def get_position_counter(self) -> int:
        ...
    def get_position_fix_quality(self) -> int:
        """
        < fix quality in cm;
        """
    def get_position_fix_quality_in_meters(self) -> float:
        """
        Get the position fix quality in meters
        
        Returns:
            _position_fix_quality * 0.01m (float)
        """
    def get_position_system_SIMRAD90_flag(self) -> bool:
        """
        Evaluate if the position_system_descriptor for the used system number
        
        xxxx 1xxx – the position may have to be derived from the input
        datagram which is then in SIMRAD 90 format.
        
        Returns:
            true or false (bool)
        """
    def get_position_system_descriptor(self) -> int:
        ...
    def get_position_system_number(self) -> int:
        """
        Evaluate if the position_system_descriptor for the used system number
        
        Returns:
            1, 2 or 3 (uint8_t )
        """
    def get_position_system_system_time_has_been_used(self) -> bool:
        """
        Evaluate the position_system_descriptor for the used time
        
        Returns:
            true: system time has been used
        
        Returns:
            false: input datagram time has been used
        """
    def get_size_of_input_datagram(self) -> int:
        """
        < in input datagram;
        """
    def get_spare(self) -> int:
        """
        < only if required to make the datagram size even
        """
    def get_speed(self) -> int:
        """
        < over ground in cm/s
        """
    def get_speed_in_meters_per_second(self) -> float:
        """
        Get the speed of vessel in meter per second
        
        Returns:
            _speed * 0.01m/s (float)
        """
    def get_system_serial_number(self) -> int:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_course(self, arg0: int) -> None:
        """
        < over ground in 0.01°
        """
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_heading(self, arg0: int) -> None:
        """
        < in 0.01°
        """
    def set_latitude(self, arg0: int) -> None:
        """
        < latitude in 0.00000005° negative if southern hemishpere
        """
    def set_longitude(self, arg0: int) -> None:
        """
        < longitude in 0.0000001° negative if western hemishpere
        """
    def set_position_counter(self, arg0: int) -> None:
        ...
    def set_position_fix_quality(self, arg0: int) -> None:
        """
        < fix quality in cm;
        """
    def set_position_system_descriptor(self, arg0: int) -> None:
        ...
    def set_size_of_input_datagram(self, arg0: int) -> None:
        """
        < in input datagram;
        """
    def set_spare(self, arg0: int) -> None:
        """
        < only if required to make the datagram size even
        """
    def set_speed(self, arg0: int) -> None:
        """
        < over ground in cm/s
        """
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class QualityFactorDatagram(EM3000Datagram):
    """
    The Quality Factor is an estimate of the standard deviation of the
    detected depth. QF = − log(Est(dz)/z) QF = 3.0 means an estimated
    standard deviation of 0.1% of the detected depth. QF = 2.0 means an
    estimated standard deviation of 1.0% of the detected depth. QF = 0
    means that the Quality Factor could not be computed. The Quality
    Factor is calculated by the echo sounder according to formulas
    provided by IFREMER. Used for EM 122, EM 302, EM 710, EM 2040, EM
    2040C, EM 3002 and ME70BO.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> QualityFactorDatagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> QualityFactorDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> QualityFactorDatagram:
        ...
    def __eq__(self, other: QualityFactorDatagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> QualityFactorDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def get_checksum(self) -> int:
        ...
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_number_of_parameters_per_beam(self) -> int:
        """
        < Npar
        """
    def get_number_of_receive_beams(self) -> int:
        """
        < Nrx
        """
    def get_ping_counter(self) -> int:
        """
        < 0-65535 ping number (in this file)
        """
    def get_quality_factors(self) -> numpy.ndarray[numpy.float32]:
        """
        < dimension is [Nrx, Npar]
        """
    def get_spare(self) -> int:
        """
        < always 0
        """
    def get_system_serial_number(self) -> int:
        """
        < 100 -
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def qf_shape(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)]:
        """
        return the shape of the quality factor array Computed as
        [_number_of_receive_beams, _number_of_parameters_per_beam]
        
        Returns:
            xt::xtensor<float, 2>::shape_type
        """
    def quality_factors(self) -> numpy.ndarray[numpy.float32]:
        """
        < dimension is [Nrx, Npar]
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_number_of_parameters_per_beam(self, arg0: int) -> None:
        """
        < Npar
        """
    def set_number_of_receive_beams(self, arg0: int) -> None:
        """
        < Nrx
        """
    def set_ping_counter(self, arg0: int) -> None:
        """
        < 0-65535 ping number (in this file)
        """
    def set_quality_factors(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < dimension is [Nrx, Npar]
        """
    def set_spare(self, arg0: int) -> None:
        """
        < always 0
        """
    def set_system_serial_number(self, arg0: int) -> None:
        """
        < 100 -
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class RawRangeAndAngle(EM3000Datagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
    122, EM 302 and ME70BO. All receiver beams are included, check
    detection info and real time cleaning for beam status (note 4 and 5).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> RawRangeAndAngle:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> RawRangeAndAngle:
        ...
    def __deepcopy__(self, arg0: dict) -> RawRangeAndAngle:
        ...
    def __eq__(self, other: RawRangeAndAngle) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def beams(self) -> list[substructures.RawRangeAndAngleBeam]:
        ...
    def copy(self) -> RawRangeAndAngle:
        """
        return a copy using the c++ default copy constructor
        """
    def get_beams(self) -> list[substructures.RawRangeAndAngleBeam]:
        ...
    def get_checksum(self) -> int:
        ...
    def get_d_scale(self) -> int:
        ...
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_number_of_receiver_beams(self) -> int:
        """
        < in Datagram nrx
        """
    def get_number_of_transmit_sectors(self) -> int:
        """
        < ntx
        """
    def get_number_of_valid_detections(self) -> int:
        ...
    def get_ping_counter(self) -> int:
        """
        < sequential number
        """
    def get_sampling_frequency(self) -> float:
        ...
    def get_sound_speed_at_transducer(self) -> int:
        """
        < in 0.1 m/s
        """
    def get_sound_speed_at_transducer_in_m_per_s(self) -> float:
        """
        Get the sound speed at the transducerin meters per seconds
        
        Returns:
            _sound_speed_at_transducer * 0.1 meters per seconds (float)
        """
    def get_system_serial_number(self) -> int:
        ...
    def get_transmit_sectors(self) -> list[substructures.RawRangeAndAngleTransmitSector]:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_beams(self, arg0: list[substructures.RawRangeAndAngleBeam]) -> None:
        ...
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_d_scale(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_number_of_receiver_beams(self, arg0: int) -> None:
        """
        < in Datagram nrx
        """
    def set_number_of_transmit_sectors(self, arg0: int) -> None:
        """
        < ntx
        """
    def set_number_of_valid_detections(self, arg0: int) -> None:
        ...
    def set_ping_counter(self, arg0: int) -> None:
        """
        < sequential number
        """
    def set_sampling_frequency(self, arg0: float) -> None:
        ...
    def set_sound_speed_at_transducer(self, arg0: int) -> None:
        """
        < in 0.1 m/s
        """
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def set_transmit_sectors(self, arg0: list[substructures.RawRangeAndAngleTransmitSector]) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
    def transmit_sectors(self) -> list[substructures.RawRangeAndAngleTransmitSector]:
        ...
class RuntimeParameters(EM3000Datagram):
    """
    Runtime parameters datagrams
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> RuntimeParameters:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> RuntimeParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> RuntimeParameters:
        ...
    def __eq__(self, other: RuntimeParameters) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> RuntimeParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def get_absorption_coefficient(self) -> int:
        """
        < in 0.01 dB/km
        """
    def get_absorption_coefficient_in_db_per_meter(self) -> float:
        """
        Get the absorption coefficient in db per meter
        
        Returns:
            _absorption_coefficient * 0.00001f (float)
        """
    def get_beam_spacing(self) -> int:
        ...
    def get_bsp_status(self) -> int:
        ...
    def get_checksum(self) -> int:
        ...
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_filter_identifier(self) -> int:
        ...
    def get_filter_identifier2(self) -> int:
        ...
    def get_maximum_depth(self) -> int:
        """
        < in meter
        """
    def get_maximum_port_coverage(self) -> int:
        """
        < in degrees
        """
    def get_maximum_port_swath_width(self) -> int:
        """
        < in meter
        """
    def get_maximum_starboard_coverage(self) -> int:
        """
        < in degrees
        """
    def get_maximum_starboard_swath_width(self) -> int:
        """
        < in meter
        """
    def get_minimum_depth(self) -> int:
        """
        < in meter
        """
    def get_mode(self) -> int:
        ...
    def get_mode2_or_receiver_fixed_gain_setting(self) -> int:
        """
        < in dB
        """
    def get_operator_station_status(self) -> int:
        ...
    def get_ping_counter(self) -> int:
        ...
    def get_processing_unit_status(self) -> int:
        ...
    def get_receive_bandwidth_50hz(self) -> int:
        """
        < in 50 Hz resolution
        """
    def get_receive_bandwidth_in_hertz(self) -> float:
        """
        Get the receive bandwidth in Hz
        
        Returns:
            _receive_bandwidth_50hz * 50.f (float)
        """
    def get_receive_beamwidth_degree(self) -> int:
        """
        < in 0.1 degrees
        """
    def get_receive_beamwidth_in_degrees(self) -> float:
        """
        Get the receive beamwidth in degrees
        
        Returns:
            _receive_beamwidth_degree * 0.1f (float)
        """
    def get_sonar_head_or_transceiver_status(self) -> int:
        ...
    def get_source_of_sound_speed_at_transducer(self) -> int:
        ...
    def get_system_serial_number(self) -> int:
        ...
    def get_transmit_along_tilt(self) -> int:
        """
        < in 0.1 degree
        """
    def get_transmit_along_tilt_in_degrees(self) -> float:
        """
        Get the transmit along tilt in degrees
        
        Returns:
            _transmit_along_tilt * 0.1f (float)
        """
    def get_transmit_beamwidth(self) -> int:
        """
        < in 0.1 degrees
        """
    def get_transmit_beamwidth_in_degrees(self) -> float:
        """
        Get the transmit beamwidth in degrees
        
        Returns:
            _transmit_beamwidth * 0.1f (float)
        """
    def get_transmit_power_relative_maximum(self) -> int:
        """
        < in dB
        """
    def get_transmit_pulse_length(self) -> int:
        """
        < in μs
        """
    def get_transmit_pulse_length_in_seconds(self) -> float:
        """
        Get the transmit pulse length in seconds
        
        Returns:
            _transmit_pulse_length * 0.000001f (float)
        """
    def get_tvg_law_crossover_angle(self) -> int:
        """
        < in degrees
        """
    def get_yaw_and_pitch_stabilization_mode(self) -> int:
        ...
    def hash_content_only(self) -> int:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_absorption_coefficient(self, arg0: int) -> None:
        """
        < in 0.01 dB/km
        """
    def set_beam_spacing(self, arg0: int) -> None:
        ...
    def set_bsp_status(self, arg0: int) -> None:
        ...
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_filter_identifier(self, arg0: int) -> None:
        ...
    def set_filter_identifier2(self, arg0: int) -> None:
        ...
    def set_maximum_depth(self, arg0: int) -> None:
        """
        < in meter
        """
    def set_maximum_port_coverage(self, arg0: int) -> None:
        """
        < in degrees
        """
    def set_maximum_port_swath_width(self, arg0: int) -> None:
        """
        < in meter
        """
    def set_maximum_starboard_coverage(self, arg0: int) -> None:
        """
        < in degrees
        """
    def set_maximum_starboard_swath_width(self, arg0: int) -> None:
        """
        < in meter
        """
    def set_minimum_depth(self, arg0: int) -> None:
        """
        < in meter
        """
    def set_mode(self, arg0: int) -> None:
        ...
    def set_mode2_or_receiver_fixed_gain_setting(self, arg0: int) -> None:
        """
        < in dB
        """
    def set_operator_station_status(self, arg0: int) -> None:
        ...
    def set_ping_counter(self, arg0: int) -> None:
        ...
    def set_processing_unit_status(self, arg0: int) -> None:
        ...
    def set_receive_bandwidth_50hz(self, arg0: int) -> None:
        """
        < in 50 Hz resolution
        """
    def set_receive_beamwidth_degree(self, arg0: int) -> None:
        """
        < in 0.1 degrees
        """
    def set_sonar_head_or_transceiver_status(self, arg0: int) -> None:
        ...
    def set_source_of_sound_speed_at_transducer(self, arg0: int) -> None:
        ...
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def set_transmit_along_tilt(self, arg0: int) -> None:
        """
        < in 0.1 degree
        """
    def set_transmit_beamwidth(self, arg0: int) -> None:
        """
        < in 0.1 degrees
        """
    def set_transmit_power_relative_maximum(self, arg0: int) -> None:
        """
        < in dB
        """
    def set_transmit_pulse_length(self, arg0: int) -> None:
        """
        < in μs
        """
    def set_tvg_law_crossover_angle(self, arg0: int) -> None:
        """
        < in degrees
        """
    def set_yaw_and_pitch_stabilization_mode(self, arg0: int) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class SeabedImageData(EM3000Datagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
    122, EM 302 and ME70BO. All receiver beams are included, check
    detection info and real time cleaning for beam status (note 4 and 5).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> SeabedImageData:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SeabedImageData:
        ...
    def __deepcopy__(self, arg0: dict) -> SeabedImageData:
        ...
    def __eq__(self, other: SeabedImageData) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def beams(self) -> list[substructures.SeabedImageDataBeam]:
        ...
    def copy(self) -> SeabedImageData:
        """
        return a copy using the c++ default copy constructor
        """
    def get_beams(self) -> list[substructures.SeabedImageDataBeam]:
        ...
    def get_checksum(self) -> int:
        ...
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_normal_incidence_backscatter(self) -> int:
        """
        < in 0.01 dB (BSN)
        """
    def get_normal_incidence_backscatter_in_db(self) -> float:
        """
        Get the normal incidence backscatter in db
        
        Returns:
            _normal_incidence_backscatter * 0.01f (float)
        """
    def get_number_of_valid_beams(self) -> int:
        ...
    def get_oblique_backscatter(self) -> int:
        """
        < in 0.01 dB (BSO)
        """
    def get_oblique_backscatter_in_db(self) -> float:
        """
        Get the oblique backscatter in db
        
        Returns:
            _oblique_backscatter * 0.01f (float)
        """
    def get_ping_counter(self) -> int:
        """
        < sequential number
        """
    def get_range_to_normal_incidence(self) -> int:
        """
        < used to correct sample amplitudes in no. of samples
        """
    def get_sample_amplitudes(self) -> substructures.SampleAmplitudesStructure_int16_t:
        """
        < in 0.1 dB (size = sum of _Number_of_samples of all Beams
        """
    def get_sampling_frequency(self) -> float:
        """
        < in Hz
        """
    def get_spare_byte(self) -> int:
        ...
    def get_system_serial_number(self) -> int:
        ...
    def get_tvg_law_crossover_angle(self) -> int:
        """
        < in 0.1 degree
        """
    def get_tvg_law_crossover_angle_in_degrees(self) -> float:
        """
        get the tvg law crossover angle in degrees
        
        Returns:
            _tvg_law_crossover_angle * 0.1f (float)
        """
    def get_tx_beamwidth_along(self) -> int:
        """
        < in 0.1 degree
        """
    def get_tx_beamwidth_along_in_degrees(self) -> float:
        """
        get the tx beamwidth along in degrees
        
        Returns:
            _tx_beamwidth_along * 0.1f (float)
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def sample_amplitudes(self) -> substructures.SampleAmplitudesStructure_int16_t:
        """
        < in 0.1 dB (size = sum of _Number_of_samples of all Beams
        """
    def set_beams(self, arg0: list[substructures.SeabedImageDataBeam]) -> None:
        ...
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_normal_incidence_backscatter(self, arg0: int) -> None:
        """
        < in 0.01 dB (BSN)
        """
    def set_number_of_valid_beams(self, arg0: int) -> None:
        ...
    def set_oblique_backscatter(self, arg0: int) -> None:
        """
        < in 0.01 dB (BSO)
        """
    def set_ping_counter(self, arg0: int) -> None:
        """
        < sequential number
        """
    def set_range_to_normal_incidence(self, arg0: int) -> None:
        """
        < used to correct sample amplitudes in no. of samples
        """
    def set_sample_amplitudes(self, arg0: substructures.SampleAmplitudesStructure_int16_t) -> None:
        """
        < in 0.1 dB (size = sum of _Number_of_samples of all Beams
        """
    def set_sampling_frequency(self, arg0: float) -> None:
        """
        < in Hz
        """
    def set_spare_byte(self, arg0: int) -> None:
        ...
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def set_tvg_law_crossover_angle(self, arg0: int) -> None:
        """
        < in 0.1 degree
        """
    def set_tx_beamwidth_along(self, arg0: int) -> None:
        """
        < in 0.1 degree
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class SingleBeamEchoSounderDepth(EM3000Datagram):
    """
    Single beam echo sounder depth datagram
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> SingleBeamEchoSounderDepth:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SingleBeamEchoSounderDepth:
        ...
    def __deepcopy__(self, arg0: dict) -> SingleBeamEchoSounderDepth:
        ...
    def __eq__(self, other: SingleBeamEchoSounderDepth) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> SingleBeamEchoSounderDepth:
        """
        return a copy using the c++ default copy constructor
        """
    def get_checksum(self) -> int:
        ...
    def get_echo_sounder_counter(self) -> int:
        """
        < Sequential Number
        """
    def get_echo_sounder_depth(self) -> int:
        """
        < from waterline in cm
        """
    def get_echo_sounder_depth_in_meters(self) -> float:
        """
        Get the echo sounder depth in meters
        
        Returns:
            _echo_sounder_depth * 0.01f (float)
        """
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_input_date(self) -> int:
        """
        < year*10000 + month*100 + day (from input datagram if available)
        """
    def get_input_date_string(self, arg0: int, arg1: str) -> str:
        """
        Get the time as string
        
        Parameter ``fractionalSecondsDigits``:
            $Parameter ``format``:
        
        Returns:
            std::string
        """
    def get_input_time_since_midnight(self) -> int:
        """
        < time since midnight in milliseconds (from input < datagram if
        available)
        """
    def get_input_timestamp(self) -> float:
        """
        convert the date and time_since_midnight field to a unix timestamp
        
        Returns:
            unixtime as double
        """
    def get_source_identifier(self) -> str:
        """
        < 'S', 'T', '1', '2' or '3'
        """
    def get_system_serial_number(self) -> int:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_echo_sounder_counter(self, arg0: int) -> None:
        """
        < Sequential Number
        """
    def set_echo_sounder_depth(self, arg0: int) -> None:
        """
        < from waterline in cm
        """
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_input_date(self, arg0: int) -> None:
        """
        < year*10000 + month*100 + day (from input datagram if available)
        """
    def set_input_time_since_midnight(self, arg0: int) -> None:
        """
        < time since midnight in milliseconds (from input < datagram if
        available)
        """
    def set_source_identifier(self, arg0: str) -> None:
        """
        < 'S', 'T', '1', '2' or '3'
        """
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class SoundSpeedProfileDatagram(EM3000Datagram):
    """
    This datagram will contain the profile actually used in the real time
    raybending calculations to convert range and angle to xyz data. It
    will usually be issued together with the installation parameter
    datagram.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> SoundSpeedProfileDatagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SoundSpeedProfileDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> SoundSpeedProfileDatagram:
        ...
    def __eq__(self, other: SoundSpeedProfileDatagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> SoundSpeedProfileDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def depths_and_sound_speeds(self) -> numpy.ndarray[numpy.uint32]:
        """
        < 2xN array of depth in cm and sound speed in dm/s
        """
    def get_checksum(self) -> int:
        ...
    def get_depth_resolution(self) -> int:
        """
        < in cm
        """
    def get_depth_resolution_in_meters(self) -> float:
        """
        return the depths in meters
        
        Returns:
            _depth_resolution * 0.01 (float)
        """
    def get_depths_and_sound_speeds(self) -> numpy.ndarray[numpy.uint32]:
        """
        < 2xN array of depth in cm and sound speed in dm/s
        """
    def get_depths_in_meters(self) -> numpy.ndarray[numpy.float64]:
        """
        return the depths in meters by multiplying the depths by 0.01
        
        Returns:
            np.array([_number_of_entries], dtype = np.float64)
        """
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_number_of_entries(self) -> int:
        ...
    def get_profile_counter(self) -> int:
        """
        < Sequential Number
        """
    def get_profile_date(self) -> int:
        """
        < year*10000 + month*100 + day (when profile was taken)
        """
    def get_profile_date_string(self, arg0: int, arg1: str) -> str:
        """
        Get the profile time as string
        
        Parameter ``fractionalSecondsDigits``:
            $Parameter ``format``:
        
        Returns:
            std::string
        """
    def get_profile_time_since_midnight(self) -> int:
        """
        < time since midnight in milliseconds (when profile < was taken)
        """
    def get_profile_timestamp(self) -> float:
        """
        convert the profile date and time_since_midnight field to a unix
        timestamp
        
        Returns:
            unixtime as double
        """
    def get_sound_speeds_in_meters_per_second(self) -> numpy.ndarray[numpy.float32]:
        """
        return sound speeds in meter per second by multiplying the
        sound_speeds by 0.1
        
        Returns:
            np.array([_number_of_entries], dtype = np.float32)
        """
    def get_spare(self) -> int:
        ...
    def get_system_serial_number(self) -> int:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_depth_resolution(self, arg0: int) -> None:
        """
        < in cm
        """
    def set_depths_and_sound_speeds(self, arg0: numpy.ndarray[numpy.uint32]) -> None:
        """
        < 2xN array of depth in cm and sound speed in dm/s
        """
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_number_of_entries(self, arg0: int) -> None:
        """
        < N
        """
    def set_profile_counter(self, arg0: int) -> None:
        """
        < Sequential Number
        """
    def set_profile_date(self, arg0: int) -> None:
        """
        < year*10000 + month*100 + day (when profile was taken)
        """
    def set_profile_time_since_midnight(self, arg0: int) -> None:
        """
        < time since midnight in milliseconds (when profile < was taken)
        """
    def set_spare(self, arg0: int) -> None:
        ...
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class SurfaceSoundSpeedDatagram(EM3000Datagram):
    """
    Sound_speed datagrams
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> SurfaceSoundSpeedDatagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SurfaceSoundSpeedDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> SurfaceSoundSpeedDatagram:
        ...
    def __eq__(self, other: SurfaceSoundSpeedDatagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def copy(self) -> SurfaceSoundSpeedDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def get_checksum(self) -> int:
        ...
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_number_of_entries(self) -> int:
        ...
    def get_sound_speed_counter(self) -> int:
        """
        < Sequential Number
        """
    def get_sound_speed_timestamps(self) -> numpy.ndarray[numpy.float64]:
        """
        return the times converted to unix timestamps
        
        Returns:
            np.array([_number_of_entries], dtype = np.float64)
        """
    def get_sound_speeds_in_meters_per_second(self) -> numpy.ndarray[numpy.float32]:
        """
        return sound_speeds in meters by multiplying the surface sound_speed
        by 0.1
        
        Returns:
            np.array([_number_of_entries], dtype = np.float32)
        """
    def get_spare(self) -> int:
        ...
    def get_system_serial_number(self) -> int:
        ...
    def get_times_and_sound_speeds(self) -> numpy.ndarray[numpy.uint16]:
        """
        < 2xN array of time in ms since record < start and sound_speed in dm/s
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_number_of_entries(self, arg0: int) -> None:
        """
        < N
        """
    def set_sound_speed_counter(self, arg0: int) -> None:
        """
        < Sequential Number
        """
    def set_spare(self, arg0: int) -> None:
        ...
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def set_times_and_sound_speeds(self, arg0: numpy.ndarray[numpy.uint16]) -> None:
        """
        < 2xN array of time in ms since record < start and sound_speed in dm/s
        """
    def times_and_sound_speeds(self) -> numpy.ndarray[numpy.uint16]:
        """
        < 2xN array of time in ms since record < start and sound_speed in dm/s
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class WatercolumnDatagram(EM3000Datagram):
    """
    Used for EM 122, EM 302, EM 710, EM 2040, EM 3002. The receiver beams
    are roll stabilized.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> WatercolumnDatagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> WatercolumnDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> WatercolumnDatagram:
        ...
    def __eq__(self, other: WatercolumnDatagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def beams(self) -> list[substructures.WatercolumnDatagramBeam]:
        ...
    def copy(self) -> WatercolumnDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def get_beams(self) -> list[substructures.WatercolumnDatagramBeam]:
        ...
    def get_checksum(self) -> int:
        ...
    def get_datagram_number(self) -> int:
        ...
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_number_of_beams_in_datagram(self) -> int:
        """
        < Beam vector of 2 elements
        """
    def get_number_of_datagrams(self) -> int:
        ...
    def get_number_of_transmit_sectors(self) -> int:
        """
        < Transmit_sector vector of 2 elements
        """
    def get_ping_counter(self) -> int:
        ...
    def get_samples(self) -> numpy.ndarray[numpy.float32]:
        ...
    def get_sampling_frequency(self) -> int:
        ...
    def get_sampling_frequency_in_hz(self) -> float:
        """
        Get the sampling frequency in Hz
        
        Returns:
            _sampling_frequency * 0.01 Hz (float)
        """
    def get_scanning_info(self) -> int:
        ...
    def get_sound_speed(self) -> int:
        """
        < in 0.1 m/s
        """
    def get_sound_speed_m_s(self) -> float:
        """
        Get the sound speed in m/s
        
        Returns:
            _sound_speed * 0.1 m/s (float)
        """
    def get_spare(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]:
        ...
    def get_system_serial_number(self) -> int:
        ...
    def get_total_no_of_receive_beams(self) -> int:
        ...
    def get_transmit_sectors(self) -> list[substructures.WatercolumnDatagramTransmitSector]:
        ...
    def get_tvg_function_applied(self) -> int:
        ...
    def get_tvg_offset_in_db(self) -> int:
        ...
    def get_tx_time_heave(self) -> int:
        """
        < in cm
        """
    def get_tx_time_heave_in_m(self) -> float:
        """
        Get the transmit time heave in m
        
        Returns:
            _tx_time_heave * 0.01 m (float)
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_beams(self, arg0: list[substructures.WatercolumnDatagramBeam]) -> None:
        ...
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_datagram_number(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_number_of_beams_in_datagram(self, arg0: int) -> None:
        """
        < Beam vector of 2 elements
        """
    def set_number_of_datagrams(self, arg0: int) -> None:
        ...
    def set_number_of_transmit_sectors(self, arg0: int) -> None:
        """
        < Transmit_sector vector of 2 elements
        """
    def set_ping_counter(self, arg0: int) -> None:
        ...
    def set_sampling_frequency(self, arg0: int) -> None:
        ...
    def set_scanning_info(self, arg0: int) -> None:
        ...
    def set_sound_speed(self, arg0: int) -> None:
        """
        < in 0.1 m/s
        """
    def set_spare(self, arg0: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        ...
    def set_system_serial_number(self, arg0: int) -> None:
        ...
    def set_total_no_of_receive_beams(self, arg0: int) -> None:
        ...
    def set_transmit_sectors(self, arg0: list[substructures.WatercolumnDatagramTransmitSector]) -> None:
        ...
    def set_tvg_function_applied(self, arg0: int) -> None:
        ...
    def set_tvg_offset_in_db(self, arg0: int) -> None:
        ...
    def set_tx_time_heave(self, arg0: int) -> None:
        """
        < in cm
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
    def transmit_sectors(self) -> list[substructures.WatercolumnDatagramTransmitSector]:
        ...
class XYZDatagram(EM3000Datagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
    122, EM 302 and ME70BO. All receiver beams are included, check
    detection info and real time cleaning for beam status (note 4 and 5).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> XYZDatagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XYZDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> XYZDatagram:
        ...
    def __eq__(self, other: XYZDatagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None:
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
    def beams(self) -> list[substructures.XYZDatagramBeam]:
        """
        < beam detection information
        """
    def copy(self) -> XYZDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def get_beams(self) -> list[substructures.XYZDatagramBeam]:
        """
        < beam detection information
        """
    def get_checksum(self) -> int:
        ...
    def get_etx(self) -> int:
        """
        < end identifier (always 0x03)
        """
    def get_heading(self) -> int:
        """
        < (at TX time) in 0.01 degree
        """
    def get_heading_in_degrees(self) -> float:
        """
        Get the vessel heading in degrees
        
        Returns:
            heading * 0.01 degrees (double)
        """
    def get_number_of_beams(self) -> int:
        """
        < in Datagram
        """
    def get_number_of_valid_detections(self) -> int:
        ...
    def get_ping_counter(self) -> int:
        """
        < 0-65535 ping number (in this file)
        """
    def get_sampling_frequency(self) -> float:
        """
        < in Hz
        """
    def get_scanning_info(self) -> int:
        """
        < only used by em2040. 0 means scanning is not used.
        """
    def get_sound_speed(self) -> int:
        """
        < at transducer in dm/s
        """
    def get_sound_speed_in_m_per_s(self) -> float:
        """
        Get the sound speed in meters per seconds
        
        Returns:
            sound_speed * 0.1 meters per seconds (double)
        """
    def get_spare_byte(self) -> int:
        ...
    def get_spare_bytes(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]:
        ...
    def get_system_serial_number(self) -> int:
        """
        < 100 -
        """
    def get_transmit_transducer_depth(self) -> float:
        """
        < in meter relative water level at time of ping
        """
    @typing.overload
    def get_xyz(self) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1:
        """
        Convert the XYZDatagramBeams to a XYZ structure
        
        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>
        """
    @typing.overload
    def get_xyz(self, beam_numbers: list[int]) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1:
        """
        Convert the XYZDatagramBeams for a given beam_number vector to a XYZ
        structure Note: if a beam number is not found, the corresponding XYZ
        value will be NaN
        
        Parameter ``beam_numbers``:
            $Returns:
        
        algorithms::geoprocessing::datastructures::XYZ<1>
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_beams(self, arg0: list[substructures.XYZDatagramBeam]) -> None:
        """
        < beam detection information
        """
    def set_checksum(self, arg0: int) -> None:
        ...
    def set_etx(self, arg0: int) -> None:
        """
        < end identifier (always 0x03)
        """
    def set_heading(self, arg0: int) -> None:
        """
        < (at TX time) in 0.01 degree
        """
    def set_number_of_beams(self, arg0: int) -> None:
        """
        < in Datagram
        """
    def set_number_of_valid_detections(self, arg0: int) -> None:
        ...
    def set_ping_counter(self, arg0: int) -> None:
        """
        < 0-65535 ping number (in this file)
        """
    def set_sampling_frequency(self, arg0: float) -> None:
        """
        < in Hz
        """
    def set_scanning_info(self, arg0: int) -> None:
        """
        < only used by em2040. 0 means scanning is not used.
        """
    def set_sound_speed(self, arg0: int) -> None:
        """
        < at transducer in dm/s
        """
    def set_spare_byte(self, arg0: int) -> None:
        ...
    def set_spare_bytes(self, arg0: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        ...
    def set_system_serial_number(self, arg0: int) -> None:
        """
        < 100 -
        """
    def set_transmit_transducer_depth(self, arg0: float) -> None:
        """
        < in meter relative water level at time of ping
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
Bscorr: ExtraParameters_t_ContentIdentifier  # value = <ExtraParameters_t_ContentIdentifier.Bscorr: 6>
CalibTxt: ExtraParameters_t_ContentIdentifier  # value = <ExtraParameters_t_ContentIdentifier.CalibTxt: 1>
LogAllHeights: ExtraParameters_t_ContentIdentifier  # value = <ExtraParameters_t_ContentIdentifier.LogAllHeights: 2>
MultiCastInputStatus: ExtraParameters_t_ContentIdentifier  # value = <ExtraParameters_t_ContentIdentifier.MultiCastInputStatus: 5>
SoundVelocityAtTransducer: ExtraParameters_t_ContentIdentifier  # value = <ExtraParameters_t_ContentIdentifier.SoundVelocityAtTransducer: 3>
SoundVelocityProfile: ExtraParameters_t_ContentIdentifier  # value = <ExtraParameters_t_ContentIdentifier.SoundVelocityProfile: 4>
