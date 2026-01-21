from collections.abc import Sequence
from typing import overload

import themachinethatgoesping.echosounders_nanopy.kmall
import themachinethatgoesping.echosounders_nanopy.kmall.datagrams
import themachinethatgoesping.echosounders_nanopy.kmall.filetypes
import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.tools_nanopy.pyhelper


class KMALLDatagramContainer_Header_stream:
    def copy(self) -> KMALLDatagramContainer_Header_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_Header_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_Header_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_Header_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_Header_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_Header_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_Header_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.KMALLDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_Header_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_Header_stream: ...

class KMALLDatagramContainer_Header:
    def copy(self) -> KMALLDatagramContainer_Header:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_Header: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_Header: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_Header]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_Header: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_Header: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_Header: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.KMALLDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_Header: ...

    def __reversed__(self) -> KMALLDatagramContainer_Header: ...

class KMALLDatagramContainer_Unknown_stream:
    def copy(self) -> KMALLDatagramContainer_Unknown_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_Unknown_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_Unknown_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_Unknown_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_Unknown_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_Unknown_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_Unknown_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.KMALLUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_Unknown_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_Unknown_stream: ...

class KMALLDatagramContainer_Unknown:
    def copy(self) -> KMALLDatagramContainer_Unknown:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_Unknown: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_Unknown: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_Unknown]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_Unknown: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_Unknown: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_Unknown: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.KMALLUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_Unknown: ...

    def __reversed__(self) -> KMALLDatagramContainer_Unknown: ...

class KMALLDatagramContainer_IInstallationParam_stream:
    def copy(self) -> KMALLDatagramContainer_IInstallationParam_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_IInstallationParam_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_IInstallationParam_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_IInstallationParam_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_IInstallationParam_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_IInstallationParam_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_IInstallationParam_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IInstallationParam: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_IInstallationParam_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_IInstallationParam_stream: ...

class KMALLDatagramContainer_IInstallationParam:
    def copy(self) -> KMALLDatagramContainer_IInstallationParam:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_IInstallationParam: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_IInstallationParam: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_IInstallationParam]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_IInstallationParam: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_IInstallationParam: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_IInstallationParam: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IInstallationParam: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_IInstallationParam: ...

    def __reversed__(self) -> KMALLDatagramContainer_IInstallationParam: ...

class KMALLDatagramContainer_IOpRuntime_stream:
    def copy(self) -> KMALLDatagramContainer_IOpRuntime_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_IOpRuntime_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_IOpRuntime_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_IOpRuntime_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_IOpRuntime_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_IOpRuntime_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_IOpRuntime_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IOpRuntime: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_IOpRuntime_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_IOpRuntime_stream: ...

class KMALLDatagramContainer_IOpRuntime:
    def copy(self) -> KMALLDatagramContainer_IOpRuntime:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_IOpRuntime: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_IOpRuntime: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_IOpRuntime]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_IOpRuntime: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_IOpRuntime: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_IOpRuntime: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IOpRuntime: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_IOpRuntime: ...

    def __reversed__(self) -> KMALLDatagramContainer_IOpRuntime: ...

class KMALLDatagramContainer_SPosition_stream:
    def copy(self) -> KMALLDatagramContainer_SPosition_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_SPosition_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_SPosition_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_SPosition_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_SPosition_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_SPosition_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_SPosition_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SPosition: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_SPosition_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_SPosition_stream: ...

class KMALLDatagramContainer_SPosition:
    def copy(self) -> KMALLDatagramContainer_SPosition:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_SPosition: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_SPosition: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_SPosition]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_SPosition: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_SPosition: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_SPosition: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SPosition: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_SPosition: ...

    def __reversed__(self) -> KMALLDatagramContainer_SPosition: ...

class KMALLDatagramContainer_SPositionError_stream:
    def copy(self) -> KMALLDatagramContainer_SPositionError_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_SPositionError_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_SPositionError_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_SPositionError_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_SPositionError_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_SPositionError_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_SPositionError_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SPositionError: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_SPositionError_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_SPositionError_stream: ...

class KMALLDatagramContainer_SPositionError:
    def copy(self) -> KMALLDatagramContainer_SPositionError:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_SPositionError: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_SPositionError: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_SPositionError]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_SPositionError: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_SPositionError: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_SPositionError: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SPositionError: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_SPositionError: ...

    def __reversed__(self) -> KMALLDatagramContainer_SPositionError: ...

