"""
SimradRaw EK60 and EK80 file data types
"""
from __future__ import annotations
import themachinethatgoesping.echosounders_cppy.filetemplates
import themachinethatgoesping.echosounders_cppy.simradraw.datagrams
import themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams
import themachinethatgoesping.echosounders_cppy.simradraw.datagrams.raw3datatypes
import typing
__all__ = ['FileInfoData_simradraw_FileInfoData', 'SimradRawPing', 'SimradRawPingRawData', 'SimradRawPingRawData_mapped', 'SimradRawPing_mapped']
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
class SimradRawPing(themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping):
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
    def raw_data(self) -> SimradRawPingRawData:
        ...
class SimradRawPingRawData:
    """
    """
    def __copy__(self) -> SimradRawPingRawData:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingRawData:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawPingRawData:
        """
        return a copy using the c++ default copy constructor
        """
    def get_parameter(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel:
        ...
    def get_sample_data(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.raw3datatypes.RAW3DataSkipped | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.raw3datatypes.RAW3DataComplexFloat32 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.raw3datatypes.RAW3DataPowerAndAngle | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.raw3datatypes.RAW3DataPower | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.raw3datatypes.RAW3DataAngle:
        ...
    def has_angle(self) -> bool:
        ...
    def has_power(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def load(self) -> None:
        ...
    @typing.overload
    def load(self) -> None:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    @property
    def ping_data(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)
        """
class SimradRawPingRawData_mapped:
    """
    """
    def __copy__(self) -> SimradRawPingRawData_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingRawData_mapped:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawPingRawData_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def get_parameter(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel:
        ...
    def get_sample_data(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.raw3datatypes.RAW3DataSkipped | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.raw3datatypes.RAW3DataComplexFloat32 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.raw3datatypes.RAW3DataPowerAndAngle | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.raw3datatypes.RAW3DataPower | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.raw3datatypes.RAW3DataAngle:
        ...
    def has_angle(self) -> bool:
        ...
    def has_power(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def load(self) -> None:
        ...
    @typing.overload
    def load(self) -> None:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    @property
    def ping_data(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)
        """
class SimradRawPing_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping):
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
    def raw_data(self) -> SimradRawPingRawData_mapped:
        ...
