from collections.abc import Sequence
from typing import overload

import themachinethatgoesping.echosounders_nanopy.simradraw
import themachinethatgoesping.echosounders_nanopy.simradraw.datagrams
import themachinethatgoesping.echosounders_nanopy.simradraw.filedatatypes
import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.tools_nanopy.pyhelper


class SimradRawDatagramContainer_Header_stream:
    def copy(self) -> SimradRawDatagramContainer_Header_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_Header_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_Header_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Header_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Header_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Header_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Header_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.SimradRawDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Header_stream: ...

    def __reversed__(self) -> SimradRawDatagramContainer_Header_stream: ...

class SimradRawDatagramContainer_Header:
    def copy(self) -> SimradRawDatagramContainer_Header:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_Header: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_Header: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Header]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Header: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Header: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Header: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.SimradRawDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Header: ...

    def __reversed__(self) -> SimradRawDatagramContainer_Header: ...

class SimradRawDatagramContainer_Unknown_stream:
    def copy(self) -> SimradRawDatagramContainer_Unknown_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_Unknown_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_Unknown_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Unknown_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Unknown_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Unknown_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Unknown_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.SimradRawUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Unknown_stream: ...

    def __reversed__(self) -> SimradRawDatagramContainer_Unknown_stream: ...

class SimradRawDatagramContainer_Unknown:
    def copy(self) -> SimradRawDatagramContainer_Unknown:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_Unknown: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_Unknown: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Unknown]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Unknown: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Unknown: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Unknown: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.SimradRawUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Unknown: ...

    def __reversed__(self) -> SimradRawDatagramContainer_Unknown: ...

class SimradRawDatagramContainer_MRU0_stream:
    def copy(self) -> SimradRawDatagramContainer_MRU0_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_MRU0_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_MRU0_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_MRU0_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_MRU0_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_MRU0_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_MRU0_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.MRU0: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_MRU0_stream: ...

    def __reversed__(self) -> SimradRawDatagramContainer_MRU0_stream: ...

class SimradRawDatagramContainer_MRU0:
    def copy(self) -> SimradRawDatagramContainer_MRU0:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_MRU0: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_MRU0: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_MRU0]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_MRU0: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_MRU0: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_MRU0: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.MRU0: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_MRU0: ...

    def __reversed__(self) -> SimradRawDatagramContainer_MRU0: ...

class SimradRawDatagramContainer_TAG0_stream:
    def copy(self) -> SimradRawDatagramContainer_TAG0_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_TAG0_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_TAG0_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_TAG0_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_TAG0_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_TAG0_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_TAG0_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.TAG0: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_TAG0_stream: ...

    def __reversed__(self) -> SimradRawDatagramContainer_TAG0_stream: ...

class SimradRawDatagramContainer_TAG0:
    def copy(self) -> SimradRawDatagramContainer_TAG0:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_TAG0: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_TAG0: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_TAG0]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_TAG0: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_TAG0: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_TAG0: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.TAG0: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_TAG0: ...

    def __reversed__(self) -> SimradRawDatagramContainer_TAG0: ...

class SimradRawDatagramContainer_FIL1_stream:
    def copy(self) -> SimradRawDatagramContainer_FIL1_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_FIL1_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_FIL1_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_FIL1_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_FIL1_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_FIL1_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_FIL1_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.FIL1: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_FIL1_stream: ...

    def __reversed__(self) -> SimradRawDatagramContainer_FIL1_stream: ...

class SimradRawDatagramContainer_FIL1:
    def copy(self) -> SimradRawDatagramContainer_FIL1:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_FIL1: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_FIL1: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_FIL1]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_FIL1: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_FIL1: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_FIL1: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.FIL1: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_FIL1: ...

    def __reversed__(self) -> SimradRawDatagramContainer_FIL1: ...

class SimradRawDatagramContainer_RAW3_stream:
    def copy(self) -> SimradRawDatagramContainer_RAW3_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_RAW3_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_RAW3_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_RAW3_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_RAW3_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.RAW3: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3_stream: ...

    def __reversed__(self) -> SimradRawDatagramContainer_RAW3_stream: ...

class SimradRawDatagramContainer_RAW3:
    def copy(self) -> SimradRawDatagramContainer_RAW3:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_RAW3: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_RAW3: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_RAW3]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_RAW3: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.RAW3: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3: ...

    def __reversed__(self) -> SimradRawDatagramContainer_RAW3: ...

class SimradRawDatagramContainer_RAW3_skipped_data_stream:
    def copy(self) -> SimradRawDatagramContainer_RAW3_skipped_data_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_RAW3_skipped_data_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_RAW3_skipped_data_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_RAW3_skipped_data_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3_skipped_data_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_RAW3_skipped_data_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3_skipped_data_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.RAW3: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3_skipped_data_stream: ...

    def __reversed__(self) -> SimradRawDatagramContainer_RAW3_skipped_data_stream: ...

class SimradRawDatagramContainer_RAW3_skipped_data:
    def copy(self) -> SimradRawDatagramContainer_RAW3_skipped_data:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_RAW3_skipped_data: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_RAW3_skipped_data: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_RAW3_skipped_data]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3_skipped_data: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_RAW3_skipped_data: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3_skipped_data: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.RAW3: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3_skipped_data: ...

    def __reversed__(self) -> SimradRawDatagramContainer_RAW3_skipped_data: ...

class SimradRawDatagramContainer_XML0_stream:
    def copy(self) -> SimradRawDatagramContainer_XML0_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_XML0_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_XML0_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_XML0_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_XML0_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_XML0_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_XML0_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_XML0_stream: ...

    def __reversed__(self) -> SimradRawDatagramContainer_XML0_stream: ...

