"""Teledyne RESON .s7k (7k) file data container classes"""

from collections.abc import Sequence
from typing import overload

import themachinethatgoesping.echosounders_nanopy.s7k
import themachinethatgoesping.echosounders_nanopy.s7k.datagrams
import themachinethatgoesping.tools_nanopy.pyhelper


class S7KDatagramContainer_Header_stream:
    def copy(self) -> S7KDatagramContainer_Header_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Header_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Header_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Header_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Header_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Header_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Header_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.S7KDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Header_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Header_stream: ...

class S7KDatagramContainer_Header:
    def copy(self) -> S7KDatagramContainer_Header:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Header: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Header: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Header]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Header: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Header: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Header: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.S7KDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Header: ...

    def __reversed__(self) -> S7KDatagramContainer_Header: ...

class S7KDatagramContainer_Unknown_stream:
    def copy(self) -> S7KDatagramContainer_Unknown_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Unknown_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Unknown_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Unknown_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Unknown_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Unknown_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Unknown_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.S7KUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Unknown_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Unknown_stream: ...

class S7KDatagramContainer_Unknown:
    def copy(self) -> S7KDatagramContainer_Unknown:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Unknown: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Unknown: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Unknown]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Unknown: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Unknown: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Unknown: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.S7KUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Unknown: ...

    def __reversed__(self) -> S7KDatagramContainer_Unknown: ...

class S7KDatagramContainer_ReferencePoint_stream:
    def copy(self) -> S7KDatagramContainer_ReferencePoint_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_ReferencePoint_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_ReferencePoint_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_ReferencePoint_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_ReferencePoint_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_ReferencePoint_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_ReferencePoint_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.ReferencePoint: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_ReferencePoint_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_ReferencePoint_stream: ...

class S7KDatagramContainer_ReferencePoint:
    def copy(self) -> S7KDatagramContainer_ReferencePoint:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_ReferencePoint: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_ReferencePoint: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_ReferencePoint]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_ReferencePoint: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_ReferencePoint: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_ReferencePoint: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.ReferencePoint: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_ReferencePoint: ...

    def __reversed__(self) -> S7KDatagramContainer_ReferencePoint: ...

class S7KDatagramContainer_Position_stream:
    def copy(self) -> S7KDatagramContainer_Position_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Position_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Position_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Position_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Position_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Position_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Position_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Position: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Position_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Position_stream: ...

class S7KDatagramContainer_Position:
    def copy(self) -> S7KDatagramContainer_Position:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Position: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Position: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Position]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Position: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Position: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Position: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Position: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Position: ...

    def __reversed__(self) -> S7KDatagramContainer_Position: ...

class S7KDatagramContainer_RollPitchHeave_stream:
    def copy(self) -> S7KDatagramContainer_RollPitchHeave_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_RollPitchHeave_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_RollPitchHeave_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_RollPitchHeave_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_RollPitchHeave_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_RollPitchHeave_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_RollPitchHeave_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.RollPitchHeave: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_RollPitchHeave_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_RollPitchHeave_stream: ...

class S7KDatagramContainer_RollPitchHeave:
    def copy(self) -> S7KDatagramContainer_RollPitchHeave:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_RollPitchHeave: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_RollPitchHeave: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_RollPitchHeave]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_RollPitchHeave: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_RollPitchHeave: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_RollPitchHeave: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.RollPitchHeave: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_RollPitchHeave: ...

    def __reversed__(self) -> S7KDatagramContainer_RollPitchHeave: ...

class S7KDatagramContainer_Heading_stream:
    def copy(self) -> S7KDatagramContainer_Heading_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Heading_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Heading_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Heading_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Heading_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Heading_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Heading_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Heading: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Heading_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Heading_stream: ...

class S7KDatagramContainer_Heading:
    def copy(self) -> S7KDatagramContainer_Heading:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Heading: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Heading: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Heading]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Heading: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Heading: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Heading: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Heading: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Heading: ...

    def __reversed__(self) -> S7KDatagramContainer_Heading: ...

class S7KDatagramContainer_Navigation_stream:
    def copy(self) -> S7KDatagramContainer_Navigation_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Navigation_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Navigation_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Navigation_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Navigation_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Navigation_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Navigation_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Navigation: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Navigation_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Navigation_stream: ...

