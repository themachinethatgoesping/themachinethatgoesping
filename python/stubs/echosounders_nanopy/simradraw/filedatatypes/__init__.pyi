import typing
from collections.abc import Sequence
from typing import overload

from . import calibration as calibration
import themachinethatgoesping.echosounders_nanopy.filetemplates
import themachinethatgoesping.echosounders_nanopy.simradraw
import themachinethatgoesping.echosounders_nanopy.simradraw.datagrams
import themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams
import themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces


class FilePackageIndex_simradraw_FilePackageIndex:
    def __init__(self) -> None: ...

    @property
    def file_path(self) -> str: ...

    @file_path.setter
    def file_path(self, arg: str, /) -> None: ...

    @property
    def file_size(self) -> int: ...

    @file_size.setter
    def file_size(self, arg: int, /) -> None: ...

    @property
    def datagram_info_data(self) -> list["themachinethatgoesping::echosounders::filetemplates::datatypes::DatagramInfoData_themachinethatgoesping_echosounders_simradraw_t_SimradRawDatagramIdentifier"]:
        """all datagrams"""

    @datagram_info_data.setter
    def datagram_info_data(self, arg: Sequence["themachinethatgoesping::echosounders::filetemplates::datatypes::DatagramInfoData_themachinethatgoesping_echosounders_simradraw_t_SimradRawDatagramIdentifier"], /) -> None: ...

    def __eq__(self, other: FilePackageIndex_simradraw_FilePackageIndex) -> bool: ...

    def copy(self) -> FilePackageIndex_simradraw_FilePackageIndex:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> FilePackageIndex_simradraw_FilePackageIndex: ...

    def __deepcopy__(self, arg: dict, /) -> FilePackageIndex_simradraw_FilePackageIndex: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FilePackageIndex_simradraw_FilePackageIndex:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class TransceiverInformation:
    """
    This is a substructure of the simradrawPingWaterColumn class. It is
    used to store information necessary to efficiently read water column
    data from the file. It does not hold the actual water column samples

    Note this is a private substructure and is thus not part of the public
    API or pybind11 interface.
    """

    def __init__(self, ping_transceiver: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver, ping_transceiver_channel: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver_Channel) -> None: ...

    def get_transceiver(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver: ...

    def get_transceiver_channel(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver_Channel: ...

    def get_transducer(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XMLConfigurationTransceiverChannelTransducer: ...

    def is_initialized(self) -> bool: ...

    def get_impedance_factor(self) -> float: ...

    @staticmethod
    def compute_impedance_factor(transceiver_impedance: float, transducer_impedance: float = 75) -> float: ...

    @overload
    def get_pulse_duration_index(self, xml_parameter_datagram: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel) -> int: ...

    @overload
    def get_pulse_duration_index(self, pulse_duration: float, fm: bool) -> int: ...

    @overload
    def get_pulse_duration_index_optional(self, xml_parameter_datagram: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel) -> int: ...

    @overload
    def get_pulse_duration_index_optional(self, pulse_duration: float, fm: bool) -> int: ...

    def __eq__(self, other: TransceiverInformation) -> bool: ...

    def copy(self) -> TransceiverInformation:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> TransceiverInformation: ...

    def __deepcopy__(self, arg: dict, /) -> TransceiverInformation: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> TransceiverInformation:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SimradRawPingFileData_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingFileData):
    def get_ping_data(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.RAW3: ...

    def get_parameter(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel: ...

    @overload
    def get_environment(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Environment: ...

    @overload
    def get_environment(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Environment: ...

    def get_filter_stages(self) -> typing.Any: ...

    def get_pulse_duration_index(self) -> int:
        """
        Get the pulse duration index This index is used to look up the correct
        sa correction / gain value in the transceiver Is determined by the
        index of the used pulse duration in the transceiver configuration

        Returns:
            size_t
        """

    def init_watercolumn_calibration(self, force: bool = False) -> None: ...

    def release_watercolumn_calibration(self) -> None: ...

    def has_watercolumn_calibration(self) -> bool: ...

    def set_watercolumn_calibration(self, calibration: calibration.SimradRawWaterColumnCalibration) -> None: ...

    def get_watercolumn_calibration(self) -> calibration.SimradRawWaterColumnCalibration: ...

    def watercolumn_calibration_loaded(self) -> bool: ...

    @property
    def transceiver_information(self) -> TransceiverInformation: ...

    def copy(self) -> SimradRawPingFileData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawPingFileData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawPingFileData_stream: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> str: ...

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str: ...

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawDatagramInterface_stream]: ...

class SimradRawPingFileData(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingFileData):
    def get_ping_data(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.RAW3: ...

    def get_parameter(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel: ...

    @overload
    def get_environment(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Environment: ...

    @overload
    def get_environment(self) -> themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Environment: ...

    def get_filter_stages(self) -> typing.Any: ...

    def get_pulse_duration_index(self) -> int:
        """
        Get the pulse duration index This index is used to look up the correct
        sa correction / gain value in the transceiver Is determined by the
        index of the used pulse duration in the transceiver configuration

        Returns:
            size_t
        """

    def init_watercolumn_calibration(self, force: bool = False) -> None: ...

    def release_watercolumn_calibration(self) -> None: ...

    def has_watercolumn_calibration(self) -> bool: ...

    def set_watercolumn_calibration(self, calibration: calibration.SimradRawWaterColumnCalibration) -> None: ...

    def get_watercolumn_calibration(self) -> calibration.SimradRawWaterColumnCalibration: ...

    def watercolumn_calibration_loaded(self) -> bool: ...

    @property
    def transceiver_information(self) -> TransceiverInformation: ...

    def copy(self) -> SimradRawPingFileData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawPingFileData: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawPingFileData: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> str: ...

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str: ...

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.t_SimradRawDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.simradraw.o_SimradRawDatagramIdentifier) -> object: ...

    def per_file(self) -> list[themachinethatgoesping.echosounders_nanopy.simradraw.filedatainterfaces.SimradRawDatagramInterface]: ...

class SimradRawPingCommon_stream:
    def copy(self) -> SimradRawPingCommon_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawPingCommon_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawPingCommon_stream: ...

    @property
    def file_data(self) -> SimradRawPingFileData_stream: ...

class SimradRawPingCommon:
    def copy(self) -> SimradRawPingCommon:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawPingCommon: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawPingCommon: ...

    @property
    def file_data(self) -> SimradRawPingFileData: ...

class SimradRawPingBottom_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom):
    def copy(self) -> SimradRawPingBottom_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawPingBottom_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawPingBottom_stream: ...

class SimradRawPingBottom(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom):
    def copy(self) -> SimradRawPingBottom:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawPingBottom: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawPingBottom: ...

class SimradRawPingWatercolumn_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn):
    def get_watercolumn_calibration(self) -> calibration.SimradRawWaterColumnCalibration: ...

    def copy(self) -> SimradRawPingWatercolumn_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawPingWatercolumn_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawPingWatercolumn_stream: ...

class SimradRawPingWatercolumn(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn):
    def get_watercolumn_calibration(self) -> calibration.SimradRawWaterColumnCalibration: ...

    def copy(self) -> SimradRawPingWatercolumn:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawPingWatercolumn: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawPingWatercolumn: ...

class SimradRawPing_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping):
    def copy(self) -> SimradRawPing_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawPing_stream: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawPing_stream: ...

    @property
    def file_data(self) -> SimradRawPingFileData_stream: ...

class SimradRawPing(themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping):
    def copy(self) -> SimradRawPing:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawPing: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawPing: ...

    @property
    def file_data(self) -> SimradRawPingFileData: ...
