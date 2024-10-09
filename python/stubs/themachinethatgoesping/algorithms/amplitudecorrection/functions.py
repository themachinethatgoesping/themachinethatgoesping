"""
M that holds functions used for amplitude corrections
"""
from __future__ import annotations
import numpy
import typing
__all__ = ['apply_beam_correction', 'apply_beam_sample_correction', 'apply_beam_sample_correction_loop', 'apply_beam_sample_correction_xsimd', 'apply_beam_sample_correction_xtensor2', 'apply_beam_sample_correction_xtensor3', 'apply_sample_correction', 'approximate_range_factor', 'approximate_ranges', 'calc_absorption_coefficient_db_m', 'calc_sound_velocity', 'compute_cw_range_correction', 'get_sample_numbers_plus_half']
@typing.overload
def apply_beam_correction(wci: numpy.ndarray[numpy.float32], per_beam_offset: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def apply_beam_correction(wci: numpy.ndarray[numpy.float64], per_beam_offset: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def apply_beam_sample_correction(wci: numpy.ndarray[numpy.float32], per_beam_offset: numpy.ndarray[numpy.float32], per_sample_offset: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def apply_beam_sample_correction(wci: numpy.ndarray[numpy.float64], per_beam_offset: numpy.ndarray[numpy.float64], per_sample_offset: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def apply_beam_sample_correction_loop(wci: numpy.ndarray[numpy.float32], per_beam_offset: numpy.ndarray[numpy.float32], per_sample_offset: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def apply_beam_sample_correction_loop(wci: numpy.ndarray[numpy.float64], per_beam_offset: numpy.ndarray[numpy.float64], per_sample_offset: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def apply_beam_sample_correction_xsimd(wci: numpy.ndarray[numpy.float32], per_beam_offset: numpy.ndarray[numpy.float32], per_sample_offset: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def apply_beam_sample_correction_xsimd(wci: numpy.ndarray[numpy.float64], per_beam_offset: numpy.ndarray[numpy.float64], per_sample_offset: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def apply_beam_sample_correction_xtensor2(wci: numpy.ndarray[numpy.float32], per_beam_offset: numpy.ndarray[numpy.float32], per_sample_offset: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def apply_beam_sample_correction_xtensor2(wci: numpy.ndarray[numpy.float64], per_beam_offset: numpy.ndarray[numpy.float64], per_sample_offset: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def apply_beam_sample_correction_xtensor3(wci: numpy.ndarray[numpy.float32], per_beam_offset: numpy.ndarray[numpy.float32], per_sample_offset: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def apply_beam_sample_correction_xtensor3(wci: numpy.ndarray[numpy.float64], per_beam_offset: numpy.ndarray[numpy.float64], per_sample_offset: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def apply_sample_correction(wci: numpy.ndarray[numpy.float32], per_sample_offset: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def apply_sample_correction(wci: numpy.ndarray[numpy.float64], per_sample_offset: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def approximate_range_factor(sample_interval_s: float, sound_velocity_m_s: float) -> float:
    ...
@typing.overload
def approximate_range_factor(sample_interval_s: float, sound_velocity_m_s: float) -> float:
    ...
@typing.overload
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, first_sample_nr: int, last_sample_nr: int, step: int = 1) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, sample_numbers: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, first_sample_nr: int, last_sample_nr: int, step: int = 1) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, sample_numbers: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def calc_absorption_coefficient_db_m(frequency_hz: float, depth_m: float, sound_velocity_m_s: float, temperature_c: float, salinity_psu: float, pH: float = 8) -> float:
    """
    Compute the logarithmic absorption coefficient in dB/m based on
    Francois and Garrison (1982) [taken from Fisheries Acoustics Theory
    and Practice, 2nd Edition, Simmonds and MacLennan, 2005]
    
    Parameter ``frequency_hz``:
        // Frequency_hz in Hz
    
    Parameter ``depth_m``:
        // Depth_m in m
    
    Parameter ``sound_velocity_m_s``:
        // Speed of sound in m/s
    
    Parameter ``temperature_c``:
        // ITS-90 temperature_c in degrees Celsius
    
    Parameter ``salinity_psu``:
        // Salinity in PSU
    
    Parameter ``pH``:
        // pH
    
    Returns:
        double
    """
@typing.overload
def calc_absorption_coefficient_db_m(frequency_hz: float, depth_m: float, sound_velocity_m_s: float, temperature_c: float, salinity_psu: float, pH: float = 8) -> float:
    """
    Compute the logarithmic absorption coefficient in dB/m based on
    Francois and Garrison (1982) [taken from Fisheries Acoustics Theory
    and Practice, 2nd Edition, Simmonds and MacLennan, 2005]
    
    Parameter ``frequency_hz``:
        // Frequency_hz in Hz
    
    Parameter ``depth_m``:
        // Depth_m in m
    
    Parameter ``sound_velocity_m_s``:
        // Speed of sound in m/s
    
    Parameter ``temperature_c``:
        // ITS-90 temperature_c in degrees Celsius
    
    Parameter ``salinity_psu``:
        // Salinity in PSU
    
    Parameter ``pH``:
        // pH
    
    Returns:
        double
    """
@typing.overload
def calc_sound_velocity(depth_m: float, temperature_c: float, salinity_psu: float, latitude: float = 0.0, longitude: float = 0.0) -> float:
    """
    Compute the speed of sound in seawater using the TEOS-10 library
    
    Parameter ``depth_m``:
        $Parameter ``temperature_c``:
    
    Parameter ``salinity_psu``:
        $Parameter ``latitude``:
    
    Parameter ``longitude``:
        $Returns:
    
    double
    """
@typing.overload
def calc_sound_velocity(depth_m: float, temperature_c: float, salinity_psu: float, latitude: float = 0.0, longitude: float = 0.0) -> float:
    """
    Compute the speed of sound in seawater using the TEOS-10 library
    
    Parameter ``depth_m``:
        $Parameter ``temperature_c``:
    
    Parameter ``salinity_psu``:
        $Parameter ``latitude``:
    
    Parameter ``longitude``:
        $Returns:
    
    double
    """
@typing.overload
def compute_cw_range_correction(ranges_m: numpy.ndarray[numpy.float32], absorption_db_m: float, tvg_factor: float) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def compute_cw_range_correction(ranges_m: numpy.ndarray[numpy.float64], absorption_db_m: float, tvg_factor: float) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def get_sample_numbers_plus_half(first_sample_nr: int, last_sample_nr: int, step: int = 1) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def get_sample_numbers_plus_half(first_sample_nr: int, last_sample_nr: int, step: int = 1) -> numpy.ndarray[numpy.float64]:
    ...
