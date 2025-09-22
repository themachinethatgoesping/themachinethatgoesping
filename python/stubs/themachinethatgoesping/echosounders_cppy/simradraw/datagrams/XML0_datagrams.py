"""
SimradRaw EK80 XML datagram classes (subtypes of XML0)
"""
from __future__ import annotations
import collections.abc
import themachinethatgoesping.navigation
import themachinethatgoesping.navigation.datastructures
import typing
__all__: list[str] = ['BeamTypeRef', 'BeamTypeRefB', 'BeamTypeSingle', 'BeamTypeSplit', 'BeamTypeSplit2', 'BeamTypeSplit3', 'BeamTypeSplit3C', 'BeamTypeSplit3CN', 'BeamTypeSplit3CW', 'ChannelConfiguration', 'XMLConfigurationActivePingMode', 'XMLConfigurationTransceiverChannelTransducer', 'XML_Configuration', 'XML_Configuration_Sensor', 'XML_Configuration_Sensor_Telegram', 'XML_Configuration_Sensor_TelegramValue', 'XML_Configuration_Transceiver', 'XML_Configuration_Transceiver_Channel', 'XML_Configuration_Transceiver_Channel_FrequencyPar', 'XML_Configuration_Transducer', 'XML_Environment', 'XML_Environment_Transducer', 'XML_InitialParameter', 'XML_Node', 'XML_Parameter', 'XML_Parameter_Channel', 'XML_PingSequence', 'XML_PingSequence_Ping', 'XML_Sensor', 't_BeamType']
class ChannelConfiguration:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ChannelConfiguration:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> ChannelConfiguration:
        ...
    def __deepcopy__(self, arg0: dict) -> ChannelConfiguration:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, ChannelID: str, Channel: XML_Configuration_Transceiver_Channel, Transceiver: XML_Configuration_Transceiver, Transducer: XML_Configuration_Transducer) -> None:
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
    def copy(self) -> ChannelConfiguration:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def Channel(self) -> XML_Configuration_Transceiver_Channel:
        ...
    @property
    def ChannelID(self) -> str:
        ...
    @property
    def Transceiver(self) -> XML_Configuration_Transceiver:
        ...
    @property
    def Transducer(self) -> XML_Configuration_Transducer:
        ...
    @property
    def sensor_offsets(self) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets:
        ...
