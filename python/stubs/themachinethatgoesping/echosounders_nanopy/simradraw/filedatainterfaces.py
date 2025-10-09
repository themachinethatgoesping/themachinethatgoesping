"""
SimradRaw EK60 and EK80 file data interface classes
"""
from __future__ import annotations
import collections.abc
import themachinethatgoesping.echosounders_nanopy.simradraw
import themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams
import themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers
import themachinethatgoesping.navigation_nanopy
import typing
__all__: list[str] = ['SimradRawAnnotationDataInterface', 'SimradRawAnnotationDataInterfacePerFile', 'SimradRawAnnotationDataInterfacePerFile_stream', 'SimradRawAnnotationDataInterface_stream', 'SimradRawConfigurationDataInterface', 'SimradRawConfigurationDataInterfacePerFile', 'SimradRawConfigurationDataInterfacePerFile_stream', 'SimradRawConfigurationDataInterface_stream', 'SimradRawDatagramDataInterface', 'SimradRawDatagramDataInterfacePerFile', 'SimradRawDatagramDataInterfacePerFile_stream', 'SimradRawDatagramDataInterface_stream', 'SimradRawDatagramInterface', 'SimradRawDatagramInterface_stream', 'SimradRawEnvironmentDataInterface', 'SimradRawEnvironmentDataInterfacePerFile', 'SimradRawEnvironmentDataInterfacePerFile_stream', 'SimradRawEnvironmentDataInterface_stream', 'SimradRawNavigationDataInterface', 'SimradRawNavigationDataInterfacePerFile', 'SimradRawNavigationDataInterfacePerFile_stream', 'SimradRawNavigationDataInterface_stream', 'SimradRawOtherFileDataInterface', 'SimradRawOtherFileDataInterfacePerFile', 'SimradRawOtherFileDataInterfacePerFile_stream', 'SimradRawOtherFileDataInterface_stream', 'SimradRawPingDataInterface', 'SimradRawPingDataInterfacePerFile', 'SimradRawPingDataInterfacePerFile_stream', 'SimradRawPingDataInterface_stream']
class SimradRawAnnotationDataInterface:
    """
    Interface to read SimradRaw annotation data (TAG0) from a file
    (multiple files)
    
    Only sorts the supported datagrams. No caching is done. Gives access
    to SimradRawAnnotationDataInterfacePerFile using the per_file
    function.
    
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
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawAnnotationDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::SimradRawAnnotationDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawAnnotationDataInterfacePerFile``
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
class SimradRawAnnotationDataInterfacePerFile:
    """
    Interface to read annotation data (TAG0) from a file (per file)
    
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
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
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
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class SimradRawAnnotationDataInterfacePerFile_stream:
    """
    Interface to read annotation data (TAG0) from a file (per file)
    
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
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
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
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class SimradRawAnnotationDataInterface_stream:
    """
    Interface to read SimradRaw annotation data (TAG0) from a file
    (multiple files)
    
    Only sorts the supported datagrams. No caching is done. Gives access
    to SimradRawAnnotationDataInterfacePerFile using the per_file
    function.
    
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
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawAnnotationDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::SimradRawAnnotationDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawAnnotationDataInterfacePerFile_stream``
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
class SimradRawConfigurationDataInterface:
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
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawConfigurationDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::SimradRawConfigurationDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawConfigurationDataInterfacePerFile``
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
class SimradRawConfigurationDataInterfacePerFile:
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
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_attitude_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all attitude sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_configuration_datagram(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration:
        ...
    def get_depth_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all depth sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
        """
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
    def get_heading_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
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
    def get_position_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all position sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
        """
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
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration:
        ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation_nanopy.SensorConfiguration) -> None:
        ...
