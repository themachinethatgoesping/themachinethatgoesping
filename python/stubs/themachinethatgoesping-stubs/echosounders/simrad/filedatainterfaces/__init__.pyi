"""Simrad EK60 and EK80 file data interface classes"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad.filedatainterfaces
import typing
import themachinethatgoesping.echosounders.simrad
import themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams
import themachinethatgoesping.echosounders.simrad.filedatacontainers
import themachinethatgoesping.navigation
import themachinethatgoesping.navigation.datastructures
import themachinethatgoesping.tools.progressbars

__all__ = [
    "SimradAnnotationDataInterface",
    "SimradAnnotationDataInterfacePerFile",
    "SimradAnnotationDataInterfacePerFile_mapped",
    "SimradAnnotationDataInterface_mapped",
    "SimradConfigurationDataInterface",
    "SimradConfigurationDataInterfacePerFile",
    "SimradConfigurationDataInterfacePerFile_mapped",
    "SimradConfigurationDataInterface_mapped",
    "SimradDatagramInterface",
    "SimradDatagramInterface_mapped",
    "SimradEnvironmentDataInterface",
    "SimradEnvironmentDataInterfacePerFile",
    "SimradEnvironmentDataInterfacePerFile_mapped",
    "SimradEnvironmentDataInterface_mapped",
    "SimradNavigationDataInterface",
    "SimradNavigationDataInterfacePerFile",
    "SimradNavigationDataInterfacePerFile_mapped",
    "SimradNavigationDataInterface_mapped",
    "SimradOtherFileDataInterface",
    "SimradOtherFileDataInterface_mapped",
    "SimradPingDataInterface",
    "SimradPingDataInterfacePerFile",
    "SimradPingDataInterfacePerFile_mapped",
    "SimradPingDataInterface_mapped",
    "init_c_simradotherfiledatainterfaceperfile",
    "init_c_simradotherfiledatainterfaceperfile_mapped"
]


class SimradAnnotationDataInterface():
    """
    Interface to read Simrad annotation data (TAG0) from a file (multiple
    files)

    Only sorts the supported datagrams. No caching is done. Gives access
    to SimradAnnotationDataInterfacePerFile using the per_file function.

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
    def deinitialize(self) -> None: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_primary_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_secondary_file(*args, **kwargs) -> typing.Any: 
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
    pass
