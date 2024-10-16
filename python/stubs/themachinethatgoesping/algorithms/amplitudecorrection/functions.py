"""
M that holds functions used for amplitude corrections
"""
from __future__ import annotations
import numpy
import typing
__all__ = ['apply_beam_correction', 'apply_beam_sample_correction', 'apply_beam_sample_correction_loop', 'apply_beam_sample_correction_xsimd', 'apply_beam_sample_correction_xtensor2', 'apply_beam_sample_correction_xtensor3', 'apply_sample_correction', 'apply_system_offset', 'approximate_range_factor', 'approximate_ranges', 'calc_absorption_coefficient_db_m', 'calc_sound_velocity', 'compute_cw_range_correction', 'get_sample_numbers_plus_half', 'inplace_beam_correction', 'inplace_beam_sample_correction', 'inplace_sample_correction', 'inplace_system_offset']
@typing.overload
def apply_beam_correction(wci: numpy.ndarray[numpy.float32], per_beam_offset: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def apply_beam_correction(wci: numpy.ndarray[numpy.float64], per_beam_offset: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def apply_beam_sample_correction(wci: numpy.ndarray[numpy.float32], per_beam_offset: numpy.ndarray[numpy.float32], per_sample_offset: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
    """
    Applies beam and sample corrections to the given 2D tensor.
    
    Apply beam and sample corrections to the input 2D tensor. per_beam
    correction is applied to each sample in a beam, per_sample correction
    to each sample nr for each beam
    
    Template parameter ``t_xtensor_2d``:
        Type of the 2D tensor.
    
    Template parameter ``t_xtensor_1d``:
        Type of the 1D tensor.
    
    Parameter ``wci``:
        The input 2D tensor to which corrections will be applied.
    
    Parameter ``per_beam_offset``:
        A 1D tensor containing the per-beam offsets.
    
    Parameter ``per_sample_offset``:
        A 1D tensor containing the per-sample offsets.
    
    Parameter ``mp_cores``:
        The number of cores to use for parallel processing (default is 1).
    
    Returns:
        A 2D tensor with the applied beam and sample corrections.
    """
@typing.overload
def apply_beam_sample_correction(wci: numpy.ndarray[numpy.float64], per_beam_offset: numpy.ndarray[numpy.float64], per_sample_offset: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
    """
    Applies beam and sample corrections to the given 2D tensor.
    
    Apply beam and sample corrections to the input 2D tensor. per_beam
    correction is applied to each sample in a beam, per_sample correction
    to each sample nr for each beam
    
    Template parameter ``t_xtensor_2d``:
        Type of the 2D tensor.
    
    Template parameter ``t_xtensor_1d``:
        Type of the 1D tensor.
    
    Parameter ``wci``:
        The input 2D tensor to which corrections will be applied.
    
    Parameter ``per_beam_offset``:
        A 1D tensor containing the per-beam offsets.
    
    Parameter ``per_sample_offset``:
        A 1D tensor containing the per-sample offsets.
    
    Parameter ``mp_cores``:
        The number of cores to use for parallel processing (default is 1).
    
    Returns:
        A 2D tensor with the applied beam and sample corrections.
    """
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
def apply_system_offset(wci: numpy.ndarray[numpy.float32], system_offset: float, mp_cores: int = 1) -> numpy.ndarray[numpy.float32]:
    ...
@typing.overload
def apply_system_offset(wci: numpy.ndarray[numpy.float64], system_offset: float, mp_cores: int = 1) -> numpy.ndarray[numpy.float64]:
    ...
@typing.overload
def approximate_range_factor(sample_interval_s: float, sound_velocity_m_s: float) -> float:
    """
    Approximates the range factor based on the sample interval and a
    single sound velocity.
    
    This function calculates the range factor using the given sample
    interval and sound velocity. The formula used is: range_factor =
    sample_interval_s * sound_velocity_m_s * 0.5
    
    Template parameter ``t_float``:
        The floating-point type used for the calculations.
    
    Parameter ``sample_interval_s``:
        The sample interval in seconds.
    
    Parameter ``sound_velocity_m_s``:
        The sound velocity in meters per second.
    
    Returns:
        The approximated range factor.
    """
@typing.overload
def approximate_range_factor(sample_interval_s: float, sound_velocity_m_s: float) -> float:
    """
    Approximates the range factor based on the sample interval and a
    single sound velocity.
    
    This function calculates the range factor using the given sample
    interval and sound velocity. The formula used is: range_factor =
    sample_interval_s * sound_velocity_m_s * 0.5
    
    Template parameter ``t_float``:
        The floating-point type used for the calculations.
    
    Parameter ``sample_interval_s``:
        The sample interval in seconds.
    
    Parameter ``sound_velocity_m_s``:
        The sound velocity in meters per second.
    
    Returns:
        The approximated range factor.
    """
@typing.overload
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, first_sample_nr: int, last_sample_nr: int, step: int = 1) -> numpy.ndarray[numpy.float32]:
    """
    Approximates the ranges based on the provided sample interval and a
    single sound velocity.
    
    This function calculates the approximate ranges for a given set of
    sample numbers by multiplying the sample numbers (plus half) with the
    approximate range factor.
    
    Template parameter ``t_xtensor_1d``:
        A 1D tensor type that satisfies the c_xtensor_1d concept.
    
    Template parameter ``t_int``:
        An integer type for sample numbers.
    
    Parameter ``sample_interval_s``:
        The sample interval in seconds.
    
    Parameter ``sound_velocity_m_s``:
        The sound velocity in meters per second.
    
    Parameter ``first_sample_nr``:
        The first sample number.
    
    Parameter ``last_sample_nr``:
        The last sample number.
    
    Parameter ``step``:
        The step size between sample numbers (default is 1).
    
    Returns:
        A 1D tensor containing the approximated ranges.
    """
@typing.overload
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, sample_numbers: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.float32]:
    """
    Approximates the ranges based on sample interval, a single sound
    velocity, and sample numbers.
    
    This function calculates the approximate ranges by using the provided
    sample interval, sound velocity, and sample numbers. The calculation
    is performed by adding 0.5 to each sample number and then multiplying
    by the approximate range factor.
    
    Template parameter ``t_xtensor_1d``:
        A 1D tensor type that satisfies the tools::helper::c_xtensor
        concept.
    
    Template parameter ``t_xtensor_1d_int``:
        A 1D tensor type for integers that satisfies the
        tools::helper::c_xtensor concept.
    
    Parameter ``sample_interval_s``:
        The interval between samples in seconds.
    
    Parameter ``sound_velocity_m_s``:
        The velocity of sound in meters per second.
    
    Parameter ``sample_numbers``:
        A 1D tensor containing the sample numbers.
    
    Returns:
        A 1D tensor containing the approximated ranges.
    """
@typing.overload
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, first_sample_nr: int, last_sample_nr: int, step: int = 1) -> numpy.ndarray[numpy.float64]:
    """
    Approximates the ranges based on the provided sample interval and a
    single sound velocity.
    
    This function calculates the approximate ranges for a given set of
    sample numbers by multiplying the sample numbers (plus half) with the
    approximate range factor.
    
    Template parameter ``t_xtensor_1d``:
        A 1D tensor type that satisfies the c_xtensor_1d concept.
    
    Template parameter ``t_int``:
        An integer type for sample numbers.
    
    Parameter ``sample_interval_s``:
        The sample interval in seconds.
    
    Parameter ``sound_velocity_m_s``:
        The sound velocity in meters per second.
    
    Parameter ``first_sample_nr``:
        The first sample number.
    
    Parameter ``last_sample_nr``:
        The last sample number.
    
    Parameter ``step``:
        The step size between sample numbers (default is 1).
    
    Returns:
        A 1D tensor containing the approximated ranges.
    """
@typing.overload
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, sample_numbers: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.float64]:
    """
    Approximates the ranges based on sample interval, a single sound
    velocity, and sample numbers.
    
    This function calculates the approximate ranges by using the provided
    sample interval, sound velocity, and sample numbers. The calculation
    is performed by adding 0.5 to each sample number and then multiplying
    by the approximate range factor.
    
    Template parameter ``t_xtensor_1d``:
        A 1D tensor type that satisfies the tools::helper::c_xtensor
        concept.
    
    Template parameter ``t_xtensor_1d_int``:
        A 1D tensor type for integers that satisfies the
        tools::helper::c_xtensor concept.
    
    Parameter ``sample_interval_s``:
        The interval between samples in seconds.
    
    Parameter ``sound_velocity_m_s``:
        The velocity of sound in meters per second.
    
    Parameter ``sample_numbers``:
        A 1D tensor containing the sample numbers.
    
    Returns:
        A 1D tensor containing the approximated ranges.
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
def compute_cw_range_correction(ranges_m: numpy.ndarray[numpy.float32], absorption_db_m: float | None, tvg_factor: float | None) -> numpy.ndarray[numpy.float32]:
    """
    Computes the continuous wave (CW) range correction.
    
    This function calculates the range correction based on the provided
    ranges, absorption coefficient, and time-varying gain (TVG) factor.
    The range correction is computed using the formula:
    
    \f[ \text{range correction} = 2 \cdot \text{absorption\_db\_m} \cdot
    \text{ranges\_m} + \text{tvg\_factor} \cdot
    \log_{10}(\text{ranges\_m}) \f]
    
    If the absorption coefficient is finite and non-zero, it is used in
    the calculation. If the TVG factor is finite and non-zero, it is also
    included in the calculation. If neither the absorption coefficient nor
    the TVG factor are finite and non-zero, the function returns a tensor
    of zeros with the same shape as the input ranges.
    
    Template parameter ``t_xtensor_1d``:
        A 1D tensor type that satisfies the tools::helper::c_xtensor_1d
        concept.
    
    Parameter ``ranges_m``:
        A 1D tensor representing the ranges in meters.
    
    Parameter ``absorption_db_m``:
        The absorption coefficient in decibels per meter.
    
    Parameter ``tvg_factor``:
        The time-varying gain factor.
    
    Returns:
        A 1D tensor representing the computed range correction.
    """
@typing.overload
def compute_cw_range_correction(ranges_m: numpy.ndarray[numpy.float64], absorption_db_m: float | None, tvg_factor: float | None) -> numpy.ndarray[numpy.float64]:
    """
    Computes the continuous wave (CW) range correction.
    
    This function calculates the range correction based on the provided
    ranges, absorption coefficient, and time-varying gain (TVG) factor.
    The range correction is computed using the formula:
    
    \f[ \text{range correction} = 2 \cdot \text{absorption\_db\_m} \cdot
    \text{ranges\_m} + \text{tvg\_factor} \cdot
    \log_{10}(\text{ranges\_m}) \f]
    
    If the absorption coefficient is finite and non-zero, it is used in
    the calculation. If the TVG factor is finite and non-zero, it is also
    included in the calculation. If neither the absorption coefficient nor
    the TVG factor are finite and non-zero, the function returns a tensor
    of zeros with the same shape as the input ranges.
    
    Template parameter ``t_xtensor_1d``:
        A 1D tensor type that satisfies the tools::helper::c_xtensor_1d
        concept.
    
    Parameter ``ranges_m``:
        A 1D tensor representing the ranges in meters.
    
    Parameter ``absorption_db_m``:
        The absorption coefficient in decibels per meter.
    
    Parameter ``tvg_factor``:
        The time-varying gain factor.
    
    Returns:
        A 1D tensor representing the computed range correction.
    """
@typing.overload
def get_sample_numbers_plus_half(first_sample_nr: int, last_sample_nr: int, step: int = 1) -> numpy.ndarray[numpy.float32]:
    """
    Generates a 1D tensor of sample numbers incremented by half. (used for
    range compuation)
    
    This function calculates a range of sample numbers starting from
    `first_sample_nr + 0.5` to `last_sample_nr + 1.5` with a specified
    step.
    
    Template parameter ``t_xtensor_1d``:
        A 1D tensor type that satisfies the `tools::helper::c_xtensor`
        concept.
    
    Template parameter ``t_int``:
        An integer type for the sample numbers.
    
    Parameter ``first_sample_nr``:
        The starting sample number.
    
    Parameter ``last_sample_nr``:
        The ending sample number.
    
    Parameter ``step``:
        The step size for the range (default is 1).
    
    Returns:
        A 1D tensor of sample numbers incremented by half. @note The
        template parameter must be a 1D tensor.
    """
@typing.overload
def get_sample_numbers_plus_half(first_sample_nr: int, last_sample_nr: int, step: int = 1) -> numpy.ndarray[numpy.float64]:
    """
    Generates a 1D tensor of sample numbers incremented by half. (used for
    range compuation)
    
    This function calculates a range of sample numbers starting from
    `first_sample_nr + 0.5` to `last_sample_nr + 1.5` with a specified
    step.
    
    Template parameter ``t_xtensor_1d``:
        A 1D tensor type that satisfies the `tools::helper::c_xtensor`
        concept.
    
    Template parameter ``t_int``:
        An integer type for the sample numbers.
    
    Parameter ``first_sample_nr``:
        The starting sample number.
    
    Parameter ``last_sample_nr``:
        The ending sample number.
    
    Parameter ``step``:
        The step size for the range (default is 1).
    
    Returns:
        A 1D tensor of sample numbers incremented by half. @note The
        template parameter must be a 1D tensor.
    """
@typing.overload
def inplace_beam_correction(wci: numpy.ndarray[numpy.float32], per_beam_offset: numpy.ndarray[numpy.float32], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
    ...
@typing.overload
def inplace_beam_correction(wci: numpy.ndarray[numpy.float64], per_beam_offset: numpy.ndarray[numpy.float64], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
    ...
@typing.overload
def inplace_beam_sample_correction(wci: numpy.ndarray[numpy.float32], per_beam_offset: numpy.ndarray[numpy.float32], per_sample_offset: numpy.ndarray[numpy.float32], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
    ...
@typing.overload
def inplace_beam_sample_correction(wci: numpy.ndarray[numpy.float64], per_beam_offset: numpy.ndarray[numpy.float64], per_sample_offset: numpy.ndarray[numpy.float64], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
    ...
@typing.overload
def inplace_sample_correction(wci: numpy.ndarray[numpy.float32], per_sample_offset: numpy.ndarray[numpy.float32], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
    ...
@typing.overload
def inplace_sample_correction(wci: numpy.ndarray[numpy.float64], per_sample_offset: numpy.ndarray[numpy.float64], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
    ...
@typing.overload
def inplace_system_offset(wci: numpy.ndarray[numpy.float32], system_offset: float, min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
    ...
@typing.overload
def inplace_system_offset(wci: numpy.ndarray[numpy.float64], system_offset: float, min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
    ...
