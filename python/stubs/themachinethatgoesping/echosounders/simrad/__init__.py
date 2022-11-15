"""Classes related to Simrad EK60 and EK80 data files"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad
import typing
import numpy
import themachinethatgoesping.navigation
import themachinethatgoesping.tools.progressbars
import themachinethatgoesping.tools.pyhelper
_Shape = typing.Tuple[int, ...]

__all__ = [
    "FIL1",
    "FileRaw",
    "FileRawIterator_FIL1",
    "FileRawIterator_FIL1_mapped",
    "FileRawIterator_Header",
    "FileRawIterator_Header_mapped",
    "FileRawIterator_MRU0",
    "FileRawIterator_MRU0_mapped",
    "FileRawIterator_NME0",
    "FileRawIterator_NME0_mapped",
    "FileRawIterator_RAW3",
    "FileRawIterator_RAW3_header",
    "FileRawIterator_RAW3_header_mapped",
    "FileRawIterator_RAW3_mapped",
    "FileRawIterator_TAG0",
    "FileRawIterator_TAG0_mapped",
    "FileRawIterator_Unknown",
    "FileRawIterator_Unknown_mapped",
    "FileRawIterator_Variant",
    "FileRawIterator_Variant_mapped",
    "FileRawIterator_XML0",
    "FileRawIterator_XML0_mapped",
    "FileRaw_mapped",
    "MRU0",
    "NME0",
    "RAW3",
    "SimradAnnotationDataInterface",
    "SimradAnnotationDataInterface_mapped",
    "SimradConfigurationDataInterface",
    "SimradConfigurationDataInterface_mapped",
    "SimradDatagram_type_from_string",
    "SimradEnvironmentDataInterface",
    "SimradEnvironmentDataInterface_mapped",
    "SimradFileData",
    "SimradNavigationDataInterface",
    "SimradNavigationDataInterface_mapped",
    "SimradOtherDataInterface",
    "SimradOtherDataInterface_mapped",
    "SimradPackageDataInterface",
    "SimradPackageDataInterface_mapped",
    "SimradPing",
    "SimradPingContainer",
    "SimradPingContainer_mapped",
    "SimradPing_RawData",
    "SimradPing_mapped",
    "SimradPing_mapped_RawData",
    "TAG0",
    "XML0",
    "datagram_type_to_string",
    "datagrams",
    "t_SimradDatagramIdentifier",
    "test_speed_decode_nmea",
    "test_speed_decode_xml",
    "test_speed_header",
    "test_speed_raw",
    "test_speed_raw_all",
    "test_speed_type"
]


class FileRaw():
    @typing.overload
    def __init__(self, file_path: str, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def __init__(self, file_path: str, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_path: typing.List[str], show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_paths: typing.List[str], progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def append_file(self, file_path: str, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def append_file(self, file_path: str, show_progress: bool = True) -> None: ...
    @typing.overload
    def append_files(self, file_path: typing.List[str], progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def append_files(self, file_path: typing.List[str], show_progress: bool = True) -> None: ...
    def channel_ids(self) -> typing.List[str]: ...
    def get_navigation_interpolators(self) -> typing.List[themachinethatgoesping.navigation.NavigationInterpolatorLatLon]: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def pings(self) -> SimradPingContainer: ...
    @typing.overload
    def pings(self, channel_id: str) -> SimradPingContainer: ...
    @typing.overload
    def pings(self, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> SimradPingContainer: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> SimradAnnotationDataInterface:
        """
        :type: SimradAnnotationDataInterface
        """
    @property
    def configuration_interface(self) -> SimradConfigurationDataInterface:
        """
        :type: SimradConfigurationDataInterface
        """
    @property
    def environment_interface(self) -> SimradEnvironmentDataInterface:
        """
        :type: SimradEnvironmentDataInterface
        """
    @property
    def i_Pings(self) -> SimradPingContainer:
        """
        :type: SimradPingContainer
        """
    @property
    def navigation_interface(self) -> SimradNavigationDataInterface:
        """
        :type: SimradNavigationDataInterface
        """
    @property
    def otherdata_interface(self) -> SimradOtherDataInterface:
        """
        :type: SimradOtherDataInterface
        """
    @property
    def package_data_interface(self) -> SimradPackageDataInterface:
        """
        :type: SimradPackageDataInterface
        """
    pass
class FileRawIterator_FIL1():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_FIL1: ...
    def __getitem__(self, index: int) -> datagrams.FIL1: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_FIL1_mapped():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_FIL1_mapped: ...
    def __getitem__(self, index: int) -> datagrams.FIL1: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_Header():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_Header: ...
    def __getitem__(self, index: int) -> datagrams.SimradDatagram: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_Header_mapped():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_Header_mapped: ...
    def __getitem__(self, index: int) -> datagrams.SimradDatagram: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_MRU0():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_MRU0: ...
    def __getitem__(self, index: int) -> datagrams.MRU0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_MRU0_mapped():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_MRU0_mapped: ...
    def __getitem__(self, index: int) -> datagrams.MRU0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_NME0():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_NME0: ...
    def __getitem__(self, index: int) -> datagrams.NME0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_NME0_mapped():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_NME0_mapped: ...
    def __getitem__(self, index: int) -> datagrams.NME0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_RAW3():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_RAW3: ...
    def __getitem__(self, index: int) -> datagrams.RAW3: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_RAW3_header():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_RAW3_header: ...
    def __getitem__(self, index: int) -> datagrams.RAW3: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_RAW3_header_mapped():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_RAW3_header_mapped: ...
    def __getitem__(self, index: int) -> datagrams.RAW3: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_RAW3_mapped():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_RAW3_mapped: ...
    def __getitem__(self, index: int) -> datagrams.RAW3: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_TAG0():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_TAG0: ...
    def __getitem__(self, index: int) -> datagrams.TAG0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_TAG0_mapped():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_TAG0_mapped: ...
    def __getitem__(self, index: int) -> datagrams.TAG0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_Unknown():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_Unknown: ...
    def __getitem__(self, index: int) -> datagrams.SimradUnknown: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_Unknown_mapped():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_Unknown_mapped: ...
    def __getitem__(self, index: int) -> datagrams.SimradUnknown: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_Variant():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_Variant: ...
    def __getitem__(self, index: int) -> typing.Union[datagrams.SimradDatagram, datagrams.NME0, datagrams.XML0, datagrams.MRU0, datagrams.RAW3, datagrams.FIL1, datagrams.TAG0, datagrams.SimradUnknown]: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_Variant_mapped():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_Variant_mapped: ...
    def __getitem__(self, index: int) -> typing.Union[datagrams.SimradDatagram, datagrams.NME0, datagrams.XML0, datagrams.MRU0, datagrams.RAW3, datagrams.FIL1, datagrams.TAG0, datagrams.SimradUnknown]: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_XML0():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_XML0: ...
    def __getitem__(self, index: int) -> datagrams.XML0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_XML0_mapped():
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> FileRawIterator_XML0_mapped: ...
    def __getitem__(self, index: int) -> datagrams.XML0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRaw_mapped():
    @typing.overload
    def __init__(self, file_path: str, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def __init__(self, file_path: str, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_path: typing.List[str], show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_paths: typing.List[str], progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def append_file(self, file_path: str, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def append_file(self, file_path: str, show_progress: bool = True) -> None: ...
    @typing.overload
    def append_files(self, file_path: typing.List[str], progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def append_files(self, file_path: typing.List[str], show_progress: bool = True) -> None: ...
    def channel_ids(self) -> typing.List[str]: ...
    def get_navigation_interpolators(self) -> typing.List[themachinethatgoesping.navigation.NavigationInterpolatorLatLon]: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def pings(self) -> SimradPingContainer_mapped: ...
    @typing.overload
    def pings(self, channel_id: str) -> SimradPingContainer_mapped: ...
    @typing.overload
    def pings(self, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> SimradPingContainer_mapped: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> SimradAnnotationDataInterface_mapped:
        """
        :type: SimradAnnotationDataInterface_mapped
        """
    @property
    def configuration_interface(self) -> SimradConfigurationDataInterface_mapped:
        """
        :type: SimradConfigurationDataInterface_mapped
        """
    @property
    def environment_interface(self) -> SimradEnvironmentDataInterface_mapped:
        """
        :type: SimradEnvironmentDataInterface_mapped
        """
    @property
    def i_Pings(self) -> SimradPingContainer_mapped:
        """
        :type: SimradPingContainer_mapped
        """
    @property
    def navigation_interface(self) -> SimradNavigationDataInterface_mapped:
        """
        :type: SimradNavigationDataInterface_mapped
        """
    @property
    def otherdata_interface(self) -> SimradOtherDataInterface_mapped:
        """
        :type: SimradOtherDataInterface_mapped
        """
    @property
    def package_data_interface(self) -> SimradPackageDataInterface_mapped:
        """
        :type: SimradPackageDataInterface_mapped
        """
    pass
class SimradAnnotationDataInterface():
    @property
    def package_data_interface_per_file(self) -> typing.List[SimradPackageDataInterface]:
        """
        :type: typing.List[SimradPackageDataInterface]
        """
    pass
class SimradAnnotationDataInterface_mapped():
    @property
    def package_data_interface_per_file(self) -> typing.List[SimradPackageDataInterface_mapped]:
        """
        :type: typing.List[SimradPackageDataInterface_mapped]
        """
    pass
class SimradConfigurationDataInterface():
    @property
    def package_data_interface_per_file(self) -> typing.List[SimradPackageDataInterface]:
        """
        :type: typing.List[SimradPackageDataInterface]
        """
    pass
class SimradConfigurationDataInterface_mapped():
    @property
    def package_data_interface_per_file(self) -> typing.List[SimradPackageDataInterface_mapped]:
        """
        :type: typing.List[SimradPackageDataInterface_mapped]
        """
    pass
class SimradEnvironmentDataInterface():
    @property
    def package_data_interface_per_file(self) -> typing.List[SimradPackageDataInterface]:
        """
        :type: typing.List[SimradPackageDataInterface]
        """
    pass
class SimradEnvironmentDataInterface_mapped():
    @property
    def package_data_interface_per_file(self) -> typing.List[SimradPackageDataInterface_mapped]:
        """
        :type: typing.List[SimradPackageDataInterface_mapped]
        """
    pass
class SimradFileData():
    def FIL1(self) -> typing.List[datagrams.FIL1]: ...
    def TAG0(self) -> typing.List[datagrams.TAG0]: ...
    def XML0_Configuration(self) -> datagrams.XML0_datagrams.XML_Configuration: ...
    def XML0_Environment(self) -> typing.List[datagrams.XML0_datagrams.XML_Environment]: ...
    def XML0_InitialParameter(self) -> typing.List[datagrams.XML0_datagrams.XML_InitialParameter]: ...
    def XML0_Other(self) -> typing.Dict[str, typing.List[datagrams.XML0]]: ...
    pass
class SimradNavigationDataInterface():
    @property
    def package_data_interface_per_file(self) -> typing.List[SimradPackageDataInterface]:
        """
        :type: typing.List[SimradPackageDataInterface]
        """
    pass
class SimradNavigationDataInterface_mapped():
    @property
    def package_data_interface_per_file(self) -> typing.List[SimradPackageDataInterface_mapped]:
        """
        :type: typing.List[SimradPackageDataInterface_mapped]
        """
    pass
class SimradOtherDataInterface():
    @property
    def package_data_interface_per_file(self) -> typing.List[SimradPackageDataInterface]:
        """
        :type: typing.List[SimradPackageDataInterface]
        """
    pass
class SimradOtherDataInterface_mapped():
    @property
    def package_data_interface_per_file(self) -> typing.List[SimradPackageDataInterface_mapped]:
        """
        :type: typing.List[SimradPackageDataInterface_mapped]
        """
    pass
class SimradPackageDataInterface():
    @typing.overload
    def __call__(self, datagram_type: t_SimradDatagramIdentifier, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> object: ...
    @typing.overload
    def __call__(self, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> object: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def headers(self, datagram_type: t_SimradDatagramIdentifier, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> object: ...
    @typing.overload
    def headers(self, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> object: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @typing.overload
    def raw(self, datagram_type: t_SimradDatagramIdentifier, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> object: ...
    @typing.overload
    def raw(self, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> object: ...
    @property
    def i_FIL1(self) -> FileRawIterator_FIL1:
        """
        :type: FileRawIterator_FIL1
        """
    @property
    def i_MRU0(self) -> FileRawIterator_MRU0:
        """
        :type: FileRawIterator_MRU0
        """
    @property
    def i_NME0(self) -> FileRawIterator_NME0:
        """
        :type: FileRawIterator_NME0
        """
    @property
    def i_RAW3(self) -> FileRawIterator_RAW3:
        """
        :type: FileRawIterator_RAW3
        """
    @property
    def i_RAW3_header(self) -> FileRawIterator_RAW3_header:
        """
        :type: FileRawIterator_RAW3_header
        """
    @property
    def i_TAG0(self) -> FileRawIterator_TAG0:
        """
        :type: FileRawIterator_TAG0
        """
    @property
    def i_XML0(self) -> FileRawIterator_XML0:
        """
        :type: FileRawIterator_XML0
        """
    pass
class SimradPackageDataInterface_mapped():
    @typing.overload
    def __call__(self, datagram_type: t_SimradDatagramIdentifier, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> object: ...
    @typing.overload
    def __call__(self, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> object: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def headers(self, datagram_type: t_SimradDatagramIdentifier, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> object: ...
    @typing.overload
    def headers(self, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> object: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @typing.overload
    def raw(self, datagram_type: t_SimradDatagramIdentifier, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> object: ...
    @typing.overload
    def raw(self, start: int = 0, end: int = 9223372036854775807, step: int = 1) -> object: ...
    @property
    def i_FIL1(self) -> FileRawIterator_FIL1_mapped:
        """
        :type: FileRawIterator_FIL1_mapped
        """
    @property
    def i_MRU0(self) -> FileRawIterator_MRU0_mapped:
        """
        :type: FileRawIterator_MRU0_mapped
        """
    @property
    def i_NME0(self) -> FileRawIterator_NME0_mapped:
        """
        :type: FileRawIterator_NME0_mapped
        """
    @property
    def i_RAW3(self) -> FileRawIterator_RAW3_mapped:
        """
        :type: FileRawIterator_RAW3_mapped
        """
    @property
    def i_RAW3_header(self) -> FileRawIterator_RAW3_header_mapped:
        """
        :type: FileRawIterator_RAW3_header_mapped
        """
    @property
    def i_TAG0(self) -> FileRawIterator_TAG0_mapped:
        """
        :type: FileRawIterator_TAG0_mapped
        """
    @property
    def i_XML0(self) -> FileRawIterator_XML0_mapped:
        """
        :type: FileRawIterator_XML0_mapped
        """
    pass
class SimradPing():
    def file_data(self) -> SimradFileData: ...
    def get_angle(self) -> numpy.ndarray[numpy.float32]: ...
    def get_channel_id(self) -> str: ...
    def get_number_of_samples(self) -> int: ...
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_timestamp(self) -> float: ...
    def load_data(self) -> None: ...
    def raw(self) -> SimradPing_RawData: ...
    def release_data(self) -> None: ...
    pass
class SimradPingContainer():
    @typing.overload
    def __call__(self, channel_id: str) -> SimradPingContainer: ...
    @typing.overload
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> SimradPingContainer: ...
    @typing.overload
    def __getitem__(self, index: int) -> SimradPing: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradPingContainer: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> SimradPingContainer: ...
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradPingContainer]: ...
    def filter_by_channel_ids(self, channel_ids: typing.List[str]) -> SimradPingContainer: ...
    def find_channel_ids(self) -> typing.List[str]: ...
    def get_sorted_by_time(self) -> SimradPingContainer: ...
    def max_number_of_samples(self) -> int: ...
    def size(self) -> int: ...
    pass
class SimradPingContainer_mapped():
    @typing.overload
    def __call__(self, channel_id: str) -> SimradPingContainer_mapped: ...
    @typing.overload
    def __call__(self, start: int = 0, end: int = 18446744073709551615, step: int = 1) -> SimradPingContainer_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> SimradPing_mapped: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradPingContainer_mapped: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> SimradPingContainer_mapped: ...
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradPingContainer_mapped]: ...
    def filter_by_channel_ids(self, channel_ids: typing.List[str]) -> SimradPingContainer_mapped: ...
    def find_channel_ids(self) -> typing.List[str]: ...
    def get_sorted_by_time(self) -> SimradPingContainer_mapped: ...
    def max_number_of_samples(self) -> int: ...
    def size(self) -> int: ...
    pass
class SimradPing_RawData():
    def get_parameter(self) -> datagrams.XML0_datagrams.XML_Parameter_Channel: ...
    def get_sample_data(self) -> typing.Union[datagrams.RAW3_datatypes.RAW3_DataSkipped, datagrams.RAW3_datatypes.RAW3_DataComplexFloat32, datagrams.RAW3_datatypes.RAW3_DataPowerAndAngle, datagrams.RAW3_datatypes.RAW3_DataPower, datagrams.RAW3_datatypes.RAW3_DataAngle]: ...
    def load_data(self) -> None: ...
    def release_data(self) -> None: ...
    @property
    def file_data(self) -> SimradFileData:
        """
        :type: SimradFileData
        """
    @property
    def ping_data(self) -> datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)

        :type: datagrams.RAW3
        """
    pass
