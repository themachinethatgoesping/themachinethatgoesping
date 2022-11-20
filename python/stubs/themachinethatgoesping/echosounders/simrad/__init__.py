"""Classes related to Simrad EK60 and EK80 data files"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad
import typing
import numpy
import themachinethatgoesping.navigation
import themachinethatgoesping.tools.progressbars
import themachinethatgoesping.tools.pyhelper
_Shape = typing.Tuple[int, ...]

__all__ = [
    "FIL1",
    "FileSimradRaw",
    "FileSimradRaw_mapped",
    "MRU0",
    "NME0",
    "RAW3",
    "SimradAnnotationDataInterface",
    "SimradAnnotationDataInterface_mapped",
    "SimradConfigurationDataCollection",
    "SimradConfigurationDataCollection_mapped",
    "SimradConfigurationDataInterface",
    "SimradConfigurationDataInterface_mapped",
    "SimradDatagramInterface",
    "SimradDatagramInterface_mapped",
    "SimradDatagram_type_from_string",
    "SimradEnvironmentDataInterface",
    "SimradEnvironmentDataInterface_mapped",
    "SimradNavigationDataInterface",
    "SimradNavigationDataInterface_mapped",
    "SimradOtherDataInterface",
    "SimradOtherDataInterface_mapped",
    "SimradPing",
    "SimradPingContainer",
    "SimradPingContainer_mapped",
    "SimradPing_RawData",
    "SimradPing_mapped",
    "SimradPing_mapped_RawData",
    "SimradRawDatagramContainer_FIL1",
    "SimradRawDatagramContainer_FIL1_mapped",
    "SimradRawDatagramContainer_Header",
    "SimradRawDatagramContainer_Header_mapped",
    "SimradRawDatagramContainer_MRU0",
    "SimradRawDatagramContainer_MRU0_mapped",
    "SimradRawDatagramContainer_NME0",
    "SimradRawDatagramContainer_NME0_mapped",
    "SimradRawDatagramContainer_RAW3",
    "SimradRawDatagramContainer_RAW3_header",
    "SimradRawDatagramContainer_RAW3_header_mapped",
    "SimradRawDatagramContainer_RAW3_mapped",
    "SimradRawDatagramContainer_TAG0",
    "SimradRawDatagramContainer_TAG0_mapped",
    "SimradRawDatagramContainer_Unknown",
    "SimradRawDatagramContainer_Unknown_mapped",
    "SimradRawDatagramContainer_Variant",
    "SimradRawDatagramContainer_Variant_mapped",
    "SimradRawDatagramContainer_XML0",
    "SimradRawDatagramContainer_XML0_mapped",
    "TAG0",
    "XML0",
    "datagram_type_to_string",
    "datagrams",
    "t_SimradDatagramIdentifier",
    "test_speed_decode_nmea",
    "test_speed_decode_xml",
    "test_speed_header",
    "test_speed_raw",
    "test_speed_raw_all",
    "test_speed_type"
]


class FileSimradRaw():
    @typing.overload
    def __init__(self, file_path: str, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def __init__(self, file_path: str, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_path: typing.List[str], show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_paths: typing.List[str], progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def append_file(self, file_path: str, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def append_file(self, file_path: str, show_progress: bool = True) -> None: ...
    @typing.overload
    def append_files(self, file_path: typing.List[str], progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def append_files(self, file_path: typing.List[str], show_progress: bool = True) -> None: ...
    def channel_ids(self) -> typing.List[str]: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def pings(self) -> SimradPingContainer: ...
    @typing.overload
    def pings(self, channel_id: str) -> SimradPingContainer: ...
    @typing.overload
    def pings(self, channel_ids: typing.List[str]) -> SimradPingContainer: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> SimradAnnotationDataInterface:
        """
        :type: SimradAnnotationDataInterface
        """
    @property
    def configuration_interface(self) -> SimradConfigurationDataInterface:
        """
        :type: SimradConfigurationDataInterface
        """
    @property
    def datagram_interface(self) -> SimradDatagramInterface:
        """
        :type: SimradDatagramInterface
        """
    @property
    def environment_interface(self) -> SimradEnvironmentDataInterface:
        """
        :type: SimradEnvironmentDataInterface
        """
    @property
    def i_Pings(self) -> SimradPingContainer:
        """
        :type: SimradPingContainer
        """
    @property
    def navigation_interface(self) -> SimradNavigationDataInterface:
        """
        :type: SimradNavigationDataInterface
        """
    @property
    def otherdata_interface(self) -> SimradOtherDataInterface:
        """
        :type: SimradOtherDataInterface
        """
    pass
class FileSimradRaw_mapped():
    @typing.overload
    def __init__(self, file_path: str, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def __init__(self, file_path: str, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_path: typing.List[str], show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_paths: typing.List[str], progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def append_file(self, file_path: str, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def append_file(self, file_path: str, show_progress: bool = True) -> None: ...
    @typing.overload
    def append_files(self, file_path: typing.List[str], progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def append_files(self, file_path: typing.List[str], show_progress: bool = True) -> None: ...
    def channel_ids(self) -> typing.List[str]: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def pings(self) -> SimradPingContainer_mapped: ...
    @typing.overload
    def pings(self, channel_id: str) -> SimradPingContainer_mapped: ...
    @typing.overload
    def pings(self, channel_ids: typing.List[str]) -> SimradPingContainer_mapped: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> SimradAnnotationDataInterface_mapped:
        """
        :type: SimradAnnotationDataInterface_mapped
        """
    @property
    def configuration_interface(self) -> SimradConfigurationDataInterface_mapped:
        """
        :type: SimradConfigurationDataInterface_mapped
        """
    @property
    def datagram_interface(self) -> SimradDatagramInterface_mapped:
        """
        :type: SimradDatagramInterface_mapped
        """
    @property
    def environment_interface(self) -> SimradEnvironmentDataInterface_mapped:
        """
        :type: SimradEnvironmentDataInterface_mapped
        """
    @property
    def i_Pings(self) -> SimradPingContainer_mapped:
        """
        :type: SimradPingContainer_mapped
        """
    @property
    def navigation_interface(self) -> SimradNavigationDataInterface_mapped:
        """
        :type: SimradNavigationDataInterface_mapped
        """
    @property
    def otherdata_interface(self) -> SimradOtherDataInterface_mapped:
        """
        :type: SimradOtherDataInterface_mapped
        """
    pass
class SimradAnnotationDataInterface():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def per_file(self) -> typing.List[SimradDatagramInterface]:
        """
        :type: typing.List[SimradDatagramInterface]
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def per_file(self) -> typing.List[SimradDatagramInterface_mapped]:
        """
        :type: typing.List[SimradDatagramInterface_mapped]
        """
    pass
