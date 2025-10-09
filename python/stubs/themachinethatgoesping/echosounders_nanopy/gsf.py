"""
Classes related to GSF data files
"""
from __future__ import annotations
import collections.abc
import enum
import typing
__all__: list[str] = ['GSFDatagram_type_from_string', 'GSFFileHandler', 'GSFFileHandler_stream', 'datagram_type_to_string', 'o_GSFDatagramIdentifier', 't_GSFDatagramIdentifier']
class GSFFileHandler:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        """
        __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        __init__(self, file_path: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None
        __init__(self, file_paths: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def get_index_paths(self) -> dict[str, str]:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        """
        init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @property
    def datagram_interface(self) -> ...:
        ...
class GSFFileHandler_stream:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        """
        __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        __init__(self, file_path: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None
        __init__(self, file_paths: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def get_index_paths(self) -> dict[str, str]:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        """
        init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @property
    def datagram_interface(self) -> ...:
        ...
class o_GSFDatagramIdentifier:
    """
    Helper class to convert between strings and enum values of type 't_GSFDatagramIdentifier'
    """
    __default_value__: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.unspecified
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> o_GSFDatagramIdentifier:
        ...
    def __deepcopy__(self, arg: dict) -> o_GSFDatagramIdentifier:
        ...
    def __eq__(self, arg: o_GSFDatagramIdentifier) -> bool:
        """
        __eq__(self, arg: themachinethatgoesping.echosounders_nanopy.gsf.t_GSFDatagramIdentifier, /) -> bool
        __eq__(self, arg: int, /) -> bool
        __eq__(self, arg: str, /) -> bool
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, value: t_GSFDatagramIdentifier = ...) -> None:
        """
        __init__(self, value: str) -> None
        __init__(self, value: int) -> None
        
        Overloaded function.
        
        1. ``__init__(self, value: themachinethatgoesping.echosounders_nanopy.gsf.t_GSFDatagramIdentifier = t_GSFDatagramIdentifier.unspecified) -> None``
        
        Construct from enum value
        
        2. ``__init__(self, value: str) -> None``
        
        Construct from string
        
        3. ``__init__(self, value: int) -> None``
        
        Construct from string
        """
    def __repr__(self) -> str:
        """
        __repr__(self) -> None
        
        Overloaded function.
        
        1. ``__repr__(self) -> str``
        
        Return object information as string
        
        2. ``__repr__(self) -> None``
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        __str__(self) -> str
        
        Overloaded function.
        
        1. ``__str__(self) -> str``
        
        
        2. ``__str__(self) -> str``
        
        Return object information as string
        """
    def copy(self) -> o_GSFDatagramIdentifier:
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
    def value(self) -> t_GSFDatagramIdentifier:
        """
        enum value
        """
    @value.setter
    def value(self, arg: t_GSFDatagramIdentifier) -> None:
        """
        enum value
        """
class t_GSFDatagramIdentifier(enum.Enum):
    """
    """
    ATTITUDE: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.ATTITUDE
    COMMENT: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.COMMENT
    HEADER: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.HEADER
    HISTORY: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.HISTORY
    NAVIGATION_ERROR: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.NAVIGATION_ERROR
    PROCESSING_PARAMETERS: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.PROCESSING_PARAMETERS
    SENSOR_PARAMETERS: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.SENSOR_PARAMETERS
    SINGLE_BEAM_SOUNDING: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.SINGLE_BEAM_SOUNDING
    SOUND_VELOCITY_PROFILE: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.SOUND_VELOCITY_PROFILE
    SWATH_BATHYMETRY: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.SWATH_BATHYMETRY
    SWATH_BATHY_SUMMARY: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.SWATH_BATHY_SUMMARY
    unspecified: typing.ClassVar[t_GSFDatagramIdentifier]  # value = t_GSFDatagramIdentifier.unspecified
GSFDatagram_type_from_string: nanobind.nb_func  # value = <nanobind.nb_func object>
datagram_type_to_string: nanobind.nb_func  # value = <nanobind.nb_func object>
