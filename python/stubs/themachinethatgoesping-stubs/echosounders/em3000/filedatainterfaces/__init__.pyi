"""EM3000 (kongsberg .all/.wcd) file data interface classes"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000.filedatainterfaces
import typing
import themachinethatgoesping.echosounders.em3000
import themachinethatgoesping.echosounders.em3000.datagrams
import themachinethatgoesping.echosounders.em3000.filedatacontainers
import themachinethatgoesping.navigation
import themachinethatgoesping.navigation.datastructures
import themachinethatgoesping.tools.progressbars

__all__ = [
    "EM3000AnnotationDataInterface",
    "EM3000AnnotationDataInterfacePerFile",
    "EM3000AnnotationDataInterfacePerFile_mapped",
    "EM3000AnnotationDataInterface_mapped",
    "EM3000ConfigurationDataInterface",
    "EM3000ConfigurationDataInterfacePerFile",
    "EM3000ConfigurationDataInterfacePerFile_mapped",
    "EM3000ConfigurationDataInterface_mapped",
    "EM3000DatagramInterface",
    "EM3000DatagramInterface_mapped",
    "EM3000EnvironmentDataInterface",
    "EM3000EnvironmentDataInterfacePerFile",
    "EM3000EnvironmentDataInterfacePerFile_mapped",
    "EM3000EnvironmentDataInterface_mapped",
    "EM3000NavigationDataInterface",
    "EM3000NavigationDataInterfacePerFile",
    "EM3000NavigationDataInterfacePerFile_mapped",
    "EM3000NavigationDataInterface_mapped",
    "EM3000OtherFileDataInterface",
    "EM3000OtherFileDataInterfacePerFile",
    "EM3000OtherFileDataInterfacePerFile_mapped",
    "EM3000OtherFileDataInterface_mapped",
    "EM3000PingDataInterface",
    "EM3000PingDataInterfacePerFile",
    "EM3000PingDataInterfacePerFile_mapped",
    "EM3000PingDataInterface_mapped"
]


class EM3000AnnotationDataInterface():
    """
    Interface to read annotation data (no kongsberg datagram is currently
    supported) from a file (multiple files)

    Only sorts the supported datagrams. No caching is done. Gives access
    to AnnotationDataInterfacePerFile using the per_file function.

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
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
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
class EM3000AnnotationDataInterfacePerFile():
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
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
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
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class EM3000AnnotationDataInterfacePerFile_mapped():
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
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
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
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface_mapped]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class EM3000AnnotationDataInterface_mapped():
    """
    Interface to read annotation data (no kongsberg datagram is currently
    supported) from a file (multiple files)

    Only sorts the supported datagrams. No caching is done. Gives access
    to AnnotationDataInterfacePerFile using the per_file function.

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
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
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
class EM3000ConfigurationDataInterface():
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
class EM3000ConfigurationDataInterfacePerFile():
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
    def get_active_heading_sensor(self) -> themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor: ...
    def get_active_heave_sensor(self) -> themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor: ...
    def get_active_pitch_roll_sensor(self) -> themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor: ...
    def get_active_position_system_number(self) -> int: ...
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
    def get_installation_parameters(self) -> themachinethatgoesping.echosounders.em3000.datagrams.InstallationParameters: ...
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
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def set_active_heading_sensor(self, sensor: themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor) -> None: 
        """
        Set the active heading sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        t_EM3000ActiveSensor

        Parameter ``sensor``:
        """
    def set_active_heave_sensor(self, sensor: themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor) -> None: 
        """
        Set the active heave sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        t_EM3000ActiveSensor

        Parameter ``sensor``:
        """
    def set_active_pitch_roll_sensor(self, sensor: themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor) -> None: 
        """
        Set the active roll pitch sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        t_EM3000ActiveSensor

        Parameter ``sensor``:
        """
    def set_active_position_system_number(self, number: int) -> None: 
        """
        Set the active position system number 0: this will be overwritten by
        "read_sensor_configuration" / "init_interface" 1-3: position system
        1-3

        Parameter ``number``:
        """
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
    pass
class EM3000ConfigurationDataInterfacePerFile_mapped():
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
    def get_active_heading_sensor(self) -> themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor: ...
    def get_active_heave_sensor(self) -> themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor: ...
    def get_active_pitch_roll_sensor(self) -> themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor: ...
    def get_active_position_system_number(self) -> int: ...
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
    def get_installation_parameters(self) -> themachinethatgoesping.echosounders.em3000.datagrams.InstallationParameters: ...
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
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface_mapped]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def set_active_heading_sensor(self, sensor: themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor) -> None: 
        """
        Set the active heading sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        t_EM3000ActiveSensor

        Parameter ``sensor``:
        """
    def set_active_heave_sensor(self, sensor: themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor) -> None: 
        """
        Set the active heave sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        t_EM3000ActiveSensor

        Parameter ``sensor``:
        """
    def set_active_pitch_roll_sensor(self, sensor: themachinethatgoesping.echosounders.em3000.t_EM3000ActiveSensor) -> None: 
        """
        Set the active roll pitch sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        t_EM3000ActiveSensor

        Parameter ``sensor``:
        """
    def set_active_position_system_number(self, number: int) -> None: 
        """
        Set the active position system number 0: this will be overwritten by
        "read_sensor_configuration" / "init_interface" 1-3: position system
        1-3

        Parameter ``number``:
        """
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
    pass
class EM3000ConfigurationDataInterface_mapped():
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
class EM3000DatagramInterface():
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class EM3000DatagramInterface_mapped():
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface_mapped]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class EM3000EnvironmentDataInterface():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> EM3000ConfigurationDataInterface: ...
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
    def navigation_data_interface(self) -> EM3000NavigationDataInterface: ...
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
class EM3000EnvironmentDataInterfacePerFile():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> EM3000ConfigurationDataInterface: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
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
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def navigation_data_interface(self) -> EM3000NavigationDataInterface: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class EM3000EnvironmentDataInterfacePerFile_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> EM3000ConfigurationDataInterface_mapped: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
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
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def navigation_data_interface(self) -> EM3000NavigationDataInterface_mapped: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface_mapped]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class EM3000EnvironmentDataInterface_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> EM3000ConfigurationDataInterface_mapped: ...
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
    def navigation_data_interface(self) -> EM3000NavigationDataInterface_mapped: ...
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
class EM3000NavigationDataInterface():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def channel_ids(self) -> typing.List[str]: ...
    def configuration_data_interface(self) -> EM3000ConfigurationDataInterface: ...
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
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
    def verify_linked_file_interfaces_are_consistent(self) -> None: 
        """
        This functions throws if linked file interfaces are not consistent
        """
    pass
class EM3000NavigationDataInterfacePerFile():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> EM3000ConfigurationDataInterface: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
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
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon: ...
    pass
class EM3000NavigationDataInterfacePerFile_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> EM3000ConfigurationDataInterface_mapped: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
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
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface_mapped]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation.NavigationInterpolatorLatLon: ...
    pass
class EM3000NavigationDataInterface_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def channel_ids(self) -> typing.List[str]: ...
    def configuration_data_interface(self) -> EM3000ConfigurationDataInterface_mapped: ...
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
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
    def verify_linked_file_interfaces_are_consistent(self) -> None: 
        """
        This functions throws if linked file interfaces are not consistent
        """
    pass
class EM3000OtherFileDataInterface():
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
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
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
class EM3000OtherFileDataInterfacePerFile():
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
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
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class EM3000OtherFileDataInterfacePerFile_mapped():
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
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
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
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface_mapped]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class EM3000OtherFileDataInterface_mapped():
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
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
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
class EM3000PingDataInterface():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def channel_ids(self) -> typing.List[str]: ...
    def configuration_data_interface(self) -> EM3000ConfigurationDataInterface: ...
    def deinitialize(self) -> None: ...
    def environment_data_interface(self) -> EM3000EnvironmentDataInterface: ...
    @typing.overload
    def get_pings(self) -> themachinethatgoesping.echosounders.em3000.filedatacontainers.EM3000PingContainer: ...
    @typing.overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders.em3000.filedatacontainers.EM3000PingContainer: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> EM3000NavigationDataInterface: ...
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
class EM3000PingDataInterfacePerFile():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> EM3000ConfigurationDataInterface: ...
    def configuration_data_interface_for_file(self) -> EM3000ConfigurationDataInterfacePerFile: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
    def environment_data_interface(self) -> EM3000EnvironmentDataInterface: ...
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
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def navigation_data_interface(self) -> EM3000NavigationDataInterface: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_pings(self) -> themachinethatgoesping.echosounders.em3000.filedatacontainers.EM3000PingContainer: ...
    pass
class EM3000PingDataInterfacePerFile_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> EM3000ConfigurationDataInterface_mapped: ...
    def configuration_data_interface_for_file(self) -> EM3000ConfigurationDataInterfacePerFile_mapped: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    def deinitialize(self) -> None: ...
    def environment_data_interface(self) -> EM3000EnvironmentDataInterface_mapped: ...
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
    def has_linked_file(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def init_from_file(self, force: bool = False) -> None: ...
    def initialized(self) -> bool: ...
    def is_primary_file(self) -> bool: ...
    def is_secondary_file(self) -> bool: ...
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def navigation_data_interface(self) -> EM3000NavigationDataInterface_mapped: ...
    def per_file(self) -> typing.List[EM3000DatagramInterface_mapped]: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_pings(self) -> themachinethatgoesping.echosounders.em3000.filedatacontainers.EM3000PingContainer_mapped: ...
    pass
class EM3000PingDataInterface_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def channel_ids(self) -> typing.List[str]: ...
    def configuration_data_interface(self) -> EM3000ConfigurationDataInterface_mapped: ...
    def deinitialize(self) -> None: ...
    def environment_data_interface(self) -> EM3000EnvironmentDataInterface_mapped: ...
    @typing.overload
    def get_pings(self) -> themachinethatgoesping.echosounders.em3000.filedatacontainers.EM3000PingContainer_mapped: ...
    @typing.overload
    def get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders.em3000.filedatacontainers.EM3000PingContainer_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_from_file(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_from_file(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def initialized(self) -> bool: ...
    def navigation_data_interface(self) -> EM3000NavigationDataInterface_mapped: ...
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
