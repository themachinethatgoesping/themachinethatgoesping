"""Classes related to SimradRaw EK60 and EK80 data files"""

from collections.abc import Mapping, Sequence
import enum
from typing import overload

from . import (
    datagrams as datagrams,
    filedatacontainers as filedatacontainers,
    filedatainterfaces as filedatainterfaces,
    filedatatypes as filedatatypes
)
import themachinethatgoesping.tools_nanopy.progressbars


class t_SimradRawDatagramIdentifier(enum.Enum):
    """Datagram identifiers used in Simrad raw (EK60/EK80) files."""

    XML0 = 810306904
    """Unspecified (unknown) XML datagram"""

    FIL1 = 827083078
    """Filter datagram"""

    NME0 = 809848142
    """Unspecified (unknown) NMEA datagram"""

    MRU0 = 810897997
    """Motion datagram"""

    TAG0 = 809976148
    """Annotation datagram"""

    RAW3 = 861356370
    """Raw sample data datagram"""

class o_SimradRawDatagramIdentifier:
    """
    Helper class to convert between strings and enum values of type 't_SimradRawDatagramIdentifier'
    """

    @overload
    def __init__(self, value: t_SimradRawDatagramIdentifier = t_SimradRawDatagramIdentifier.XML0) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> t_SimradRawDatagramIdentifier:
        """enum value"""

    @value.setter
    def value(self, arg: t_SimradRawDatagramIdentifier, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_SimradRawDatagramIdentifier, /) -> bool: ...

    @overload
    def __eq__(self, arg: t_SimradRawDatagramIdentifier, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_SimradRawDatagramIdentifier:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_SimradRawDatagramIdentifier: ...

    def __deepcopy__(self, arg: dict, /) -> o_SimradRawDatagramIdentifier: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_SimradRawDatagramIdentifier:
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

@overload
def datagram_type_to_string(datagram_type: int) -> str:
    """
    Convert datagram type from simradraw_long to string representation.
    Args:
        value: Datagram type as simradraw_long.

    Returns:
        String representation (decimal) of the datagram type.
    """

@overload
def datagram_type_to_string(datagram_type: t_SimradRawDatagramIdentifier) -> str:
    """
    Convert datagram type identifier to string representation.
    Args:
        value: Datagram type identifier enum.

    Returns:
        String representation (decimal) of the datagram type.
    """

def SimradRawDatagram_type_from_string(datagram_type: str) -> int:
    """
    Parse datagram type from string representation.
    Args:
        value: String view containing decimal representation.

    Returns:
        Parsed datagram type numeric value.
    """

class SimradRawFileHandler_stream:
    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, mp_cores: int = 1) -> None: ...

    @overload
    def __init__(self, file_path: Sequence[str], index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def __init__(self, file_paths: Sequence[str], index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, mp_cores: int = 1) -> None: ...

    def get_index_paths(self) -> dict[str, str]: ...

    @overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, mp_cores: int = 1) -> None: ...

    @property
    def datagram_interface(self) -> filedatainterfaces.SimradRawDatagramInterface_stream: ...

    @property
    def datagramdata_interface(self) -> filedatainterfaces.SimradRawDatagramDataInterface_stream: ...

    @property
    def configuration_interface(self) -> filedatainterfaces.SimradRawConfigurationDataInterface_stream: ...

    @property
    def navigation_interface(self) -> filedatainterfaces.SimradRawNavigationDataInterface_stream: ...

    @property
    def environment_interface(self) -> filedatainterfaces.SimradRawEnvironmentDataInterface_stream: ...

    @property
    def ping_interface(self) -> filedatainterfaces.SimradRawPingDataInterface_stream: ...

    @property
    def otherfiledata_interface(self) -> filedatainterfaces.SimradRawOtherFileDataInterface_stream: ...

    def get_pings(self, sorted_by_time: bool = True) -> filedatacontainers.SimradRawPingContainer_stream: ...

    def get_channel_ids(self) -> list[str]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawFileHandler:
    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, mp_cores: int = 1) -> None: ...

    @overload
    def __init__(self, file_path: Sequence[str], index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def __init__(self, file_paths: Sequence[str], index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, mp_cores: int = 1) -> None: ...

    def get_index_paths(self) -> dict[str, str]: ...

    @overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, mp_cores: int = 1) -> None: ...

    @property
    def datagram_interface(self) -> filedatainterfaces.SimradRawDatagramInterface: ...

    @property
    def datagramdata_interface(self) -> filedatainterfaces.SimradRawDatagramDataInterface: ...

    @property
    def configuration_interface(self) -> filedatainterfaces.SimradRawConfigurationDataInterface: ...

    @property
    def navigation_interface(self) -> filedatainterfaces.SimradRawNavigationDataInterface: ...

    @property
    def environment_interface(self) -> filedatainterfaces.SimradRawEnvironmentDataInterface: ...

    @property
    def ping_interface(self) -> filedatainterfaces.SimradRawPingDataInterface: ...

    @property
    def otherfiledata_interface(self) -> filedatainterfaces.SimradRawOtherFileDataInterface: ...

    def get_pings(self, sorted_by_time: bool = True) -> filedatacontainers.SimradRawPingContainer: ...

    def get_channel_ids(self) -> list[str]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

def test_speed_raw(arg0: SimradRawFileHandler, arg1: t_SimradRawDatagramIdentifier, /) -> None: ...

def test_speed_type(arg0: SimradRawFileHandler, arg1: t_SimradRawDatagramIdentifier, /) -> None: ...

def test_speed_decode_nmea(arg: SimradRawFileHandler, /) -> None: ...

def test_speed_decode_xml(mapped_file_stream: SimradRawFileHandler, level: int = 10) -> None: ...

def test_speed_raw_all(arg: SimradRawFileHandler, /) -> None: ...

def test_speed_header(arg0: SimradRawFileHandler, arg1: t_SimradRawDatagramIdentifier, /) -> None: ...
