"""SimradRaw EK80 XML datagram classes (subtypes of XML0)"""

from collections.abc import Mapping, Sequence
import enum
from typing import overload

import themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures
import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.navigation_nanopy.datastructures


class t_BeamType(enum.Enum):
    BeamTypeSingle = 0

    BeamTypeSplit = 1

    BeamTypeRef = 2

    BeamTypeRefB = 4

    BeamTypeSplit3 = 17

    BeamTypeSplit2 = 33

    BeamTypeSplit3C = 49

    BeamTypeSplit3CN = 65

    BeamTypeSplit3CW = 81

BeamTypeSingle: t_BeamType = t_BeamType.BeamTypeSingle

BeamTypeSplit: t_BeamType = t_BeamType.BeamTypeSplit

BeamTypeRef: t_BeamType = t_BeamType.BeamTypeRef

BeamTypeRefB: t_BeamType = t_BeamType.BeamTypeRefB

BeamTypeSplit3: t_BeamType = t_BeamType.BeamTypeSplit3

BeamTypeSplit2: t_BeamType = t_BeamType.BeamTypeSplit2

BeamTypeSplit3C: t_BeamType = t_BeamType.BeamTypeSplit3C

BeamTypeSplit3CN: t_BeamType = t_BeamType.BeamTypeSplit3CN

BeamTypeSplit3CW: t_BeamType = t_BeamType.BeamTypeSplit3CW

class XML_Node:
    """XML base datagram"""

    def __init__(self) -> None: ...

    def name(self) -> str: ...

    @overload
    def children(self) -> dict[str, list[XML_Node]]: ...

    @overload
    def children(self, key: str) -> list[XML_Node]: ...

    def first_child(self, arg: str, /) -> XML_Node: ...

    @overload
    def attributes(self) -> dict[str, str]: ...

    @overload
    def attributes(self, key: str) -> str: ...

    def copy(self) -> XML_Node:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Node: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Node: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Node:
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

