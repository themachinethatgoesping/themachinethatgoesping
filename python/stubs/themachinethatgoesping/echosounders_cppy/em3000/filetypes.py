"""
EM3000 EK60 and EK80 file data types
"""
from __future__ import annotations
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import themachinethatgoesping.echosounders_cppy.em3000
import themachinethatgoesping.echosounders_cppy.em3000.datagrams
import themachinethatgoesping.echosounders_cppy.filetemplates
import themachinethatgoesping.echosounders_cppy.pingtools
import typing
__all__ = ['EM3000Ping', 'EM3000PingBottom', 'EM3000PingBottom_mapped', 'EM3000PingCommon', 'EM3000PingCommon_mapped', 'EM3000PingRawData', 'EM3000PingRawData_mapped', 'EM3000PingWatercolumn', 'EM3000PingWatercolumn_mapped', 'EM3000Ping_mapped', 'FileInfoData_em3000_FileInfoData']
class EM3000Ping(themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, EM3000PingCommon):
    """
    """
    def __copy__(self) -> EM3000Ping:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000Ping:
        ...
    def copy(self) -> EM3000Ping:
        """
        return a copy using the c++ default copy constructor
        """
class EM3000PingBottom(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingBottom, EM3000PingCommon):
    """
    """
    def __copy__(self) -> EM3000PingBottom:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingBottom:
        ...
    def copy(self) -> EM3000PingBottom:
        """
        return a copy using the c++ default copy constructor
        """
class EM3000PingBottom_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingBottom, EM3000PingCommon_mapped):
    """
    """
    def __copy__(self) -> EM3000PingBottom_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingBottom_mapped:
        ...
    def copy(self) -> EM3000PingBottom_mapped:
        """
        return a copy using the c++ default copy constructor
        """
class EM3000PingCommon(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingCommon):
    """
    """
    def __copy__(self) -> EM3000PingCommon:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingCommon:
        ...
    def copy(self) -> EM3000PingCommon:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def raw_data(self) -> EM3000PingRawData:
        ...
class EM3000PingCommon_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingCommon):
    """
    """
    def __copy__(self) -> EM3000PingCommon_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingCommon_mapped:
        ...
    def copy(self) -> EM3000PingCommon_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def raw_data(self) -> EM3000PingRawData_mapped:
        ...
class EM3000PingRawData:
    """
    """
    def __copy__(self) -> EM3000PingRawData:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingRawData:
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
    def copy(self) -> EM3000PingRawData:
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.em3000.t_EM3000DatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.em3000.t_EM3000DatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.em3000.t_EM3000DatagramIdentifier) -> typing.Any:
        ...
    def get_runtime_parameters(self) -> themachinethatgoesping.echosounders_cppy.em3000.datagrams.RuntimeParameters:
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
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.em3000.t_EM3000DatagramIdentifier]:
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
    def read_merged_watercolumndatagram(self, skip_data: bool = False) -> themachinethatgoesping.echosounders_cppy.em3000.datagrams.WatercolumnDatagram:
        ...
    @typing.overload
    def read_xyz(self) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1:
        """
        read XYZ for the bottom detection datagram
        
        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>
        """
    @typing.overload
    def read_xyz(self, selection: themachinethatgoesping.echosounders_cppy.pingtools.BeamSelection) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1:
        """
        read XYZ for the specified beams from the bottom detection datagram
        Note: if the beam numbers from the beam selection exceed the number of
        beams in the datagram, the corresponding XYZ values will be NaN
        
        Parameter ``bs``:
            beam selection
        
        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>
        """
class EM3000PingRawData_mapped:
    """
    """
    def __copy__(self) -> EM3000PingRawData_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingRawData_mapped:
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
    def copy(self) -> EM3000PingRawData_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.em3000.t_EM3000DatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.em3000.t_EM3000DatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.em3000.t_EM3000DatagramIdentifier) -> typing.Any:
        ...
    def get_runtime_parameters(self) -> themachinethatgoesping.echosounders_cppy.em3000.datagrams.RuntimeParameters:
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
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.em3000.t_EM3000DatagramIdentifier]:
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
    def read_merged_watercolumndatagram(self, skip_data: bool = False) -> themachinethatgoesping.echosounders_cppy.em3000.datagrams.WatercolumnDatagram:
        ...
    @typing.overload
    def read_xyz(self) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1:
        """
        read XYZ for the bottom detection datagram
        
        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>
        """
    @typing.overload
    def read_xyz(self, selection: themachinethatgoesping.echosounders_cppy.pingtools.BeamSelection) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1:
        """
        read XYZ for the specified beams from the bottom detection datagram
        Note: if the beam numbers from the beam selection exceed the number of
        beams in the datagram, the corresponding XYZ values will be NaN
        
        Parameter ``bs``:
            beam selection
        
        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>
        """
class EM3000PingWatercolumn(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingWatercolumn, EM3000PingCommon):
    """
    """
    def __copy__(self) -> EM3000PingWatercolumn:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingWatercolumn:
        ...
    def copy(self) -> EM3000PingWatercolumn:
        """
        return a copy using the c++ default copy constructor
        """
class EM3000PingWatercolumn_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingWatercolumn, EM3000PingCommon_mapped):
    """
    """
    def __copy__(self) -> EM3000PingWatercolumn_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingWatercolumn_mapped:
        ...
    def copy(self) -> EM3000PingWatercolumn_mapped:
        """
        return a copy using the c++ default copy constructor
        """
class EM3000Ping_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, EM3000PingCommon_mapped):
    """
    """
    def __copy__(self) -> EM3000Ping_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000Ping_mapped:
        ...
    def copy(self) -> EM3000Ping_mapped:
        """
        return a copy using the c++ default copy constructor
        """
class FileInfoData_em3000_FileInfoData:
    """
    """
    file_path: str
    file_size: int
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FileInfoData_em3000_FileInfoData:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> FileInfoData_em3000_FileInfoData:
        ...
    def __deepcopy__(self, arg0: dict) -> FileInfoData_em3000_FileInfoData:
        ...
    def __eq__(self, other: FileInfoData_em3000_FileInfoData) -> bool:
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
    def copy(self) -> FileInfoData_em3000_FileInfoData:
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
