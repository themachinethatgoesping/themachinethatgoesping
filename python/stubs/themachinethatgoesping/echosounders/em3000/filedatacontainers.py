"""
EM3000 (kongsberg .all / .wcd) file data container classes
"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000
import themachinethatgoesping.echosounders.em3000.datagrams
import themachinethatgoesping.echosounders.em3000.filetypes
import themachinethatgoesping.tools.pyhelper
import typing
__all__ = ['EM3000DatagramContainer_AttitudeDatagram', 'EM3000DatagramContainer_AttitudeDatagram_mapped', 'EM3000DatagramContainer_ClockDatagram', 'EM3000DatagramContainer_ClockDatagram_mapped', 'EM3000DatagramContainer_DepthOrHeightDatagram', 'EM3000DatagramContainer_DepthOrHeightDatagram_mapped', 'EM3000DatagramContainer_ExtraDetections', 'EM3000DatagramContainer_ExtraDetections_mapped', 'EM3000DatagramContainer_ExtraParameters', 'EM3000DatagramContainer_ExtraParameters_mapped', 'EM3000DatagramContainer_Header', 'EM3000DatagramContainer_Header_mapped', 'EM3000DatagramContainer_HeadingDatagram', 'EM3000DatagramContainer_HeadingDatagram_mapped', 'EM3000DatagramContainer_InstallationParameters', 'EM3000DatagramContainer_InstallationParameters_mapped', 'EM3000DatagramContainer_NetworkAttitudeVelocityDatagram', 'EM3000DatagramContainer_NetworkAttitudeVelocityDatagram_mapped', 'EM3000DatagramContainer_PUIDOutput', 'EM3000DatagramContainer_PUIDOutput_mapped', 'EM3000DatagramContainer_PUStatusOutput', 'EM3000DatagramContainer_PUStatusOutput_mapped', 'EM3000DatagramContainer_PositionDatagram', 'EM3000DatagramContainer_PositionDatagram_mapped', 'EM3000DatagramContainer_QualityFactorDatagram', 'EM3000DatagramContainer_QualityFactorDatagram_mapped', 'EM3000DatagramContainer_RawRangeAndAngle', 'EM3000DatagramContainer_RawRangeAndAngle_mapped', 'EM3000DatagramContainer_RuntimeParameters', 'EM3000DatagramContainer_RuntimeParameters_mapped', 'EM3000DatagramContainer_SeabedImageData', 'EM3000DatagramContainer_SeabedImageData_mapped', 'EM3000DatagramContainer_SingleBeamEchoSounderDepth', 'EM3000DatagramContainer_SingleBeamEchoSounderDepth_mapped', 'EM3000DatagramContainer_SoundSpeedProfileDatagram', 'EM3000DatagramContainer_SoundSpeedProfileDatagram_mapped', 'EM3000DatagramContainer_SurfaceSoundSpeedDatagram', 'EM3000DatagramContainer_SurfaceSoundSpeedDatagram_mapped', 'EM3000DatagramContainer_Unknown', 'EM3000DatagramContainer_Unknown_mapped', 'EM3000DatagramContainer_Variant', 'EM3000DatagramContainer_Variant_SkippedData', 'EM3000DatagramContainer_Variant_SkippedData_mapped', 'EM3000DatagramContainer_Variant_mapped', 'EM3000DatagramContainer_WatercolumnDatagram', 'EM3000DatagramContainer_WatercolumnDatagram_SkippedData', 'EM3000DatagramContainer_WatercolumnDatagram_SkippedData_mapped', 'EM3000DatagramContainer_WatercolumnDatagram_mapped', 'EM3000DatagramContainer_XYZDatagram', 'EM3000DatagramContainer_XYZDatagram_mapped', 'EM3000PingContainer', 'EM3000PingContainer_mapped']
class EM3000DatagramContainer_AttitudeDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_AttitudeDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_AttitudeDatagram:
        ...
    def __copy__(self) -> EM3000DatagramContainer_AttitudeDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_AttitudeDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.AttitudeDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_AttitudeDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_AttitudeDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_AttitudeDatagram]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_AttitudeDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_AttitudeDatagram:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_AttitudeDatagram_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_AttitudeDatagram_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_AttitudeDatagram_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_AttitudeDatagram_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_AttitudeDatagram_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.AttitudeDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_AttitudeDatagram_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_AttitudeDatagram_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_AttitudeDatagram_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_AttitudeDatagram_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_AttitudeDatagram_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_ClockDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_ClockDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_ClockDatagram:
        ...
    def __copy__(self) -> EM3000DatagramContainer_ClockDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_ClockDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.ClockDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_ClockDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_ClockDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_ClockDatagram]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_ClockDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_ClockDatagram:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_ClockDatagram_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_ClockDatagram_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_ClockDatagram_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_ClockDatagram_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_ClockDatagram_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.ClockDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_ClockDatagram_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_ClockDatagram_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_ClockDatagram_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_ClockDatagram_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_ClockDatagram_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_DepthOrHeightDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_DepthOrHeightDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_DepthOrHeightDatagram:
        ...
    def __copy__(self) -> EM3000DatagramContainer_DepthOrHeightDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_DepthOrHeightDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.DepthOrHeightDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_DepthOrHeightDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_DepthOrHeightDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_DepthOrHeightDatagram]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_DepthOrHeightDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_DepthOrHeightDatagram:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_DepthOrHeightDatagram_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_DepthOrHeightDatagram_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_DepthOrHeightDatagram_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_DepthOrHeightDatagram_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_DepthOrHeightDatagram_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.DepthOrHeightDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_DepthOrHeightDatagram_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_DepthOrHeightDatagram_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_DepthOrHeightDatagram_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_DepthOrHeightDatagram_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_DepthOrHeightDatagram_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_ExtraDetections:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_ExtraDetections:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_ExtraDetections:
        ...
    def __copy__(self) -> EM3000DatagramContainer_ExtraDetections:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_ExtraDetections:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.ExtraDetections:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_ExtraDetections:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_ExtraDetections:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_ExtraDetections]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_ExtraDetections:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_ExtraDetections:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_ExtraDetections_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_ExtraDetections_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_ExtraDetections_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_ExtraDetections_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_ExtraDetections_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.ExtraDetections:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_ExtraDetections_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_ExtraDetections_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_ExtraDetections_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_ExtraDetections_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_ExtraDetections_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_ExtraParameters:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_ExtraParameters:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_ExtraParameters:
        ...
    def __copy__(self) -> EM3000DatagramContainer_ExtraParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_ExtraParameters:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.ExtraParameters:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_ExtraParameters:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_ExtraParameters:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_ExtraParameters]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_ExtraParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_ExtraParameters:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_ExtraParameters_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_ExtraParameters_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_ExtraParameters_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_ExtraParameters_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_ExtraParameters_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.ExtraParameters:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_ExtraParameters_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_ExtraParameters_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_ExtraParameters_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_ExtraParameters_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_ExtraParameters_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_Header:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_Header:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_Header:
        ...
    def __copy__(self) -> EM3000DatagramContainer_Header:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_Header:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.EM3000Datagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_Header:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_Header:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_Header]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_Header:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_Header:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_Header_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_Header_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_Header_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_Header_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_Header_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.EM3000Datagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_Header_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_Header_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_Header_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_Header_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_Header_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_HeadingDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_HeadingDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_HeadingDatagram:
        ...
    def __copy__(self) -> EM3000DatagramContainer_HeadingDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_HeadingDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.HeadingDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_HeadingDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_HeadingDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_HeadingDatagram]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_HeadingDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_HeadingDatagram:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_HeadingDatagram_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_HeadingDatagram_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_HeadingDatagram_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_HeadingDatagram_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_HeadingDatagram_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.HeadingDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_HeadingDatagram_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_HeadingDatagram_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_HeadingDatagram_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_HeadingDatagram_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_HeadingDatagram_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_InstallationParameters:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_InstallationParameters:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_InstallationParameters:
        ...
    def __copy__(self) -> EM3000DatagramContainer_InstallationParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_InstallationParameters:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.InstallationParameters:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_InstallationParameters:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_InstallationParameters:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_InstallationParameters]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_InstallationParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_InstallationParameters:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_InstallationParameters_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_InstallationParameters_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_InstallationParameters_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_InstallationParameters_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_InstallationParameters_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.InstallationParameters:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_InstallationParameters_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_InstallationParameters_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_InstallationParameters_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_InstallationParameters_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_InstallationParameters_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_NetworkAttitudeVelocityDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def __copy__(self) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.NetworkAttitudeVelocityDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_NetworkAttitudeVelocityDatagram]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_NetworkAttitudeVelocityDatagram_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.NetworkAttitudeVelocityDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_NetworkAttitudeVelocityDatagram_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_NetworkAttitudeVelocityDatagram_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_PUIDOutput:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_PUIDOutput:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_PUIDOutput:
        ...
    def __copy__(self) -> EM3000DatagramContainer_PUIDOutput:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_PUIDOutput:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.PUIDOutput:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_PUIDOutput:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_PUIDOutput:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_PUIDOutput]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_PUIDOutput:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_PUIDOutput:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_PUIDOutput_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_PUIDOutput_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_PUIDOutput_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_PUIDOutput_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_PUIDOutput_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.PUIDOutput:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_PUIDOutput_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_PUIDOutput_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_PUIDOutput_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_PUIDOutput_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_PUIDOutput_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_PUStatusOutput:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_PUStatusOutput:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_PUStatusOutput:
        ...
    def __copy__(self) -> EM3000DatagramContainer_PUStatusOutput:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_PUStatusOutput:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.PUStatusOutput:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_PUStatusOutput:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_PUStatusOutput:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_PUStatusOutput]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_PUStatusOutput:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_PUStatusOutput:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_PUStatusOutput_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_PUStatusOutput_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_PUStatusOutput_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_PUStatusOutput_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_PUStatusOutput_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.PUStatusOutput:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_PUStatusOutput_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_PUStatusOutput_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_PUStatusOutput_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_PUStatusOutput_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_PUStatusOutput_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_PositionDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_PositionDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_PositionDatagram:
        ...
    def __copy__(self) -> EM3000DatagramContainer_PositionDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_PositionDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.PositionDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_PositionDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_PositionDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_PositionDatagram]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_PositionDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_PositionDatagram:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_PositionDatagram_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_PositionDatagram_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_PositionDatagram_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_PositionDatagram_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_PositionDatagram_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.PositionDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_PositionDatagram_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_PositionDatagram_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_PositionDatagram_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_PositionDatagram_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_PositionDatagram_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_QualityFactorDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_QualityFactorDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_QualityFactorDatagram:
        ...
    def __copy__(self) -> EM3000DatagramContainer_QualityFactorDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_QualityFactorDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.QualityFactorDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_QualityFactorDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_QualityFactorDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_QualityFactorDatagram]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_QualityFactorDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_QualityFactorDatagram:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_QualityFactorDatagram_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_QualityFactorDatagram_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_QualityFactorDatagram_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_QualityFactorDatagram_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_QualityFactorDatagram_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.QualityFactorDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_QualityFactorDatagram_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_QualityFactorDatagram_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_QualityFactorDatagram_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_QualityFactorDatagram_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_QualityFactorDatagram_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_RawRangeAndAngle:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_RawRangeAndAngle:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_RawRangeAndAngle:
        ...
    def __copy__(self) -> EM3000DatagramContainer_RawRangeAndAngle:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_RawRangeAndAngle:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.RawRangeAndAngle:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_RawRangeAndAngle:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_RawRangeAndAngle:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_RawRangeAndAngle]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_RawRangeAndAngle:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_RawRangeAndAngle:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_RawRangeAndAngle_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_RawRangeAndAngle_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_RawRangeAndAngle_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_RawRangeAndAngle_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_RawRangeAndAngle_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.RawRangeAndAngle:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_RawRangeAndAngle_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_RawRangeAndAngle_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_RawRangeAndAngle_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_RawRangeAndAngle_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_RawRangeAndAngle_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_RuntimeParameters:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_RuntimeParameters:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_RuntimeParameters:
        ...
    def __copy__(self) -> EM3000DatagramContainer_RuntimeParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_RuntimeParameters:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.RuntimeParameters:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_RuntimeParameters:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_RuntimeParameters:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_RuntimeParameters]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_RuntimeParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_RuntimeParameters:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_RuntimeParameters_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_RuntimeParameters_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_RuntimeParameters_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_RuntimeParameters_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_RuntimeParameters_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.RuntimeParameters:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_RuntimeParameters_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_RuntimeParameters_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_RuntimeParameters_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_RuntimeParameters_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_RuntimeParameters_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_SeabedImageData:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_SeabedImageData:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_SeabedImageData:
        ...
    def __copy__(self) -> EM3000DatagramContainer_SeabedImageData:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_SeabedImageData:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.SeabedImageData:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_SeabedImageData:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_SeabedImageData:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_SeabedImageData]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_SeabedImageData:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_SeabedImageData:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_SeabedImageData_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_SeabedImageData_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_SeabedImageData_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_SeabedImageData_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_SeabedImageData_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.SeabedImageData:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_SeabedImageData_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_SeabedImageData_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_SeabedImageData_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_SeabedImageData_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_SeabedImageData_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_SingleBeamEchoSounderDepth:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def __copy__(self) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.SingleBeamEchoSounderDepth:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_SingleBeamEchoSounderDepth]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_SingleBeamEchoSounderDepth_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.SingleBeamEchoSounderDepth:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_SingleBeamEchoSounderDepth_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_SingleBeamEchoSounderDepth_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_SoundSpeedProfileDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_SoundSpeedProfileDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_SoundSpeedProfileDatagram:
        ...
    def __copy__(self) -> EM3000DatagramContainer_SoundSpeedProfileDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_SoundSpeedProfileDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.SoundSpeedProfileDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_SoundSpeedProfileDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_SoundSpeedProfileDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_SoundSpeedProfileDatagram]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_SoundSpeedProfileDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_SoundSpeedProfileDatagram:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_SoundSpeedProfileDatagram_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_SoundSpeedProfileDatagram_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_SoundSpeedProfileDatagram_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_SoundSpeedProfileDatagram_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_SoundSpeedProfileDatagram_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.SoundSpeedProfileDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_SoundSpeedProfileDatagram_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_SoundSpeedProfileDatagram_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_SoundSpeedProfileDatagram_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_SoundSpeedProfileDatagram_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_SoundSpeedProfileDatagram_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_SurfaceSoundSpeedDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def __copy__(self) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.SurfaceSoundSpeedDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_SurfaceSoundSpeedDatagram]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_SurfaceSoundSpeedDatagram_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.SurfaceSoundSpeedDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_SurfaceSoundSpeedDatagram_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_SurfaceSoundSpeedDatagram_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_Unknown:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_Unknown:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_Unknown:
        ...
    def __copy__(self) -> EM3000DatagramContainer_Unknown:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_Unknown:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.EM3000Unknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_Unknown:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_Unknown:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_Unknown]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_Unknown:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_Unknown:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_Unknown_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_Unknown_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_Unknown_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_Unknown_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_Unknown_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.EM3000Unknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_Unknown_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_Unknown_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_Unknown_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_Unknown_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_Unknown_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_Variant:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_Variant:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_Variant:
        ...
    def __copy__(self) -> EM3000DatagramContainer_Variant:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_Variant:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.EM3000Datagram | themachinethatgoesping.echosounders.em3000.datagrams.XYZDatagram | themachinethatgoesping.echosounders.em3000.datagrams.ExtraDetections | themachinethatgoesping.echosounders.em3000.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders.em3000.datagrams.SeabedImageData | themachinethatgoesping.echosounders.em3000.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders.em3000.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders.em3000.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders.em3000.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders.em3000.datagrams.ClockDatagram | themachinethatgoesping.echosounders.em3000.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders.em3000.datagrams.HeadingDatagram | themachinethatgoesping.echosounders.em3000.datagrams.PositionDatagram | themachinethatgoesping.echosounders.em3000.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders.em3000.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders.em3000.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders.em3000.datagrams.InstallationParameters | themachinethatgoesping.echosounders.em3000.datagrams.RuntimeParameters | themachinethatgoesping.echosounders.em3000.datagrams.ExtraParameters | themachinethatgoesping.echosounders.em3000.datagrams.PUIDOutput | themachinethatgoesping.echosounders.em3000.datagrams.PUStatusOutput | themachinethatgoesping.echosounders.em3000.datagrams.EM3000Unknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_Variant:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_Variant:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_Variant]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_Variant:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_Variant:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_Variant_SkippedData:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_Variant_SkippedData:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_Variant_SkippedData:
        ...
    def __copy__(self) -> EM3000DatagramContainer_Variant_SkippedData:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_Variant_SkippedData:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.EM3000Datagram | themachinethatgoesping.echosounders.em3000.datagrams.XYZDatagram | themachinethatgoesping.echosounders.em3000.datagrams.ExtraDetections | themachinethatgoesping.echosounders.em3000.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders.em3000.datagrams.SeabedImageData | themachinethatgoesping.echosounders.em3000.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders.em3000.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders.em3000.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders.em3000.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders.em3000.datagrams.ClockDatagram | themachinethatgoesping.echosounders.em3000.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders.em3000.datagrams.HeadingDatagram | themachinethatgoesping.echosounders.em3000.datagrams.PositionDatagram | themachinethatgoesping.echosounders.em3000.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders.em3000.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders.em3000.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders.em3000.datagrams.InstallationParameters | themachinethatgoesping.echosounders.em3000.datagrams.RuntimeParameters | themachinethatgoesping.echosounders.em3000.datagrams.ExtraParameters | themachinethatgoesping.echosounders.em3000.datagrams.PUIDOutput | themachinethatgoesping.echosounders.em3000.datagrams.PUStatusOutput | themachinethatgoesping.echosounders.em3000.datagrams.EM3000Unknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_Variant_SkippedData:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_Variant_SkippedData:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_Variant_SkippedData]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_Variant_SkippedData:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_Variant_SkippedData:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_Variant_SkippedData_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_Variant_SkippedData_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_Variant_SkippedData_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_Variant_SkippedData_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_Variant_SkippedData_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.EM3000Datagram | themachinethatgoesping.echosounders.em3000.datagrams.XYZDatagram | themachinethatgoesping.echosounders.em3000.datagrams.ExtraDetections | themachinethatgoesping.echosounders.em3000.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders.em3000.datagrams.SeabedImageData | themachinethatgoesping.echosounders.em3000.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders.em3000.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders.em3000.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders.em3000.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders.em3000.datagrams.ClockDatagram | themachinethatgoesping.echosounders.em3000.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders.em3000.datagrams.HeadingDatagram | themachinethatgoesping.echosounders.em3000.datagrams.PositionDatagram | themachinethatgoesping.echosounders.em3000.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders.em3000.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders.em3000.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders.em3000.datagrams.InstallationParameters | themachinethatgoesping.echosounders.em3000.datagrams.RuntimeParameters | themachinethatgoesping.echosounders.em3000.datagrams.ExtraParameters | themachinethatgoesping.echosounders.em3000.datagrams.PUIDOutput | themachinethatgoesping.echosounders.em3000.datagrams.PUStatusOutput | themachinethatgoesping.echosounders.em3000.datagrams.EM3000Unknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_Variant_SkippedData_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_Variant_SkippedData_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_Variant_SkippedData_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_Variant_SkippedData_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_Variant_SkippedData_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_Variant_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_Variant_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_Variant_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_Variant_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_Variant_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.EM3000Datagram | themachinethatgoesping.echosounders.em3000.datagrams.XYZDatagram | themachinethatgoesping.echosounders.em3000.datagrams.ExtraDetections | themachinethatgoesping.echosounders.em3000.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders.em3000.datagrams.SeabedImageData | themachinethatgoesping.echosounders.em3000.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders.em3000.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders.em3000.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders.em3000.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders.em3000.datagrams.ClockDatagram | themachinethatgoesping.echosounders.em3000.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders.em3000.datagrams.HeadingDatagram | themachinethatgoesping.echosounders.em3000.datagrams.PositionDatagram | themachinethatgoesping.echosounders.em3000.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders.em3000.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders.em3000.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders.em3000.datagrams.InstallationParameters | themachinethatgoesping.echosounders.em3000.datagrams.RuntimeParameters | themachinethatgoesping.echosounders.em3000.datagrams.ExtraParameters | themachinethatgoesping.echosounders.em3000.datagrams.PUIDOutput | themachinethatgoesping.echosounders.em3000.datagrams.PUStatusOutput | themachinethatgoesping.echosounders.em3000.datagrams.EM3000Unknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_Variant_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_Variant_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_Variant_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_Variant_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_Variant_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_WatercolumnDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_WatercolumnDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_WatercolumnDatagram:
        ...
    def __copy__(self) -> EM3000DatagramContainer_WatercolumnDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_WatercolumnDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.WatercolumnDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_WatercolumnDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_WatercolumnDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_WatercolumnDatagram]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_WatercolumnDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_WatercolumnDatagram:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_WatercolumnDatagram_SkippedData:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def __copy__(self) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.WatercolumnDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_WatercolumnDatagram_SkippedData]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_WatercolumnDatagram_SkippedData_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.WatercolumnDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_WatercolumnDatagram_SkippedData_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_WatercolumnDatagram_SkippedData_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_WatercolumnDatagram_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_WatercolumnDatagram_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_WatercolumnDatagram_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_WatercolumnDatagram_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_WatercolumnDatagram_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.WatercolumnDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_WatercolumnDatagram_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_WatercolumnDatagram_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_WatercolumnDatagram_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_WatercolumnDatagram_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_WatercolumnDatagram_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_XYZDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_XYZDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_XYZDatagram:
        ...
    def __copy__(self) -> EM3000DatagramContainer_XYZDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_XYZDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.XYZDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_XYZDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_XYZDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_XYZDatagram]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_XYZDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_XYZDatagram:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000DatagramContainer_XYZDatagram_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> EM3000DatagramContainer_XYZDatagram_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]) -> EM3000DatagramContainer_XYZDatagram_mapped:
        ...
    def __copy__(self) -> EM3000DatagramContainer_XYZDatagram_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000DatagramContainer_XYZDatagram_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.datagrams.XYZDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000DatagramContainer_XYZDatagram_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000DatagramContainer_XYZDatagram_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000DatagramContainer_XYZDatagram_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<DatagramContainer>
        """
    def copy(self) -> EM3000DatagramContainer_XYZDatagram_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> EM3000DatagramContainer_XYZDatagram_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000PingContainer:
    """
    """
    @typing.overload
    def __call__(self, channel_id: str) -> EM3000PingContainer:
        ...
    @typing.overload
    def __call__(self, channel_ids: list[str]) -> EM3000PingContainer:
        ...
    def __copy__(self) -> EM3000PingContainer:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingContainer:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.filetypes.EM3000Ping:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000PingContainer:
        ...
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new empty PingContainer object
        """
    @typing.overload
    def __init__(self, arg0: list[themachinethatgoesping.echosounders.em3000.filetypes.EM3000Ping]) -> None:
        """
        Construct a new empty PingContainer object
        """
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000PingContainer:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000PingContainer]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<PingContainer<type_Ping>>
        """
    def copy(self) -> EM3000PingContainer:
        """
        return a copy using the c++ default copy constructor
        """
    def count_pings_per_channel_id(self) -> dict[str, int]:
        ...
    def find_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> list[themachinethatgoesping.echosounders.em3000.filetypes.EM3000Ping]:
        ...
    def get_sorted_by_time(self) -> EM3000PingContainer:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def max_number_of_samples(self) -> int:
        ...
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
class EM3000PingContainer_mapped:
    """
    """
    @typing.overload
    def __call__(self, channel_id: str) -> EM3000PingContainer_mapped:
        ...
    @typing.overload
    def __call__(self, channel_ids: list[str]) -> EM3000PingContainer_mapped:
        ...
    def __copy__(self) -> EM3000PingContainer_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingContainer_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.em3000.filetypes.EM3000Ping_mapped:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> EM3000PingContainer_mapped:
        ...
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new empty PingContainer object
        """
    @typing.overload
    def __init__(self, arg0: list[themachinethatgoesping.echosounders.em3000.filetypes.EM3000Ping_mapped]) -> None:
        """
        Construct a new empty PingContainer object
        """
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> EM3000PingContainer_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[EM3000PingContainer_mapped]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time
        
        Parameter ``max_time_diff_seconds:``:
            maximum time difference between two subsequent datagrams in
            seconds
        
        Returns:
            std::vector<PingContainer<type_Ping>>
        """
    def copy(self) -> EM3000PingContainer_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_pings_per_channel_id(self) -> dict[str, int]:
        ...
    def find_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> list[themachinethatgoesping.echosounders.em3000.filetypes.EM3000Ping_mapped]:
        ...
    def get_sorted_by_time(self) -> EM3000PingContainer_mapped:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def max_number_of_samples(self) -> int:
        ...
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
