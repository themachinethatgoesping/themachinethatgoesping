"""KMALL (kongsberg .kmall/.kmwcd) file data interface classes"""
import typing

from collections.abc import Mapping, Sequence
from typing import overload

import themachinethatgoesping.echosounders_nanopy.kmall
import themachinethatgoesping.echosounders_nanopy.kmall.datagrams
import themachinethatgoesping.echosounders_nanopy.kmall.filedatacontainers
import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.navigation_nanopy.datastructures
import themachinethatgoesping.tools_nanopy.progressbars


class KMALLDatagramInterface_stream:
    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLDatagramInterface:
    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLDatagramDataInterfacePerFile_stream:
    """
    FileDataInterface (for single files) for packages that fit neither of
    the other FileDataInterfaces (Configuration, Navigation, Environment,
    Ping)

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file

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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLDatagramDataInterfacePerFile:
    """
    FileDataInterface (for single files) for packages that fit neither of
    the other FileDataInterfaces (Configuration, Navigation, Environment,
    Ping)

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file

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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLDatagramDataInterface_stream:
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Environment, Ping)

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file

    Template Args:
        t_ifstream:
    """

    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KMALLDatagramDataInterfacePerFile_stream]) -> list[KMALLDatagramDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[KMALLDatagramDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KMALLDatagramDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[KMALLDatagramDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KMALLDatagramDataInterfacePerFile_stream]:
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

class KMALLDatagramDataInterface:
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Environment, Ping)

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file

    Template Args:
        t_ifstream:
    """

    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KMALLDatagramDataInterfacePerFile]) -> list[KMALLDatagramDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[KMALLDatagramDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KMALLDatagramDataInterfacePerFile: ...

    def per_primary_file(self) -> list[KMALLDatagramDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KMALLDatagramDataInterfacePerFile]:
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

class KMALLOtherFileDataInterfacePerFile_stream:
    """
    FileDataInterface (for single files) for packages that fit neither of
    the other FileDataInterfaces (Configuration, Navigation, Environment,
    Ping)

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file

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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLOtherFileDataInterfacePerFile:
    """
    FileDataInterface (for single files) for packages that fit neither of
    the other FileDataInterfaces (Configuration, Navigation, Environment,
    Ping)

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file

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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLOtherFileDataInterface_stream:
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Environment, Ping)

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file

    Template Args:
        t_ifstream:
    """

    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KMALLOtherFileDataInterfacePerFile_stream]) -> list[KMALLOtherFileDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[KMALLOtherFileDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KMALLOtherFileDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[KMALLOtherFileDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KMALLOtherFileDataInterfacePerFile_stream]:
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

class KMALLOtherFileDataInterface:
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Environment, Ping)

    No datagram caching is implemented for this interface. Accessed
    packages are always read from file

    Template Args:
        t_ifstream:
    """

    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KMALLOtherFileDataInterfacePerFile]) -> list[KMALLOtherFileDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[KMALLOtherFileDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KMALLOtherFileDataInterfacePerFile: ...

    def per_primary_file(self) -> list[KMALLOtherFileDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KMALLOtherFileDataInterfacePerFile]:
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

class KMALLConfigurationDataInterfacePerFile_stream:
    def read_installation_parameters(self) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IInstallationParam:
        """
        Read the installation parameters from the file

        Returns:
            datagrams::IInstallationParam
        """

    def init_runtime_parameters(self) -> None:
        """
        Read the runtime parameters from the file and save them in the
        internal map This function is automatically called by
        get_runtime_parameters
        """

    def get_runtime_parameters(self, system_serial_number: int, ping_counter: int, ping_time: float, last_index: int = 0) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IOpRuntime:
        """
        Get the runtime parameters for a specific ping

        This function searches for the runtime parameters that were active at
        the given ping time. It uses last_index as an optimization to avoid
        searching from the beginning each time.

        Args:
            system_serial_number: The PU serial number to search for
            ping_time: The timestamp of the ping
            last_index: Shared pointer to the last index used for optimization
                        (will be updated)

        Returns:
            boost::flyweight_datagrams_IOpRuntime The runtime parameters for
                  the ping
        """

    def get_transducer_id(self) -> str: ...

    def get_active_position_system_number(self) -> int: ...

    def get_active_attitude_sensor_number(self) -> int: ...

    def set_active_position_system_number(self, number: int) -> None:
        """
        Set the active position system number
        0: this will be overwritten by "read_sensor_configuration" /
           "init_interface"
        1-4: position system 1-4

        Args:
            number:
        """

    def set_active_attitude_sensor_number(self, number: int) -> None:
        """
        Set the active attitude sensor number
        0: this will be overwritten by "read_sensor_configuration" /
           "init_interface"
        1-4: attitude sensor 1-4

        Args:
            number:
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

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLConfigurationDataInterfacePerFile:
    def read_installation_parameters(self) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IInstallationParam:
        """
        Read the installation parameters from the file

        Returns:
            datagrams::IInstallationParam
        """

    def init_runtime_parameters(self) -> None:
        """
        Read the runtime parameters from the file and save them in the
        internal map This function is automatically called by
        get_runtime_parameters
        """

    def get_runtime_parameters(self, system_serial_number: int, ping_counter: int, ping_time: float, last_index: int = 0) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IOpRuntime:
        """
        Get the runtime parameters for a specific ping

        This function searches for the runtime parameters that were active at
        the given ping time. It uses last_index as an optimization to avoid
        searching from the beginning each time.

        Args:
            system_serial_number: The PU serial number to search for
            ping_time: The timestamp of the ping
            last_index: Shared pointer to the last index used for optimization
                        (will be updated)

        Returns:
            boost::flyweight_datagrams_IOpRuntime The runtime parameters for
                  the ping
        """

    def get_transducer_id(self) -> str: ...

    def get_active_position_system_number(self) -> int: ...

    def get_active_attitude_sensor_number(self) -> int: ...

    def set_active_position_system_number(self, number: int) -> None:
        """
        Set the active position system number
        0: this will be overwritten by "read_sensor_configuration" /
           "init_interface"
        1-4: position system 1-4

        Args:
            number:
        """

    def set_active_attitude_sensor_number(self, number: int) -> None:
        """
        Set the active attitude sensor number
        0: this will be overwritten by "read_sensor_configuration" /
           "init_interface"
        1-4: attitude sensor 1-4

        Args:
            number:
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

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLConfigurationDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KMALLConfigurationDataInterfacePerFile_stream]) -> list[KMALLConfigurationDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[KMALLConfigurationDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KMALLConfigurationDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[KMALLConfigurationDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KMALLConfigurationDataInterfacePerFile_stream]:
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

class KMALLConfigurationDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KMALLConfigurationDataInterfacePerFile]) -> list[KMALLConfigurationDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[KMALLConfigurationDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KMALLConfigurationDataInterfacePerFile: ...

    def per_primary_file(self) -> list[KMALLConfigurationDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KMALLConfigurationDataInterfacePerFile]:
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

class KMALLEnvironmentDataInterfacePerFile_stream:
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

    def configuration_data_interface(self) -> KMALLConfigurationDataInterface_stream: ...

    def navigation_data_interface(self) -> KMALLNavigationDataInterface_stream: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLEnvironmentDataInterfacePerFile:
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

    def configuration_data_interface(self) -> KMALLConfigurationDataInterface: ...

    def navigation_data_interface(self) -> KMALLNavigationDataInterface: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLEnvironmentDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KMALLEnvironmentDataInterfacePerFile_stream]) -> list[KMALLEnvironmentDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[KMALLEnvironmentDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KMALLEnvironmentDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[KMALLEnvironmentDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KMALLEnvironmentDataInterfacePerFile_stream]:
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

    def configuration_data_interface(self) -> KMALLConfigurationDataInterface_stream: ...

    def navigation_data_interface(self) -> KMALLNavigationDataInterface_stream: ...

class KMALLEnvironmentDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KMALLEnvironmentDataInterfacePerFile]) -> list[KMALLEnvironmentDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[KMALLEnvironmentDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KMALLEnvironmentDataInterfacePerFile: ...

    def per_primary_file(self) -> list[KMALLEnvironmentDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KMALLEnvironmentDataInterfacePerFile]:
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

    def configuration_data_interface(self) -> KMALLConfigurationDataInterface: ...

    def navigation_data_interface(self) -> KMALLNavigationDataInterface: ...

class KMALLNavigationDataInterfacePerFile_stream:
    def get_prefer_spo_over_cpo(self) -> bool:
        """
        Get whether S_POSITION is preferred over C_POSITION
        Returns:
            true if S_POSITION is preferred (default)
        """

    def set_prefer_spo_over_cpo(self, prefer: bool) -> None:
        """
        Set whether S_POSITION is preferred over C_POSITION
        Args:
            prefer: true to prefer S_POSITION (default), false to prefer
                    C_POSITION
        """

    def get_prefer_skm_over_che(self) -> bool:
        """
        Get whether S_KM_BINARY is preferred over C_HEAVE for heave data
        Returns:
            true if S_KM_BINARY is preferred (default)
        """

    def set_prefer_skm_over_che(self, prefer: bool) -> None:
        """
        Set whether S_KM_BINARY is preferred over C_HEAVE for heave data
        Args:
            prefer: true to prefer S_KM_BINARY (default), false to prefer
                    C_HEAVE
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

    def configuration_data_interface(self) -> KMALLConfigurationDataInterface_stream: ...

    def read_navigation_data(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> tuple[float, float]: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLNavigationDataInterfacePerFile:
    def get_prefer_spo_over_cpo(self) -> bool:
        """
        Get whether S_POSITION is preferred over C_POSITION
        Returns:
            true if S_POSITION is preferred (default)
        """

    def set_prefer_spo_over_cpo(self, prefer: bool) -> None:
        """
        Set whether S_POSITION is preferred over C_POSITION
        Args:
            prefer: true to prefer S_POSITION (default), false to prefer
                    C_POSITION
        """

    def get_prefer_skm_over_che(self) -> bool:
        """
        Get whether S_KM_BINARY is preferred over C_HEAVE for heave data
        Returns:
            true if S_KM_BINARY is preferred (default)
        """

    def set_prefer_skm_over_che(self, prefer: bool) -> None:
        """
        Set whether S_KM_BINARY is preferred over C_HEAVE for heave data
        Args:
            prefer: true to prefer S_KM_BINARY (default), false to prefer
                    C_HEAVE
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

    def configuration_data_interface(self) -> KMALLConfigurationDataInterface: ...

    def read_navigation_data(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> tuple[float, float]: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLNavigationDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KMALLNavigationDataInterfacePerFile_stream]) -> list[KMALLNavigationDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[KMALLNavigationDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KMALLNavigationDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[KMALLNavigationDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KMALLNavigationDataInterfacePerFile_stream]:
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

    def configuration_data_interface(self) -> KMALLConfigurationDataInterface_stream: ...

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

class KMALLNavigationDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KMALLNavigationDataInterfacePerFile]) -> list[KMALLNavigationDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[KMALLNavigationDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KMALLNavigationDataInterfacePerFile: ...

    def per_primary_file(self) -> list[KMALLNavigationDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KMALLNavigationDataInterfacePerFile]:
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

    def configuration_data_interface(self) -> KMALLConfigurationDataInterface: ...

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

class KMALLPingDataInterfacePerFile_stream:
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

    def configuration_data_interface(self) -> KMALLConfigurationDataInterface_stream: ...

    def configuration_data_interface_for_file(self) -> KMALLConfigurationDataInterfacePerFile_stream: ...

    def navigation_data_interface(self) -> KMALLNavigationDataInterface_stream: ...

    def environment_data_interface(self) -> KMALLEnvironmentDataInterface_stream: ...

    def read_pings(self, index_paths: Mapping[str, str] = {}) -> themachinethatgoesping.echosounders_nanopy.kmall.filedatacontainers.KMALLPingContainer_stream: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLPingDataInterfacePerFile:
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

    def configuration_data_interface(self) -> KMALLConfigurationDataInterface: ...

    def configuration_data_interface_for_file(self) -> KMALLConfigurationDataInterfacePerFile: ...

    def navigation_data_interface(self) -> KMALLNavigationDataInterface: ...

    def environment_data_interface(self) -> KMALLEnvironmentDataInterface: ...

    def read_pings(self, index_paths: Mapping[str, str] = {}) -> themachinethatgoesping.echosounders_nanopy.kmall.filedatacontainers.KMALLPingContainer: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KMALLDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLPingDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KMALLPingDataInterfacePerFile_stream]) -> list[KMALLPingDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[KMALLPingDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KMALLPingDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[KMALLPingDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KMALLPingDataInterfacePerFile_stream]:
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

    def configuration_data_interface(self) -> KMALLConfigurationDataInterface_stream: ...

    def navigation_data_interface(self) -> KMALLNavigationDataInterface_stream: ...

    def environment_data_interface(self) -> KMALLEnvironmentDataInterface_stream: ...

    def get_channel_ids(self) -> list[str]: ...

    @overload
    def get_pings(self) -> themachinethatgoesping.echosounders_nanopy.kmall.filedatacontainers.KMALLPingContainer_stream: ...

    @overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_nanopy.kmall.filedatacontainers.KMALLPingContainer_stream: ...

class KMALLPingDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KMALLPingDataInterfacePerFile]) -> list[KMALLPingDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[KMALLPingDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KMALLPingDataInterfacePerFile: ...

    def per_primary_file(self) -> list[KMALLPingDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KMALLPingDataInterfacePerFile]:
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

    def configuration_data_interface(self) -> KMALLConfigurationDataInterface: ...

    def navigation_data_interface(self) -> KMALLNavigationDataInterface: ...

    def environment_data_interface(self) -> KMALLEnvironmentDataInterface: ...

    def get_channel_ids(self) -> list[str]: ...

    @overload
    def get_pings(self) -> themachinethatgoesping.echosounders_nanopy.kmall.filedatacontainers.KMALLPingContainer: ...

    @overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_nanopy.kmall.filedatacontainers.KMALLPingContainer: ...