class KMALLDatagramContainer_SClock_stream:
    def copy(self) -> KMALLDatagramContainer_SClock_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_SClock_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_SClock_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_SClock_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_SClock_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_SClock_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_SClock_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SClock: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_SClock_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_SClock_stream: ...

class KMALLDatagramContainer_SClock:
    def copy(self) -> KMALLDatagramContainer_SClock:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_SClock: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_SClock: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_SClock]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_SClock: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_SClock: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_SClock: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SClock: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_SClock: ...

    def __reversed__(self) -> KMALLDatagramContainer_SClock: ...

class KMALLDatagramContainer_SSoundVelocityProfile_stream:
    def copy(self) -> KMALLDatagramContainer_SSoundVelocityProfile_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_SSoundVelocityProfile_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_SSoundVelocityProfile_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_SSoundVelocityProfile_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_SSoundVelocityProfile_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_SSoundVelocityProfile_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_SSoundVelocityProfile_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityProfile: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_SSoundVelocityProfile_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_SSoundVelocityProfile_stream: ...

class KMALLDatagramContainer_SSoundVelocityProfile:
    def copy(self) -> KMALLDatagramContainer_SSoundVelocityProfile:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_SSoundVelocityProfile: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_SSoundVelocityProfile: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_SSoundVelocityProfile]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_SSoundVelocityProfile: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_SSoundVelocityProfile: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_SSoundVelocityProfile: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityProfile: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_SSoundVelocityProfile: ...

    def __reversed__(self) -> KMALLDatagramContainer_SSoundVelocityProfile: ...

class KMALLDatagramContainer_SSoundVelocityTransducer_stream:
    def copy(self) -> KMALLDatagramContainer_SSoundVelocityTransducer_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_SSoundVelocityTransducer_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_SSoundVelocityTransducer_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_SSoundVelocityTransducer_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_SSoundVelocityTransducer_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_SSoundVelocityTransducer_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_SSoundVelocityTransducer_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityTransducer: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_SSoundVelocityTransducer_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_SSoundVelocityTransducer_stream: ...

class KMALLDatagramContainer_SSoundVelocityTransducer:
    def copy(self) -> KMALLDatagramContainer_SSoundVelocityTransducer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_SSoundVelocityTransducer: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_SSoundVelocityTransducer: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_SSoundVelocityTransducer]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_SSoundVelocityTransducer: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_SSoundVelocityTransducer: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_SSoundVelocityTransducer: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityTransducer: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_SSoundVelocityTransducer: ...

    def __reversed__(self) -> KMALLDatagramContainer_SSoundVelocityTransducer: ...

class KMALLDatagramContainer_SKMBinary_stream:
    def copy(self) -> KMALLDatagramContainer_SKMBinary_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_SKMBinary_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_SKMBinary_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_SKMBinary_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_SKMBinary_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_SKMBinary_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_SKMBinary_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SKMBinary: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_SKMBinary_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_SKMBinary_stream: ...

class KMALLDatagramContainer_SKMBinary:
    def copy(self) -> KMALLDatagramContainer_SKMBinary:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_SKMBinary: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_SKMBinary: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_SKMBinary]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_SKMBinary: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_SKMBinary: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_SKMBinary: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SKMBinary: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_SKMBinary: ...

    def __reversed__(self) -> KMALLDatagramContainer_SKMBinary: ...

class KMALLDatagramContainer_CPosition_stream:
    def copy(self) -> KMALLDatagramContainer_CPosition_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_CPosition_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_CPosition_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_CPosition_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_CPosition_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_CPosition_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_CPosition_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.CPosition: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_CPosition_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_CPosition_stream: ...

class KMALLDatagramContainer_CPosition:
    def copy(self) -> KMALLDatagramContainer_CPosition:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_CPosition: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_CPosition: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_CPosition]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_CPosition: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_CPosition: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_CPosition: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.CPosition: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_CPosition: ...

    def __reversed__(self) -> KMALLDatagramContainer_CPosition: ...

class KMALLDatagramContainer_CHeave_stream:
    def copy(self) -> KMALLDatagramContainer_CHeave_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_CHeave_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_CHeave_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_CHeave_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_CHeave_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_CHeave_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_CHeave_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.CHeave: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_CHeave_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_CHeave_stream: ...

