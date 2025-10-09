"""
SimradRaw EK60 and EK80 file data types
"""
from __future__ import annotations
import themachinethatgoesping.echosounders_nanopy.filetemplates
import themachinethatgoesping.echosounders_nanopy.simradraw
import themachinethatgoesping.echosounders_nanopy.simradraw.datagrams
import themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams
import themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces
import typing
from . import calibration
__all__: list[str] = ['FilePackageIndex_simradraw_FilePackageIndex', 'SimradRawPing', 'SimradRawPingBottom', 'SimradRawPingBottom_stream', 'SimradRawPingCommon', 'SimradRawPingCommon_stream', 'SimradRawPingFileData', 'SimradRawPingFileData_stream', 'SimradRawPingWatercolumn', 'SimradRawPingWatercolumn_stream', 'SimradRawPing_stream', 'TransceiverInformation', 'calibration']
class FilePackageIndex_simradraw_FilePackageIndex:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    file_path: str
    file_size: int
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> FilePackageIndex_simradraw_FilePackageIndex:
        ...
    def __deepcopy__(self, arg: dict) -> FilePackageIndex_simradraw_FilePackageIndex:
        ...
    def __eq__(self, other: FilePackageIndex_simradraw_FilePackageIndex) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> FilePackageIndex_simradraw_FilePackageIndex:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def datagram_info_data(self) -> ...:
        """
        < all datagrams
        """
    @datagram_info_data.setter
    def datagram_info_data(self, arg: ..., std: ...) -> None:
        """
        < all datagrams
        """
