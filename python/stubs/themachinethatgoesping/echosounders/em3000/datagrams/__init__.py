"""Kongsberg EM3000 (.all/.wcd) EK80 datagram classes"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000.datagrams
import typing
import numpy
import themachinethatgoesping.echosounders.em3000
_Shape = typing.Tuple[int, ...]

__all__ = [
    "AttitudeDatagram",
    "EM3000Datagram",
    "EM3000Unknown",
    "ExtraDetections",
    "NetworkAttitudeVelocityDatagram",
    "QualityFactorDatagram",
    "RawRangeAndAngle",
    "SeabedImageData",
    "WaterColumnDatagram",
    "XYZDatagram",
    "substructures"
]


class EM3000Datagram():
    def __copy__(self) -> EM3000Datagram: ...
    def __deepcopy__(self, arg0: dict) -> EM3000Datagram: ...
    def __eq__(self, other: EM3000Datagram) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> EM3000Datagram: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> EM3000Datagram: 
        """
        create T_CLASS object from bytearray
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
    def get_date_string(self, fractional_seconds_digits: int = 2, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str: ...
    def get_model_number(self) -> int: 
        """
        < EM3000 model number (example: EM 3002 = 3002)
        """
    def get_stx(self) -> int: 
        """
        < (start identifier)
        """
    def get_time_since_midnight(self) -> int: ...
    def get_timestamp(self) -> float: 
        """
        convert the date and time_since_midnight field to a unix timestamp

        Returns:
            unixtime as double
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
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
    def set_time_since_midnight(self, arg0: int) -> None: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
class AttitudeDatagram(EM3000Datagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
    122, EM 302 and ME70BO. All receiver beams are included, check
    detection info and real time cleaning for beam status (note 4 and 5).
    """
    def __copy__(self) -> AttitudeDatagram: ...
    def __deepcopy__(self, arg0: dict) -> AttitudeDatagram: ...
    def __eq__(self, other: AttitudeDatagram) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def attitudes(self) -> typing.List[substructures.AttitudeDatagramAttitude]: 
        """
        < N x Attitude data
        """
    def copy(self) -> AttitudeDatagram: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> AttitudeDatagram: 
        """
        create T_CLASS object from bytearray
        """
    def get_attitude_counter(self) -> int: ...
    def get_attitudes(self) -> typing.List[substructures.AttitudeDatagramAttitude]: 
        """
        < N x Attitude data
        """
    def get_checksum(self) -> int: ...
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
    def get_motion_sensor_number(self) -> int: 
        """
        Get the number of motion sensor from the sensor system descriptor
        field. xx00 xxxx – motion sensor number 1 xx01 xxxx – motion sensor
        number 1

        Returns:
            1 or 2
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
    def get_sensor_system_descriptor(self) -> int: ...
    def get_system_serial_number(self) -> int: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_attitude_counter(self, arg0: int) -> None: ...
    def set_attitudes(self, arg0: typing.List[substructures.AttitudeDatagramAttitude]) -> None: 
        """
        < N x Attitude data
        """
    def set_checksum(self, arg0: int) -> None: ...
    def set_etx(self, arg0: int) -> None: 
        """
        < end identifier (always 0x03)
        """
    def set_number_of_entries(self, arg0: int) -> None: 
        """
        < N
        """
    def set_sensor_system_descriptor(self, arg0: int) -> None: ...
    def set_system_serial_number(self, arg0: int) -> None: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
class EM3000Unknown(EM3000Datagram):
    def __copy__(self) -> EM3000Unknown: ...
    def __deepcopy__(self, arg0: dict) -> EM3000Unknown: ...
    def __eq__(self, other: EM3000Unknown) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> EM3000Unknown: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> EM3000Unknown: 
        """
        create T_CLASS object from bytearray
        """
    def get_checksum(self) -> int: ...
    def get_etx(self) -> int: ...
    def get_raw_content(self) -> str: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_checksum(self, arg0: int) -> None: ...
    def set_etx(self, arg0: int) -> None: ...
    def set_raw_content(self, arg0: str) -> None: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
class ExtraDetections(EM3000Datagram):
    """
    This datagram is used for the models EM 2040 and EM 2040C with Slim
    Processing Unit.
    """
    def __copy__(self) -> ExtraDetections: ...
    def __deepcopy__(self, arg0: dict) -> ExtraDetections: ...
    def __eq__(self, other: ExtraDetections) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> ExtraDetections: 
        """
        return a copy using the c++ default copy constructor
        """
    def detection_classes(self) -> typing.List[substructures.ExtraDetectionsDetectionClasses]: ...
    def extra_detections(self) -> typing.List[substructures.ExtraDetectionsExtraDetections]: ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ExtraDetections: 
        """
        create T_CLASS object from bytearray
        """
    def get_checksum(self) -> int: ...
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
    def get_detection_classes(self) -> typing.List[substructures.ExtraDetectionsDetectionClasses]: 
        """
        < substructure 1
        """
    def get_etx(self) -> int: 
        """
        < end identifier (always 0x03)
        """
    def get_extra_detections(self) -> typing.List[substructures.ExtraDetectionsExtraDetections]: 
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def raw_amplitude_samples(self) -> substructures.SampleAmplitudesStructure_int16_t: ...
    def set_checksum(self, arg0: int) -> None: ...
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
    def set_detection_classes(self, arg0: typing.List[substructures.ExtraDetectionsDetectionClasses]) -> None: 
        """
        < substructure 1
        """
    def set_etx(self, arg0: int) -> None: 
        """
        < end identifier (always 0x03)
        """
    def set_extra_detections(self, arg0: typing.List[substructures.ExtraDetectionsExtraDetections]) -> None: 
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
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
class NetworkAttitudeVelocityDatagram(EM3000Datagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
    122, EM 302 and ME70BO. All receiver beams are included, check
    detection info and real time cleaning for beam status (note 4 and 5).
    """
    def __copy__(self) -> NetworkAttitudeVelocityDatagram: ...
    def __deepcopy__(self, arg0: dict) -> NetworkAttitudeVelocityDatagram: ...
    def __eq__(self, other: NetworkAttitudeVelocityDatagram) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def attitudes(self) -> typing.List[substructures.NetworkAttitudeVelocityDatagramAttitude]: 
        """
        < N x Attitude data
        """
    def copy(self) -> NetworkAttitudeVelocityDatagram: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NetworkAttitudeVelocityDatagram: 
        """
        create T_CLASS object from bytearray
        """
    def get_attitude_velocity_sensor_number(self) -> int: 
        """
        Get the number of motion sensor from the sensor system descriptor
        field. xx10 xxxx – attitude velocity sensor 1 (UDP5) xx11 xxxx –
        attitude velocity sensor 2 (UDP6)

        Returns:
            1 or 2
        """
    def get_attitudes(self) -> typing.List[substructures.NetworkAttitudeVelocityDatagramAttitude]: 
        """
        < N x Attitude data
        """
    def get_checksum(self) -> int: ...
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
    def get_network_attitude_counter(self) -> int: ...
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
    def get_sensor_system_descriptor(self) -> int: ...
    def get_spare(self) -> int: ...
    def get_spare_align(self) -> int: ...
    def get_system_serial_number(self) -> int: ...
    def get_velocity_sensor_is_active(self) -> bool: 
        """
        Evaluate if the velocity sensor is active using sensor system
        descriptor field. 0bxxxxxxx1 : velocity is active 0bxxxxxxx1 :
        velocity is inactive

        Returns:
            bool
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_attitudes(self, arg0: typing.List[substructures.NetworkAttitudeVelocityDatagramAttitude]) -> None: 
        """
        < N x Attitude data
        """
    def set_checksum(self, arg0: int) -> None: ...
    def set_etx(self, arg0: int) -> None: 
        """
        < end identifier (always 0x03)
        """
    def set_network_attitude_counter(self, arg0: int) -> None: ...
    def set_number_of_entries(self, arg0: int) -> None: 
        """
        < N
        """
    def set_sensor_system_descriptor(self, arg0: int) -> None: ...
    def set_spare(self, arg0: int) -> None: ...
    def set_spare_align(self, arg0: int) -> None: ...
    def set_system_serial_number(self, arg0: int) -> None: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
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
    def __copy__(self) -> QualityFactorDatagram: ...
    def __deepcopy__(self, arg0: dict) -> QualityFactorDatagram: ...
    def __eq__(self, other: QualityFactorDatagram) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> QualityFactorDatagram: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> QualityFactorDatagram: 
        """
        create T_CLASS object from bytearray
        """
    def get_checksum(self) -> int: ...
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def qf_shape(self) -> typing.List[int[2]]: 
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
    def set_checksum(self, arg0: int) -> None: ...
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
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
class RawRangeAndAngle(EM3000Datagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
    122, EM 302 and ME70BO. All receiver beams are included, check
    detection info and real time cleaning for beam status (note 4 and 5).
    """
    def __copy__(self) -> RawRangeAndAngle: ...
    def __deepcopy__(self, arg0: dict) -> RawRangeAndAngle: ...
    def __eq__(self, other: RawRangeAndAngle) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def beams(self) -> typing.List[substructures.RawRangeAndAngleBeam]: ...
    def copy(self) -> RawRangeAndAngle: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RawRangeAndAngle: 
        """
        create T_CLASS object from bytearray
        """
    def get_beams(self) -> typing.List[substructures.RawRangeAndAngleBeam]: ...
    def get_checksum(self) -> int: ...
    def get_d_scale(self) -> int: ...
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
    def get_number_of_valid_detections(self) -> int: ...
    def get_ping_counter(self) -> int: 
        """
        < sequential number
        """
    def get_sampling_frequency(self) -> float: ...
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
    def get_system_serial_number(self) -> int: ...
    def get_transmit_sectors(self) -> typing.List[substructures.RawRangeAndAngleTransmitSector]: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_beams(self, arg0: typing.List[substructures.RawRangeAndAngleBeam]) -> None: ...
    def set_checksum(self, arg0: int) -> None: ...
    def set_d_scale(self, arg0: int) -> None: ...
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
    def set_number_of_valid_detections(self, arg0: int) -> None: ...
    def set_ping_counter(self, arg0: int) -> None: 
        """
        < sequential number
        """
    def set_sampling_frequency(self, arg0: float) -> None: ...
    def set_sound_speed_at_transducer(self, arg0: int) -> None: 
        """
        < in 0.1 m/s
        """
    def set_system_serial_number(self, arg0: int) -> None: ...
    def set_transmit_sectors(self, arg0: typing.List[substructures.RawRangeAndAngleTransmitSector]) -> None: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    def transmit_sectors(self) -> typing.List[substructures.RawRangeAndAngleTransmitSector]: ...
    pass
class SeabedImageData(EM3000Datagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
    122, EM 302 and ME70BO. All receiver beams are included, check
    detection info and real time cleaning for beam status (note 4 and 5).
    """
    def __copy__(self) -> SeabedImageData: ...
    def __deepcopy__(self, arg0: dict) -> SeabedImageData: ...
    def __eq__(self, other: SeabedImageData) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def beams(self) -> typing.List[substructures.SeabedImageDataBeam]: ...
    def copy(self) -> SeabedImageData: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SeabedImageData: 
        """
        create T_CLASS object from bytearray
        """
    def get_beams(self) -> typing.List[substructures.SeabedImageDataBeam]: ...
    def get_checksum(self) -> int: ...
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
    def get_number_of_valid_beams(self) -> int: ...
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
    def get_spare_byte(self) -> int: ...
    def get_system_serial_number(self) -> int: ...
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def sample_amplitudes(self) -> substructures.SampleAmplitudesStructure_int16_t: 
        """
        < in 0.1 dB (size = sum of _Number_of_samples of all Beams
        """
    def set_beams(self, arg0: typing.List[substructures.SeabedImageDataBeam]) -> None: ...
    def set_checksum(self, arg0: int) -> None: ...
    def set_etx(self, arg0: int) -> None: 
        """
        < end identifier (always 0x03)
        """
    def set_normal_incidence_backscatter(self, arg0: int) -> None: 
        """
        < in 0.01 dB (BSN)
        """
    def set_number_of_valid_beams(self, arg0: int) -> None: ...
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
    def set_spare_byte(self, arg0: int) -> None: ...
    def set_system_serial_number(self, arg0: int) -> None: ...
    def set_tvg_law_crossover_angle(self, arg0: int) -> None: 
        """
        < in 0.1 degree
        """
    def set_tx_beamwidth_along(self, arg0: int) -> None: 
        """
        < in 0.1 degree
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
class WaterColumnDatagram(EM3000Datagram):
    """
    Used for EM 122, EM 302, EM 710, EM 2040, EM 3002. The receiver beams
    are roll stabilized.
    """
    def __copy__(self) -> WaterColumnDatagram: ...
    def __deepcopy__(self, arg0: dict) -> WaterColumnDatagram: ...
    def __eq__(self, other: WaterColumnDatagram) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def beams(self) -> typing.List[substructures.WaterColumnDatagramBeam]: ...
    def copy(self) -> WaterColumnDatagram: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> WaterColumnDatagram: 
        """
        create T_CLASS object from bytearray
        """
    def get_beams(self) -> typing.List[substructures.WaterColumnDatagramBeam]: ...
    def get_checksum(self) -> int: ...
    def get_datagram_number(self) -> int: ...
    def get_etx(self) -> int: 
        """
        < end identifier (always 0x03)
        """
    def get_number_of_beams_in_datagram(self) -> int: 
        """
        < Beam vector of 2 elements
        """
    def get_number_of_datagrams(self) -> int: ...
    def get_number_of_transmit_sectors(self) -> int: 
        """
        < Transmit_sector vector of 2 elements
        """
    def get_ping_counter(self) -> int: ...
    def get_sampling_frequency(self) -> int: ...
    def get_sampling_frequency_in_hz(self) -> float: 
        """
        Get the sampling frequency in Hz

        Returns:
            _sampling_frequency * 0.01 Hz (float)
        """
    def get_scanning_info(self) -> int: ...
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
    def get_spare(self) -> typing.List[int[3]]: ...
    def get_system_serial_number(self) -> int: ...
    def get_total_no_of_receive_beams(self) -> int: ...
    def get_transmit_sectors(self) -> typing.List[substructures.WaterColumnDatagramTransmitSector]: ...
    def get_tvg_function_applied(self) -> int: ...
    def get_tvg_offset_in_db(self) -> int: ...
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_beams(self, arg0: typing.List[substructures.WaterColumnDatagramBeam]) -> None: ...
    def set_checksum(self, arg0: int) -> None: ...
    def set_datagram_number(self, arg0: int) -> None: ...
    def set_etx(self, arg0: int) -> None: 
        """
        < end identifier (always 0x03)
        """
    def set_number_of_beams_in_datagram(self, arg0: int) -> None: 
        """
        < Beam vector of 2 elements
        """
    def set_number_of_datagrams(self, arg0: int) -> None: ...
    def set_number_of_transmit_sectors(self, arg0: int) -> None: 
        """
        < Transmit_sector vector of 2 elements
        """
    def set_ping_counter(self, arg0: int) -> None: ...
    def set_sampling_frequency(self, arg0: int) -> None: ...
    def set_scanning_info(self, arg0: int) -> None: ...
    def set_sound_speed(self, arg0: int) -> None: 
        """
        < in 0.1 m/s
        """
    def set_spare(self, arg0: typing.List[int[3]]) -> None: ...
    def set_system_serial_number(self, arg0: int) -> None: ...
    def set_total_no_of_receive_beams(self, arg0: int) -> None: ...
    def set_transmit_sectors(self, arg0: typing.List[substructures.WaterColumnDatagramTransmitSector]) -> None: ...
    def set_tvg_function_applied(self, arg0: int) -> None: ...
    def set_tvg_offset_in_db(self, arg0: int) -> None: ...
    def set_tx_time_heave(self, arg0: int) -> None: 
        """
        < in cm
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    def transmit_sectors(self) -> typing.List[substructures.WaterColumnDatagramTransmitSector]: ...
    pass
class XYZDatagram(EM3000Datagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
    122, EM 302 and ME70BO. All receiver beams are included, check
    detection info and real time cleaning for beam status (note 4 and 5).
    """
    def __copy__(self) -> XYZDatagram: ...
    def __deepcopy__(self, arg0: dict) -> XYZDatagram: ...
    def __eq__(self, other: XYZDatagram) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def beams(self) -> typing.List[substructures.XYZDatagramBeam]: 
        """
        < beam detection information
        """
    def copy(self) -> XYZDatagram: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XYZDatagram: 
        """
        create T_CLASS object from bytearray
        """
    def get_beams(self) -> typing.List[substructures.XYZDatagramBeam]: 
        """
        < beam detection information
        """
    def get_checksum(self) -> int: ...
    def get_etx(self) -> int: 
        """
        < end identifier (always 0x03)
        """
    def get_heading_of_vessel(self) -> int: 
        """
        < (at TX time) in 0.01 degree
        """
    def get_heading_of_vessel_in_degrees(self) -> float: 
        """
        Get the vessel heading in degrees

        Returns:
            heading_of_vessel * 0.01 degrees (double)
        """
    def get_number_of_beams(self) -> int: 
        """
        < in Datagram
        """
    def get_number_of_valid_detections(self) -> int: ...
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
    def get_system_serial_number(self) -> int: 
        """
        < 100 -
        """
    def get_transmit_transducer_depth(self) -> float: 
        """
        < in meter relative water level at time of ping
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_beams(self, arg0: typing.List[substructures.XYZDatagramBeam]) -> None: 
        """
        < beam detection information
        """
    def set_checksum(self, arg0: int) -> None: ...
    def set_etx(self, arg0: int) -> None: 
        """
        < end identifier (always 0x03)
        """
    def set_heading_of_vessel(self, arg0: int) -> None: 
        """
        < (at TX time) in 0.01 degree
        """
    def set_number_of_beams(self, arg0: int) -> None: 
        """
        < in Datagram
        """
    def set_number_of_valid_detections(self, arg0: int) -> None: ...
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
    def set_system_serial_number(self, arg0: int) -> None: 
        """
        < 100 -
        """
    def set_transmit_transducer_depth(self, arg0: float) -> None: 
        """
        < in meter relative water level at time of ping
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
