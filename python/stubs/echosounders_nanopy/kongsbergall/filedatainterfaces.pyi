"""KongsbergAll (kongsberg .all/.wcd) file data interface classes"""
import typing

from collections.abc import Mapping, Sequence
from typing import overload

import themachinethatgoesping.echosounders_nanopy
import themachinethatgoesping.echosounders_nanopy.kongsbergall
import themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams
import themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers
import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.navigation_nanopy.datastructures
import themachinethatgoesping.tools_nanopy.progressbars


class KongsbergAllDatagramInterface_stream:
    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllDatagramInterface:
    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllDatagramDataInterface_stream:
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
    def sort_by_time(fileinterfaces: Sequence[KongsbergAllDatagramDataInterfacePerFile_stream]) -> list[KongsbergAllDatagramDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[KongsbergAllDatagramDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KongsbergAllDatagramDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[KongsbergAllDatagramDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KongsbergAllDatagramDataInterfacePerFile_stream]:
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

class KongsbergAllDatagramDataInterface:
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
    def sort_by_time(fileinterfaces: Sequence[KongsbergAllDatagramDataInterfacePerFile]) -> list[KongsbergAllDatagramDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[KongsbergAllDatagramDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KongsbergAllDatagramDataInterfacePerFile: ...

    def per_primary_file(self) -> list[KongsbergAllDatagramDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KongsbergAllDatagramDataInterfacePerFile]:
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

class KongsbergAllDatagramDataInterfacePerFile_stream:
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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllDatagramDataInterfacePerFile:
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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllConfigurationDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KongsbergAllConfigurationDataInterfacePerFile_stream]) -> list[KongsbergAllConfigurationDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[KongsbergAllConfigurationDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KongsbergAllConfigurationDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[KongsbergAllConfigurationDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KongsbergAllConfigurationDataInterfacePerFile_stream]:
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

class KongsbergAllConfigurationDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KongsbergAllConfigurationDataInterfacePerFile]) -> list[KongsbergAllConfigurationDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[KongsbergAllConfigurationDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KongsbergAllConfigurationDataInterfacePerFile: ...

    def per_primary_file(self) -> list[KongsbergAllConfigurationDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KongsbergAllConfigurationDataInterfacePerFile]:
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

class KongsbergAllConfigurationDataInterfacePerFile_stream:
    def read_installation_parameters(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters:
        """
        Read the installation parameters from the file, this function also
        checks if the start and end parameters are the same

        Returns:
            datagrams::InstallationParameters
        """

    def init_runtime_parameters(self) -> None:
        """
        read the runtime parameters from the file and save them in the
        internal map This function is automatically called by
        get_runtime_parameters
        """

    def get_runtime_parameters(self, system_serial_number: int, ping_counter: int, ping_time: float, last_index: int = 0) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters: ...

    def get_active_position_system_number(self) -> int: ...

    def get_active_pitch_roll_sensor(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor: ...

    def get_active_heave_sensor(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor: ...

    def get_active_heading_sensor(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor: ...

    def set_active_position_system_number(self, number: int) -> None:
        """
        Set the active position system number
        0: this will be overwritten by "read_sensor_configuration" /
           "init_interface"
        1-3: position system 1-3

        Args:
            number:
        """

    def set_active_pitch_roll_sensor(self, sensor: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> None:
        """
        Set the active roll pitch sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        o_KongsbergAllActiveSensor

        Args:
            sensor:
        """

    def set_active_heave_sensor(self, sensor: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> None:
        """
        Set the active heave sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        o_KongsbergAllActiveSensor

        Args:
            sensor:
        """

    def set_active_heading_sensor(self, sensor: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> None:
        """
        Set the active heading sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        o_KongsbergAllActiveSensor

        Args:
            sensor:
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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllConfigurationDataInterfacePerFile:
    def read_installation_parameters(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters:
        """
        Read the installation parameters from the file, this function also
        checks if the start and end parameters are the same

        Returns:
            datagrams::InstallationParameters
        """

    def init_runtime_parameters(self) -> None:
        """
        read the runtime parameters from the file and save them in the
        internal map This function is automatically called by
        get_runtime_parameters
        """

    def get_runtime_parameters(self, system_serial_number: int, ping_counter: int, ping_time: float, last_index: int = 0) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters: ...

    def get_active_position_system_number(self) -> int: ...

    def get_active_pitch_roll_sensor(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor: ...

    def get_active_heave_sensor(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor: ...

    def get_active_heading_sensor(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor: ...

    def set_active_position_system_number(self, number: int) -> None:
        """
        Set the active position system number
        0: this will be overwritten by "read_sensor_configuration" /
           "init_interface"
        1-3: position system 1-3

        Args:
            number:
        """

    def set_active_pitch_roll_sensor(self, sensor: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> None:
        """
        Set the active roll pitch sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        o_KongsbergAllActiveSensor

        Args:
            sensor:
        """

    def set_active_heave_sensor(self, sensor: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> None:
        """
        Set the active heave sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        o_KongsbergAllActiveSensor

        Args:
            sensor:
        """

    def set_active_heading_sensor(self, sensor: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> None:
        """
        Set the active heading sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        o_KongsbergAllActiveSensor

        Args:
            sensor:
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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllNavigationDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KongsbergAllNavigationDataInterfacePerFile_stream]) -> list[KongsbergAllNavigationDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[KongsbergAllNavigationDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KongsbergAllNavigationDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[KongsbergAllNavigationDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KongsbergAllNavigationDataInterfacePerFile_stream]:
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

    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_stream: ...

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

class KongsbergAllNavigationDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KongsbergAllNavigationDataInterfacePerFile]) -> list[KongsbergAllNavigationDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[KongsbergAllNavigationDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KongsbergAllNavigationDataInterfacePerFile: ...

    def per_primary_file(self) -> list[KongsbergAllNavigationDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KongsbergAllNavigationDataInterfacePerFile]:
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

    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface: ...

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

class KongsbergAllNavigationDataInterfacePerFile_stream:
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

    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_stream: ...

    def read_navigation_data(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> tuple[float, float]: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllNavigationDataInterfacePerFile:
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

    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface: ...

    def read_navigation_data(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> tuple[float, float]: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllEnvironmentDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KongsbergAllEnvironmentDataInterfacePerFile_stream]) -> list[KongsbergAllEnvironmentDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[KongsbergAllEnvironmentDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KongsbergAllEnvironmentDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[KongsbergAllEnvironmentDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KongsbergAllEnvironmentDataInterfacePerFile_stream]:
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

    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_stream: ...

    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface_stream: ...

class KongsbergAllEnvironmentDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KongsbergAllEnvironmentDataInterfacePerFile]) -> list[KongsbergAllEnvironmentDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[KongsbergAllEnvironmentDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KongsbergAllEnvironmentDataInterfacePerFile: ...

    def per_primary_file(self) -> list[KongsbergAllEnvironmentDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KongsbergAllEnvironmentDataInterfacePerFile]:
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

    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface: ...

    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface: ...

class KongsbergAllEnvironmentDataInterfacePerFile_stream:
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

    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_stream: ...

    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface_stream: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllEnvironmentDataInterfacePerFile:
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

    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface: ...

    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllOtherFileDataInterface_stream:
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
    def sort_by_time(fileinterfaces: Sequence[KongsbergAllOtherFileDataInterfacePerFile_stream]) -> list[KongsbergAllOtherFileDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[KongsbergAllOtherFileDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KongsbergAllOtherFileDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[KongsbergAllOtherFileDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KongsbergAllOtherFileDataInterfacePerFile_stream]:
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

class KongsbergAllOtherFileDataInterface:
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
    def sort_by_time(fileinterfaces: Sequence[KongsbergAllOtherFileDataInterfacePerFile]) -> list[KongsbergAllOtherFileDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[KongsbergAllOtherFileDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KongsbergAllOtherFileDataInterfacePerFile: ...

    def per_primary_file(self) -> list[KongsbergAllOtherFileDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KongsbergAllOtherFileDataInterfacePerFile]:
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

class KongsbergAllOtherFileDataInterfacePerFile_stream:
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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllOtherFileDataInterfacePerFile:
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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllPingDataInterface_stream:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KongsbergAllPingDataInterfacePerFile_stream]) -> list[KongsbergAllPingDataInterfacePerFile_stream]: ...

    @overload
    def per_file(self) -> list[KongsbergAllPingDataInterfacePerFile_stream]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KongsbergAllPingDataInterfacePerFile_stream: ...

    def per_primary_file(self) -> list[KongsbergAllPingDataInterfacePerFile_stream]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KongsbergAllPingDataInterfacePerFile_stream]:
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

    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_stream: ...

    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface_stream: ...

    def environment_data_interface(self) -> KongsbergAllEnvironmentDataInterface_stream: ...

    def get_channel_ids(self) -> list[str]: ...

    @overload
    def get_pings(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer_stream: ...

    @overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer_stream: ...

class KongsbergAllPingDataInterface:
    @staticmethod
    def sort_by_time(fileinterfaces: Sequence[KongsbergAllPingDataInterfacePerFile]) -> list[KongsbergAllPingDataInterfacePerFile]: ...

    @overload
    def per_file(self) -> list[KongsbergAllPingDataInterfacePerFile]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    @overload
    def per_file(self, file_nr: int) -> KongsbergAllPingDataInterfacePerFile: ...

    def per_primary_file(self) -> list[KongsbergAllPingDataInterfacePerFile]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector_t_filedatainterface_perfile&
        """

    def per_secondary_file(self) -> list[KongsbergAllPingDataInterfacePerFile]:
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

    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface: ...

    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface: ...

    def environment_data_interface(self) -> KongsbergAllEnvironmentDataInterface: ...

    def get_channel_ids(self) -> list[str]: ...

    @overload
    def get_pings(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer: ...

    @overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer: ...

class KongsbergAllPingDataInterfacePerFile_stream:
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

    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_stream: ...

    def configuration_data_interface_for_file(self) -> KongsbergAllConfigurationDataInterfacePerFile_stream: ...

    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface_stream: ...

    def environment_data_interface(self) -> KongsbergAllEnvironmentDataInterface_stream: ...

    def read_pings(self, index_paths: Mapping[str, str] = {}) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer_stream: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllPingDataInterfacePerFile:
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

    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface: ...

    def configuration_data_interface_for_file(self) -> KongsbergAllConfigurationDataInterfacePerFile: ...

    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface: ...

    def environment_data_interface(self) -> KongsbergAllEnvironmentDataInterface: ...

    def read_pings(self, index_paths: Mapping[str, str] = {}) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[KongsbergAllDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