class S7KDatagramContainer_Navigation:
    def copy(self) -> S7KDatagramContainer_Navigation:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Navigation: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Navigation: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Navigation]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Navigation: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Navigation: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Navigation: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Navigation: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Navigation: ...

    def __reversed__(self) -> S7KDatagramContainer_Navigation: ...

class S7KDatagramContainer_SonarSettings_stream:
    def copy(self) -> S7KDatagramContainer_SonarSettings_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_SonarSettings_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_SonarSettings_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_SonarSettings_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_SonarSettings_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_SonarSettings_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_SonarSettings_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SonarSettings: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_SonarSettings_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_SonarSettings_stream: ...

class S7KDatagramContainer_SonarSettings:
    def copy(self) -> S7KDatagramContainer_SonarSettings:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_SonarSettings: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_SonarSettings: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_SonarSettings]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_SonarSettings: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_SonarSettings: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_SonarSettings: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SonarSettings: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_SonarSettings: ...

    def __reversed__(self) -> S7KDatagramContainer_SonarSettings: ...

class S7KDatagramContainer_MatchFilter_stream:
    def copy(self) -> S7KDatagramContainer_MatchFilter_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_MatchFilter_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_MatchFilter_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_MatchFilter_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_MatchFilter_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_MatchFilter_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_MatchFilter_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.MatchFilter: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_MatchFilter_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_MatchFilter_stream: ...

class S7KDatagramContainer_MatchFilter:
    def copy(self) -> S7KDatagramContainer_MatchFilter:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_MatchFilter: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_MatchFilter: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_MatchFilter]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_MatchFilter: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_MatchFilter: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_MatchFilter: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.MatchFilter: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_MatchFilter: ...

    def __reversed__(self) -> S7KDatagramContainer_MatchFilter: ...

class S7KDatagramContainer_SoundVelocity_stream:
    def copy(self) -> S7KDatagramContainer_SoundVelocity_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_SoundVelocity_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_SoundVelocity_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_SoundVelocity_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_SoundVelocity_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_SoundVelocity_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_SoundVelocity_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SoundVelocity: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_SoundVelocity_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_SoundVelocity_stream: ...

class S7KDatagramContainer_SoundVelocity:
    def copy(self) -> S7KDatagramContainer_SoundVelocity:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_SoundVelocity: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_SoundVelocity: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_SoundVelocity]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_SoundVelocity: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_SoundVelocity: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_SoundVelocity: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SoundVelocity: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_SoundVelocity: ...

    def __reversed__(self) -> S7KDatagramContainer_SoundVelocity: ...

class S7KDatagramContainer_AbsorptionLoss_stream:
    def copy(self) -> S7KDatagramContainer_AbsorptionLoss_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_AbsorptionLoss_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.AbsorptionLoss: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

class S7KDatagramContainer_AbsorptionLoss:
    def copy(self) -> S7KDatagramContainer_AbsorptionLoss:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_AbsorptionLoss: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_AbsorptionLoss: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_AbsorptionLoss]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_AbsorptionLoss: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_AbsorptionLoss: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_AbsorptionLoss: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.AbsorptionLoss: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_AbsorptionLoss: ...

    def __reversed__(self) -> S7KDatagramContainer_AbsorptionLoss: ...

class S7KDatagramContainer_SpreadingLoss_stream:
    def copy(self) -> S7KDatagramContainer_SpreadingLoss_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_SpreadingLoss_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_SpreadingLoss_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_SpreadingLoss_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_SpreadingLoss_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_SpreadingLoss_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_SpreadingLoss_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SpreadingLoss: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_SpreadingLoss_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_SpreadingLoss_stream: ...

class S7KDatagramContainer_SpreadingLoss:
    def copy(self) -> S7KDatagramContainer_SpreadingLoss:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_SpreadingLoss: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_SpreadingLoss: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_SpreadingLoss]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_SpreadingLoss: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_SpreadingLoss: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_SpreadingLoss: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SpreadingLoss: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_SpreadingLoss: ...

    def __reversed__(self) -> S7KDatagramContainer_SpreadingLoss: ...

