"""
SimradRaw EK60 and EK80 datagram classes
"""
from __future__ import annotations
import numpy
import themachinethatgoesping.echosounders_cppy.simradraw
import themachinethatgoesping.navigation.nmea_0183
import typing
from . import XML0_datagrams
from . import raw3datatypes
__all__ = ['FIL1', 'MRU0', 'NME0', 'RAW3', 'SimradRawDatagram', 'SimradRawUnknown', 'TAG0', 'XML0', 'XML0_datagrams', 'raw3datatypes']
class FIL1(SimradRawDatagram):
    """
    Filter binary datagram (FIL1) This datagram contains filter
    coefficients used by the EK80 to filter the received signal.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FIL1:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> FIL1:
        ...
    def __deepcopy__(self, arg0: dict) -> FIL1:
        ...
    def __eq__(self, other: FIL1) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
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
    def copy(self) -> FIL1:
        """
        return a copy using the c++ default copy constructor
        """
    def get_channel_id(self) -> str:
        """
        < Channel identification (size is always 128)
        """
    def get_coefficients(self) -> numpy.ndarray[numpy.float32]:
        """
        < Filter coefficients, ...)
        """
    def get_decimation_factor(self) -> int:
        """
        < Filter decimation factor
        """
    def get_no_of_coefficients(self) -> int:
        """
        < Number of complex filter coefficients
        """
    def get_stage(self) -> int:
        """
        < Filter stage number
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
    def set_channel_id(self, arg0: str) -> None:
        """
        < Channel identification (size is always 128)
        """
    def set_coefficients(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < Filter coefficients, ...)
        """
    def set_decimation_factor(self, arg0: int) -> None:
        """
        < Filter decimation factor
        """
    def set_no_of_coefficients(self, arg0: int) -> None:
        """
        < Number of complex filter coefficients
        """
    def set_stage(self, arg0: int) -> None:
        """
        < Filter stage number
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class MRU0(SimradRawDatagram):
    """
    Motion binary datagram (MRU0) This datagram contains heave, roll,
    pitch and heading as float values. Conveniently, these values can be
    used directly in themachinethatgoesping navigation processing because
    they are defined in the default coordinate system / value range.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> MRU0:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> MRU0:
        ...
    def __deepcopy__(self, arg0: dict) -> MRU0:
        ...
    def __eq__(self, other: MRU0) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
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
    def copy(self) -> MRU0:
        """
        return a copy using the c++ default copy constructor
        """
    def get_heading(self) -> float:
        """
        < Heading in degrees, 0° north, 90° east
        """
    def get_heave(self) -> float:
        """
        < Heave in m, positive up
        """
    def get_pitch(self) -> float:
        """
        < Pitch in degrees, positive nose up
        """
    def get_roll(self) -> float:
        """
        < Roll in degrees, positive port up
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
    def set_heading(self, arg0: float) -> None:
        """
        < Heading in degrees, 0° north, 90° east
        """
    def set_heave(self, arg0: float) -> None:
        """
        < Heave in m, positive up
        """
    def set_pitch(self, arg0: float) -> None:
        """
        < Pitch in degrees, positive nose up
        """
    def set_roll(self, arg0: float) -> None:
        """
        < Roll in degrees, positive port up
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class NME0(SimradRawDatagram):
    """
    NMEA text datagram (NME0) This datagram contains NMEA sentences
    received by the EK60/EK80 transceiver.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NME0:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> NME0:
        ...
    def __deepcopy__(self, arg0: dict) -> NME0:
        ...
    def __eq__(self, other: NME0) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
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
    def copy(self) -> NME0:
        """
        return a copy using the c++ default copy constructor
        """
    def decode(self) -> themachinethatgoesping.navigation.nmea_0183.NMEA_Unknown | themachinethatgoesping.navigation.nmea_0183.NMEA_ZDA | themachinethatgoesping.navigation.nmea_0183.NMEA_VLW | themachinethatgoesping.navigation.nmea_0183.NMEA_VTG | themachinethatgoesping.navigation.nmea_0183.NMEA_VHW | themachinethatgoesping.navigation.nmea_0183.NMEA_RMC | themachinethatgoesping.navigation.nmea_0183.NMEA_HDT | themachinethatgoesping.navigation.nmea_0183.NMEA_GLL | themachinethatgoesping.navigation.nmea_0183.NMEA_GGA | themachinethatgoesping.navigation.nmea_0183.NMEA_GST:
        ...
    def get_field(self, arg0: int) -> str:
        ...
    def get_field_as_floattype(self, arg0: int) -> float:
        ...
    def get_field_as_int(self, arg0: int) -> int:
        ...
    def get_nmea_base(self) -> themachinethatgoesping.navigation.nmea_0183.NMEA_Base:
        """
        < Raw NMEA sentence
        """
    def get_sender_id(self) -> str:
        ...
    def get_sentence(self) -> str:
        ...
    def get_sentence_id(self) -> str:
        ...
    def get_sentence_type(self) -> str:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parse_fields(self) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_nmea_base(self, arg0: themachinethatgoesping.navigation.nmea_0183.NMEA_Base) -> None:
        """
        < Raw NMEA sentence
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class RAW3(SimradRawDatagram):
    """
    Sample binary datagram (RAW3) This datagram contains the sample data
    for each ping. The exact datatype and size depends on the data_type
    field!
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RAW3:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> RAW3:
        ...
    def __deepcopy__(self, arg0: dict) -> RAW3:
        ...
    def __eq__(self, other: RAW3) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
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
    def copy(self) -> RAW3:
        """
        return a copy using the c++ default copy constructor
        """
    def get_channel_id(self) -> str:
        """
        < Channel identification (size is always 128)
        """
    def get_channel_id_stripped(self) -> str:
        ...
    def get_count(self) -> int:
        """
        < Number of samples in the datagram
        """
    def get_data_type(self) -> raw3datatypes.t_RAW3DataType:
        """
        < data_type
        """
    def get_number_of_complex_samples(self) -> int:
        """
        < data_type
        """
    def get_offset(self) -> int:
        """
        < First sample number in the datagram
        """
    def get_sample_data(self) -> raw3datatypes.RAW3DataSkipped | raw3datatypes.RAW3DataComplexFloat32 | raw3datatypes.RAW3DataPowerAndAngle | raw3datatypes.RAW3DataPower | raw3datatypes.RAW3DataAngle:
        """
        < Sample data
        """
    def get_spare1(self) -> str:
        """
        < Spare 1
        """
    def get_spare_2(self) -> str:
        """
        < Spare 2
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
    def sample_data(self) -> raw3datatypes.RAW3DataSkipped | raw3datatypes.RAW3DataComplexFloat32 | raw3datatypes.RAW3DataPowerAndAngle | raw3datatypes.RAW3DataPower | raw3datatypes.RAW3DataAngle:
        """
        < Sample data
        """
    def set_channel_id(self, arg0: str) -> None:
        """
        < Channel identification (size is always 128)
        """
    def set_count(self, arg0: int) -> None:
        """
        < Number of samples in the datagram
        """
    def set_data_type(self, arg0: raw3datatypes.t_RAW3DataType) -> None:
        """
        < data_type
        """
    def set_number_of_complex_samples(self, arg0: int) -> None:
        """
        < Number of transducer samples per sample (used when < data_type is
        complex)
        """
    def set_offset(self, arg0: int) -> None:
        """
        < First sample number in the datagram
        """
    def set_sample_data(self, arg0: raw3datatypes.RAW3DataSkipped | raw3datatypes.RAW3DataComplexFloat32 | raw3datatypes.RAW3DataPowerAndAngle | raw3datatypes.RAW3DataPower | raw3datatypes.RAW3DataAngle) -> None:
        """
        < Sample data
        """
    def set_spare1(self, arg0: str) -> None:
        """
        < Spare 1
        """
    def set_spare_2(self, arg0: str) -> None:
        """
        < Spare 2
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class SimradRawDatagram:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SimradRawDatagram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SimradRawDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagram:
        ...
    def __eq__(self, other: SimradRawDatagram) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
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
    def copy(self) -> SimradRawDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def get_datagram_identifier(self) -> themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier:
        """
        Ek60 datagram type (XML0, FIL1, NME0, MRU0, RAW3, ...)
        """
    def get_datagram_type(self) -> int:
        """
        < Raw: Datagram type as
        """
    def get_date_string(self, arg0: int, arg1: str) -> str:
        ...
    def get_datetime(self, timezone_offset_hours: float = 0.0) -> typing.Any:
        """
        Return the timestamp as datetime object
        """
    def get_high_date_time(self) -> int:
        """
        < Raw: High part of Windows NT FILETIME (100ns ticks since 1601-01-01)
        """
    def get_length(self) -> int:
        """
        < Raw: Length of the datagram in bytes
        """
    def get_low_date_time(self) -> int:
        """
        < Raw: Low part of Windows NT FILETIME (100ns ticks since 1601-01-01)
        """
    def get_timestamp(self) -> float:
        """
        unix timestamp in seconds since epoch (1970-01-01). Data is converted
        to/from internal windows high/low timestamp representation.
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
    def set_datagram_identifier(self, arg0: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> None:
        ...
    def set_datagram_type(self, arg0: int) -> None:
        """
        < Raw: Datagram type as
        """
    def set_datetime(self, datetime: typing.Any) -> None:
        """
        Set the timestamp using a datetime object
        """
    def set_high_date_time(self, arg0: int) -> None:
        """
        < Raw: High part of Windows NT FILETIME (100ns ticks since 1601-01-01)
        """
    def set_length(self, arg0: int) -> None:
        """
        < Raw: Length of the datagram in bytes
        """
    def set_low_date_time(self, arg0: int) -> None:
        """
        < Raw: Low part of Windows NT FILETIME (100ns ticks since 1601-01-01)
        """
    def set_timestamp(self, arg0: float) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class SimradRawUnknown(SimradRawDatagram):
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SimradRawUnknown:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SimradRawUnknown:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawUnknown:
        ...
    def __eq__(self, other: SimradRawUnknown) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
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
    def copy(self) -> SimradRawUnknown:
        """
        return a copy using the c++ default copy constructor
        """
    def get_raw_content(self) -> bytes:
        """
        < raw content of the datagram as byte string;
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
    def set_raw_content(self, arg0: bytes) -> None:
        """
        < raw content of the datagram as byte string;
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class TAG0(SimradRawDatagram):
    """
    Motion binary datagram (TAG0) This datagram contains heave, roll,
    pitch and heading as float values. Conveniently, these values can be
    used directly in themachinethatgoesping navigation processing because
    they are defined in the default coordinate system / value range.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> TAG0:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> TAG0:
        ...
    def __deepcopy__(self, arg0: dict) -> TAG0:
        ...
    def __eq__(self, other: TAG0) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
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
    def copy(self) -> TAG0:
        """
        return a copy using the c++ default copy constructor
        """
    def get_text(self) -> str:
        """
        < _text annotation string (e.g. interesting fish shoal in echogram)
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
    def set_text(self, arg0: str) -> None:
        """
        < _text annotation string (e.g. interesting fish shoal in echogram)
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML0(SimradRawDatagram):
    """
    Motion binary datagram (XML0) This datagram contains heave, roll,
    pitch and heading as float values. Conveniently, these values can be
    used directly in themachinethatgoesping navigation processing because
    they are defined in the default coordinate system / value range.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML0:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML0:
        ...
    def __deepcopy__(self, arg0: dict) -> XML0:
        ...
    def __eq__(self, other: XML0) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
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
    def copy(self) -> XML0:
        """
        return a copy using the c++ default copy constructor
        """
    def decode(self) -> XML0_datagrams.XML_Node | XML0_datagrams.XML_Parameter | XML0_datagrams.XML_InitialParameter | XML0_datagrams.XML_PingSequence | XML0_datagrams.XML_Environment | XML0_datagrams.XML_Sensor | XML0_datagrams.XML_Configuration:
        ...
    def get_raw_xml_content(self) -> str:
        ...
    def get_xml_content(self) -> str:
        ...
    @typing.overload
    def get_xml_datagram_type(self) -> str:
        ...
    @typing.overload
    def get_xml_datagram_type(self) -> str:
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
    def raw(self) -> XML0_datagrams.XML_Node:
        ...
    def set_raw_xml_content(self, arg0: str) -> None:
        ...
    def set_xml_content(self, xml_content: str) -> None:
        ...
    def test_xml(self) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
