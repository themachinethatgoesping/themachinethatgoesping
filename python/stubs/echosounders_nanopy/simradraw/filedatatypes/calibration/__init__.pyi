"""SimradRaw EK60 and EK80 calibration structures and functions"""
import typing

from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

from . import functions as functions
import themachinethatgoesping.echosounders_nanopy.filetemplates
import themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams
import themachinethatgoesping.echosounders_nanopy.simradraw.filedatatypes


class SimradRawWaterColumnCalibration(themachinethatgoesping.echosounders_nanopy.filetemplates.WaterColumnCalibration):
    """
    TODO: check effective pulse length
    - for power/angle data, do I only use the nominal pulse length?
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, other: themachinethatgoesping.echosounders_nanopy.filetemplates.WaterColumnCalibration) -> None: ...

    @overload
    def __init__(self, environment: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Environment, parameters: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel, transceiver_information: themachinethatgoesping.echosounders_nanopy.simradraw.filedatatypes.TransceiverInformation, filter_stages: typing.Any, n_complex_samples: int) -> None: ...

    @overload
    def set_transducer_parameters(self, transducer: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XMLConfigurationTransceiverChannelTransducer, pulse_duration_index: int) -> None: ...

    @overload
    def set_transducer_parameters(self, transducer_gain_db: float, sa_correction_db: float, equivalent_beam_angle_db: float, frequency_nominal_hz: float) -> None: ...

    @overload
    def set_environment_parameters(self, environment: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Environment) -> None: ...

    @overload
    def set_environment_parameters(self, reference_depth_m: float, temperature_c: float, salinity_psu: float, acidity_ph: float = 8.0600004196167) -> None: ...

    @overload
    def set_environment_parameters(self, forced_sound_velocity_m_s: float, forced_absorption_db_m: float) -> None: ...

    @overload
    def set_runtime_parameters(self, parameters: themachinethatgoesping.echosounders_nanopy.simradraw.datagrams.XML0_datagrams.XML_Parameter_Channel) -> None: ...

    @overload
    def set_runtime_parameters(self, frequency_hz: float, transmit_power_w: float, nominal_pulse_duration_s: float, slope: float, sample_interval_s: float) -> None: ...

    @overload
    def set_filter_parameters(self, filter_stages: typing.Any) -> None: ...

    @overload
    def set_filter_parameters(self, stage1_decimation_factor: int, stage1_coefficients: Annotated[NDArray[numpy.complex64], dict(shape=(None,), order='C')], stage2_decimation_factor: int, stage2_coefficients: Annotated[NDArray[numpy.complex64], dict(shape=(None,), order='C')]) -> None: ...

    def set_power_calibration_parameters(self, n_complex_samples: int, impedance_factor: float | None = None) -> None: ...

    def set_optional_parameters(self, rounded_latitude_deg: float | None = None, rounded_longitude_deg: float | None = None) -> None: ...

    def force_sound_velocity_m_s(self, forced_sound_velocity_m_s: float) -> None: ...

    def force_absorption_db_m(self, forced_absorption_db_m: float) -> None: ...

    def force_effective_pulse_duration_s(self, forced_effective_pulse_duration_s: float | None = None) -> None: ...

    def get_transducer_gain_db(self) -> float: ...

    def get_sa_correction_db(self) -> float: ...

    def get_equivalent_beam_angle_db(self) -> float: ...

    def get_frequency_nominal_hz(self) -> float: ...

    def get_reference_depth_m(self) -> float: ...

    def get_temperature_c(self) -> float: ...

    def get_salinity_psu(self) -> float: ...

    def get_acidity_ph(self) -> float: ...

    def get_frequency_hz(self) -> float: ...

    def get_transmit_power_w(self) -> float: ...

    def get_nominal_pulse_duration_s(self) -> float: ...

    def get_slope_factor(self) -> float: ...

    def get_sample_interval_s(self) -> float: ...

    def get_computed_effective_pulse_duration_s(self) -> float: ...

    def get_sound_velocity_m_s(self) -> float: ...

    def get_forced_sound_velocity_m_s(self) -> float | None: ...

    def get_computed_sound_velocity_m_s(self) -> float: ...

    def get_absorption_db_m(self) -> float: ...

    def get_forced_absorption_db_m(self) -> float | None: ...

    def get_computed_absorption_db_m(self) -> float: ...

    def get_wavelength_m(self) -> float: ...

    def get_corr_transducer_gain_db(self) -> float: ...

    def get_corr_equivalent_beam_angle_db(self) -> float: ...

    def get_filter_stage_1_decimation_factor(self) -> int: ...

    def get_filter_stage_2_decimation_factor(self) -> int: ...

    def get_filter_stage_1_coefficients(self) -> Annotated[NDArray[numpy.complex64], dict(order='C')]: ...

    def get_filter_stage_2_coefficients(self) -> Annotated[NDArray[numpy.complex64], dict(order='C')]: ...

    def get_computed_internal_sampling_interval_hz(self) -> float: ...

    def get_n_complex_samples(self) -> int | None: ...

    def get_power_conversion_factor_db(self) -> float | None: ...

    def get_rounded_latitude_deg(self) -> float | None: ...

    def get_rounded_longitude_deg(self) -> float | None: ...

    def compute_internal_sampling_interval_hz(self) -> float:
        """
        Compute the interal sampling interval in Hz based on the filter stages
        (decimation factors) and the resulting final sample interval

        Returns:
            float
        """

    def compute_raw_transmit_pulse(self, start_phase_degrees: float = 0.0) -> typing.Any:
        """
        This function computes the raw, unfiltered transmit signal from the
        parameters set in this calibration. It is used as input for the
        filter/decimation function that generate the theoretical transmit
        pulse when calling 'compute_filtered_transmit_pulse'.

        Note: The transmit pulse is generated with the nominal pulse duration
              and slope factor as a
        linear cosine chirp.

        Note: This function assumes the
              _computed_internal_sampling_interval_hz to be set, e.g.
        during initialization.

        Args:
            start_phase_degrees: start phase of the transmit pulse in degrees
                                 (default 0)

        Template Args:
            t_xtensor_float: 

        Returns:
            auto
        """

    def compute_filtered_transmit_pulse(self, start_phase_degrees: float = 0.0) -> typing.Any:
        """
        This function computes the filtered transmit signal from the
        parameters set in this calibration. It is used to generate the
        theoretical transmit pulse that is then used to compute the effective
        pulse duration when calling compute_effective_pulse_duration_s.

        Note the transmit pulse is generated with the nominal pulse duration
        and slope factor as a linear cosine chirp.

        Note: This function assumes the
              _computed_internal_sampling_interval_hz to be set, e.g.
        during initialization.

        Args:
            start_phase_degrees: start_phase_degrees start phase of the
                                 transmit pulse in degrees (default 0)

        Template Args:
            t_xtensor_float: 

        Returns:
            auto
        """

    def compute_effective_pulse_duration_s(self, round_to_full_samples: bool = True, start_phase_degrees: float = 0.0) -> float:
        """
        Compute the effective pulse duration by integrating the filtered
        transmit pulse.

        Note: This function assumes the
              _computed_internal_sampling_interval_hz to be set, e.g.
        during initialization.

        Args:
            round_to_full_samples: Round energy to full samples (default
                                   true). This matches ESP3s implementation.
            start_phase_degrees: Start phase of the transmit pulse in degrees
                                 (default 0). For testing only, should not
                                 affect the result.

        Returns:
            float
        """

    def setup_simrad_calibration(self) -> None: ...

    def initialized(self) -> bool: ...

    def check_initialized(self) -> None: ...

    def check_initialization(self) -> None: ...

    def check_can_be_initialized(self) -> None: ...

    def check_modifying_base_calibration_allowed(self) -> None: ...

    def __eq__(self, other: SimradRawWaterColumnCalibration) -> bool: ...

    def copy(self) -> SimradRawWaterColumnCalibration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SimradRawWaterColumnCalibration: ...

    def __deepcopy__(self, arg: dict, /) -> SimradRawWaterColumnCalibration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SimradRawWaterColumnCalibration:
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
