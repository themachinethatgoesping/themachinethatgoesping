"""Simrad EK80 XML datagram classes (subtypes of XML0)"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams
import typing

__all__ = [
    "XML_Configuration",
    "XML_Configuration_ActivePingMode",
    "XML_Configuration_Sensor",
    "XML_Configuration_Sensor_Telegram",
    "XML_Configuration_Sensor_TelegramValue",
    "XML_Configuration_Transducer",
    "XML_Environment",
    "XML_Environment_Transducer",
    "XML_InitialParameter",
    "XML_Node",
    "XML_Parameter_Channel",
    "XML_PingSequence",
    "XML_Sensor"
]


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
    def TimeBias(self) -> str:
        """
        :type: str
        """
    @TimeBias.setter
    def TimeBias(self, arg0: str) -> None:
        pass
    @property
    def Transceivers(self) -> typing.List[XML_Node]:
        """
        :type: typing.List[XML_Node]
        """
    @Transceivers.setter
    def Transceivers(self, arg0: typing.List[XML_Node]) -> None:
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
    def Transducer(self) -> XML_Environment_Transducer:
        """
        :type: XML_Environment_Transducer
        """
    @Transducer.setter
    def Transducer(self, arg0: XML_Environment_Transducer) -> None:
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
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
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