class SimradRawPing(themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SimradRawPing:
        ...
    def __deepcopy__(self, arg: dict) -> SimradRawPing:
        ...
    def copy(self) -> SimradRawPing:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def file_data(self) -> SimradRawPingFileData:
        ...
class SimradRawPingBottom(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SimradRawPingBottom:
        ...
    def __deepcopy__(self, arg: dict) -> SimradRawPingBottom:
        ...
    def copy(self) -> SimradRawPingBottom:
        """
        return a copy using the c++ default copy constructor
        """
class SimradRawPingBottom_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SimradRawPingBottom_stream:
        ...
    def __deepcopy__(self, arg: dict) -> SimradRawPingBottom_stream:
        ...
    def copy(self) -> SimradRawPingBottom_stream:
        """
        return a copy using the c++ default copy constructor
        """
class SimradRawPingCommon:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SimradRawPingCommon:
        ...
    def __deepcopy__(self, arg: dict) -> SimradRawPingCommon:
        ...
    def copy(self) -> SimradRawPingCommon:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def file_data(self) -> SimradRawPingFileData:
        ...
class SimradRawPingCommon_stream:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SimradRawPingCommon_stream:
        ...
    def __deepcopy__(self, arg: dict) -> SimradRawPingCommon_stream:
        ...
    def copy(self) -> SimradRawPingCommon_stream:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def file_data(self) -> SimradRawPingFileData_stream:
        ...
class SimradRawPingFileData(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingFileData):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SimradRawPingFileData:
        ...
    def __deepcopy__(self, arg: dict) -> SimradRawPingFileData:
        ...
    def __repr__(self) -> str:
        """
        __repr__(self) -> str
        
        Return object information as string
        """
    def __str__(self) -> str:
        """
        __str__(self) -> str
        
        Return object information as string
        """
    def copy(self) -> SimradRawPingFileData:
        """
        return a copy using the c++ default copy constructor
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
    def get_environment(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Environment:
        """
        get_environment(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Environment
        """
    def get_filter_stages(self) -> ...:
        ...
    def get_parameter(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel:
        ...
    def get_ping_data(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.RAW3:
        ...
    def get_pulse_duration_index(self) -> int:
        """
        Get the pulse duration index This index is used to look up the correct
        sa correction / gain value in the transceiver Is determined by the
        index of the used pulse duration in the transceiver configuration
        
        Returns:
            size_t
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def get_watercolumn_calibration(self) -> calibration.SimradRawWaterColumnCalibration:
        ...
    def has_watercolumn_calibration(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str
        
        Return object information as string
        """
    def init_watercolumn_calibration(self, force: bool = False) -> None:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawDatagramInterface]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None
        
        Print object information
        """
    def release_watercolumn_calibration(self) -> None:
        ...
    def set_watercolumn_calibration(self, calibration: calibration.SimradRawWaterColumnCalibration) -> None:
        ...
    def watercolumn_calibration_loaded(self) -> bool:
        ...
    @property
    def transceiver_information(self) -> TransceiverInformation:
        ...
class SimradRawPingFileData_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingFileData):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SimradRawPingFileData_stream:
        ...
    def __deepcopy__(self, arg: dict) -> SimradRawPingFileData_stream:
        ...
    def __repr__(self) -> str:
        """
        __repr__(self) -> str
        
        Return object information as string
        """
    def __str__(self) -> str:
        """
        __str__(self) -> str
        
        Return object information as string
        """
    def copy(self) -> SimradRawPingFileData_stream:
        """
        return a copy using the c++ default copy constructor
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
    def get_environment(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Environment:
        """
        get_environment(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Environment
        """
    def get_filter_stages(self) -> ...:
        ...
    def get_parameter(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel:
        ...
    def get_ping_data(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.RAW3:
        ...
    def get_pulse_duration_index(self) -> int:
        """
        Get the pulse duration index This index is used to look up the correct
        sa correction / gain value in the transceiver Is determined by the
        index of the used pulse duration in the transceiver configuration
        
        Returns:
            size_t
        """
    def get_timestamp_first(self) -> float:
        ...
    def get_timestamp_last(self) -> float:
        ...
    def get_timestamp_range(self) -> ...:
        ...
    def get_watercolumn_calibration(self) -> calibration.SimradRawWaterColumnCalibration:
        ...
    def has_watercolumn_calibration(self) -> bool:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str
        
        Return object information as string
        """
    def init_watercolumn_calibration(self, force: bool = False) -> None:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawDatagramInterface_stream]:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None
        
        Print object information
        """
    def release_watercolumn_calibration(self) -> None:
        ...
    def set_watercolumn_calibration(self, calibration: calibration.SimradRawWaterColumnCalibration) -> None:
        ...
    def watercolumn_calibration_loaded(self) -> bool:
        ...
    @property
    def transceiver_information(self) -> TransceiverInformation:
        ...
class SimradRawPingWatercolumn(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SimradRawPingWatercolumn:
        ...
    def __deepcopy__(self, arg: dict) -> SimradRawPingWatercolumn:
        ...
    def copy(self) -> SimradRawPingWatercolumn:
        """
        return a copy using the c++ default copy constructor
        """
    def get_watercolumn_calibration(self) -> calibration.SimradRawWaterColumnCalibration:
        ...
class SimradRawPingWatercolumn_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SimradRawPingWatercolumn_stream:
        ...
    def __deepcopy__(self, arg: dict) -> SimradRawPingWatercolumn_stream:
        ...
    def copy(self) -> SimradRawPingWatercolumn_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def get_watercolumn_calibration(self) -> calibration.SimradRawWaterColumnCalibration:
        ...
class SimradRawPing_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SimradRawPing_stream:
        ...
    def __deepcopy__(self, arg: dict) -> SimradRawPing_stream:
        ...
    def copy(self) -> SimradRawPing_stream:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def file_data(self) -> SimradRawPingFileData_stream:
        ...
class TransceiverInformation:
    """
    This is a substructure of the simradrawPingWaterColumn class. It is
    used to store information necessary to efficiently read water column
    data from the file. It does not hold the actual water column samples
    
    Note this is a private substructure and is thus not part of the public
    API or pybind11 interface.
    """
    compute_impedance_factor: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> TransceiverInformation:
        ...
    def __deepcopy__(self, arg: dict) -> TransceiverInformation:
        ...
    def __eq__(self, other: TransceiverInformation) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, ping_transceiver: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver, ping_transceiver_channel: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver_Channel) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> TransceiverInformation:
        """
        return a copy using the c++ default copy constructor
        """
    def get_impedance_factor(self) -> float:
        ...
    def get_pulse_duration_index(self, xml_parameter_datagram: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel) -> int:
        """
        get_pulse_duration_index(self, pulse_duration: float, fm: bool) -> int
        """
    def get_pulse_duration_index_optional(self, xml_parameter_datagram: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel) -> int:
        """
        get_pulse_duration_index_optional(self, pulse_duration: float, fm: bool) -> int
        """
    def get_transceiver(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver:
        ...
    def get_transceiver_channel(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver_Channel:
        ...
    def get_transducer(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XMLConfigurationTransceiverChannelTransducer:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def is_initialized(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
