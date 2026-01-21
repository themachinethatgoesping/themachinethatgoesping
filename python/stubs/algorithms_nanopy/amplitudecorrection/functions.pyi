from typing import Annotated, overload

import numpy
from numpy.typing import NDArray


@overload
def calc_sound_velocity(depth_m: float, temperature_c: float, salinity_psu: float, latitude: float = 0.0, longitude: float = 0.0) -> float:
    """
    Compute the speed of sound in seawater using the TEOS-10 library

    Args:
        depth_m: 
        temperature_c: 
        salinity_psu: 
        latitude: 
        longitude: 

    Returns:
        double
    """

@overload
def calc_sound_velocity(depth_m: float, temperature_c: float, salinity_psu: float, latitude: float = 0.0, longitude: float = 0.0) -> float: ...

@overload
def calc_absorption_coefficient_db_m(frequency_hz: float, depth_m: float, sound_velocity_m_s: float, temperature_c: float, salinity_psu: float, pH: float = 8) -> float:
    """
    Compute the logarithmic absorption coefficient in dB/m based on
    Francois and Garrison
    (1982) [taken from Fisheries Acoustics Theory and Practice, 2nd
           Edition, Simmonds and MacLennan,
    2005]

    Args:
        frequency_hz: // Frequency_hz in Hz
        depth_m: // Depth_m in m
        sound_velocity_m_s: // Speed of sound in m/s
        temperature_c: // ITS-90 temperature_c in degrees Celsius
        salinity_psu: // Salinity in PSU
        pH: // pH

    Returns:
        double
    """

@overload
def calc_absorption_coefficient_db_m(frequency_hz: float, depth_m: float, sound_velocity_m_s: float, temperature_c: float, salinity_psu: float, pH: float = 8) -> float: ...

@overload
def get_sample_numbers_plus_half(first_sample_nr: int, last_sample_nr: int, step: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]:
    """
    Generates a 1D tensor of sample numbers incremented by half. (used for
    range compuation)

    This function calculates a range of sample numbers starting from
    `first_sample_nr + 0.5` to `last_sample_nr + 1.5` with a specified
    step.

    Args:
        first_sample_nr: The starting sample number.
        last_sample_nr: The ending sample number.
        step: The step size for the range (default is 1).

    Template Args:
        t_xtensor_1d: A 1D tensor type that satisfies the
                      `tools::helper::c_xtensor` concept.
        t_int: An integer type for the sample numbers.

    Returns:
        A 1D tensor of sample numbers incremented by half.

    @note The template parameter must be a 1D tensor.
    """

@overload
def get_sample_numbers_plus_half(first_sample_nr: int, last_sample_nr: int, step: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]: ...

@overload
def approximate_range_factor(sample_interval_s: float, sound_velocity_m_s: float) -> float:
    """
    Approximates the range factor based on the sample interval and a
    single sound velocity.

    This function calculates the range factor using the given sample
    interval and sound velocity. The formula used is: range_factor =
    sample_interval_s * sound_velocity_m_s * 0.5

    Args:
        sample_interval_s: The sample interval in seconds.
        sound_velocity_m_s: The sound velocity in meters per second.

    Template Args:
        t_float: The floating-point type used for the calculations.

    Returns:
        The approximated range factor.
    """

@overload
def approximate_range_factor(sample_interval_s: float, sound_velocity_m_s: float) -> float: ...

@overload
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, first_sample_nr: int, last_sample_nr: int, step: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]:
    """
    Approximates the ranges based on the provided sample interval and a
    single sound velocity.

    This function calculates the approximate ranges for a given set of
    sample numbers by multiplying the sample numbers (plus half) with the
    approximate range factor.

    Args:
        sample_interval_s: The sample interval in seconds.
        sound_velocity_m_s: The sound velocity in meters per second.
        first_sample_nr: The first sample number.
        last_sample_nr: The last sample number.
        step: The step size between sample numbers (default is 1).

    Template Args:
        t_xtensor_1d: A 1D tensor type that satisfies the c_xtensor_1d
                      concept.
        t_int: An integer type for sample numbers.

    Returns:
        A 1D tensor containing the approximated ranges.
    """

@overload
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, sample_numbers: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='A')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]:
    """
    Approximates the ranges based on sample interval, a single sound
    velocity, and sample numbers.

    This function calculates the approximate ranges by using the provided
    sample interval, sound velocity, and sample numbers. The calculation
    is performed by adding 0.5 to each sample number and then multiplying
    by the approximate range factor.

    Args:
        sample_interval_s: The interval between samples in seconds.
        sound_velocity_m_s: The velocity of sound in meters per second.
        sample_numbers: A 1D tensor containing the sample numbers.

    Template Args:
        t_xtensor_1d: A 1D tensor type that satisfies the
                      tools::helper::c_xtensor concept.
        t_xtensor_1d_int: A 1D tensor type for integers that satisfies the
                          tools::helper::c_xtensor concept.

    Returns:
        A 1D tensor containing the approximated ranges.
    """

