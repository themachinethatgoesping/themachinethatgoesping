from collections.abc import Mapping, Sequence
import enum
from typing import overload

from . import (
    datagrams as datagrams,
    filedatacontainers as filedatacontainers,
    filedatainterfaces as filedatainterfaces,
    filetypes as filetypes
)
import themachinethatgoesping.tools_nanopy.progressbars


class t_KMALLDatagramIdentifier(enum.Enum):
    I_INSTALLATION_PARAM = 1346980131

    I_OP_RUNTIME = 1347373347

    S_POSITION = 1330664227

    S_POSITION_ERROR = 1162892067

    S_POSITION_DATUM = 1146114851

    S_KM_BINARY = 1296782115

    S_SOUND_VELOCITY_PROFILE = 1347834659

    S_SOUND_VELOCITY_TRANSDUCER = 1414943523

    S_CLOCK = 1279480611

    S_DEPTH = 1162105635

    S_HEIGHT = 1229476643

    M_RANGE_AND_DEPTH = 1515343139

    M_WATER_COLUMN = 1129794851

    C_POSITION = 1330660131

    KM_BINARY = 1112361763

class o_KMALLDatagramIdentifier:
    """
    Helper class to convert between strings and enum values of type 't_KMALLDatagramIdentifier'
    """

    @overload
    def __init__(self, value: t_KMALLDatagramIdentifier = t_KMALLDatagramIdentifier.I_INSTALLATION_PARAM) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> t_KMALLDatagramIdentifier:
        """enum value"""

    @value.setter
    def value(self, arg: t_KMALLDatagramIdentifier, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_KMALLDatagramIdentifier, /) -> bool: ...

    @overload
    def __eq__(self, arg: t_KMALLDatagramIdentifier, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_KMALLDatagramIdentifier:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_KMALLDatagramIdentifier: ...

    def __deepcopy__(self, arg: dict, /) -> o_KMALLDatagramIdentifier: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_KMALLDatagramIdentifier:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> None: ...

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class t_KMALLSystemTransducerConfiguration(enum.Enum):
    SingleTxSingleRx = 0
    """EM122, EM302, EM710, EM2040 Single"""

    SingleHead = 1
    """EM3002 Single Head, EM2040C Single Head"""

    DualHead = 2
    """EM3002 Dual Head, EM2040C Dual Head"""

    SingleTxDualRx = 3
    """EM2040 Dual RX"""

    DualTxDualRx = 4
    """EM2040 Dual TX"""

    PortableSingleHead = 5
    """EM2040P"""

    Modular = 6
    """EM2040M"""

    PortableMKIIHead = 7
    """EM2042P?"""

class o_KMALLSystemTransducerConfiguration:
    """
    Helper class to convert between strings and enum values of type 't_KMALLSystemTransducerConfiguration'
    """

    @overload
    def __init__(self, value: t_KMALLSystemTransducerConfiguration = t_KMALLSystemTransducerConfiguration.SingleTxSingleRx) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> t_KMALLSystemTransducerConfiguration:
        """enum value"""

    @value.setter
    def value(self, arg: t_KMALLSystemTransducerConfiguration, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLSystemTransducerConfiguration = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_KMALLSystemTransducerConfiguration, /) -> bool: ...

    @overload
    def __eq__(self, arg: t_KMALLSystemTransducerConfiguration, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_KMALLSystemTransducerConfiguration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_KMALLSystemTransducerConfiguration: ...

    def __deepcopy__(self, arg: dict, /) -> o_KMALLSystemTransducerConfiguration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_KMALLSystemTransducerConfiguration:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> None: ...

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

def datagram_type_to_string(datagram_type: t_KMALLDatagramIdentifier) -> str:
    """
    Convert datagram type from uint32_t to string representation.
    Args:
        value: Datagram type as uint32_t.

    Returns:
        String representation (decimal) of the datagram type.
    """

def KMALLDatagram_type_from_string(datagram_type: str) -> int:
    """
    Parse datagram type from string representation.
    Args:
        value: String view containing decimal representation.

    Returns:
        Parsed datagram type numeric value.
    """

class KMALLFileHandler_stream:
    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None: ...

    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None: ...

    @overload
    def __init__(self, file_path: Sequence[str], index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None: ...

    @overload
    def __init__(self, file_paths: Sequence[str], index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None: ...

    def get_index_paths(self) -> dict[str, str]: ...

    @overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None: ...

    @overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None: ...

    @property
    def datagram_interface(self) -> filedatainterfaces.KMALLDatagramInterface_stream: ...

    @property
    def datagramdata_interface(self) -> filedatainterfaces.KMALLDatagramDataInterface_stream: ...

    @property
    def configuration_interface(self) -> filedatainterfaces.KMALLConfigurationDataInterface_stream: ...

    @property
    def navigation_interface(self) -> filedatainterfaces.KMALLNavigationDataInterface_stream: ...

    @property
    def environment_interface(self) -> filedatainterfaces.KMALLEnvironmentDataInterface_stream: ...

    @property
    def otherfiledata_interface(self) -> filedatainterfaces.KMALLOtherFileDataInterface_stream: ...

    @property
    def ping_interface(self) -> filedatainterfaces.KMALLPingDataInterface_stream: ...

    def get_pings(self, sorted_by_time: bool = True) -> filedatacontainers.KMALLPingContainer_stream: ...

    def get_channel_ids(self) -> list[str]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLFileHandler:
    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None: ...

    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None: ...

    @overload
    def __init__(self, file_path: Sequence[str], index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None: ...

    @overload
    def __init__(self, file_paths: Sequence[str], index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None: ...

    def get_index_paths(self) -> dict[str, str]: ...

    @overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None: ...

    @overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None: ...

    @property
    def datagram_interface(self) -> filedatainterfaces.KMALLDatagramInterface: ...

    @property
    def datagramdata_interface(self) -> filedatainterfaces.KMALLDatagramDataInterface: ...

    @property
    def configuration_interface(self) -> filedatainterfaces.KMALLConfigurationDataInterface: ...

    @property
    def navigation_interface(self) -> filedatainterfaces.KMALLNavigationDataInterface: ...

    @property
    def environment_interface(self) -> filedatainterfaces.KMALLEnvironmentDataInterface: ...

    @property
    def otherfiledata_interface(self) -> filedatainterfaces.KMALLOtherFileDataInterface: ...

    @property
    def ping_interface(self) -> filedatainterfaces.KMALLPingDataInterface: ...

    def get_pings(self, sorted_by_time: bool = True) -> filedatacontainers.KMALLPingContainer: ...

    def get_channel_ids(self) -> list[str]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
