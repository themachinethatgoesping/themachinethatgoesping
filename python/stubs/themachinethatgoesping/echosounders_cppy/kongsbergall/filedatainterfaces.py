"""
KongsbergAll (kongsberg .all/.wcd) file data interface classes
"""
from __future__ import annotations
import themachinethatgoesping.echosounders_cppy.kongsbergall
import themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams
import themachinethatgoesping.echosounders_cppy.kongsbergall.filedatacontainers
import themachinethatgoesping.navigation
import themachinethatgoesping.navigation.datastructures
import themachinethatgoesping.tools_cppy.progressbars
import typing
__all__ = ['KongsbergAllAnnotationDataInterface', 'KongsbergAllAnnotationDataInterfacePerFile', 'KongsbergAllAnnotationDataInterfacePerFile_mapped', 'KongsbergAllAnnotationDataInterface_mapped', 'KongsbergAllConfigurationDataInterface', 'KongsbergAllConfigurationDataInterfacePerFile', 'KongsbergAllConfigurationDataInterfacePerFile_mapped', 'KongsbergAllConfigurationDataInterface_mapped', 'KongsbergAllDatagramDataInterface', 'KongsbergAllDatagramDataInterfacePerFile', 'KongsbergAllDatagramDataInterfacePerFile_mapped', 'KongsbergAllDatagramDataInterface_mapped', 'KongsbergAllDatagramInterface', 'KongsbergAllDatagramInterface_mapped', 'KongsbergAllEnvironmentDataInterface', 'KongsbergAllEnvironmentDataInterfacePerFile', 'KongsbergAllEnvironmentDataInterfacePerFile_mapped', 'KongsbergAllEnvironmentDataInterface_mapped', 'KongsbergAllNavigationDataInterface', 'KongsbergAllNavigationDataInterfacePerFile', 'KongsbergAllNavigationDataInterfacePerFile_mapped', 'KongsbergAllNavigationDataInterface_mapped', 'KongsbergAllOtherFileDataInterface', 'KongsbergAllOtherFileDataInterfacePerFile', 'KongsbergAllOtherFileDataInterfacePerFile_mapped', 'KongsbergAllOtherFileDataInterface_mapped', 'KongsbergAllPingDataInterface', 'KongsbergAllPingDataInterfacePerFile', 'KongsbergAllPingDataInterfacePerFile_mapped', 'KongsbergAllPingDataInterface_mapped']
class KongsbergAllAnnotationDataInterface:
    """
    Interface to read annotation data (no kongsberg datagram is currently
    supported) from a file (multiple files)
    
    Only sorts the supported datagrams. No caching is done. Gives access
    to AnnotationDataInterfacePerFile using the per_file function.
    
    Template parameter ``t_ifstream``:
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[..., ...]) -> list[..., ...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def per_file(self) -> list[..., ...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[..., ...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[..., ...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllAnnotationDataInterfacePerFile:
    """
    Interface to read annotation data (no kongsberg datagram is currently
    supported) from a file (per file)
    
    This class can be accessed using the per_file function of the
    AnnotationDataInterface.
    
    Template parameter ``t_ifstream``:
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class KongsbergAllAnnotationDataInterfacePerFile_mapped:
    """
    Interface to read annotation data (no kongsberg datagram is currently
    supported) from a file (per file)
    
    This class can be accessed using the per_file function of the
    AnnotationDataInterface.
    
    Template parameter ``t_ifstream``:
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class KongsbergAllAnnotationDataInterface_mapped:
    """
    Interface to read annotation data (no kongsberg datagram is currently
    supported) from a file (multiple files)
    
    Only sorts the supported datagrams. No caching is done. Gives access
    to AnnotationDataInterfacePerFile using the per_file function.
    
    Template parameter ``t_ifstream``:
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[...]) -> list[...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def per_file(self) -> list[...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllConfigurationDataInterface:
    """
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[..., ...]) -> list[..., ...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def get_sensor_configuration(self, index: int) -> themachinethatgoesping.navigation.SensorConfiguration:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def per_file(self) -> list[..., ...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[..., ...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[..., ...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllConfigurationDataInterfacePerFile:
    """
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_active_heading_sensor(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllActiveSensor:
        ...
    def get_active_heave_sensor(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllActiveSensor:
        ...
    def get_active_pitch_roll_sensor(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllActiveSensor:
        ...
    def get_active_position_system_number(self) -> int:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_installation_parameters(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.InstallationParameters:
        ...
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration:
        ...
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration:
        ...
    def set_active_heading_sensor(self, sensor: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllActiveSensor) -> None:
        """
        Set the active heading sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        t_KongsbergAllActiveSensor
        
        Parameter ``sensor``:
        """
    def set_active_heave_sensor(self, sensor: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllActiveSensor) -> None:
        """
        Set the active heave sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        t_KongsbergAllActiveSensor
        
        Parameter ``sensor``:
        """
    def set_active_pitch_roll_sensor(self, sensor: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllActiveSensor) -> None:
        """
        Set the active roll pitch sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        t_KongsbergAllActiveSensor
        
        Parameter ``sensor``:
        """
    def set_active_position_system_number(self, number: int) -> None:
        """
        Set the active position system number 0: this will be overwritten by
        "read_sensor_configuration" / "init_interface" 1-3: position system
        1-3
        
        Parameter ``number``:
        """
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None:
        ...
class KongsbergAllConfigurationDataInterfacePerFile_mapped:
    """
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_active_heading_sensor(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllActiveSensor:
        ...
    def get_active_heave_sensor(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllActiveSensor:
        ...
    def get_active_pitch_roll_sensor(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllActiveSensor:
        ...
    def get_active_position_system_number(self) -> int:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_installation_parameters(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.InstallationParameters:
        ...
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration:
        ...
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration:
        ...
    def set_active_heading_sensor(self, sensor: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllActiveSensor) -> None:
        """
        Set the active heading sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        t_KongsbergAllActiveSensor
        
        Parameter ``sensor``:
        """
    def set_active_heave_sensor(self, sensor: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllActiveSensor) -> None:
        """
        Set the active heave sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        t_KongsbergAllActiveSensor
        
        Parameter ``sensor``:
        """
    def set_active_pitch_roll_sensor(self, sensor: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllActiveSensor) -> None:
        """
        Set the active roll pitch sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        t_KongsbergAllActiveSensor
        
        Parameter ``sensor``:
        """
    def set_active_position_system_number(self, number: int) -> None:
        """
        Set the active position system number 0: this will be overwritten by
        "read_sensor_configuration" / "init_interface" 1-3: position system
        1-3
        
        Parameter ``number``:
        """
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None:
        ...
class KongsbergAllConfigurationDataInterface_mapped:
    """
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[...]) -> list[...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def get_sensor_configuration(self, index: int) -> themachinethatgoesping.navigation.SensorConfiguration:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def per_file(self) -> list[...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllDatagramDataInterface:
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Annotation, Environment, Ping)
    
    No datagram caching is implemented for this interface. Accessed
    packages are always read from file
    
    Template parameter ``t_ifstream``:
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[..., ...]) -> list[..., ...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def per_file(self) -> list[..., ...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[..., ...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[..., ...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllDatagramDataInterfacePerFile:
    """
    FileDataInterface (for single files) for packages that fit neither of
    the other FileDataInterfaces (Configuration, Navigation, Annotation,
    Environment, Ping)
    
    No datagram caching is implemented for this interface. Accessed
    packages are always read from file
    
    Template parameter ``t_ifstream``:
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class KongsbergAllDatagramDataInterfacePerFile_mapped:
    """
    FileDataInterface (for single files) for packages that fit neither of
    the other FileDataInterfaces (Configuration, Navigation, Annotation,
    Environment, Ping)
    
    No datagram caching is implemented for this interface. Accessed
    packages are always read from file
    
    Template parameter ``t_ifstream``:
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class KongsbergAllDatagramDataInterface_mapped:
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Annotation, Environment, Ping)
    
    No datagram caching is implemented for this interface. Accessed
    packages are always read from file
    
    Template parameter ``t_ifstream``:
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[...]) -> list[...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def per_file(self) -> list[...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllDatagramInterface:
    """
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class KongsbergAllDatagramInterface_mapped:
    """
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class KongsbergAllEnvironmentDataInterface:
    """
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[..., ...]) -> list[..., ...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface:
        ...
    @typing.overload
    def per_file(self) -> list[..., ...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[..., ...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[..., ...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllEnvironmentDataInterfacePerFile:
    """
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface:
        ...
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class KongsbergAllEnvironmentDataInterfacePerFile_mapped:
    """
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_mapped:
        ...
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface_mapped:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class KongsbergAllEnvironmentDataInterface_mapped:
    """
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[...]) -> list[...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_mapped:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface_mapped:
        ...
    @typing.overload
    def per_file(self) -> list[...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllNavigationDataInterface:
    """
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[..., ...]) -> list[..., ...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def channel_ids(self) -> list[str]:
        ...
    @typing.overload
    def channel_ids(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> list[str]:
        ...
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def get_geolocation(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration, channel_id: str, timestamp: float) -> themachinethatgoesping.navigation.datastructures.GeolocationLatLon:
        ...
    @typing.overload
    def get_navigation_cache(self, show_progress: bool = True) -> dict[str, themachinethatgoesping.navigation.NavigationInterpolatorLatLon]:
        ...
    @typing.overload
    def get_navigation_cache(self, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> dict[str, themachinethatgoesping.navigation.NavigationInterpolatorLatLon]:
        ...
    def get_navigation_interpolator(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon:
        ...
    def get_navigation_interpolators(self) -> dict[themachinethatgoesping.navigation.SensorConfiguration, themachinethatgoesping.navigation.NavigationInterpolatorLatLon]:
        ...
    def get_sensor_data(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration, timestamp: float) -> themachinethatgoesping.navigation.datastructures.SensordataLatLon:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def init_from_file_or_cache(self, cached_paths_per_file_path: dict[str, str] = {}, cache: dict[str, themachinethatgoesping.navigation.NavigationInterpolatorLatLon] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file_or_cache(self, cached_paths_per_file_path: dict[str, str], cache: dict[str, themachinethatgoesping.navigation.NavigationInterpolatorLatLon], force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def per_file(self) -> list[..., ...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[..., ...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[..., ...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllNavigationDataInterfacePerFile:
    """
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface:
        ...
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon:
        ...
class KongsbergAllNavigationDataInterfacePerFile_mapped:
    """
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_mapped:
        ...
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon:
        ...
class KongsbergAllNavigationDataInterface_mapped:
    """
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[...]) -> list[...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def channel_ids(self) -> list[str]:
        ...
    @typing.overload
    def channel_ids(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> list[str]:
        ...
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_mapped:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def get_geolocation(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration, channel_id: str, timestamp: float) -> themachinethatgoesping.navigation.datastructures.GeolocationLatLon:
        ...
    @typing.overload
    def get_navigation_cache(self, show_progress: bool = True) -> dict[str, themachinethatgoesping.navigation.NavigationInterpolatorLatLon]:
        ...
    @typing.overload
    def get_navigation_cache(self, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> dict[str, themachinethatgoesping.navigation.NavigationInterpolatorLatLon]:
        ...
    def get_navigation_interpolator(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon:
        ...
    def get_navigation_interpolators(self) -> dict[themachinethatgoesping.navigation.SensorConfiguration, themachinethatgoesping.navigation.NavigationInterpolatorLatLon]:
        ...
    def get_sensor_data(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration, timestamp: float) -> themachinethatgoesping.navigation.datastructures.SensordataLatLon:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def init_from_file_or_cache(self, cached_paths_per_file_path: dict[str, str] = {}, cache: dict[str, themachinethatgoesping.navigation.NavigationInterpolatorLatLon] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file_or_cache(self, cached_paths_per_file_path: dict[str, str], cache: dict[str, themachinethatgoesping.navigation.NavigationInterpolatorLatLon], force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def per_file(self) -> list[...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllOtherFileDataInterface:
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Annotation, Environment, Ping)
    
    No datagram caching is implemented for this interface. Accessed
    packages are always read from file
    
    Template parameter ``t_ifstream``:
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[..., ...]) -> list[..., ...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def per_file(self) -> list[..., ...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[..., ...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[..., ...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllOtherFileDataInterfacePerFile:
    """
    FileDataInterface (for single files) for packages that fit neither of
    the other FileDataInterfaces (Configuration, Navigation, Annotation,
    Environment, Ping)
    
    No datagram caching is implemented for this interface. Accessed
    packages are always read from file
    
    Template parameter ``t_ifstream``:
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class KongsbergAllOtherFileDataInterfacePerFile_mapped:
    """
    FileDataInterface (for single files) for packages that fit neither of
    the other FileDataInterfaces (Configuration, Navigation, Annotation,
    Environment, Ping)
    
    No datagram caching is implemented for this interface. Accessed
    packages are always read from file
    
    Template parameter ``t_ifstream``:
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class KongsbergAllOtherFileDataInterface_mapped:
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Annotation, Environment, Ping)
    
    No datagram caching is implemented for this interface. Accessed
    packages are always read from file
    
    Template parameter ``t_ifstream``:
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[...]) -> list[...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def per_file(self) -> list[...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllPingDataInterface:
    """
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[..., ...]) -> list[..., ...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def channel_ids(self) -> list[str]:
        ...
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def environment_data_interface(self) -> KongsbergAllEnvironmentDataInterface:
        ...
    @typing.overload
    def get_pings(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.filedatacontainers.KongsbergAllPingContainer:
        ...
    @typing.overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_cppy.kongsbergall.filedatacontainers.KongsbergAllPingContainer:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface:
        ...
    @typing.overload
    def per_file(self) -> list[..., ...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[..., ...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[..., ...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllPingDataInterfacePerFile:
    """
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface:
        ...
    def configuration_data_interface_for_file(self) -> KongsbergAllConfigurationDataInterfacePerFile:
        ...
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def environment_data_interface(self) -> KongsbergAllEnvironmentDataInterface:
        ...
    def get_deduplicated_runtime_parameters(self) -> dict[str, themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RuntimeParameters]:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def read_pings(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.filedatacontainers.KongsbergAllPingContainer:
        ...
class KongsbergAllPingDataInterfacePerFile_mapped:
    """
    """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_mapped:
        ...
    def configuration_data_interface_for_file(self) -> KongsbergAllConfigurationDataInterfacePerFile_mapped:
        ...
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def environment_data_interface(self) -> KongsbergAllEnvironmentDataInterface_mapped:
        ...
    def get_deduplicated_runtime_parameters(self) -> dict[str, themachinethatgoesping.echosounders_cppy.kongsbergall.datagrams.RuntimeParameters]:
        ...
    def get_file_nr(self) -> int:
        """
        Get the file nr This function assumes that the file nr is the same for
        all datagrams in the file
        
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
    def get_linked_file_nr(self) -> int:
        """
        Get the file nr of the linked file
        
        Returns:
            size_t
        """
    def get_linked_file_path(self) -> str:
        """
        Get the file name of the linked file
        
        Returns:
            std::string
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, cache_file_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface_mapped:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def read_pings(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.filedatacontainers.KongsbergAllPingContainer_mapped:
        ...
class KongsbergAllPingDataInterface_mapped:
    """
    """
    @staticmethod
    def sort_by_time(fileinterfaces: list[...]) -> list[...]:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def channel_ids(self) -> list[str]:
        ...
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_mapped:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def environment_data_interface(self) -> KongsbergAllEnvironmentDataInterface_mapped:
        ...
    @typing.overload
    def get_pings(self) -> themachinethatgoesping.echosounders_cppy.kongsbergall.filedatacontainers.KongsbergAllPingContainer_mapped:
        ...
    @typing.overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_cppy.kongsbergall.filedatacontainers.KongsbergAllPingContainer_mapped:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, cached_paths_per_file_path: dict[str, str] = {}, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface_mapped:
        ...
    @typing.overload
    def per_file(self) -> list[...]:
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @typing.overload
    def per_file(self, file_nr: int) -> ...:
        ...
    def per_primary_file(self) -> list[...]:
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def per_secondary_file(self) -> list[...]:
        """
        get a vector with references to the secondary per file interfaces This
        is useful for iterating over all secondary files Primary files will be
        ignored (e.g. .all for Kongsberg data if .wcd is present)
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