class SimradRawDatagramContainer_XML0:
    def copy(self) -> SimradRawDatagramContainer_XML0:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_XML0: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_XML0: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_XML0]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_XML0: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_XML0: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_XML0: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_XML0: ...

    def __reversed__(self) -> SimradRawDatagramContainer_XML0: ...

class SimradRawDatagramContainer_NME0_stream:
    def copy(self) -> SimradRawDatagramContainer_NME0_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_NME0_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_NME0_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_NME0_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_NME0_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_NME0_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_NME0_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.NME0: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_NME0_stream: ...

    def __reversed__(self) -> SimradRawDatagramContainer_NME0_stream: ...

class SimradRawDatagramContainer_NME0:
    def copy(self) -> SimradRawDatagramContainer_NME0:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_NME0: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_NME0: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_NME0]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_NME0: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_NME0: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_NME0: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.NME0: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_NME0: ...

    def __reversed__(self) -> SimradRawDatagramContainer_NME0: ...

class SimradRawDatagramContainer_Variant_stream:
    def copy(self) -> SimradRawDatagramContainer_Variant_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_Variant_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_Variant_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Variant_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Variant_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Variant_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.SimradRawDatagram | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.NME0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.MRU0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.RAW3 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.FIL1 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.TAG0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.SimradRawUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant_stream: ...

    def __reversed__(self) -> SimradRawDatagramContainer_Variant_stream: ...

class SimradRawDatagramContainer_Variant:
    def copy(self) -> SimradRawDatagramContainer_Variant:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_Variant: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_Variant: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Variant]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Variant: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Variant: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.SimradRawDatagram | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.NME0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.MRU0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.RAW3 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.FIL1 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.TAG0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.SimradRawUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant: ...

    def __reversed__(self) -> SimradRawDatagramContainer_Variant: ...

class SimradRawDatagramContainer_Variant_skipped_data_stream:
    def copy(self) -> SimradRawDatagramContainer_Variant_skipped_data_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_Variant_skipped_data_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_Variant_skipped_data_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Variant_skipped_data_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant_skipped_data_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Variant_skipped_data_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Variant_skipped_data_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.SimradRawDatagram | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.NME0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.MRU0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.RAW3 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.FIL1 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.TAG0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.SimradRawUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant_skipped_data_stream: ...

    def __reversed__(self) -> SimradRawDatagramContainer_Variant_skipped_data_stream: ...

class SimradRawDatagramContainer_Variant_skipped_data:
    def copy(self) -> SimradRawDatagramContainer_Variant_skipped_data:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawDatagramContainer_Variant_skipped_data: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawDatagramContainer_Variant_skipped_data: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawDatagramContainer_Variant_skipped_data]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant_skipped_data: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> SimradRawDatagramContainer_Variant_skipped_data: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]) -> SimradRawDatagramContainer_Variant_skipped_data: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.SimradRawDatagram | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.NME0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.MRU0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.RAW3 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.FIL1 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.TAG0 | themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.SimradRawUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant_skipped_data: ...

    def __reversed__(self) -> SimradRawDatagramContainer_Variant_skipped_data: ...

class SimradRawPingContainer_stream:
    @overload
    def __init__(self) -> None:
        """Construct a new empty PingContainer object"""

    @overload
    def __init__(self, arg: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.filedatatypes.SimradRawPing_stream], /) -> None: ...

    def copy(self) -> SimradRawPingContainer_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawPingContainer_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawPingContainer_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def max_number_of_samples(self) -> int: ...

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawPingContainer_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_PingContainer<type_Ping>
        """

    def split_by_sensor_configuration(self) -> dict[themachinethatgoesping.navigation_nanopy.SensorConfiguration, SimradRawPingContainer_stream]: ...

    def get_sorted_by_time(self) -> SimradRawPingContainer_stream: ...

    def count_pings_per_channel_id(self) -> dict[str, int]: ...

    def find_channel_ids(self) -> list[str]: ...

    @overload
    def __call__(self, channel_id: str) -> SimradRawPingContainer_stream: ...

    @overload
    def __call__(self, channel_ids: Sequence[str]) -> SimradRawPingContainer_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    def get_pings(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.filedatatypes.SimradRawPing_stream]: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatatypes.SimradRawPing_stream: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawPingContainer_stream: ...

    def __reversed__(self) -> SimradRawPingContainer_stream: ...

class SimradRawPingContainer:
    @overload
    def __init__(self) -> None:
        """Construct a new empty PingContainer object"""

    @overload
    def __init__(self, arg: Sequence[themachinethatgoesping.echosounders_nanopy.simradraw.filedatatypes.SimradRawPing], /) -> None: ...

    def copy(self) -> SimradRawPingContainer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawPingContainer: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawPingContainer: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def max_number_of_samples(self) -> int: ...

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[SimradRawPingContainer]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_PingContainer<type_Ping>
        """

    def split_by_sensor_configuration(self) -> dict[themachinethatgoesping.navigation_nanopy.SensorConfiguration, SimradRawPingContainer]: ...

    def get_sorted_by_time(self) -> SimradRawPingContainer: ...

    def count_pings_per_channel_id(self) -> dict[str, int]: ...

    def find_channel_ids(self) -> list[str]: ...

    @overload
    def __call__(self, channel_id: str) -> SimradRawPingContainer: ...

    @overload
    def __call__(self, channel_ids: Sequence[str]) -> SimradRawPingContainer: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    def get_pings(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.filedatatypes.SimradRawPing]: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatatypes.SimradRawPing: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> SimradRawPingContainer: ...

    def __reversed__(self) -> SimradRawPingContainer: ...
