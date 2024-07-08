"""
SimradRaw EK60 and EK80 file data types
"""
from __future__ import annotations
import numpy
import themachinethatgoesping.echosounders_cppy.filetemplates
import themachinethatgoesping.echosounders_cppy.simradraw
import themachinethatgoesping.echosounders_cppy.simradraw.datagrams
import themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams
import typing
__all__ = ['FilePackageIndex_simradraw_FilePackageIndex', 'SimradRawPing', 'SimradRawPingBottom', 'SimradRawPingBottom_stream', 'SimradRawPingCommon', 'SimradRawPingCommon_stream', 'SimradRawPingFileData', 'SimradRawPingFileData_stream', 'SimradRawPingWatercolumn', 'SimradRawPingWatercolumn_stream', 'SimradRawPing_stream']
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
class SimradRawPingBottom(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingBottom, SimradRawPingCommon):
    """
    """
    def __copy__(self) -> SimradRawPingBottom:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingBottom:
        ...
    def copy(self) -> SimradRawPingBottom:
        """
        return a copy using the c++ default copy constructor
        """
class SimradRawPingBottom_stream(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingBottom, SimradRawPingCommon_stream):
    """
    """
    def __copy__(self) -> SimradRawPingBottom_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingBottom_stream:
        ...
    def copy(self) -> SimradRawPingBottom_stream:
        """
        return a copy using the c++ default copy constructor
        """
class SimradRawPingCommon:
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
class SimradRawPingCommon_stream:
    """
    """
    def __copy__(self) -> SimradRawPingCommon_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingCommon_stream:
        ...
    def copy(self) -> SimradRawPingCommon_stream:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def file_data(self) -> SimradRawPingFileData_stream:
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
    def get_environmnet(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Environment:
        ...
    def get_parameter(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel:
        ...
    def get_ping_data(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3:
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
    def read_sample_data(self, dB: bool = True) -> numpy.ndarray[numpy.float32]:
        ...
class SimradRawPingFileData_stream(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingFileData):
    """
    """
    def __copy__(self) -> SimradRawPingFileData_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingFileData_stream:
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
    def copy(self) -> SimradRawPingFileData_stream:
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
    def get_environmnet(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Environment:
        ...
    def get_parameter(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel:
        ...
    def get_ping_data(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3:
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
    def read_sample_data(self, dB: bool = True) -> numpy.ndarray[numpy.float32]:
        ...
class SimradRawPingWatercolumn(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingWatercolumn, SimradRawPingCommon):
    """
    """
    def __copy__(self) -> SimradRawPingWatercolumn:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingWatercolumn:
        ...
    def copy(self) -> SimradRawPingWatercolumn:
        """
        return a copy using the c++ default copy constructor
        """
class SimradRawPingWatercolumn_stream(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingWatercolumn, SimradRawPingCommon_stream):
    """
    """
    def __copy__(self) -> SimradRawPingWatercolumn_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingWatercolumn_stream:
        ...
    def copy(self) -> SimradRawPingWatercolumn_stream:
        """
        return a copy using the c++ default copy constructor
        """
class SimradRawPing_stream(themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, SimradRawPingCommon_stream):
    """
    """
    def __copy__(self) -> SimradRawPing_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPing_stream:
        ...
    def copy(self) -> SimradRawPing_stream:
        """
        return a copy using the c++ default copy constructor
        """
