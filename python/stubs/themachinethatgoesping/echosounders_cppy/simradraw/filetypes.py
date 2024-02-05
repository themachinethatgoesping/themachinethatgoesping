"""
SimradRaw EK60 and EK80 file data types
"""
from __future__ import annotations
import themachinethatgoesping.echosounders_cppy.filetemplates
import themachinethatgoesping.echosounders_cppy.simradraw
import themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams
import typing
__all__ = ['FilePackageIndex_simradraw_FilePackageIndex', 'SimradRawPing', 'SimradRawPingCommon', 'SimradRawPingCommon_mapped', 'SimradRawPingFileData', 'SimradRawPingFileData_mapped', 'SimradRawPing_mapped']
class FilePackageIndex_simradraw_FilePackageIndex:
    """
    """
    file_path: str
    file_size: int
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FilePackageIndex_simradraw_FilePackageIndex:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> FilePackageIndex_simradraw_FilePackageIndex:
        ...
    def __deepcopy__(self, arg0: dict) -> FilePackageIndex_simradraw_FilePackageIndex:
        ...
    def __eq__(self, other: FilePackageIndex_simradraw_FilePackageIndex) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> FilePackageIndex_simradraw_FilePackageIndex:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def datagram_info_data(self) -> list[...]:
        """
        < all datagrams
        """
    @datagram_info_data.setter
    def datagram_info_data(self, arg0: list[...]) -> None:
        ...
class SimradRawPing(themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, SimradRawPingCommon):
    """
    """
    def __copy__(self) -> SimradRawPing:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPing:
        ...
    def copy(self) -> SimradRawPing:
        """
        return a copy using the c++ default copy constructor
        """
class SimradRawPingCommon(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingCommon):
    """
    """
    def __copy__(self) -> SimradRawPingCommon:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingCommon:
        ...
    def copy(self) -> SimradRawPingCommon:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def file_data(self) -> SimradRawPingFileData:
        ...
class SimradRawPingCommon_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingCommon):
    """
    """
    def __copy__(self) -> SimradRawPingCommon_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingCommon_mapped:
        ...
    def copy(self) -> SimradRawPingCommon_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def file_data(self) -> SimradRawPingFileData_mapped:
        ...
class SimradRawPingFileData(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingFileData):
    """
    """
    def __copy__(self) -> SimradRawPingFileData:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingFileData:
        ...
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawPingFileData:
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    def get_parameter(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel:
        ...
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    @typing.overload
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[..., ...]:
        ...
    @typing.overload
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    @typing.overload
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class SimradRawPingFileData_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingFileData):
    """
    """
    def __copy__(self) -> SimradRawPingFileData_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingFileData_mapped:
        ...
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawPingFileData_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    def get_parameter(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel:
        ...
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    @typing.overload
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[...]:
        ...
    @typing.overload
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    @typing.overload
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class SimradRawPing_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, SimradRawPingCommon_mapped):
    """
    """
    def __copy__(self) -> SimradRawPing_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPing_mapped:
        ...
    def copy(self) -> SimradRawPing_mapped:
        """
        return a copy using the c++ default copy constructor
        """
