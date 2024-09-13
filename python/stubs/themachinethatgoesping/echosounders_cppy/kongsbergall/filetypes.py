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
__all__ = ['FilePackageIndex_kongsbergall_FilePackageIndex', 'KongsbergAllPing', 'KongsbergAllPingBottom', 'KongsbergAllPingBottom_stream', 'KongsbergAllPingCommon', 'KongsbergAllPingCommon_stream', 'KongsbergAllPingFileData', 'KongsbergAllPingFileData_stream', 'KongsbergAllPingWatercolumn', 'KongsbergAllPingWatercolumn_stream', 'KongsbergAllPing_stream']
class FilePackageIndex_kongsbergall_FilePackageIndex:
    """
    """
    file_path: str
    file_size: int
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FilePackageIndex_kongsbergall_FilePackageIndex:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> FilePackageIndex_kongsbergall_FilePackageIndex:
        ...
    def __deepcopy__(self, arg0: dict) -> FilePackageIndex_kongsbergall_FilePackageIndex:
        ...
    def __eq__(self, other: FilePackageIndex_kongsbergall_FilePackageIndex) -> bool:
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
    def copy(self) -> FilePackageIndex_kongsbergall_FilePackageIndex:
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
class KongsbergAllPingBottom_stream(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingBottom, KongsbergAllPingCommon_stream):
    """
    """
    def __copy__(self) -> KongsbergAllPingBottom_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingBottom_stream:
        ...
    def copy(self) -> KongsbergAllPingBottom_stream:
        """
        return a copy using the c++ default copy constructor
        """
class KongsbergAllPingCommon:
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
class KongsbergAllPingCommon_stream:
    """
    """
    def __copy__(self) -> KongsbergAllPingCommon_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingCommon_stream:
        ...
    def copy(self) -> KongsbergAllPingCommon_stream:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def file_data(self) -> KongsbergAllPingFileData_stream:
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
class KongsbergAllPingFileData_stream(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingFileData):
    """
    """
    def __copy__(self) -> KongsbergAllPingFileData_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingFileData_stream:
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
    def copy(self) -> KongsbergAllPingFileData_stream:
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
    def get_tvg_factor_applied(self) -> int:
        ...
    def get_tvg_offset(self) -> int:
        ...
class KongsbergAllPingWatercolumn_stream(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingWatercolumn, KongsbergAllPingCommon_stream):
    """
    """
    def __copy__(self) -> KongsbergAllPingWatercolumn_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingWatercolumn_stream:
        ...
    def copy(self) -> KongsbergAllPingWatercolumn_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def get_tvg_factor_applied(self) -> int:
        ...
    def get_tvg_offset(self) -> int:
        ...
class KongsbergAllPing_stream(themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, KongsbergAllPingCommon_stream):
    """
    """
    def __copy__(self) -> KongsbergAllPing_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPing_stream:
        ...
    def copy(self) -> KongsbergAllPing_stream:
        """
        return a copy using the c++ default copy constructor
        """
