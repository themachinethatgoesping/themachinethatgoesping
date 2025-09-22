"""
Classes related to GSF data files
"""
from __future__ import annotations
import collections.abc
import themachinethatgoesping.tools_cppy.progressbars
import typing
__all__: list[str] = ['ATTITUDE', 'COMMENT', 'GSFDatagram_type_from_string', 'GSFFileHandler', 'GSFFileHandler_stream', 'HEADER', 'HISTORY', 'NAVIGATION_ERROR', 'PROCESSING_PARAMETERS', 'SENSOR_PARAMETERS', 'SINGLE_BEAM_SOUNDING', 'SOUND_VELOCITY_PROFILE', 'SWATH_BATHYMETRY', 'SWATH_BATHY_SUMMARY', 'datagram_type_to_string', 't_GSFDatagramIdentifier', 'unspecified']
class GSFFileHandler:
    """
    """
    @typing.overload
    def __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_paths: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
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
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @property
    def datagram_interface(self) -> ...:
        ...
class GSFFileHandler_stream:
    """
    """
    @typing.overload
    def __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_paths: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
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
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @property
    def datagram_interface(self) -> ...:
        ...
class t_GSFDatagramIdentifier:
    """
    
    
    Members:
    
      HEADER : 
    
      SWATH_BATHYMETRY : 
    
      SOUND_VELOCITY_PROFILE : 
    
      PROCESSING_PARAMETERS : 
    
      SENSOR_PARAMETERS : 
    
      COMMENT : 
    
      HISTORY : 
    
      NAVIGATION_ERROR : 
    
      SWATH_BATHY_SUMMARY : 
    
      SINGLE_BEAM_SOUNDING : 
    
      ATTITUDE : 
    
      unspecified : 
    """
    ATTITUDE: typing.ClassVar[t_GSFDatagramIdentifier]  # value = <t_GSFDatagramIdentifier.ATTITUDE: 12>
    COMMENT: typing.ClassVar[t_GSFDatagramIdentifier]  # value = <t_GSFDatagramIdentifier.COMMENT: 6>
    HEADER: typing.ClassVar[t_GSFDatagramIdentifier]  # value = <t_GSFDatagramIdentifier.HEADER: 1>
    HISTORY: typing.ClassVar[t_GSFDatagramIdentifier]  # value = <t_GSFDatagramIdentifier.HISTORY: 7>
    NAVIGATION_ERROR: typing.ClassVar[t_GSFDatagramIdentifier]  # value = <t_GSFDatagramIdentifier.NAVIGATION_ERROR: 8>
    PROCESSING_PARAMETERS: typing.ClassVar[t_GSFDatagramIdentifier]  # value = <t_GSFDatagramIdentifier.PROCESSING_PARAMETERS: 4>
    SENSOR_PARAMETERS: typing.ClassVar[t_GSFDatagramIdentifier]  # value = <t_GSFDatagramIdentifier.SENSOR_PARAMETERS: 5>
    SINGLE_BEAM_SOUNDING: typing.ClassVar[t_GSFDatagramIdentifier]  # value = <t_GSFDatagramIdentifier.SINGLE_BEAM_SOUNDING: 10>
    SOUND_VELOCITY_PROFILE: typing.ClassVar[t_GSFDatagramIdentifier]  # value = <t_GSFDatagramIdentifier.SOUND_VELOCITY_PROFILE: 3>
    SWATH_BATHYMETRY: typing.ClassVar[t_GSFDatagramIdentifier]  # value = <t_GSFDatagramIdentifier.SWATH_BATHYMETRY: 2>
    SWATH_BATHY_SUMMARY: typing.ClassVar[t_GSFDatagramIdentifier]  # value = <t_GSFDatagramIdentifier.SWATH_BATHY_SUMMARY: 9>
    __members__: typing.ClassVar[dict[str, t_GSFDatagramIdentifier]]  # value = {'HEADER': <t_GSFDatagramIdentifier.HEADER: 1>, 'SWATH_BATHYMETRY': <t_GSFDatagramIdentifier.SWATH_BATHYMETRY: 2>, 'SOUND_VELOCITY_PROFILE': <t_GSFDatagramIdentifier.SOUND_VELOCITY_PROFILE: 3>, 'PROCESSING_PARAMETERS': <t_GSFDatagramIdentifier.PROCESSING_PARAMETERS: 4>, 'SENSOR_PARAMETERS': <t_GSFDatagramIdentifier.SENSOR_PARAMETERS: 5>, 'COMMENT': <t_GSFDatagramIdentifier.COMMENT: 6>, 'HISTORY': <t_GSFDatagramIdentifier.HISTORY: 7>, 'NAVIGATION_ERROR': <t_GSFDatagramIdentifier.NAVIGATION_ERROR: 8>, 'SWATH_BATHY_SUMMARY': <t_GSFDatagramIdentifier.SWATH_BATHY_SUMMARY: 9>, 'SINGLE_BEAM_SOUNDING': <t_GSFDatagramIdentifier.SINGLE_BEAM_SOUNDING: 10>, 'ATTITUDE': <t_GSFDatagramIdentifier.ATTITUDE: 12>, 'unspecified': <t_GSFDatagramIdentifier.unspecified: 4294967295>}
    unspecified: typing.ClassVar[t_GSFDatagramIdentifier]  # value = <t_GSFDatagramIdentifier.unspecified: 4294967295>
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
def GSFDatagram_type_from_string(datagram_type: str) -> t_GSFDatagramIdentifier:
    ...
def datagram_type_to_string(datagram_type: t_GSFDatagramIdentifier) -> str:
    ...
ATTITUDE: t_GSFDatagramIdentifier  # value = <t_GSFDatagramIdentifier.ATTITUDE: 12>
COMMENT: t_GSFDatagramIdentifier  # value = <t_GSFDatagramIdentifier.COMMENT: 6>
HEADER: t_GSFDatagramIdentifier  # value = <t_GSFDatagramIdentifier.HEADER: 1>
HISTORY: t_GSFDatagramIdentifier  # value = <t_GSFDatagramIdentifier.HISTORY: 7>
NAVIGATION_ERROR: t_GSFDatagramIdentifier  # value = <t_GSFDatagramIdentifier.NAVIGATION_ERROR: 8>
PROCESSING_PARAMETERS: t_GSFDatagramIdentifier  # value = <t_GSFDatagramIdentifier.PROCESSING_PARAMETERS: 4>
SENSOR_PARAMETERS: t_GSFDatagramIdentifier  # value = <t_GSFDatagramIdentifier.SENSOR_PARAMETERS: 5>
SINGLE_BEAM_SOUNDING: t_GSFDatagramIdentifier  # value = <t_GSFDatagramIdentifier.SINGLE_BEAM_SOUNDING: 10>
SOUND_VELOCITY_PROFILE: t_GSFDatagramIdentifier  # value = <t_GSFDatagramIdentifier.SOUND_VELOCITY_PROFILE: 3>
SWATH_BATHYMETRY: t_GSFDatagramIdentifier  # value = <t_GSFDatagramIdentifier.SWATH_BATHYMETRY: 2>
SWATH_BATHY_SUMMARY: t_GSFDatagramIdentifier  # value = <t_GSFDatagramIdentifier.SWATH_BATHY_SUMMARY: 9>
unspecified: t_GSFDatagramIdentifier  # value = <t_GSFDatagramIdentifier.unspecified: 4294967295>