class KMALLDatagramContainer_CHeave:
    def copy(self) -> KMALLDatagramContainer_CHeave:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_CHeave: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_CHeave: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_CHeave]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_CHeave: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_CHeave: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_CHeave: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.CHeave: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_CHeave: ...

    def __reversed__(self) -> KMALLDatagramContainer_CHeave: ...

class KMALLDatagramContainer_MRangeAndDepth_stream:
    def copy(self) -> KMALLDatagramContainer_MRangeAndDepth_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_MRangeAndDepth_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_MRangeAndDepth_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_MRangeAndDepth_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_MRangeAndDepth_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_MRangeAndDepth_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_MRangeAndDepth_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MRangeAndDepth: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_MRangeAndDepth_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_MRangeAndDepth_stream: ...

class KMALLDatagramContainer_MRangeAndDepth:
    def copy(self) -> KMALLDatagramContainer_MRangeAndDepth:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_MRangeAndDepth: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_MRangeAndDepth: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_MRangeAndDepth]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_MRangeAndDepth: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_MRangeAndDepth: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_MRangeAndDepth: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MRangeAndDepth: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_MRangeAndDepth: ...

    def __reversed__(self) -> KMALLDatagramContainer_MRangeAndDepth: ...

class KMALLDatagramContainer_MWaterColumn_stream:
    def copy(self) -> KMALLDatagramContainer_MWaterColumn_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_MWaterColumn_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_MWaterColumn_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_MWaterColumn_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_MWaterColumn_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_MWaterColumn_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_MWaterColumn_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MWaterColumn: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_MWaterColumn_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_MWaterColumn_stream: ...

class KMALLDatagramContainer_MWaterColumn:
    def copy(self) -> KMALLDatagramContainer_MWaterColumn:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_MWaterColumn: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_MWaterColumn: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_MWaterColumn]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_MWaterColumn: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_MWaterColumn: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_MWaterColumn: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MWaterColumn: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_MWaterColumn: ...

    def __reversed__(self) -> KMALLDatagramContainer_MWaterColumn: ...

class KMALLDatagramContainer_MWaterColumn_SkippedData_stream:
    def copy(self) -> KMALLDatagramContainer_MWaterColumn_SkippedData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_MWaterColumn_SkippedData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_MWaterColumn_SkippedData_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_MWaterColumn_SkippedData_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_MWaterColumn_SkippedData_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_MWaterColumn_SkippedData_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_MWaterColumn_SkippedData_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MWaterColumn: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_MWaterColumn_SkippedData_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_MWaterColumn_SkippedData_stream: ...

class KMALLDatagramContainer_MWaterColumn_SkippedData:
    def copy(self) -> KMALLDatagramContainer_MWaterColumn_SkippedData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_MWaterColumn_SkippedData: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_MWaterColumn_SkippedData: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_MWaterColumn_SkippedData]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_MWaterColumn_SkippedData: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_MWaterColumn_SkippedData: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_MWaterColumn_SkippedData: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MWaterColumn: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_MWaterColumn_SkippedData: ...

    def __reversed__(self) -> KMALLDatagramContainer_MWaterColumn_SkippedData: ...

class KMALLDatagramContainer_Variant_stream:
    def copy(self) -> KMALLDatagramContainer_Variant_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_Variant_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_Variant_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_Variant_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_Variant_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_Variant_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_Variant_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.KMALLDatagram | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.KMALLUnknown | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MRangeAndDepth | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MWaterColumn | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IInstallationParam | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IOpRuntime | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SPosition | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SPositionError | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SClock | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityProfile | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityTransducer | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SKMBinary | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.CPosition | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.CHeave: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_Variant_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_Variant_stream: ...

class KMALLDatagramContainer_Variant:
    def copy(self) -> KMALLDatagramContainer_Variant:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_Variant: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_Variant: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_Variant]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_Variant: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_Variant: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_Variant: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.KMALLDatagram | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.KMALLUnknown | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MRangeAndDepth | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MWaterColumn | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IInstallationParam | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IOpRuntime | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SPosition | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SPositionError | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SClock | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityProfile | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityTransducer | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SKMBinary | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.CPosition | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.CHeave: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_Variant: ...

    def __reversed__(self) -> KMALLDatagramContainer_Variant: ...

