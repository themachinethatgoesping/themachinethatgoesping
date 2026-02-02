"""KongsbergAll (kongsberg .all / .wcd) file data container classes"""

from collections.abc import Sequence
from typing import overload

import themachinethatgoesping.echosounders_nanopy.kongsbergall
import themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams
import themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes
import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.tools_nanopy.pyhelper


class KongsbergAllDatagramContainer_Header_stream:
    def copy(self) -> KongsbergAllDatagramContainer_Header_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_Header_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_Header_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Header_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Header_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Header_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Header_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Header_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_Header_stream: ...

class KongsbergAllDatagramContainer_Header:
    def copy(self) -> KongsbergAllDatagramContainer_Header:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_Header: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_Header: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Header]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Header: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Header: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Header: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Header: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_Header: ...

class KongsbergAllDatagramContainer_Unknown_stream:
    def copy(self) -> KongsbergAllDatagramContainer_Unknown_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_Unknown_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_Unknown_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Unknown_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Unknown_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Unknown_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Unknown_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Unknown_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_Unknown_stream: ...

class KongsbergAllDatagramContainer_Unknown:
    def copy(self) -> KongsbergAllDatagramContainer_Unknown:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_Unknown: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_Unknown: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Unknown]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Unknown: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Unknown: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Unknown: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Unknown: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_Unknown: ...

class KongsbergAllDatagramContainer_XYZDatagram_stream:
    def copy(self) -> KongsbergAllDatagramContainer_XYZDatagram_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_XYZDatagram_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_XYZDatagram_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_XYZDatagram_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_XYZDatagram_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_XYZDatagram_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_XYZDatagram_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.XYZDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_XYZDatagram_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_XYZDatagram_stream: ...

class KongsbergAllDatagramContainer_XYZDatagram:
    def copy(self) -> KongsbergAllDatagramContainer_XYZDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_XYZDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_XYZDatagram: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_XYZDatagram]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_XYZDatagram: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_XYZDatagram: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_XYZDatagram: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.XYZDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_XYZDatagram: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_XYZDatagram: ...

class KongsbergAllDatagramContainer_ExtraDetections_stream:
    def copy(self) -> KongsbergAllDatagramContainer_ExtraDetections_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_ExtraDetections_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_ExtraDetections_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_ExtraDetections_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ExtraDetections_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ExtraDetections_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_ExtraDetections_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraDetections: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_ExtraDetections_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_ExtraDetections_stream: ...

class KongsbergAllDatagramContainer_ExtraDetections:
    def copy(self) -> KongsbergAllDatagramContainer_ExtraDetections:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_ExtraDetections: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_ExtraDetections: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_ExtraDetections]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ExtraDetections: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ExtraDetections: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_ExtraDetections: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraDetections: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_ExtraDetections: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_ExtraDetections: ...

class KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
    def copy(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_RawRangeAndAngle_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RawRangeAndAngle: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle_stream: ...

class KongsbergAllDatagramContainer_RawRangeAndAngle:
    def copy(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_RawRangeAndAngle: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_RawRangeAndAngle]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_RawRangeAndAngle: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_RawRangeAndAngle: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RawRangeAndAngle: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_RawRangeAndAngle: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_RawRangeAndAngle: ...

class KongsbergAllDatagramContainer_SeabedImageData_stream:
    def copy(self) -> KongsbergAllDatagramContainer_SeabedImageData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_SeabedImageData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_SeabedImageData_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SeabedImageData_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SeabedImageData_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SeabedImageData_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SeabedImageData_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SeabedImageData: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SeabedImageData_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_SeabedImageData_stream: ...

class KongsbergAllDatagramContainer_SeabedImageData:
    def copy(self) -> KongsbergAllDatagramContainer_SeabedImageData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_SeabedImageData: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_SeabedImageData: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SeabedImageData]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SeabedImageData: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SeabedImageData: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SeabedImageData: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SeabedImageData: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SeabedImageData: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_SeabedImageData: ...

class KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
    def copy(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_WatercolumnDatagram_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_stream: ...

class KongsbergAllDatagramContainer_WatercolumnDatagram:
    def copy(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_WatercolumnDatagram: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_WatercolumnDatagram]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_WatercolumnDatagram: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_WatercolumnDatagram: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_WatercolumnDatagram: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram: ...

class KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
    def copy(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData_stream: ...

class KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
    def copy(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_WatercolumnDatagram_SkippedData: ...

class KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
    def copy(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_QualityFactorDatagram_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.QualityFactorDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram_stream: ...

class KongsbergAllDatagramContainer_QualityFactorDatagram:
    def copy(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_QualityFactorDatagram: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_QualityFactorDatagram]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_QualityFactorDatagram: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_QualityFactorDatagram: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.QualityFactorDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_QualityFactorDatagram: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_QualityFactorDatagram: ...

class KongsbergAllDatagramContainer_AttitudeDatagram_stream:
    def copy(self) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_AttitudeDatagram_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.AttitudeDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_AttitudeDatagram_stream: ...

class KongsbergAllDatagramContainer_AttitudeDatagram:
    def copy(self) -> KongsbergAllDatagramContainer_AttitudeDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_AttitudeDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_AttitudeDatagram: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_AttitudeDatagram]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_AttitudeDatagram: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_AttitudeDatagram: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_AttitudeDatagram: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.AttitudeDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_AttitudeDatagram: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_AttitudeDatagram: ...

class KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
    def copy(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram_stream: ...

class KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
    def copy(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_NetworkAttitudeVelocityDatagram: ...

class KongsbergAllDatagramContainer_ClockDatagram_stream:
    def copy(self) -> KongsbergAllDatagramContainer_ClockDatagram_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_ClockDatagram_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_ClockDatagram_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_ClockDatagram_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ClockDatagram_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ClockDatagram_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_ClockDatagram_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ClockDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_ClockDatagram_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_ClockDatagram_stream: ...

class KongsbergAllDatagramContainer_ClockDatagram:
    def copy(self) -> KongsbergAllDatagramContainer_ClockDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_ClockDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_ClockDatagram: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_ClockDatagram]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ClockDatagram: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ClockDatagram: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_ClockDatagram: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ClockDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_ClockDatagram: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_ClockDatagram: ...

class KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
    def copy(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.DepthOrHeightDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram_stream: ...

class KongsbergAllDatagramContainer_DepthOrHeightDatagram:
    def copy(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_DepthOrHeightDatagram]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.DepthOrHeightDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_DepthOrHeightDatagram: ...

class KongsbergAllDatagramContainer_HeadingDatagram_stream:
    def copy(self) -> KongsbergAllDatagramContainer_HeadingDatagram_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_HeadingDatagram_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_HeadingDatagram_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_HeadingDatagram_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_HeadingDatagram_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_HeadingDatagram_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_HeadingDatagram_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.HeadingDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_HeadingDatagram_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_HeadingDatagram_stream: ...

class KongsbergAllDatagramContainer_HeadingDatagram:
    def copy(self) -> KongsbergAllDatagramContainer_HeadingDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_HeadingDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_HeadingDatagram: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_HeadingDatagram]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_HeadingDatagram: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_HeadingDatagram: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_HeadingDatagram: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.HeadingDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_HeadingDatagram: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_HeadingDatagram: ...

class KongsbergAllDatagramContainer_PositionDatagram_stream:
    def copy(self) -> KongsbergAllDatagramContainer_PositionDatagram_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_PositionDatagram_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_PositionDatagram_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_PositionDatagram_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PositionDatagram_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PositionDatagram_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_PositionDatagram_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PositionDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_PositionDatagram_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_PositionDatagram_stream: ...

class KongsbergAllDatagramContainer_PositionDatagram:
    def copy(self) -> KongsbergAllDatagramContainer_PositionDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_PositionDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_PositionDatagram: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_PositionDatagram]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PositionDatagram: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PositionDatagram: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_PositionDatagram: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PositionDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_PositionDatagram: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_PositionDatagram: ...

class KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
    def copy(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SingleBeamEchoSounderDepth: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth_stream: ...

class KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
    def copy(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SingleBeamEchoSounderDepth: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_SingleBeamEchoSounderDepth: ...

class KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
    def copy(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram_stream: ...

class KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
    def copy(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_SurfaceSoundSpeedDatagram: ...

class KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
    def copy(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SoundSpeedProfileDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram_stream: ...

class KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
    def copy(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_SoundSpeedProfileDatagram]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SoundSpeedProfileDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_SoundSpeedProfileDatagram: ...

class KongsbergAllDatagramContainer_InstallationParameters_stream:
    def copy(self) -> KongsbergAllDatagramContainer_InstallationParameters_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_InstallationParameters_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_InstallationParameters_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_InstallationParameters_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_InstallationParameters_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_InstallationParameters_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_InstallationParameters_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_InstallationParameters_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_InstallationParameters_stream: ...

class KongsbergAllDatagramContainer_InstallationParameters:
    def copy(self) -> KongsbergAllDatagramContainer_InstallationParameters:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_InstallationParameters: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_InstallationParameters: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_InstallationParameters]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_InstallationParameters: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_InstallationParameters: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_InstallationParameters: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_InstallationParameters: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_InstallationParameters: ...

class KongsbergAllDatagramContainer_RuntimeParameters_stream:
    def copy(self) -> KongsbergAllDatagramContainer_RuntimeParameters_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_RuntimeParameters_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_RuntimeParameters_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_RuntimeParameters_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_RuntimeParameters_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_RuntimeParameters_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_RuntimeParameters_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_RuntimeParameters_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_RuntimeParameters_stream: ...

class KongsbergAllDatagramContainer_RuntimeParameters:
    def copy(self) -> KongsbergAllDatagramContainer_RuntimeParameters:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_RuntimeParameters: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_RuntimeParameters: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_RuntimeParameters]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_RuntimeParameters: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_RuntimeParameters: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_RuntimeParameters: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_RuntimeParameters: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_RuntimeParameters: ...

class KongsbergAllDatagramContainer_ExtraParameters_stream:
    def copy(self) -> KongsbergAllDatagramContainer_ExtraParameters_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_ExtraParameters_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_ExtraParameters_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_ExtraParameters_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ExtraParameters_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ExtraParameters_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_ExtraParameters_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_ExtraParameters_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_ExtraParameters_stream: ...

class KongsbergAllDatagramContainer_ExtraParameters:
    def copy(self) -> KongsbergAllDatagramContainer_ExtraParameters:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_ExtraParameters: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_ExtraParameters: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_ExtraParameters]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_ExtraParameters: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_ExtraParameters: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_ExtraParameters: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_ExtraParameters: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_ExtraParameters: ...

class KongsbergAllDatagramContainer_PUIDOutput_stream:
    def copy(self) -> KongsbergAllDatagramContainer_PUIDOutput_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_PUIDOutput_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_PUIDOutput_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_PUIDOutput_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PUIDOutput_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PUIDOutput_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_PUIDOutput_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUIDOutput: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_PUIDOutput_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_PUIDOutput_stream: ...

class KongsbergAllDatagramContainer_PUIDOutput:
    def copy(self) -> KongsbergAllDatagramContainer_PUIDOutput:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_PUIDOutput: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_PUIDOutput: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_PUIDOutput]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PUIDOutput: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PUIDOutput: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_PUIDOutput: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUIDOutput: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_PUIDOutput: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_PUIDOutput: ...

class KongsbergAllDatagramContainer_PUStatusOutput_stream:
    def copy(self) -> KongsbergAllDatagramContainer_PUStatusOutput_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_PUStatusOutput_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_PUStatusOutput_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_PUStatusOutput_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PUStatusOutput_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PUStatusOutput_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_PUStatusOutput_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUStatusOutput: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_PUStatusOutput_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_PUStatusOutput_stream: ...

class KongsbergAllDatagramContainer_PUStatusOutput:
    def copy(self) -> KongsbergAllDatagramContainer_PUStatusOutput:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_PUStatusOutput: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_PUStatusOutput: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_PUStatusOutput]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_PUStatusOutput: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_PUStatusOutput: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_PUStatusOutput: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUStatusOutput: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_PUStatusOutput: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_PUStatusOutput: ...

class KongsbergAllDatagramContainer_Variant_stream:
    def copy(self) -> KongsbergAllDatagramContainer_Variant_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_Variant_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_Variant_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Variant_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Variant_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Variant_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Variant_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.XYZDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraDetections | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SeabedImageData | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ClockDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.HeadingDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PositionDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUIDOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUStatusOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Variant_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_Variant_stream: ...

class KongsbergAllDatagramContainer_Variant:
    def copy(self) -> KongsbergAllDatagramContainer_Variant:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_Variant: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_Variant: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Variant]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Variant: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Variant: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Variant: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.XYZDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraDetections | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SeabedImageData | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ClockDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.HeadingDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PositionDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUIDOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUStatusOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Variant: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_Variant: ...

class KongsbergAllDatagramContainer_Variant_SkippedData_stream:
    def copy(self) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Variant_SkippedData_stream]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.XYZDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraDetections | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SeabedImageData | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ClockDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.HeadingDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PositionDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUIDOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUStatusOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_Variant_SkippedData_stream: ...

class KongsbergAllDatagramContainer_Variant_SkippedData:
    def copy(self) -> KongsbergAllDatagramContainer_Variant_SkippedData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagramContainer_Variant_SkippedData: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagramContainer_Variant_SkippedData: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllDatagramContainer_Variant_SkippedData]:
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

    def get_sorted_by_time(self) -> KongsbergAllDatagramContainer_Variant_SkippedData: ...

    def count_datagrams_per_type(self) -> dict[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> KongsbergAllDatagramContainer_Variant_SkippedData: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]) -> KongsbergAllDatagramContainer_Variant_SkippedData: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.XYZDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraDetections | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RawRangeAndAngle | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SeabedImageData | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.QualityFactorDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.AttitudeDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.NetworkAttitudeVelocityDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ClockDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.DepthOrHeightDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.HeadingDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PositionDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SingleBeamEchoSounderDepth | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SurfaceSoundSpeedDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.SoundSpeedProfileDatagram | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUIDOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.PUStatusOutput | themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.KongsbergAllUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllDatagramContainer_Variant_SkippedData: ...

    def __reversed__(self) -> KongsbergAllDatagramContainer_Variant_SkippedData: ...

