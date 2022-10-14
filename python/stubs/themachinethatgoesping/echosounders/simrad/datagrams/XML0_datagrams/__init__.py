"""Simrad EK80 XML datagram classes (subtypes of XML0)"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams
import typing
import themachinethatgoesping.navigation
import themachinethatgoesping.navigation.datastructures

__all__ = [
    "BeamTypeRef",
    "BeamTypeRefB",
    "BeamTypeSingle",
    "BeamTypeSplit",
    "BeamTypeSplit2",
    "BeamTypeSplit3",
    "BeamTypeSplit3C",
    "BeamTypeSplit3CN",
    "BeamTypeSplit3CW",
    "ChannelConfiguration",
    "XML_Configuration",
    "XML_Configuration_ActivePingMode",
    "XML_Configuration_Sensor",
    "XML_Configuration_Sensor_Telegram",
    "XML_Configuration_Sensor_TelegramValue",
    "XML_Configuration_Transceiver",
    "XML_Configuration_Transceiver_Channel",
    "XML_Configuration_Transceiver_Channel_FrequencyPar",
    "XML_Configuration_Transceiver_Channel_Transducer",
    "XML_Configuration_Transducer",
    "XML_Environment",
    "XML_Environment_Transducer",
    "XML_InitialParameter",
    "XML_Node",
    "XML_Parameter",
    "XML_Parameter_Channel",
    "XML_PingSequence",
    "XML_PingSequence_Ping",
    "XML_Sensor",
    "t_BeamType"
]


class ChannelConfiguration():
    """
    XML base datagram
    """
    def __copy__(self) -> ChannelConfiguration: ...
    def __deepcopy__(self, arg0: dict) -> ChannelConfiguration: ...
    def __getstate__(self) -> bytes: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, ChannelID: str, Channel: XML_Configuration_Transceiver_Channel, Transceiver: XML_Configuration_Transceiver, Transducer: XML_Configuration_Transducer) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> ChannelConfiguration: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ChannelConfiguration: 
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
    def Channel(self) -> XML_Configuration_Transceiver_Channel:
        """
        :type: XML_Configuration_Transceiver_Channel
        """
    @property
    def ChannelID(self) -> str:
        """
        :type: str
        """
    @property
    def Transceiver(self) -> XML_Configuration_Transceiver:
        """
        :type: XML_Configuration_Transceiver
        """
    @property
    def Transducer(self) -> XML_Configuration_Transducer:
        """
        :type: XML_Configuration_Transducer
        """
    @property
    def sensor_offsets(self) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets:
        """
        :type: themachinethatgoesping.navigation.datastructures.PositionalOffsets
        """
    pass
class XML_Configuration():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Configuration: ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration: ...
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
    def copy(self) -> XML_Configuration: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration: 
        """
        create T_CLASS object from bytearray
        """
    def get_prioritized_sensor(self, prio_values: typing.List[str]) -> XML_Configuration_Sensor: ...
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def get_transceiver(self, channel_id: str) -> XML_Configuration_Transceiver: ...
    def get_transceiver_channel(self, channel_id: str) -> XML_Configuration_Transceiver_Channel: ...
    def get_transceiver_channels(self) -> typing.Dict[str, XML_Configuration_Transceiver_Channel]: ...
    def get_transceivers(self) -> typing.Dict[str, XML_Configuration_Transceiver]: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def ActivePingMode(self) -> XML_Configuration_ActivePingMode:
        """
        :type: XML_Configuration_ActivePingMode
        """
    @ActivePingMode.setter
    def ActivePingMode(self, arg0: XML_Configuration_ActivePingMode) -> None:
        pass
    @property
    def ApplicationName(self) -> str:
        """
        :type: str
        """
    @ApplicationName.setter
    def ApplicationName(self, arg0: str) -> None:
        pass
    @property
    def ChannelConfigurations(self) -> typing.Dict[str, ChannelConfiguration]:
        """
        :type: typing.Dict[str, ChannelConfiguration]
        """
    @ChannelConfigurations.setter
    def ChannelConfigurations(self, arg0: typing.Dict[str, ChannelConfiguration]) -> None:
        pass
    @property
    def ConfiguredSensors(self) -> typing.List[XML_Configuration_Sensor]:
        """
        :type: typing.List[XML_Configuration_Sensor]
        """
    @ConfiguredSensors.setter
    def ConfiguredSensors(self, arg0: typing.List[XML_Configuration_Sensor]) -> None:
        pass
    @property
    def Copyright(self) -> str:
        """
        :type: str
        """
    @Copyright.setter
    def Copyright(self, arg0: str) -> None:
        pass
    @property
    def FileFormatVersion(self) -> str:
        """
        :type: str
        """
    @FileFormatVersion.setter
    def FileFormatVersion(self, arg0: str) -> None:
        pass
    @property
    def SensorConfigurations(self) -> typing.Dict[str, typing.List[XML_Configuration_Sensor]]:
        """
        :type: typing.Dict[str, typing.List[XML_Configuration_Sensor]]
        """
    @SensorConfigurations.setter
    def SensorConfigurations(self, arg0: typing.Dict[str, typing.List[XML_Configuration_Sensor]]) -> None:
        pass
    @property
    def TimeBias(self) -> str:
        """
        :type: str
        """
    @TimeBias.setter
    def TimeBias(self, arg0: str) -> None:
        pass
    @property
    def Transceivers(self) -> typing.List[XML_Configuration_Transceiver]:
        """
        :type: typing.List[XML_Configuration_Transceiver]
        """
    @Transceivers.setter
    def Transceivers(self, arg0: typing.List[XML_Configuration_Transceiver]) -> None:
        pass
    @property
    def Transducers(self) -> typing.List[XML_Configuration_Transducer]:
        """
        :type: typing.List[XML_Configuration_Transducer]
        """
    @Transducers.setter
    def Transducers(self, arg0: typing.List[XML_Configuration_Transducer]) -> None:
        pass
    @property
    def Version(self) -> str:
        """
        :type: str
        """
    @Version.setter
    def Version(self, arg0: str) -> None:
        pass
    pass
class XML_Configuration_ActivePingMode():
    def __copy__(self) -> XML_Configuration_ActivePingMode: ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_ActivePingMode: ...
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
    def copy(self) -> XML_Configuration_ActivePingMode: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_ActivePingMode: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def Mode(self) -> str:
        """
        :type: str
        """
    @Mode.setter
    def Mode(self, arg0: str) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_Configuration_Sensor():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Configuration_Sensor: ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Sensor: ...
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
    def copy(self) -> XML_Configuration_Sensor: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Sensor: 
        """
        create T_CLASS object from bytearray
        """
    def get_sensor_offsets(self) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets: 
        """
        Return the sensor offsets as
        navigation::datastructures::PositionalOffsets structure

        Returns:
            navigation::datastructures::PositionalOffsets
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def AngleX(self) -> float:
        """
        :type: float
        """
    @AngleX.setter
    def AngleX(self, arg0: float) -> None:
        pass
    @property
    def AngleY(self) -> float:
        """
        :type: float
        """
    @AngleY.setter
    def AngleY(self, arg0: float) -> None:
        pass
    @property
    def AngleZ(self) -> float:
        """
        :type: float
        """
    @AngleZ.setter
    def AngleZ(self, arg0: float) -> None:
        pass
    @property
    def Name(self) -> str:
        """
        :type: str
        """
    @Name.setter
    def Name(self, arg0: str) -> None:
        pass
    @property
    def Port(self) -> str:
        """
        :type: str
        """
    @Port.setter
    def Port(self, arg0: str) -> None:
        pass
    @property
    def TalkerID(self) -> str:
        """
        :type: str
        """
    @TalkerID.setter
    def TalkerID(self, arg0: str) -> None:
        pass
    @property
    def Telegrams(self) -> typing.List[XML_Configuration_Sensor_Telegram]:
        """
        :type: typing.List[XML_Configuration_Sensor_Telegram]
        """
    @Telegrams.setter
    def Telegrams(self, arg0: typing.List[XML_Configuration_Sensor_Telegram]) -> None:
        pass
    @property
    def Timeout(self) -> float:
        """
        :type: float
        """
    @Timeout.setter
    def Timeout(self, arg0: float) -> None:
        pass
    @property
    def Type(self) -> str:
        """
        :type: str
        """
    @Type.setter
    def Type(self, arg0: str) -> None:
        pass
    @property
    def Unique(self) -> int:
        """
        :type: int
        """
    @Unique.setter
    def Unique(self, arg0: int) -> None:
        pass
    @property
    def X(self) -> float:
        """
        :type: float
        """
    @X.setter
    def X(self, arg0: float) -> None:
        pass
    @property
    def Y(self) -> float:
        """
        :type: float
        """
    @Y.setter
    def Y(self, arg0: float) -> None:
        pass
    @property
    def Z(self) -> float:
        """
        :type: float
        """
    @Z.setter
    def Z(self, arg0: float) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_Configuration_Sensor_Telegram():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Configuration_Sensor_Telegram: ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Sensor_Telegram: ...
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
    def copy(self) -> XML_Configuration_Sensor_Telegram: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Sensor_Telegram: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def Enabled(self) -> bool:
        """
        :type: bool
        """
    @Enabled.setter
    def Enabled(self, arg0: bool) -> None:
        pass
    @property
    def Name(self) -> str:
        """
        :type: str
        """
    @Name.setter
    def Name(self, arg0: str) -> None:
        pass
    @property
    def SubscriptionPath(self) -> str:
        """
        :type: str
        """
    @SubscriptionPath.setter
    def SubscriptionPath(self, arg0: str) -> None:
        pass
    @property
    def Type(self) -> str:
        """
        :type: str
        """
    @Type.setter
    def Type(self, arg0: str) -> None:
        pass
    @property
    def Values(self) -> typing.List[XML_Configuration_Sensor_TelegramValue]:
        """
        :type: typing.List[XML_Configuration_Sensor_TelegramValue]
        """
    @Values.setter
    def Values(self, arg0: typing.List[XML_Configuration_Sensor_TelegramValue]) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_Configuration_Sensor_TelegramValue():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Configuration_Sensor_TelegramValue: ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Sensor_TelegramValue: ...
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
    def copy(self) -> XML_Configuration_Sensor_TelegramValue: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Sensor_TelegramValue: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def Name(self) -> str:
        """
        :type: str
        """
    @Name.setter
    def Name(self, arg0: str) -> None:
        pass
    @property
    def Priority(self) -> int:
        """
        :type: int
        """
    @Priority.setter
    def Priority(self, arg0: int) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_Configuration_Transceiver():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Configuration_Transceiver: ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Transceiver: ...
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
    def copy(self) -> XML_Configuration_Transceiver: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transceiver: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def Channels(self) -> typing.List[XML_Configuration_Transceiver_Channel]:
        """
        :type: typing.List[XML_Configuration_Transceiver_Channel]
        """
    @Channels.setter
    def Channels(self, arg0: typing.List[XML_Configuration_Transceiver_Channel]) -> None:
        pass
    @property
    def EthernetAddress(self) -> str:
        """
        :type: str
        """
    @EthernetAddress.setter
    def EthernetAddress(self, arg0: str) -> None:
        pass
    @property
    def IPAddress(self) -> str:
        """
        :type: str
        """
    @IPAddress.setter
    def IPAddress(self, arg0: str) -> None:
        pass
    @property
    def Impedance(self) -> float:
        """
        :type: float
        """
    @Impedance.setter
    def Impedance(self, arg0: float) -> None:
        pass
    @property
    def MarketSegment(self) -> str:
        """
        :type: str
        """
    @MarketSegment.setter
    def MarketSegment(self, arg0: str) -> None:
        pass
    @property
    def Multiplexing(self) -> int:
        """
        :type: int
        """
    @Multiplexing.setter
    def Multiplexing(self, arg0: int) -> None:
        pass
    @property
    def RxSampleFrequency(self) -> float:
        """
        :type: float
        """
    @RxSampleFrequency.setter
    def RxSampleFrequency(self, arg0: float) -> None:
        pass
    @property
    def SerialNumber(self) -> int:
        """
        :type: int
        """
    @SerialNumber.setter
    def SerialNumber(self, arg0: int) -> None:
        pass
    @property
    def TransceiverName(self) -> str:
        """
        :type: str
        """
    @TransceiverName.setter
    def TransceiverName(self, arg0: str) -> None:
        pass
    @property
    def TransceiverNumber(self) -> int:
        """
        :type: int
        """
    @TransceiverNumber.setter
    def TransceiverNumber(self, arg0: int) -> None:
        pass
    @property
    def TransceiverSoftwareVersion(self) -> str:
        """
        :type: str
        """
    @TransceiverSoftwareVersion.setter
    def TransceiverSoftwareVersion(self, arg0: str) -> None:
        pass
    @property
    def TransceiverType(self) -> str:
        """
        :type: str
        """
    @TransceiverType.setter
    def TransceiverType(self, arg0: str) -> None:
        pass
    @property
    def Version(self) -> str:
        """
        :type: str
        """
    @Version.setter
    def Version(self, arg0: str) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_Configuration_Transceiver_Channel():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Configuration_Transceiver_Channel: ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Transceiver_Channel: ...
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
    def copy(self) -> XML_Configuration_Transceiver_Channel: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transceiver_Channel: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def ChannelID(self) -> str:
        """
        :type: str
        """
    @ChannelID.setter
    def ChannelID(self, arg0: str) -> None:
        pass
    @property
    def ChannelIdShort(self) -> str:
        """
        :type: str
        """
    @ChannelIdShort.setter
    def ChannelIdShort(self, arg0: str) -> None:
        pass
    @property
    def ChannelNumber(self) -> int:
        """
        :type: int
        """
    @ChannelNumber.setter
    def ChannelNumber(self, arg0: int) -> None:
        pass
    @property
    def HWChannelConfiguration(self) -> int:
        """
        :type: int
        """
    @HWChannelConfiguration.setter
    def HWChannelConfiguration(self, arg0: int) -> None:
        pass
    @property
    def LogicalChannelID(self) -> str:
        """
        :type: str
        """
    @LogicalChannelID.setter
    def LogicalChannelID(self, arg0: str) -> None:
        pass
    @property
    def MaxTxPowerTransceiver(self) -> float:
        """
        :type: float
        """
    @MaxTxPowerTransceiver.setter
    def MaxTxPowerTransceiver(self, arg0: float) -> None:
        pass
    @property
    def PulseDuration(self) -> typing.List[float]:
        """
        :type: typing.List[float]
        """
    @PulseDuration.setter
    def PulseDuration(self, arg0: typing.List[float]) -> None:
        pass
    @property
    def PulseDurationFM(self) -> typing.List[float]:
        """
        :type: typing.List[float]
        """
    @PulseDurationFM.setter
    def PulseDurationFM(self, arg0: typing.List[float]) -> None:
        pass
    @property
    def PulseLength(self) -> typing.List[float]:
        """
        :type: typing.List[float]
        """
    @PulseLength.setter
    def PulseLength(self, arg0: typing.List[float]) -> None:
        pass
    @property
    def SampleInterval(self) -> typing.List[float]:
        """
        :type: typing.List[float]
        """
    @SampleInterval.setter
    def SampleInterval(self, arg0: typing.List[float]) -> None:
        pass
    @property
    def Transducer(self) -> XML_Configuration_Transceiver_Channel_Transducer:
        """
        :type: XML_Configuration_Transceiver_Channel_Transducer
        """
    @Transducer.setter
    def Transducer(self, arg0: XML_Configuration_Transceiver_Channel_Transducer) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_Configuration_Transceiver_Channel_FrequencyPar():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Configuration_Transceiver_Channel_FrequencyPar: ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Transceiver_Channel_FrequencyPar: ...
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
    def copy(self) -> XML_Configuration_Transceiver_Channel_FrequencyPar: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transceiver_Channel_FrequencyPar: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def AngleOffsetAlongship(self) -> float:
        """
        :type: float
        """
    @AngleOffsetAlongship.setter
    def AngleOffsetAlongship(self, arg0: float) -> None:
        pass
    @property
    def AngleOffsetAthwartship(self) -> float:
        """
        :type: float
        """
    @AngleOffsetAthwartship.setter
    def AngleOffsetAthwartship(self, arg0: float) -> None:
        pass
    @property
    def BeamWidthAlongship(self) -> float:
        """
        :type: float
        """
    @BeamWidthAlongship.setter
    def BeamWidthAlongship(self, arg0: float) -> None:
        pass
    @property
    def BeamWidthAthwartship(self) -> float:
        """
        :type: float
        """
    @BeamWidthAthwartship.setter
    def BeamWidthAthwartship(self, arg0: float) -> None:
        pass
    @property
    def Frequency(self) -> float:
        """
        :type: float
        """
    @Frequency.setter
    def Frequency(self, arg0: float) -> None:
        pass
    @property
    def Gain(self) -> float:
        """
        :type: float
        """
    @Gain.setter
    def Gain(self, arg0: float) -> None:
        pass
    @property
    def Impedance(self) -> float:
        """
        :type: float
        """
    @Impedance.setter
    def Impedance(self, arg0: float) -> None:
        pass
    @property
    def Phase(self) -> float:
        """
        :type: float
        """
    @Phase.setter
    def Phase(self, arg0: float) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_Configuration_Transceiver_Channel_Transducer():
    def __copy__(self) -> XML_Configuration_Transceiver_Channel_Transducer: ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Transceiver_Channel_Transducer: ...
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
    def copy(self) -> XML_Configuration_Transceiver_Channel_Transducer: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transceiver_Channel_Transducer: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def AngleOffsetAlongship(self) -> float:
        """
        :type: float
        """
    @AngleOffsetAlongship.setter
    def AngleOffsetAlongship(self, arg0: float) -> None:
        pass
    @property
    def AngleOffsetAthwartship(self) -> float:
        """
        :type: float
        """
    @AngleOffsetAthwartship.setter
    def AngleOffsetAthwartship(self, arg0: float) -> None:
        pass
    @property
    def AngleSensitivityAlongship(self) -> float:
        """
        :type: float
        """
    @AngleSensitivityAlongship.setter
    def AngleSensitivityAlongship(self, arg0: float) -> None:
        pass
    @property
    def AngleSensitivityAthwartship(self) -> float:
        """
        :type: float
        """
    @AngleSensitivityAthwartship.setter
    def AngleSensitivityAthwartship(self, arg0: float) -> None:
        pass
    @property
    def ArticleNumber(self) -> str:
        """
        :type: str
        """
    @ArticleNumber.setter
    def ArticleNumber(self, arg0: str) -> None:
        pass
    @property
    def BeamType(self) -> t_BeamType:
        """
        :type: t_BeamType
        """
    @BeamType.setter
    def BeamType(self, arg0: t_BeamType) -> None:
        pass
    @property
    def BeamWidthAlongship(self) -> float:
        """
        :type: float
        """
    @BeamWidthAlongship.setter
    def BeamWidthAlongship(self, arg0: float) -> None:
        pass
    @property
    def BeamWidthAthwartship(self) -> float:
        """
        :type: float
        """
    @BeamWidthAthwartship.setter
    def BeamWidthAthwartship(self, arg0: float) -> None:
        pass
    @property
    def DirectivityDropAt2XBeamWidth(self) -> float:
        """
        :type: float
        """
    @DirectivityDropAt2XBeamWidth.setter
    def DirectivityDropAt2XBeamWidth(self, arg0: float) -> None:
        pass
    @property
    def EquivalentBeamAngle(self) -> float:
        """
        :type: float
        """
    @EquivalentBeamAngle.setter
    def EquivalentBeamAngle(self, arg0: float) -> None:
        pass
    @property
    def Frequency(self) -> float:
        """
        :type: float
        """
    @Frequency.setter
    def Frequency(self, arg0: float) -> None:
        pass
    @property
    def FrequencyMaximum(self) -> float:
        """
        :type: float
        """
    @FrequencyMaximum.setter
    def FrequencyMaximum(self, arg0: float) -> None:
        pass
    @property
    def FrequencyMinimum(self) -> float:
        """
        :type: float
        """
    @FrequencyMinimum.setter
    def FrequencyMinimum(self, arg0: float) -> None:
        pass
    @property
    def FrequencyPars(self) -> typing.List[XML_Configuration_Transceiver_Channel_FrequencyPar]:
        """
        :type: typing.List[XML_Configuration_Transceiver_Channel_FrequencyPar]
        """
    @FrequencyPars.setter
    def FrequencyPars(self, arg0: typing.List[XML_Configuration_Transceiver_Channel_FrequencyPar]) -> None:
        pass
    @property
    def Gain(self) -> typing.List[float]:
        """
        :type: typing.List[float]
        """
    @Gain.setter
    def Gain(self, arg0: typing.List[float]) -> None:
        pass
    @property
    def MaxTxPowerTransducer(self) -> float:
        """
        :type: float
        """
    @MaxTxPowerTransducer.setter
    def MaxTxPowerTransducer(self, arg0: float) -> None:
        pass
    @property
    def SaCorrection(self) -> typing.List[float]:
        """
        :type: typing.List[float]
        """
    @SaCorrection.setter
    def SaCorrection(self, arg0: typing.List[float]) -> None:
        pass
    @property
    def SerialNumber(self) -> int:
        """
        :type: int
        """
    @SerialNumber.setter
    def SerialNumber(self, arg0: int) -> None:
        pass
    @property
    def TransducerName(self) -> str:
        """
        :type: str
        """
    @TransducerName.setter
    def TransducerName(self, arg0: str) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_Configuration_Transducer():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Configuration_Transducer: ...
    def __deepcopy__(self, arg0: dict) -> XML_Configuration_Transducer: ...
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
    def copy(self) -> XML_Configuration_Transducer: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transducer: 
        """
        create T_CLASS object from bytearray
        """
    def get_sensor_offsets(self) -> themachinethatgoesping.navigation.datastructures.PositionalOffsets: 
        """
        Return the offsets as navigation::datastructures::PositionalOffsets
        structure

        Returns:
            navigation::datastructures::PositionalOffsets
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
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

        :type: float
        """
    @HeadingQuickCalibration.setter
    def HeadingQuickCalibration(self, arg0: float) -> None:
        """
        < Seems to be used seldomly?
        """
    @property
    def TransducerAlphaX(self) -> float:
        """
        :type: float
        """
    @TransducerAlphaX.setter
    def TransducerAlphaX(self, arg0: float) -> None:
        pass
    @property
    def TransducerAlphaY(self) -> float:
        """
        :type: float
        """
    @TransducerAlphaY.setter
    def TransducerAlphaY(self, arg0: float) -> None:
        pass
    @property
    def TransducerAlphaZ(self) -> float:
        """
        :type: float
        """
    @TransducerAlphaZ.setter
    def TransducerAlphaZ(self, arg0: float) -> None:
        pass
    @property
    def TransducerCustomName(self) -> str:
        """
        :type: str
        """
    @TransducerCustomName.setter
    def TransducerCustomName(self, arg0: str) -> None:
        pass
    @property
    def TransducerMounting(self) -> str:
        """
        :type: str
        """
    @TransducerMounting.setter
    def TransducerMounting(self, arg0: str) -> None:
        pass
    @property
    def TransducerName(self) -> str:
        """
        :type: str
        """
    @TransducerName.setter
    def TransducerName(self, arg0: str) -> None:
        pass
    @property
    def TransducerOffsetX(self) -> float:
        """
        :type: float
        """
    @TransducerOffsetX.setter
    def TransducerOffsetX(self, arg0: float) -> None:
        pass
    @property
    def TransducerOffsetY(self) -> float:
        """
        :type: float
        """
    @TransducerOffsetY.setter
    def TransducerOffsetY(self, arg0: float) -> None:
        pass
    @property
    def TransducerOffsetZ(self) -> float:
        """
        :type: float
        """
    @TransducerOffsetZ.setter
    def TransducerOffsetZ(self, arg0: float) -> None:
        pass
    @property
    def TransducerSerialNumber(self) -> int:
        """
        :type: int
        """
    @TransducerSerialNumber.setter
    def TransducerSerialNumber(self, arg0: int) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_Environment():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Environment: ...
    def __deepcopy__(self, arg0: dict) -> XML_Environment: ...
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
    def copy(self) -> XML_Environment: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Environment: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def Acidity(self) -> float:
        """
        :type: float
        """
    @Acidity.setter
    def Acidity(self, arg0: float) -> None:
        pass
    @property
    def Depth(self) -> float:
        """
        :type: float
        """
    @Depth.setter
    def Depth(self, arg0: float) -> None:
        pass
    @property
    def DropKeelOffset(self) -> float:
        """
        :type: float
        """
    @DropKeelOffset.setter
    def DropKeelOffset(self, arg0: float) -> None:
        pass
    @property
    def DropKeelOffsetIsManual(self) -> bool:
        """
        :type: bool
        """
    @DropKeelOffsetIsManual.setter
    def DropKeelOffsetIsManual(self, arg0: bool) -> None:
        pass
    @property
    def Latitude(self) -> float:
        """
        :type: float
        """
    @Latitude.setter
    def Latitude(self, arg0: float) -> None:
        pass
    @property
    def Salinity(self) -> float:
        """
        :type: float
        """
    @Salinity.setter
    def Salinity(self, arg0: float) -> None:
        pass
    @property
    def SoundSpeed(self) -> float:
        """
        :type: float
        """
    @SoundSpeed.setter
    def SoundSpeed(self, arg0: float) -> None:
        pass
    @property
    def SoundVelocityProfile(self) -> typing.List[float]:
        """
        :type: typing.List[float]
        """
    @SoundVelocityProfile.setter
    def SoundVelocityProfile(self, arg0: typing.List[float]) -> None:
        pass
    @property
    def SoundVelocitySource(self) -> str:
        """
        :type: str
        """
    @SoundVelocitySource.setter
    def SoundVelocitySource(self, arg0: str) -> None:
        pass
    @property
    def Temperature(self) -> float:
        """
        :type: float
        """
    @Temperature.setter
    def Temperature(self, arg0: float) -> None:
        pass
    @property
    def Transducers(self) -> typing.List[XML_Environment_Transducer]:
        """
        :type: typing.List[XML_Environment_Transducer]
        """
    @Transducers.setter
    def Transducers(self, arg0: typing.List[XML_Environment_Transducer]) -> None:
        pass
    @property
    def WaterLevelDraft(self) -> float:
        """
        :type: float
        """
    @WaterLevelDraft.setter
    def WaterLevelDraft(self, arg0: float) -> None:
        pass
    @property
    def WaterLevelDraftIsManual(self) -> bool:
        """
        :type: bool
        """
    @WaterLevelDraftIsManual.setter
    def WaterLevelDraftIsManual(self, arg0: bool) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_Environment_Transducer():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Environment_Transducer: ...
    def __deepcopy__(self, arg0: dict) -> XML_Environment_Transducer: ...
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
    def copy(self) -> XML_Environment_Transducer: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Environment_Transducer: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def SoundSpeed(self) -> float:
        """
        :type: float
        """
    @SoundSpeed.setter
    def SoundSpeed(self, arg0: float) -> None:
        pass
    @property
    def TransducerName(self) -> str:
        """
        :type: str
        """
    @TransducerName.setter
    def TransducerName(self, arg0: str) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_InitialParameter():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_InitialParameter: ...
    def __deepcopy__(self, arg0: dict) -> XML_InitialParameter: ...
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
    def copy(self) -> XML_InitialParameter: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_InitialParameter: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def Channels(self) -> typing.List[XML_Parameter_Channel]:
        """
        :type: typing.List[XML_Parameter_Channel]
        """
    @Channels.setter
    def Channels(self, arg0: typing.List[XML_Parameter_Channel]) -> None:
        pass
    pass
