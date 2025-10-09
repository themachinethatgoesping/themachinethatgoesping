"""
KongsbergAll (kongsberg .all / .wcd) file data container classes
"""
from __future__ import annotations
import themachinethatgoesping.echosounders_nanopy.kongsbergall
import themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams
import themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes
import typing
__all__: list[str] = ['KongsbergAllDatagramContainer_AttitudeDatagram', 'KongsbergAllDatagramContainer_AttitudeDatagram_stream', 'KongsbergAllDatagramContainer_ClockDatagram', 'KongsbergAllDatagramContainer_ClockDatagram_stream', 'KongsbergAllDatagramContainer_DepthOrHeightDatagram', 'KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream', 'KongsbergAllDatagramContainer_ExtraDetections', 'KongsbergAllDatagramContainer_ExtraDetections_stream', 'KongsbergAllDatagramContainer_ExtraParameters', 'KongsbergAllDatagramContainer_ExtraParameters_stream', 'KongsbergAllDatagramContainer_Header', 'KongsbergAllDatagramContainer_Header_stream', 'KongsbergAllDatagramContainer_HeadingDatagram', 'KongsbergAllDatagramContainer_HeadingDatagram_stream', 'KongsbergAllDatagramContainer_InstallationParameters', 'KongsbergAllDatagramContainer_InstallationParameters_stream', 'KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram', 'KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream', 'KongsbergAllDatagramContainer_PUIDOutput', 'KongsbergAllDatagramContainer_PUIDOutput_stream', 'KongsbergAllDatagramContainer_PUStatusOutput', 'KongsbergAllDatagramContainer_PUStatusOutput_stream', 'KongsbergAllDatagramContainer_PositionDatagram', 'KongsbergAllDatagramContainer_PositionDatagram_stream', 'KongsbergAllDatagramContainer_QualityFactorDatagram', 'KongsbergAllDatagramContainer_QualityFactorDatagram_stream', 'KongsbergAllDatagramContainer_RawRangeAndAngle', 'KongsbergAllDatagramContainer_RawRangeAndAngle_stream', 'KongsbergAllDatagramContainer_RuntimeParameters', 'KongsbergAllDatagramContainer_RuntimeParameters_stream', 'KongsbergAllDatagramContainer_SeabedImageData', 'KongsbergAllDatagramContainer_SeabedImageData_stream', 'KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth', 'KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream', 'KongsbergAllDatagramContainer_SoundSpeedProfileDatagram', 'KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream', 'KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram', 'KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream', 'KongsbergAllDatagramContainer_Unknown', 'KongsbergAllDatagramContainer_Unknown_stream', 'KongsbergAllDatagramContainer_Variant', 'KongsbergAllDatagramContainer_Variant_SkippedData', 'KongsbergAllDatagramContainer_Variant_SkippedData_stream', 'KongsbergAllDatagramContainer_Variant_stream', 'KongsbergAllDatagramContainer_WatercolumnDatagram', 'KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData', 'KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream', 'KongsbergAllDatagramContainer_WatercolumnDatagram_stream', 'KongsbergAllDatagramContainer_XYZDatagram', 'KongsbergAllDatagramContainer_XYZDatagram_stream', 'KongsbergAllPingContainer', 'KongsbergAllPingContainer_stream']
class KongsbergAllDatagramContainer_AttitudeDatagram:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_AttitudeDatagram
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.AttitudeDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_AttitudeDatagram
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_AttitudeDatagram]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_AttitudeDatagram_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.AttitudeDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_AttitudeDatagram_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_AttitudeDatagram_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ClockDatagram:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_ClockDatagram
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_ClockDatagram:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_ClockDatagram:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ClockDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_ClockDatagram
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ClockDatagram:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_ClockDatagram]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_ClockDatagram_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ClockDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_ClockDatagram_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_ClockDatagram_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_DepthOrHeightDatagram
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.DepthOrHeightDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_DepthOrHeightDatagram
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_DepthOrHeightDatagram]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.DepthOrHeightDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ExtraDetections:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_ExtraDetections
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_ExtraDetections:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_ExtraDetections:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraDetections:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_ExtraDetections
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ExtraDetections:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_ExtraDetections]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_ExtraDetections_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraDetections:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_ExtraDetections_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_ExtraDetections_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ExtraParameters:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_ExtraParameters
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_ExtraParameters:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_ExtraParameters:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_ExtraParameters
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ExtraParameters:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_ExtraParameters]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_ExtraParameters_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_ExtraParameters_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_ExtraParameters_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Header:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Header
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_Header:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_Header:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Header
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Header:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Header]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Header_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Header_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_Header_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_Header_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Header_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Header_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Header_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_HeadingDatagram:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_HeadingDatagram
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_HeadingDatagram:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_HeadingDatagram:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.HeadingDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_HeadingDatagram
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_HeadingDatagram:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_HeadingDatagram]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_HeadingDatagram_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.HeadingDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_HeadingDatagram_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_HeadingDatagram_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_InstallationParameters:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_InstallationParameters
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_InstallationParameters:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_InstallationParameters:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_InstallationParameters
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_InstallationParameters:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_InstallationParameters]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_InstallationParameters_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_InstallationParameters_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_InstallationParameters_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PUIDOutput:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_PUIDOutput
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_PUIDOutput:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_PUIDOutput:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUIDOutput:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_PUIDOutput
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PUIDOutput:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_PUIDOutput]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_PUIDOutput_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUIDOutput:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_PUIDOutput_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_PUIDOutput_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PUStatusOutput:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_PUStatusOutput
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_PUStatusOutput:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_PUStatusOutput:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUStatusOutput:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_PUStatusOutput
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PUStatusOutput:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_PUStatusOutput]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_PUStatusOutput_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUStatusOutput:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_PUStatusOutput_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_PUStatusOutput_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PositionDatagram:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_PositionDatagram
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_PositionDatagram:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_PositionDatagram:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PositionDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_PositionDatagram
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PositionDatagram:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_PositionDatagram]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_PositionDatagram_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PositionDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_PositionDatagram_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_PositionDatagram_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_QualityFactorDatagram
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.QualityFactorDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_QualityFactorDatagram
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_QualityFactorDatagram]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_QualityFactorDatagram_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.QualityFactorDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_QualityFactorDatagram_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_QualityFactorDatagram_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_RawRangeAndAngle
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RawRangeAndAngle:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_RawRangeAndAngle
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_RawRangeAndAngle]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_RawRangeAndAngle_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RawRangeAndAngle:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_RawRangeAndAngle_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_RawRangeAndAngle_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_RuntimeParameters:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_RuntimeParameters
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_RuntimeParameters:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_RuntimeParameters:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_RuntimeParameters
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_RuntimeParameters:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_RuntimeParameters]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_RuntimeParameters_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_RuntimeParameters_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_RuntimeParameters_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SeabedImageData:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SeabedImageData
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_SeabedImageData:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_SeabedImageData:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SeabedImageData:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SeabedImageData
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SeabedImageData:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SeabedImageData]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SeabedImageData_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SeabedImageData:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SeabedImageData_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SeabedImageData_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SingleBeamEchoSounderDepth:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SingleBeamEchoSounderDepth:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SoundSpeedProfileDatagram
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SoundSpeedProfileDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SoundSpeedProfileDatagram
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SoundSpeedProfileDatagram]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SoundSpeedProfileDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Unknown:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Unknown
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_Unknown:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_Unknown:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllUnknown:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Unknown
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Unknown:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Unknown]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Unknown_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Unknown_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_Unknown_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_Unknown_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllUnknown:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Unknown_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Unknown_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Unknown_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Variant:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Variant
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_Variant:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_Variant:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.XYZDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraDetections | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SeabedImageData | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ClockDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.HeadingDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PositionDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUIDOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUStatusOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllUnknown:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Variant
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Variant:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Variant]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Variant_SkippedData
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.XYZDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraDetections | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SeabedImageData | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ClockDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.HeadingDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PositionDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUIDOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUStatusOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllUnknown:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Variant_SkippedData
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Variant_SkippedData]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Variant_SkippedData_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.XYZDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraDetections | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SeabedImageData | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ClockDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.HeadingDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PositionDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUIDOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUStatusOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllUnknown:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Variant_SkippedData_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Variant_SkippedData_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Variant_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Variant_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_Variant_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_Variant_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.XYZDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraDetections | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SeabedImageData | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ClockDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.HeadingDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PositionDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUIDOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUStatusOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllUnknown:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_Variant_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Variant_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Variant_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_WatercolumnDatagram
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_WatercolumnDatagram
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_WatercolumnDatagram]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_WatercolumnDatagram_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_WatercolumnDatagram_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_WatercolumnDatagram_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_XYZDatagram:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_XYZDatagram
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_XYZDatagram:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_XYZDatagram:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.XYZDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_XYZDatagram
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_XYZDatagram:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_XYZDatagram]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        """
        __call__(self, datagram_identifiers: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_XYZDatagram_stream
        """
    def __copy__(self) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.XYZDatagram:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllDatagramContainer_XYZDatagram_stream
        """
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
    def count_datagrams_per_type(self) -> ...:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_XYZDatagram_stream]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, channel_id: str) -> KongsbergAllPingContainer:
        """
        __call__(self, channel_ids: collections.abc.Sequence[str]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer
        """
    def __copy__(self) -> KongsbergAllPingContainer:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllPingContainer:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes.KongsbergAllPing:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer
        """
    def __init__(self) -> None:
        """
        __init__(self, arg: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes.KongsbergAllPing], /) -> None
        
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
    def count_pings_per_channel_id(self) -> ...:
        ...
    def find_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes.KongsbergAllPing]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllPingContainer:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def max_number_of_samples(self) -> int:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_sensor_configuration(self) -> ...:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllPingContainer]:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, channel_id: str) -> KongsbergAllPingContainer_stream:
        """
        __call__(self, channel_ids: collections.abc.Sequence[str]) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer_stream
        """
    def __copy__(self) -> KongsbergAllPingContainer_stream:
        ...
    def __deepcopy__(self, arg: dict) -> KongsbergAllPingContainer_stream:
        ...
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes.KongsbergAllPing_stream:
        """
        __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer_stream
        """
    def __init__(self) -> None:
        """
        __init__(self, arg: collections.abc.Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes.KongsbergAllPing_stream], /) -> None
        
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
    def count_pings_per_channel_id(self) -> ...:
        ...
    def find_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes.KongsbergAllPing_stream]:
        ...
    def get_sorted_by_time(self) -> KongsbergAllPingContainer_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def max_number_of_samples(self) -> int:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_sensor_configuration(self) -> ...:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllPingContainer_stream]:
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