class KongsbergAllPingContainer_stream:
    @overload
    def __init__(self) -> None:
        """Construct a new empty PingContainer object"""

    @overload
    def __init__(self, arg: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes.KongsbergAllPing_stream], /) -> None: ...

    def copy(self) -> KongsbergAllPingContainer_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllPingContainer_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllPingContainer_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def max_number_of_samples(self) -> int: ...

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllPingContainer_stream]:
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

    def split_by_sensor_configuration(self) -> dict[themachinethatgoesping.navigation_nanopy.SensorConfiguration, KongsbergAllPingContainer_stream]: ...

    def get_sorted_by_time(self) -> KongsbergAllPingContainer_stream: ...

    def count_pings_per_channel_id(self) -> dict[str, int]: ...

    def find_channel_ids(self) -> list[str]: ...

    @overload
    def __call__(self, channel_id: str) -> KongsbergAllPingContainer_stream: ...

    @overload
    def __call__(self, channel_ids: Sequence[str]) -> KongsbergAllPingContainer_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    def get_pings(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes.KongsbergAllPing_stream]: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes.KongsbergAllPing_stream: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllPingContainer_stream: ...

    def __reversed__(self) -> KongsbergAllPingContainer_stream: ...

class KongsbergAllPingContainer:
    @overload
    def __init__(self) -> None:
        """Construct a new empty PingContainer object"""

    @overload
    def __init__(self, arg: Sequence[themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes.KongsbergAllPing], /) -> None: ...

    def copy(self) -> KongsbergAllPingContainer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllPingContainer: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllPingContainer: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def max_number_of_samples(self) -> int: ...

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[KongsbergAllPingContainer]:
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

    def split_by_sensor_configuration(self) -> dict[themachinethatgoesping.navigation_nanopy.SensorConfiguration, KongsbergAllPingContainer]: ...

    def get_sorted_by_time(self) -> KongsbergAllPingContainer: ...

    def count_pings_per_channel_id(self) -> dict[str, int]: ...

    def find_channel_ids(self) -> list[str]: ...

    @overload
    def __call__(self, channel_id: str) -> KongsbergAllPingContainer: ...

    @overload
    def __call__(self, channel_ids: Sequence[str]) -> KongsbergAllPingContainer: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    def get_pings(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes.KongsbergAllPing]: ...

    @overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filetypes.KongsbergAllPing: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> KongsbergAllPingContainer: ...

    def __reversed__(self) -> KongsbergAllPingContainer: ...