class SimradConfigurationDataCollection():
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
    def datagram_headers(self, datagram_type: t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: t_SimradDatagramIdentifier) -> object: ...
    def get_attitude_sources(self) -> typing.List[datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all attitude sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_configuration_datagram(self) -> datagrams.XML0_datagrams.XML_Configuration: ...
    def get_depth_sources(self) -> typing.List[datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all depth sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_heading_sources(self) -> typing.List[datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all heading sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_position_sources(self) -> typing.List[datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
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
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
    pass
class SimradConfigurationDataCollection_mapped():
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
    def datagram_headers(self, datagram_type: t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: t_SimradDatagramIdentifier) -> object: ...
    def get_attitude_sources(self) -> typing.List[datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all attitude sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_configuration_datagram(self) -> datagrams.XML0_datagrams.XML_Configuration: ...
    def get_depth_sources(self) -> typing.List[datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all depth sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_heading_sources(self) -> typing.List[datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
        """
        Return all heading sources registered in the configuration datagram
        (sorted by priority)

        Returns:
            std::vector<XML_Configuration_Sensor>
        """
    def get_position_sources(self) -> typing.List[datagrams.XML0_datagrams.XML_Configuration_Sensor]: 
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
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def read_sensor_configuration(self) -> themachinethatgoesping.navigation.SensorConfiguration: ...
    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation.SensorConfiguration) -> None: ...
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def per_file(self) -> typing.List[SimradConfigurationDataCollection]:
        """
        :type: typing.List[SimradConfigurationDataCollection]
        """
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def per_file(self) -> typing.List[SimradConfigurationDataCollection_mapped]:
        """
        :type: typing.List[SimradConfigurationDataCollection_mapped]
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
    def datagram_headers(self, datagram_type: t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: t_SimradDatagramIdentifier) -> object: ...
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
    def datagram_headers(self, datagram_type: t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: t_SimradDatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: t_SimradDatagramIdentifier) -> object: ...
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def per_file(self) -> typing.List[SimradDatagramInterface]:
        """
        :type: typing.List[SimradDatagramInterface]
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def per_file(self) -> typing.List[SimradDatagramInterface_mapped]:
        """
        :type: typing.List[SimradDatagramInterface_mapped]
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def per_file(self) -> typing.List[SimradDatagramInterface]:
        """
        :type: typing.List[SimradDatagramInterface]
        """
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def per_file(self) -> typing.List[SimradDatagramInterface_mapped]:
        """
        :type: typing.List[SimradDatagramInterface_mapped]
        """
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def per_file(self) -> typing.List[SimradDatagramInterface]:
        """
        :type: typing.List[SimradDatagramInterface]
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
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def per_file(self) -> typing.List[SimradDatagramInterface_mapped]:
        """
        :type: typing.List[SimradDatagramInterface_mapped]
        """
    pass
class SimradPing():
    def get_angle(self) -> numpy.ndarray[numpy.float32]: ...
    def get_channel_id(self) -> str: ...
    def get_number_of_samples(self) -> int: ...
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_timestamp(self) -> float: ...
    def load_data(self) -> None: ...
    def raw(self) -> SimradPing_RawData: ...
    def release_data(self) -> None: ...
    pass
class SimradPingContainer():
    @typing.overload
    def __call__(self, channel_id: str) -> SimradPingContainer: ...
    @typing.overload
    def __call__(self, channel_ids: typing.List[str]) -> SimradPingContainer: ...
    def __copy__(self) -> SimradPingContainer: ...
    def __deepcopy__(self, arg0: dict) -> SimradPingContainer: ...
    @typing.overload
    def __getitem__(self, index: int) -> SimradPing: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradPingContainer: ...
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new empty PingContainer object

        Construct a new empty PingContainer object
        """
    @typing.overload
    def __init__(self, arg0: typing.List[SimradPing]) -> None: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradPingContainer: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradPingContainer]: ...
    def copy(self) -> SimradPingContainer: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_pings_per_channel_id(self) -> typing.Dict[str, int]: ...
    def find_channel_ids(self) -> typing.List[str]: ...
    def get_sorted_by_time(self) -> SimradPingContainer: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def max_number_of_samples(self) -> int: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradPingContainer_mapped():
    @typing.overload
    def __call__(self, channel_id: str) -> SimradPingContainer_mapped: ...
    @typing.overload
    def __call__(self, channel_ids: typing.List[str]) -> SimradPingContainer_mapped: ...
    def __copy__(self) -> SimradPingContainer_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradPingContainer_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> SimradPing_mapped: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradPingContainer_mapped: ...
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new empty PingContainer object

        Construct a new empty PingContainer object
        """
    @typing.overload
    def __init__(self, arg0: typing.List[SimradPing_mapped]) -> None: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradPingContainer_mapped: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradPingContainer_mapped]: ...
    def copy(self) -> SimradPingContainer_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_pings_per_channel_id(self) -> typing.Dict[str, int]: ...
    def find_channel_ids(self) -> typing.List[str]: ...
    def get_sorted_by_time(self) -> SimradPingContainer_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def max_number_of_samples(self) -> int: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradPing_RawData():
    def get_parameter(self) -> datagrams.XML0_datagrams.XML_Parameter_Channel: ...
    def get_sample_data(self) -> typing.Union[datagrams.RAW3_datatypes.RAW3_DataSkipped, datagrams.RAW3_datatypes.RAW3_DataComplexFloat32, datagrams.RAW3_datatypes.RAW3_DataPowerAndAngle, datagrams.RAW3_datatypes.RAW3_DataPower, datagrams.RAW3_datatypes.RAW3_DataAngle]: ...
    def load_data(self) -> None: ...
    def release_data(self) -> None: ...
    @property
    def ping_data(self) -> datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)

        :type: datagrams.RAW3
        """
    pass
class SimradPing_mapped():
    def get_angle(self) -> numpy.ndarray[numpy.float32]: ...
    def get_channel_id(self) -> str: ...
    def get_number_of_samples(self) -> int: ...
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_timestamp(self) -> float: ...
    def load_data(self) -> None: ...
    def raw(self) -> SimradPing_mapped_RawData: ...
    def release_data(self) -> None: ...
    pass
class SimradPing_mapped_RawData():
    def get_parameter(self) -> datagrams.XML0_datagrams.XML_Parameter_Channel: ...
    def get_sample_data(self) -> typing.Union[datagrams.RAW3_datatypes.RAW3_DataSkipped, datagrams.RAW3_datatypes.RAW3_DataComplexFloat32, datagrams.RAW3_datatypes.RAW3_DataPowerAndAngle, datagrams.RAW3_datatypes.RAW3_DataPower, datagrams.RAW3_datatypes.RAW3_DataAngle]: ...
    def load_data(self) -> None: ...
    def release_data(self) -> None: ...
    @property
    def ping_data(self) -> datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)

        :type: datagrams.RAW3
        """
    pass
class SimradRawDatagramContainer_FIL1():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_FIL1: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_FIL1: ...
    def __copy__(self) -> SimradRawDatagramContainer_FIL1: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_FIL1: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.FIL1: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_FIL1: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_FIL1: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_FIL1]: ...
    def copy(self) -> SimradRawDatagramContainer_FIL1: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_FIL1: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_FIL1_mapped():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_FIL1_mapped: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_FIL1_mapped: ...
    def __copy__(self) -> SimradRawDatagramContainer_FIL1_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_FIL1_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.FIL1: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_FIL1_mapped: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_FIL1_mapped: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_FIL1_mapped]: ...
    def copy(self) -> SimradRawDatagramContainer_FIL1_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_FIL1_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_Header():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Header: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Header: ...
    def __copy__(self) -> SimradRawDatagramContainer_Header: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Header: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.SimradDatagram: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Header: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Header: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_Header]: ...
    def copy(self) -> SimradRawDatagramContainer_Header: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Header: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_Header_mapped():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Header_mapped: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Header_mapped: ...
    def __copy__(self) -> SimradRawDatagramContainer_Header_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Header_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.SimradDatagram: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Header_mapped: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Header_mapped: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_Header_mapped]: ...
    def copy(self) -> SimradRawDatagramContainer_Header_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Header_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_MRU0():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_MRU0: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_MRU0: ...
    def __copy__(self) -> SimradRawDatagramContainer_MRU0: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_MRU0: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.MRU0: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_MRU0: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_MRU0: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_MRU0]: ...
    def copy(self) -> SimradRawDatagramContainer_MRU0: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_MRU0: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_MRU0_mapped():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_MRU0_mapped: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_MRU0_mapped: ...
    def __copy__(self) -> SimradRawDatagramContainer_MRU0_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_MRU0_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.MRU0: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_MRU0_mapped: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_MRU0_mapped: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_MRU0_mapped]: ...
    def copy(self) -> SimradRawDatagramContainer_MRU0_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_MRU0_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_NME0():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_NME0: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_NME0: ...
    def __copy__(self) -> SimradRawDatagramContainer_NME0: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_NME0: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.NME0: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_NME0: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_NME0: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_NME0]: ...
    def copy(self) -> SimradRawDatagramContainer_NME0: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_NME0: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_NME0_mapped():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_NME0_mapped: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_NME0_mapped: ...
    def __copy__(self) -> SimradRawDatagramContainer_NME0_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_NME0_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.NME0: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_NME0_mapped: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_NME0_mapped: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_NME0_mapped]: ...
    def copy(self) -> SimradRawDatagramContainer_NME0_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_NME0_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_RAW3():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_RAW3: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3: ...
    def __copy__(self) -> SimradRawDatagramContainer_RAW3: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_RAW3: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.RAW3: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_RAW3: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_RAW3]: ...
    def copy(self) -> SimradRawDatagramContainer_RAW3: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_RAW3_header():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_RAW3_header: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3_header: ...
    def __copy__(self) -> SimradRawDatagramContainer_RAW3_header: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_RAW3_header: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.RAW3: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3_header: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_RAW3_header: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_RAW3_header]: ...
    def copy(self) -> SimradRawDatagramContainer_RAW3_header: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3_header: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_RAW3_header_mapped():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_RAW3_header_mapped: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3_header_mapped: ...
    def __copy__(self) -> SimradRawDatagramContainer_RAW3_header_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_RAW3_header_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.RAW3: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3_header_mapped: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_RAW3_header_mapped: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_RAW3_header_mapped]: ...
    def copy(self) -> SimradRawDatagramContainer_RAW3_header_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3_header_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_RAW3_mapped():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_RAW3_mapped: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_RAW3_mapped: ...
    def __copy__(self) -> SimradRawDatagramContainer_RAW3_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_RAW3_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.RAW3: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_RAW3_mapped: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_RAW3_mapped: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_RAW3_mapped]: ...
    def copy(self) -> SimradRawDatagramContainer_RAW3_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_RAW3_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_TAG0():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_TAG0: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_TAG0: ...
    def __copy__(self) -> SimradRawDatagramContainer_TAG0: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_TAG0: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.TAG0: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_TAG0: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_TAG0: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_TAG0]: ...
    def copy(self) -> SimradRawDatagramContainer_TAG0: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_TAG0: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_TAG0_mapped():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_TAG0_mapped: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_TAG0_mapped: ...
    def __copy__(self) -> SimradRawDatagramContainer_TAG0_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_TAG0_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.TAG0: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_TAG0_mapped: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_TAG0_mapped: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_TAG0_mapped]: ...
    def copy(self) -> SimradRawDatagramContainer_TAG0_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_TAG0_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_Unknown():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Unknown: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Unknown: ...
    def __copy__(self) -> SimradRawDatagramContainer_Unknown: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Unknown: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.SimradUnknown: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Unknown: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Unknown: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_Unknown]: ...
    def copy(self) -> SimradRawDatagramContainer_Unknown: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Unknown: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_Unknown_mapped():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Unknown_mapped: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Unknown_mapped: ...
    def __copy__(self) -> SimradRawDatagramContainer_Unknown_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Unknown_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.SimradUnknown: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Unknown_mapped: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Unknown_mapped: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_Unknown_mapped]: ...
    def copy(self) -> SimradRawDatagramContainer_Unknown_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Unknown_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_Variant():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Variant: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Variant: ...
    def __copy__(self) -> SimradRawDatagramContainer_Variant: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Variant: ...
    @typing.overload
    def __getitem__(self, index: int) -> typing.Union[datagrams.SimradDatagram, datagrams.NME0, datagrams.XML0, datagrams.MRU0, datagrams.RAW3, datagrams.FIL1, datagrams.TAG0, datagrams.SimradUnknown]: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Variant: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_Variant]: ...
    def copy(self) -> SimradRawDatagramContainer_Variant: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_Variant_mapped():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_Variant_mapped: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_Variant_mapped: ...
    def __copy__(self) -> SimradRawDatagramContainer_Variant_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_Variant_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> typing.Union[datagrams.SimradDatagram, datagrams.NME0, datagrams.XML0, datagrams.MRU0, datagrams.RAW3, datagrams.FIL1, datagrams.TAG0, datagrams.SimradUnknown]: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_Variant_mapped: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_Variant_mapped: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_Variant_mapped]: ...
    def copy(self) -> SimradRawDatagramContainer_Variant_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_Variant_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_XML0():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_XML0: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_XML0: ...
    def __copy__(self) -> SimradRawDatagramContainer_XML0: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_XML0: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.XML0: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_XML0: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_XML0: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_XML0]: ...
    def copy(self) -> SimradRawDatagramContainer_XML0: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_XML0: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradRawDatagramContainer_XML0_mapped():
    @typing.overload
    def __call__(self, datagram_identifier: t_SimradDatagramIdentifier) -> SimradRawDatagramContainer_XML0_mapped: ...
    @typing.overload
    def __call__(self, datagram_identifiers: typing.List[t_SimradDatagramIdentifier]) -> SimradRawDatagramContainer_XML0_mapped: ...
    def __copy__(self) -> SimradRawDatagramContainer_XML0_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradRawDatagramContainer_XML0_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> datagrams.XML0: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradRawDatagramContainer_XML0_mapped: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradRawDatagramContainer_XML0_mapped: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradRawDatagramContainer_XML0_mapped]: ...
    def copy(self) -> SimradRawDatagramContainer_XML0_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_datagrams_per_type(self) -> typing.Dict[t_SimradDatagramIdentifier, int]: ...
    def find_datagram_types(self) -> typing.List[t_SimradDatagramIdentifier]: ...
    def get_sorted_by_time(self) -> SimradRawDatagramContainer_XML0_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class t_SimradDatagramIdentifier():
    """
    Members:

      XML0 : < Unspecified (unknown) XML datagram

      FIL1 : < Filter datagram

      NME0 : < Unspecified (unknown) NMEA datagram

      MRU0 : < Motion datagram

      TAG0 : < ???

      RAW3 : < Raw sample data datagram
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    @typing.overload
    def __init__(self, str: str) -> None: 
        """
        Construct this enum type from string
        """
    @typing.overload
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    FIL1: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.FIL1: 827083078>
    MRU0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.MRU0: 810897997>
    NME0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.NME0: 809848142>
    RAW3: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.RAW3: 861356370>
    TAG0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.TAG0: 809976148>
    XML0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.XML0: 810306904>
    __members__: dict # value = {'XML0': <t_SimradDatagramIdentifier.XML0: 810306904>, 'FIL1': <t_SimradDatagramIdentifier.FIL1: 827083078>, 'NME0': <t_SimradDatagramIdentifier.NME0: 809848142>, 'MRU0': <t_SimradDatagramIdentifier.MRU0: 810897997>, 'TAG0': <t_SimradDatagramIdentifier.TAG0: 809976148>, 'RAW3': <t_SimradDatagramIdentifier.RAW3: 861356370>}
    pass
def SimradDatagram_type_from_string(datagram_type: str) -> int:
    pass
@typing.overload
def datagram_type_to_string(datagram_type: int) -> str:
    pass
@typing.overload
def datagram_type_to_string(datagram_type: t_SimradDatagramIdentifier) -> str:
    pass
def test_speed_decode_nmea(arg0: FileSimradRaw_mapped) -> None:
    pass
def test_speed_decode_xml(mapped_file_stream: FileSimradRaw_mapped, level: int = 10) -> None:
    pass
def test_speed_header(arg0: FileSimradRaw_mapped, arg1: t_SimradDatagramIdentifier) -> None:
    pass
def test_speed_raw(arg0: FileSimradRaw_mapped, arg1: t_SimradDatagramIdentifier) -> None:
    pass
def test_speed_raw_all(arg0: FileSimradRaw_mapped) -> None:
    pass
def test_speed_type(arg0: FileSimradRaw_mapped, arg1: t_SimradDatagramIdentifier) -> None:
    pass
FIL1: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.FIL1: 827083078>
MRU0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.MRU0: 810897997>
NME0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.NME0: 809848142>
RAW3: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.RAW3: 861356370>
TAG0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.TAG0: 809976148>
XML0: themachinethatgoesping.echosounders.simrad.t_SimradDatagramIdentifier # value = <t_SimradDatagramIdentifier.XML0: 810306904>
