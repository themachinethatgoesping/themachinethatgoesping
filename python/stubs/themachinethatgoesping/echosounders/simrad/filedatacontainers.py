"""
Simrad EK60 and EK80 file data container classes
"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad
import themachinethatgoesping.echosounders.simrad.datagrams
import themachinethatgoesping.echosounders.simrad.filetypes
import themachinethatgoesping.tools.pyhelper
import typing
__all__ = ['SimradPingContainer', 'SimradPingContainer_mapped', 'SimradRawDatagramContainer_FIL1', 'SimradRawDatagramContainer_FIL1_mapped', 'SimradRawDatagramContainer_Header', 'SimradRawDatagramContainer_Header_mapped', 'SimradRawDatagramContainer_MRU0', 'SimradRawDatagramContainer_MRU0_mapped', 'SimradRawDatagramContainer_NME0', 'SimradRawDatagramContainer_NME0_mapped', 'SimradRawDatagramContainer_RAW3', 'SimradRawDatagramContainer_RAW3_mapped', 'SimradRawDatagramContainer_RAW3_skipped_data', 'SimradRawDatagramContainer_RAW3_skipped_data_mapped', 'SimradRawDatagramContainer_TAG0', 'SimradRawDatagramContainer_TAG0_mapped', 'SimradRawDatagramContainer_Unknown', 'SimradRawDatagramContainer_Unknown_mapped', 'SimradRawDatagramContainer_Variant', 'SimradRawDatagramContainer_Variant_mapped', 'SimradRawDatagramContainer_Variant_skipped_data', 'SimradRawDatagramContainer_Variant_skipped_data_mapped', 'SimradRawDatagramContainer_XML0', 'SimradRawDatagramContainer_XML0_mapped']
class SimradPingContainer:
    """
    """
    @typing.overload
    def __call__(self, channel_id: str) -> SimradPingContainer:
        ...
    @typing.overload
    def __call__(self, channel_ids: list[str]) -> SimradPingContainer:
        ...
    def __copy__(self) -> SimradPingContainer:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradPingContainer:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.filetypes.SimradPing:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradPingContainer:
        ...
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new empty PingContainer object
        """
    @typing.overload
    def __init__(self, arg0: list[themachinethatgoesping.echosounders.simrad.filetypes.SimradPing]) -> None:
        """
        Construct a new empty PingContainer object
        """
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradPingContainer:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradPingContainer]:
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
    def copy(self) -> SimradPingContainer:
        """
        return a copy using the c++ default copy constructor
        """
    def count_pings_per_channel_id(self) -> dict[str, int]:
        ...
    def find_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> list[themachinethatgoesping.echosounders.simrad.filetypes.SimradPing]:
        ...
    def get_sorted_by_time(self) -> SimradPingContainer:
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
class SimradPingContainer_mapped:
    """
    """
    @typing.overload
    def __call__(self, channel_id: str) -> SimradPingContainer_mapped:
        ...
    @typing.overload
    def __call__(self, channel_ids: list[str]) -> SimradPingContainer_mapped:
        ...
    def __copy__(self) -> SimradPingContainer_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradPingContainer_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.filetypes.SimradPing_mapped:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradPingContainer_mapped:
        ...
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new empty PingContainer object
        """
    @typing.overload
    def __init__(self, arg0: list[themachinethatgoesping.echosounders.simrad.filetypes.SimradPing_mapped]) -> None:
        """
        Construct a new empty PingContainer object
        """
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradPingContainer_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradPingContainer_mapped]:
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
    def copy(self) -> SimradPingContainer_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_pings_per_channel_id(self) -> dict[str, int]:
        ...
    def find_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> list[themachinethatgoesping.echosounders.simrad.filetypes.SimradPing_mapped]:
        ...
    def get_sorted_by_time(self) -> SimradPingContainer_mapped:
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
class SimradRawDatagramContainer_FIL1:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_FIL1:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_FIL1:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_FIL1:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_FIL1:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.FIL1:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_FIL1:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_FIL1:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_FIL1]:
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
    def copy(self) -> SimradRawDatagramContainer_FIL1:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_FIL1:
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
class SimradRawDatagramContainer_FIL1_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_FIL1_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_FIL1_mapped:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_FIL1_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_FIL1_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.FIL1:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_FIL1_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_FIL1_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_FIL1_mapped]:
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
    def copy(self) -> SimradRawDatagramContainer_FIL1_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_FIL1_mapped:
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
class SimradRawDatagramContainer_Header:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Header:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Header:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Header:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Header:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.SimradDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Header:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Header:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Header]:
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
    def copy(self) -> SimradRawDatagramContainer_Header:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Header:
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
class SimradRawDatagramContainer_Header_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Header_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Header_mapped:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Header_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Header_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.SimradDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Header_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Header_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Header_mapped]:
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
    def copy(self) -> SimradRawDatagramContainer_Header_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Header_mapped:
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
class SimradRawDatagramContainer_MRU0:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_MRU0:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_MRU0:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_MRU0:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_MRU0:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.MRU0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_MRU0:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_MRU0:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_MRU0]:
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
    def copy(self) -> SimradRawDatagramContainer_MRU0:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_MRU0:
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
class SimradRawDatagramContainer_MRU0_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_MRU0_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_MRU0_mapped:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_MRU0_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_MRU0_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.MRU0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_MRU0_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_MRU0_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_MRU0_mapped]:
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
    def copy(self) -> SimradRawDatagramContainer_MRU0_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_MRU0_mapped:
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
class SimradRawDatagramContainer_NME0:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_NME0:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_NME0:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_NME0:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_NME0:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.NME0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_NME0:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_NME0:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_NME0]:
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
    def copy(self) -> SimradRawDatagramContainer_NME0:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_NME0:
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
class SimradRawDatagramContainer_NME0_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_NME0_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_NME0_mapped:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_NME0_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_NME0_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.NME0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_NME0_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_NME0_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_NME0_mapped]:
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
    def copy(self) -> SimradRawDatagramContainer_NME0_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_NME0_mapped:
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
class SimradRawDatagramContainer_RAW3:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_RAW3:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_RAW3:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_RAW3:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.RAW3:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_RAW3:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_RAW3]:
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
    def copy(self) -> SimradRawDatagramContainer_RAW3:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3:
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
class SimradRawDatagramContainer_RAW3_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_RAW3_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3_mapped:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_RAW3_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_RAW3_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.RAW3:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_RAW3_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_RAW3_mapped]:
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
    def copy(self) -> SimradRawDatagramContainer_RAW3_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3_mapped:
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
class SimradRawDatagramContainer_RAW3_skipped_data:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_RAW3_skipped_data:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3_skipped_data:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_RAW3_skipped_data:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_RAW3_skipped_data:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.RAW3:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3_skipped_data:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_RAW3_skipped_data:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_RAW3_skipped_data]:
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
    def copy(self) -> SimradRawDatagramContainer_RAW3_skipped_data:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3_skipped_data:
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
class SimradRawDatagramContainer_RAW3_skipped_data_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_RAW3_skipped_data_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3_skipped_data_mapped:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_RAW3_skipped_data_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_RAW3_skipped_data_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.RAW3:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3_skipped_data_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_RAW3_skipped_data_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_RAW3_skipped_data_mapped]:
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
    def copy(self) -> SimradRawDatagramContainer_RAW3_skipped_data_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3_skipped_data_mapped:
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
class SimradRawDatagramContainer_TAG0:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_TAG0:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_TAG0:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_TAG0:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_TAG0:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.TAG0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_TAG0:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_TAG0:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_TAG0]:
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
    def copy(self) -> SimradRawDatagramContainer_TAG0:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_TAG0:
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
class SimradRawDatagramContainer_TAG0_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_TAG0_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_TAG0_mapped:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_TAG0_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_TAG0_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.TAG0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_TAG0_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_TAG0_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_TAG0_mapped]:
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
    def copy(self) -> SimradRawDatagramContainer_TAG0_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_TAG0_mapped:
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
class SimradRawDatagramContainer_Unknown:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Unknown:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Unknown:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Unknown:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Unknown:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.SimradUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Unknown:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Unknown:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Unknown]:
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
    def copy(self) -> SimradRawDatagramContainer_Unknown:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Unknown:
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
class SimradRawDatagramContainer_Unknown_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Unknown_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Unknown_mapped:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Unknown_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Unknown_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.SimradUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Unknown_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Unknown_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Unknown_mapped]:
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
    def copy(self) -> SimradRawDatagramContainer_Unknown_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Unknown_mapped:
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
class SimradRawDatagramContainer_Variant:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Variant:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Variant:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Variant:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Variant:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.SimradDatagram | themachinethatgoesping.echosounders.simrad.datagrams.NME0 | themachinethatgoesping.echosounders.simrad.datagrams.XML0 | themachinethatgoesping.echosounders.simrad.datagrams.MRU0 | themachinethatgoesping.echosounders.simrad.datagrams.RAW3 | themachinethatgoesping.echosounders.simrad.datagrams.FIL1 | themachinethatgoesping.echosounders.simrad.datagrams.TAG0 | themachinethatgoesping.echosounders.simrad.datagrams.SimradUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Variant:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Variant]:
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
    def copy(self) -> SimradRawDatagramContainer_Variant:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant:
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
class SimradRawDatagramContainer_Variant_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Variant_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Variant_mapped:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Variant_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Variant_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.SimradDatagram | themachinethatgoesping.echosounders.simrad.datagrams.NME0 | themachinethatgoesping.echosounders.simrad.datagrams.XML0 | themachinethatgoesping.echosounders.simrad.datagrams.MRU0 | themachinethatgoesping.echosounders.simrad.datagrams.RAW3 | themachinethatgoesping.echosounders.simrad.datagrams.FIL1 | themachinethatgoesping.echosounders.simrad.datagrams.TAG0 | themachinethatgoesping.echosounders.simrad.datagrams.SimradUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Variant_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Variant_mapped]:
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
    def copy(self) -> SimradRawDatagramContainer_Variant_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant_mapped:
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
class SimradRawDatagramContainer_Variant_skipped_data:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Variant_skipped_data:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Variant_skipped_data:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Variant_skipped_data:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Variant_skipped_data:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.SimradDatagram | themachinethatgoesping.echosounders.simrad.datagrams.NME0 | themachinethatgoesping.echosounders.simrad.datagrams.XML0 | themachinethatgoesping.echosounders.simrad.datagrams.MRU0 | themachinethatgoesping.echosounders.simrad.datagrams.RAW3 | themachinethatgoesping.echosounders.simrad.datagrams.FIL1 | themachinethatgoesping.echosounders.simrad.datagrams.TAG0 | themachinethatgoesping.echosounders.simrad.datagrams.SimradUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant_skipped_data:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Variant_skipped_data:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Variant_skipped_data]:
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
    def copy(self) -> SimradRawDatagramContainer_Variant_skipped_data:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant_skipped_data:
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
class SimradRawDatagramContainer_Variant_skipped_data_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Variant_skipped_data_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Variant_skipped_data_mapped:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Variant_skipped_data_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Variant_skipped_data_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.SimradDatagram | themachinethatgoesping.echosounders.simrad.datagrams.NME0 | themachinethatgoesping.echosounders.simrad.datagrams.XML0 | themachinethatgoesping.echosounders.simrad.datagrams.MRU0 | themachinethatgoesping.echosounders.simrad.datagrams.RAW3 | themachinethatgoesping.echosounders.simrad.datagrams.FIL1 | themachinethatgoesping.echosounders.simrad.datagrams.TAG0 | themachinethatgoesping.echosounders.simrad.datagrams.SimradUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant_skipped_data_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Variant_skipped_data_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Variant_skipped_data_mapped]:
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
    def copy(self) -> SimradRawDatagramContainer_Variant_skipped_data_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant_skipped_data_mapped:
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
class SimradRawDatagramContainer_XML0:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_XML0:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_XML0:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_XML0:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_XML0:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.XML0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_XML0:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_XML0:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_XML0]:
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
    def copy(self) -> SimradRawDatagramContainer_XML0:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_XML0:
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
class SimradRawDatagramContainer_XML0_mapped:
    """
    """
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_XML0_mapped:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_XML0_mapped:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_XML0_mapped:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_XML0_mapped:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.datagrams.XML0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_XML0_mapped:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_XML0_mapped:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_XML0_mapped]:
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
    def copy(self) -> SimradRawDatagramContainer_XML0_mapped:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_XML0_mapped:
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
