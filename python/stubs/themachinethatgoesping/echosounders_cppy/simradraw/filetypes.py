"""
SimradRaw EK60 and EK80 file data types
"""
from __future__ import annotations
import themachinethatgoesping.echosounders_cppy.filetemplates
import themachinethatgoesping.echosounders_cppy.simradraw
import themachinethatgoesping.echosounders_cppy.simradraw.datagrams
import themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams
import typing
__all__ = ['FilePackageIndex_simradraw_FilePackageIndex', 'SimradRawPing', 'SimradRawPingBottom', 'SimradRawPingBottom_stream', 'SimradRawPingCommon', 'SimradRawPingCommon_stream', 'SimradRawPingFileData', 'SimradRawPingFileData_stream', 'SimradRawPingWatercolumn', 'SimradRawPingWatercolumn_stream', 'SimradRawPing_stream', 'SimradRawWaterColumnCalibration', 'TransceiverInformation']
class FilePackageIndex_simradraw_FilePackageIndex:
    """
    """
    file_path: str
    file_size: int
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FilePackageIndex_simradraw_FilePackageIndex:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> FilePackageIndex_simradraw_FilePackageIndex:
        ...
    def __deepcopy__(self, arg0: dict) -> FilePackageIndex_simradraw_FilePackageIndex:
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
    def __setstate__(self, arg0: bytes) -> None:
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
    def datagram_info_data(self) -> list[...]:
        """
        < all datagrams
        """
    @datagram_info_data.setter
    def datagram_info_data(self, arg0: list[...]) -> None:
        ...
class SimradRawPing(themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, SimradRawPingCommon):
    """
    """
    def __copy__(self) -> SimradRawPing:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPing:
        ...
    def copy(self) -> SimradRawPing:
        """
        return a copy using the c++ default copy constructor
        """
class SimradRawPingBottom(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingBottom, SimradRawPingCommon):
    """
    """
    def __copy__(self) -> SimradRawPingBottom:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingBottom:
        ...
    def copy(self) -> SimradRawPingBottom:
        """
        return a copy using the c++ default copy constructor
        """
class SimradRawPingBottom_stream(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingBottom, SimradRawPingCommon_stream):
    """
    """
    def __copy__(self) -> SimradRawPingBottom_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingBottom_stream:
        ...
    def copy(self) -> SimradRawPingBottom_stream:
        """
        return a copy using the c++ default copy constructor
        """
class SimradRawPingCommon:
    """
    """
    def __copy__(self) -> SimradRawPingCommon:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingCommon:
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
    def __copy__(self) -> SimradRawPingCommon_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingCommon_stream:
        ...
    def copy(self) -> SimradRawPingCommon_stream:
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def file_data(self) -> SimradRawPingFileData_stream:
        ...
