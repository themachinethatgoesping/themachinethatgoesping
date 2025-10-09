"""
SimradRaw EK80 XML datagram classes (subtypes of XML0)
"""
from __future__ import annotations
import collections.abc
import enum
import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.navigation_nanopy.datastructures
import typing
__all__: list[str] = ['BeamTypeRef', 'BeamTypeRefB', 'BeamTypeSingle', 'BeamTypeSplit', 'BeamTypeSplit2', 'BeamTypeSplit3', 'BeamTypeSplit3C', 'BeamTypeSplit3CN', 'BeamTypeSplit3CW', 'ChannelConfiguration', 'XMLConfigurationActivePingMode', 'XMLConfigurationTransceiverChannelTransducer', 'XML_Configuration', 'XML_Configuration_Sensor', 'XML_Configuration_Sensor_Telegram', 'XML_Configuration_Sensor_TelegramValue', 'XML_Configuration_Transceiver', 'XML_Configuration_Transceiver_Channel', 'XML_Configuration_Transceiver_Channel_FrequencyPar', 'XML_Configuration_Transducer', 'XML_Environment', 'XML_Environment_Transducer', 'XML_InitialParameter', 'XML_Node', 'XML_Parameter', 'XML_Parameter_Channel', 'XML_PingSequence', 'XML_PingSequence_Ping', 'XML_Sensor', 't_BeamType']
class ChannelConfiguration:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> ChannelConfiguration:
        ...
    def __deepcopy__(self, arg: dict) -> ChannelConfiguration:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, ChannelID: str, Channel: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver_Channel, Transceiver: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver, Transducer: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transducer) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    def sensor_offsets(self) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
        ...
class XMLConfigurationActivePingMode:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    Mode: str
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XMLConfigurationActivePingMode:
        ...
    def __deepcopy__(self, arg: dict) -> XMLConfigurationActivePingMode:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XMLConfigurationTransceiverChannelTransducer:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    AngleOffsetAlongship: float
    AngleOffsetAthwartship: float
    AngleSensitivityAlongship: float
    AngleSensitivityAthwartship: float
    ArticleNumber: str
    BeamType: t_BeamType
    BeamWidthAlongship: float
    BeamWidthAthwartship: float
    DirectivityDropAt2XBeamWidth: float
    EquivalentBeamAngle: float
    Frequency: float
    FrequencyMaximum: float
    FrequencyMinimum: float
    MaxTxPowerTransducer: float
    SerialNumber: int
    TransducerName: str
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XMLConfigurationTransceiverChannelTransducer:
        ...
    def __deepcopy__(self, arg: dict) -> XMLConfigurationTransceiverChannelTransducer:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def FrequencyPars(self) -> ...:
        ...
    @FrequencyPars.setter
    def FrequencyPars(self, arg: ..., std: ...) -> None:
        ...
    @property
    def Gain(self) -> ...:
        ...
    @Gain.setter
    def Gain(self, arg: ..., std: ...) -> None:
        ...
    @property
    def SaCorrection(self) -> ...:
        ...
    @SaCorrection.setter
    def SaCorrection(self, arg: ..., std: ...) -> None:
        ...
