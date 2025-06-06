"""
Classes related to SimradRaw EK60 and EK80 data files
"""
from __future__ import annotations
import themachinethatgoesping.tools_cppy.progressbars
import typing
from . import datagrams
from . import filedatacontainers
from . import filedatainterfaces
from . import filetypes
__all__ = ['FIL1', 'MRU0', 'NME0', 'RAW3', 'SimradRawDatagram_type_from_string', 'SimradRawFileHandler', 'SimradRawFileHandler_stream', 'TAG0', 'XML0', 'datagram_type_to_string', 'datagrams', 'filedatacontainers', 'filedatainterfaces', 'filetypes', 't_SimradRawDatagramIdentifier', 'test_speed_decode_nmea', 'test_speed_decode_xml', 'test_speed_header', 'test_speed_raw', 'test_speed_raw_all', 'test_speed_type']
class SimradRawFileHandler:
    """
    """
    @typing.overload
    def __init__(self, file_path: str, index_paths: dict[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: str, index_paths: dict[str, str], init: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: list[str], index_paths: dict[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_paths: list[str], index_paths: dict[str, str], init: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def get_channel_ids(self) -> list[str]:
        ...
    def get_index_paths(self) -> dict[str, str]:
        ...
    def get_pings(self, sorted_by_time: bool = True) -> filedatacontainers.SimradRawPingContainer:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> filedatainterfaces.SimradRawAnnotationDataInterface:
        ...
    @property
    def configuration_interface(self) -> filedatainterfaces.SimradRawConfigurationDataInterface:
        ...
    @property
    def datagram_interface(self) -> filedatainterfaces.SimradRawDatagramInterface:
        ...
    @property
    def datagramdata_interface(self) -> filedatainterfaces.SimradRawDatagramDataInterface:
        ...
    @property
    def environment_interface(self) -> filedatainterfaces.SimradRawEnvironmentDataInterface:
        ...
    @property
    def navigation_interface(self) -> filedatainterfaces.SimradRawNavigationDataInterface:
        ...
    @property
    def otherfiledata_interface(self) -> filedatainterfaces.SimradRawOtherFileDataInterface:
        ...
    @property
    def ping_interface(self) -> filedatainterfaces.SimradRawPingDataInterface:
        ...
class SimradRawFileHandler_stream:
    """
    """
    @typing.overload
    def __init__(self, file_path: str, index_paths: dict[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: str, index_paths: dict[str, str], init: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: list[str], index_paths: dict[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_paths: list[str], index_paths: dict[str, str], init: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def get_channel_ids(self) -> list[str]:
        ...
    def get_index_paths(self) -> dict[str, str]:
        ...
    def get_pings(self, sorted_by_time: bool = True) -> filedatacontainers.SimradRawPingContainer_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> filedatainterfaces.SimradRawAnnotationDataInterface_stream:
        ...
    @property
    def configuration_interface(self) -> filedatainterfaces.SimradRawConfigurationDataInterface_stream:
        ...
    @property
    def datagram_interface(self) -> filedatainterfaces.SimradRawDatagramInterface_stream:
        ...
    @property
    def datagramdata_interface(self) -> filedatainterfaces.SimradRawDatagramDataInterface_stream:
        ...
    @property
    def environment_interface(self) -> filedatainterfaces.SimradRawEnvironmentDataInterface_stream:
        ...
    @property
    def navigation_interface(self) -> filedatainterfaces.SimradRawNavigationDataInterface_stream:
        ...
    @property
    def otherfiledata_interface(self) -> filedatainterfaces.SimradRawOtherFileDataInterface_stream:
        ...
    @property
    def ping_interface(self) -> filedatainterfaces.SimradRawPingDataInterface_stream:
        ...
class t_SimradRawDatagramIdentifier:
    """
    
    
    Members:
    
      XML0 : < Unspecified (unknown) XML datagram
    
      FIL1 : < Filter datagram
    
      NME0 : < Unspecified (unknown) NMEA datagram
    
      MRU0 : < Motion datagram
    
      TAG0 : < ???
    
      RAW3 : < Raw sample data datagram
    """
    FIL1: typing.ClassVar[t_SimradRawDatagramIdentifier]  # value = <t_SimradRawDatagramIdentifier.FIL1: 827083078>
    MRU0: typing.ClassVar[t_SimradRawDatagramIdentifier]  # value = <t_SimradRawDatagramIdentifier.MRU0: 810897997>
    NME0: typing.ClassVar[t_SimradRawDatagramIdentifier]  # value = <t_SimradRawDatagramIdentifier.NME0: 809848142>
    RAW3: typing.ClassVar[t_SimradRawDatagramIdentifier]  # value = <t_SimradRawDatagramIdentifier.RAW3: 861356370>
    TAG0: typing.ClassVar[t_SimradRawDatagramIdentifier]  # value = <t_SimradRawDatagramIdentifier.TAG0: 809976148>
    XML0: typing.ClassVar[t_SimradRawDatagramIdentifier]  # value = <t_SimradRawDatagramIdentifier.XML0: 810306904>
    __members__: typing.ClassVar[dict[str, t_SimradRawDatagramIdentifier]]  # value = {'XML0': <t_SimradRawDatagramIdentifier.XML0: 810306904>, 'FIL1': <t_SimradRawDatagramIdentifier.FIL1: 827083078>, 'NME0': <t_SimradRawDatagramIdentifier.NME0: 809848142>, 'MRU0': <t_SimradRawDatagramIdentifier.MRU0: 810897997>, 'TAG0': <t_SimradRawDatagramIdentifier.TAG0: 809976148>, 'RAW3': <t_SimradRawDatagramIdentifier.RAW3: 861356370>}
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
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
def SimradRawDatagram_type_from_string(datagram_type: str) -> int:
    ...
@typing.overload
def datagram_type_to_string(datagram_type: int) -> str:
    ...
@typing.overload
def datagram_type_to_string(datagram_type: t_SimradRawDatagramIdentifier) -> str:
    ...
def test_speed_decode_nmea(arg0: SimradRawFileHandler) -> None:
    ...
def test_speed_decode_xml(mapped_file_stream: SimradRawFileHandler, level: int = 10) -> None:
    ...
def test_speed_header(arg0: SimradRawFileHandler, arg1: t_SimradRawDatagramIdentifier) -> None:
    ...
def test_speed_raw(arg0: SimradRawFileHandler, arg1: t_SimradRawDatagramIdentifier) -> None:
    ...
def test_speed_raw_all(arg0: SimradRawFileHandler) -> None:
    ...
def test_speed_type(arg0: SimradRawFileHandler, arg1: t_SimradRawDatagramIdentifier) -> None:
    ...
FIL1: t_SimradRawDatagramIdentifier  # value = <t_SimradRawDatagramIdentifier.FIL1: 827083078>
MRU0: t_SimradRawDatagramIdentifier  # value = <t_SimradRawDatagramIdentifier.MRU0: 810897997>
NME0: t_SimradRawDatagramIdentifier  # value = <t_SimradRawDatagramIdentifier.NME0: 809848142>
RAW3: t_SimradRawDatagramIdentifier  # value = <t_SimradRawDatagramIdentifier.RAW3: 861356370>
TAG0: t_SimradRawDatagramIdentifier  # value = <t_SimradRawDatagramIdentifier.TAG0: 809976148>
XML0: t_SimradRawDatagramIdentifier  # value = <t_SimradRawDatagramIdentifier.XML0: 810306904>
