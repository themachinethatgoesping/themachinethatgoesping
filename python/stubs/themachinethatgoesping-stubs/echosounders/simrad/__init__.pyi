"""Classes related to Simrad EK60 and EK80 data files"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad
import typing
import themachinethatgoesping.tools.progressbars

__all__ = [
    "FIL1",
    "FileRaw",
    "FileRawIterator_Header",
    "FileRawIterator_Header_mapped",
    "FileRawIterator_Unknown",
    "FileRawIterator_Unknown_mapped",
    "FileRawIterator_Variant",
    "FileRawIterator_Variant_mapped",
    "FileRaw_mapped",
    "MRU0",
    "NME0",
    "RAW3",
    "XML0",
    "datagram_type_to_string",
    "datagrams",
    "ek60_datagram_type_from_string",
    "peter",
    "t_EK60_DatagramType"
]


class FileRaw():
    @typing.overload
    def __call__(self, datagram_type: t_EK60_DatagramType, only_header: bool = False) -> object: ...
    @typing.overload
    def __call__(self, only_header: bool = False) -> object: ...
    def __getitem__(self, index: int) -> typing.Union[datagrams.EK60_Datagram, datagrams.EK60_Unknown]: ...
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
    def datagram_identifier_info(self, datagram_identifier: t_EK60_DatagramType) -> str: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def number_of_packages(self) -> int: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def sort_packages_by_time(self) -> None: ...
    def static_datagram_identifier_to_string(self, datagram_identifier: t_EK60_DatagramType) -> str: ...
    @property
    def i_FIL1(self) -> FileRawIterator_Unknown:
        """
        :type: FileRawIterator_Unknown
        """
    @property
    def i_MRU0(self) -> FileRawIterator_Unknown:
        """
        :type: FileRawIterator_Unknown
        """
    @property
    def i_NME0(self) -> FileRawIterator_Unknown:
        """
        :type: FileRawIterator_Unknown
        """
    @property
    def i_RAW3(self) -> FileRawIterator_Unknown:
        """
        :type: FileRawIterator_Unknown
        """
    @property
    def i_TAG0(self) -> FileRawIterator_Unknown:
        """
        :type: FileRawIterator_Unknown
        """
    @property
    def i_XML0(self) -> FileRawIterator_Unknown:
        """
        :type: FileRawIterator_Unknown
        """
    pass
class FileRawIterator_Header():
    def __getitem__(self, index: int) -> datagrams.EK60_Datagram: ...
    def __len__(self) -> int: ...
    def number_of_packages(self) -> int: ...
    pass
class FileRawIterator_Header_mapped():
    def __getitem__(self, index: int) -> datagrams.EK60_Datagram: ...
    def __len__(self) -> int: ...
    def number_of_packages(self) -> int: ...
    pass
class FileRawIterator_Unknown():
    def __getitem__(self, index: int) -> datagrams.EK60_Unknown: ...
    def __len__(self) -> int: ...
    def number_of_packages(self) -> int: ...
    pass
class FileRawIterator_Unknown_mapped():
    def __getitem__(self, index: int) -> datagrams.EK60_Unknown: ...
    def __len__(self) -> int: ...
    def number_of_packages(self) -> int: ...
    pass
class FileRawIterator_Variant():
    def __getitem__(self, index: int) -> typing.Union[datagrams.EK60_Datagram, datagrams.EK60_Unknown]: ...
    def __len__(self) -> int: ...
    def number_of_packages(self) -> int: ...
    pass
class FileRawIterator_Variant_mapped():
    def __getitem__(self, index: int) -> typing.Union[datagrams.EK60_Datagram, datagrams.EK60_Unknown]: ...
    def __len__(self) -> int: ...
    def number_of_packages(self) -> int: ...
    pass
class FileRaw_mapped():
    @typing.overload
    def __call__(self, datagram_type: t_EK60_DatagramType, only_header: bool = False) -> object: ...
    @typing.overload
    def __call__(self, only_header: bool = False) -> object: ...
    def __getitem__(self, index: int) -> typing.Union[datagrams.EK60_Datagram, datagrams.EK60_Unknown]: ...
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
    def datagram_identifier_info(self, datagram_identifier: t_EK60_DatagramType) -> str: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def number_of_packages(self) -> int: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def sort_packages_by_time(self) -> None: ...
    def static_datagram_identifier_to_string(self, datagram_identifier: t_EK60_DatagramType) -> str: ...
    @property
    def i_FIL1(self) -> FileRawIterator_Unknown_mapped:
        """
        :type: FileRawIterator_Unknown_mapped
        """
    @property
    def i_MRU0(self) -> FileRawIterator_Unknown_mapped:
        """
        :type: FileRawIterator_Unknown_mapped
        """
    @property
    def i_NME0(self) -> FileRawIterator_Unknown_mapped:
        """
        :type: FileRawIterator_Unknown_mapped
        """
    @property
    def i_RAW3(self) -> FileRawIterator_Unknown_mapped:
        """
        :type: FileRawIterator_Unknown_mapped
        """
    @property
    def i_TAG0(self) -> FileRawIterator_Unknown_mapped:
        """
        :type: FileRawIterator_Unknown_mapped
        """
    @property
    def i_XML0(self) -> FileRawIterator_Unknown_mapped:
        """
        :type: FileRawIterator_Unknown_mapped
        """
    pass
class t_EK60_DatagramType():
    """
    Members:

      XML0 : < Unspecified (unknown) XML datagram

      FIL1 : < Filter datagram

      NME0 : < Unspecified (unknown) NMEA datagram

      MRU0 : < Motion datagram

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
    FIL1: themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType # value = <t_EK60_DatagramType.FIL1: 827083078>
    MRU0: themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType # value = <t_EK60_DatagramType.MRU0: 810897997>
    NME0: themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType # value = <t_EK60_DatagramType.NME0: 809848142>
    RAW3: themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType # value = <t_EK60_DatagramType.RAW3: 861356370>
    XML0: themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType # value = <t_EK60_DatagramType.XML0: 810306904>
    __members__: dict # value = {'XML0': <t_EK60_DatagramType.XML0: 810306904>, 'FIL1': <t_EK60_DatagramType.FIL1: 827083078>, 'NME0': <t_EK60_DatagramType.NME0: 809848142>, 'MRU0': <t_EK60_DatagramType.MRU0: 810897997>, 'RAW3': <t_EK60_DatagramType.RAW3: 861356370>}
    pass
def datagram_type_to_string(datagram_type: int) -> str:
    pass
def ek60_datagram_type_from_string(datagram_type: str) -> int:
    pass
def peter(*args, **kwargs) -> typing.Any:
    pass
FIL1: themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType # value = <t_EK60_DatagramType.FIL1: 827083078>
MRU0: themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType # value = <t_EK60_DatagramType.MRU0: 810897997>
NME0: themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType # value = <t_EK60_DatagramType.NME0: 809848142>
RAW3: themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType # value = <t_EK60_DatagramType.RAW3: 861356370>
XML0: themachinethatgoesping.echosounders.simrad.t_EK60_DatagramType # value = <t_EK60_DatagramType.XML0: 810306904>
