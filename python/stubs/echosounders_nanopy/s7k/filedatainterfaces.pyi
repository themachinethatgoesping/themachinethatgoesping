"""Teledyne RESON .s7k (7k) file data interface classes"""
import typing

from collections.abc import Mapping, Sequence
from typing import overload

import themachinethatgoesping.echosounders_nanopy.s7k
import themachinethatgoesping.echosounders_nanopy.s7k.filedatacontainers
import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.navigation_nanopy.datastructures
import themachinethatgoesping.tools_nanopy.progressbars


class S7KDatagramInterface_stream:
    """
    Datagram interface for the .s7k (7k) data format. Holds the datagram
    index (position, timestamp and record type of every datagram) and
    provides access to the raw datagrams.
    """

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KDatagramInterface:
    """
    Datagram interface for the .s7k (7k) data format. Holds the datagram
    index (position, timestamp and record type of every datagram) and
    provides access to the raw datagrams.
    """

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KDatagramDataInterfacePerFile_stream:
    """
    FileDataInterface (for single files) that indexes all datagrams of a
    file. This is the generic interface that keeps track of every datagram
    (regardless of the specialized interface it was sorted into).

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file.

    Template Args:
        t_ifstream:
    """

    def init_from_file(self, index_path: str = '', force: bool = False) -> None: ...

    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file

        Returns:
            size_t
        """

    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file

        Returns:
            size_t
        """

    def get_file_path(self) -> str:
        """
        Get the file name This function assumes that the file name is the same
        for_linked_file all datagrams in the file

        Returns:
            std::string
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file

        Returns:
            std::string
        """

    def deinitialize(self) -> None: ...

    def is_initialized(self) -> bool: ...

    def is_primary_file(self) -> bool: ...

    def is_secondary_file(self) -> bool: ...

    def has_linked_file(self) -> bool: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KDatagramDataInterfacePerFile:
    """
    FileDataInterface (for single files) that indexes all datagrams of a
    file. This is the generic interface that keeps track of every datagram
    (regardless of the specialized interface it was sorted into).

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file.

    Template Args:
        t_ifstream:
    """

    def init_from_file(self, index_path: str = '', force: bool = False) -> None: ...

    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file

        Returns:
            size_t
        """

    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file

        Returns:
            size_t
        """

    def get_file_path(self) -> str:
        """
        Get the file name This function assumes that the file name is the same
        for_linked_file all datagrams in the file

        Returns:
            std::string
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file

        Returns:
            std::string
        """

    def deinitialize(self) -> None: ...

    def is_initialized(self) -> bool: ...

    def is_primary_file(self) -> bool: ...

    def is_secondary_file(self) -> bool: ...

    def has_linked_file(self) -> bool: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KDatagramDataInterface_stream:
    """
    FileDataInterface (for multiple files) that indexes all datagrams of
    the files. This is the generic interface that keeps track of every
    datagram (regardless of the specialized interface it was sorted into).

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file.

    Template Args:
        t_ifstream:
    """

    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[S7KDatagramDataInterfacePerFile_stream]) -> list[S7KDatagramDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[S7KDatagramDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> S7KDatagramDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[S7KDatagramDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[S7KDatagramDataInterfacePerFile_stream]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """This functions throws if linked file interfaces are not consistent"""

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str] = {}, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False, mp_cores: int = 1) -> None: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KDatagramDataInterface:
    """
    FileDataInterface (for multiple files) that indexes all datagrams of
    the files. This is the generic interface that keeps track of every
    datagram (regardless of the specialized interface it was sorted into).

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file.

    Template Args:
        t_ifstream:
    """

    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[S7KDatagramDataInterfacePerFile]) -> list[S7KDatagramDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[S7KDatagramDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> S7KDatagramDataInterfacePerFile: ...

    def per_primary_file(self) -> list[S7KDatagramDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[S7KDatagramDataInterfacePerFile]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """This functions throws if linked file interfaces are not consistent"""

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str] = {}, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False, mp_cores: int = 1) -> None: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KOtherFileDataInterfacePerFile_stream:
    """
    FileDataInterface (for single files) for packages that fit neither of
    the other FileDataInterfaces (Configuration, Navigation, Environment,
    Ping)

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file.

    Template Args:
        t_ifstream:
    """

    def init_from_file(self, index_path: str = '', force: bool = False) -> None: ...

    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file

        Returns:
            size_t
        """

    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file

        Returns:
            size_t
        """

    def get_file_path(self) -> str:
        """
        Get the file name This function assumes that the file name is the same
        for_linked_file all datagrams in the file

        Returns:
            std::string
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file

        Returns:
            std::string
        """

    def deinitialize(self) -> None: ...

    def is_initialized(self) -> bool: ...

    def is_primary_file(self) -> bool: ...

    def is_secondary_file(self) -> bool: ...

    def has_linked_file(self) -> bool: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KOtherFileDataInterfacePerFile:
    """
    FileDataInterface (for single files) for packages that fit neither of
    the other FileDataInterfaces (Configuration, Navigation, Environment,
    Ping)

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file.

    Template Args:
        t_ifstream:
    """

    def init_from_file(self, index_path: str = '', force: bool = False) -> None: ...

    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file

        Returns:
            size_t
        """

    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file

        Returns:
            size_t
        """

    def get_file_path(self) -> str:
        """
        Get the file name This function assumes that the file name is the same
        for_linked_file all datagrams in the file

        Returns:
            std::string
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file

        Returns:
            std::string
        """

    def deinitialize(self) -> None: ...

    def is_initialized(self) -> bool: ...

    def is_primary_file(self) -> bool: ...

    def is_secondary_file(self) -> bool: ...

    def has_linked_file(self) -> bool: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KOtherFileDataInterface_stream:
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Environment, Ping)

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file.

    Template Args:
        t_ifstream:
    """

    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[S7KOtherFileDataInterfacePerFile_stream]) -> list[S7KOtherFileDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[S7KOtherFileDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> S7KOtherFileDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[S7KOtherFileDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[S7KOtherFileDataInterfacePerFile_stream]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """This functions throws if linked file interfaces are not consistent"""

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str] = {}, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False, mp_cores: int = 1) -> None: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KOtherFileDataInterface:
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Environment, Ping)

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file.

    Template Args:
        t_ifstream:
    """

    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[S7KOtherFileDataInterfacePerFile]) -> list[S7KOtherFileDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[S7KOtherFileDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> S7KOtherFileDataInterfacePerFile: ...

    def per_primary_file(self) -> list[S7KOtherFileDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[S7KOtherFileDataInterfacePerFile]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """This functions throws if linked file interfaces are not consistent"""

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str] = {}, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False, mp_cores: int = 1) -> None: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KConfigurationDataInterfacePerFile_stream:
    """
    Interface that reads the sensor/sonar configuration (installation
    offsets, transducer setup) of a single .s7k file.



    $.. note::

    The datagram-processing functions (read_sensor_configuration) are not
    implemented yet. The class currently only provides the structure so
    the configuration can be filled in in a later step; until then the
    inherited base behavior (empty configuration fallback) is used.

    Template Args:
        t_ifstream:
    """

    def init_from_file(self, index_path: str = '', force: bool = False) -> None: ...

    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file

        Returns:
            size_t
        """

    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file

        Returns:
            size_t
        """

    def get_file_path(self) -> str:
        """
        Get the file name This function assumes that the file name is the same
        for_linked_file all datagrams in the file

        Returns:
            std::string
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file

        Returns:
            std::string
        """

    def deinitialize(self) -> None: ...

    def is_initialized(self) -> bool: ...

    def is_primary_file(self) -> bool: ...

    def is_secondary_file(self) -> bool: ...

    def has_linked_file(self) -> bool: ...

    def read_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration: ...

    def get_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration: ...

    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation_nanopy.SensorConfiguration) -> None: ...

    def get_use_surface_sound_speed_in_sound_velocity_profile(self) -> bool:
        """
        Whether the measured transducer/surface sound speed is integrated into
        the sound velocity profile at the transducer depth when ray tracing.

        This is read from the file's installation parameters when the
        interface is initialized (e.g. from the Kongsberg .all "SHC" field: 0
        -> true, 1 -> false). Formats that do not specify it default to true.
        It can be overridden with
        set_use_surface_sound_speed_in_sound_velocity_profile().

        Returns:
            true if the surface sound speed should be used, false otherwise.
        """

    def set_use_surface_sound_speed_in_sound_velocity_profile(self, use_surface_sound_speed: bool) -> None:
        """
        Set whether the measured transducer/surface sound speed is integrated
        into the sound velocity profile at the transducer depth when ray
        tracing.

        Args:
            use_surface_sound_speed: true to use the surface sound speed,
                                     false to raytrace the archived profile as
                                     is.
        """

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KConfigurationDataInterfacePerFile:
    """
    Interface that reads the sensor/sonar configuration (installation
    offsets, transducer setup) of a single .s7k file.



    $.. note::

    The datagram-processing functions (read_sensor_configuration) are not
    implemented yet. The class currently only provides the structure so
    the configuration can be filled in in a later step; until then the
    inherited base behavior (empty configuration fallback) is used.

    Template Args:
        t_ifstream:
    """

    def init_from_file(self, index_path: str = '', force: bool = False) -> None: ...

    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file

        Returns:
            size_t
        """

    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file

        Returns:
            size_t
        """

    def get_file_path(self) -> str:
        """
        Get the file name This function assumes that the file name is the same
        for_linked_file all datagrams in the file

        Returns:
            std::string
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file

        Returns:
            std::string
        """

    def deinitialize(self) -> None: ...

    def is_initialized(self) -> bool: ...

    def is_primary_file(self) -> bool: ...

    def is_secondary_file(self) -> bool: ...

    def has_linked_file(self) -> bool: ...

    def read_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration: ...

    def get_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration: ...

    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation_nanopy.SensorConfiguration) -> None: ...

    def get_use_surface_sound_speed_in_sound_velocity_profile(self) -> bool:
        """
        Whether the measured transducer/surface sound speed is integrated into
        the sound velocity profile at the transducer depth when ray tracing.

        This is read from the file's installation parameters when the
        interface is initialized (e.g. from the Kongsberg .all "SHC" field: 0
        -> true, 1 -> false). Formats that do not specify it default to true.
        It can be overridden with
        set_use_surface_sound_speed_in_sound_velocity_profile().

        Returns:
            true if the surface sound speed should be used, false otherwise.
        """

    def set_use_surface_sound_speed_in_sound_velocity_profile(self, use_surface_sound_speed: bool) -> None:
        """
        Set whether the measured transducer/surface sound speed is integrated
        into the sound velocity profile at the transducer depth when ray
        tracing.

        Args:
            use_surface_sound_speed: true to use the surface sound speed,
                                     false to raytrace the archived profile as
                                     is.
        """

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KConfigurationDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[S7KConfigurationDataInterfacePerFile_stream]) -> list[S7KConfigurationDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[S7KConfigurationDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> S7KConfigurationDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[S7KConfigurationDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[S7KConfigurationDataInterfacePerFile_stream]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """This functions throws if linked file interfaces are not consistent"""

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str] = {}, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False, mp_cores: int = 1) -> None: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def get_sensor_configuration(self, index: int) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration: ...

    def get_trx_sensor_configuration_per_target_id(self, index: int) -> dict: ...

class S7KConfigurationDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[S7KConfigurationDataInterfacePerFile]) -> list[S7KConfigurationDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[S7KConfigurationDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> S7KConfigurationDataInterfacePerFile: ...

    def per_primary_file(self) -> list[S7KConfigurationDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[S7KConfigurationDataInterfacePerFile]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """This functions throws if linked file interfaces are not consistent"""

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str] = {}, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False, mp_cores: int = 1) -> None: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def get_sensor_configuration(self, index: int) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration: ...

    def get_trx_sensor_configuration_per_target_id(self, index: int) -> dict: ...

class S7KNavigationDataInterfacePerFile_stream:
    """
    Interface that reads the navigation (position, attitude, heading) of a
    single .s7k file.

    The 7k format stores each navigation quantity in two kinds of records:
    a modern "fused" record (1015 Navigation for position/heading, 1016
    Attitude for roll/pitch/heave/heading) and a legacy single-quantity
    record (1003 Position, 1012 Roll Pitch Heave, 1013 Heading). By
    default the modern records are preferred; the two preferences can be
    toggled with the setters below.

    Template Args:
        t_ifstream:
    """

    def get_prefer_navigation_over_position(self) -> bool:
        """
        Get whether the 1015 Navigation record is preferred over the 1003
        Position record
        Returns:
            true if 1015 Navigation is preferred (default)
        """

    def set_prefer_navigation_over_position(self, prefer: bool) -> None:
        """
        Set whether the 1015 Navigation record is preferred over the 1003
        Position record
        Args:
            prefer: true to prefer 1015 Navigation (default), false to prefer
                    1003 Position
        """

    def get_prefer_attitude_over_rollpitchheave(self) -> bool:
        """
        Get whether the 1016 Attitude record is preferred over the 1012 Roll
        Pitch Heave record
        Returns:
            true if 1016 Attitude is preferred (default)
        """

    def set_prefer_attitude_over_rollpitchheave(self, prefer: bool) -> None:
        """
        Set whether the 1016 Attitude record is preferred over the 1012 Roll
        Pitch Heave record
        Args:
            prefer: true to prefer 1016 Attitude (default), false to prefer
                    1012 Roll Pitch Heave
        """

    def init_from_file(self, index_path: str = '', force: bool = False) -> None: ...

    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file

        Returns:
            size_t
        """

    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file

        Returns:
            size_t
        """

    def get_file_path(self) -> str:
        """
        Get the file name This function assumes that the file name is the same
        for_linked_file all datagrams in the file

        Returns:
            std::string
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file

        Returns:
            std::string
        """

    def deinitialize(self) -> None: ...

    def is_initialized(self) -> bool: ...

    def is_primary_file(self) -> bool: ...

    def is_secondary_file(self) -> bool: ...

    def has_linked_file(self) -> bool: ...

    def configuration_data_interface(self) -> S7KConfigurationDataInterface_stream: ...

    def read_navigation_data(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> tuple[float, float]: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KNavigationDataInterfacePerFile:
    """
    Interface that reads the navigation (position, attitude, heading) of a
    single .s7k file.

    The 7k format stores each navigation quantity in two kinds of records:
    a modern "fused" record (1015 Navigation for position/heading, 1016
    Attitude for roll/pitch/heave/heading) and a legacy single-quantity
    record (1003 Position, 1012 Roll Pitch Heave, 1013 Heading). By
    default the modern records are preferred; the two preferences can be
    toggled with the setters below.

    Template Args:
        t_ifstream:
    """

    def get_prefer_navigation_over_position(self) -> bool:
        """
        Get whether the 1015 Navigation record is preferred over the 1003
        Position record
        Returns:
            true if 1015 Navigation is preferred (default)
        """

    def set_prefer_navigation_over_position(self, prefer: bool) -> None:
        """
        Set whether the 1015 Navigation record is preferred over the 1003
        Position record
        Args:
            prefer: true to prefer 1015 Navigation (default), false to prefer
                    1003 Position
        """

    def get_prefer_attitude_over_rollpitchheave(self) -> bool:
        """
        Get whether the 1016 Attitude record is preferred over the 1012 Roll
        Pitch Heave record
        Returns:
            true if 1016 Attitude is preferred (default)
        """

    def set_prefer_attitude_over_rollpitchheave(self, prefer: bool) -> None:
        """
        Set whether the 1016 Attitude record is preferred over the 1012 Roll
        Pitch Heave record
        Args:
            prefer: true to prefer 1016 Attitude (default), false to prefer
                    1012 Roll Pitch Heave
        """

    def init_from_file(self, index_path: str = '', force: bool = False) -> None: ...

    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file

        Returns:
            size_t
        """

    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file

        Returns:
            size_t
        """

    def get_file_path(self) -> str:
        """
        Get the file name This function assumes that the file name is the same
        for_linked_file all datagrams in the file

        Returns:
            std::string
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file

        Returns:
            std::string
        """

    def deinitialize(self) -> None: ...

    def is_initialized(self) -> bool: ...

    def is_primary_file(self) -> bool: ...

    def is_secondary_file(self) -> bool: ...

    def has_linked_file(self) -> bool: ...

    def configuration_data_interface(self) -> S7KConfigurationDataInterface: ...

    def read_navigation_data(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> tuple[float, float]: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KNavigationDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[S7KNavigationDataInterfacePerFile_stream]) -> list[S7KNavigationDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[S7KNavigationDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> S7KNavigationDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[S7KNavigationDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[S7KNavigationDataInterfacePerFile_stream]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """This functions throws if linked file interfaces are not consistent"""

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str] = {}, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False, mp_cores: int = 1) -> None: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def configuration_data_interface(self) -> S7KConfigurationDataInterface_stream: ...

    def get_navigation_interpolator_keys(self) -> list[int]: ...

    def set_navigation_interpolators(self, navigation_interpolators: Mapping[int, "boost::flyweights::flyweight_themachinethatgoesping_navigation_NavigationInterpolatorLatLon_boost_parameter_void__boost_parameter_void__boost_parameter_void__boost_parameter_void__boost_parameter_void_"]) -> None: ...

    def has_navigation_interpolator(self, sensor_configuration_hash: int) -> bool: ...

    def get_navigation_interpolator(self, sensor_configuration: int) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon: ...

    def set_navigation_interpolator(self, sensor_configuration_hash: int, navigation_interpolator: themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon) -> None: ...

    @overload
    def get_channel_ids(self) -> list[str]: ...

    @overload
    def get_channel_ids(self, sensor_configuration_hash: int) -> list[str]: ...

    def get_navigation_data(self, downsample_interval_sec: float = 1.0, max_gap_sec: float = -1.0) -> dict[str, themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLatLonVector]:
        """
        Get navigation data as a map of GeolocationLatLonVector per channel

        This function extracts navigation data for all available channels at
        regular time intervals. It automatically detects available sensor
        configurations, time ranges, and handles data gaps by not
        interpolating across them.

        Args:
            downsample_interval_sec: Time interval between samples in seconds.
                                     Use 0 or negative to disable downsampling
                                     (use all original timestamps)
            max_gap: Maximum allowed gap in the original data before
                     considering it a data gap. Points that would require
                     interpolating across a gap larger than this are skipped.
                     If <= 0, defaults to 2x downsample_interval (or 10
                     seconds if no downsampling)

        Returns:
            std::unordered_map_std_string_
navigation_datastructures_GeolocationLatLonVector Map from
                channel_id to GeolocationLatLonVector containing timestamps
                and positions
        """

class S7KNavigationDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[S7KNavigationDataInterfacePerFile]) -> list[S7KNavigationDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[S7KNavigationDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> S7KNavigationDataInterfacePerFile: ...

    def per_primary_file(self) -> list[S7KNavigationDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[S7KNavigationDataInterfacePerFile]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """This functions throws if linked file interfaces are not consistent"""

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str] = {}, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False, mp_cores: int = 1) -> None: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def configuration_data_interface(self) -> S7KConfigurationDataInterface: ...

    def get_navigation_interpolator_keys(self) -> list[int]: ...

    def set_navigation_interpolators(self, navigation_interpolators: Mapping[int, "boost::flyweights::flyweight_themachinethatgoesping_navigation_NavigationInterpolatorLatLon_boost_parameter_void__boost_parameter_void__boost_parameter_void__boost_parameter_void__boost_parameter_void_"]) -> None: ...

    def has_navigation_interpolator(self, sensor_configuration_hash: int) -> bool: ...

    def get_navigation_interpolator(self, sensor_configuration: int) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon: ...

    def set_navigation_interpolator(self, sensor_configuration_hash: int, navigation_interpolator: themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon) -> None: ...

    @overload
    def get_channel_ids(self) -> list[str]: ...

    @overload
    def get_channel_ids(self, sensor_configuration_hash: int) -> list[str]: ...

    def get_navigation_data(self, downsample_interval_sec: float = 1.0, max_gap_sec: float = -1.0) -> dict[str, themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLatLonVector]:
        """
        Get navigation data as a map of GeolocationLatLonVector per channel

        This function extracts navigation data for all available channels at
        regular time intervals. It automatically detects available sensor
        configurations, time ranges, and handles data gaps by not
        interpolating across them.

        Args:
            downsample_interval_sec: Time interval between samples in seconds.
                                     Use 0 or negative to disable downsampling
                                     (use all original timestamps)
            max_gap: Maximum allowed gap in the original data before
                     considering it a data gap. Points that would require
                     interpolating across a gap larger than this are skipped.
                     If <= 0, defaults to 2x downsample_interval (or 10
                     seconds if no downsampling)

        Returns:
            std::unordered_map_std_string_
navigation_datastructures_GeolocationLatLonVector Map from
                channel_id to GeolocationLatLonVector containing timestamps
                and positions
        """

class S7KEnvironmentDataInterfacePerFile_stream:
    """
    Interface that reads the environment (sound velocity, CTD, water
    properties) of a single .s7k file.



    $.. note::

    The datagram-processing functions are not implemented yet. The class
    currently only provides the structure so the environment can be filled
    in in a later step.

    Template Args:
        t_ifstream:
    """

    def init_from_file(self, index_path: str = '', force: bool = False) -> None: ...

    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file

        Returns:
            size_t
        """

    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file

        Returns:
            size_t
        """

    def get_file_path(self) -> str:
        """
        Get the file name This function assumes that the file name is the same
        for_linked_file all datagrams in the file

        Returns:
            std::string
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file

        Returns:
            std::string
        """

    def deinitialize(self) -> None: ...

    def is_initialized(self) -> bool: ...

    def is_primary_file(self) -> bool: ...

    def is_secondary_file(self) -> bool: ...

    def has_linked_file(self) -> bool: ...

    def configuration_data_interface(self) -> S7KConfigurationDataInterface_stream: ...

    def navigation_data_interface(self) -> S7KNavigationDataInterface_stream: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KEnvironmentDataInterfacePerFile:
    """
    Interface that reads the environment (sound velocity, CTD, water
    properties) of a single .s7k file.



    $.. note::

    The datagram-processing functions are not implemented yet. The class
    currently only provides the structure so the environment can be filled
    in in a later step.

    Template Args:
        t_ifstream:
    """

    def init_from_file(self, index_path: str = '', force: bool = False) -> None: ...

    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file

        Returns:
            size_t
        """

    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file

        Returns:
            size_t
        """

    def get_file_path(self) -> str:
        """
        Get the file name This function assumes that the file name is the same
        for_linked_file all datagrams in the file

        Returns:
            std::string
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file

        Returns:
            std::string
        """

    def deinitialize(self) -> None: ...

    def is_initialized(self) -> bool: ...

    def is_primary_file(self) -> bool: ...

    def is_secondary_file(self) -> bool: ...

    def has_linked_file(self) -> bool: ...

    def configuration_data_interface(self) -> S7KConfigurationDataInterface: ...

    def navigation_data_interface(self) -> S7KNavigationDataInterface: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KEnvironmentDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[S7KEnvironmentDataInterfacePerFile_stream]) -> list[S7KEnvironmentDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[S7KEnvironmentDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> S7KEnvironmentDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[S7KEnvironmentDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[S7KEnvironmentDataInterfacePerFile_stream]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """This functions throws if linked file interfaces are not consistent"""

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str] = {}, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False, mp_cores: int = 1) -> None: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def configuration_data_interface(self) -> S7KConfigurationDataInterface_stream: ...

    def navigation_data_interface(self) -> S7KNavigationDataInterface_stream: ...

class S7KEnvironmentDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[S7KEnvironmentDataInterfacePerFile]) -> list[S7KEnvironmentDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[S7KEnvironmentDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> S7KEnvironmentDataInterfacePerFile: ...

    def per_primary_file(self) -> list[S7KEnvironmentDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[S7KEnvironmentDataInterfacePerFile]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """This functions throws if linked file interfaces are not consistent"""

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str] = {}, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False, mp_cores: int = 1) -> None: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def configuration_data_interface(self) -> S7KConfigurationDataInterface: ...

    def navigation_data_interface(self) -> S7KNavigationDataInterface: ...

class S7KPingDataInterfacePerFile_stream:
    """
    Interface that reads the pings (bathymetry, water column) of a single
    .s7k file.



    $.. note::

    The datagram-processing function (read_pings) is not implemented yet.
    The class currently only provides the structure so the pings can be
    filled in in a later step.

    Template Args:
        t_ifstream:
    """

    def init_from_file(self, index_path: str = '', force: bool = False) -> None: ...

    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file

        Returns:
            size_t
        """

    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file

        Returns:
            size_t
        """

    def get_file_path(self) -> str:
        """
        Get the file name This function assumes that the file name is the same
        for_linked_file all datagrams in the file

        Returns:
            std::string
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file

        Returns:
            std::string
        """

    def deinitialize(self) -> None: ...

    def is_initialized(self) -> bool: ...

    def is_primary_file(self) -> bool: ...

    def is_secondary_file(self) -> bool: ...

    def has_linked_file(self) -> bool: ...

    def configuration_data_interface(self) -> S7KConfigurationDataInterface_stream: ...

    def configuration_data_interface_for_file(self) -> S7KConfigurationDataInterfacePerFile_stream: ...

    def navigation_data_interface(self) -> S7KNavigationDataInterface_stream: ...

    def environment_data_interface(self) -> S7KEnvironmentDataInterface_stream: ...

    def read_pings(self, index_paths: Mapping[str, str] = {}) -> themachinethatgoesping.echosounders_nanopy.s7k.filedatacontainers.S7KPingContainer_stream: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KPingDataInterfacePerFile:
    """
    Interface that reads the pings (bathymetry, water column) of a single
    .s7k file.



    $.. note::

    The datagram-processing function (read_pings) is not implemented yet.
    The class currently only provides the structure so the pings can be
    filled in in a later step.

    Template Args:
        t_ifstream:
    """

    def init_from_file(self, index_path: str = '', force: bool = False) -> None: ...

    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file

        Returns:
            size_t
        """

    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file

        Returns:
            size_t
        """

    def get_file_path(self) -> str:
        """
        Get the file name This function assumes that the file name is the same
        for_linked_file all datagrams in the file

        Returns:
            std::string
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file

        Returns:
            std::string
        """

    def deinitialize(self) -> None: ...

    def is_initialized(self) -> bool: ...

    def is_primary_file(self) -> bool: ...

    def is_secondary_file(self) -> bool: ...

    def has_linked_file(self) -> bool: ...

    def configuration_data_interface(self) -> S7KConfigurationDataInterface: ...

    def configuration_data_interface_for_file(self) -> S7KConfigurationDataInterfacePerFile: ...

    def navigation_data_interface(self) -> S7KNavigationDataInterface: ...

    def environment_data_interface(self) -> S7KEnvironmentDataInterface: ...

    def read_pings(self, index_paths: Mapping[str, str] = {}) -> themachinethatgoesping.echosounders_nanopy.s7k.filedatacontainers.S7KPingContainer: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KPingDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[S7KPingDataInterfacePerFile_stream]) -> list[S7KPingDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[S7KPingDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> S7KPingDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[S7KPingDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[S7KPingDataInterfacePerFile_stream]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """This functions throws if linked file interfaces are not consistent"""

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str] = {}, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False, mp_cores: int = 1) -> None: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def configuration_data_interface(self) -> S7KConfigurationDataInterface_stream: ...

    def navigation_data_interface(self) -> S7KNavigationDataInterface_stream: ...

    def environment_data_interface(self) -> S7KEnvironmentDataInterface_stream: ...

    def get_channel_ids(self) -> list[str]: ...

    @overload
    def get_pings(self) -> themachinethatgoesping.echosounders_nanopy.s7k.filedatacontainers.S7KPingContainer_stream: ...

    @overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_nanopy.s7k.filedatacontainers.S7KPingContainer_stream: ...

class S7KPingDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[S7KPingDataInterfacePerFile]) -> list[S7KPingDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[S7KPingDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> S7KPingDataInterfacePerFile: ...

    def per_primary_file(self) -> list[S7KPingDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[S7KPingDataInterfacePerFile]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """This functions throws if linked file interfaces are not consistent"""

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def is_initialized(self) -> bool: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def deinitialize(self) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str] = {}, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_from_file(self, index_paths: Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False, mp_cores: int = 1) -> None: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def configuration_data_interface(self) -> S7KConfigurationDataInterface: ...

    def navigation_data_interface(self) -> S7KNavigationDataInterface: ...

    def environment_data_interface(self) -> S7KEnvironmentDataInterface: ...

    def get_channel_ids(self) -> list[str]: ...

    @overload
    def get_pings(self) -> themachinethatgoesping.echosounders_nanopy.s7k.filedatacontainers.S7KPingContainer: ...

    @overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_nanopy.s7k.filedatacontainers.S7KPingContainer: ...
