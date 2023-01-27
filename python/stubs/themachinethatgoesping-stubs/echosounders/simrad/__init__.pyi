"""Classes related to Simrad EK60 and EK80 data files"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad
import typing
import themachinethatgoesping.tools.progressbars

__all__ = [
    "FIL1",
    "FileSimradRaw",
    "FileSimradRaw_mapped",
    "MRU0",
    "NME0",
    "RAW3",
    "SimradDatagram_type_from_string",
    "TAG0",
    "XML0",
    "datagram_type_to_string",
    "datagrams",
    "filedatacontainers",
    "filedatainterfaces",
    "filetypes",
    "t_SimradDatagramIdentifier",
    "test_speed_decode_nmea",
    "test_speed_decode_xml",
    "test_speed_header",
    "test_speed_raw",
    "test_speed_raw_all",
    "test_speed_type"
]


class FileSimradRaw():
    @typing.overload
    def __init__(self, file_path: str, init: bool = True, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_path: str, init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def __init__(self, file_path: typing.List[str], init: bool = True, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_paths: typing.List[str], init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def channel_ids(self) -> typing.List[str]: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def pings(self) -> filedatacontainers.SimradPingContainer: ...
    @typing.overload
    def pings(self, channel_id: str) -> filedatacontainers.SimradPingContainer: ...
    @typing.overload
    def pings(self, channel_ids: typing.List[str]) -> filedatacontainers.SimradPingContainer: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> filedatainterfaces.SimradAnnotationDataInterface:
        """
        :type: filedatainterfaces.SimradAnnotationDataInterface
        """
    @property
    def configuration_interface(self) -> filedatainterfaces.SimradConfigurationDataInterface:
        """
        :type: filedatainterfaces.SimradConfigurationDataInterface
        """
    @property
    def datagram_interface(self) -> filedatainterfaces.SimradDatagramInterface:
        """
        :type: filedatainterfaces.SimradDatagramInterface
        """
    @property
    def environment_interface(self) -> filedatainterfaces.SimradEnvironmentDataInterface:
        """
        :type: filedatainterfaces.SimradEnvironmentDataInterface
        """
    @property
    def navigation_interface(self) -> filedatainterfaces.SimradNavigationDataInterface:
        """
        :type: filedatainterfaces.SimradNavigationDataInterface
        """
    @property
    def otherfiledata_interface(self) -> filedatainterfaces.SimradOtherFileDataInterface:
        """
        :type: filedatainterfaces.SimradOtherFileDataInterface
        """
    @property
    def ping_interface(self) -> filedatainterfaces.SimradPingDataInterface:
        """
        :type: filedatainterfaces.SimradPingDataInterface
        """
    pass
class FileSimradRaw_mapped():
    @typing.overload
    def __init__(self, file_path: str, init: bool = True, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_path: str, init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def __init__(self, file_path: typing.List[str], init: bool = True, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_paths: typing.List[str], init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def channel_ids(self) -> typing.List[str]: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def pings(self) -> filedatacontainers.SimradPingContainer_mapped: ...
    @typing.overload
    def pings(self, channel_id: str) -> filedatacontainers.SimradPingContainer_mapped: ...
    @typing.overload
    def pings(self, channel_ids: typing.List[str]) -> filedatacontainers.SimradPingContainer_mapped: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> filedatainterfaces.SimradAnnotationDataInterface_mapped:
        """
        :type: filedatainterfaces.SimradAnnotationDataInterface_mapped
        """
    @property
    def configuration_interface(self) -> filedatainterfaces.SimradConfigurationDataInterface_mapped:
        """
        :type: filedatainterfaces.SimradConfigurationDataInterface_mapped
        """
    @property
    def datagram_interface(self) -> filedatainterfaces.SimradDatagramInterface_mapped:
        """
        :type: filedatainterfaces.SimradDatagramInterface_mapped
        """
    @property
    def environment_interface(self) -> filedatainterfaces.SimradEnvironmentDataInterface_mapped:
        """
        :type: filedatainterfaces.SimradEnvironmentDataInterface_mapped
        """
    @property
    def navigation_interface(self) -> filedatainterfaces.SimradNavigationDataInterface_mapped:
        """
        :type: filedatainterfaces.SimradNavigationDataInterface_mapped
        """
    @property
    def otherfiledata_interface(self) -> filedatainterfaces.SimradOtherFileDataInterface_mapped:
        """
        :type: filedatainterfaces.SimradOtherFileDataInterface_mapped
        """
    @property
    def ping_interface(self) -> filedatainterfaces.SimradPingDataInterface_mapped:
        """
        :type: filedatainterfaces.SimradPingDataInterface_mapped
        """
    pass
class t_SimradDatagramIdentifier():
    """
    Members:

      XML0 : < Unspecified (unknown) XML datagram

      FIL1 : < Filter datagram

      NME0 : < Unspecified (unknown) NMEA datagram

      MRU0 : < Motion datagram

      TAG0 : < ???

      RAW3 : < Raw sample data datagram
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    @typing.overload
    def __init__(self, str: str) -> None: 
        """
        Construct this enum type from string
        """
    @typing.overload
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    FIL1: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.FIL1: 827083078>
    MRU0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.MRU0: 810897997>
    NME0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.NME0: 809848142>
    RAW3: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.RAW3: 861356370>
    TAG0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.TAG0: 809976148>
    XML0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.XML0: 810306904>
    __members__: dict # value = {'XML0': <t_SimradDatagramIdentifier.XML0: 810306904>, 'FIL1': <t_SimradDatagramIdentifier.FIL1: 827083078>, 'NME0': <t_SimradDatagramIdentifier.NME0: 809848142>, 'MRU0': <t_SimradDatagramIdentifier.MRU0: 810897997>, 'TAG0': <t_SimradDatagramIdentifier.TAG0: 809976148>, 'RAW3': <t_SimradDatagramIdentifier.RAW3: 861356370>}
    pass
def SimradDatagram_type_from_string(datagram_type: str) -> int:
    pass
@typing.overload
def datagram_type_to_string(datagram_type: int) -> str:
    pass
@typing.overload
def datagram_type_to_string(datagram_type: t_SimradDatagramIdentifier) -> str:
    pass
def test_speed_decode_nmea(arg0: FileSimradRaw_mapped) -> None:
    pass
def test_speed_decode_xml(mapped_file_stream: FileSimradRaw_mapped, level: int = 10) -> None:
    pass
def test_speed_header(arg0: FileSimradRaw_mapped, arg1: t_SimradDatagramIdentifier) -> None:
    pass
def test_speed_raw(arg0: FileSimradRaw_mapped, arg1: t_SimradDatagramIdentifier) -> None:
    pass
def test_speed_raw_all(arg0: FileSimradRaw_mapped) -> None:
    pass
def test_speed_type(arg0: FileSimradRaw_mapped, arg1: t_SimradDatagramIdentifier) -> None:
    pass
FIL1: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.FIL1: 827083078>
MRU0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.MRU0: 810897997>
NME0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.NME0: 809848142>
RAW3: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.RAW3: 861356370>
TAG0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.TAG0: 809976148>
XML0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.XML0: 810306904>
