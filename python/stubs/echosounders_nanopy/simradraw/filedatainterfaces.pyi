"""SimradRaw EK60 and EK80 file data interface classes"""
import typing

from collections.abc import Mapping, Sequence
from typing import overload

import themachinethatgoesping.echosounders_nanopy.simradraw
import themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams
import themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers
import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.navigation_nanopy.datastructures
import themachinethatgoesping.tools_nanopy.progressbars


class SimradRawDatagramInterface_stream:
    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawDatagramInterface:
    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawDatagramDataInterface_stream:
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
    def sort_by_time(fileinterfaces: Sequence[SimradRawDatagramDataInterfacePerFile_stream]) -> list[SimradRawDatagramDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[SimradRawDatagramDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> SimradRawDatagramDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[SimradRawDatagramDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[SimradRawDatagramDataInterfacePerFile_stream]:
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

class SimradRawDatagramDataInterface:
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
    def sort_by_time(fileinterfaces: Sequence[SimradRawDatagramDataInterfacePerFile]) -> list[SimradRawDatagramDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[SimradRawDatagramDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> SimradRawDatagramDataInterfacePerFile: ...

    def per_primary_file(self) -> list[SimradRawDatagramDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[SimradRawDatagramDataInterfacePerFile]:
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

class SimradRawDatagramDataInterfacePerFile_stream:
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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawDatagramDataInterfacePerFile:
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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawConfigurationDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[SimradRawConfigurationDataInterfacePerFile_stream]) -> list[SimradRawConfigurationDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[SimradRawConfigurationDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> SimradRawConfigurationDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[SimradRawConfigurationDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[SimradRawConfigurationDataInterfacePerFile_stream]:
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

class SimradRawConfigurationDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[SimradRawConfigurationDataInterfacePerFile]) -> list[SimradRawConfigurationDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[SimradRawConfigurationDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> SimradRawConfigurationDataInterfacePerFile: ...

    def per_primary_file(self) -> list[SimradRawConfigurationDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[SimradRawConfigurationDataInterfacePerFile]:
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

class SimradRawConfigurationDataInterfacePerFile_stream:
    def get_configuration_datagram(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration: ...

    def get_position_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all position sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector_XML_Configuration_Sensor
        """

    def get_depth_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all depth sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector_XML_Configuration_Sensor
        """

    def get_attitude_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all attitude sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector_XML_Configuration_Sensor
        """

    def get_heading_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all heading sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector_XML_Configuration_Sensor
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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawConfigurationDataInterfacePerFile:
    def get_configuration_datagram(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration: ...

    def get_position_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all position sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector_XML_Configuration_Sensor
        """

    def get_depth_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all depth sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector_XML_Configuration_Sensor
        """

    def get_attitude_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all attitude sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector_XML_Configuration_Sensor
        """

    def get_heading_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all heading sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector_XML_Configuration_Sensor
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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawNavigationDataInterface_stream:
    def set_min_gga_quality(self, min_gga_quality: int) -> None: ...

    def set_max_gga_quality(self, max_gga_quality: int) -> None: ...

    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[SimradRawNavigationDataInterfacePerFile_stream]) -> list[SimradRawNavigationDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[SimradRawNavigationDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> SimradRawNavigationDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[SimradRawNavigationDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[SimradRawNavigationDataInterfacePerFile_stream]:
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

    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_stream: ...

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

class SimradRawNavigationDataInterface:
    def set_min_gga_quality(self, min_gga_quality: int) -> None: ...

    def set_max_gga_quality(self, max_gga_quality: int) -> None: ...

    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[SimradRawNavigationDataInterfacePerFile]) -> list[SimradRawNavigationDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[SimradRawNavigationDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> SimradRawNavigationDataInterfacePerFile: ...

    def per_primary_file(self) -> list[SimradRawNavigationDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[SimradRawNavigationDataInterfacePerFile]:
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

    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface: ...

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

class SimradRawNavigationDataInterfacePerFile_stream:
    def set_min_gga_quality(self, min_gga_quality: int) -> None: ...

    def set_max_gga_quality(self, max_gga_quality: int) -> None: ...

    def get_min_gga_quality(self) -> int: ...

    def get_max_gga_quality(self) -> int: ...

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

    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_stream: ...

    def read_navigation_data(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> tuple[float, float]: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawNavigationDataInterfacePerFile:
    def set_min_gga_quality(self, min_gga_quality: int) -> None: ...

    def set_max_gga_quality(self, max_gga_quality: int) -> None: ...

    def get_min_gga_quality(self) -> int: ...

    def get_max_gga_quality(self) -> int: ...

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

    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface: ...

    def read_navigation_data(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> tuple[float, float]: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawEnvironmentDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[SimradRawEnvironmentDataInterfacePerFile_stream]) -> list[SimradRawEnvironmentDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[SimradRawEnvironmentDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> SimradRawEnvironmentDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[SimradRawEnvironmentDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[SimradRawEnvironmentDataInterfacePerFile_stream]:
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

    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_stream: ...

    def navigation_data_interface(self) -> SimradRawNavigationDataInterface_stream: ...

class SimradRawEnvironmentDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[SimradRawEnvironmentDataInterfacePerFile]) -> list[SimradRawEnvironmentDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[SimradRawEnvironmentDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> SimradRawEnvironmentDataInterfacePerFile: ...

    def per_primary_file(self) -> list[SimradRawEnvironmentDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[SimradRawEnvironmentDataInterfacePerFile]:
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

    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface: ...

    def navigation_data_interface(self) -> SimradRawNavigationDataInterface: ...

class SimradRawEnvironmentDataInterfacePerFile_stream:
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

    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_stream: ...

    def navigation_data_interface(self) -> SimradRawNavigationDataInterface_stream: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawEnvironmentDataInterfacePerFile:
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

    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface: ...

    def navigation_data_interface(self) -> SimradRawNavigationDataInterface: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawPingDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[SimradRawPingDataInterfacePerFile_stream]) -> list[SimradRawPingDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[SimradRawPingDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> SimradRawPingDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[SimradRawPingDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[SimradRawPingDataInterfacePerFile_stream]:
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

    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_stream: ...

    def navigation_data_interface(self) -> SimradRawNavigationDataInterface_stream: ...

    def environment_data_interface(self) -> SimradRawEnvironmentDataInterface_stream: ...

    def get_channel_ids(self) -> list[str]: ...

    @overload
    def get_pings(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers.SimradRawPingContainer_stream: ...

    @overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers.SimradRawPingContainer_stream: ...

class SimradRawPingDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[SimradRawPingDataInterfacePerFile]) -> list[SimradRawPingDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[SimradRawPingDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> SimradRawPingDataInterfacePerFile: ...

    def per_primary_file(self) -> list[SimradRawPingDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[SimradRawPingDataInterfacePerFile]:
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

    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface: ...

    def navigation_data_interface(self) -> SimradRawNavigationDataInterface: ...

    def environment_data_interface(self) -> SimradRawEnvironmentDataInterface: ...

    def get_channel_ids(self) -> list[str]: ...

    @overload
    def get_pings(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers.SimradRawPingContainer: ...

    @overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers.SimradRawPingContainer: ...

class SimradRawPingDataInterfacePerFile_stream:
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

    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_stream: ...

    def configuration_data_interface_for_file(self) -> SimradRawConfigurationDataInterfacePerFile_stream: ...

    def navigation_data_interface(self) -> SimradRawNavigationDataInterface_stream: ...

    def environment_data_interface(self) -> SimradRawEnvironmentDataInterface_stream: ...

    def read_pings(self, index_paths: Mapping[str, str] = {}) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers.SimradRawPingContainer_stream: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawPingDataInterfacePerFile:
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

    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface: ...

    def configuration_data_interface_for_file(self) -> SimradRawConfigurationDataInterfacePerFile: ...

    def navigation_data_interface(self) -> SimradRawNavigationDataInterface: ...

    def environment_data_interface(self) -> SimradRawEnvironmentDataInterface: ...

    def read_pings(self, index_paths: Mapping[str, str] = {}) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers.SimradRawPingContainer: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawOtherFileDataInterface_stream:
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
    def sort_by_time(fileinterfaces: Sequence[SimradRawOtherFileDataInterfacePerFile_stream]) -> list[SimradRawOtherFileDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[SimradRawOtherFileDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> SimradRawOtherFileDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[SimradRawOtherFileDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[SimradRawOtherFileDataInterfacePerFile_stream]:
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

class SimradRawOtherFileDataInterface:
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
    def sort_by_time(fileinterfaces: Sequence[SimradRawOtherFileDataInterfacePerFile]) -> list[SimradRawOtherFileDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[SimradRawOtherFileDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> SimradRawOtherFileDataInterfacePerFile: ...

    def per_primary_file(self) -> list[SimradRawOtherFileDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[SimradRawOtherFileDataInterfacePerFile]:
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

class SimradRawOtherFileDataInterfacePerFile_stream:
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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawOtherFileDataInterfacePerFile:
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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[SimradRawDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