class XML_Parameter_Channel:
    """XML base datagram"""

    def __init__(self) -> None: ...

    @property
    def ChannelID(self) -> str: ...

    @ChannelID.setter
    def ChannelID(self, arg: str, /) -> None: ...

    @property
    def ChannelMode(self) -> int: ...

    @ChannelMode.setter
    def ChannelMode(self, arg: int, /) -> None: ...

    @property
    def PulseForm(self) -> int:
        """0 means cw, ?1 means chirp?"""

    @PulseForm.setter
    def PulseForm(self, arg: int, /) -> None: ...

    @property
    def FrequencyStart(self) -> float:
        """used used for chirp pulse (PulseForm > 0)"""

    @FrequencyStart.setter
    def FrequencyStart(self, arg: float, /) -> None: ...

    @property
    def FrequencyEnd(self) -> float:
        """used used for chirp pulse (PulseForm > 0)"""

    @FrequencyEnd.setter
    def FrequencyEnd(self, arg: float, /) -> None: ...

    @property
    def BandWidth(self) -> float:
        """TODO: when is this one used"""

    @BandWidth.setter
    def BandWidth(self, arg: float, /) -> None: ...

    @property
    def Frequency(self) -> float:
        """used for cv ( PulseForm == 0)"""

    @Frequency.setter
    def Frequency(self, arg: float, /) -> None: ...

    @property
    def PulseDuration(self) -> float:
        """used for cv ( PulseForm == 0)"""

    @PulseDuration.setter
    def PulseDuration(self, arg: float, /) -> None: ...

    @property
    def PulseLength(self) -> float:
        """used for chirp pulse (PulseForm > 0)"""

    @PulseLength.setter
    def PulseLength(self, arg: float, /) -> None: ...

    @property
    def SampleInterval(self) -> float: ...

    @SampleInterval.setter
    def SampleInterval(self, arg: float, /) -> None: ...

    @property
    def TransducerDepth(self) -> float:
        """when is this one used? only old format?"""

    @TransducerDepth.setter
    def TransducerDepth(self, arg: float, /) -> None: ...

    @property
    def TransmitPower(self) -> float: ...

    @TransmitPower.setter
    def TransmitPower(self, arg: float, /) -> None: ...

    @property
    def Slope(self) -> float: ...

    @Slope.setter
    def Slope(self, arg: float, /) -> None: ...

    @property
    def SoundVelocity(self) -> float: ...

    @SoundVelocity.setter
    def SoundVelocity(self, arg: float, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def get_pulse_duration(self) -> float: ...

    def get_pulse_form_is_cw(self) -> bool: ...

    def get_pulse_form_is_fm(self) -> bool: ...

    def get_tx_signal_parameters(self) -> themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.CWSignalParameters | themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.FMSignalParameters | themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.GenericSignalParameters: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_Parameter_Channel:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Parameter_Channel: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Parameter_Channel: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Parameter_Channel:
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

class XML_Parameter:
    """XML base datagram"""

    def __init__(self) -> None: ...

    @property
    def Channels(self) -> list[XML_Parameter_Channel]: ...

    @Channels.setter
    def Channels(self, arg: Sequence[XML_Parameter_Channel], /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_Parameter:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Parameter: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Parameter: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Parameter:
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

class XML_InitialParameter:
    """XML base datagram"""

    def __init__(self) -> None: ...

    @property
    def Channels(self) -> list[XML_Parameter_Channel]: ...

    @Channels.setter
    def Channels(self, arg: Sequence[XML_Parameter_Channel], /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_InitialParameter:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_InitialParameter: ...

    def __deepcopy__(self, arg: dict, /) -> XML_InitialParameter: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_InitialParameter:
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

class XML_PingSequence_Ping:
    """XML base datagram"""

    def __init__(self) -> None: ...

    @property
    def ChannelID(self) -> str: ...

    @ChannelID.setter
    def ChannelID(self, arg: str, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_PingSequence_Ping:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_PingSequence_Ping: ...

    def __deepcopy__(self, arg: dict, /) -> XML_PingSequence_Ping: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_PingSequence_Ping:
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

class XML_PingSequence:
    """XML base datagram"""

    def __init__(self) -> None: ...

    @property
    def Pings(self) -> list[XML_PingSequence_Ping]: ...

    @Pings.setter
    def Pings(self, arg: Sequence[XML_PingSequence_Ping], /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_PingSequence:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_PingSequence: ...

    def __deepcopy__(self, arg: dict, /) -> XML_PingSequence: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_PingSequence:
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

class XML_Environment_Transducer:
    """XML base datagram"""

    def __init__(self) -> None: ...

    @property
    def SoundSpeed(self) -> float: ...

    @SoundSpeed.setter
    def SoundSpeed(self, arg: float, /) -> None: ...

    @property
    def TransducerName(self) -> str: ...

    @TransducerName.setter
    def TransducerName(self, arg: str, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_Environment_Transducer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Environment_Transducer: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Environment_Transducer: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Environment_Transducer:
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

class XML_Environment:
    """XML base datagram"""

    def __init__(self) -> None: ...

    @property
    def Transducers(self) -> list[XML_Environment_Transducer]: ...

    @Transducers.setter
    def Transducers(self, arg: Sequence[XML_Environment_Transducer], /) -> None: ...

    @property
    def WaterLevelDraft(self) -> float: ...

    @WaterLevelDraft.setter
    def WaterLevelDraft(self, arg: float, /) -> None: ...

    @property
    def DropKeelOffsetIsManual(self) -> bool: ...

    @DropKeelOffsetIsManual.setter
    def DropKeelOffsetIsManual(self, arg: bool, /) -> None: ...

    @property
    def DropKeelOffset(self) -> float: ...

    @DropKeelOffset.setter
    def DropKeelOffset(self, arg: float, /) -> None: ...

    @property
    def SoundVelocityProfile(self) -> list[float]: ...

    @SoundVelocityProfile.setter
    def SoundVelocityProfile(self, arg: Sequence[float], /) -> None: ...

    @property
    def WaterLevelDraftIsManual(self) -> bool: ...

    @WaterLevelDraftIsManual.setter
    def WaterLevelDraftIsManual(self, arg: bool, /) -> None: ...

    @property
    def Latitude(self) -> float: ...

    @Latitude.setter
    def Latitude(self, arg: float, /) -> None: ...

    @property
    def SoundSpeed(self) -> float: ...

    @SoundSpeed.setter
    def SoundSpeed(self, arg: float, /) -> None: ...

    @property
    def Salinity(self) -> float: ...

    @Salinity.setter
    def Salinity(self, arg: float, /) -> None: ...

    @property
    def SoundVelocitySource(self) -> str: ...

    @SoundVelocitySource.setter
    def SoundVelocitySource(self, arg: str, /) -> None: ...

    @property
    def Acidity(self) -> float: ...

    @Acidity.setter
    def Acidity(self, arg: float, /) -> None: ...

    @property
    def Temperature(self) -> float: ...

    @Temperature.setter
    def Temperature(self, arg: float, /) -> None: ...

    @property
    def Depth(self) -> float: ...

    @Depth.setter
    def Depth(self, arg: float, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_Environment:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Environment: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Environment: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Environment:
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

class XML_Sensor:
    """XML base datagram"""

    def __init__(self) -> None: ...

    @property
    def IsManual(self) -> bool: ...

    @IsManual.setter
    def IsManual(self, arg: bool, /) -> None: ...

    @property
    def ManualValue(self) -> float: ...

    @ManualValue.setter
    def ManualValue(self, arg: float, /) -> None: ...

    @property
    def Type(self) -> str: ...

    @Type.setter
    def Type(self, arg: str, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_Sensor:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Sensor: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Sensor: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Sensor:
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

class XML_Configuration_Sensor_TelegramValue:
    """XML Configuration Sensor Telegram Value (single <Value> node)."""

    def __init__(self) -> None: ...

    @property
    def Priority(self) -> int: ...

    @Priority.setter
    def Priority(self, arg: int, /) -> None: ...

    @property
    def Name(self) -> str: ...

    @Name.setter
    def Name(self, arg: str, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool:
        """Returns true if no unknown children/attributes were encountered."""

    def copy(self) -> XML_Configuration_Sensor_TelegramValue:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Configuration_Sensor_TelegramValue: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Configuration_Sensor_TelegramValue: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Sensor_TelegramValue:
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

class XML_Configuration_Sensor_Telegram:
    """XML Configuration Sensor Telegram (single <Telegram> node)."""

    def __init__(self) -> None: ...

    @property
    def Values(self) -> list[XML_Configuration_Sensor_TelegramValue]: ...

    @Values.setter
    def Values(self, arg: Sequence[XML_Configuration_Sensor_TelegramValue], /) -> None: ...

    @property
    def Enabled(self) -> bool: ...

    @Enabled.setter
    def Enabled(self, arg: bool, /) -> None: ...

    @property
    def SubscriptionPath(self) -> str: ...

    @SubscriptionPath.setter
    def SubscriptionPath(self, arg: str, /) -> None: ...

    @property
    def Type(self) -> str: ...

    @Type.setter
    def Type(self, arg: str, /) -> None: ...

    @property
    def Name(self) -> str: ...

    @Name.setter
    def Name(self, arg: str, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool:
        """Returns true if no unknown children/attributes were encountered."""

    def copy(self) -> XML_Configuration_Sensor_Telegram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Configuration_Sensor_Telegram: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Configuration_Sensor_Telegram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Sensor_Telegram:
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

class XML_Configuration_Sensor:
    """XML base datagram"""

    def __init__(self) -> None: ...

    def get_sensor_offsets(self) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
        """
        Return the sensor offsets as
        navigation::datastructures::PositionalOffsets structure

        Returns:
            navigation::datastructures::PositionalOffsets
        """

    @property
    def Telegrams(self) -> list[XML_Configuration_Sensor_Telegram]: ...

    @Telegrams.setter
    def Telegrams(self, arg: Sequence[XML_Configuration_Sensor_Telegram], /) -> None: ...

    @property
    def Timeout(self) -> float: ...

    @Timeout.setter
    def Timeout(self, arg: float, /) -> None: ...

    @property
    def Unique(self) -> int: ...

    @Unique.setter
    def Unique(self, arg: int, /) -> None: ...

    @property
    def AngleZ(self) -> float: ...

    @AngleZ.setter
    def AngleZ(self, arg: float, /) -> None: ...

    @property
    def AngleY(self) -> float: ...

    @AngleY.setter
    def AngleY(self, arg: float, /) -> None: ...

    @property
    def AngleX(self) -> float: ...

    @AngleX.setter
    def AngleX(self, arg: float, /) -> None: ...

    @property
    def X(self) -> float: ...

    @X.setter
    def X(self, arg: float, /) -> None: ...

    @property
    def Y(self) -> float: ...

    @Y.setter
    def Y(self, arg: float, /) -> None: ...

    @property
    def Z(self) -> float: ...

    @Z.setter
    def Z(self, arg: float, /) -> None: ...

    @property
    def Port(self) -> str: ...

    @Port.setter
    def Port(self, arg: str, /) -> None: ...

    @property
    def Type(self) -> str: ...

    @Type.setter
    def Type(self, arg: str, /) -> None: ...

    @property
    def Name(self) -> str: ...

    @Name.setter
    def Name(self, arg: str, /) -> None: ...

    @property
    def TalkerID(self) -> str: ...

    @TalkerID.setter
    def TalkerID(self, arg: str, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_Configuration_Sensor:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Configuration_Sensor: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Configuration_Sensor: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Sensor:
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

class XML_Configuration_Transducer:
    """XML base datagram"""

    def __init__(self) -> None: ...

    def get_sensor_offsets(self) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
        """
        Return the offsets as navigation::datastructures::PositionalOffsets
        structure

        Returns:
            navigation::datastructures::PositionalOffsets
        """

    @property
    def TransducerAlphaX(self) -> float: ...

    @TransducerAlphaX.setter
    def TransducerAlphaX(self, arg: float, /) -> None: ...

    @property
    def TransducerAlphaY(self) -> float: ...

    @TransducerAlphaY.setter
    def TransducerAlphaY(self, arg: float, /) -> None: ...

    @property
    def TransducerAlphaZ(self) -> float: ...

    @TransducerAlphaZ.setter
    def TransducerAlphaZ(self, arg: float, /) -> None: ...

    @property
    def TransducerOffsetX(self) -> float: ...

    @TransducerOffsetX.setter
    def TransducerOffsetX(self, arg: float, /) -> None: ...

    @property
    def TransducerOffsetY(self) -> float: ...

    @TransducerOffsetY.setter
    def TransducerOffsetY(self, arg: float, /) -> None: ...

    @property
    def TransducerOffsetZ(self) -> float: ...

    @TransducerOffsetZ.setter
    def TransducerOffsetZ(self, arg: float, /) -> None: ...

    @property
    def HeadingQuickCalibration(self) -> float:
        """Seems to be used seldomly?"""

    @HeadingQuickCalibration.setter
    def HeadingQuickCalibration(self, arg: float, /) -> None: ...

    @property
    def TransducerSerialNumber(self) -> int: ...

    @TransducerSerialNumber.setter
    def TransducerSerialNumber(self, arg: int, /) -> None: ...

    @property
    def TransducerMounting(self) -> str: ...

    @TransducerMounting.setter
    def TransducerMounting(self, arg: str, /) -> None: ...

    @property
    def TransducerName(self) -> str: ...

    @TransducerName.setter
    def TransducerName(self, arg: str, /) -> None: ...

    @property
    def TransducerCustomName(self) -> str: ...

    @TransducerCustomName.setter
    def TransducerCustomName(self, arg: str, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_Configuration_Transducer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Configuration_Transducer: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Configuration_Transducer: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transducer:
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

class XMLConfigurationActivePingMode:
    """XML base datagram"""

    def __init__(self) -> None: ...

    @property
    def Mode(self) -> str: ...

    @Mode.setter
    def Mode(self, arg: str, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XMLConfigurationActivePingMode:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XMLConfigurationActivePingMode: ...

    def __deepcopy__(self, arg: dict, /) -> XMLConfigurationActivePingMode: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XMLConfigurationActivePingMode:
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

class XML_Configuration_Transceiver_Channel_FrequencyPar:
    """XML base datagram"""

    def __init__(self) -> None: ...

    @property
    def Frequency(self) -> float: ...

    @Frequency.setter
    def Frequency(self, arg: float, /) -> None: ...

    @property
    def Gain(self) -> float: ...

    @Gain.setter
    def Gain(self, arg: float, /) -> None: ...

    @property
    def Impedance(self) -> float: ...

    @Impedance.setter
    def Impedance(self, arg: float, /) -> None: ...

    @property
    def Phase(self) -> float: ...

    @Phase.setter
    def Phase(self, arg: float, /) -> None: ...

    @property
    def BeamWidthAlongship(self) -> float: ...

    @BeamWidthAlongship.setter
    def BeamWidthAlongship(self, arg: float, /) -> None: ...

    @property
    def BeamWidthAthwartship(self) -> float: ...

    @BeamWidthAthwartship.setter
    def BeamWidthAthwartship(self, arg: float, /) -> None: ...

    @property
    def AngleOffsetAlongship(self) -> float: ...

    @AngleOffsetAlongship.setter
    def AngleOffsetAlongship(self, arg: float, /) -> None: ...

    @property
    def AngleOffsetAthwartship(self) -> float: ...

    @AngleOffsetAthwartship.setter
    def AngleOffsetAthwartship(self, arg: float, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_Configuration_Transceiver_Channel_FrequencyPar:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Configuration_Transceiver_Channel_FrequencyPar: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Configuration_Transceiver_Channel_FrequencyPar: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transceiver_Channel_FrequencyPar:
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

class XMLConfigurationTransceiverChannelTransducer:
    """XML base datagram"""

    def __init__(self) -> None: ...

    @property
    def FrequencyPars(self) -> list[XML_Configuration_Transceiver_Channel_FrequencyPar]: ...

    @FrequencyPars.setter
    def FrequencyPars(self, arg: Sequence[XML_Configuration_Transceiver_Channel_FrequencyPar], /) -> None: ...

    @property
    def TransducerName(self) -> str: ...

    @TransducerName.setter
    def TransducerName(self, arg: str, /) -> None: ...

    @property
    def ArticleNumber(self) -> str: ...

    @ArticleNumber.setter
    def ArticleNumber(self, arg: str, /) -> None: ...

    @property
    def Gain(self) -> list[float]: ...

    @Gain.setter
    def Gain(self, arg: Sequence[float], /) -> None: ...

    @property
    def SaCorrection(self) -> list[float]: ...

    @SaCorrection.setter
    def SaCorrection(self, arg: Sequence[float], /) -> None: ...

    @property
    def SerialNumber(self) -> int: ...

    @SerialNumber.setter
    def SerialNumber(self, arg: int, /) -> None: ...

    @property
    def BeamType(self) -> t_BeamType: ...

    @BeamType.setter
    def BeamType(self, arg: t_BeamType, /) -> None: ...

    @property
    def Frequency(self) -> float: ...

    @Frequency.setter
    def Frequency(self, arg: float, /) -> None: ...

    @property
    def FrequencyMinimum(self) -> float: ...

    @FrequencyMinimum.setter
    def FrequencyMinimum(self, arg: float, /) -> None: ...

    @property
    def FrequencyMaximum(self) -> float: ...

    @FrequencyMaximum.setter
    def FrequencyMaximum(self, arg: float, /) -> None: ...

    @property
    def EquivalentBeamAngle(self) -> float: ...

    @EquivalentBeamAngle.setter
    def EquivalentBeamAngle(self, arg: float, /) -> None: ...

    @property
    def MaxTxPowerTransducer(self) -> float: ...

    @MaxTxPowerTransducer.setter
    def MaxTxPowerTransducer(self, arg: float, /) -> None: ...

    @property
    def BeamWidthAlongship(self) -> float: ...

    @BeamWidthAlongship.setter
    def BeamWidthAlongship(self, arg: float, /) -> None: ...

    @property
    def BeamWidthAthwartship(self) -> float: ...

    @BeamWidthAthwartship.setter
    def BeamWidthAthwartship(self, arg: float, /) -> None: ...

    @property
    def AngleSensitivityAlongship(self) -> float: ...

    @AngleSensitivityAlongship.setter
    def AngleSensitivityAlongship(self, arg: float, /) -> None: ...

    @property
    def AngleSensitivityAthwartship(self) -> float: ...

    @AngleSensitivityAthwartship.setter
    def AngleSensitivityAthwartship(self, arg: float, /) -> None: ...

    @property
    def AngleOffsetAlongship(self) -> float: ...

    @AngleOffsetAlongship.setter
    def AngleOffsetAlongship(self, arg: float, /) -> None: ...

    @property
    def AngleOffsetAthwartship(self) -> float: ...

    @AngleOffsetAthwartship.setter
    def AngleOffsetAthwartship(self, arg: float, /) -> None: ...

    @property
    def DirectivityDropAt2XBeamWidth(self) -> float: ...

    @DirectivityDropAt2XBeamWidth.setter
    def DirectivityDropAt2XBeamWidth(self, arg: float, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XMLConfigurationTransceiverChannelTransducer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XMLConfigurationTransceiverChannelTransducer: ...

    def __deepcopy__(self, arg: dict, /) -> XMLConfigurationTransceiverChannelTransducer: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XMLConfigurationTransceiverChannelTransducer:
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

class XML_Configuration_Transceiver_Channel:
    """XML base datagram"""

    def __init__(self) -> None: ...

    def get_pulse_durations(self, fm: bool) -> list[float]: ...

    @property
    def Transducer(self) -> XMLConfigurationTransceiverChannelTransducer: ...

    @Transducer.setter
    def Transducer(self, arg: XMLConfigurationTransceiverChannelTransducer, /) -> None: ...

    @property
    def ChannelID(self) -> str: ...

    @ChannelID.setter
    def ChannelID(self, arg: str, /) -> None: ...

    @property
    def LogicalChannelID(self) -> str: ...

    @LogicalChannelID.setter
    def LogicalChannelID(self, arg: str, /) -> None: ...

    @property
    def ChannelIdShort(self) -> str: ...

    @ChannelIdShort.setter
    def ChannelIdShort(self, arg: str, /) -> None: ...

    @property
    def PulseLength(self) -> list[float]: ...

    @PulseLength.setter
    def PulseLength(self, arg: Sequence[float], /) -> None: ...

    @property
    def PulseDuration(self) -> list[float]: ...

    @PulseDuration.setter
    def PulseDuration(self, arg: Sequence[float], /) -> None: ...

    @property
    def PulseDurationFM(self) -> list[float]: ...

    @PulseDurationFM.setter
    def PulseDurationFM(self, arg: Sequence[float], /) -> None: ...

    @property
    def SampleInterval(self) -> list[float]: ...

    @SampleInterval.setter
    def SampleInterval(self, arg: Sequence[float], /) -> None: ...

    @property
    def MaxTxPowerTransceiver(self) -> float: ...

    @MaxTxPowerTransceiver.setter
    def MaxTxPowerTransceiver(self, arg: float, /) -> None: ...

    @property
    def HWChannelConfiguration(self) -> int: ...

    @HWChannelConfiguration.setter
    def HWChannelConfiguration(self, arg: int, /) -> None: ...

    @property
    def ChannelNumber(self) -> int: ...

    @ChannelNumber.setter
    def ChannelNumber(self, arg: int, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_Configuration_Transceiver_Channel:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Configuration_Transceiver_Channel: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Configuration_Transceiver_Channel: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transceiver_Channel:
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

class XML_Configuration_Transceiver:
    """XML base datagram"""

    def __init__(self) -> None: ...

    def get_transceiver_channel(self, channel_id: str) -> XML_Configuration_Transceiver_Channel: ...

    @property
    def Channels(self) -> list[XML_Configuration_Transceiver_Channel]: ...

    @Channels.setter
    def Channels(self, arg: Sequence[XML_Configuration_Transceiver_Channel], /) -> None: ...

    @property
    def TransceiverName(self) -> str: ...

    @TransceiverName.setter
    def TransceiverName(self, arg: str, /) -> None: ...

    @property
    def TransceiverType(self) -> str: ...

    @TransceiverType.setter
    def TransceiverType(self, arg: str, /) -> None: ...

    @property
    def MarketSegment(self) -> str: ...

    @MarketSegment.setter
    def MarketSegment(self, arg: str, /) -> None: ...

    @property
    def EthernetAddress(self) -> str: ...

    @EthernetAddress.setter
    def EthernetAddress(self, arg: str, /) -> None: ...

    @property
    def IPAddress(self) -> str: ...

    @IPAddress.setter
    def IPAddress(self, arg: str, /) -> None: ...

    @property
    def TransceiverSoftwareVersion(self) -> str: ...

    @TransceiverSoftwareVersion.setter
    def TransceiverSoftwareVersion(self, arg: str, /) -> None: ...

    @property
    def Version(self) -> str: ...

    @Version.setter
    def Version(self, arg: str, /) -> None: ...

    @property
    def Impedance(self) -> float: ...

    @Impedance.setter
    def Impedance(self, arg: float, /) -> None: ...

    @property
    def RxSampleFrequency(self) -> float: ...

    @RxSampleFrequency.setter
    def RxSampleFrequency(self, arg: float, /) -> None: ...

    @property
    def SerialNumber(self) -> int: ...

    @SerialNumber.setter
    def SerialNumber(self, arg: int, /) -> None: ...

    @property
    def TransceiverNumber(self) -> int: ...

    @TransceiverNumber.setter
    def TransceiverNumber(self, arg: int, /) -> None: ...

    @property
    def Multiplexing(self) -> int: ...

    @Multiplexing.setter
    def Multiplexing(self, arg: int, /) -> None: ...

    @property
    def unknown_children(self) -> int: ...

    @unknown_children.setter
    def unknown_children(self, arg: int, /) -> None: ...

    @property
    def unknown_attributes(self) -> int: ...

    @unknown_attributes.setter
    def unknown_attributes(self, arg: int, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_Configuration_Transceiver:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Configuration_Transceiver: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Configuration_Transceiver: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration_Transceiver:
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

class ChannelConfiguration:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, ChannelID: str, Channel: XML_Configuration_Transceiver_Channel, Transceiver: XML_Configuration_Transceiver, Transducer: XML_Configuration_Transducer) -> None: ...

    @property
    def ChannelID(self) -> str: ...

    @property
    def sensor_offsets(self) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets: ...

    @property
    def Channel(self) -> XML_Configuration_Transceiver_Channel: ...

    @property
    def Transceiver(self) -> XML_Configuration_Transceiver: ...

    @property
    def Transducer(self) -> XML_Configuration_Transducer: ...

    def copy(self) -> ChannelConfiguration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ChannelConfiguration: ...

    def __deepcopy__(self, arg: dict, /) -> ChannelConfiguration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ChannelConfiguration:
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

class XML_Configuration:
    """XML Configuration datagram structure."""

    def __init__(self) -> None: ...

    @property
    def ChannelConfigurations(self) -> dict[str, ChannelConfiguration]: ...

    @ChannelConfigurations.setter
    def ChannelConfigurations(self, arg: Mapping[str, ChannelConfiguration], /) -> None: ...

    @property
    def SensorConfigurations(self) -> dict[str, list[XML_Configuration_Sensor]]: ...

    @SensorConfigurations.setter
    def SensorConfigurations(self, arg: Mapping[str, Sequence[XML_Configuration_Sensor]], /) -> None: ...

    def get_transceiver(self, channel_id: str) -> XML_Configuration_Transceiver: ...

    def get_transceivers(self) -> dict[str, XML_Configuration_Transceiver]: ...

    def get_transceiver_channel(self, channel_id: str) -> XML_Configuration_Transceiver_Channel: ...

    def get_transceiver_channels(self) -> dict[str, XML_Configuration_Transceiver_Channel]: ...

    def get_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration: ...

    def get_prioritized_sensor(self, prio_values: Sequence[str]) -> XML_Configuration_Sensor: ...

    def get_sensors_sorted_by_priority(self, prio_values: Sequence[str]) -> list[XML_Configuration_Sensor]: ...

    @property
    def ConfiguredSensors(self) -> list[XML_Configuration_Sensor]: ...

    @ConfiguredSensors.setter
    def ConfiguredSensors(self, arg: Sequence[XML_Configuration_Sensor], /) -> None: ...

    @property
    def Transducers(self) -> list[XML_Configuration_Transducer]: ...

    @Transducers.setter
    def Transducers(self, arg: Sequence[XML_Configuration_Transducer], /) -> None: ...

    @property
    def Transceivers(self) -> list[XML_Configuration_Transceiver]: ...

    @Transceivers.setter
    def Transceivers(self, arg: Sequence[XML_Configuration_Transceiver], /) -> None: ...

    @property
    def ActivePingMode(self) -> XMLConfigurationActivePingMode: ...

    @ActivePingMode.setter
    def ActivePingMode(self, arg: XMLConfigurationActivePingMode, /) -> None: ...

    @property
    def FileFormatVersion(self) -> str: ...

    @FileFormatVersion.setter
    def FileFormatVersion(self, arg: str, /) -> None: ...

    @property
    def Version(self) -> str: ...

    @Version.setter
    def Version(self, arg: str, /) -> None: ...

    @property
    def TimeBias(self) -> str: ...

    @TimeBias.setter
    def TimeBias(self, arg: str, /) -> None: ...

    @property
    def ApplicationName(self) -> str: ...

    @ApplicationName.setter
    def ApplicationName(self, arg: str, /) -> None: ...

    @property
    def Copyright(self) -> str: ...

    @Copyright.setter
    def Copyright(self, arg: str, /) -> None: ...

    def parsed_completely(self) -> bool: ...

    def copy(self) -> XML_Configuration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XML_Configuration: ...

    def __deepcopy__(self, arg: dict, /) -> XML_Configuration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XML_Configuration:
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
