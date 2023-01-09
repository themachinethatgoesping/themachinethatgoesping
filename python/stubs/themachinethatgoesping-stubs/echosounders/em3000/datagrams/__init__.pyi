"""Kongsberg EM3000 (.all/.wcd) EK80 datagram classes"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000.datagrams
import typing
import themachinethatgoesping.echosounders.em3000

__all__ = [
    "EM3000Datagram",
    "EM3000Unknown",
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
    @staticmethod
    def beams(*args, **kwargs) -> typing.Any: 
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
    @staticmethod
    def get_beams(*args, **kwargs) -> typing.Any: 
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
    @staticmethod
    def set_beams(*args, **kwargs) -> typing.Any: 
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
