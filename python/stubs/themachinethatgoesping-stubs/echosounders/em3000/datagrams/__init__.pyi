"""Kongsberg EM3000 (.all/.wcd) EK80 datagram classes"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000.datagrams
import typing
import themachinethatgoesping.echosounders.em3000

__all__ = [
    "AmplitudeDetect",
    "EM3000Datagram",
    "EM3000Unknown",
    "Estimated",
    "Interpolated",
    "Invalid",
    "InvalidNormalDetection",
    "NoDetection",
    "PhaseDetect",
    "Rejected",
    "XYZBeam",
    "XYZBeam_t_DetectionType",
    "XYZDatagram"
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
class XYZBeam():
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    def __copy__(self) -> XYZBeam: ...
    def __deepcopy__(self, arg0: dict) -> XYZBeam: ...
    def __eq__(self, other: XYZBeam) -> bool: ...
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> XYZBeam: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_acrosstrack_distance(self) -> float: 
        """
        < distance (y) in meter
        """
    def get_alongtrack_distance(self) -> float: 
        """
        < distance (x) in meter
        """
    def get_backscatter(self) -> float: ...
    def get_backscatter_is_compensated(self) -> bool: ...
    def get_beam_incidence_angle_adjustment(self) -> int: 
        """
        < (IBA) in 0.1 degree
        """
    def get_beam_incidence_angle_adjustment_in_degrees(self) -> float: ...
    def get_depth(self) -> float: 
        """
        < (Z) from transmit transducer in meter
        """
    def get_detection_information(self) -> int: 
        """
        < Flag that indicates the type and validity of detection
        """
    def get_detection_type(self) -> XYZBeam_t_DetectionType: ...
    def get_detection_window_length(self) -> int: 
        """
        < in samples
        """
    def get_quality_factor(self) -> int: 
        """
        < 0-254 Scaled standard deviation (sd) of the range detection <
        divided by the detected range (dr) (qf = 250*sd/sr)
        """
    def get_realtime_cleaning_information(self) -> int: 
        """
        < Flag that indicates if the beam was flagged by real < time cleaning
        (negative values indicate that this < beam is flagged out)
        """
    def get_reflectivity(self) -> int: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_acrosstrack_distance(self, arg0: float) -> None: 
        """
        < distance (y) in meter
        """
    def set_alongtrack_distance(self, arg0: float) -> None: 
        """
        < distance (x) in meter
        """
    def set_beam_incidence_angle_adjustment(self, arg0: float) -> None: 
        """
        < (IBA) in 0.1 degree
        """
    def set_depth(self, arg0: float) -> None: 
        """
        < (Z) from transmit transducer in meter
        """
    def set_detection_information(self, arg0: int) -> None: 
        """
        < Flag that indicates the type and validity of detection
        """
    def set_detection_window_length(self, arg0: int) -> None: 
        """
        < in samples
        """
    def set_quality_factor(self, arg0: int) -> None: 
        """
        < 0-254 Scaled standard deviation (sd) of the range detection <
        divided by the detected range (dr) (qf = 250*sd/sr)
        """
    def set_realtime_cleaning_information(self, arg0: int) -> None: 
        """
        < Flag that indicates if the beam was flagged by real < time cleaning
        (negative values indicate that this < beam is flagged out)
        """
    def set_reflectivity(self, arg0: int) -> None: ...
    __hash__ = None
    pass
class XYZBeam_t_DetectionType():
    """
    Members:

      AmplitudeDetect : 

      PhaseDetect : 

      InvalidNormalDetection : < Invalid: Normal detection

      Interpolated : < Invalid: Therefor interpolated or extrapolated

      Estimated : < Invalid: Therefor estimated

      Rejected : < Invalid: Therefor rejected

      NoDetection : < Invalid: No detection data is available for this beam

      Invalid : 
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    @typing.overload
    def __init__(self, str: str) -> None: 
        """
        Construct this enum type from string
        """
    @typing.overload
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    def str(self) -> str: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    AmplitudeDetect: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.AmplitudeDetect: 0>
    Estimated: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.Estimated: 130>
    Interpolated: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.Interpolated: 129>
    Invalid: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.Invalid: 133>
    InvalidNormalDetection: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.InvalidNormalDetection: 128>
    NoDetection: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.NoDetection: 132>
    PhaseDetect: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.PhaseDetect: 1>
    Rejected: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.Rejected: 131>
    __members__: dict # value = {'AmplitudeDetect': <XYZBeam_t_DetectionType.AmplitudeDetect: 0>, 'PhaseDetect': <XYZBeam_t_DetectionType.PhaseDetect: 1>, 'InvalidNormalDetection': <XYZBeam_t_DetectionType.InvalidNormalDetection: 128>, 'Interpolated': <XYZBeam_t_DetectionType.Interpolated: 129>, 'Estimated': <XYZBeam_t_DetectionType.Estimated: 130>, 'Rejected': <XYZBeam_t_DetectionType.Rejected: 131>, 'NoDetection': <XYZBeam_t_DetectionType.NoDetection: 132>, 'Invalid': <XYZBeam_t_DetectionType.Invalid: 133>}
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
    def beams(self) -> typing.List[XYZBeam]: 
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
    def get_beams(self) -> typing.List[XYZBeam]: 
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
    def get_heading_of_vessel_in_degrees(self) -> float: ...
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
    def get_sound_speed_in_meters_per_seconds(self) -> float: ...
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
    def set_beams(self, arg0: typing.List[XYZBeam]) -> None: 
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
AmplitudeDetect: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.AmplitudeDetect: 0>
Estimated: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.Estimated: 130>
Interpolated: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.Interpolated: 129>
Invalid: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.Invalid: 133>
InvalidNormalDetection: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.InvalidNormalDetection: 128>
NoDetection: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.NoDetection: 132>
PhaseDetect: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.PhaseDetect: 1>
Rejected: themachinethatgoesping.echosounders.em3000.datagrams.XYZBeam_t_DetectionType # value = <XYZBeam_t_DetectionType.Rejected: 131>
