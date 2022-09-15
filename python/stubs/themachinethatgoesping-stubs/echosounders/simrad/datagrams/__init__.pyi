"""Simrad EK60 and EK80 datagram classes"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad.datagrams
import typing
import themachinethatgoesping.navigation.nmea_0183

__all__ = [
    "EK60_Datagram",
    "EK60_NME0",
    "EK60_Unknown",
    "EK80_MRU0",
    "EK80_TAG0",
    "EK80_XML0",
    "XML0_datagrams"
]


class EK60_Datagram():
    def __copy__(self) -> EK60_Datagram: ...
    def __deepcopy__(self, arg0: dict) -> EK60_Datagram: ...
    def __eq__(self, other: EK60_Datagram) -> bool: ...
    def __getstate__(self) -> bytes: ...
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
    def copy(self) -> EK60_Datagram: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> EK60_Datagram: 
        """
        create T_CLASS object from bytearray
        """
    def get_date_string(self, fractional_seconds_digits: int = 2, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def _raw_DatagramType(self) -> int:
        """
        < Raw: Datagram type as

        :type: int
        """
    @_raw_DatagramType.setter
    def _raw_DatagramType(self, arg0: int) -> None:
        """
        < Raw: Datagram type as
        """
    @property
    def _raw_HighDateTime(self) -> int:
        """
        < Raw: High part of Windows NT FILETIME (100ns ticks since 1601-01-01)

        :type: int
        """
    @_raw_HighDateTime.setter
    def _raw_HighDateTime(self, arg0: int) -> None:
        """
        < Raw: High part of Windows NT FILETIME (100ns ticks since 1601-01-01)
        """
    @property
    def _raw_Length(self) -> int:
        """
        < Raw: Length of the datagram in bytes

        :type: int
        """
    @_raw_Length.setter
    def _raw_Length(self, arg0: int) -> None:
        """
        < Raw: Length of the datagram in bytes
        """
    @property
    def _raw_LowDateTime(self) -> int:
        """
        < Raw: Low part of Windows NT FILETIME (100ns ticks since 1601-01-01)

        :type: int
        """
    @_raw_LowDateTime.setter
    def _raw_LowDateTime(self, arg0: int) -> None:
        """
        < Raw: Low part of Windows NT FILETIME (100ns ticks since 1601-01-01)
        """
    @property
    def datagram_type(self) -> themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType:
        """
        Ek60 datagram type (XML0, FIL1, NME0, MRU0, RAW3, ...)

        :type: themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType
        """
    @datagram_type.setter
    def datagram_type(self, arg1: themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType) -> None:
        """
        Ek60 datagram type (XML0, FIL1, NME0, MRU0, RAW3, ...)
        """
    @property
    def length(self) -> int:
        """
        length of the datagram in bytes (excluding the length fields at the
        beginning and end of the datagram)

        :type: int
        """
    @length.setter
    def length(self, arg1: int) -> None:
        """
        length of the datagram in bytes (excluding the length fields at the
        beginning and end of the datagram)
        """
    @property
    def timestamp(self) -> float:
        """
        unix timestamp in seconds since epoch (1970-01-01). Data is converted
        to/from internal windows high/low timestamp representation.

        :type: float
        """
    @timestamp.setter
    def timestamp(self, arg1: float) -> None:
        """
        unix timestamp in seconds since epoch (1970-01-01). Data is converted
        to/from internal windows high/low timestamp representation.
        """
    __hash__ = None
    pass
class EK60_NME0(EK60_Datagram):
    """
    NMEA text datagram (NME0) This datagram contains NMEA sentences
    received by the EK60/EK80 transceiver.
    """
    def __copy__(self) -> EK60_NME0: ...
    def __deepcopy__(self, arg0: dict) -> EK60_NME0: ...
    def __eq__(self, other: EK60_NME0) -> bool: ...
    def __getstate__(self) -> bytes: ...
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
    def copy(self) -> EK60_NME0: 
        """
        return a copy using the c++ default copy constructor
        """
    def decode(self) -> typing.Union[themachinethatgoesping.navigation.nmea_0183.NMEA_Unknown, themachinethatgoesping.navigation.nmea_0183.NMEA_ZDA, themachinethatgoesping.navigation.nmea_0183.NMEA_VLW, themachinethatgoesping.navigation.nmea_0183.NMEA_VTG, themachinethatgoesping.navigation.nmea_0183.NMEA_VHW, themachinethatgoesping.navigation.nmea_0183.NMEA_RMC, themachinethatgoesping.navigation.nmea_0183.NMEA_HDT, themachinethatgoesping.navigation.nmea_0183.NMEA_GLL, themachinethatgoesping.navigation.nmea_0183.NMEA_GGA, themachinethatgoesping.navigation.nmea_0183.NMEA_GST]: ...
    def field(self, arg0: int) -> str: ...
    def field_double(self, arg0: int) -> float: ...
    def field_int(self, arg0: int) -> int: ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> EK60_NME0: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parse_fields(self) -> None: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def _raw_sentence(self) -> str:
        """
        :type: str
        """
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def sender(self) -> str:
        """
        :type: str
        """
    @property
    def type(self) -> str:
        """
        :type: str
        """
    __hash__ = None
    pass
class EK60_Unknown(EK60_Datagram):
    def __copy__(self) -> EK60_Unknown: ...
    def __deepcopy__(self, arg0: dict) -> EK60_Unknown: ...
    def __eq__(self, other: EK60_Unknown) -> bool: ...
    def __getstate__(self) -> bytes: ...
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
    def copy(self) -> EK60_Unknown: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> EK60_Unknown: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def raw_content(self) -> bytes:
        """
        :type: bytes
        """
    @raw_content.setter
    def raw_content(self, arg1: bytes) -> None:
        pass
    __hash__ = None
    pass
class EK80_MRU0(EK60_Datagram):
    """
    Motion binary datagram (MRU0) This datagram contains heave, roll,
    pitch and heading as float values. Conveniently, these values can be
    used directly in themachinethatgoesping navigation processing because
    they are defined in the default coordinate system / value range.
    """
    def __copy__(self) -> EK80_MRU0: ...
    def __deepcopy__(self, arg0: dict) -> EK80_MRU0: ...
    def __eq__(self, other: EK80_MRU0) -> bool: ...
    def __getstate__(self) -> bytes: ...
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
    def copy(self) -> EK80_MRU0: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> EK80_MRU0: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def _raw_Heading(self) -> float:
        """
        < Heading in degrees, 0° north, 90° east

        :type: float
        """
    @_raw_Heading.setter
    def _raw_Heading(self, arg0: float) -> None:
        """
        < Heading in degrees, 0° north, 90° east
        """
    @property
    def _raw_Heave(self) -> float:
        """
        < Heave in m, positive up

        :type: float
        """
    @_raw_Heave.setter
    def _raw_Heave(self, arg0: float) -> None:
        """
        < Heave in m, positive up
        """
    @property
    def _raw_Pitch(self) -> float:
        """
        < Pitch in degrees, positive nose up

        :type: float
        """
    @_raw_Pitch.setter
    def _raw_Pitch(self, arg0: float) -> None:
        """
        < Pitch in degrees, positive nose up
        """
    @property
    def _raw_Roll(self) -> float:
        """
        < Roll in degrees, positive port up

        :type: float
        """
    @_raw_Roll.setter
    def _raw_Roll(self, arg0: float) -> None:
        """
        < Roll in degrees, positive port up
        """
    @property
    def heading(self) -> float:
        """
        < Heading in degrees, 0° north, 90° east

        :type: float
        """
    @heading.setter
    def heading(self, arg1: float) -> None:
        """
        < Heading in degrees, 0° north, 90° east
        """
    @property
    def heave(self) -> float:
        """
        < Heave in m, positive up

        :type: float
        """
    @heave.setter
    def heave(self, arg1: float) -> None:
        """
        < Heave in m, positive up
        """
    @property
    def pitch(self) -> float:
        """
        < Pitch in degrees, positive nose up

        :type: float
        """
    @pitch.setter
    def pitch(self, arg1: float) -> None:
        """
        < Pitch in degrees, positive nose up
        """
    @property
    def roll(self) -> float:
        """
        < Roll in degrees, positive port up

        :type: float
        """
    @roll.setter
    def roll(self, arg1: float) -> None:
        """
        < Roll in degrees, positive port up
        """
    __hash__ = None
    pass
class EK80_TAG0(EK60_Datagram):
    """
    Motion binary datagram (TAG0) This datagram contains heave, roll,
    pitch and heading as float values. Conveniently, these values can be
    used directly in themachinethatgoesping navigation processing because
    they are defined in the default coordinate system / value range.
    """
    def __copy__(self) -> EK80_TAG0: ...
    def __deepcopy__(self, arg0: dict) -> EK80_TAG0: ...
    def __eq__(self, other: EK80_TAG0) -> bool: ...
    def __getstate__(self) -> bytes: ...
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
    def copy(self) -> EK80_TAG0: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> EK80_TAG0: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def _raw_Text(self) -> str:
        """
        < _Text annotation string (e.g. interesting fish shoal in echogram)

        :type: str
        """
    @_raw_Text.setter
    def _raw_Text(self, arg0: str) -> None:
        """
        < _Text annotation string (e.g. interesting fish shoal in echogram)
        """
    @property
    def text(self) -> str:
        """
        < _Text annotation string (e.g. interesting fish shoal in echogram)

        :type: str
        """
    @text.setter
    def text(self, arg1: str) -> None:
        """
        < _Text annotation string (e.g. interesting fish shoal in echogram)
        """
    __hash__ = None
    pass
class EK80_XML0(EK60_Datagram):
    """
    Motion binary datagram (XML0) This datagram contains heave, roll,
    pitch and heading as float values. Conveniently, these values can be
    used directly in themachinethatgoesping navigation processing because
    they are defined in the default coordinate system / value range.
    """
    def __copy__(self) -> EK80_XML0: ...
    def __deepcopy__(self, arg0: dict) -> EK80_XML0: ...
    def __eq__(self, other: EK80_XML0) -> bool: ...
    def __getstate__(self) -> bytes: ...
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
    def copy(self) -> EK80_XML0: 
        """
        return a copy using the c++ default copy constructor
        """
    def decode(self) -> typing.Union[XML0_datagrams.XML_Node, XML0_datagrams.XML_Parameter, XML0_datagrams.XML_InitialParameter, XML0_datagrams.XML_PingSequence, XML0_datagrams.XML_Environment, XML0_datagrams.XML_Sensor, XML0_datagrams.XML_Configuration]: ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> EK80_XML0: 
        """
        create T_CLASS object from bytearray
        """
    def get_xml_content(self) -> str: ...
    def get_xml_datagram_type(self) -> str: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def raw(self) -> XML0_datagrams.XML_Node: ...
    def set_xml_content(self, xml_content: str) -> None: ...
    def test_xml(self) -> None: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def _raw_xml_content(self) -> str:
        """
        :type: str
        """
    @_raw_xml_content.setter
    def _raw_xml_content(self, arg1: str) -> None:
        pass
    __hash__ = None
    pass
