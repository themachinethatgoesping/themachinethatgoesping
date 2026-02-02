"""SimradRaw EK60 and EK80 datagram classes"""

from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

from . import (
    XML0_datagrams as XML0_datagrams,
    raw3datatypes as raw3datatypes
)
import themachinethatgoesping.echosounders_nanopy.simradraw
import themachinethatgoesping.navigation_nanopy.nmea_0183


class SimradRawDatagram:
    def __init__(self) -> None: ...

    def get_length(self) -> int:
        """Raw: Length of the datagram in bytes"""

    def set_length(self, arg: int, /) -> None:
        """Raw: Length of the datagram in bytes"""

    def get_datagram_type(self) -> int:
        """Raw: Datagram type as"""

    def set_datagram_type(self, arg: int, /) -> None:
        """Raw: Datagram type as"""

    def get_low_date_time(self) -> int:
        """Raw: Low part of Windows NT FILETIME (100ns ticks since 1601-01-01)"""

    def set_low_date_time(self, arg: int, /) -> None:
        """Raw: Low part of Windows NT FILETIME (100ns ticks since 1601-01-01)"""

    def get_high_date_time(self) -> int:
        """Raw: High part of Windows NT FILETIME (100ns ticks since 1601-01-01)"""

    def set_high_date_time(self, arg: int, /) -> None:
        """Raw: High part of Windows NT FILETIME (100ns ticks since 1601-01-01)"""

    def get_timestamp(self) -> float:
        """
        unix timestamp in seconds since epoch (1970-01-01). Data is converted
        to/from internal windows high/low timestamp representation.
        """

    def set_timestamp(self, arg: float, /) -> None: ...

    def get_datagram_identifier(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier:
        """Ek60 datagram type (XML0, FIL1, NME0, MRU0, RAW3, ...)"""

    def set_datagram_identifier(self, arg: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, /) -> None: ...

    def get_date_string(self, arg0: int, arg1: str, /) -> str: ...

    def get_datetime(self, timezone_offset_hours: float = 0.0) -> object:
        """Return the timestamp as datetime object"""

    def set_datetime(self, datetime: object) -> None:
        """Set the timestamp using a datetime object"""

    def __eq__(self, other: SimradRawDatagram) -> bool: ...

    def copy(self) -> SimradRawDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SimradRawDatagram:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawUnknown(SimradRawDatagram):
    def __init__(self) -> None: ...

    def get_raw_content(self) -> str:
        """raw content of the datagram as byte string;"""

    def set_raw_content(self, raw_content: str) -> None:
        """raw content of the datagram as byte string;"""

    def __eq__(self, other: SimradRawUnknown) -> bool: ...

    def copy(self) -> SimradRawUnknown:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawUnknown: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawUnknown: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SimradRawUnknown:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class NME0(SimradRawDatagram):
    """
    NMEA text datagram (NME0) This datagram contains NMEA sentences
    received by the EK60/EK80 transceiver.
    """

    def __init__(self) -> None: ...

    def get_nmea_base(self) -> themachinethatgoesping.navigation_nanopy.nmea_0183.NMEA_Base:
        """Raw NMEA sentence"""

    def set_nmea_base(self, arg: themachinethatgoesping.navigation_nanopy.nmea_0183.NMEA_Base, /) -> None:
        """Raw NMEA sentence"""

    def get_sentence(self) -> str: ...

    def get_sender_id(self) -> str: ...

    def get_sentence_type(self) -> str: ...

    def get_sentence_id(self) -> str: ...

    def get_field(self, arg: int, /) -> str: ...

    def get_field_as_floattype(self, arg: int, /) -> float: ...

    def get_field_as_int(self, arg: int, /) -> int: ...

    def parse_fields(self) -> None: ...

    def decode(self) -> themachinethatgoesping.navigation_nanopy.nmea_0183.NMEA_Unknown | themachinethatgoesping.navigation_nanopy.nmea_0183.NMEA_ZDA | themachinethatgoesping.navigation_nanopy.nmea_0183.NMEA_VLW | themachinethatgoesping.navigation_nanopy.nmea_0183.NMEA_VTG | themachinethatgoesping.navigation_nanopy.nmea_0183.NMEA_VHW | themachinethatgoesping.navigation_nanopy.nmea_0183.NMEA_RMC | themachinethatgoesping.navigation_nanopy.nmea_0183.NMEA_HDT | themachinethatgoesping.navigation_nanopy.nmea_0183.NMEA_GLL | themachinethatgoesping.navigation_nanopy.nmea_0183.NMEA_GGA | themachinethatgoesping.navigation_nanopy.nmea_0183.NMEA_GST: ...

    def __eq__(self, other: NME0) -> bool: ...

    def copy(self) -> NME0:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NME0: ...

    def __deepcopy__(self, arg: dict, /) -> NME0: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NME0:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class MRU0(SimradRawDatagram):
    """
    Motion binary datagram (MRU0) This datagram contains heave, roll,
    pitch and heading as float values. Conveniently, these values can be
    used directly in themachinethatgoesping navigation processing because
    they are defined in the default coordinate system / value range.
    """

    def __init__(self) -> None: ...

    def get_heave(self) -> float:
        """Heave in m, positive up"""

    def set_heave(self, arg: float, /) -> None:
        """Heave in m, positive up"""

    def get_roll(self) -> float:
        """Roll in degrees, positive port up"""

    def set_roll(self, arg: float, /) -> None:
        """Roll in degrees, positive port up"""

    def get_pitch(self) -> float:
        """Pitch in degrees, positive nose up"""

    def set_pitch(self, arg: float, /) -> None:
        """Pitch in degrees, positive nose up"""

    def get_heading(self) -> float:
        """Heading in degrees, 0° north, 90° east"""

    def set_heading(self, arg: float, /) -> None:
        """Heading in degrees, 0° north, 90° east"""

    def __eq__(self, other: MRU0) -> bool: ...

    def copy(self) -> MRU0:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MRU0: ...

    def __deepcopy__(self, arg: dict, /) -> MRU0: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> MRU0:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class XML0(SimradRawDatagram):
    """
    Motion binary datagram (XML0) This datagram contains heave, roll,
    pitch and heading as float values. Conveniently, these values can be
    used directly in themachinethatgoesping navigation processing because
    they are defined in the default coordinate system / value range.
    """

    def __init__(self) -> None: ...

    def set_xml_content(self, xml_content: str) -> None: ...

    def get_xml_content(self) -> str: ...

    @overload
    def get_xml_datagram_type(self) -> str: ...

    @overload
    def get_xml_datagram_type(self) -> str: ...

    def raw(self) -> XML0_datagrams.XML_Node: ...

    def decode(self) -> XML0_datagrams.XML_Node | XML0_datagrams.XML_Parameter | XML0_datagrams.XML_InitialParameter | XML0_datagrams.XML_PingSequence | XML0_datagrams.XML_Environment | XML0_datagrams.XML_Sensor | XML0_datagrams.XML_Configuration: ...

    def test_xml(self) -> None: ...

    def get_raw_xml_content(self) -> str: ...

    def set_raw_xml_content(self, arg: str, /) -> None: ...

    def __eq__(self, other: XML0) -> bool: ...

    def copy(self) -> XML0:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML0: ...

    def __deepcopy__(self, arg: dict, /) -> XML0: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML0:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class TAG0(SimradRawDatagram):
    """
    Motion binary datagram (TAG0) This datagram contains heave, roll,
    pitch and heading as float values. Conveniently, these values can be
    used directly in themachinethatgoesping navigation processing because
    they are defined in the default coordinate system / value range.
    """

    def __init__(self) -> None: ...

    def get_text(self) -> str:
        """_text annotation string (e.g. interesting fish shoal in echogram)"""

    def set_text(self, arg: str, /) -> None:
        """_text annotation string (e.g. interesting fish shoal in echogram)"""

    def __eq__(self, other: TAG0) -> bool: ...

    def copy(self) -> TAG0:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> TAG0: ...

    def __deepcopy__(self, arg: dict, /) -> TAG0: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> TAG0:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class FIL1(SimradRawDatagram):
    """
    Filter binary datagram (FIL1) This datagram contains filter
    coefficients used by the EK80 to filter the received signal.
    """

    def __init__(self) -> None: ...

    def get_stage(self) -> int:
        """Filter stage number"""

    def set_stage(self, arg: int, /) -> None:
        """Filter stage number"""

    def get_channel_id(self) -> str:
        """Channel identification (size is always 128)"""

    def get_channel_id_stripped(self) -> str: ...

    def set_channel_id(self, arg: str, /) -> None:
        """Channel identification (size is always 128)"""

    def get_no_of_coefficients(self) -> int:
        """Number of complex filter coefficients"""

    def set_no_of_coefficients(self, arg: int, /) -> None:
        """Number of complex filter coefficients"""

    def get_decimation_factor(self) -> int:
        """Filter decimation factor"""

    def set_decimation_factor(self, arg: int, /) -> None:
        """Filter decimation factor"""

    def get_coefficients(self) -> Annotated[NDArray[numpy.complex64], dict(shape=(None,), order='C')]:
        """Filter coefficients"""

    def set_coefficients(self, arg: Annotated[NDArray[numpy.complex64], dict(shape=(None,), order='C')], /) -> None:
        """Filter coefficients"""

    def __eq__(self, other: FIL1) -> bool: ...

    def copy(self) -> FIL1:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> FIL1: ...

    def __deepcopy__(self, arg: dict, /) -> FIL1: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FIL1:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class RAW3(SimradRawDatagram):
    """
    Sample binary datagram (RAW3) This datagram contains the sample data
    for each ping. The exact datatype and size depends on the data_type
    field!
    """

    def __init__(self) -> None: ...

    def get_channel_id(self) -> str:
        """Channel identification (size is always 128)"""

    def set_channel_id(self, arg: str, /) -> None:
        """Channel identification (size is always 128)"""

    def get_data_type(self) -> raw3datatypes.t_RAW3DataType:
        """data_type"""

    def set_data_type(self, arg: raw3datatypes.t_RAW3DataType, /) -> None:
        """data_type"""

    def get_number_of_complex_samples(self) -> int:
        """data_type"""

    def set_number_of_complex_samples(self, arg: int, /) -> None:
        """
        Number of transducer samples per sample (used when data_type is
        complex)
        """

    def get_offset(self) -> int:
        """First sample number in the datagram"""

    def set_offset(self, arg: int, /) -> None:
        """First sample number in the datagram"""

    def get_count(self) -> int:
        """Number of samples in the datagram"""

    def set_count(self, arg: int, /) -> None:
        """Number of samples in the datagram"""

    def get_spare1(self) -> str:
        """Spare 1"""

    def set_spare1(self, arg: str, /) -> None:
        """Spare 1"""

    def get_spare_2(self) -> str:
        """Spare 2"""

    def set_spare_2(self, arg: str, /) -> None:
        """Spare 2"""

    def sample_data(self) -> raw3datatypes.RAW3DataSkipped | raw3datatypes.RAW3DataComplexFloat32 | raw3datatypes.RAW3DataPowerAndAngle | raw3datatypes.RAW3DataPower | raw3datatypes.RAW3DataAngle:
        """Sample data"""

    def get_sample_data(self) -> raw3datatypes.RAW3DataSkipped | raw3datatypes.RAW3DataComplexFloat32 | raw3datatypes.RAW3DataPowerAndAngle | raw3datatypes.RAW3DataPower | raw3datatypes.RAW3DataAngle:
        """Sample data"""

    def set_sample_data(self, arg: raw3datatypes.RAW3DataSkipped | raw3datatypes.RAW3DataComplexFloat32 | raw3datatypes.RAW3DataPowerAndAngle | raw3datatypes.RAW3DataPower | raw3datatypes.RAW3DataAngle, /) -> None:
        """Sample data"""

    def get_channel_id_stripped(self) -> str: ...

    def __eq__(self, other: RAW3) -> bool: ...

    def copy(self) -> RAW3:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RAW3: ...

    def __deepcopy__(self, arg: dict, /) -> RAW3: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RAW3:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
