"""
KongsbergAll (kongsberg .all / .wcd) file data container classes
"""
from __future__ import annotations
import collections.abc
import themachinethatgoesping.echosounders_cppy.kongsbergall
import themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams
import themachinethatgoesping.echosounders_cppy.kongsbergall.filetypes
import themachinethatgoesping.navigation
import themachinethatgoesping.tools_cppy.pyhelper
import typing
__all__: list[str] = ['KongsbergAllDatagramContainer_AttitudeDatagram', 'KongsbergAllDatagramContainer_AttitudeDatagram_stream', 'KongsbergAllDatagramContainer_ClockDatagram', 'KongsbergAllDatagramContainer_ClockDatagram_stream', 'KongsbergAllDatagramContainer_DepthOrHeightDatagram', 'KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream', 'KongsbergAllDatagramContainer_ExtraDetections', 'KongsbergAllDatagramContainer_ExtraDetections_stream', 'KongsbergAllDatagramContainer_ExtraParameters', 'KongsbergAllDatagramContainer_ExtraParameters_stream', 'KongsbergAllDatagramContainer_Header', 'KongsbergAllDatagramContainer_Header_stream', 'KongsbergAllDatagramContainer_HeadingDatagram', 'KongsbergAllDatagramContainer_HeadingDatagram_stream', 'KongsbergAllDatagramContainer_InstallationParameters', 'KongsbergAllDatagramContainer_InstallationParameters_stream', 'KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram', 'KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream', 'KongsbergAllDatagramContainer_PUIDOutput', 'KongsbergAllDatagramContainer_PUIDOutput_stream', 'KongsbergAllDatagramContainer_PUStatusOutput', 'KongsbergAllDatagramContainer_PUStatusOutput_stream', 'KongsbergAllDatagramContainer_PositionDatagram', 'KongsbergAllDatagramContainer_PositionDatagram_stream', 'KongsbergAllDatagramContainer_QualityFactorDatagram', 'KongsbergAllDatagramContainer_QualityFactorDatagram_stream', 'KongsbergAllDatagramContainer_RawRangeAndAngle', 'KongsbergAllDatagramContainer_RawRangeAndAngle_stream', 'KongsbergAllDatagramContainer_RuntimeParameters', 'KongsbergAllDatagramContainer_RuntimeParameters_stream', 'KongsbergAllDatagramContainer_SeabedImageData', 'KongsbergAllDatagramContainer_SeabedImageData_stream', 'KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth', 'KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream', 'KongsbergAllDatagramContainer_SoundSpeedProfileDatagram', 'KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream', 'KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram', 'KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream', 'KongsbergAllDatagramContainer_Unknown', 'KongsbergAllDatagramContainer_Unknown_stream', 'KongsbergAllDatagramContainer_Variant', 'KongsbergAllDatagramContainer_Variant_SkippedData', 'KongsbergAllDatagramContainer_Variant_SkippedData_stream', 'KongsbergAllDatagramContainer_Variant_stream', 'KongsbergAllDatagramContainer_WatercolumnDatagram', 'KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData', 'KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream', 'KongsbergAllDatagramContainer_WatercolumnDatagram_stream', 'KongsbergAllDatagramContainer_XYZDatagram', 'KongsbergAllDatagramContainer_XYZDatagram_stream', 'KongsbergAllPingContainer', 'KongsbergAllPingContainer_stream']
class KongsbergAllDatagramContainer_AttitudeDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.AttitudeDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_AttitudeDatagram]:
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
class KongsbergAllDatagramContainer_AttitudeDatagram_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.AttitudeDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_AttitudeDatagram_stream]:
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
class KongsbergAllDatagramContainer_ClockDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ClockDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_ClockDatagram:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_ClockDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_ClockDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ClockDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_ClockDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_ClockDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_ClockDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ClockDatagram:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_ClockDatagram]:
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
class KongsbergAllDatagramContainer_ClockDatagram_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ClockDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_ClockDatagram_stream]:
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
class KongsbergAllDatagramContainer_DepthOrHeightDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.DepthOrHeightDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_DepthOrHeightDatagram]:
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
class KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.DepthOrHeightDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream]:
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
class KongsbergAllDatagramContainer_ExtraDetections:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ExtraDetections:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_ExtraDetections:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_ExtraDetections:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_ExtraDetections:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ExtraDetections:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_ExtraDetections:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_ExtraDetections:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_ExtraDetections:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ExtraDetections:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_ExtraDetections]:
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
class KongsbergAllDatagramContainer_ExtraDetections_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ExtraDetections:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_ExtraDetections_stream]:
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
class KongsbergAllDatagramContainer_ExtraParameters:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ExtraParameters:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_ExtraParameters:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_ExtraParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_ExtraParameters:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ExtraParameters:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_ExtraParameters:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_ExtraParameters:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_ExtraParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ExtraParameters:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_ExtraParameters]:
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
class KongsbergAllDatagramContainer_ExtraParameters_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ExtraParameters:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_ExtraParameters_stream]:
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
class KongsbergAllDatagramContainer_Header:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Header:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Header:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_Header:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_Header:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.KongsbergAllDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Header:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_Header:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_Header:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Header:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_Header]:
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
class KongsbergAllDatagramContainer_Header_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Header_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Header_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_Header_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_Header_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.KongsbergAllDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Header_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_Header_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_Header_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Header_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_Header_stream]:
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
class KongsbergAllDatagramContainer_HeadingDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_HeadingDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_HeadingDatagram:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_HeadingDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_HeadingDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.HeadingDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_HeadingDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_HeadingDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_HeadingDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_HeadingDatagram:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_HeadingDatagram]:
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
class KongsbergAllDatagramContainer_HeadingDatagram_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.HeadingDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_HeadingDatagram_stream]:
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
class KongsbergAllDatagramContainer_InstallationParameters:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_InstallationParameters:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_InstallationParameters:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_InstallationParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_InstallationParameters:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.InstallationParameters:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_InstallationParameters:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_InstallationParameters:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_InstallationParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_InstallationParameters:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_InstallationParameters]:
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
class KongsbergAllDatagramContainer_InstallationParameters_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.InstallationParameters:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_InstallationParameters_stream]:
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
class KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram]:
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
class KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream]:
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
class KongsbergAllDatagramContainer_PUIDOutput:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PUIDOutput:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_PUIDOutput:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_PUIDOutput:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_PUIDOutput:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PUIDOutput:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_PUIDOutput:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_PUIDOutput:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_PUIDOutput:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PUIDOutput:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_PUIDOutput]:
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
class KongsbergAllDatagramContainer_PUIDOutput_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PUIDOutput:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_PUIDOutput_stream]:
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
class KongsbergAllDatagramContainer_PUStatusOutput:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PUStatusOutput:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_PUStatusOutput:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_PUStatusOutput:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_PUStatusOutput:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PUStatusOutput:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_PUStatusOutput:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_PUStatusOutput:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_PUStatusOutput:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PUStatusOutput:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_PUStatusOutput]:
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
class KongsbergAllDatagramContainer_PUStatusOutput_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PUStatusOutput:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_PUStatusOutput_stream]:
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
class KongsbergAllDatagramContainer_PositionDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PositionDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_PositionDatagram:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_PositionDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_PositionDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PositionDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_PositionDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_PositionDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_PositionDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PositionDatagram:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_PositionDatagram]:
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
class KongsbergAllDatagramContainer_PositionDatagram_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PositionDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_PositionDatagram_stream]:
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
class KongsbergAllDatagramContainer_QualityFactorDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.QualityFactorDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_QualityFactorDatagram]:
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
class KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.QualityFactorDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_QualityFactorDatagram_stream]:
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
class KongsbergAllDatagramContainer_RawRangeAndAngle:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RawRangeAndAngle:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_RawRangeAndAngle]:
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
class KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RawRangeAndAngle:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_RawRangeAndAngle_stream]:
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
class KongsbergAllDatagramContainer_RuntimeParameters:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_RuntimeParameters:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_RuntimeParameters:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_RuntimeParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_RuntimeParameters:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RuntimeParameters:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_RuntimeParameters:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_RuntimeParameters:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_RuntimeParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_RuntimeParameters:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_RuntimeParameters]:
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
class KongsbergAllDatagramContainer_RuntimeParameters_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RuntimeParameters:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_RuntimeParameters_stream]:
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
class KongsbergAllDatagramContainer_SeabedImageData:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SeabedImageData:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SeabedImageData:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_SeabedImageData:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_SeabedImageData:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SeabedImageData:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SeabedImageData:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_SeabedImageData:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_SeabedImageData:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SeabedImageData:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_SeabedImageData]:
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
class KongsbergAllDatagramContainer_SeabedImageData_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SeabedImageData:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_SeabedImageData_stream]:
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
class KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SingleBeamEchoSounderDepth:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth]:
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
class KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SingleBeamEchoSounderDepth:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream]:
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
class KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SoundSpeedProfileDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_SoundSpeedProfileDatagram]:
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
class KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SoundSpeedProfileDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream]:
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
class KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram]:
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
class KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream]:
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
class KongsbergAllDatagramContainer_Unknown:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Unknown:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Unknown:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_Unknown:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_Unknown:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.KongsbergAllUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Unknown:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_Unknown:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_Unknown:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Unknown:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_Unknown]:
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
class KongsbergAllDatagramContainer_Unknown_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Unknown_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Unknown_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_Unknown_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_Unknown_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.KongsbergAllUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Unknown_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_Unknown_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_Unknown_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Unknown_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_Unknown_stream]:
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
class KongsbergAllDatagramContainer_Variant:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Variant:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Variant:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_Variant:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_Variant:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.KongsbergAllDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.XYZDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ExtraDetections | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SeabedImageData | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ClockDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.HeadingDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PositionDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.InstallationParameters | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RuntimeParameters | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ExtraParameters | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PUIDOutput | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PUStatusOutput | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.KongsbergAllUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Variant:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_Variant:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_Variant:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Variant:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_Variant]:
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
class KongsbergAllDatagramContainer_Variant_SkippedData:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.KongsbergAllDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.XYZDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ExtraDetections | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SeabedImageData | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ClockDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.HeadingDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PositionDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.InstallationParameters | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RuntimeParameters | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ExtraParameters | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PUIDOutput | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PUStatusOutput | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.KongsbergAllUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_Variant_SkippedData]:
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
class KongsbergAllDatagramContainer_Variant_SkippedData_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.KongsbergAllDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.XYZDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ExtraDetections | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SeabedImageData | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ClockDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.HeadingDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PositionDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.InstallationParameters | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RuntimeParameters | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ExtraParameters | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PUIDOutput | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PUStatusOutput | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.KongsbergAllUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_Variant_SkippedData_stream]:
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
class KongsbergAllDatagramContainer_Variant_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Variant_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Variant_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_Variant_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_Variant_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.KongsbergAllDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.XYZDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ExtraDetections | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SeabedImageData | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ClockDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.HeadingDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PositionDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.InstallationParameters | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RuntimeParameters | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.ExtraParameters | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PUIDOutput | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.PUStatusOutput | themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.KongsbergAllUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Variant_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_Variant_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_Variant_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Variant_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_Variant_stream]:
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
class KongsbergAllDatagramContainer_WatercolumnDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.WatercolumnDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_WatercolumnDatagram]:
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
class KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.WatercolumnDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData]:
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
class KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.WatercolumnDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream]:
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
class KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.WatercolumnDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_WatercolumnDatagram_stream]:
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
class KongsbergAllDatagramContainer_XYZDatagram:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_XYZDatagram:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_XYZDatagram:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_XYZDatagram:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_XYZDatagram:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.XYZDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_XYZDatagram:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_XYZDatagram:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_XYZDatagram:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_XYZDatagram:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_XYZDatagram]:
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
class KongsbergAllDatagramContainer_XYZDatagram_stream:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        ...
    def __copy__(self) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.XYZDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllDatagramContainer_XYZDatagram_stream]:
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
class KongsbergAllPingContainer:
    """
    """
    @typing.overload
    def __call__(self, channel_id: str) -> KongsbergAllPingContainer:
        ...
    @typing.overload
    def __call__(self, channel_ids: collections.abc.Sequence[str]) -> KongsbergAllPingContainer:
        ...
    def __copy__(self) -> KongsbergAllPingContainer:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingContainer:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.filetypes.KongsbergAllPing:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllPingContainer:
        ...
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new empty PingContainer object
        """
    @typing.overload
    def __init__(self, arg0: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.filetypes.KongsbergAllPing]) -> None:
        """
        Construct a new empty PingContainer object
        """
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllPingContainer:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllPingContainer:
        """
        return a copy using the c++ default copy constructor
        """
    def count_pings_per_channel_id(self) -> dict[str, int]:
        ...
    def find_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.filetypes.KongsbergAllPing]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllPingContainer:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def max_number_of_samples(self) -> int:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_sensor_configuration(self) -> dict[themachinethatgoesping.navigation.SensorConfiguration, KongsbergAllPingContainer]:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllPingContainer]:
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
class KongsbergAllPingContainer_stream:
    """
    """
    @typing.overload
    def __call__(self, channel_id: str) -> KongsbergAllPingContainer_stream:
        ...
    @typing.overload
    def __call__(self, channel_ids: collections.abc.Sequence[str]) -> KongsbergAllPingContainer_stream:
        ...
    def __copy__(self) -> KongsbergAllPingContainer_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> KongsbergAllPingContainer_stream:
        ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsInt) -> themachinethatgoesping.echosounders_cppy.kongsbergall.filetypes.KongsbergAllPing_stream:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> KongsbergAllPingContainer_stream:
        ...
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new empty PingContainer object
        """
    @typing.overload
    def __init__(self, arg0: collections.abc.Sequence[themachinethatgoesping.echosounders_cppy.kongsbergall.filetypes.KongsbergAllPing_stream]) -> None:
        """
        Construct a new empty PingContainer object
        """
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> KongsbergAllPingContainer_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> KongsbergAllPingContainer_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_pings_per_channel_id(self) -> dict[str, int]:
        ...
    def find_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.filetypes.KongsbergAllPing_stream]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllPingContainer_stream:
        ...
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def max_number_of_samples(self) -> int:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_sensor_configuration(self) -> dict[themachinethatgoesping.navigation.SensorConfiguration, KongsbergAllPingContainer_stream]:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: typing.SupportsFloat) -> list[KongsbergAllPingContainer_stream]:
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