class S7KDatagramContainer_RawDetection_stream:
    def copy(self) -> S7KDatagramContainer_RawDetection_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_RawDetection_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_RawDetection_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_RawDetection_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_RawDetection_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_RawDetection_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_RawDetection_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.RawDetection: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_RawDetection_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_RawDetection_stream: ...

class S7KDatagramContainer_RawDetection:
    def copy(self) -> S7KDatagramContainer_RawDetection:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_RawDetection: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_RawDetection: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_RawDetection]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_RawDetection: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_RawDetection: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_RawDetection: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.RawDetection: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_RawDetection: ...

    def __reversed__(self) -> S7KDatagramContainer_RawDetection: ...

class S7KDatagramContainer_Snippet_stream:
    def copy(self) -> S7KDatagramContainer_Snippet_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Snippet_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Snippet_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Snippet_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Snippet_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Snippet_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Snippet_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SnippetData: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Snippet_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Snippet_stream: ...

class S7KDatagramContainer_Snippet:
    def copy(self) -> S7KDatagramContainer_Snippet:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Snippet: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Snippet: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Snippet]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Snippet: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Snippet: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Snippet: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SnippetData: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Snippet: ...

    def __reversed__(self) -> S7KDatagramContainer_Snippet: ...

class S7KDatagramContainer_CompressedWaterColumn_stream:
    def copy(self) -> S7KDatagramContainer_CompressedWaterColumn_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_CompressedWaterColumn_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.CompressedWaterColumn: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

class S7KDatagramContainer_CompressedWaterColumn:
    def copy(self) -> S7KDatagramContainer_CompressedWaterColumn:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_CompressedWaterColumn: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_CompressedWaterColumn: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_CompressedWaterColumn]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_CompressedWaterColumn: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_CompressedWaterColumn: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_CompressedWaterColumn: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.CompressedWaterColumn: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_CompressedWaterColumn: ...

    def __reversed__(self) -> S7KDatagramContainer_CompressedWaterColumn: ...

class S7KDatagramContainer_BeamGeometry_stream:
    def copy(self) -> S7KDatagramContainer_BeamGeometry_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_BeamGeometry_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_BeamGeometry_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_BeamGeometry_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_BeamGeometry_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_BeamGeometry_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_BeamGeometry_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.BeamGeometry: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_BeamGeometry_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_BeamGeometry_stream: ...

class S7KDatagramContainer_BeamGeometry:
    def copy(self) -> S7KDatagramContainer_BeamGeometry:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_BeamGeometry: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_BeamGeometry: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_BeamGeometry]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_BeamGeometry: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_BeamGeometry: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_BeamGeometry: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.BeamGeometry: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_BeamGeometry: ...

    def __reversed__(self) -> S7KDatagramContainer_BeamGeometry: ...

class S7KDatagramContainer_Attitude_stream:
    def copy(self) -> S7KDatagramContainer_Attitude_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Attitude_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Attitude_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Attitude_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Attitude_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Attitude_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Attitude_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Attitude: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Attitude_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Attitude_stream: ...

class S7KDatagramContainer_Attitude:
    def copy(self) -> S7KDatagramContainer_Attitude:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Attitude: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Attitude: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Attitude]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Attitude: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Attitude: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Attitude: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Attitude: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Attitude: ...

    def __reversed__(self) -> S7KDatagramContainer_Attitude: ...

class S7KDatagramContainer_FileHeader_stream:
    def copy(self) -> S7KDatagramContainer_FileHeader_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_FileHeader_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_FileHeader_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_FileHeader_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_FileHeader_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_FileHeader_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_FileHeader_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.FileHeader: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_FileHeader_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_FileHeader_stream: ...

class S7KDatagramContainer_FileHeader:
    def copy(self) -> S7KDatagramContainer_FileHeader:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_FileHeader: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_FileHeader: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_FileHeader]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_FileHeader: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_FileHeader: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_FileHeader: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.FileHeader: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_FileHeader: ...

    def __reversed__(self) -> S7KDatagramContainer_FileHeader: ...

class S7KDatagramContainer_Snippet_SkippedData_stream:
    def copy(self) -> S7KDatagramContainer_Snippet_SkippedData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Snippet_SkippedData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Snippet_SkippedData_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Snippet_SkippedData_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Snippet_SkippedData_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Snippet_SkippedData_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Snippet_SkippedData_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SnippetData: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Snippet_SkippedData_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Snippet_SkippedData_stream: ...