class SimradPing_mapped():
    def file_data(self) -> SimradFileData: ...
    def get_angle(self) -> numpy.ndarray[numpy.float32]: ...
    def get_channel_id(self) -> str: ...
    def get_number_of_samples(self) -> int: ...
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_timestamp(self) -> float: ...
    def load_data(self) -> None: ...
    def raw(self) -> SimradPing_mapped_RawData: ...
    def release_data(self) -> None: ...
    pass
class SimradPing_mapped_RawData():
    def get_parameter(self) -> datagrams.XML0_datagrams.XML_Parameter_Channel: ...
    def get_sample_data(self) -> typing.Union[datagrams.RAW3_datatypes.RAW3_DataSkipped, datagrams.RAW3_datatypes.RAW3_DataComplexFloat32, datagrams.RAW3_datatypes.RAW3_DataPowerAndAngle, datagrams.RAW3_datatypes.RAW3_DataPower, datagrams.RAW3_datatypes.RAW3_DataAngle]: ...
    def load_data(self) -> None: ...
    def release_data(self) -> None: ...
    @property
    def file_data(self) -> SimradFileData:
        """
        :type: SimradFileData
        """
    @property
    def ping_data(self) -> datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)

        :type: datagrams.RAW3
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
def test_speed_decode_nmea(arg0: FileRaw_mapped) -> None:
    pass
def test_speed_decode_xml(mapped_file_stream: FileRaw_mapped, level: int = 10) -> None:
    pass
def test_speed_header(arg0: FileRaw_mapped, arg1: t_SimradDatagramIdentifier) -> None:
    pass
def test_speed_raw(arg0: FileRaw_mapped, arg1: t_SimradDatagramIdentifier) -> None:
    pass
def test_speed_raw_all(arg0: FileRaw_mapped) -> None:
    pass
def test_speed_type(arg0: FileRaw_mapped, arg1: t_SimradDatagramIdentifier) -> None:
    pass
FIL1: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.FIL1: 827083078>
MRU0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.MRU0: 810897997>
NME0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.NME0: 809848142>
RAW3: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.RAW3: 861356370>
TAG0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.TAG0: 809976148>
XML0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.XML0: 810306904>