class KMALLDatagramContainer_Variant_SkippedData_stream:
    def copy(self) -> KMALLDatagramContainer_Variant_SkippedData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_Variant_SkippedData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_Variant_SkippedData_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_Variant_SkippedData_stream]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_Variant_SkippedData_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_Variant_SkippedData_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_Variant_SkippedData_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.KMALLDatagram | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.KMALLUnknown | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MRangeAndDepth | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MWaterColumn | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IInstallationParam | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IOpRuntime | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SPosition | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SPositionError | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SClock | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityProfile | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityTransducer | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SKMBinary | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.CPosition | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.CHeave: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_Variant_SkippedData_stream: ...

    def __reversed__(self) -> KMALLDatagramContainer_Variant_SkippedData_stream: ...

class KMALLDatagramContainer_Variant_SkippedData:
    def copy(self) -> KMALLDatagramContainer_Variant_SkippedData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagramContainer_Variant_SkippedData: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagramContainer_Variant_SkippedData: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLDatagramContainer_Variant_SkippedData]:
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

    def get_sorted_by_time(self) -> KMALLDatagramContainer_Variant_SkippedData: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier) -> KMALLDatagramContainer_Variant_SkippedData: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]) -> KMALLDatagramContainer_Variant_SkippedData: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.KMALLDatagram | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.KMALLUnknown | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MRangeAndDepth | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.MWaterColumn | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IInstallationParam | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IOpRuntime | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SPosition | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SPositionError | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SClock | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityProfile | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityTransducer | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SKMBinary | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.CPosition | themachinethatgoesping.echosounders_nanopy.kmall.datagrams.CHeave: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLDatagramContainer_Variant_SkippedData: ...

    def __reversed__(self) -> KMALLDatagramContainer_Variant_SkippedData: ...

class KMALLPingContainer_stream:
    @overload
    def __init__(self) -> None:
        """Construct a new empty PingContainer object"""

    @overload
    def __init__(self, arg: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.filetypes.KMALLPing_stream], /) -> None: ...

    def copy(self) -> KMALLPingContainer_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLPingContainer_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLPingContainer_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def max_number_of_samples(self) -> int: ...

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLPingContainer_stream]:
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

    def split_by_sensor_configuration(self) -> dict[themachinethatgoesping.navigation_nanopy.SensorConfiguration, KMALLPingContainer_stream]: ...

    def get_sorted_by_time(self) -> KMALLPingContainer_stream: ...

    def count_pings_per_channel_id(self) -> dict[str, int]: ...

    def find_channel_ids(self) -> list[str]: ...

    @overload
    def __call__(self, channel_id: str) -> KMALLPingContainer_stream: ...

    @overload
    def __call__(self, channel_ids: Sequence[str]) -> KMALLPingContainer_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    def get_pings(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.filetypes.KMALLPing_stream]: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.filetypes.KMALLPing_stream: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLPingContainer_stream: ...

    def __reversed__(self) -> KMALLPingContainer_stream: ...

class KMALLPingContainer:
    @overload
    def __init__(self) -> None:
        """Construct a new empty PingContainer object"""

    @overload
    def __init__(self, arg: Sequence[themachinethatgoesping.echosounders_nanopy.kmall.filetypes.KMALLPing], /) -> None: ...

    def copy(self) -> KMALLPingContainer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLPingContainer: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLPingContainer: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def max_number_of_samples(self) -> int: ...

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KMALLPingContainer]:
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

    def split_by_sensor_configuration(self) -> dict[themachinethatgoesping.navigation_nanopy.SensorConfiguration, KMALLPingContainer]: ...

    def get_sorted_by_time(self) -> KMALLPingContainer: ...

    def count_pings_per_channel_id(self) -> dict[str, int]: ...

    def find_channel_ids(self) -> list[str]: ...

    @overload
    def __call__(self, channel_id: str) -> KMALLPingContainer: ...

    @overload
    def __call__(self, channel_ids: Sequence[str]) -> KMALLPingContainer: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    def get_pings(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.filetypes.KMALLPing]: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kmall.filetypes.KMALLPing: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KMALLPingContainer: ...

    def __reversed__(self) -> KMALLPingContainer: ...
