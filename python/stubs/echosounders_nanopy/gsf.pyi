"""Classes related to GSF data files"""

from collections.abc import Mapping, Sequence
import enum
from typing import overload

import themachinethatgoesping.tools_nanopy.progressbars


class t_GSFDatagramIdentifier(enum.Enum):
    HEADER = 1

    SWATH_BATHYMETRY = 2

    SOUND_VELOCITY_PROFILE = 3

    PROCESSING_PARAMETERS = 4

    SENSOR_PARAMETERS = 5

    COMMENT = 6

    HISTORY = 7

    NAVIGATION_ERROR = 8

    SWATH_BATHY_SUMMARY = 9

    SINGLE_BEAM_SOUNDING = 10

    ATTITUDE = 12

    unspecified = 4294967295

class o_GSFDatagramIdentifier:
    """
    Helper class to convert between strings and enum values of type 't_GSFDatagramIdentifier'
    """

    @overload
    def __init__(self, value: t_GSFDatagramIdentifier = t_GSFDatagramIdentifier.unspecified) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> t_GSFDatagramIdentifier:
        """enum value"""

    @value.setter
    def value(self, arg: t_GSFDatagramIdentifier, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.gsf.t_GSFDatagramIdentifier = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_GSFDatagramIdentifier, /) -> bool: ...

    @overload
    def __eq__(self, arg: t_GSFDatagramIdentifier, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_GSFDatagramIdentifier:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_GSFDatagramIdentifier: ...

    def __deepcopy__(self, arg: dict, /) -> o_GSFDatagramIdentifier: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_GSFDatagramIdentifier:
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

def datagram_type_to_string(datagram_type: t_GSFDatagramIdentifier) -> str: ...

def GSFDatagram_type_from_string(datagram_type: str) -> t_GSFDatagramIdentifier: ...

class GSFFileHandler_stream:
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
    def datagram_interface(self) -> "themachinethatgoesping::echosounders::gsf::filedatainterfaces::GSFDatagramInterface_std_basic_ifstream<char_std_char_traits<char > >": ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class GSFFileHandler:
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
    def datagram_interface(self) -> "themachinethatgoesping::echosounders::gsf::filedatainterfaces::GSFDatagramInterface_themachinethatgoesping_echosounders_filetemplates_datastreams_MappedFileStream": ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
