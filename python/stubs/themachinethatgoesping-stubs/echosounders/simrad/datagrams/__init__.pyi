"""Simrad EK60 and EK80 datagram classes"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad.datagrams
import typing
import themachinethatgoesping.navigation.nmea_0183

__all__ = [
    "FIL1",
    "MRU0",
    "NME0",
    "RAW3",
    "RAW3_datatypes",
    "SimradDatagram",
    "SimradUnknown",
    "TAG0",
    "XML0",
    "XML0_datagrams"
]


class SimradDatagram():
    def __copy__(self) -> SimradDatagram: ...
    def __deepcopy__(self, arg0: dict) -> SimradDatagram: ...
    def __eq__(self, other: SimradDatagram) -> bool: ...
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
    def copy(self) -> SimradDatagram: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SimradDatagram: 
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
    def datagram_type(self) -> themachinethatgoesping.echosounders.simrad.t_SimradDatagramType:
        """
        Ek60 datagram type (XML0, FIL1, NME0, MRU0, RAW3, ...)

        :type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType
        """
    @datagram_type.setter
    def datagram_type(self, arg1: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType) -> None:
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
class MRU0(SimradDatagram):
    """
    Motion binary datagram (MRU0) This datagram contains heave, roll,
    pitch and heading as float values. Conveniently, these values can be
    used directly in themachinethatgoesping navigation processing because
    they are defined in the default coordinate system / value range.
    """
    def __copy__(self) -> MRU0: ...
    def __deepcopy__(self, arg0: dict) -> MRU0: ...
    def __eq__(self, other: MRU0) -> bool: ...
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
    def copy(self) -> MRU0: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> MRU0: 
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
class NME0(SimradDatagram):
    """
    NMEA text datagram (NME0) This datagram contains NMEA sentences
    received by the EK60/EK80 transceiver.
    """
    def __copy__(self) -> NME0: ...
    def __deepcopy__(self, arg0: dict) -> NME0: ...
    def __eq__(self, other: NME0) -> bool: ...
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
    def copy(self) -> NME0: 
        """
        return a copy using the c++ default copy constructor
        """
    def decode(self) -> typing.Union[themachinethatgoesping.navigation.nmea_0183.NMEA_Unknown, themachinethatgoesping.navigation.nmea_0183.NMEA_ZDA, themachinethatgoesping.navigation.nmea_0183.NMEA_VLW, themachinethatgoesping.navigation.nmea_0183.NMEA_VTG, themachinethatgoesping.navigation.nmea_0183.NMEA_VHW, themachinethatgoesping.navigation.nmea_0183.NMEA_RMC, themachinethatgoesping.navigation.nmea_0183.NMEA_HDT, themachinethatgoesping.navigation.nmea_0183.NMEA_GLL, themachinethatgoesping.navigation.nmea_0183.NMEA_GGA, themachinethatgoesping.navigation.nmea_0183.NMEA_GST]: ...
    def field(self, arg0: int) -> str: ...
    def field_double(self, arg0: int) -> float: ...
    def field_int(self, arg0: int) -> int: ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NME0: 
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
class RAW3(SimradDatagram):
    """
    Sample binary datagram (RAW3) This datagram contains the sample data
    for each ping. The exact datatype and size depends on the Datatype
    field!
    """
    def __copy__(self) -> RAW3: ...
    def __deepcopy__(self, arg0: dict) -> RAW3: ...
    def __eq__(self, other: RAW3) -> bool: ...
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
    def copy(self) -> RAW3: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RAW3: 
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
    def _raw_ChannelID(self) -> typing.List[str[128]]:
        """
        < Channel identification (size is always 128)

        :type: typing.List[str[128]]
        """
    @_raw_ChannelID.setter
    def _raw_ChannelID(self, arg0: typing.List[str[128]]) -> None:
        """
        < Channel identification (size is always 128)
        """
    @property
    def _raw_Count(self) -> int:
        """
        < Number of samples in the datagram

        :type: int
        """
    @_raw_Count.setter
    def _raw_Count(self, arg0: int) -> None:
        """
        < Number of samples in the datagram
        """
    @property
    def _raw_Datatype(self) -> RAW3_datatypes.t_RAW3_DataType:
        """
        < Datatype

        :type: RAW3_datatypes.t_RAW3_DataType
        """
    @_raw_Datatype.setter
    def _raw_Datatype(self, arg0: RAW3_datatypes.t_RAW3_DataType) -> None:
        """
        < Datatype
        """
    @property
    def _raw_NumberOfComplexSamples(self) -> int:
        """
        < Number of transducer samples per sample (used when < Datatype is
        complex)

        :type: int
        """
    @_raw_NumberOfComplexSamples.setter
    def _raw_NumberOfComplexSamples(self, arg0: int) -> None:
        """
        < Number of transducer samples per sample (used when < Datatype is
        complex)
        """
    @property
    def _raw_Offset(self) -> int:
        """
        < First sample number in the datagram

        :type: int
        """
    @_raw_Offset.setter
    def _raw_Offset(self, arg0: int) -> None:
        """
        < First sample number in the datagram
        """
    @property
    def _raw_Spare_1(self) -> str:
        """
        < Spare 1

        :type: str
        """
    @_raw_Spare_1.setter
    def _raw_Spare_1(self, arg0: str) -> None:
        """
        < Spare 1
        """
    @property
    def _raw_Spare_2(self) -> str:
        """
        < Spare 2

        :type: str
        """
    @_raw_Spare_2.setter
    def _raw_Spare_2(self, arg0: str) -> None:
        """
        < Spare 2
        """
    @property
    def channel_id(self) -> str:
        """
        < Channel identification (size is always 128)

        :type: str
        """
    @channel_id.setter
    def channel_id(self, arg1: str) -> None:
        """
        < Channel identification (size is always 128)
        """
    @property
    def count(self) -> int:
        """
        < Number of samples in the datagram

        :type: int
        """
    @count.setter
    def count(self, arg1: int) -> None:
        """
        < Number of samples in the datagram
        """
    @property
    def data_type(self) -> RAW3_datatypes.t_RAW3_DataType:
        """
        :type: RAW3_datatypes.t_RAW3_DataType
        """
    @data_type.setter
    def data_type(self, arg1: RAW3_datatypes.t_RAW3_DataType) -> None:
        pass
    @property
    def number_of_complex_samples(self) -> int:
        """
        Get the number of complex samples. This corresponds to the number of
        transducer elements. This field is only valid for complex data types.

        Returns:
            simrad_short

        :type: int
        """
    @number_of_complex_samples.setter
    def number_of_complex_samples(self, arg1: int) -> None:
        """
        Get the number of complex samples. This corresponds to the number of
        transducer elements. This field is only valid for complex data types.

        Returns:
            simrad_short
        """
    @property
    def offset(self) -> int:
        """
        < First sample number in the datagram

        :type: int
        """
    @offset.setter
    def offset(self, arg1: int) -> None:
        """
        < First sample number in the datagram
        """
    @property
    def sample_data(self) -> typing.Union[RAW3_datatypes.RAW3_DataSkipped, RAW3_datatypes.RAW3_DataComplexFloat32, RAW3_datatypes.RAW3_DataPowerAndAngle, RAW3_datatypes.RAW3_DataPower, RAW3_datatypes.RAW3_DataAngle]:
        """
        Get the sample data. The sample data is stored in a variant of xtensor
        containers. The exact type depends on the data type.

        Returns:
            RAW3_datatypes::RAW3_DataVariant

        :type: typing.Union[RAW3_datatypes.RAW3_DataSkipped, RAW3_datatypes.RAW3_DataComplexFloat32, RAW3_datatypes.RAW3_DataPowerAndAngle, RAW3_datatypes.RAW3_DataPower, RAW3_datatypes.RAW3_DataAngle]
        """
    @sample_data.setter
    def sample_data(self, arg1: typing.Union[RAW3_datatypes.RAW3_DataSkipped, RAW3_datatypes.RAW3_DataComplexFloat32, RAW3_datatypes.RAW3_DataPowerAndAngle, RAW3_datatypes.RAW3_DataPower, RAW3_datatypes.RAW3_DataAngle]) -> None:
        """
        Get the sample data. The sample data is stored in a variant of xtensor
        containers. The exact type depends on the data type.

        Returns:
            RAW3_datatypes::RAW3_DataVariant
        """
    __hash__ = None
    pass
class FIL1(SimradDatagram):
    """
    Filter binary datagram (FIL1) This datagram contains filter
    coefficients used by the EK80 to filter the received signal.
    """
    def __copy__(self) -> FIL1: ...
    def __deepcopy__(self, arg0: dict) -> FIL1: ...
    def __eq__(self, other: FIL1) -> bool: ...
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
    def copy(self) -> FIL1: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FIL1: 
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
    def _raw_ChannelID(self) -> str:
        """
        < Channel identification (size is always 128)

        :type: str
        """
    @_raw_ChannelID.setter
    def _raw_ChannelID(self, arg0: str) -> None:
        """
        < Channel identification (size is always 128)
        """
    @property
    def _raw_Coefficients(self) -> numpy.ndarray[numpy.float32]:
        """
        < Filter coefficients, ...)

        :type: numpy.ndarray[numpy.float32]
        """
    @_raw_Coefficients.setter
    def _raw_Coefficients(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < Filter coefficients, ...)
        """
    @property
    def _raw_DecimationFactor(self) -> int:
        """
        < Filter decimation factor

        :type: int
        """
    @_raw_DecimationFactor.setter
    def _raw_DecimationFactor(self, arg0: int) -> None:
        """
        < Filter decimation factor
        """
    @property
    def _raw_NoOfCoefficients(self) -> int:
        """
        < Number of complex filter coefficients

        :type: int
        """
    @_raw_NoOfCoefficients.setter
    def _raw_NoOfCoefficients(self, arg0: int) -> None:
        """
        < Number of complex filter coefficients
        """
    @property
    def _raw_Spare_1(self) -> str:
        """
        < For future expansions

        :type: str
        """
    @_raw_Spare_1.setter
    def _raw_Spare_1(self, arg0: str) -> None:
        """
        < For future expansions
        """
    @property
    def _raw_Spare_2(self) -> str:
        """
        < For future expansions

        :type: str
        """
    @_raw_Spare_2.setter
    def _raw_Spare_2(self, arg0: str) -> None:
        """
        < For future expansions
        """
    @property
    def _raw_Stage(self) -> int:
        """
        < Filter stage number

        :type: int
        """
    @_raw_Stage.setter
    def _raw_Stage(self, arg0: int) -> None:
        """
        < Filter stage number
        """
    @property
    def channel_id(self) -> str:
        """
        < Channel identification (size is always 128)

        :type: str
        """
    @channel_id.setter
    def channel_id(self, arg1: str) -> None:
        """
        < Channel identification (size is always 128)
        """
    @property
    def coefficients(self) -> numpy.ndarray[numpy.float32]:
        """
        < Filter coefficients, ...)

        :type: numpy.ndarray[numpy.float32]
        """
    @coefficients.setter
    def coefficients(self, arg1: numpy.ndarray[numpy.float32]) -> None:
        """
        < Filter coefficients, ...)
        """
    @property
    def decimation_factor(self) -> int:
        """
        < Filter decimation factor

        :type: int
        """
    @decimation_factor.setter
    def decimation_factor(self, arg1: int) -> None:
        """
        < Filter decimation factor
        """
    @property
    def no_of_coefficients(self) -> int:
        """
        < Number of complex filter coefficients

        :type: int
        """
    @no_of_coefficients.setter
    def no_of_coefficients(self, arg1: int) -> None:
        """
        < Number of complex filter coefficients
        """
    @property
    def stage(self) -> int:
        """
        < Filter stage number

        :type: int
        """
    @stage.setter
    def stage(self, arg1: int) -> None:
        """
        < Filter stage number
        """
    __hash__ = None
    pass