@overload
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, first_sample_nr: int, last_sample_nr: int, step: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]:
    """
    Approximates the ranges based on the provided sample interval and a
    single sound velocity.

    This function calculates the approximate ranges for a given set of
    sample numbers by multiplying the sample numbers (plus half) with the
    approximate range factor.

    Args:
        sample_interval_s: The sample interval in seconds.
        sound_velocity_m_s: The sound velocity in meters per second.
        first_sample_nr: The first sample number.
        last_sample_nr: The last sample number.
        step: The step size between sample numbers (default is 1).

    Template Args:
        t_xtensor_1d: A 1D tensor type that satisfies the c_xtensor_1d
                      concept.
        t_int: An integer type for sample numbers.

    Returns:
        A 1D tensor containing the approximated ranges.
    """

@overload
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, sample_numbers: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='A')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]:
    """
    Approximates the ranges based on sample interval, a single sound
    velocity, and sample numbers.

    This function calculates the approximate ranges by using the provided
    sample interval, sound velocity, and sample numbers. The calculation
    is performed by adding 0.5 to each sample number and then multiplying
    by the approximate range factor.

    Args:
        sample_interval_s: The interval between samples in seconds.
        sound_velocity_m_s: The velocity of sound in meters per second.
        sample_numbers: A 1D tensor containing the sample numbers.

    Template Args:
        t_xtensor_1d: A 1D tensor type that satisfies the
                      tools::helper::c_xtensor concept.
        t_xtensor_1d_int: A 1D tensor type for integers that satisfies the
                          tools::helper::c_xtensor concept.

    Returns:
        A 1D tensor containing the approximated ranges.
    """

@overload
def compute_cw_range_correction(ranges_m: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], absorption_db_m: float, tvg_factor: float) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]:
    r"""
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

    Args:
        ranges_m: A 1D tensor representing the ranges in meters.
        absorption_db_m: The absorption coefficient in decibels per meter.
        tvg_factor: The time-varying gain factor.

    Template Args:
        t_xtensor_1d: A 1D tensor type that satisfies the
                      tools::helper::c_xtensor_1d concept.

    Returns:
        A 1D tensor representing the computed range correction.
    """

@overload
def compute_cw_range_correction(ranges_m: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], absorption_db_m: float, tvg_factor: float) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]: ...

@overload
def compute_cw_range_correction_per_beam(ranges_m: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], tvg_factor: float, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]:
    r"""
    Computes the per-beam continuous wave (CW) range correction for 2D
    water column data.

    This function calculates the range correction for each beam
    individually, allowing for per-beam absorption coefficients. This is
    useful for multi-sector sonars where each transmit sector may have a
    different absorption coefficient.

    The range correction for each beam is computed using the formula: \f[
    \text{range correction}[beam, sample] = 2 \cdot
    \text{absorption\_db\_m}[beam] \cdot \text{ranges\_m}[sample] +
    \text{tvg\_factor} \cdot \log_{10}(\text{ranges\_m}[sample]) \f]

    Args:
        ranges_m: A 1D tensor representing the ranges in meters (size =
                  number of samples).
        absorption_db_m_per_beam: A 1D tensor of absorption coefficients
                                  in dB/m per beam (size = number of
                                  beams).
        tvg_factor: Optional time-varying gain factor (applied uniformly
                    to all beams).
        mp_cores: The number of cores to use for parallel processing
                  (default is 1).

    Template Args:
        t_xtensor_2d: A 2D tensor type that satisfies the
                      tools::helper::c_xtensor_2d concept.
        t_xtensor_1d: A 1D tensor type that satisfies the
                      tools::helper::c_xtensor_1d concept.

    Returns:
        A 2D tensor (beams x samples) representing the computed range
        correction per beam.
    """

@overload
def compute_cw_range_correction_per_beam(ranges_m: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], tvg_factor: float, mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

@overload
def apply_beam_sample_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]:
    """
    Applies beam and sample corrections to the given 2D tensor.

    Apply beam and sample corrections to the input 2D tensor. per_beam
    correction is applied to each sample in a beam, per_sample correction
    to each sample nr for each beam

    Args:
        wci: The input 2D tensor to which corrections will be applied.
        per_beam_offset: A 1D tensor containing the per-beam offsets.
        per_sample_offset: A 1D tensor containing the per-sample offsets.
        mp_cores: The number of cores to use for parallel processing
                  (default is 1).

    Template Args:
        t_xtensor_2d: Type of the 2D tensor.
        t_xtensor_1d: Type of the 1D tensor.

    Returns:
        A 2D tensor with the applied beam and sample corrections.
    """

