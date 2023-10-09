"""
Classes related to Simrad EK60 and EK80 data files
"""
from __future__ import annotations
import themachinethatgoesping.tools.progressbars
import typing
from . import datagrams
from . import filedatacontainers
from . import filedatainterfaces
from . import filetypes
__all__ = ['FIL1', 'FileSimradRaw', 'FileSimradRaw_mapped', 'MRU0', 'NME0', 'RAW3', 'SimradDatagram_type_from_string', 'TAG0', 'XML0', 'datagram_type_to_string', 'datagrams', 'filedatacontainers', 'filedatainterfaces', 'filetypes', 't_SimradDatagramIdentifier', 'test_speed_decode_nmea', 'test_speed_decode_xml', 'test_speed_header', 'test_speed_raw', 'test_speed_raw_all', 'test_speed_type']
class FileSimradRaw:
    """
    """
    @typing.overload
    def __init__(self, file_path: str, cached_index: dict[str, filetypes.FileInfoData_simrad_FileInfoData] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: str, cached_index: dict[str, filetypes.FileInfoData_simrad_FileInfoData], init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: list[str], cached_index: dict[str, filetypes.FileInfoData_simrad_FileInfoData] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_paths: list[str], cached_index: dict[str, filetypes.FileInfoData_simrad_FileInfoData], init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def channel_ids(self) -> list[str]:
        ...
    def get_cached_file_index(self) -> dict[str, filetypes.FileInfoData_simrad_FileInfoData]:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def pings(self) -> filedatacontainers.SimradPingContainer:
        ...
    @typing.overload
    def pings(self, channel_id: str) -> filedatacontainers.SimradPingContainer:
        ...
    @typing.overload
    def pings(self, channel_ids: list[str]) -> filedatacontainers.SimradPingContainer:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> filedatainterfaces.SimradAnnotationDataInterface:
        ...
    @property
    def configuration_interface(self) -> filedatainterfaces.SimradConfigurationDataInterface:
        ...
    @property
    def datagram_interface(self) -> filedatainterfaces.SimradDatagramInterface:
        ...
    @property
    def environment_interface(self) -> filedatainterfaces.SimradEnvironmentDataInterface:
        ...
    @property
    def navigation_interface(self) -> filedatainterfaces.SimradNavigationDataInterface:
        ...
    @property
    def otherfiledata_interface(self) -> filedatainterfaces.SimradOtherFileDataInterface:
        ...
    @property
    def ping_interface(self) -> filedatainterfaces.SimradPingDataInterface:
        ...
class FileSimradRaw_mapped:
    """
    """
    @typing.overload
    def __init__(self, file_path: str, cached_index: dict[str, filetypes.FileInfoData_simrad_FileInfoData] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: str, cached_index: dict[str, filetypes.FileInfoData_simrad_FileInfoData], init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: list[str], cached_index: dict[str, filetypes.FileInfoData_simrad_FileInfoData] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_paths: list[str], cached_index: dict[str, filetypes.FileInfoData_simrad_FileInfoData], init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def channel_ids(self) -> list[str]:
        ...
    def get_cached_file_index(self) -> dict[str, filetypes.FileInfoData_simrad_FileInfoData]:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def pings(self) -> filedatacontainers.SimradPingContainer_mapped:
        ...
    @typing.overload
    def pings(self, channel_id: str) -> filedatacontainers.SimradPingContainer_mapped:
        ...
    @typing.overload
    def pings(self, channel_ids: list[str]) -> filedatacontainers.SimradPingContainer_mapped:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> filedatainterfaces.SimradAnnotationDataInterface_mapped:
        ...
    @property
    def configuration_interface(self) -> filedatainterfaces.SimradConfigurationDataInterface_mapped:
        ...
    @property
    def datagram_interface(self) -> filedatainterfaces.SimradDatagramInterface_mapped:
        ...
    @property
    def environment_interface(self) -> filedatainterfaces.SimradEnvironmentDataInterface_mapped:
        ...
    @property
    def navigation_interface(self) -> filedatainterfaces.SimradNavigationDataInterface_mapped:
        ...
    @property
    def otherfiledata_interface(self) -> filedatainterfaces.SimradOtherFileDataInterface_mapped:
        ...
    @property
    def ping_interface(self) -> filedatainterfaces.SimradPingDataInterface_mapped:
        ...
class t_SimradDatagramIdentifier:
    """
    
    
    Members:
    
      XML0 : < Unspecified (unknown) XML datagram
    
      FIL1 : < Filter datagram
    
      NME0 : < Unspecified (unknown) NMEA datagram
    
      MRU0 : < Motion datagram
    
      TAG0 : < ???
    
      RAW3 : < Raw sample data datagram
    """
    FIL1: typing.ClassVar[t_SimradDatagramIdentifier]  # value = <t_SimradDatagramIdentifier.FIL1: 827083078>
    MRU0: typing.ClassVar[t_SimradDatagramIdentifier]  # value = <t_SimradDatagramIdentifier.MRU0: 810897997>
    NME0: typing.ClassVar[t_SimradDatagramIdentifier]  # value = <t_SimradDatagramIdentifier.NME0: 809848142>
    RAW3: typing.ClassVar[t_SimradDatagramIdentifier]  # value = <t_SimradDatagramIdentifier.RAW3: 861356370>
    TAG0: typing.ClassVar[t_SimradDatagramIdentifier]  # value = <t_SimradDatagramIdentifier.TAG0: 809976148>
    XML0: typing.ClassVar[t_SimradDatagramIdentifier]  # value = <t_SimradDatagramIdentifier.XML0: 810306904>
    __members__: typing.ClassVar[dict[str, t_SimradDatagramIdentifier]]  # value = {'XML0': <t_SimradDatagramIdentifier.XML0: 810306904>, 'FIL1': <t_SimradDatagramIdentifier.FIL1: 827083078>, 'NME0': <t_SimradDatagramIdentifier.NME0: 809848142>, 'MRU0': <t_SimradDatagramIdentifier.MRU0: 810897997>, 'TAG0': <t_SimradDatagramIdentifier.TAG0: 809976148>, 'RAW3': <t_SimradDatagramIdentifier.RAW3: 861356370>}
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
def SimradDatagram_type_from_string(datagram_type: str) -> int:
    ...
@typing.overload
def datagram_type_to_string(datagram_type: int) -> str:
    ...
@typing.overload
def datagram_type_to_string(datagram_type: t_SimradDatagramIdentifier) -> str:
    ...
def test_speed_decode_nmea(arg0: FileSimradRaw_mapped) -> None:
    ...
def test_speed_decode_xml(mapped_file_stream: FileSimradRaw_mapped, level: int = 10) -> None:
    ...
def test_speed_header(arg0: FileSimradRaw_mapped, arg1: t_SimradDatagramIdentifier) -> None:
    ...
def test_speed_raw(arg0: FileSimradRaw_mapped, arg1: t_SimradDatagramIdentifier) -> None:
    ...
def test_speed_raw_all(arg0: FileSimradRaw_mapped) -> None:
    ...
def test_speed_type(arg0: FileSimradRaw_mapped, arg1: t_SimradDatagramIdentifier) -> None:
    ...
FIL1: t_SimradDatagramIdentifier  # value = <t_SimradDatagramIdentifier.FIL1: 827083078>
MRU0: t_SimradDatagramIdentifier  # value = <t_SimradDatagramIdentifier.MRU0: 810897997>
NME0: t_SimradDatagramIdentifier  # value = <t_SimradDatagramIdentifier.NME0: 809848142>
RAW3: t_SimradDatagramIdentifier  # value = <t_SimradDatagramIdentifier.RAW3: 861356370>
TAG0: t_SimradDatagramIdentifier  # value = <t_SimradDatagramIdentifier.TAG0: 809976148>
XML0: t_SimradDatagramIdentifier  # value = <t_SimradDatagramIdentifier.XML0: 810306904>
