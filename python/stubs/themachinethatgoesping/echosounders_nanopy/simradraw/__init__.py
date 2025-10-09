"""
Classes related to SimradRaw EK60 and EK80 data files
"""
from __future__ import annotations
import collections.abc
import enum
import typing
from . import datagrams
from . import filedatacontainers
from . import filedatainterfaces
from . import filedatatypes
__all__: list[str] = ['FIL1', 'MRU0', 'NME0', 'RAW3', 'SimradRawDatagram_type_from_string', 'SimradRawFileHandler', 'SimradRawFileHandler_stream', 'TAG0', 'XML0', 'datagram_type_to_string', 'datagrams', 'filedatacontainers', 'filedatainterfaces', 'filedatatypes', 't_SimradRawDatagramIdentifier', 'test_speed_decode_nmea', 'test_speed_decode_xml', 'test_speed_header', 'test_speed_raw', 'test_speed_raw_all', 'test_speed_type']
class SimradRawFileHandler:
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
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        """
        init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        """
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
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        """
        init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        """
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
class t_SimradRawDatagramIdentifier(enum.Enum):
    """
    Datagram identifiers used in Simrad raw (EK60/EK80) files.
    """
    FIL1: typing.ClassVar[t_SimradRawDatagramIdentifier]  # value = t_SimradRawDatagramIdentifier.FIL1
    MRU0: typing.ClassVar[t_SimradRawDatagramIdentifier]  # value = t_SimradRawDatagramIdentifier.MRU0
    NME0: typing.ClassVar[t_SimradRawDatagramIdentifier]  # value = t_SimradRawDatagramIdentifier.NME0
    RAW3: typing.ClassVar[t_SimradRawDatagramIdentifier]  # value = t_SimradRawDatagramIdentifier.RAW3
    TAG0: typing.ClassVar[t_SimradRawDatagramIdentifier]  # value = t_SimradRawDatagramIdentifier.TAG0
    XML0: typing.ClassVar[t_SimradRawDatagramIdentifier]  # value = t_SimradRawDatagramIdentifier.XML0
FIL1: t_SimradRawDatagramIdentifier  # value = t_SimradRawDatagramIdentifier.FIL1
MRU0: t_SimradRawDatagramIdentifier  # value = t_SimradRawDatagramIdentifier.MRU0
NME0: t_SimradRawDatagramIdentifier  # value = t_SimradRawDatagramIdentifier.NME0
RAW3: t_SimradRawDatagramIdentifier  # value = t_SimradRawDatagramIdentifier.RAW3
SimradRawDatagram_type_from_string: nanobind.nb_func  # value = <nanobind.nb_func object>
TAG0: t_SimradRawDatagramIdentifier  # value = t_SimradRawDatagramIdentifier.TAG0
XML0: t_SimradRawDatagramIdentifier  # value = t_SimradRawDatagramIdentifier.XML0
datagram_type_to_string: nanobind.nb_func  # value = <nanobind.nb_func object>
test_speed_decode_nmea: nanobind.nb_func  # value = <nanobind.nb_func object>
test_speed_decode_xml: nanobind.nb_func  # value = <nanobind.nb_func object>
test_speed_header: nanobind.nb_func  # value = <nanobind.nb_func object>
test_speed_raw: nanobind.nb_func  # value = <nanobind.nb_func object>
test_speed_raw_all: nanobind.nb_func  # value = <nanobind.nb_func object>
test_speed_type: nanobind.nb_func  # value = <nanobind.nb_func object>