class SimradRawConfigurationDataInterfacePerFile_stream:
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
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def get_attitude_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all attitude sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_configuration_datagram(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration:
        ...
    def get_depth_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all depth sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
        """
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
    def get_heading_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
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
    def get_position_sources(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Sensor]:
        """
        Return all position sources registered in the configuration datagram
        (sorted by priority)
        
        Returns:
            std::vector<XML_Configuration_Sensor>
        """
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
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration:
        ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation_nanopy.SensorConfiguration) -> None:
        ...
class SimradRawConfigurationDataInterface_stream:
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
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawConfigurationDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::SimradRawConfigurationDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawConfigurationDataInterfacePerFile_stream``
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
class SimradRawDatagramDataInterface:
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
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawDatagramDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::SimradRawDatagramDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawDatagramDataInterfacePerFile``
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
class SimradRawDatagramDataInterfacePerFile:
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
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
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
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class SimradRawDatagramDataInterfacePerFile_stream:
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
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
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
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class SimradRawDatagramDataInterface_stream:
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
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawDatagramDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::SimradRawDatagramDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawDatagramDataInterfacePerFile_stream``
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
class SimradRawDatagramInterface:
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
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
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
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class SimradRawDatagramInterface_stream:
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
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
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
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class SimradRawEnvironmentDataInterface:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface:
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
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface:
        ...
    def per_file(self) -> list[...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawEnvironmentDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::SimradRawEnvironmentDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawEnvironmentDataInterfacePerFile``
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
class SimradRawEnvironmentDataInterfacePerFile:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface:
        ...
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
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
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class SimradRawEnvironmentDataInterfacePerFile_stream:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_stream:
        ...
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
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
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface_stream:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class SimradRawEnvironmentDataInterface_stream:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_stream:
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
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface_stream:
        ...
    def per_file(self) -> list[..., ...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawEnvironmentDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::SimradRawEnvironmentDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawEnvironmentDataInterfacePerFile_stream``
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
class SimradRawNavigationDataInterface:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface:
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
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawNavigationDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::SimradRawNavigationDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawNavigationDataInterfacePerFile``
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
    def set_max_gga_quality(self, max_gga_quality: int) -> None:
        ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None:
        ...
    def set_navigation_interpolator(self, sensor_configuration_hash: int, navigation_interpolator: themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon) -> None:
        ...
    def set_navigation_interpolators(self, navigation_interpolators: collections.abc.Mapping[int, ..., ..., ..., ..., ..., ...]) -> None:
        ...
    def verify_linked_file_interfaces_are_consistent(self) -> None:
        """
        This functions throws if linked file interfaces are not consistent
        """
class SimradRawNavigationDataInterfacePerFile:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface:
        ...
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
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
    def get_max_gga_quality(self) -> int:
        ...
    def get_min_gga_quality(self) -> int:
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
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon:
        ...
    def set_max_gga_quality(self, max_gga_quality: int) -> None:
        ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None:
        ...
class SimradRawNavigationDataInterfacePerFile_stream:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_stream:
        ...
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
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
    def get_max_gga_quality(self) -> int:
        ...
    def get_min_gga_quality(self) -> int:
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
    def is_initialized(self) -> bool:
        ...
    def is_primary_file(self) -> bool:
        ...
    def is_secondary_file(self) -> bool:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def read_navigation_data(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon:
        ...
    def set_max_gga_quality(self, max_gga_quality: int) -> None:
        ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None:
        ...
class SimradRawNavigationDataInterface_stream:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_stream:
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
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawNavigationDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::SimradRawNavigationDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawNavigationDataInterfacePerFile_stream``
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
    def set_max_gga_quality(self, max_gga_quality: int) -> None:
        ...
    def set_min_gga_quality(self, min_gga_quality: int) -> None:
        ...
    def set_navigation_interpolator(self, sensor_configuration_hash: int, navigation_interpolator: themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon) -> None:
        ...
    def set_navigation_interpolators(self, navigation_interpolators: collections.abc.Mapping[int, ..., ..., ..., ..., ..., ...]) -> None:
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
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawOtherFileDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::init_c_simradrawotherfiledatainterfaceperfile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawOtherFileDataInterfacePerFile``
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
class SimradRawOtherFileDataInterfacePerFile:
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
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
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
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class SimradRawOtherFileDataInterfacePerFile_stream:
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
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
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
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class SimradRawOtherFileDataInterface_stream:
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
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawOtherFileDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::init_c_simradrawotherfiledatainterfaceperfile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawOtherFileDataInterfacePerFile_stream``
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
class SimradRawPingDataInterface:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface:
        ...
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def environment_data_interface(self) -> SimradRawEnvironmentDataInterface:
        ...
    def get_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers.SimradRawPingContainer:
        """
        get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers.SimradRawPingContainer
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
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface:
        ...
    def per_file(self) -> list[...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawPingDataInterfacePerFile
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::SimradRawPingDataInterfacePerFile<themachinethatgoesping::echosounders::filetemplates::datastreams::MappedFileStream> >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawPingDataInterfacePerFile``
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
class SimradRawPingDataInterfacePerFile:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface:
        ...
    def configuration_data_interface_for_file(self) -> SimradRawConfigurationDataInterfacePerFile:
        ...
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def environment_data_interface(self) -> SimradRawEnvironmentDataInterface:
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
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def read_pings(self, index_paths: collections.abc.Mapping[str, str] = {}) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers.SimradRawPingContainer:
        ...
class SimradRawPingDataInterfacePerFile_stream:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_stream:
        ...
    def configuration_data_interface_for_file(self) -> SimradRawConfigurationDataInterfacePerFile_stream:
        ...
    def datagram_headers(self) -> typing.Any:
        """
        datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def datagrams(self, skip_data: bool = False) -> typing.Any:
        """
        datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier, skip_data: bool = False) -> object
        """
    def datagrams_raw(self) -> typing.Any:
        """
        datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier) -> object
        """
    def deinitialize(self) -> None:
        ...
    def environment_data_interface(self) -> SimradRawEnvironmentDataInterface_stream:
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
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface_stream:
        ...
    def per_file(self) -> list[SimradRawDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def read_pings(self, index_paths: collections.abc.Mapping[str, str] = {}) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers.SimradRawPingContainer_stream:
        ...
class SimradRawPingDataInterface_stream:
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
    def configuration_data_interface(self) -> SimradRawConfigurationDataInterface_stream:
        ...
    def deinitialize(self) -> None:
        """
        deinitialize(self) -> None
        """
    def environment_data_interface(self) -> SimradRawEnvironmentDataInterface_stream:
        ...
    def get_channel_ids(self) -> list[str]:
        ...
    def get_pings(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers.SimradRawPingContainer_stream:
        """
        get_pings(self, channel_id: str) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatacontainers.SimradRawPingContainer_stream
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
    def navigation_data_interface(self) -> SimradRawNavigationDataInterface_stream:
        ...
    def per_file(self) -> list[..., ...]:
        """
        per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawPingDataInterfacePerFile_stream
        
        Overloaded function.
        
        1. ``per_file(self) -> list[std::shared_ptr<themachinethatgoesping::echosounders::simradraw::filedatainterfaces::SimradRawPingDataInterfacePerFile<std::basic_ifstream<char, std::char_traits<char> > > >]``
        
        get a vector with references to the per file interfaces This is useful
        for iterating over all files
        
        Returns:
            std::vector<t_filedatainterface_perfile&>
        
        2. ``per_file(self, file_nr: int) -> themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawPingDataInterfacePerFile_stream``
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
