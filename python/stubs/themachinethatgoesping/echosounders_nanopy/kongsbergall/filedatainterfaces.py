"""
KongsbergAll (kongsberg .all/.wcd) file data interface classes
"""
from __future__ import annotations
import collections.abc
import themachinethatgoesping.echosounders_nanopy
import themachinethatgoesping.echosounders_nanopy.kongsbergall
import themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams
import themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers
import themachinethatgoesping.navigation_nanopy
import typing
__all__: list[str] = ['KongsbergAllAnnotationDataInterface', 'KongsbergAllAnnotationDataInterfacePerFile', 'KongsbergAllAnnotationDataInterfacePerFile_stream', 'KongsbergAllAnnotationDataInterface_stream', 'KongsbergAllConfigurationDataInterface', 'KongsbergAllConfigurationDataInterfacePerFile', 'KongsbergAllConfigurationDataInterfacePerFile_stream', 'KongsbergAllConfigurationDataInterface_stream', 'KongsbergAllDatagramDataInterface', 'KongsbergAllDatagramDataInterfacePerFile', 'KongsbergAllDatagramDataInterfacePerFile_stream', 'KongsbergAllDatagramDataInterface_stream', 'KongsbergAllDatagramInterface', 'KongsbergAllDatagramInterface_stream', 'KongsbergAllEnvironmentDataInterface', 'KongsbergAllEnvironmentDataInterfacePerFile', 'KongsbergAllEnvironmentDataInterfacePerFile_stream', 'KongsbergAllEnvironmentDataInterface_stream', 'KongsbergAllNavigationDataInterface', 'KongsbergAllNavigationDataInterfacePerFile', 'KongsbergAllNavigationDataInterfacePerFile_stream', 'KongsbergAllNavigationDataInterface_stream', 'KongsbergAllOtherFileDataInterface', 'KongsbergAllOtherFileDataInterfacePerFile', 'KongsbergAllOtherFileDataInterfacePerFile_stream', 'KongsbergAllOtherFileDataInterface_stream', 'KongsbergAllPingDataInterface', 'KongsbergAllPingDataInterfacePerFile', 'KongsbergAllPingDataInterfacePerFile_stream', 'KongsbergAllPingDataInterface_stream']
class KongsbergAllAnnotationDataInterface:
    """
    Interface to read annotation data (no kongsberg datagram is currently
    supported) from a file (multiple files)
    
    Only sorts the supported datagrams. No caching is done. Gives access
    to AnnotationDataInterfacePerFile using the per_file function.
    
    Template parameter ``t_ifstream``:
    """
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def per_file(self) -> list[...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllAnnotationDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllAnnotationDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllAnnotationDataInterfacePerFile``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class KongsbergAllAnnotationDataInterfacePerFile_stream:
    """
    Interface to read annotation data (no kongsberg datagram is currently
    supported) from a file (per file)
    
    This class can be accessed using the per_file function of the
    AnnotationDataInterface.
    
    Template parameter ``t_ifstream``:
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class KongsbergAllAnnotationDataInterface_stream:
    """
    Interface to read annotation data (no kongsberg datagram is currently
    supported) from a file (multiple files)
    
    Only sorts the supported datagrams. No caching is done. Gives access
    to AnnotationDataInterfacePerFile using the per_file function.
    
    Template parameter ``t_ifstream``:
    """
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def per_file(self) -> list[..., ...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllAnnotationDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllAnnotationDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllAnnotationDataInterfacePerFile_stream``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def get_sensor_configuration(self, index: int) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration:
        ...
    def get_trx_sensor_configuration_per_target_id(self, index: int) -> dict:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def per_file(self) -> list[...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllConfigurationDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllConfigurationDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllConfigurationDataInterfacePerFile``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_active_heading_sensor(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor:
        ...
    def get_active_heave_sensor(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor:
        ...
    def get_active_pitch_roll_sensor(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor:
        ...
    def get_active_position_system_number(self) -> int:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_runtime_parameters(self, system_serial_number: int, ping_counter: int, ping_time: float, last_index: int = 0) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters:
        ...
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration:
        ...
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def init_runtime_parameters(self) -> None:
        """
        read the runtime parameters from the file and save them in the
        internal map This function is automatically called by
        get_runtime_parameters
        """
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def read_installation_parameters(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters:
        """
        Read the installation parameters from the file, this function also
        checks if the start and end parameters are the same
        
        Returns:
            datagrams::InstallationParameters
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration:
        ...
    def set_active_heading_sensor(self, sensor: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> None:
        """
        Set the active heading sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        o_KongsbergAllActiveSensor
        
        Parameter ``sensor``:
        """
    def set_active_heave_sensor(self, sensor: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> None:
        """
        Set the active heave sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        o_KongsbergAllActiveSensor
        
        Parameter ``sensor``:
        """
    def set_active_pitch_roll_sensor(self, sensor: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> None:
        """
        Set the active roll pitch sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        o_KongsbergAllActiveSensor
        
        Parameter ``sensor``:
        """
    def set_active_position_system_number(self, number: int) -> None:
        """
        Set the active position system number 0: this will be overwritten by
        "read_sensor_configuration" / "init_interface" 1-3: position system
        1-3
        
        Parameter ``number``:
        """
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation_nanopy.SensorConfiguration) -> None:
        ...
class KongsbergAllConfigurationDataInterfacePerFile_stream:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_active_heading_sensor(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor:
        ...
    def get_active_heave_sensor(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor:
        ...
    def get_active_pitch_roll_sensor(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor:
        ...
    def get_active_position_system_number(self) -> int:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_runtime_parameters(self, system_serial_number: int, ping_counter: int, ping_time: float, last_index: int = 0) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters:
        ...
    def get_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration:
        ...
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def init_runtime_parameters(self) -> None:
        """
        read the runtime parameters from the file and save them in the
        internal map This function is automatically called by
        get_runtime_parameters
        """
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def read_installation_parameters(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.InstallationParameters:
        """
        Read the installation parameters from the file, this function also
        checks if the start and end parameters are the same
        
        Returns:
            datagrams::InstallationParameters
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration:
        ...
    def set_active_heading_sensor(self, sensor: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> None:
        """
        Set the active heading sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        o_KongsbergAllActiveSensor
        
        Parameter ``sensor``:
        """
    def set_active_heave_sensor(self, sensor: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> None:
        """
        Set the active heave sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        o_KongsbergAllActiveSensor
        
        Parameter ``sensor``:
        """
    def set_active_pitch_roll_sensor(self, sensor: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> None:
        """
        Set the active roll pitch sensor "NotSet": this will be overwritten by
        "read_sensor_configuration" / "init_interface" All other values: see
        o_KongsbergAllActiveSensor
        
        Parameter ``sensor``:
        """
    def set_active_position_system_number(self, number: int) -> None:
        """
        Set the active position system number 0: this will be overwritten by
        "read_sensor_configuration" / "init_interface" 1-3: position system
        1-3
        
        Parameter ``number``:
        """
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation_nanopy.SensorConfiguration) -> None:
        ...
class KongsbergAllConfigurationDataInterface_stream:
    """
    """
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def get_sensor_configuration(self, index: int) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration:
        ...
    def get_trx_sensor_configuration_per_target_id(self, index: int) -> dict:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def per_file(self) -> list[..., ...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllConfigurationDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllConfigurationDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllConfigurationDataInterfacePerFile_stream``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def per_file(self) -> list[...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllDatagramDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllDatagramDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllDatagramDataInterfacePerFile``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class KongsbergAllDatagramDataInterfacePerFile_stream:
    """
    FileDataInterface (for single files) for packages that fit neither of
    the other FileDataInterfaces (Configuration, Navigation, Annotation,
    Environment, Ping)
    
    No datagram caching is implemented for this interface. Accessed
    packages are always read from file
    
    Template parameter ``t_ifstream``:
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class KongsbergAllDatagramDataInterface_stream:
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Annotation, Environment, Ping)
    
    No datagram caching is implemented for this interface. Accessed
    packages are always read from file
    
    Template parameter ``t_ifstream``:
    """
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def per_file(self) -> list[..., ...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllDatagramDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllDatagramDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllDatagramDataInterfacePerFile_stream``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class KongsbergAllDatagramInterface_stream:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class KongsbergAllEnvironmentDataInterface:
    """
    """
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
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
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface:
        ...
    def per_file(self) -> list[...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllEnvironmentDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllEnvironmentDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllEnvironmentDataInterfacePerFile``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
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
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class KongsbergAllEnvironmentDataInterfacePerFile_stream:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_stream:
        ...
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface_stream:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class KongsbergAllEnvironmentDataInterface_stream:
    """
    """
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_stream:
        ...
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface_stream:
        ...
    def per_file(self) -> list[..., ...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllEnvironmentDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllEnvironmentDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllEnvironmentDataInterfacePerFile_stream``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
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
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def get_channel_ids(self) -> list[str]:
        """
        get_channel_ids(self, sensor_configuration_hash: int) -> list[str]
        """
    def get_navigation_interpolator(self, sensor_configuration: int) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon:
        ...
    def get_navigation_interpolator_keys(self) -> list[int]:
        ...
    def has_navigation_interpolator(self, sensor_configuration_hash: int) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def per_file(self) -> list[...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllNavigationDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllNavigationDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllNavigationDataInterfacePerFile``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_navigation_interpolator(self, sensor_configuration_hash: int, navigation_interpolator: themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon) -> None:
        ...
    def set_navigation_interpolators(self, navigation_interpolators: collections.abc.Mapping[int, ..., ..., ..., ..., ..., ...]) -> None:
        ...
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class KongsbergAllNavigationDataInterfacePerFile:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
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
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon:
        ...
class KongsbergAllNavigationDataInterfacePerFile_stream:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_stream:
        ...
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon:
        ...
class KongsbergAllNavigationDataInterface_stream:
    """
    """
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_stream:
        ...
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def get_channel_ids(self) -> list[str]:
        """
        get_channel_ids(self, sensor_configuration_hash: int) -> list[str]
        """
    def get_navigation_interpolator(self, sensor_configuration: int) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon:
        ...
    def get_navigation_interpolator_keys(self) -> list[int]:
        ...
    def has_navigation_interpolator(self, sensor_configuration_hash: int) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def per_file(self) -> list[..., ...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllNavigationDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllNavigationDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllNavigationDataInterfacePerFile_stream``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_navigation_interpolator(self, sensor_configuration_hash: int, navigation_interpolator: themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon) -> None:
        ...
    def set_navigation_interpolators(self, navigation_interpolators: collections.abc.Mapping[int, ..., ..., ..., ..., ..., ...]) -> None:
        ...
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
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def per_file(self) -> list[...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllOtherFileDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllOtherFileDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllOtherFileDataInterfacePerFile``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class KongsbergAllOtherFileDataInterfacePerFile_stream:
    """
    FileDataInterface (for single files) for packages that fit neither of
    the other FileDataInterfaces (Configuration, Navigation, Annotation,
    Environment, Ping)
    
    No datagram caching is implemented for this interface. Accessed
    packages are always read from file
    
    Template parameter ``t_ifstream``:
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class KongsbergAllOtherFileDataInterface_stream:
    """
    FileDataInterface (for multiple files) for packages that fit neither
    of the other FileDataInterfaces (Configuration, Navigation,
    Annotation, Environment, Ping)
    
    No datagram caching is implemented for this interface. Accessed
    packages are always read from file
    
    Template parameter ``t_ifstream``:
    """
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def per_file(self) -> list[..., ...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllOtherFileDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllOtherFileDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllOtherFileDataInterfacePerFile_stream``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
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
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def environment_data_interface(self) -> KongsbergAllEnvironmentDataInterface:
        ...
    def get_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer:
        """
        get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface:
        ...
    def per_file(self) -> list[...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllPingDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllPingDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllPingDataInterfacePerFile``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
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
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
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
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def environment_data_interface(self) -> KongsbergAllEnvironmentDataInterface:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def read_pings(self, index_paths: collections.abc.Mapping[str, str] = {}) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer:
        ...
class KongsbergAllPingDataInterfacePerFile_stream:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_stream:
        ...
    def configuration_data_interface_for_file(self) -> KongsbergAllConfigurationDataInterfacePerFile_stream:
        ...
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def environment_data_interface(self) -> KongsbergAllEnvironmentDataInterface_stream:
        ...
    def get_file_name(self) -> str:
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
    def get_file_size(self) -> int:
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
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def has_linked_file(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_path: str = '', force: bool = False) -> None:
        ...
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface_stream:
        ...
    def per_file(self) -> list[KongsbergAllDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def read_pings(self, index_paths: collections.abc.Mapping[str, str] = {}) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer_stream:
        ...
class KongsbergAllPingDataInterface_stream:
    """
    """
    sort_by_time: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def configuration_data_interface(self) -> KongsbergAllConfigurationDataInterface_stream:
        ...
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def environment_data_interface(self) -> KongsbergAllEnvironmentDataInterface_stream:
        ...
    def get_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer_stream:
        """
        get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatacontainers.KongsbergAllPingContainer_stream
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_from_file(self, index_paths: collections.abc.Mapping[str, str] = {}, force: bool = False, show_progress: bool = True) -> None:
        """
        init_from_file(self, index_paths: collections.abc.Mapping[str, str], force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, external_progress_tick: bool = False) -> None
        """
    def is_initialized(self) -> bool:
        """
        is_initialized(self) -> bool
        """
    def navigation_data_interface(self) -> KongsbergAllNavigationDataInterface_stream:
        ...
    def per_file(self) -> list[..., ...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllPingDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::kongsbergall::filedatainterfaces::KongsbergAllPingDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllPingDataInterfacePerFile_stream``
        """
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
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