@overload
def apply_beam_sample_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

@overload
def apply_beam_sample_correction_with_absorption(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges_m: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]:
    """
    Applies beam, sample, and per-beam absorption corrections to the given
    2D tensor.

    This function applies per-beam offset, per-sample offset, and per-beam
    absorption correction to the input 2D tensor. The absorption
    correction is computed as 2 * absorption_db_m * ranges_m for each beam
    individually, allowing for multi-sector sonar data with different
    absorption coefficients per sector/beam.

    Args:
        wci: The input 2D tensor to which corrections will be applied.
        per_beam_offset: A 1D tensor containing the per-beam offsets (size
                         = number of beams).
        per_sample_offset: A 1D tensor containing the per-sample offsets
                           (size = number of samples).
        ranges_m: A 1D tensor containing the ranges in meters (size =
                  number of samples).
        absorption_db_m_per_beam: A 1D tensor of absorption coefficients
                                  in dB/m per beam (size = number of
                                  beams).
        mp_cores: The number of cores to use for parallel processing
                  (default is 1).

    Template Args:
        t_xtensor_2d: Type of the 2D tensor.
        t_xtensor_1d: Type of the 1D tensor.

    Returns:
        A 2D tensor with the applied corrections.
    """

@overload
def apply_beam_sample_correction_with_absorption(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges_m: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

@overload
def apply_beam_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

@overload
def apply_beam_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

@overload
def apply_sample_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

@overload
def apply_sample_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

@overload
def apply_system_offset(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], system_offset: float, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

@overload
def apply_system_offset(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], system_offset: float, mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

@overload
def inplace_beam_sample_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_beam_sample_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_beam_sample_correction_with_absorption(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges_m: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
    """
    Inplace applies beam, sample, and per-beam absorption corrections to
    the given 2D tensor.

    This function applies per-beam offset, per-sample offset, and per-beam
    absorption correction in-place to the input 2D tensor. The absorption
    correction is computed as 2 * absorption_db_m * ranges_m for each beam
    individually.

    Args:
        wci: The input 2D tensor to which corrections will be applied
             (modified in-place).
        per_beam_offset: A 1D tensor containing the per-beam offsets (size
                         = number of beams).
        per_sample_offset: A 1D tensor containing the per-sample offsets
                           (size = number of samples).
        ranges_m: A 1D tensor containing the ranges in meters (size =
                  number of samples).
        absorption_db_m_per_beam: A 1D tensor of absorption coefficients
                                  in dB/m per beam (size = number of
                                  beams).
        min_beam_index: Optional minimum beam index to start correction
                        from.
        max_beam_index: Optional maximum beam index to end correction at.
        mp_cores: The number of cores to use for parallel processing
                  (default is 1).

    Template Args:
        t_xtensor_2d: Type of the 2D tensor.
        t_xtensor_1d: Type of the 1D tensor.
    """

@overload
def inplace_beam_sample_correction_with_absorption(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges_m: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_sample_correction_with_absorption(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges_m: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
    """
    Inplace applies sample and per-beam absorption corrections to the
    given 2D tensor.

    This function applies per-sample offset and per-beam absorption
    correction in-place to the input 2D tensor (without per-beam offset).
    The absorption correction is computed as 2 * absorption_db_m
    * ranges_m for each beam individually.

    Args:
        wci: The input 2D tensor to which corrections will be applied
             (modified in-place).
        per_sample_offset: A 1D tensor containing the per-sample offsets
                           (size = number of samples).
        ranges_m: A 1D tensor containing the ranges in meters (size =
                  number of samples).
        absorption_db_m_per_beam: A 1D tensor of absorption coefficients
                                  in dB/m per beam (size = number of
                                  beams).
        min_beam_index: Optional minimum beam index to start correction
                        from.
        max_beam_index: Optional maximum beam index to end correction at.
        mp_cores: The number of cores to use for parallel processing
                  (default is 1).

    Template Args:
        t_xtensor_2d: Type of the 2D tensor.
        t_xtensor_1d: Type of the 1D tensor.
    """

@overload
def inplace_sample_correction_with_absorption(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges_m: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_beam_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_beam_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_sample_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_sample_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_system_offset(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], system_offset: float, min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_system_offset(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], system_offset: float, min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def apply_beam_sample_correction_loop(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

@overload
def apply_beam_sample_correction_loop(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

@overload
def apply_beam_sample_correction_xtensor2(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

@overload
def apply_beam_sample_correction_xtensor2(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

@overload
def apply_beam_sample_correction_xtensor3(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

@overload
def apply_beam_sample_correction_xtensor3(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

@overload
def apply_beam_sample_correction_xsimd(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

@overload
def apply_beam_sample_correction_xsimd(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...
