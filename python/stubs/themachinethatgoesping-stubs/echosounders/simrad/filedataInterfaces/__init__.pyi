"""Simrad EK60 and EK80 file data interface classes"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad.filedataInterfaces
import typing
import themachinethatgoesping.echosounders.simrad
import themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams
import themachinethatgoesping.echosounders.simrad.filedatacontainers
import themachinethatgoesping.navigation
import themachinethatgoesping.navigation.datastructures
import themachinethatgoesping.tools.progressbars

__all__ = [
    "SimradAnnotationDataInterface",
    "SimradAnnotationDataInterface_PerFile",
    "SimradAnnotationDataInterface_PerFile_mapped",
    "SimradAnnotationDataInterface_mapped",
    "SimradConfigurationDataInterface",
    "SimradConfigurationDataInterface_PerFile",
    "SimradConfigurationDataInterface_PerFile_mapped",
    "SimradConfigurationDataInterface_mapped",
    "SimradDatagramInterface",
    "SimradDatagramInterface_mapped",
    "SimradEnvironmentDataInterface",
    "SimradEnvironmentDataInterface_PerFile",
    "SimradEnvironmentDataInterface_PerFile_mapped",
    "SimradEnvironmentDataInterface_mapped",
    "SimradNavigationDataInterface",
    "SimradNavigationDataInterface_PerFile",
    "SimradNavigationDataInterface_PerFile_mapped",
    "SimradNavigationDataInterface_mapped",
    "SimradOtherDataInterface",
    "SimradOtherDataInterface_mapped",
    "SimradOtherFileDataInterface_PerFile",
    "SimradOtherFileDataInterface_PerFile_mapped",
    "SimradPingDataInterface",
    "SimradPingDataInterface_PerFile",
    "SimradPingDataInterface_PerFile_mapped",
    "SimradPingDataInterface_mapped"
]


class SimradAnnotationDataInterface():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def deinitialize(self) -> None: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradAnnotationDataInterface_PerFile():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
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
        for all datagrams in the file

        Returns:
            std::string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradAnnotationDataInterface_PerFile_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
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
        for all datagrams in the file

        Returns:
            std::string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradAnnotationDataInterface_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def deinitialize(self) -> None: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradConfigurationDataInterface():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def deinitialize(self) -> None: ...
    def get_sensor_configuration(self, index: int) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradConfigurationDataInterface_PerFile():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
    def get_attitude_sources(self) -> typing.List[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all attitude sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_configuration_datagram(self) -> themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Configuration: ...
    def get_depth_sources(self) -> typing.List[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
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
        for all datagrams in the file

        Returns:
            std::string
        """
    def get_heading_sources(self) -> typing.List[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all heading sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_position_sources(self) -> typing.List[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all position sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
    pass
class SimradConfigurationDataInterface_PerFile_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
    def get_attitude_sources(self) -> typing.List[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all attitude sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_configuration_datagram(self) -> themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Configuration: ...
    def get_depth_sources(self) -> typing.List[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
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
        for all datagrams in the file

        Returns:
            std::string
        """
    def get_heading_sources(self) -> typing.List[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all heading sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_position_sources(self) -> typing.List[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all position sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
    pass
class SimradConfigurationDataInterface_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def deinitialize(self) -> None: ...
    def get_sensor_configuration(self, index: int) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradDatagramInterface():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradDatagramInterface_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradEnvironmentDataInterface():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> SimradConfigurationDataInterface: ...
    def deinitialize(self) -> None: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradEnvironmentDataInterface_PerFile():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> SimradConfigurationDataInterface: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
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
        for all datagrams in the file

        Returns:
            std::string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradEnvironmentDataInterface_PerFile_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> SimradConfigurationDataInterface_mapped: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
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
        for all datagrams in the file

        Returns:
            std::string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface_mapped: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradEnvironmentDataInterface_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> SimradConfigurationDataInterface_mapped: ...
    def deinitialize(self) -> None: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface_mapped: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradNavigationDataInterface():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def channel_ids(self) -> typing.List[str]: ...
    def configuration_data_interface(self) -> SimradConfigurationDataInterface: ...
    def deinitialize(self) -> None: ...
    def get_geolocation(self, channel_id: str, timestamp: float) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: ...
    def get_navigation_data(self) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon: ...
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_max_gga_quality(self, max_gga_quality: int) -> None: ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None: ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
    pass
class SimradNavigationDataInterface_PerFile():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> SimradConfigurationDataInterface: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
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
        for all datagrams in the file

        Returns:
            std::string
        """
    def get_max_gga_quality(self) -> int: ...
    def get_min_gga_quality(self) -> int: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon: ...
    def set_max_gga_quality(self, max_gga_quality: int) -> None: ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None: ...
    pass
class SimradNavigationDataInterface_PerFile_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> SimradConfigurationDataInterface_mapped: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
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
        for all datagrams in the file

        Returns:
            std::string
        """
    def get_max_gga_quality(self) -> int: ...
    def get_min_gga_quality(self) -> int: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon: ...
    def set_max_gga_quality(self, max_gga_quality: int) -> None: ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None: ...
    pass
class SimradNavigationDataInterface_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def channel_ids(self) -> typing.List[str]: ...
    def configuration_data_interface(self) -> SimradConfigurationDataInterface_mapped: ...
    def deinitialize(self) -> None: ...
    def get_geolocation(self, channel_id: str, timestamp: float) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: ...
    def get_navigation_data(self) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon: ...
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_max_gga_quality(self, max_gga_quality: int) -> None: ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None: ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
    pass
class SimradOtherDataInterface():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def deinitialize(self) -> None: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradOtherDataInterface_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def deinitialize(self) -> None: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradOtherFileDataInterface_PerFile():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
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
        for all datagrams in the file

        Returns:
            std::string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradOtherFileDataInterface_PerFile_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
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
        for all datagrams in the file

        Returns:
            std::string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradPingDataInterface():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def channel_ids(self) -> typing.List[str]: ...
    def configuration_data_interface(self) -> SimradConfigurationDataInterface: ...
    def deinitialize(self) -> None: ...
    def environment_data_interface(self) -> SimradEnvironmentDataInterface: ...
    @typing.overload
    def get_pings(self) -> themachinethatgoesping.echosounders.simrad.filedatacontainers.SimradPingContainer: ...
    @typing.overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders.simrad.filedatacontainers.SimradPingContainer: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradPingDataInterface_PerFile():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> SimradConfigurationDataInterface: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
    def environment_data_interface(self) -> SimradEnvironmentDataInterface: ...
    def get_deduplicated_parameters(self) -> typing.Dict[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Parameter_Channel, themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Parameter_Channel]: ...
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
        for all datagrams in the file

        Returns:
            std::string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradPingDataInterface_PerFile_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> SimradConfigurationDataInterface_mapped: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
    def environment_data_interface(self) -> SimradEnvironmentDataInterface_mapped: ...
    def get_deduplicated_parameters(self) -> typing.Dict[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Parameter_Channel, themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Parameter_Channel]: ...
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
        for all datagrams in the file

        Returns:
            std::string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface_mapped: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradPingDataInterface_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def channel_ids(self) -> typing.List[str]: ...
    def configuration_data_interface(self) -> SimradConfigurationDataInterface_mapped: ...
    def deinitialize(self) -> None: ...
    def environment_data_interface(self) -> SimradEnvironmentDataInterface_mapped: ...
    @typing.overload
    def get_pings(self) -> themachinethatgoesping.echosounders.simrad.filedatacontainers.SimradPingContainer_mapped: ...
    @typing.overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders.simrad.filedatacontainers.SimradPingContainer_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface_mapped: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