class SimradUnknown(SimradDatagram):
    def __copy__(self) -> SimradUnknown: ...
    def __deepcopy__(self, arg0: dict) -> SimradUnknown: ...
    def __eq__(self, other: SimradUnknown) -> bool: ...
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
    def copy(self) -> SimradUnknown: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SimradUnknown: 
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
class TAG0(SimradDatagram):
    """
    Motion binary datagram (TAG0) This datagram contains heave, roll,
    pitch and heading as float values. Conveniently, these values can be
    used directly in themachinethatgoesping navigation processing because
    they are defined in the default coordinate system / value range.
    """
    def __copy__(self) -> TAG0: ...
    def __deepcopy__(self, arg0: dict) -> TAG0: ...
    def __eq__(self, other: TAG0) -> bool: ...
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
    def copy(self) -> TAG0: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> TAG0: 
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
class XML0(SimradDatagram):
    """
    Motion binary datagram (XML0) This datagram contains heave, roll,
    pitch and heading as float values. Conveniently, these values can be
    used directly in themachinethatgoesping navigation processing because
    they are defined in the default coordinate system / value range.
    """
    def __copy__(self) -> XML0: ...
    def __deepcopy__(self, arg0: dict) -> XML0: ...
    def __eq__(self, other: XML0) -> bool: ...
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
    def copy(self) -> XML0: 
        """
        return a copy using the c++ default copy constructor
        """
    def decode(self) -> typing.Union[XML0_datagrams.XML_Node, XML0_datagrams.XML_Parameter, XML0_datagrams.XML_InitialParameter, XML0_datagrams.XML_PingSequence, XML0_datagrams.XML_Environment, XML0_datagrams.XML_Sensor, XML0_datagrams.XML_Configuration]: ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML0: 
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
