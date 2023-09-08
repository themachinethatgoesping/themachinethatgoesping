"""
Simrad EK60 and EK80 file data types
"""
from __future__ import annotations
import themachinethatgoesping.echosounders.filetemplates
import themachinethatgoesping.echosounders.simrad.datagrams
import themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams
import themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes
import typing
__all__ = ['FileInfoData_simrad_FileInfoData', 'SimradPing', 'SimradPingRawData', 'SimradPingRawData_mapped', 'SimradPing_mapped']
class FileInfoData_simrad_FileInfoData:
    """
    """
    file_path: str
    file_size: int
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> FileInfoData_simrad_FileInfoData:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> FileInfoData_simrad_FileInfoData:
        ...
    def __deepcopy__(self, arg0: dict) -> FileInfoData_simrad_FileInfoData:
        ...
    def __eq__(self, other: FileInfoData_simrad_FileInfoData) -> bool:
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
    def copy(self) -> FileInfoData_simrad_FileInfoData:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
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
class SimradPing(themachinethatgoesping.echosounders.filetemplates.I_Ping):
    """
    """
    def __copy__(self) -> SimradPing:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradPing:
        ...
    def copy(self) -> SimradPing:
        """
        return a copy using the c++ default copy constructor
        """
    def raw_data(self) -> SimradPingRawData:
        ...
class SimradPingRawData:
    """
    """
    def __copy__(self) -> SimradPingRawData:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradPingRawData:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradPingRawData:
        """
        return a copy using the c++ default copy constructor
        """
    def get_parameter(self) -> themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Parameter_Channel:
        ...
    def get_sample_data(self) -> themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataSkipped | themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataComplexFloat32 | themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataPowerAndAngle | themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataPower | themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataAngle:
        ...
    def has_angle(self) -> bool:
        ...
    def has_power(self) -> bool:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def load(self) -> None:
        ...
    @typing.overload
    def load(self) -> None:
        ...
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    @property
    def ping_data(self) -> themachinethatgoesping.echosounders.simrad.datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)
        """
class SimradPingRawData_mapped:
    """
    """
    def __copy__(self) -> SimradPingRawData_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradPingRawData_mapped:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradPingRawData_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def get_parameter(self) -> themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Parameter_Channel:
        ...
    def get_sample_data(self) -> themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataSkipped | themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataComplexFloat32 | themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataPowerAndAngle | themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataPower | themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataAngle:
        ...
    def has_angle(self) -> bool:
        ...
    def has_power(self) -> bool:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def load(self) -> None:
        ...
    @typing.overload
    def load(self) -> None:
        ...
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    @property
    def ping_data(self) -> themachinethatgoesping.echosounders.simrad.datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)
        """
class SimradPing_mapped(themachinethatgoesping.echosounders.filetemplates.I_Ping):
    """
    """
    def __copy__(self) -> SimradPing_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradPing_mapped:
        ...
    def copy(self) -> SimradPing_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def raw_data(self) -> SimradPingRawData_mapped:
        ...