class XML_Configuration:
    """
    XML Configuration datagram structure.
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    ActivePingMode: XMLConfigurationActivePingMode
    ApplicationName: str
    Copyright: str
    FileFormatVersion: str
    TimeBias: str
    Version: str
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Configuration:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Configuration:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    def ChannelConfigurations(self, arg: collections.abc.Mapping[str, ChannelConfiguration]) -> None:
        ...
    @property
    def ConfiguredSensors(self) -> list[XML_Configuration_Sensor]:
        ...
    @ConfiguredSensors.setter
    def ConfiguredSensors(self, arg: collections.abc.Sequence[XML_Configuration_Sensor]) -> None:
        ...
    @property
    def SensorConfigurations(self) -> dict[str, list[XML_Configuration_Sensor]]:
        ...
    @SensorConfigurations.setter
    def SensorConfigurations(self, arg: collections.abc.Mapping[str, collections.abc.Sequence[XML_Configuration_Sensor]]) -> None:
        ...
    @property
    def Transceivers(self) -> list[XML_Configuration_Transceiver]:
        ...
    @Transceivers.setter
    def Transceivers(self, arg: collections.abc.Sequence[XML_Configuration_Transceiver]) -> None:
        ...
    @property
    def Transducers(self) -> list[XML_Configuration_Transducer]:
        ...
    @Transducers.setter
    def Transducers(self, arg: collections.abc.Sequence[XML_Configuration_Transducer]) -> None:
        ...
class XML_Configuration_Sensor:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    AngleX: float
    AngleY: float
    AngleZ: float
    Name: str
    Port: str
    TalkerID: str
    Timeout: float
    Type: str
    Unique: int
    X: float
    Y: float
    Z: float
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Configuration_Sensor:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Configuration_Sensor:
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
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> XML_Configuration_Sensor:
        """
        return a copy using the c++ default copy constructor
        """
    def get_sensor_offsets(self) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def Telegrams(self) -> list[XML_Configuration_Sensor_Telegram]:
        ...
    @Telegrams.setter
    def Telegrams(self, arg: collections.abc.Sequence[XML_Configuration_Sensor_Telegram]) -> None:
        ...
class XML_Configuration_Sensor_Telegram:
    """
    XML Configuration Sensor Telegram (single <Telegram> node).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    Enabled: bool
    Name: str
    SubscriptionPath: str
    Type: str
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Configuration_Sensor_Telegram:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Configuration_Sensor_Telegram:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        """
        Returns true if no unknown children/attributes were encountered.
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    def Values(self, arg: collections.abc.Sequence[XML_Configuration_Sensor_TelegramValue]) -> None:
        ...
class XML_Configuration_Sensor_TelegramValue:
    """
    XML Configuration Sensor Telegram Value (single <Value> node).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    Name: str
    Priority: int
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Configuration_Sensor_TelegramValue:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Configuration_Sensor_TelegramValue:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        """
        Returns true if no unknown children/attributes were encountered.
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Configuration_Transceiver:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    EthernetAddress: str
    IPAddress: str
    Impedance: float
    MarketSegment: str
    Multiplexing: int
    RxSampleFrequency: float
    SerialNumber: int
    TransceiverName: str
    TransceiverNumber: int
    TransceiverSoftwareVersion: str
    TransceiverType: str
    Version: str
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Configuration_Transceiver:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Configuration_Transceiver:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    def Channels(self, arg: collections.abc.Sequence[XML_Configuration_Transceiver_Channel]) -> None:
        ...
class XML_Configuration_Transceiver_Channel:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    ChannelID: str
    ChannelIdShort: str
    ChannelNumber: int
    HWChannelConfiguration: int
    LogicalChannelID: str
    MaxTxPowerTransceiver: float
    Transducer: XMLConfigurationTransceiverChannelTransducer
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Configuration_Transceiver_Channel:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Configuration_Transceiver_Channel:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def PulseDuration(self) -> list[float]:
        ...
    @PulseDuration.setter
    def PulseDuration(self, arg: collections.abc.Sequence[float]) -> None:
        ...
    @property
    def PulseDurationFM(self) -> list[float]:
        ...
    @PulseDurationFM.setter
    def PulseDurationFM(self, arg: collections.abc.Sequence[float]) -> None:
        ...
    @property
    def PulseLength(self) -> list[float]:
        ...
    @PulseLength.setter
    def PulseLength(self, arg: collections.abc.Sequence[float]) -> None:
        ...
    @property
    def SampleInterval(self) -> list[float]:
        ...
    @SampleInterval.setter
    def SampleInterval(self, arg: collections.abc.Sequence[float]) -> None:
        ...
class XML_Configuration_Transceiver_Channel_FrequencyPar:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    AngleOffsetAlongship: float
    AngleOffsetAthwartship: float
    BeamWidthAlongship: float
    BeamWidthAthwartship: float
    Frequency: float
    Gain: float
    Impedance: float
    Phase: float
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Configuration_Transceiver_Channel_FrequencyPar:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Configuration_Transceiver_Channel_FrequencyPar:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Configuration_Transducer:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    TransducerAlphaX: float
    TransducerAlphaY: float
    TransducerAlphaZ: float
    TransducerCustomName: str
    TransducerMounting: str
    TransducerName: str
    TransducerOffsetX: float
    TransducerOffsetY: float
    TransducerOffsetZ: float
    TransducerSerialNumber: int
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Configuration_Transducer:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Configuration_Transducer:
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
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> XML_Configuration_Transducer:
        """
        return a copy using the c++ default copy constructor
        """
    def get_sensor_offsets(self) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    def HeadingQuickCalibration(self, arg: float) -> None:
        """
        < Seems to be used seldomly?
        """
class XML_Environment:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    Acidity: float
    Depth: float
    DropKeelOffset: float
    DropKeelOffsetIsManual: bool
    Latitude: float
    Salinity: float
    SoundSpeed: float
    SoundVelocitySource: str
    Temperature: float
    WaterLevelDraft: float
    WaterLevelDraftIsManual: bool
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Environment:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Environment:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def SoundVelocityProfile(self) -> list[float]:
        ...
    @SoundVelocityProfile.setter
    def SoundVelocityProfile(self, arg: collections.abc.Sequence[float]) -> None:
        ...
    @property
    def Transducers(self) -> list[XML_Environment_Transducer]:
        ...
    @Transducers.setter
    def Transducers(self, arg: collections.abc.Sequence[XML_Environment_Transducer]) -> None:
        ...
class XML_Environment_Transducer:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    SoundSpeed: float
    TransducerName: str
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Environment_Transducer:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Environment_Transducer:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_InitialParameter:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_InitialParameter:
        ...
    def __deepcopy__(self, arg: dict) -> XML_InitialParameter:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def Channels(self) -> ...:
        ...
    @Channels.setter
    def Channels(self, arg: ..., std: ...) -> None:
        ...
class XML_Node:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Node:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Node:
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
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def attributes(self) -> dict[str, str]:
        """
        attributes(self, key: str) -> str
        """
    def children(self) -> dict[str, list[XML_Node]]:
        """
        children(self, key: str) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Node]
        """
    def copy(self) -> XML_Node:
        """
        return a copy using the c++ default copy constructor
        """
    def first_child(self, arg: str) -> XML_Node:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def name(self) -> str:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Parameter:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Parameter:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    def Channels(self, arg: collections.abc.Sequence[XML_Parameter_Channel]) -> None:
        ...
class XML_Parameter_Channel:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    ChannelID: str
    ChannelMode: int
    SampleInterval: float
    Slope: float
    SoundVelocity: float
    TransmitPower: float
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Parameter_Channel:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Parameter_Channel:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def get_tx_signal_parameters(self) -> ...:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    def BandWidth(self, arg: float) -> None:
        """
        < TODO: when is this one used
        """
    @property
    def Frequency(self) -> float:
        """
        < used for cv ( PulseForm == 0)
        """
    @Frequency.setter
    def Frequency(self, arg: float) -> None:
        """
        < used for cv ( PulseForm == 0)
        """
    @property
    def FrequencyEnd(self) -> float:
        """
        < used used for chirp pulse (PulseForm > 0)
        """
    @FrequencyEnd.setter
    def FrequencyEnd(self, arg: float) -> None:
        """
        < used used for chirp pulse (PulseForm > 0)
        """
    @property
    def FrequencyStart(self) -> float:
        """
        < used used for chirp pulse (PulseForm > 0)
        """
    @FrequencyStart.setter
    def FrequencyStart(self, arg: float) -> None:
        """
        < used used for chirp pulse (PulseForm > 0)
        """
    @property
    def PulseDuration(self) -> float:
        """
        < used for cv ( PulseForm == 0)
        """
    @PulseDuration.setter
    def PulseDuration(self, arg: float) -> None:
        """
        < used for cv ( PulseForm == 0)
        """
    @property
    def PulseForm(self) -> int:
        """
        < 0 means cw, ?1 means chirp?
        """
    @PulseForm.setter
    def PulseForm(self, arg: int) -> None:
        """
        < 0 means cw, ?1 means chirp?
        """
    @property
    def PulseLength(self) -> float:
        """
        < used for chirp pulse (PulseForm > 0)
        """
    @PulseLength.setter
    def PulseLength(self, arg: float) -> None:
        """
        < used for chirp pulse (PulseForm > 0)
        """
    @property
    def TransducerDepth(self) -> float:
        """
        < when is this one used? only old format?
        """
    @TransducerDepth.setter
    def TransducerDepth(self, arg: float) -> None:
        """
        < when is this one used? only old format?
        """
class XML_PingSequence:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_PingSequence:
        ...
    def __deepcopy__(self, arg: dict) -> XML_PingSequence:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    def Pings(self, arg: collections.abc.Sequence[XML_PingSequence_Ping]) -> None:
        ...
class XML_PingSequence_Ping:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    ChannelID: str
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_PingSequence_Ping:
        ...
    def __deepcopy__(self, arg: dict) -> XML_PingSequence_Ping:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Sensor:
    """
    XML base datagram
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    IsManual: bool
    ManualValue: float
    Type: str
    unknown_attributes: int
    unknown_children: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XML_Sensor:
        ...
    def __deepcopy__(self, arg: dict) -> XML_Sensor:
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
    def __setstate__(self, arg: bytes) -> None:
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class t_BeamType(enum.Enum):
    """
    """
    BeamTypeRef: typing.ClassVar[t_BeamType]  # value = t_BeamType.BeamTypeRef
    BeamTypeRefB: typing.ClassVar[t_BeamType]  # value = t_BeamType.BeamTypeRefB
    BeamTypeSingle: typing.ClassVar[t_BeamType]  # value = t_BeamType.BeamTypeSingle
    BeamTypeSplit: typing.ClassVar[t_BeamType]  # value = t_BeamType.BeamTypeSplit
    BeamTypeSplit2: typing.ClassVar[t_BeamType]  # value = t_BeamType.BeamTypeSplit2
    BeamTypeSplit3: typing.ClassVar[t_BeamType]  # value = t_BeamType.BeamTypeSplit3
    BeamTypeSplit3C: typing.ClassVar[t_BeamType]  # value = t_BeamType.BeamTypeSplit3C
    BeamTypeSplit3CN: typing.ClassVar[t_BeamType]  # value = t_BeamType.BeamTypeSplit3CN
    BeamTypeSplit3CW: typing.ClassVar[t_BeamType]  # value = t_BeamType.BeamTypeSplit3CW
BeamTypeRef: t_BeamType  # value = t_BeamType.BeamTypeRef
BeamTypeRefB: t_BeamType  # value = t_BeamType.BeamTypeRefB
BeamTypeSingle: t_BeamType  # value = t_BeamType.BeamTypeSingle
BeamTypeSplit: t_BeamType  # value = t_BeamType.BeamTypeSplit
BeamTypeSplit2: t_BeamType  # value = t_BeamType.BeamTypeSplit2
BeamTypeSplit3: t_BeamType  # value = t_BeamType.BeamTypeSplit3
BeamTypeSplit3C: t_BeamType  # value = t_BeamType.BeamTypeSplit3C
BeamTypeSplit3CN: t_BeamType  # value = t_BeamType.BeamTypeSplit3CN
BeamTypeSplit3CW: t_BeamType  # value = t_BeamType.BeamTypeSplit3CW
