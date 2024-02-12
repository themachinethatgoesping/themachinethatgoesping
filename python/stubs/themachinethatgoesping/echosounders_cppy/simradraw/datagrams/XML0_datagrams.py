"""
SimradRaw EK80 XML datagram classes (subtypes of XML0)
"""
from __future__ import annotations
import themachinethatgoesping.algorithms.signalprocessing.datastructures
import themachinethatgoesping.navigation
import themachinethatgoesping.navigation.datastructures
import typing
__all__ = ['BeamTypeRef', 'BeamTypeRefB', 'BeamTypeSingle', 'BeamTypeSplit', 'BeamTypeSplit2', 'BeamTypeSplit3', 'BeamTypeSplit3C', 'BeamTypeSplit3CN', 'BeamTypeSplit3CW', 'ChannelConfiguration', 'XMLConfigurationActivePingMode', 'XMLConfigurationTransceiverChannelTransducer', 'XML_Configuration', 'XML_Configuration_Sensor', 'XML_Configuration_Sensor_Telegram', 'XML_Configuration_Sensor_TelegramValue', 'XML_Configuration_Transceiver', 'XML_Configuration_Transceiver_Channel', 'XML_Configuration_Transceiver_Channel_FrequencyPar', 'XML_Configuration_Transducer', 'XML_Environment', 'XML_Environment_Transducer', 'XML_InitialParameter', 'XML_Node', 'XML_Parameter', 'XML_Parameter_Channel', 'XML_PingSequence', 'XML_PingSequence_Ping', 'XML_Sensor', 't_BeamType']
class ChannelConfiguration:
    """
    XML base datagram
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
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
    unknown_attributes: int
    unknown_children: int
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XMLConfigurationTransceiverChannelTransducer:
    """
    XML base datagram
    """
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
    FrequencyPars: list[XML_Configuration_Transceiver_Channel_FrequencyPar]
    Gain: list[float]
    MaxTxPowerTransducer: float
    SaCorrection: list[float]
    SerialNumber: int
    TransducerName: str
    unknown_attributes: int
    unknown_children: int
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Configuration:
    """
    XML base datagram
    """
    ActivePingMode: XMLConfigurationActivePingMode
    ApplicationName: str
    ChannelConfigurations: dict[str, ChannelConfiguration]
    ConfiguredSensors: list[XML_Configuration_Sensor]
    Copyright: str
    FileFormatVersion: str
    SensorConfigurations: dict[str, list[XML_Configuration_Sensor]]
    TimeBias: str
    Transceivers: list[XML_Configuration_Transceiver]
    Transducers: list[XML_Configuration_Transducer]
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
    def get_prioritized_sensor(self, prio_values: list[str]) -> XML_Configuration_Sensor:
        ...
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration:
        ...
    def get_sensors_sorted_by_priority(self, prio_values: list[str]) -> list[XML_Configuration_Sensor]:
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Configuration_Sensor:
    """
    XML base datagram
    """
    AngleX: float
    AngleY: float
    AngleZ: float
    Name: str
    Port: str
    TalkerID: str
    Telegrams: list[XML_Configuration_Sensor_Telegram]
    Timeout: float
    Type: str
    Unique: int
    X: float
    Y: float
    Z: float
    unknown_attributes: int
    unknown_children: int
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Configuration_Sensor_Telegram:
    """
    XML base datagram
    """
    Enabled: bool
    Name: str
    SubscriptionPath: str
    Type: str
    Values: list[XML_Configuration_Sensor_TelegramValue]
    unknown_attributes: int
    unknown_children: int
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Configuration_Sensor_TelegramValue:
    """
    XML base datagram
    """
    Name: str
    Priority: int
    unknown_attributes: int
    unknown_children: int
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Configuration_Transceiver:
    """
    XML base datagram
    """
    Channels: list[XML_Configuration_Transceiver_Channel]
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
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Configuration_Transceiver_Channel:
    """
    XML base datagram
    """
    ChannelID: str
    ChannelIdShort: str
    ChannelNumber: int
    HWChannelConfiguration: int
    LogicalChannelID: str
    MaxTxPowerTransceiver: float
    PulseDuration: list[float]
    PulseDurationFM: list[float]
    PulseLength: list[float]
    SampleInterval: list[float]
    Transducer: XMLConfigurationTransceiverChannelTransducer
    unknown_attributes: int
    unknown_children: int
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
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Configuration_Transceiver_Channel_FrequencyPar:
    """
    XML base datagram
    """
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Configuration_Transducer:
    """
    XML base datagram
    """
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
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
    def HeadingQuickCalibration(self, arg0: float) -> None:
        ...
class XML_Environment:
    """
    XML base datagram
    """
    Acidity: float
    Depth: float
    DropKeelOffset: float
    DropKeelOffsetIsManual: bool
    Latitude: float
    Salinity: float
    SoundSpeed: float
    SoundVelocityProfile: list[float]
    SoundVelocitySource: str
    Temperature: float
    Transducers: list[XML_Environment_Transducer]
    WaterLevelDraft: float
    WaterLevelDraftIsManual: bool
    unknown_attributes: int
    unknown_children: int
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Environment_Transducer:
    """
    XML base datagram
    """
    SoundSpeed: float
    TransducerName: str
    unknown_attributes: int
    unknown_children: int
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_InitialParameter:
    """
    XML base datagram
    """
    Channels: list[XML_Parameter_Channel]
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def name(self) -> str:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Parameter:
    """
    XML base datagram
    """
    Channels: list[XML_Parameter_Channel]
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Parameter_Channel:
    """
    XML base datagram
    """
    ChannelID: str
    ChannelMode: int
    SampleInterval: float
    Slope: float
    SoundVelocity: float
    TransmitPower: float
    unknown_attributes: int
    unknown_children: int
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
    def get_tx_signal_parameters(self) -> themachinethatgoesping.algorithms.signalprocessing.datastructures.CWSignalParameters | themachinethatgoesping.algorithms.signalprocessing.datastructures.FMSignalParameters | themachinethatgoesping.algorithms.signalprocessing.datastructures.GenericSignalParameters:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
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
    def BandWidth(self, arg0: float) -> None:
        ...
    @property
    def Frequency(self) -> float:
        """
        < used for cv ( PulseForm == 0)
        """
    @Frequency.setter
    def Frequency(self, arg0: float) -> None:
        ...
    @property
    def FrequencyEnd(self) -> float:
        """
        < used used for chirp pulse (PulseForm > 0)
        """
    @FrequencyEnd.setter
    def FrequencyEnd(self, arg0: float) -> None:
        ...
    @property
    def FrequencyStart(self) -> float:
        """
        < used used for chirp pulse (PulseForm > 0)
        """
    @FrequencyStart.setter
    def FrequencyStart(self, arg0: float) -> None:
        ...
    @property
    def PulseDuration(self) -> float:
        """
        < used for cv ( PulseForm == 0)
        """
    @PulseDuration.setter
    def PulseDuration(self, arg0: float) -> None:
        ...
    @property
    def PulseForm(self) -> int:
        """
        < 0 means cw, ?1 means chirp?
        """
    @PulseForm.setter
    def PulseForm(self, arg0: int) -> None:
        ...
    @property
    def PulseLength(self) -> float:
        """
        < used for chirp pulse (PulseForm > 0)
        """
    @PulseLength.setter
    def PulseLength(self, arg0: float) -> None:
        ...
    @property
    def TransducerDepth(self) -> float:
        """
        < when is this one used? only old format?
        """
    @TransducerDepth.setter
    def TransducerDepth(self, arg0: float) -> None:
        ...
class XML_PingSequence:
    """
    XML base datagram
    """
    Pings: list[XML_PingSequence_Ping]
    unknown_attributes: int
    unknown_children: int
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_PingSequence_Ping:
    """
    XML base datagram
    """
    ChannelID: str
    unknown_attributes: int
    unknown_children: int
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class XML_Sensor:
    """
    XML base datagram
    """
    IsManual: bool
    ManualValue: float
    Type: str
    unknown_attributes: int
    unknown_children: int
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def parsed_completely(self) -> bool:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
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
    def __init__(self, value: int) -> None:
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
    def __setstate__(self, state: int) -> None:
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