class XML_Node():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Node: ...
    def __deepcopy__(self, arg0: dict) -> XML_Node: ...
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
    @typing.overload
    def attributes(self) -> typing.Dict[str, str]: ...
    @typing.overload
    def attributes(self, key: str) -> str: ...
    @typing.overload
    def children(self) -> typing.Dict[str, typing.List[XML_Node]]: ...
    @typing.overload
    def children(self, key: str) -> typing.List[XML_Node]: ...
    def copy(self) -> XML_Node: 
        """
        return a copy using the c++ default copy constructor
        """
    def first_child(self, arg0: str) -> XML_Node: ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Node: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def name(self) -> str: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
class XML_Parameter():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Parameter: ...
    def __deepcopy__(self, arg0: dict) -> XML_Parameter: ...
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
    def copy(self) -> XML_Parameter: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Parameter: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def Channels(self) -> typing.List[XML_Parameter_Channel]:
        """
        :type: typing.List[XML_Parameter_Channel]
        """
    @Channels.setter
    def Channels(self, arg0: typing.List[XML_Parameter_Channel]) -> None:
        pass
    pass
class XML_Parameter_Channel():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Parameter_Channel: ...
    def __deepcopy__(self, arg0: dict) -> XML_Parameter_Channel: ...
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
    def copy(self) -> XML_Parameter_Channel: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Parameter_Channel: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
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

        :type: float
        """
    @BandWidth.setter
    def BandWidth(self, arg0: float) -> None:
        """
        < TODO: when is this one used
        """
    @property
    def ChannelID(self) -> str:
        """
        :type: str
        """
    @ChannelID.setter
    def ChannelID(self, arg0: str) -> None:
        pass
    @property
    def ChannelMode(self) -> int:
        """
        :type: int
        """
    @ChannelMode.setter
    def ChannelMode(self, arg0: int) -> None:
        pass
    @property
    def Frequency(self) -> float:
        """
        < used for cv ( PulseForm == 0)

        :type: float
        """
    @Frequency.setter
    def Frequency(self, arg0: float) -> None:
        """
        < used for cv ( PulseForm == 0)
        """
    @property
    def FrequencyEnd(self) -> float:
        """
        < used used for chirp pulse (PulseForm > 0)

        :type: float
        """
    @FrequencyEnd.setter
    def FrequencyEnd(self, arg0: float) -> None:
        """
        < used used for chirp pulse (PulseForm > 0)
        """
    @property
    def FrequencyStart(self) -> float:
        """
        < used used for chirp pulse (PulseForm > 0)

        :type: float
        """
    @FrequencyStart.setter
    def FrequencyStart(self, arg0: float) -> None:
        """
        < used used for chirp pulse (PulseForm > 0)
        """
    @property
    def PulseDuration(self) -> float:
        """
        < used used for chirp pulse (PulseForm > 0)

        :type: float
        """
    @PulseDuration.setter
    def PulseDuration(self, arg0: float) -> None:
        """
        < used used for chirp pulse (PulseForm > 0)
        """
    @property
    def PulseForm(self) -> float:
        """
        < 0 means cw, ?1 means chirp?

        :type: float
        """
    @PulseForm.setter
    def PulseForm(self, arg0: float) -> None:
        """
        < 0 means cw, ?1 means chirp?
        """
    @property
    def PulseLength(self) -> float:
        """
        < used for cv ( PulseForm == 0)

        :type: float
        """
    @PulseLength.setter
    def PulseLength(self, arg0: float) -> None:
        """
        < used for cv ( PulseForm == 0)
        """
    @property
    def SampleInterval(self) -> float:
        """
        :type: float
        """
    @SampleInterval.setter
    def SampleInterval(self, arg0: float) -> None:
        pass
    @property
    def Slope(self) -> float:
        """
        :type: float
        """
    @Slope.setter
    def Slope(self, arg0: float) -> None:
        pass
    @property
    def SoundVelocity(self) -> float:
        """
        :type: float
        """
    @SoundVelocity.setter
    def SoundVelocity(self, arg0: float) -> None:
        pass
    @property
    def TransducerDepth(self) -> float:
        """
        < when is this one used? only old format?

        :type: float
        """
    @TransducerDepth.setter
    def TransducerDepth(self, arg0: float) -> None:
        """
        < when is this one used? only old format?
        """
    @property
    def TransmitPower(self) -> float:
        """
        :type: float
        """
    @TransmitPower.setter
    def TransmitPower(self, arg0: float) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_PingSequence():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_PingSequence: ...
    def __deepcopy__(self, arg0: dict) -> XML_PingSequence: ...
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
    def copy(self) -> XML_PingSequence: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_PingSequence: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def Pings(self) -> typing.List[XML_PingSequence_Ping]:
        """
        :type: typing.List[XML_PingSequence_Ping]
        """
    @Pings.setter
    def Pings(self, arg0: typing.List[XML_PingSequence_Ping]) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_PingSequence_Ping():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_PingSequence_Ping: ...
    def __deepcopy__(self, arg0: dict) -> XML_PingSequence_Ping: ...
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
    def copy(self) -> XML_PingSequence_Ping: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_PingSequence_Ping: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def ChannelID(self) -> str:
        """
        :type: str
        """
    @ChannelID.setter
    def ChannelID(self, arg0: str) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class XML_Sensor():
    """
    XML base datagram
    """
    def __copy__(self) -> XML_Sensor: ...
    def __deepcopy__(self, arg0: dict) -> XML_Sensor: ...
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
    def copy(self) -> XML_Sensor: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Sensor: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def IsManual(self) -> bool:
        """
        :type: bool
        """
    @IsManual.setter
    def IsManual(self, arg0: bool) -> None:
        pass
    @property
    def ManualValue(self) -> float:
        """
        :type: float
        """
    @ManualValue.setter
    def ManualValue(self, arg0: float) -> None:
        pass
    @property
    def Type(self) -> str:
        """
        :type: str
        """
    @Type.setter
    def Type(self, arg0: str) -> None:
        pass
    @property
    def unknown_attributes(self) -> int:
        """
        :type: int
        """
    @unknown_attributes.setter
    def unknown_attributes(self, arg0: int) -> None:
        pass
    @property
    def unknown_children(self) -> int:
        """
        :type: int
        """
    @unknown_children.setter
    def unknown_children(self, arg0: int) -> None:
        pass
    pass
class t_BeamType():
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
    BeamTypeRef: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeRef: 2>
    BeamTypeRefB: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeRefB: 4>
    BeamTypeSingle: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSingle: 0>
    BeamTypeSplit: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSplit: 1>
    BeamTypeSplit2: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSplit2: 33>
    BeamTypeSplit3: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSplit3: 17>
    BeamTypeSplit3C: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSplit3C: 49>
    BeamTypeSplit3CN: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSplit3CN: 65>
    BeamTypeSplit3CW: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSplit3CW: 81>
    __members__: dict # value = {'BeamTypeSingle': <t_BeamType.BeamTypeSingle: 0>, 'BeamTypeSplit': <t_BeamType.BeamTypeSplit: 1>, 'BeamTypeRef': <t_BeamType.BeamTypeRef: 2>, 'BeamTypeRefB': <t_BeamType.BeamTypeRefB: 4>, 'BeamTypeSplit3': <t_BeamType.BeamTypeSplit3: 17>, 'BeamTypeSplit2': <t_BeamType.BeamTypeSplit2: 33>, 'BeamTypeSplit3C': <t_BeamType.BeamTypeSplit3C: 49>, 'BeamTypeSplit3CN': <t_BeamType.BeamTypeSplit3CN: 65>, 'BeamTypeSplit3CW': <t_BeamType.BeamTypeSplit3CW: 81>}
    pass
BeamTypeRef: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeRef: 2>
BeamTypeRefB: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeRefB: 4>
BeamTypeSingle: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSingle: 0>
BeamTypeSplit: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSplit: 1>
BeamTypeSplit2: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSplit2: 33>
BeamTypeSplit3: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSplit3: 17>
BeamTypeSplit3C: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSplit3C: 49>
BeamTypeSplit3CN: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSplit3CN: 65>
BeamTypeSplit3CW: themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.t_BeamType # value = <t_BeamType.BeamTypeSplit3CW: 81>