class S7KDatagramContainer_Snippet_SkippedData:
    def copy(self) -> S7KDatagramContainer_Snippet_SkippedData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Snippet_SkippedData: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Snippet_SkippedData: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Snippet_SkippedData]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Snippet_SkippedData: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Snippet_SkippedData: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Snippet_SkippedData: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SnippetData: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Snippet_SkippedData: ...

    def __reversed__(self) -> S7KDatagramContainer_Snippet_SkippedData: ...

class S7KDatagramContainer_CompressedWaterColumn_SkippedData_stream:
    def copy(self) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_CompressedWaterColumn_SkippedData_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.CompressedWaterColumn: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData_stream: ...

class S7KDatagramContainer_CompressedWaterColumn_SkippedData:
    def copy(self) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_CompressedWaterColumn_SkippedData]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.CompressedWaterColumn: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData: ...

    def __reversed__(self) -> S7KDatagramContainer_CompressedWaterColumn_SkippedData: ...

class S7KDatagramContainer_Variant_stream:
    def copy(self) -> S7KDatagramContainer_Variant_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Variant_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Variant_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Variant_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Variant_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Variant_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Variant_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.S7KDatagram | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.S7KUnknown | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.ReferencePoint | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Position | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.RollPitchHeave | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Heading | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Navigation | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SonarSettings | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.MatchFilter | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SoundVelocity | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.AbsorptionLoss | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SpreadingLoss | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.RawDetection | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SnippetData | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.CompressedWaterColumn | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.BeamGeometry | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Attitude | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.FileHeader: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Variant_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Variant_stream: ...

class S7KDatagramContainer_Variant:
    def copy(self) -> S7KDatagramContainer_Variant:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Variant: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Variant: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Variant]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Variant: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Variant: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Variant: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.S7KDatagram | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.S7KUnknown | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.ReferencePoint | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Position | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.RollPitchHeave | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Heading | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Navigation | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SonarSettings | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.MatchFilter | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SoundVelocity | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.AbsorptionLoss | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SpreadingLoss | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.RawDetection | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SnippetData | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.CompressedWaterColumn | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.BeamGeometry | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Attitude | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.FileHeader: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Variant: ...

    def __reversed__(self) -> S7KDatagramContainer_Variant: ...

class S7KDatagramContainer_Variant_SkippedData_stream:
    def copy(self) -> S7KDatagramContainer_Variant_SkippedData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Variant_SkippedData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Variant_SkippedData_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Variant_SkippedData_stream]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Variant_SkippedData_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Variant_SkippedData_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Variant_SkippedData_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.S7KDatagram | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.S7KUnknown | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.ReferencePoint | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Position | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.RollPitchHeave | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Heading | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Navigation | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SonarSettings | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.MatchFilter | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SoundVelocity | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.AbsorptionLoss | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SpreadingLoss | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.RawDetection | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SnippetData | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.CompressedWaterColumn | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.BeamGeometry | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Attitude | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.FileHeader: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Variant_SkippedData_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Variant_SkippedData_stream: ...

class S7KDatagramContainer_Variant_SkippedData:
    def copy(self) -> S7KDatagramContainer_Variant_SkippedData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Variant_SkippedData: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Variant_SkippedData: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Variant_SkippedData]:
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

    def get_sorted_by_time(self) -> S7KDatagramContainer_Variant_SkippedData: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier) -> S7KDatagramContainer_Variant_SkippedData: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Variant_SkippedData: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.s7k.datagrams.S7KDatagram | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.S7KUnknown | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.ReferencePoint | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Position | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.RollPitchHeave | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Heading | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Navigation | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SonarSettings | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.MatchFilter | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SoundVelocity | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.AbsorptionLoss | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SpreadingLoss | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.RawDetection | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.SnippetData | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.CompressedWaterColumn | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.BeamGeometry | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.Attitude | themachinethatgoesping.echosounders_nanopy.s7k.datagrams.FileHeader: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Variant_SkippedData: ...

    def __reversed__(self) -> S7KDatagramContainer_Variant_SkippedData: ...