class SimradAnnotationDataInterfacePerFile():
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
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
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
    def get_timestamp_first(self) -> float: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def per_file(self) -> typing.List[SimradDatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradAnnotationDataInterfacePerFile_mapped():
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
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
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
    def get_timestamp_first(self) -> float: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def per_file(self) -> typing.List[SimradDatagramInterface_mapped]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradAnnotationDataInterface_mapped():
    """
    Interface to read Simrad annotation data (TAG0) from a file (multiple
    files)

    Only sorts the supported datagrams. No caching is done. Gives access
    to SimradAnnotationDataInterfacePerFile using the per_file function.

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
    def deinitialize(self) -> None: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_primary_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_secondary_file(*args, **kwargs) -> typing.Any: 
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
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_primary_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_secondary_file(*args, **kwargs) -> typing.Any: 
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
    pass
class SimradConfigurationDataInterfacePerFile():
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
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
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
    def get_position_sources(self) -> typing.List[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all position sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def get_timestamp_first(self) -> float: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def per_file(self) -> typing.List[SimradDatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
    pass
class SimradConfigurationDataInterfacePerFile_mapped():
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
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
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
    def get_position_sources(self) -> typing.List[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all position sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def get_timestamp_first(self) -> float: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def per_file(self) -> typing.List[SimradDatagramInterface_mapped]: ...
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
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_primary_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_secondary_file(*args, **kwargs) -> typing.Any: 
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
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def get_timestamp_first(self) -> float: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def per_file(self) -> typing.List[SimradDatagramInterface]: ...
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
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def get_timestamp_first(self) -> float: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def per_file(self) -> typing.List[SimradDatagramInterface_mapped]: ...
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
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_primary_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_secondary_file(*args, **kwargs) -> typing.Any: 
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
    pass
class SimradEnvironmentDataInterfacePerFile():
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
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
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
    def get_timestamp_first(self) -> float: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface: ...
    def per_file(self) -> typing.List[SimradDatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class SimradEnvironmentDataInterfacePerFile_mapped():
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
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
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
    def get_timestamp_first(self) -> float: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface_mapped: ...
    def per_file(self) -> typing.List[SimradDatagramInterface_mapped]: ...
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
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface_mapped: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_primary_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_secondary_file(*args, **kwargs) -> typing.Any: 
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
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_primary_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_secondary_file(*args, **kwargs) -> typing.Any: 
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
    def set_max_gga_quality(self, max_gga_quality: int) -> None: ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None: ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
    def verify_linked_file_interfaces_are_consistent(self) -> None: 
        """
        This functions throws if linked file interfaces are not consistent
        """
    pass
class SimradNavigationDataInterfacePerFile():
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
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
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
    def get_max_gga_quality(self) -> int: ...
    def get_min_gga_quality(self) -> int: ...
    def get_timestamp_first(self) -> float: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def per_file(self) -> typing.List[SimradDatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon: ...
    def set_max_gga_quality(self, max_gga_quality: int) -> None: ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None: ...
    pass
class SimradNavigationDataInterfacePerFile_mapped():
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
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
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
    def get_max_gga_quality(self) -> int: ...
    def get_min_gga_quality(self) -> int: ...
    def get_timestamp_first(self) -> float: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def per_file(self) -> typing.List[SimradDatagramInterface_mapped]: ...
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
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_primary_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_secondary_file(*args, **kwargs) -> typing.Any: 
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
    def set_max_gga_quality(self, max_gga_quality: int) -> None: ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None: ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
    def verify_linked_file_interfaces_are_consistent(self) -> None: 
        """
        This functions throws if linked file interfaces are not consistent
        """
    pass
class SimradOtherFileDataInterface():
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Annotation, Environment, Ping)

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
    def deinitialize(self) -> None: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_primary_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_secondary_file(*args, **kwargs) -> typing.Any: 
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
    pass
class SimradOtherFileDataInterface_mapped():
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Annotation, Environment, Ping)

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
    def deinitialize(self) -> None: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_primary_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_secondary_file(*args, **kwargs) -> typing.Any: 
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
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_primary_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_secondary_file(*args, **kwargs) -> typing.Any: 
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
    pass
class SimradPingDataInterfacePerFile():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> SimradConfigurationDataInterface: ...
    def configuration_data_interface_for_file(self) -> SimradConfigurationDataInterfacePerFile: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
    def environment_data_interface(self) -> SimradEnvironmentDataInterface: ...
    def get_deduplicated_parameters(self) -> typing.List[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Parameter_Channel]: ...
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
    def get_timestamp_first(self) -> float: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface: ...
    def per_file(self) -> typing.List[SimradDatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_pings(self) -> themachinethatgoesping.echosounders.simrad.filedatacontainers.SimradPingContainer: ...
    pass
class SimradPingDataInterfacePerFile_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> SimradConfigurationDataInterface_mapped: ...
    def configuration_data_interface_for_file(self) -> SimradConfigurationDataInterfacePerFile_mapped: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
    def environment_data_interface(self) -> SimradEnvironmentDataInterface_mapped: ...
    def get_deduplicated_parameters(self) -> typing.List[themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Parameter_Channel]: ...
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
    def get_timestamp_first(self) -> float: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface_mapped: ...
    def per_file(self) -> typing.List[SimradDatagramInterface_mapped]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_pings(self) -> themachinethatgoesping.echosounders.simrad.filedatacontainers.SimradPingContainer_mapped: ...
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
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> SimradNavigationDataInterface_mapped: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the per file interfaces This is useful
        for iterating over all files

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_primary_file(*args, **kwargs) -> typing.Any: 
        """
        get a vector with references to the primary per file interfaces This
        is useful for iterating over all primary files Secondary files will be
        ignored (e.g. .wcd for Kongsberg data if .all is present)

        Returns:
            std::vector<t_filedatainterface_perfile&>
        """
    @staticmethod
    def per_secondary_file(*args, **kwargs) -> typing.Any: 
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
    pass
class init_c_simradotherfiledatainterfaceperfile():
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
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
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
    def get_timestamp_first(self) -> float: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def per_file(self) -> typing.List[SimradDatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class init_c_simradotherfiledatainterfaceperfile_mapped():
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
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier, skip_data: bool = False) -> object: ...
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
    def get_timestamp_first(self) -> float: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier]: ...
    def per_file(self) -> typing.List[SimradDatagramInterface_mapped]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
