"""Trampoline classes for abstract file template classes"""
import typing

from collections.abc import Sequence
import enum
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

import themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures
import themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures
import themachinethatgoesping.echosounders_nanopy.pingtools
import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.navigation_nanopy.datastructures
import themachinethatgoesping.tools_nanopy.vectorinterpolators
import themachinethatgoesping.tools_nanopy.vectorinterpolators.bivectorinterpolators


class AmplitudeCalibration:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, system_offset: float) -> None: ...

    @overload
    def __init__(self, arg: AmplitudeCalibration) -> None: ...

    def get_per_beam_offsets(self, beamangles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_per_sample_offsets(self, ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def apply_beam_sample_correction(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m: float, tvg_factor: float | None, mp_cores: int | None = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    def apply_beam_sample_correction_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], tvg_factor: float, mp_cores: int | None = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """
        Apply beam and sample corrections with per-beam absorption
        coefficients.

        This overload supports per-beam absorption coefficients for multi-
        sector sonars (e.g., Kongsberg) where each transmit sector may have a
        different absorption value.

        Args:
            wci: The input 2D tensor (beams x samples).
            beam_angles: A 1D tensor of beam angles (size = number of beams).
            ranges: A 1D tensor of ranges in meters (size = number of
                    samples).
            absorption_db_m_per_beam: A 1D tensor of absorption coefficients
                                      in dB/m per beam.
            tvg_factor: Optional time-varying gain factor.
            mp_cores: Number of parallel cores (default = 1).

        Template Args:
            t_xtensor_2d: Type of the 2D water column image tensor.
            t_xtensor_1d: Type of the 1D tensor for beam angles, ranges, and
                          absorption.

        Returns:
            Corrected 2D tensor.
        """

    def inplace_beam_sample_correction(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m: float, tvg_factor: float | None, min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int | None = 1) -> None: ...

    def inplace_beam_sample_correction_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], tvg_factor: float, min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int | None = 1) -> None:
        """
        Inplace apply beam and sample corrections with per-beam absorption
        coefficients.

        This overload supports per-beam absorption coefficients for multi-
        sector sonars (e.g., Kongsberg) where each transmit sector may have a
        different absorption value.

        Args:
            wci: The input 2D tensor to be modified in-place (beams x
                 samples).
            beam_angles: A 1D tensor of beam angles (size = number of beams).
            ranges: A 1D tensor of ranges in meters (size = number of
                    samples).
            absorption_db_m_per_beam: A 1D tensor of absorption coefficients
                                      in dB/m per beam.
            tvg_factor: Optional time-varying gain factor.
            min_beam_index: Optional minimum beam index.
            max_beam_index: Optional maximum beam index.
            mp_cores: Number of parallel cores (default = 1).

        Template Args:
            t_xtensor_2d: Type of the 2D water column image tensor.
            t_xtensor_1d: Type of the 1D tensor for beam angles, ranges, and
                          absorption.
        """

    def get_system_offset(self) -> float: ...

    def has_system_offset(self) -> bool: ...

    def set_system_offset(self, value: float) -> None: ...

    def set_offset_per_beamangle(self, beamangle: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None: ...

    def has_offset_per_beamangle(self) -> bool: ...

    def set_offset_per_range(self, range: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None: ...

    def has_offset_per_range(self) -> bool: ...

    @overload
    def set_offset_per_beamangle_and_range(self, beamangles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], values: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]) -> None: ...

    @overload
    def set_offset_per_beamangle_and_range(self, offset_per_beamangle_and_range: themachinethatgoesping.tools_nanopy.vectorinterpolators.bivectorinterpolators.BiAkimaInterpolatorF) -> None: ...

    def has_offset_per_beamangle_and_range(self) -> bool: ...

    def get_interpolator_offset_per_beamangle(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolatorF: ...

    def get_interpolator_offset_per_range(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolatorF: ...

    def get_interpolator_offset_per_beamangle_and_range(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.bivectorinterpolators.BiAkimaInterpolatorF: ...

    def __eq__(self, other: AmplitudeCalibration) -> bool: ...

    def copy(self) -> AmplitudeCalibration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> AmplitudeCalibration: ...

    def __deepcopy__(self, arg: dict, /) -> AmplitudeCalibration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> AmplitudeCalibration:
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

class t_calibration_type(enum.Enum):
    """Calibration type for water column data processing"""

    power = 0
    """
    power calibration (Received amplitudes computed to power, no
    absorption, no spreading loss)
    """

    rp = 1
    """
    power derived point scattering (uncalibrated TS without parameter and
    absorption compensation)
    """

    rv = 2
    """
    power derived volume scattering (uncalibrated SV without parameter and
    absorption compensation)
    """

    pp = 3
    """
    power derived point scattering (uncalibrated TS without parameter
    compensation)
    """

    pv = 4
    """
    power derived volume scattering (uncalibrated SV without parameter
    compensation)
    """

    ap = 5
    """amplitude derived point scattering (uncalibrated TS)"""

    av = 6
    """amplitude derived volume scattering (uncalibrated SV)"""

    sp = 7
    """point scattering (uncompensated TS)"""

    sv = 8
    """volume scattering SV"""

class o_calibration_type:
    """
    Helper class to convert between strings and enum values of type 't_calibration_type'
    """

    @overload
    def __init__(self, value: t_calibration_type = t_calibration_type.power) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> t_calibration_type:
        """enum value"""

    @value.setter
    def value(self, arg: t_calibration_type, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.filetemplates.t_calibration_type = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_calibration_type, /) -> bool: ...

    @overload
    def __eq__(self, arg: t_calibration_type, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_calibration_type:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_calibration_type: ...

    def __deepcopy__(self, arg: dict, /) -> o_calibration_type: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_calibration_type:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> None: ...

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class WaterColumnCalibration:
    @overload
    def __init__(self, tvg_absorption_db_m: float = 0.0, tvg_factor: float = 0.0) -> None: ...

    @overload
    def __init__(self, power_calibration: AmplitudeCalibration = ..., ap_calibration: AmplitudeCalibration = ..., av_calibration: AmplitudeCalibration = ..., tvg_absorption_db_m: float = 0.0, tvg_factor: float = 0.0) -> None: ...

    def set_absorption_db_m(self, absorption_db_m: float) -> None: ...

    def get_absorption_db_m(self) -> float: ...

    def has_valid_absorption_db_m(self) -> bool: ...

    def get_tvg_absorption_db_m(self) -> float: ...

    def get_tvg_factor(self) -> float: ...

    def get_absorption_to_apply(self, absorption_db_m: float | None = None) -> float | None: ...

    def get_tvg_factor_to_apply(self, tvg_factor: float) -> float | None: ...

    def has_power_calibration(self) -> bool: ...

    def has_ap_calibration(self) -> bool: ...

    def has_av_calibration(self) -> bool: ...

    def has_sp_calibration(self) -> bool: ...

    def has_sv_calibration(self) -> bool: ...

    def get_power_calibration(self) -> AmplitudeCalibration: ...

    def get_ap_calibration(self) -> AmplitudeCalibration: ...

    def get_av_calibration(self) -> AmplitudeCalibration: ...

    def get_sp_calibration(self) -> AmplitudeCalibration: ...

    def get_sv_calibration(self) -> AmplitudeCalibration: ...

    def set_power_calibration(self, calibration: AmplitudeCalibration) -> None: ...

    def set_ap_calibration(self, calibration: AmplitudeCalibration) -> None: ...

    def set_av_calibration(self, calibration: AmplitudeCalibration) -> None: ...

    def set_sp_calibration(self, calibration: AmplitudeCalibration) -> None: ...

    def set_sv_calibration(self, calibration: AmplitudeCalibration) -> None: ...

    def check_initialized(self) -> None: ...

    def check_modifying_base_calibration_allowed(self) -> None: ...

    def __eq__(self, other: WaterColumnCalibration) -> bool: ...

    def copy(self) -> WaterColumnCalibration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> WaterColumnCalibration: ...

    def __deepcopy__(self, arg: dict, /) -> WaterColumnCalibration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> WaterColumnCalibration:
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

    @overload
    def apply_beam_sample_correction_power(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_power(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_rp(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_rp(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_rv(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_rv(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pp(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pp(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pv(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pv(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_ap(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_ap(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sv(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sv(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sp(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sp(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pp_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply pp calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_pp_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pv_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply pv calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_pv_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_ap_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply ap calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_ap_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply av calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sp_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply sp calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_sp_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sv_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply sv calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_sv_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

class MultiSectorWaterColumnCalibration_flyweight:
    """Flyweight wrapper around the MultiSectorCalibration class."""

    def __init__(self, other: MultiSectorWaterColumnCalibration) -> None:
        """Create a flyweight from a MultiSectorCalibration object."""

    def get(self) -> MultiSectorWaterColumnCalibration:
        """Get the underlying T_MultiSectorCalibration object."""

class MultiSectorWaterColumnCalibration:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, calibration_per_sector: Sequence[WaterColumnCalibration]) -> None: ...

    @overload
    def __init__(self, other: MultiSectorWaterColumnCalibration) -> None: ...

    def has_power_calibration(self) -> bool: ...

    def has_ap_calibration(self) -> bool: ...

    def has_av_calibration(self) -> bool: ...

    def has_sp_calibration(self) -> bool: ...

    def has_sv_calibration(self) -> bool: ...

    def has_valid_absorption_db_m(self) -> bool: ...

    def get_number_of_sectors(self) -> int: ...

    def __len__(self) -> int: ...

    def get_calibrations(self) -> list[WaterColumnCalibration]: ...

    def pre_hashed(self) -> MultiSectorWaterColumnCalibration_flyweight:
        """
        Return this class as a flyweight with computed hash. This faster when updating the ping calibration.
        """

    def __eq__(self, other: MultiSectorWaterColumnCalibration) -> bool: ...

    def copy(self) -> MultiSectorWaterColumnCalibration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MultiSectorWaterColumnCalibration: ...

    def __deepcopy__(self, arg: dict, /) -> MultiSectorWaterColumnCalibration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> MultiSectorWaterColumnCalibration:
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

    @overload
    def apply_beam_sample_correction_power(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_power(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pp(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pp(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pv(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pv(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_ap(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_ap(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sp(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sp(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sv(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sv(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def inplace_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None: ...

    @overload
    def inplace_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None: ...

    @overload
    def apply_beam_sample_correction_pp_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply pp calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_pp_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pv_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply pv calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_pv_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_ap_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply ap calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_ap_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply av calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sp_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply sp calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_sp_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sv_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply sv calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_sv_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def inplace_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None:
        """Inplace apply av calibration with per-beam absorption coefficients."""

    @overload
    def inplace_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None: ...

class t_pingfeature(enum.Enum):
    timestamp = 0

    datetime = 1

    channel_id = 2

    sensor_configuration = 3

    navigation_interpolator_latlon = 4

    sensor_data_latlon = 5

    geolocation = 6

    bottom = 8

    watercolumn = 9

    tx_signal_parameters = 10

    beam_numbers_per_tx_sector = 12

    beam_selection_all = 13

    number_of_beams = 14

    tx_sector_per_beam = 15

    number_of_tx_sectors = 11

    beam_crosstrack_angles = 16

    two_way_travel_times = 17

    xyz = 18

    bottom_range_samples = 19

    amplitudes = 20

    ap = 25

    av = 26

    power = 27

    rp = 21

    rv = 22

    pp = 23

    pv = 24

    sp = 28

    sv = 29

    watercolumn_calibration = 30

    multisectorwatercolumn_calibration = 31

class o_pingfeature:
    """
    Helper class to convert between strings and enum values of type 't_pingfeature'
    """

    @overload
    def __init__(self, value: t_pingfeature = t_pingfeature.timestamp) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> t_pingfeature:
        """enum value"""

    @value.setter
    def value(self, arg: t_pingfeature, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.filetemplates.t_pingfeature = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_pingfeature, /) -> bool: ...

    @overload
    def __eq__(self, arg: t_pingfeature, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_pingfeature:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_pingfeature: ...

    def __deepcopy__(self, arg: dict, /) -> o_pingfeature: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_pingfeature:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> None: ...

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class I_PingCommon:
    def feature_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered features that are available or not
        available

        Args:
            available: if True (default) return available features, else
                       return not available features

        Returns:
            std::string
        """

    def feature_groups_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered feature groups that are available or
        not available

        Args:
            available: if True (default) return available features, else
                       return not available features

        Returns:
            std::string
        """

    def has_any_of_features(self, feature_names: Sequence[o_pingfeature]) -> bool:
        """
        Check if any of the specified features is available

        Returns:
            true false
        """

    def has_all_of_features(self, feature_names: Sequence[o_pingfeature]) -> bool:
        """
        Check if all of the specified features are available

        Returns:
            true false
        """

    def has_features(self) -> bool:
        """
        Check if any of the registered features is available

        Returns:
            true false
        """

    def has_primary_features(self) -> bool:
        """
        Check if any of the registered main features is available

        Returns:
            true false
        """

    def registered_features(self) -> str:
        """
        Get a string of all registered features for this ping class

        Returns:
            std::string
        """

    def primary_features(self) -> str:
        """
        Get a string of all registered primary features for this ping class

        Returns:
            std::string
        """

    def has_feature(self, feature_name: o_pingfeature) -> bool:
        """
        Check if any of the registered features is available

        Returns:
            true false
        """

    def available_features(self, available_available: bool = True) -> list[t_pingfeature]: ...

    def possible_features(self) -> list[t_pingfeature]: ...

    def available_feature_groups(self, available: bool = True) -> list[t_pingfeature]: ...

    def possible_feature_groups(self) -> list[t_pingfeature]: ...

    def load(self, force: bool = False) -> None: ...

    def release(self) -> None: ...

    def loaded(self) -> bool: ...

    @overload
    def copy(self) -> I_PingCommon:
        """return a copy using the c++ default copy constructor"""

    @overload
    def copy(self) -> I_PingCommon: ...

    @overload
    def __copy__(self) -> I_PingCommon: ...

    @overload
    def __copy__(self) -> I_PingCommon: ...

    @overload
    def __deepcopy__(self, arg: dict, /) -> I_PingCommon: ...

    @overload
    def __deepcopy__(self, arg: dict, /) -> I_PingCommon: ...

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

class I_PingFileData:
    """
    Interface for raw ping data.

    This class defines an interface for raw ping data. It provides methods
    to access and manipulate the properties of the ping data, such as the
    name, file ping counter, primary file number, file numbers, primary
    file path, and file paths.

    The class also includes a nested exception class, `not_implemented`,
    which is thrown when a method is not implemented.

    The class provides a `__printer__` function for object printing, which
    can be used to print the properties of the ping data.
    """

    def get_file_numbers(self) -> list[int]:
        """
        Get the file numbers of the contained datagrams.
        Returns:
            std::vector_size_t The file numbers.

        Raises:
            not_implemented: Exception if not implemented.
        """

    def get_primary_file_path(self) -> str:
        """
        Get the primary file path of this ping.
        Returns:
            std::string The primary file path of this ping.

        Raises:
            not_implemented: Exception if not implemented.
        """

    def get_file_paths(self) -> list[str]:
        """
        Get the file paths.
        Returns:
            std::vector_std_string The file paths associated with the
                contained datagrams.

        Raises:
            not_implemented: Exception if not implemented.
        """

    def get_primary_file_nr(self) -> int:
        """
        Get the primary file number of this ping.
        Returns:
            size_t The primary file number.
        """

    def set_primary_file_nr(self, file_nr: int) -> None:
        """
        Set the primary file number for this ping.
        Args:
            primary_file_nr: The primary file number to set.
        """

    def get_file_ping_counter(self) -> int:
        """
        Get the file ping counter.
        Returns:
            size_t The file ping counter.
        """

    def set_file_ping_counter(self, file_ping_counter: int) -> None:
        """
        Set the file ping counter.
        Args:
            file_ping_counter: The file ping counter to set.
        """

    def copy(self) -> I_PingFileData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> I_PingFileData: ...

    def __deepcopy__(self, arg: dict, /) -> I_PingFileData: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class I_PingBottom(I_PingCommon):
    """Interface for all ping bottom detection functions"""

    def feature_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered features that are available or not
        available

        Args:
            available: if True (default) return available features, else
                       return not available features

        Returns:
            std::string
        """

    def feature_groups_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered feature groups that are available or
        not available

        Args:
            available: if True (default) return available features, else
                       return not available features

        Returns:
            std::string
        """

    def has_any_of_features(self, feature_names: Sequence[o_pingfeature]) -> bool:
        """
        Check if any of the specified features is available

        Returns:
            true false
        """

    def has_all_of_features(self, feature_names: Sequence[o_pingfeature]) -> bool:
        """
        Check if all of the specified features are available

        Returns:
            true false
        """

    def has_features(self) -> bool:
        """
        Check if any of the registered features is available

        Returns:
            true false
        """

    def has_primary_features(self) -> bool:
        """
        Check if any of the registered main features is available

        Returns:
            true false
        """

    def registered_features(self) -> str:
        """
        Get a string of all registered features for this ping class

        Returns:
            std::string
        """

    def primary_features(self) -> str:
        """
        Get a string of all registered primary features for this ping class

        Returns:
            std::string
        """

    def has_feature(self, feature_name: o_pingfeature) -> bool:
        """
        Check if any of the registered features is available

        Returns:
            true false
        """

    def available_features(self, available_available: bool = True) -> list[t_pingfeature]: ...

    def possible_features(self) -> list[t_pingfeature]: ...

    def available_feature_groups(self, available: bool = True) -> list[t_pingfeature]: ...

    def possible_feature_groups(self) -> list[t_pingfeature]: ...

    def load(self, force: bool = False) -> None: ...

    def release(self) -> None: ...

    def loaded(self) -> bool: ...

    @overload
    def copy(self) -> I_PingBottom:
        """return a copy using the c++ default copy constructor"""

    @overload
    def copy(self) -> I_PingBottom: ...

    @overload
    def __copy__(self) -> I_PingBottom: ...

    @overload
    def __copy__(self) -> I_PingBottom: ...

    @overload
    def __deepcopy__(self, arg: dict, /) -> I_PingBottom: ...

    @overload
    def __deepcopy__(self, arg: dict, /) -> I_PingBottom: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def has_tx_signal_parameters(self) -> bool: ...

    def has_number_of_tx_sectors(self) -> bool: ...

    def has_beam_numbers_per_tx_sector(self) -> bool: ...

    def has_beam_selection_all(self) -> bool: ...

    def has_number_of_beams(self) -> bool: ...

    def has_tx_sector_per_beam(self) -> bool: ...

    def get_tx_signal_parameters(self) -> list[themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.CWSignalParameters | themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.FMSignalParameters | themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.GenericSignalParameters]: ...

    def get_number_of_tx_sectors(self) -> int: ...

    @overload
    def get_tx_sector_per_beam(self) -> Annotated[NDArray[numpy.uint64], dict(order='C')]: ...

    @overload
    def get_tx_sector_per_beam(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> Annotated[NDArray[numpy.uint64], dict(order='C')]: ...

    @overload
    def get_beam_numbers_per_tx_sector(self) -> list[list[int]]: ...

    @overload
    def get_beam_numbers_per_tx_sector(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> list[list[int]]: ...

    def get_beam_selection_all(self) -> themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection: ...

    def get_number_of_beams(self) -> int: ...

    @overload
    def get_beam_crosstrack_angles(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_beam_crosstrack_angles(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def has_beam_crosstrack_angles(self) -> bool: ...

    def has_xyz(self) -> bool: ...

    def has_two_way_travel_times(self) -> bool: ...

    @overload
    def get_xyz(self) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1: ...

    @overload
    def get_xyz(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1: ...

    @overload
    def get_bottom_z(self) -> float: ...

    @overload
    def get_bottom_z(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> float: ...

    @overload
    def get_two_way_travel_times(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_two_way_travel_times(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

class I_PingWatercolumn(I_PingCommon):
    """
    Interface for all ping watercolumn functions




    Interface for watercolumn ping data.

    This class represents an interface for accessing watercolumn ping
    data. It inherits from the I_PingCommon class and provides additional
    functions and variables specific to watercolumn pings.
    """

    def feature_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered features that are available or not
        available

        Args:
            available: if True (default) return available features, else
                       return not available features

        Returns:
            std::string
        """

    def feature_groups_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered feature groups that are available or
        not available

        Args:
            available: if True (default) return available features, else
                       return not available features

        Returns:
            std::string
        """

    def has_any_of_features(self, feature_names: Sequence[o_pingfeature]) -> bool:
        """
        Check if any of the specified features is available

        Returns:
            true false
        """

    def has_all_of_features(self, feature_names: Sequence[o_pingfeature]) -> bool:
        """
        Check if all of the specified features are available

        Returns:
            true false
        """

    def has_features(self) -> bool:
        """
        Check if any of the registered features is available

        Returns:
            true false
        """

    def has_primary_features(self) -> bool:
        """
        Check if any of the registered main features is available

        Returns:
            true false
        """

    def registered_features(self) -> str:
        """
        Get a string of all registered features for this ping class

        Returns:
            std::string
        """

    def primary_features(self) -> str:
        """
        Get a string of all registered primary features for this ping class

        Returns:
            std::string
        """

    def has_feature(self, feature_name: o_pingfeature) -> bool:
        """
        Check if any of the registered features is available

        Returns:
            true false
        """

    def available_features(self, available_available: bool = True) -> list[t_pingfeature]: ...

    def possible_features(self) -> list[t_pingfeature]: ...

    def available_feature_groups(self, available: bool = True) -> list[t_pingfeature]: ...

    def possible_feature_groups(self) -> list[t_pingfeature]: ...

    def load(self, force: bool = False) -> None: ...

    def release(self) -> None: ...

    def loaded(self) -> bool: ...

    @overload
    def copy(self) -> I_PingWatercolumn:
        """return a copy using the c++ default copy constructor"""

    @overload
    def copy(self) -> I_PingWatercolumn: ...

    @overload
    def __copy__(self) -> I_PingWatercolumn: ...

    @overload
    def __copy__(self) -> I_PingWatercolumn: ...

    @overload
    def __deepcopy__(self, arg: dict, /) -> I_PingWatercolumn: ...

    @overload
    def __deepcopy__(self, arg: dict, /) -> I_PingWatercolumn: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def has_tx_signal_parameters(self) -> bool: ...

    def has_number_of_tx_sectors(self) -> bool: ...

    def has_beam_numbers_per_tx_sector(self) -> bool: ...

    def has_beam_selection_all(self) -> bool: ...

    def has_number_of_beams(self) -> bool: ...

    def has_tx_sector_per_beam(self) -> bool: ...

    def get_tx_signal_parameters(self) -> list[themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.CWSignalParameters | themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.FMSignalParameters | themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.GenericSignalParameters]: ...

    def get_number_of_tx_sectors(self) -> int: ...

    @overload
    def get_watercolumn_calibration(self) -> WaterColumnCalibration: ...

    @overload
    def get_watercolumn_calibration(self, sector_nr: int) -> WaterColumnCalibration: ...

    def get_multisectorwatercolumn_calibration(self) -> "themachinethatgoesping::echosounders::filetemplates::datatypes::calibration::I_MultiSectorCalibration": ...

    def get_beam_selection_all(self) -> themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection: ...

    def get_number_of_beams(self) -> int: ...

    @overload
    def get_beam_crosstrack_angles(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_beam_crosstrack_angles(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_beam_alongtrack_angles(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_beam_alongtrack_angles(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_beam_sample_selection_all(self) -> themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection: ...

    def get_first_sample_offset_per_beam(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    @overload
    def get_number_of_samples_per_beam(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    @overload
    def get_number_of_samples_per_beam(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    @overload
    def get_tx_sector_per_beam(self) -> Annotated[NDArray[numpy.uint64], dict(order='C')]: ...

    @overload
    def get_tx_sector_per_beam(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> Annotated[NDArray[numpy.uint64], dict(order='C')]: ...

    @overload
    def get_beam_numbers_per_tx_sector(self) -> list[list[int]]: ...

    @overload
    def get_beam_numbers_per_tx_sector(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> list[list[int]]: ...

    @overload
    def get_approximate_ranges(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_approximate_ranges(self, beam_sample_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_sound_speed_at_transducer(self) -> float: ...

    def get_sample_interval(self) -> float: ...

    def has_amplitudes(self) -> bool: ...

    def has_ap(self) -> bool: ...

    def has_av(self) -> bool: ...

    def has_power(self) -> bool: ...

    def has_rp(self) -> bool: ...

    def has_rv(self) -> bool: ...

    def has_pp(self) -> bool: ...

    def has_pv(self) -> bool: ...

    def has_sp(self) -> bool: ...

    def has_sv(self) -> bool: ...

    def has_watercolumn_calibration(self) -> bool: ...

    def has_multisectorwatercolumn_calibration(self) -> bool: ...

    @overload
    def get_amplitudes(self, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_amplitudes(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_rp(self, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_rp(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_rv(self, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_rv(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_pp(self, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_pp(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_pv(self, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_pv(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_ap(self, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_ap(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_av(self, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_av(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_power(self, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_power(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_sp(self, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_sp(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_sv(self, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_sv(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def has_bottom_range_samples(self) -> bool: ...

    @overload
    def get_bottom_range_samples(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    @overload
    def get_bottom_range_samples(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    @overload
    def get_minslant_sample_nr(self) -> int: ...

    @overload
    def get_minslant_sample_nr(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> int: ...

    @overload
    def get_wci_correction(self, calibration_type: o_calibration_type, calibration_base: o_calibration_type = t_calibration_type.power, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_wci_correction(self, beam_sample_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, calibration_type: o_calibration_type, calibration_base: o_calibration_type = t_calibration_type.power, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_wci(self, calibration_type: o_calibration_type, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_wci(self, beam_sample_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection, calibration_type: o_calibration_type, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

class I_Ping(I_PingCommon):
    def __init__(self) -> None: ...

    def feature_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered features that are available or not
        available

        Args:
            available: if True (default) return available features, else
                       return not available features

        Returns:
            std::string
        """

    def feature_groups_string(self, available: bool = True, prefix: str = '') -> str:
        """
        Get a string of all registered feature groups that are available or
        not available

        Args:
            available: if True (default) return available features, else
                       return not available features

        Returns:
            std::string
        """

    def has_any_of_features(self, feature_names: Sequence[o_pingfeature]) -> bool:
        """
        Check if any of the specified features is available

        Returns:
            true false
        """

    def has_all_of_features(self, feature_names: Sequence[o_pingfeature]) -> bool:
        """
        Check if all of the specified features are available

        Returns:
            true false
        """

    def has_features(self) -> bool:
        """
        Check if any of the registered features is available

        Returns:
            true false
        """

    def has_primary_features(self) -> bool:
        """
        Check if any of the registered main features is available

        Returns:
            true false
        """

    def registered_features(self) -> str:
        """
        Get a string of all registered features for this ping class

        Returns:
            std::string
        """

    def primary_features(self) -> str:
        """
        Get a string of all registered primary features for this ping class

        Returns:
            std::string
        """

    def has_feature(self, feature_name: o_pingfeature) -> bool:
        """
        Check if any of the registered features is available

        Returns:
            true false
        """

    def available_features(self, available_available: bool = True) -> list[t_pingfeature]: ...

    def possible_features(self) -> list[t_pingfeature]: ...

    def available_feature_groups(self, available: bool = True) -> list[t_pingfeature]: ...

    def possible_feature_groups(self) -> list[t_pingfeature]: ...

    def load(self, force: bool = False) -> None: ...

    def release(self) -> None: ...

    def loaded(self) -> bool: ...

    @overload
    def copy(self) -> I_Ping:
        """return a copy using the c++ default copy constructor"""

    @overload
    def copy(self) -> I_Ping: ...

    @overload
    def __copy__(self) -> I_Ping: ...

    @overload
    def __copy__(self) -> I_Ping: ...

    @overload
    def __deepcopy__(self, arg: dict, /) -> I_Ping: ...

    @overload
    def __deepcopy__(self, arg: dict, /) -> I_Ping: ...

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

    def has_timestamp(self) -> bool: ...

    def get_timestamp(self) -> float:
        """Unix timestamp in seconds (saved in UTC0)"""

    def set_timestamp(self, timestamp: float) -> None:
        """Unix timestamp in seconds (saved in UTC0)"""

    def has_datetime(self) -> bool:
        """
        Return true if the timestamp is available that can be converted to a datetime
        """

    def get_datetime(self, timezone_offset_hours: float = 0.0) -> object:
        """Return the timestamp as datetime object"""

    def set_datetime(self, datetime: object) -> None:
        """Set the timestamp using a datetime object"""

    def has_channel_id(self) -> bool: ...

    def get_channel_id(self) -> str:
        """channel id of the transducer"""

    def set_channel_id(self, channel_id: str) -> None:
        """channel id of the transducer"""

    def has_sensor_configuration(self) -> bool: ...

    def has_navigation_interpolator_latlon(self) -> bool: ...

    def has_sensor_data_latlon(self) -> bool: ...

    def get_sensor_configuration(self) -> themachinethatgoesping.navigation_nanopy.SensorConfiguration: ...

    def get_sensor_configuration_base_hash(self) -> int:
        """
        Returns the hash of the base sensor configuraiton. This is the sensor
        configuration with the "Transducer" target removed. This hash can be
        used to get the correct navigation interpolator from the
        navigation_data_interface Note: This function is for testing and
        finding errors. It is rather slow.

        Returns:
            uint64_t
        """

    def set_sensor_configuration(self, sensor_configuration: themachinethatgoesping.navigation_nanopy.SensorConfiguration) -> None: ...

    def get_navigation_interpolator_latlon(self) -> themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon: ...

    def set_navigation_interpolator_latlon(self, nav_interpolator: themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon) -> None: ...

    def get_sensor_data_latlon(self) -> themachinethatgoesping.navigation_nanopy.datastructures.SensordataLatLon: ...

    def has_geolocation(self) -> bool: ...

    def get_geolocation(self, target_id: str = 'Transducer') -> themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLatLon: ...

    @property
    def bottom(self) -> I_PingBottom: ...

    @property
    def watercolumn(self) -> I_PingWatercolumn: ...

    def has_bottom(self) -> bool: ...

    def has_watercolumn(self) -> bool: ...

class FilePackageCache_XML_Parameter_Channel:
    def __init__(self) -> None: ...

    def __eq__(self, other: FilePackageCache_XML_Parameter_Channel) -> bool: ...

    def get_package(self, file_pos: int, timestamp: float, sub_package_nr: int = 0) -> typing.Any: ...

    def get_packages(self, file_pos: int, timestamp: float) -> list[typing.Any]: ...

    def get_subpackage_count(self, file_pos: int) -> int: ...

    def has_package(self, file_pos: int) -> bool: ...

    def get_hash_cache(self) -> dict[int, str]: ...

    def get_package_buffer(self) -> dict[int, list[str]]: ...

    def copy(self) -> FilePackageCache_XML_Parameter_Channel:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> FilePackageCache_XML_Parameter_Channel: ...

    def __deepcopy__(self, arg: dict, /) -> FilePackageCache_XML_Parameter_Channel: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FilePackageCache_XML_Parameter_Channel:
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

class FileCache:
    @overload
    def __init__(self, file_name: str, file_size: int) -> None: ...

    @overload
    def __init__(self, index_path: str, file_name: str, file_size: int, cache_keys: Sequence[str] = []) -> None: ...

    def __eq__(self, other: FileCache) -> bool: ...

    def update_file(self, index_path: str, emulate_only: bool = False) -> None:
        """
        Update or create the cache file at the specified path

        Args:
            index_path: Path where to write the cache file
            emulate_only: If true, only simulate the update without actually
                          writing
        """

    @staticmethod
    def from_file(index_path: str) -> FileCache:
        """
        Create a FileCache from a file

        Args:
            index_path: Path to the cache file to read

        Returns:
            FileCache object created from the file
        """

    def remove_from_cache(self, name: str) -> None:
        """
        Remove a cache entry and all entries added after it

        Args:
            name: Name of the cache entry to remove
        """

    def get_cache_names(self) -> list[str]: ...

    def get_loaded_cache_names(self) -> list[str]: ...

    def get_not_loaded_cache_names(self) -> list[str]: ...

    def has_cache(self, cache_name: str) -> bool:
        """
        Check if a cache entry with the given name exists

        Args:
            name: Name of the cache entry to check

        Returns:
            true if the cache entry exists
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_cache_buffer(self) -> dict[str, str]: ...

    def get_cache_buffer_header(self) -> list[typing.Any]: ...

    def copy(self) -> FileCache:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> FileCache: ...

    def __deepcopy__(self, arg: dict, /) -> FileCache: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FileCache:
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
