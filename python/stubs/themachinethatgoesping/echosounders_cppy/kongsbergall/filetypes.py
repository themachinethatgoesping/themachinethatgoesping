"""
KongsbergAll EK60 and EK80 file data types
"""
from __future__ import annotations
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import themachinethatgoesping.echosounders_cppy.filetemplates
import themachinethatgoesping.echosounders_cppy.kongsbergall
import themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams
import themachinethatgoesping.echosounders_cppy.pingtools
import typing
__all__ = ['FileInfoData_kongsbergall_FileInfoData', 'KongsbergAllPing', 'KongsbergAllPingBottom', 'KongsbergAllPingBottom_mapped', 'KongsbergAllPingCommon', 'KongsbergAllPingCommon_mapped', 'KongsbergAllPingFileData', 'KongsbergAllPingFileData_mapped', 'KongsbergAllPingWatercolumn', 'KongsbergAllPingWatercolumn_mapped', 'KongsbergAllPing_mapped']
class FileInfoData_kongsbergall_FileInfoData:
    """
    """
    file_path: str
    file_size: int
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FileInfoData_kongsbergall_FileInfoData:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> FileInfoData_kongsbergall_FileInfoData:
        ...
    def __deepcopy__(self, arg0: dict) -> FileInfoData_kongsbergall_FileInfoData:
        ...
    def __eq__(self, other: FileInfoData_kongsbergall_FileInfoData) -> bool:
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
    def copy(self) -> FileInfoData_kongsbergall_FileInfoData:
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
class KongsbergAllPing(themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, KongsbergAllPingCommon):
    """
    """
    def __copy__(self) -> KongsbergAllPing:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPing:
        ...
    def copy(self) -> KongsbergAllPing:
        """
        return a copy using the c++ default copy constructor
        """
class KongsbergAllPingBottom(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingBottom, KongsbergAllPingCommon):
    """
    """
    def __copy__(self) -> KongsbergAllPingBottom:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingBottom:
        ...
    def copy(self) -> KongsbergAllPingBottom:
        """
        return a copy using the c++ default copy constructor
        """
class KongsbergAllPingBottom_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingBottom, KongsbergAllPingCommon_mapped):
    """
    """
    def __copy__(self) -> KongsbergAllPingBottom_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingBottom_mapped:
        ...
    def copy(self) -> KongsbergAllPingBottom_mapped:
        """
        return a copy using the c++ default copy constructor
        """
class KongsbergAllPingCommon(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingCommon):
    """
    """
    def __copy__(self) -> KongsbergAllPingCommon:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingCommon:
        ...
    def copy(self) -> KongsbergAllPingCommon:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def file_data(self) -> KongsbergAllPingFileData:
        ...
class KongsbergAllPingCommon_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingCommon):
    """
    """
    def __copy__(self) -> KongsbergAllPingCommon_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingCommon_mapped:
        ...
    def copy(self) -> KongsbergAllPingCommon_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def file_data(self) -> KongsbergAllPingFileData_mapped:
        ...
class KongsbergAllPingFileData(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingFileData):
    """
    """
    def __copy__(self) -> KongsbergAllPingFileData:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingFileData:
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
    def copy(self) -> KongsbergAllPingFileData:
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def get_runtime_parameters(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RuntimeParameters:
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
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
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
    def read_merged_watercolumndatagram(self, skip_data: bool = False) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.WatercolumnDatagram:
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
class KongsbergAllPingFileData_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingFileData):
    """
    """
    def __copy__(self) -> KongsbergAllPingFileData_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingFileData_mapped:
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
    def copy(self) -> KongsbergAllPingFileData_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def get_runtime_parameters(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RuntimeParameters:
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
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
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
    def read_merged_watercolumndatagram(self, skip_data: bool = False) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.WatercolumnDatagram:
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
class KongsbergAllPingWatercolumn(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingWatercolumn, KongsbergAllPingCommon):
    """
    """
    def __copy__(self) -> KongsbergAllPingWatercolumn:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingWatercolumn:
        ...
    def copy(self) -> KongsbergAllPingWatercolumn:
        """
        return a copy using the c++ default copy constructor
        """
class KongsbergAllPingWatercolumn_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingWatercolumn, KongsbergAllPingCommon_mapped):
    """
    """
    def __copy__(self) -> KongsbergAllPingWatercolumn_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingWatercolumn_mapped:
        ...
    def copy(self) -> KongsbergAllPingWatercolumn_mapped:
        """
        return a copy using the c++ default copy constructor
        """
class KongsbergAllPing_mapped(themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, KongsbergAllPingCommon_mapped):
    """
    """
    def __copy__(self) -> KongsbergAllPing_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPing_mapped:
        ...
    def copy(self) -> KongsbergAllPing_mapped:
        """
        return a copy using the c++ default copy constructor
        """
