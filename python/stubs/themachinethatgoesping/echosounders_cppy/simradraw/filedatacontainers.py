"""
SimradRaw EK60 and EK80 file data container classes
"""
from __future__ import annotations
import themachinethatgoesping.echosounders_cppy.simradraw
import themachinethatgoesping.echosounders_cppy.simradraw.datagrams
import themachinethatgoesping.echosounders_cppy.simradraw.filetypes
import themachinethatgoesping.navigation
import themachinethatgoesping.tools_cppy.pyhelper
import typing
__all__ = ['SimradRawDatagramContainer_FIL1', 'SimradRawDatagramContainer_FIL1_stream', 'SimradRawDatagramContainer_Header', 'SimradRawDatagramContainer_Header_stream', 'SimradRawDatagramContainer_MRU0', 'SimradRawDatagramContainer_MRU0_stream', 'SimradRawDatagramContainer_NME0', 'SimradRawDatagramContainer_NME0_stream', 'SimradRawDatagramContainer_RAW3', 'SimradRawDatagramContainer_RAW3_skipped_data', 'SimradRawDatagramContainer_RAW3_skipped_data_stream', 'SimradRawDatagramContainer_RAW3_stream', 'SimradRawDatagramContainer_TAG0', 'SimradRawDatagramContainer_TAG0_stream', 'SimradRawDatagramContainer_Unknown', 'SimradRawDatagramContainer_Unknown_stream', 'SimradRawDatagramContainer_Variant', 'SimradRawDatagramContainer_Variant_skipped_data', 'SimradRawDatagramContainer_Variant_skipped_data_stream', 'SimradRawDatagramContainer_Variant_stream', 'SimradRawDatagramContainer_XML0', 'SimradRawDatagramContainer_XML0_stream', 'SimradRawPingContainer', 'SimradRawPingContainer_stream']
class SimradRawDatagramContainer_FIL1:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_FIL1:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_FIL1:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_FIL1:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_FIL1:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.FIL1:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_FIL1:
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
    def copy(self) -> SimradRawDatagramContainer_FIL1:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_FIL1:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_FIL1]:
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
class SimradRawDatagramContainer_FIL1_stream:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_FIL1_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_FIL1_stream:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_FIL1_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_FIL1_stream:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.FIL1:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_FIL1_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_FIL1_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawDatagramContainer_FIL1_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_FIL1_stream:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_FIL1_stream]:
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
class SimradRawDatagramContainer_Header:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Header:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Header:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Header:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Header:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.SimradRawDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Header:
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
    def copy(self) -> SimradRawDatagramContainer_Header:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Header:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Header]:
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
class SimradRawDatagramContainer_Header_stream:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Header_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Header_stream:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Header_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Header_stream:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.SimradRawDatagram:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Header_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Header_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawDatagramContainer_Header_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Header_stream:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Header_stream]:
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
class SimradRawDatagramContainer_MRU0:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_MRU0:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_MRU0:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_MRU0:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_MRU0:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.MRU0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_MRU0:
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
    def copy(self) -> SimradRawDatagramContainer_MRU0:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_MRU0:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_MRU0]:
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
class SimradRawDatagramContainer_MRU0_stream:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_MRU0_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_MRU0_stream:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_MRU0_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_MRU0_stream:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.MRU0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_MRU0_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_MRU0_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawDatagramContainer_MRU0_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_MRU0_stream:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_MRU0_stream]:
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
class SimradRawDatagramContainer_NME0:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_NME0:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_NME0:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_NME0:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_NME0:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.NME0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_NME0:
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
    def copy(self) -> SimradRawDatagramContainer_NME0:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_NME0:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_NME0]:
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
class SimradRawDatagramContainer_NME0_stream:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_NME0_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_NME0_stream:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_NME0_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_NME0_stream:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.NME0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_NME0_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_NME0_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawDatagramContainer_NME0_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_NME0_stream:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_NME0_stream]:
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
class SimradRawDatagramContainer_RAW3:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_RAW3:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_RAW3:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_RAW3:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3:
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
    def copy(self) -> SimradRawDatagramContainer_RAW3:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_RAW3]:
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
class SimradRawDatagramContainer_RAW3_skipped_data:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_RAW3_skipped_data:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3_skipped_data:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_RAW3_skipped_data:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_RAW3_skipped_data:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3_skipped_data:
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
    def copy(self) -> SimradRawDatagramContainer_RAW3_skipped_data:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3_skipped_data:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_RAW3_skipped_data]:
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
class SimradRawDatagramContainer_RAW3_skipped_data_stream:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_RAW3_skipped_data_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3_skipped_data_stream:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_RAW3_skipped_data_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_RAW3_skipped_data_stream:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3_skipped_data_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_RAW3_skipped_data_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawDatagramContainer_RAW3_skipped_data_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3_skipped_data_stream:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_RAW3_skipped_data_stream]:
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
class SimradRawDatagramContainer_RAW3_stream:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_RAW3_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3_stream:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_RAW3_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_RAW3_stream:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_RAW3_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawDatagramContainer_RAW3_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3_stream:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_RAW3_stream]:
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
class SimradRawDatagramContainer_TAG0:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_TAG0:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_TAG0:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_TAG0:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_TAG0:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.TAG0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_TAG0:
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
    def copy(self) -> SimradRawDatagramContainer_TAG0:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_TAG0:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_TAG0]:
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
class SimradRawDatagramContainer_TAG0_stream:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_TAG0_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_TAG0_stream:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_TAG0_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_TAG0_stream:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.TAG0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_TAG0_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_TAG0_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawDatagramContainer_TAG0_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_TAG0_stream:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_TAG0_stream]:
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
class SimradRawDatagramContainer_Unknown:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Unknown:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Unknown:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Unknown:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Unknown:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.SimradRawUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Unknown:
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
    def copy(self) -> SimradRawDatagramContainer_Unknown:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Unknown:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Unknown]:
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
class SimradRawDatagramContainer_Unknown_stream:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Unknown_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Unknown_stream:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Unknown_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Unknown_stream:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.SimradRawUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Unknown_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Unknown_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawDatagramContainer_Unknown_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Unknown_stream:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Unknown_stream]:
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
class SimradRawDatagramContainer_Variant:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Variant:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Variant:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Variant:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Variant:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.SimradRawDatagram | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.NME0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.MRU0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.FIL1 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.TAG0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.SimradRawUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant:
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
    def copy(self) -> SimradRawDatagramContainer_Variant:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Variant]:
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
class SimradRawDatagramContainer_Variant_skipped_data:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Variant_skipped_data:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Variant_skipped_data:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Variant_skipped_data:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Variant_skipped_data:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.SimradRawDatagram | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.NME0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.MRU0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.FIL1 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.TAG0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.SimradRawUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant_skipped_data:
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
    def copy(self) -> SimradRawDatagramContainer_Variant_skipped_data:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant_skipped_data:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Variant_skipped_data]:
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
class SimradRawDatagramContainer_Variant_skipped_data_stream:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Variant_skipped_data_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Variant_skipped_data_stream:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Variant_skipped_data_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Variant_skipped_data_stream:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.SimradRawDatagram | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.NME0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.MRU0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.FIL1 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.TAG0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.SimradRawUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant_skipped_data_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Variant_skipped_data_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawDatagramContainer_Variant_skipped_data_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant_skipped_data_stream:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Variant_skipped_data_stream]:
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
class SimradRawDatagramContainer_Variant_stream:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Variant_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Variant_stream:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_Variant_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Variant_stream:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.SimradRawDatagram | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.NME0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.MRU0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.FIL1 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.TAG0 | themachinethatgoesping.echosounders_cppy.simradraw.datagrams.SimradRawUnknown:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Variant_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawDatagramContainer_Variant_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant_stream:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Variant_stream]:
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
class SimradRawDatagramContainer_XML0:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_XML0:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_XML0:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_XML0:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_XML0:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_XML0:
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
    def copy(self) -> SimradRawDatagramContainer_XML0:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_XML0:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_XML0]:
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
class SimradRawDatagramContainer_XML0_stream:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_XML0_stream:
        ...
    @typing.overload
    def __call__(self, datagram_identifiers: list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_XML0_stream:
        ...
    def __copy__(self) -> SimradRawDatagramContainer_XML0_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_XML0_stream:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_XML0_stream:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_XML0_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawDatagramContainer_XML0_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, int]:
        ...
    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_XML0_stream:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_XML0_stream]:
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
class SimradRawPingContainer:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, channel_id: str) -> SimradRawPingContainer:
        ...
    @typing.overload
    def __call__(self, channel_ids: list[str]) -> SimradRawPingContainer:
        ...
    def __copy__(self) -> SimradRawPingContainer:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingContainer:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.filetypes.SimradRawPing:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawPingContainer:
        ...
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new empty PingContainer object
        """
    @typing.overload
    def __init__(self, arg0: list[themachinethatgoesping.echosounders_cppy.simradraw.filetypes.SimradRawPing]) -> None:
        """
        Construct a new empty PingContainer object
        """
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawPingContainer:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawPingContainer:
        """
        return a copy using the c++ default copy constructor
        """
    def count_pings_per_channel_id(self) -> dict[str, int]:
        ...
    def find_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.filetypes.SimradRawPing]:
        ...
    def get_sorted_by_time(self) -> SimradRawPingContainer:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def max_number_of_samples(self) -> int:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_sensor_configuration(self) -> dict[themachinethatgoesping.navigation.SensorConfiguration, SimradRawPingContainer]:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawPingContainer]:
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
class SimradRawPingContainer_stream:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __call__(self, channel_id: str) -> SimradRawPingContainer_stream:
        ...
    @typing.overload
    def __call__(self, channel_ids: list[str]) -> SimradRawPingContainer_stream:
        ...
    def __copy__(self) -> SimradRawPingContainer_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingContainer_stream:
        ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_cppy.simradraw.filetypes.SimradRawPing_stream:
        ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools_cppy.pyhelper.PyIndexerSlice) -> SimradRawPingContainer_stream:
        ...
    @typing.overload
    def __init__(self) -> None:
        """
        Construct a new empty PingContainer object
        """
    @typing.overload
    def __init__(self, arg0: list[themachinethatgoesping.echosounders_cppy.simradraw.filetypes.SimradRawPing_stream]) -> None:
        """
        Construct a new empty PingContainer object
        """
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawPingContainer_stream:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawPingContainer_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def count_pings_per_channel_id(self) -> dict[str, int]:
        ...
    def find_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.filetypes.SimradRawPing_stream]:
        ...
    def get_sorted_by_time(self) -> SimradRawPingContainer_stream:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def max_number_of_samples(self) -> int:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def size(self) -> int:
        ...
    def split_by_sensor_configuration(self) -> dict[themachinethatgoesping.navigation.SensorConfiguration, SimradRawPingContainer_stream]:
        ...
    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawPingContainer_stream]:
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