class XMLConfigurationActivePingMode:
    """
    XML base datagram
    """
    Mode: str
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XMLConfigurationActivePingMode:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XMLConfigurationActivePingMode:
        ...
    def __deepcopy__(self, arg0: dict) -> XMLConfigurationActivePingMode:
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
    def copy(self) -> XMLConfigurationActivePingMode:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XMLConfigurationTransceiverChannelTransducer:
    """
    XML base datagram
    """
    ArticleNumber: str
    BeamType: t_BeamType
    TransducerName: str
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XMLConfigurationTransceiverChannelTransducer:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XMLConfigurationTransceiverChannelTransducer:
        ...
    def __deepcopy__(self, arg0: dict) -> XMLConfigurationTransceiverChannelTransducer:
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
    def copy(self) -> XMLConfigurationTransceiverChannelTransducer:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def AngleOffsetAlongship(self) -> float:
        ...
    @AngleOffsetAlongship.setter
    def AngleOffsetAlongship(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def AngleOffsetAthwartship(self) -> float:
        ...
    @AngleOffsetAthwartship.setter
    def AngleOffsetAthwartship(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def AngleSensitivityAlongship(self) -> float:
        ...
    @AngleSensitivityAlongship.setter
    def AngleSensitivityAlongship(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def AngleSensitivityAthwartship(self) -> float:
        ...
    @AngleSensitivityAthwartship.setter
    def AngleSensitivityAthwartship(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def BeamWidthAlongship(self) -> float:
        ...
    @BeamWidthAlongship.setter
    def BeamWidthAlongship(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def BeamWidthAthwartship(self) -> float:
        ...
    @BeamWidthAthwartship.setter
    def BeamWidthAthwartship(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def DirectivityDropAt2XBeamWidth(self) -> float:
        ...
    @DirectivityDropAt2XBeamWidth.setter
    def DirectivityDropAt2XBeamWidth(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def EquivalentBeamAngle(self) -> float:
        ...
    @EquivalentBeamAngle.setter
    def EquivalentBeamAngle(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Frequency(self) -> float:
        ...
    @Frequency.setter
    def Frequency(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def FrequencyMaximum(self) -> float:
        ...
    @FrequencyMaximum.setter
    def FrequencyMaximum(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def FrequencyMinimum(self) -> float:
        ...
    @FrequencyMinimum.setter
    def FrequencyMinimum(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def FrequencyPars(self) -> list[XML_Configuration_Transceiver_Channel_FrequencyPar]:
        ...
    @FrequencyPars.setter
    def FrequencyPars(self, arg0: collections.abc.Sequence[XML_Configuration_Transceiver_Channel_FrequencyPar]) -> None:
        ...
    @property
    def Gain(self) -> list[float]:
        ...
    @Gain.setter
    def Gain(self, arg0: collections.abc.Sequence[typing.SupportsFloat]) -> None:
        ...
    @property
    def MaxTxPowerTransducer(self) -> float:
        ...
    @MaxTxPowerTransducer.setter
    def MaxTxPowerTransducer(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def SaCorrection(self) -> list[float]:
        ...
    @SaCorrection.setter
    def SaCorrection(self, arg0: collections.abc.Sequence[typing.SupportsFloat]) -> None:
        ...
    @property
    def SerialNumber(self) -> int:
        ...
    @SerialNumber.setter
    def SerialNumber(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_Configuration:
    """
    XML Configuration datagram structure.
    """
    ActivePingMode: XMLConfigurationActivePingMode
    ApplicationName: str
    Copyright: str
    FileFormatVersion: str
    TimeBias: str
    Version: str
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Configuration:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration:
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
    def copy(self) -> XML_Configuration:
        """
        return a copy using the c++ default copy constructor
        """
    def get_prioritized_sensor(self, prio_values: collections.abc.Sequence[str]) -> XML_Configuration_Sensor:
        ...
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration:
        ...
    def get_sensors_sorted_by_priority(self, prio_values: collections.abc.Sequence[str]) -> list[XML_Configuration_Sensor]:
        ...
    def get_transceiver(self, channel_id: str) -> XML_Configuration_Transceiver:
        ...
    def get_transceiver_channel(self, channel_id: str) -> XML_Configuration_Transceiver_Channel:
        ...
    def get_transceiver_channels(self) -> dict[str, XML_Configuration_Transceiver_Channel]:
        ...
    def get_transceivers(self) -> dict[str, XML_Configuration_Transceiver]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def ChannelConfigurations(self) -> dict[str, ChannelConfiguration]:
        ...
    @ChannelConfigurations.setter
    def ChannelConfigurations(self, arg0: collections.abc.Mapping[str, ChannelConfiguration]) -> None:
        ...
    @property
    def ConfiguredSensors(self) -> list[XML_Configuration_Sensor]:
        ...
    @ConfiguredSensors.setter
    def ConfiguredSensors(self, arg0: collections.abc.Sequence[XML_Configuration_Sensor]) -> None:
        ...
    @property
    def SensorConfigurations(self) -> dict[str, list[XML_Configuration_Sensor]]:
        ...
    @SensorConfigurations.setter
    def SensorConfigurations(self, arg0: collections.abc.Mapping[str, collections.abc.Sequence[XML_Configuration_Sensor]]) -> None:
        ...
    @property
    def Transceivers(self) -> list[XML_Configuration_Transceiver]:
        ...
    @Transceivers.setter
    def Transceivers(self, arg0: collections.abc.Sequence[XML_Configuration_Transceiver]) -> None:
        ...
    @property
    def Transducers(self) -> list[XML_Configuration_Transducer]:
        ...
    @Transducers.setter
    def Transducers(self, arg0: collections.abc.Sequence[XML_Configuration_Transducer]) -> None:
        ...
class XML_Configuration_Sensor:
    """
    XML base datagram
    """
    Name: str
    Port: str
    TalkerID: str
    Type: str
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Sensor:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Configuration_Sensor:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Sensor:
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
    def copy(self) -> XML_Configuration_Sensor:
        """
        return a copy using the c++ default copy constructor
        """
    def get_sensor_offsets(self) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets:
        """
        Return the sensor offsets as
        navigation::datastructures::PositionalOffsets structure
        
        Returns:
            navigation::datastructures::PositionalOffsets
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def AngleX(self) -> float:
        ...
    @AngleX.setter
    def AngleX(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def AngleY(self) -> float:
        ...
    @AngleY.setter
    def AngleY(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def AngleZ(self) -> float:
        ...
    @AngleZ.setter
    def AngleZ(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Telegrams(self) -> list[XML_Configuration_Sensor_Telegram]:
        ...
    @Telegrams.setter
    def Telegrams(self, arg0: collections.abc.Sequence[XML_Configuration_Sensor_Telegram]) -> None:
        ...
    @property
    def Timeout(self) -> float:
        ...
    @Timeout.setter
    def Timeout(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Unique(self) -> int:
        ...
    @Unique.setter
    def Unique(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def X(self) -> float:
        ...
    @X.setter
    def X(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Y(self) -> float:
        ...
    @Y.setter
    def Y(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Z(self) -> float:
        ...
    @Z.setter
    def Z(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_Configuration_Sensor_Telegram:
    """
    XML Configuration Sensor Telegram (single <Telegram> node).
    """
    Enabled: bool
    Name: str
    SubscriptionPath: str
    Type: str
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Sensor_Telegram:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Configuration_Sensor_Telegram:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Sensor_Telegram:
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
    def copy(self) -> XML_Configuration_Sensor_Telegram:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        """
        Returns true if no unknown children/attributes were encountered.
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def Values(self) -> list[XML_Configuration_Sensor_TelegramValue]:
        ...
    @Values.setter
    def Values(self, arg0: collections.abc.Sequence[XML_Configuration_Sensor_TelegramValue]) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_Configuration_Sensor_TelegramValue:
    """
    XML Configuration Sensor Telegram Value (single <Value> node).
    """
    Name: str
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Sensor_TelegramValue:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Configuration_Sensor_TelegramValue:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Sensor_TelegramValue:
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
    def copy(self) -> XML_Configuration_Sensor_TelegramValue:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        """
        Returns true if no unknown children/attributes were encountered.
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def Priority(self) -> int:
        ...
    @Priority.setter
    def Priority(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_Configuration_Transceiver:
    """
    XML base datagram
    """
    EthernetAddress: str
    IPAddress: str
    MarketSegment: str
    TransceiverName: str
    TransceiverSoftwareVersion: str
    TransceiverType: str
    Version: str
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transceiver:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Configuration_Transceiver:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Transceiver:
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
    def copy(self) -> XML_Configuration_Transceiver:
        """
        return a copy using the c++ default copy constructor
        """
    def get_transceiver_channel(self, channel_id: str) -> XML_Configuration_Transceiver_Channel:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def Channels(self) -> list[XML_Configuration_Transceiver_Channel]:
        ...
    @Channels.setter
    def Channels(self, arg0: collections.abc.Sequence[XML_Configuration_Transceiver_Channel]) -> None:
        ...
    @property
    def Impedance(self) -> float:
        ...
    @Impedance.setter
    def Impedance(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Multiplexing(self) -> int:
        ...
    @Multiplexing.setter
    def Multiplexing(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def RxSampleFrequency(self) -> float:
        ...
    @RxSampleFrequency.setter
    def RxSampleFrequency(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def SerialNumber(self) -> int:
        ...
    @SerialNumber.setter
    def SerialNumber(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def TransceiverNumber(self) -> int:
        ...
    @TransceiverNumber.setter
    def TransceiverNumber(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_Configuration_Transceiver_Channel:
    """
    XML base datagram
    """
    ChannelID: str
    ChannelIdShort: str
    LogicalChannelID: str
    Transducer: XMLConfigurationTransceiverChannelTransducer
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transceiver_Channel:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Configuration_Transceiver_Channel:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Transceiver_Channel:
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
    def copy(self) -> XML_Configuration_Transceiver_Channel:
        """
        return a copy using the c++ default copy constructor
        """
    def get_pulse_durations(self, fm: bool) -> list[float]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def ChannelNumber(self) -> int:
        ...
    @ChannelNumber.setter
    def ChannelNumber(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def HWChannelConfiguration(self) -> int:
        ...
    @HWChannelConfiguration.setter
    def HWChannelConfiguration(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def MaxTxPowerTransceiver(self) -> float:
        ...
    @MaxTxPowerTransceiver.setter
    def MaxTxPowerTransceiver(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def PulseDuration(self) -> list[float]:
        ...
    @PulseDuration.setter
    def PulseDuration(self, arg0: collections.abc.Sequence[typing.SupportsFloat]) -> None:
        ...
    @property
    def PulseDurationFM(self) -> list[float]:
        ...
    @PulseDurationFM.setter
    def PulseDurationFM(self, arg0: collections.abc.Sequence[typing.SupportsFloat]) -> None:
        ...
    @property
    def PulseLength(self) -> list[float]:
        ...
    @PulseLength.setter
    def PulseLength(self, arg0: collections.abc.Sequence[typing.SupportsFloat]) -> None:
        ...
    @property
    def SampleInterval(self) -> list[float]:
        ...
    @SampleInterval.setter
    def SampleInterval(self, arg0: collections.abc.Sequence[typing.SupportsFloat]) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_Configuration_Transceiver_Channel_FrequencyPar:
    """
    XML base datagram
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transceiver_Channel_FrequencyPar:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Configuration_Transceiver_Channel_FrequencyPar:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Transceiver_Channel_FrequencyPar:
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
    def copy(self) -> XML_Configuration_Transceiver_Channel_FrequencyPar:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def AngleOffsetAlongship(self) -> float:
        ...
    @AngleOffsetAlongship.setter
    def AngleOffsetAlongship(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def AngleOffsetAthwartship(self) -> float:
        ...
    @AngleOffsetAthwartship.setter
    def AngleOffsetAthwartship(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def BeamWidthAlongship(self) -> float:
        ...
    @BeamWidthAlongship.setter
    def BeamWidthAlongship(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def BeamWidthAthwartship(self) -> float:
        ...
    @BeamWidthAthwartship.setter
    def BeamWidthAthwartship(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Frequency(self) -> float:
        ...
    @Frequency.setter
    def Frequency(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Gain(self) -> float:
        ...
    @Gain.setter
    def Gain(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Impedance(self) -> float:
        ...
    @Impedance.setter
    def Impedance(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Phase(self) -> float:
        ...
    @Phase.setter
    def Phase(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_Configuration_Transducer:
    """
    XML base datagram
    """
    TransducerCustomName: str
    TransducerMounting: str
    TransducerName: str
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transducer:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Configuration_Transducer:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Transducer:
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
    def copy(self) -> XML_Configuration_Transducer:
        """
        return a copy using the c++ default copy constructor
        """
    def get_sensor_offsets(self) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets:
        """
        Return the offsets as navigation::datastructures::PositionalOffsets
        structure
        
        Returns:
            navigation::datastructures::PositionalOffsets
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def HeadingQuickCalibration(self) -> float:
        """
        < Seems to be used seldomly?
        """
    @HeadingQuickCalibration.setter
    def HeadingQuickCalibration(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def TransducerAlphaX(self) -> float:
        ...
    @TransducerAlphaX.setter
    def TransducerAlphaX(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def TransducerAlphaY(self) -> float:
        ...
    @TransducerAlphaY.setter
    def TransducerAlphaY(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def TransducerAlphaZ(self) -> float:
        ...
    @TransducerAlphaZ.setter
    def TransducerAlphaZ(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def TransducerOffsetX(self) -> float:
        ...
    @TransducerOffsetX.setter
    def TransducerOffsetX(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def TransducerOffsetY(self) -> float:
        ...
    @TransducerOffsetY.setter
    def TransducerOffsetY(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def TransducerOffsetZ(self) -> float:
        ...
    @TransducerOffsetZ.setter
    def TransducerOffsetZ(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def TransducerSerialNumber(self) -> int:
        ...
    @TransducerSerialNumber.setter
    def TransducerSerialNumber(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_Environment:
    """
    XML base datagram
    """
    DropKeelOffsetIsManual: bool
    SoundVelocitySource: str
    WaterLevelDraftIsManual: bool
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Environment:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Environment:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Environment:
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
    def copy(self) -> XML_Environment:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def Acidity(self) -> float:
        ...
    @Acidity.setter
    def Acidity(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Depth(self) -> float:
        ...
    @Depth.setter
    def Depth(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def DropKeelOffset(self) -> float:
        ...
    @DropKeelOffset.setter
    def DropKeelOffset(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Latitude(self) -> float:
        ...
    @Latitude.setter
    def Latitude(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Salinity(self) -> float:
        ...
    @Salinity.setter
    def Salinity(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def SoundSpeed(self) -> float:
        ...
    @SoundSpeed.setter
    def SoundSpeed(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def SoundVelocityProfile(self) -> list[float]:
        ...
    @SoundVelocityProfile.setter
    def SoundVelocityProfile(self, arg0: collections.abc.Sequence[typing.SupportsFloat]) -> None:
        ...
    @property
    def Temperature(self) -> float:
        ...
    @Temperature.setter
    def Temperature(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Transducers(self) -> list[XML_Environment_Transducer]:
        ...
    @Transducers.setter
    def Transducers(self, arg0: collections.abc.Sequence[XML_Environment_Transducer]) -> None:
        ...
    @property
    def WaterLevelDraft(self) -> float:
        ...
    @WaterLevelDraft.setter
    def WaterLevelDraft(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_Environment_Transducer:
    """
    XML base datagram
    """
    TransducerName: str
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Environment_Transducer:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Environment_Transducer:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Environment_Transducer:
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
    def copy(self) -> XML_Environment_Transducer:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def SoundSpeed(self) -> float:
        ...
    @SoundSpeed.setter
    def SoundSpeed(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_InitialParameter:
    """
    XML base datagram
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_InitialParameter:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_InitialParameter:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_InitialParameter:
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
    def copy(self) -> XML_InitialParameter:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def Channels(self) -> list[XML_Parameter_Channel]:
        ...
    @Channels.setter
    def Channels(self, arg0: collections.abc.Sequence[XML_Parameter_Channel]) -> None:
        ...
class XML_Node:
    """
    XML base datagram
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Node:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Node:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Node:
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
    @typing.overload
    def attributes(self) -> dict[str, str]:
        ...
    @typing.overload
    def attributes(self, key: str) -> str:
        ...
    @typing.overload
    def children(self) -> dict[str, list[XML_Node]]:
        ...
    @typing.overload
    def children(self, key: str) -> list[XML_Node]:
        ...
    def copy(self) -> XML_Node:
        """
        return a copy using the c++ default copy constructor
        """
    def first_child(self, arg0: str) -> XML_Node:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def name(self) -> str:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Parameter:
    """
    XML base datagram
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Parameter:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Parameter:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Parameter:
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
    def copy(self) -> XML_Parameter:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def Channels(self) -> list[XML_Parameter_Channel]:
        ...
    @Channels.setter
    def Channels(self, arg0: collections.abc.Sequence[XML_Parameter_Channel]) -> None:
        ...
class XML_Parameter_Channel:
    """
    XML base datagram
    """
    ChannelID: str
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Parameter_Channel:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Parameter_Channel:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Parameter_Channel:
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
    def copy(self) -> XML_Parameter_Channel:
        """
        return a copy using the c++ default copy constructor
        """
    def get_pulse_duration(self) -> float:
        ...
    def get_pulse_form_is_cw(self) -> bool:
        ...
    def get_pulse_form_is_fm(self) -> bool:
        ...
    def get_tx_signal_parameters(self) -> themachinethatgoesping.algorithms.signalprocessing.datastructures.CWSignalParameters | themachinethatgoesping.algorithms.signalprocessing.datastructures.FMSignalParameters | themachinethatgoesping.algorithms.signalprocessing.datastructures.GenericSignalParameters:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def BandWidth(self) -> float:
        """
        < TODO: when is this one used
        """
    @BandWidth.setter
    def BandWidth(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def ChannelMode(self) -> int:
        ...
    @ChannelMode.setter
    def ChannelMode(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def Frequency(self) -> float:
        """
        < used for cv ( PulseForm == 0)
        """
    @Frequency.setter
    def Frequency(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def FrequencyEnd(self) -> float:
        """
        < used used for chirp pulse (PulseForm > 0)
        """
    @FrequencyEnd.setter
    def FrequencyEnd(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def FrequencyStart(self) -> float:
        """
        < used used for chirp pulse (PulseForm > 0)
        """
    @FrequencyStart.setter
    def FrequencyStart(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def PulseDuration(self) -> float:
        """
        < used for cv ( PulseForm == 0)
        """
    @PulseDuration.setter
    def PulseDuration(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def PulseForm(self) -> int:
        """
        < 0 means cw, ?1 means chirp?
        """
    @PulseForm.setter
    def PulseForm(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def PulseLength(self) -> float:
        """
        < used for chirp pulse (PulseForm > 0)
        """
    @PulseLength.setter
    def PulseLength(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def SampleInterval(self) -> float:
        ...
    @SampleInterval.setter
    def SampleInterval(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def Slope(self) -> float:
        ...
    @Slope.setter
    def Slope(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def SoundVelocity(self) -> float:
        ...
    @SoundVelocity.setter
    def SoundVelocity(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def TransducerDepth(self) -> float:
        """
        < when is this one used? only old format?
        """
    @TransducerDepth.setter
    def TransducerDepth(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def TransmitPower(self) -> float:
        ...
    @TransmitPower.setter
    def TransmitPower(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_PingSequence:
    """
    XML base datagram
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_PingSequence:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_PingSequence:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_PingSequence:
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
    def copy(self) -> XML_PingSequence:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def Pings(self) -> list[XML_PingSequence_Ping]:
        ...
    @Pings.setter
    def Pings(self, arg0: collections.abc.Sequence[XML_PingSequence_Ping]) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_PingSequence_Ping:
    """
    XML base datagram
    """
    ChannelID: str
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_PingSequence_Ping:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_PingSequence_Ping:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_PingSequence_Ping:
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
    def copy(self) -> XML_PingSequence_Ping:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class XML_Sensor:
    """
    XML base datagram
    """
    IsManual: bool
    Type: str
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Sensor:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> XML_Sensor:
        ...
    def __deepcopy__(self, arg0: dict) -> XML_Sensor:
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
    def copy(self) -> XML_Sensor:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def ManualValue(self) -> float:
        ...
    @ManualValue.setter
    def ManualValue(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def unknown_attributes(self) -> int:
        ...
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def unknown_children(self) -> int:
        ...
    @unknown_children.setter
    def unknown_children(self, arg0: typing.SupportsInt) -> None:
        ...
class t_BeamType:
    """
    
    
    Members:
    
      BeamTypeSingle : 
    
      BeamTypeSplit : 
    
      BeamTypeRef : 
    
      BeamTypeRefB : 
    
      BeamTypeSplit3 : 
    
      BeamTypeSplit2 : 
    
      BeamTypeSplit3C : 
    
      BeamTypeSplit3CN : 
    
      BeamTypeSplit3CW : 
    """
    BeamTypeRef: typing.ClassVar[t_BeamType]  # value = <t_BeamType.BeamTypeRef: 2>
    BeamTypeRefB: typing.ClassVar[t_BeamType]  # value = <t_BeamType.BeamTypeRefB: 4>
    BeamTypeSingle: typing.ClassVar[t_BeamType]  # value = <t_BeamType.BeamTypeSingle: 0>
    BeamTypeSplit: typing.ClassVar[t_BeamType]  # value = <t_BeamType.BeamTypeSplit: 1>
    BeamTypeSplit2: typing.ClassVar[t_BeamType]  # value = <t_BeamType.BeamTypeSplit2: 33>
    BeamTypeSplit3: typing.ClassVar[t_BeamType]  # value = <t_BeamType.BeamTypeSplit3: 17>
    BeamTypeSplit3C: typing.ClassVar[t_BeamType]  # value = <t_BeamType.BeamTypeSplit3C: 49>
    BeamTypeSplit3CN: typing.ClassVar[t_BeamType]  # value = <t_BeamType.BeamTypeSplit3CN: 65>
    BeamTypeSplit3CW: typing.ClassVar[t_BeamType]  # value = <t_BeamType.BeamTypeSplit3CW: 81>
    __members__: typing.ClassVar[dict[str, t_BeamType]]  # value = {'BeamTypeSingle': <t_BeamType.BeamTypeSingle: 0>, 'BeamTypeSplit': <t_BeamType.BeamTypeSplit: 1>, 'BeamTypeRef': <t_BeamType.BeamTypeRef: 2>, 'BeamTypeRefB': <t_BeamType.BeamTypeRefB: 4>, 'BeamTypeSplit3': <t_BeamType.BeamTypeSplit3: 17>, 'BeamTypeSplit2': <t_BeamType.BeamTypeSplit2: 33>, 'BeamTypeSplit3C': <t_BeamType.BeamTypeSplit3C: 49>, 'BeamTypeSplit3CN': <t_BeamType.BeamTypeSplit3CN: 65>, 'BeamTypeSplit3CW': <t_BeamType.BeamTypeSplit3CW: 81>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    @typing.overload
    def __init__(self, value: typing.SupportsInt) -> None:
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
    def __setstate__(self, state: typing.SupportsInt) -> None:
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
BeamTypeRef: t_BeamType  # value = <t_BeamType.BeamTypeRef: 2>
BeamTypeRefB: t_BeamType  # value = <t_BeamType.BeamTypeRefB: 4>
BeamTypeSingle: t_BeamType  # value = <t_BeamType.BeamTypeSingle: 0>
BeamTypeSplit: t_BeamType  # value = <t_BeamType.BeamTypeSplit: 1>
BeamTypeSplit2: t_BeamType  # value = <t_BeamType.BeamTypeSplit2: 33>
BeamTypeSplit3: t_BeamType  # value = <t_BeamType.BeamTypeSplit3: 17>
BeamTypeSplit3C: t_BeamType  # value = <t_BeamType.BeamTypeSplit3C: 49>
BeamTypeSplit3CN: t_BeamType  # value = <t_BeamType.BeamTypeSplit3CN: 65>
BeamTypeSplit3CW: t_BeamType  # value = <t_BeamType.BeamTypeSplit3CW: 81>
