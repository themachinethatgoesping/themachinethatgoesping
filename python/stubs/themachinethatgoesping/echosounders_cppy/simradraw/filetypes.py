"""
SimradRaw EK60 and EK80 file data types
"""
from __future__ import annotations
import themachinethatgoesping.echosounders_cppy.filetemplates
__all__ = ['FileInfoData_simradraw_FileInfoData', 'SimradRawPing', 'SimradRawPingCommon', 'SimradRawPingCommon_mapped', 'SimradRawPingFileData', 'SimradRawPingFileData_mapped', 'SimradRawPing_mapped']
class FileInfoData_simradraw_FileInfoData:
    """
    """
    file_path: str
    file_size: int
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FileInfoData_simradraw_FileInfoData:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> FileInfoData_simradraw_FileInfoData:
        ...
    def __deepcopy__(self, arg0: dict) -> FileInfoData_simradraw_FileInfoData:
        ...
    def __eq__(self, other: FileInfoData_simradraw_FileInfoData) -> bool:
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
    def copy(self) -> FileInfoData_simradraw_FileInfoData:
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
    def datagram_infos(self) -> list[...]:
        """
        < all datagrams
        """
    @datagram_infos.setter
    def datagram_infos(self, arg0: list[...]) -> None:
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
class SimradRawPingFileData(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingFileData):
    """
    """
    def __copy__(self) -> SimradRawPingFileData:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingFileData:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawPingFileData:
        """
        return a copy using the c++ default copy constructor
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
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
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawPingFileData_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
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