class SimradRawPingFileData(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingFileData):
    """
    """
    def __copy__(self) -> SimradRawPingFileData:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingFileData:
        ...
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawPingFileData:
        """
        return a copy using the c++ default copy constructor
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
    @typing.overload
    def get_environment(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Environment:
        ...
    @typing.overload
    def get_environment(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Environment:
        ...
    def get_parameter(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel:
        ...
    def get_ping_data(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3:
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
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def get_watercolumn_calibration(self) -> SimradRawWaterColumnCalibration:
        ...
    def has_watercolumn_calibration(self) -> bool:
        ...
    @typing.overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_watercolumn_calibration(self, force: bool = False) -> None:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[...]:
        ...
    @typing.overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @typing.overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def release_watercolumn_calibration(self) -> None:
        ...
    def set_watercolumn_calibration(self, calibration: SimradRawWaterColumnCalibration) -> None:
        ...
    def watercolumn_calibration_loaded(self) -> bool:
        ...
    @property
    def transceiver_information(self) -> TransceiverInformation:
        ...
class SimradRawPingFileData_stream(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingFileData):
    """
    """
    def __copy__(self) -> SimradRawPingFileData_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingFileData_stream:
        ...
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SimradRawPingFileData_stream:
        """
        return a copy using the c++ default copy constructor
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
    @typing.overload
    def get_environment(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Environment:
        ...
    @typing.overload
    def get_environment(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Environment:
        ...
    def get_parameter(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel:
        ...
    def get_ping_data(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.RAW3:
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
    def get_timestamp_range(self) -> tuple[float, float]:
        ...
    def get_watercolumn_calibration(self) -> SimradRawWaterColumnCalibration:
        ...
    def has_watercolumn_calibration(self) -> bool:
        ...
    @typing.overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_watercolumn_calibration(self, force: bool = False) -> None:
        ...
    def keys(self) -> list[themachinethatgoesping.echosounders_cppy.simradraw.t_SimradRawDatagramIdentifier]:
        ...
    def per_file(self) -> list[..., ...]:
        ...
    @typing.overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @typing.overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def release_watercolumn_calibration(self) -> None:
        ...
    def set_watercolumn_calibration(self, calibration: SimradRawWaterColumnCalibration) -> None:
        ...
    def watercolumn_calibration_loaded(self) -> bool:
        ...
    @property
    def transceiver_information(self) -> TransceiverInformation:
        ...
class SimradRawPingWatercolumn(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingWatercolumn, SimradRawPingCommon):
    """
    """
    def __copy__(self) -> SimradRawPingWatercolumn:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingWatercolumn:
        ...
    def copy(self) -> SimradRawPingWatercolumn:
        """
        return a copy using the c++ default copy constructor
        """
    def get_watercolumn_calibration(self) -> SimradRawWaterColumnCalibration:
        ...
class SimradRawPingWatercolumn_stream(themachinethatgoesping.echosounders_cppy.filetemplates.I_PingWatercolumn, SimradRawPingCommon_stream):
    """
    """
    def __copy__(self) -> SimradRawPingWatercolumn_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPingWatercolumn_stream:
        ...
    def copy(self) -> SimradRawPingWatercolumn_stream:
        """
        return a copy using the c++ default copy constructor
        """
    def get_watercolumn_calibration(self) -> SimradRawWaterColumnCalibration:
        ...
class SimradRawPing_stream(themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping, SimradRawPingCommon_stream):
    """
    """
    def __copy__(self) -> SimradRawPing_stream:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawPing_stream:
        ...
    def copy(self) -> SimradRawPing_stream:
        """
        return a copy using the c++ default copy constructor
        """
class SimradRawWaterColumnCalibration(themachinethatgoesping.echosounders_cppy.filetemplates.WaterColumnCalibration):
    """
    TODO: check effective pulse length - for power/angle data, do I only
    use the nominal pulse length?
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SimradRawWaterColumnCalibration:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SimradRawWaterColumnCalibration:
        ...
    def __deepcopy__(self, arg0: dict) -> SimradRawWaterColumnCalibration:
        ...
    def __eq__(self, other: SimradRawWaterColumnCalibration) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, environment: themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Environment, parameters: themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel, transceiver_information: TransceiverInformation, n_complex_samples: int) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def check_can_be_initialized(self) -> None:
        ...
    def check_initialization(self) -> None:
        ...
    def check_initialized(self) -> None:
        ...
    def copy(self) -> SimradRawWaterColumnCalibration:
        """
        return a copy using the c++ default copy constructor
        """
    def force_absorption_db_m(self, forced_absorption_db_m: float | None) -> None:
        ...
    def force_sound_velocity_m_s(self, forced_sound_velocity_m_s: float | None) -> None:
        ...
    def get_absorption_db_m(self) -> float:
        ...
    def get_acidity_ph(self) -> float:
        ...
    def get_computed_absorption_db_m(self) -> float:
        ...
    def get_computed_sound_velocity_m_s(self) -> float:
        ...
    def get_corr_equivalent_beam_angle_db(self) -> float:
        ...
    def get_corr_transducer_gain_db(self) -> float:
        ...
    def get_effective_pulse_duration_s(self) -> float:
        ...
    def get_equivalent_beam_angle_db(self) -> float:
        ...
    def get_forced_absorption_db_m(self) -> float | None:
        ...
    def get_forced_sound_velocity_m_s(self) -> float | None:
        ...
    def get_frequency_hz(self) -> float:
        ...
    def get_frequency_nominal_hz(self) -> float:
        ...
    def get_n_complex_samples(self) -> int | None:
        ...
    def get_power_conversion_factor_db(self) -> float | None:
        ...
    def get_reference_depth_m(self) -> float:
        ...
    def get_rounded_latitude_deg(self) -> float | None:
        ...
    def get_rounded_longitude_deg(self) -> float | None:
        ...
    def get_sa_correction_db(self) -> float:
        ...
    def get_salinity_psu(self) -> float:
        ...
    def get_sound_velocity_m_s(self) -> float:
        ...
    def get_temperature_c(self) -> float:
        ...
    def get_transducer_gain_db(self) -> float:
        ...
    def get_transmit_power_w(self) -> float:
        ...
    def get_wavelength_m(self) -> float:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def initialized(self) -> bool:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_absorption_db_m(self, transducer: themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XMLConfigurationTransceiverChannelTransducer, pulse_duration_index: int) -> None:
        ...
    @typing.overload
    def set_environment_parameters(self, environment: themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Environment) -> None:
        ...
    @typing.overload
    def set_environment_parameters(self, reference_depth_m: float, temperature_c: float, salinity_psu: float, acidity_ph: float = 8.0600004196167) -> None:
        ...
    @typing.overload
    def set_environment_parameters(self, forced_sound_velocity_m_s: float, forced_absorption_db_m: float) -> None:
        ...
    def set_optional_parameters(self, rounded_latitude_deg: float | None = None, rounded_longitude_deg: float | None = None) -> None:
        ...
    def set_power_calibration_parameters(self, n_complex_samples: int, impedance_factor: float | None = None) -> None:
        ...
    @typing.overload
    def set_runtime_parameters(self, parameters: themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel) -> None:
        ...
    @typing.overload
    def set_runtime_parameters(self, frequency_hz: float, transmit_power_w: float, effective_pulse_duration_s: float) -> None:
        ...
    @typing.overload
    def set_transducer_parameters(self, transducer: themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XMLConfigurationTransceiverChannelTransducer, pulse_duration_index: int) -> None:
        ...
    @typing.overload
    def set_transducer_parameters(self, transducer_gain_db: float, sa_correction_db: float, equivalent_beam_angle_db: float, frequency_nominal_hz: float) -> None:
        ...
    def setup_simrad_calibration(self) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class TransceiverInformation:
    """
    This is a substructure of the simradrawPingWaterColumn class. It is
    used to store information necessary to efficiently read water column
    data from the file. It does not hold the actual water column samples
    
    Note this is a private substructure and is thus not part of the public
    API or pybind11 interface.
    """
    @staticmethod
    def compute_impedance_factor(transceiver_impedance: float, transducer_impedance: float = 75) -> float:
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> TransceiverInformation:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> TransceiverInformation:
        ...
    def __deepcopy__(self, arg0: dict) -> TransceiverInformation:
        ...
    def __eq__(self, other: TransceiverInformation) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, ping_transceiver: themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver, ping_transceiver_channel: themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver_Channel) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
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
    @typing.overload
    def get_pulse_duration_index(self, xml_parameter_datagram: themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel) -> int:
        ...
    @typing.overload
    def get_pulse_duration_index(self, pulse_duration: float, fm: bool) -> int:
        ...
    @typing.overload
    def get_pulse_duration_index_optional(self, xml_parameter_datagram: themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel) -> int:
        ...
    @typing.overload
    def get_pulse_duration_index_optional(self, pulse_duration: float, fm: bool) -> int:
        ...
    def get_transceiver(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver:
        ...
    def get_transceiver_channel(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XML_Configuration_Transceiver_Channel:
        ...
    def get_transducer(self) -> themachinethatgoesping.echosounders_cppy.simradraw.datagrams.XML0_datagrams.XMLConfigurationTransceiverChannelTransducer:
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
