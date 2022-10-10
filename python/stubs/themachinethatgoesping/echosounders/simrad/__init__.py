"""Classes related to Simrad EK60 and EK80 data files"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad
import typing
import themachinethatgoesping.navigation
import themachinethatgoesping.tools.progressbars

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
    "SimradDatagram_type_from_string",
    "SimradPing",
    "SimradPingIterator",
    "SimradPingIterator_mapped",
    "SimradPing_RawData",
    "SimradPing_mapped",
    "SimradPing_mapped_RawData",
    "TAG0",
    "XML0",
    "datagram_type_to_string",
    "datagrams",
    "t_SimradDatagramType",
    "test_speed_decode_nmea",
    "test_speed_decode_xml",
    "test_speed_header",
    "test_speed_raw",
    "test_speed_raw_all",
    "test_speed_type"
]


class FileRaw():
    @typing.overload
    def __call__(self, datagram_type: t_SimradDatagramType, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    @typing.overload
    def __call__(self, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    def __getitem__(self, index: int) -> typing.Union[datagrams.SimradDatagram, datagrams.NME0, datagrams.XML0, datagrams.MRU0, datagrams.RAW3, datagrams.FIL1, datagrams.TAG0, datagrams.SimradUnknown]: ...
    @typing.overload
    def __init__(self, file_path: str, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def __init__(self, file_path: str, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_path: typing.List[str], show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_paths: typing.List[str], progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def __len__(self) -> int: ...
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
    def datagram_identifier_info(self, datagram_identifier: t_SimradDatagramType) -> str: ...
    def get_navigation_interpolators(self) -> typing.List[themachinethatgoesping.navigation.NavigationInterpolatorLatLon]: ...
    @typing.overload
    def headers(self, datagram_type: t_SimradDatagramType, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    @typing.overload
    def headers(self, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def pings(self, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @typing.overload
    def raw(self, datagram_type: t_SimradDatagramType, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    @typing.overload
    def raw(self, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    def size(self) -> int: ...
    def sort_packages_by_time(self) -> None: ...
    def static_datagram_identifier_to_string(self, datagram_identifier: t_SimradDatagramType) -> str: ...
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
    def i_Pings(self) -> SimradPingIterator:
        """
        :type: SimradPingIterator
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
class FileRawIterator_FIL1():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_FIL1: ...
    def __getitem__(self, index: int) -> datagrams.FIL1: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_FIL1_mapped():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_FIL1_mapped: ...
    def __getitem__(self, index: int) -> datagrams.FIL1: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_Header():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_Header: ...
    def __getitem__(self, index: int) -> datagrams.SimradDatagram: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_Header_mapped():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_Header_mapped: ...
    def __getitem__(self, index: int) -> datagrams.SimradDatagram: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_MRU0():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_MRU0: ...
    def __getitem__(self, index: int) -> datagrams.MRU0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_MRU0_mapped():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_MRU0_mapped: ...
    def __getitem__(self, index: int) -> datagrams.MRU0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_NME0():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_NME0: ...
    def __getitem__(self, index: int) -> datagrams.NME0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_NME0_mapped():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_NME0_mapped: ...
    def __getitem__(self, index: int) -> datagrams.NME0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_RAW3():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_RAW3: ...
    def __getitem__(self, index: int) -> datagrams.RAW3: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_RAW3_header():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_RAW3_header: ...
    def __getitem__(self, index: int) -> datagrams.RAW3: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_RAW3_header_mapped():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_RAW3_header_mapped: ...
    def __getitem__(self, index: int) -> datagrams.RAW3: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_RAW3_mapped():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_RAW3_mapped: ...
    def __getitem__(self, index: int) -> datagrams.RAW3: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_TAG0():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_TAG0: ...
    def __getitem__(self, index: int) -> datagrams.TAG0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_TAG0_mapped():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_TAG0_mapped: ...
    def __getitem__(self, index: int) -> datagrams.TAG0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_Unknown():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_Unknown: ...
    def __getitem__(self, index: int) -> datagrams.SimradUnknown: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_Unknown_mapped():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_Unknown_mapped: ...
    def __getitem__(self, index: int) -> datagrams.SimradUnknown: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_Variant():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_Variant: ...
    def __getitem__(self, index: int) -> typing.Union[datagrams.SimradDatagram, datagrams.NME0, datagrams.XML0, datagrams.MRU0, datagrams.RAW3, datagrams.FIL1, datagrams.TAG0, datagrams.SimradUnknown]: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_Variant_mapped():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_Variant_mapped: ...
    def __getitem__(self, index: int) -> typing.Union[datagrams.SimradDatagram, datagrams.NME0, datagrams.XML0, datagrams.MRU0, datagrams.RAW3, datagrams.FIL1, datagrams.TAG0, datagrams.SimradUnknown]: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_XML0():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_XML0: ...
    def __getitem__(self, index: int) -> datagrams.XML0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRawIterator_XML0_mapped():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> FileRawIterator_XML0_mapped: ...
    def __getitem__(self, index: int) -> datagrams.XML0: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class FileRaw_mapped():
    @typing.overload
    def __call__(self, datagram_type: t_SimradDatagramType, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    @typing.overload
    def __call__(self, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    def __getitem__(self, index: int) -> typing.Union[datagrams.SimradDatagram, datagrams.NME0, datagrams.XML0, datagrams.MRU0, datagrams.RAW3, datagrams.FIL1, datagrams.TAG0, datagrams.SimradUnknown]: ...
    @typing.overload
    def __init__(self, file_path: str, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def __init__(self, file_path: str, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_path: typing.List[str], show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_paths: typing.List[str], progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def __len__(self) -> int: ...
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
    def datagram_identifier_info(self, datagram_identifier: t_SimradDatagramType) -> str: ...
    def get_navigation_interpolators(self) -> typing.List[themachinethatgoesping.navigation.NavigationInterpolatorLatLon]: ...
    @typing.overload
    def headers(self, datagram_type: t_SimradDatagramType, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    @typing.overload
    def headers(self, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def pings(self, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @typing.overload
    def raw(self, datagram_type: t_SimradDatagramType, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    @typing.overload
    def raw(self, index_min: int = 0, index_max: int = 9223372036854775807, index_step: int = 1) -> object: ...
    def size(self) -> int: ...
    def sort_packages_by_time(self) -> None: ...
    def static_datagram_identifier_to_string(self, datagram_identifier: t_SimradDatagramType) -> str: ...
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
    def i_Pings(self) -> SimradPingIterator_mapped:
        """
        :type: SimradPingIterator_mapped
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
    def raw(self) -> SimradPing_RawData: ...
    pass
class SimradPingIterator():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> SimradPingIterator: ...
    @staticmethod
    def __getitem__(*args, **kwargs) -> typing.Any: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class SimradPingIterator_mapped():
    def __call__(self, index_min: int = 0, index_max: int = 18446744073709551615, index_step: int = 1) -> SimradPingIterator_mapped: ...
    @staticmethod
    def __getitem__(*args, **kwargs) -> typing.Any: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    pass
class SimradPing_RawData():
    @property
    def ping_data(self) -> datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)

        :type: datagrams.RAW3
        """
    pass
class SimradPing_mapped():
    def raw(self) -> SimradPing_mapped_RawData: ...
    pass
class SimradPing_mapped_RawData():
    @property
    def ping_data(self) -> datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)

        :type: datagrams.RAW3
        """
    pass
class t_SimradDatagramType():
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
    FIL1: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType # value = <t_SimradDatagramType.FIL1: 827083078>
    MRU0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType # value = <t_SimradDatagramType.MRU0: 810897997>
    NME0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType # value = <t_SimradDatagramType.NME0: 809848142>
    RAW3: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType # value = <t_SimradDatagramType.RAW3: 861356370>
    TAG0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType # value = <t_SimradDatagramType.TAG0: 809976148>
    XML0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType # value = <t_SimradDatagramType.XML0: 810306904>
    __members__: dict # value = {'XML0': <t_SimradDatagramType.XML0: 810306904>, 'FIL1': <t_SimradDatagramType.FIL1: 827083078>, 'NME0': <t_SimradDatagramType.NME0: 809848142>, 'MRU0': <t_SimradDatagramType.MRU0: 810897997>, 'TAG0': <t_SimradDatagramType.TAG0: 809976148>, 'RAW3': <t_SimradDatagramType.RAW3: 861356370>}
    pass
def SimradDatagram_type_from_string(datagram_type: str) -> int:
    pass
def datagram_type_to_string(datagram_type: int) -> str:
    pass
def test_speed_decode_nmea(arg0: FileRaw_mapped) -> None:
    pass
def test_speed_decode_xml(mapped_file_stream: FileRaw_mapped, level: int = 10) -> None:
    pass
def test_speed_header(arg0: FileRaw_mapped, arg1: t_SimradDatagramType) -> None:
    pass
def test_speed_raw(arg0: FileRaw_mapped, arg1: t_SimradDatagramType) -> None:
    pass
def test_speed_raw_all(arg0: FileRaw_mapped) -> None:
    pass
def test_speed_type(arg0: FileRaw_mapped, arg1: t_SimradDatagramType) -> None:
    pass
FIL1: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType # value = <t_SimradDatagramType.FIL1: 827083078>
MRU0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType # value = <t_SimradDatagramType.MRU0: 810897997>
NME0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType # value = <t_SimradDatagramType.NME0: 809848142>
RAW3: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType # value = <t_SimradDatagramType.RAW3: 861356370>
TAG0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType # value = <t_SimradDatagramType.TAG0: 809976148>
XML0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramType # value = <t_SimradDatagramType.XML0: 810306904>
