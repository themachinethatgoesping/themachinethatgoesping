"""
SimradRaw EK60 and EK80 file data interface classes
"""
from __future__ import annotations
import themachinethatgoesping.echosounders_cppy.simradraw
import themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams
import themachinethatgoesping.echosounders_cppy.simradraw.filedatacontainers
import themachinethatgoesping.navigation
import themachinethatgoesping.navigation.datastructures
import themachinethatgoesping.tools_cppy.progressbars
import typing
__all__ = ['SimradRawAnnotationDataInterface', 'SimradRawAnnotationDataInterfacePerFile', 'SimradRawAnnotationDataInterfacePerFile_mapped', 'SimradRawAnnotationDataInterface_mapped', 'SimradRawConfigurationDataInterface', 'SimradRawConfigurationDataInterfacePerFile', 'SimradRawConfigurationDataInterfacePerFile_mapped', 'SimradRawConfigurationDataInterface_mapped', 'SimradRawDatagramDataInterface', 'SimradRawDatagramDataInterfacePerFile', 'SimradRawDatagramDataInterfacePerFile_mapped', 'SimradRawDatagramDataInterface_mapped', 'SimradRawDatagramInterface', 'SimradRawDatagramInterface_mapped', 'SimradRawEnvironmentDataInterface', 'SimradRawEnvironmentDataInterfacePerFile', 'SimradRawEnvironmentDataInterfacePerFile_mapped', 'SimradRawEnvironmentDataInterface_mapped', 'SimradRawNavigationDataInterface', 'SimradRawNavigationDataInterfacePerFile', 'SimradRawNavigationDataInterfacePerFile_mapped', 'SimradRawNavigationDataInterface_mapped', 'SimradRawOtherFileDataInterface', 'SimradRawOtherFileDataInterface_mapped', 'SimradRawPingDataInterface', 'SimradRawPingDataInterfacePerFile', 'SimradRawPingDataInterfacePerFile_mapped', 'SimradRawPingDataInterface_mapped', 'init_c_simradrawotherfiledatainterfaceperfile', 'init_c_simradrawotherfiledatainterfaceperfile_mapped']
class SimradRawAnnotationDataInterface:
    """
    Interface to read SimradRaw annotation data (TAG0) from a file
    (multiple files)
    
    Only sorts the supported datagrams. No caching is done. Gives access
    to SimradRawAnnotationDataInterfacePerFile using the per_file
    function.
    
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
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
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
class SimradRawAnnotationDataInterfacePerFile:
    """
    Interface to read annotation data (TAG0) from a file (per file)
    
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class SimradRawAnnotationDataInterfacePerFile_mapped:
    """
    Interface to read annotation data (TAG0) from a file (per file)
    
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class SimradRawAnnotationDataInterface_mapped:
    """
    Interface to read SimradRaw annotation data (TAG0) from a file
    (multiple files)
    
    Only sorts the supported datagrams. No caching is done. Gives access
    to SimradRawAnnotationDataInterfacePerFile using the per_file
    function.
    
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
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
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
class SimradRawConfigurationDataInterface:
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
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
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
class SimradRawConfigurationDataInterfacePerFile:
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_attitude_sources(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all attitude sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_configuration_datagram(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration:
        ...
    def get_depth_sources(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all depth sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
        """
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
    def get_heading_sources(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all heading sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
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
    def get_position_sources(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all position sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration:
        ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None:
        ...
class SimradRawConfigurationDataInterfacePerFile_mapped:
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def get_attitude_sources(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all attitude sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_configuration_datagram(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration:
        ...
    def get_depth_sources(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all depth sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
        """
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
    def get_heading_sources(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all heading sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
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
    def get_position_sources(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all position sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration:
        ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None:
        ...
class SimradRawConfigurationDataInterface_mapped:
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
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
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
class SimradRawDatagramDataInterface:
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
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
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
class SimradRawDatagramDataInterfacePerFile:
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class SimradRawDatagramDataInterfacePerFile_mapped:
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class SimradRawDatagramDataInterface_mapped:
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
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
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
class SimradRawDatagramInterface:
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
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
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class SimradRawDatagramInterface_mapped:
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
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
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class SimradRawEnvironmentDataInterface:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface:
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
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface:
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
class SimradRawEnvironmentDataInterfacePerFile:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface:
        ...
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class SimradRawEnvironmentDataInterfacePerFile_mapped:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_mapped:
        ...
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface_mapped:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class SimradRawEnvironmentDataInterface_mapped:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_mapped:
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
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface_mapped:
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
class SimradRawNavigationDataInterface:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface:
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
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def init_from_file_or_cache(self, cache: dict[str, themachinethatgoesping.navigation.NavigationInterpolatorLatLon] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file_or_cache(self, cache: dict[str, themachinethatgoesping.navigation.NavigationInterpolatorLatLon], force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
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
    def set_max_gga_quality(self, max_gga_quality: int) -> None:
        ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None:
        ...
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class SimradRawNavigationDataInterfacePerFile:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface:
        ...
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
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
    def get_max_gga_quality(self) -> int:
        ...
    def get_min_gga_quality(self) -> int:
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon:
        ...
    def set_max_gga_quality(self, max_gga_quality: int) -> None:
        ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None:
        ...
class SimradRawNavigationDataInterfacePerFile_mapped:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_mapped:
        ...
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
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
    def get_max_gga_quality(self) -> int:
        ...
    def get_min_gga_quality(self) -> int:
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon:
        ...
    def set_max_gga_quality(self, max_gga_quality: int) -> None:
        ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None:
        ...
class SimradRawNavigationDataInterface_mapped:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_mapped:
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
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def init_from_file_or_cache(self, cache: dict[str, themachinethatgoesping.navigation.NavigationInterpolatorLatLon] = {}, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file_or_cache(self, cache: dict[str, themachinethatgoesping.navigation.NavigationInterpolatorLatLon], force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
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
    def set_max_gga_quality(self, max_gga_quality: int) -> None:
        ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None:
        ...
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class SimradRawOtherFileDataInterface:
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
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
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
class SimradRawOtherFileDataInterface_mapped:
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
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
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
class SimradRawPingDataInterface:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def environment_data_interface(self) -> SimradRawEnvironmentDataInterface:
        ...
    @typing.overload
    def get_pings(self) -> themachinethatgoesping.echosounders_cppy.simradraw.filedatacontainers.SimradRawPingContainer:
        ...
    @typing.overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_cppy.simradraw.filedatacontainers.SimradRawPingContainer:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface:
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
class SimradRawPingDataInterfacePerFile:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface:
        ...
    def configuration_data_interface_for_file(self) -> SimradRawConfigurationDataInterfacePerFile:
        ...
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def environment_data_interface(self) -> SimradRawEnvironmentDataInterface:
        ...
    def get_deduplicated_parameters(self) -> dict[str, themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel]:
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def read_pings(self) -> themachinethatgoesping.echosounders_cppy.simradraw.filedatacontainers.SimradRawPingContainer:
        ...
class SimradRawPingDataInterfacePerFile_mapped:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_mapped:
        ...
    def configuration_data_interface_for_file(self) -> SimradRawConfigurationDataInterfacePerFile_mapped:
        ...
    @typing.overload
    def datagram_headers(self) -> typing.Any:
        ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    def deinitialize(self) -> None:
        ...
    def environment_data_interface(self) -> SimradRawEnvironmentDataInterface_mapped:
        ...
    def get_deduplicated_parameters(self) -> dict[str, themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel]:
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface_mapped:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def read_pings(self) -> themachinethatgoesping.echosounders_cppy.simradraw.filedatacontainers.SimradRawPingContainer_mapped:
        ...
class SimradRawPingDataInterface_mapped:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_mapped:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    @typing.overload
    def deinitialize(self) -> None:
        ...
    def environment_data_interface(self) -> SimradRawEnvironmentDataInterface_mapped:
        ...
    @typing.overload
    def get_pings(self) -> themachinethatgoesping.echosounders_cppy.simradraw.filedatacontainers.SimradRawPingContainer_mapped:
        ...
    @typing.overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_cppy.simradraw.filedatacontainers.SimradRawPingContainer_mapped:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    @typing.overload
    def is_initialized(self) -> bool:
        ...
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface_mapped:
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
class init_c_simradrawotherfiledatainterfaceperfile:
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class init_c_simradrawotherfiledatainterfaceperfile_mapped:
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self) -> typing.Any:
        ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier) -> typing.Any:
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
    def init_from_file(self, force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_mapped]:
        ...
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
