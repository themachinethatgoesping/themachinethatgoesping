"""M that holds functions used for amplitude corrections"""

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
def get_sample_numbers_plus_half(first_sample_nr: int, last_sample_nr: int, step: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
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
def get_sample_numbers_plus_half(first_sample_nr: int, last_sample_nr: int, step: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

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
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, first_sample_nr: int, last_sample_nr: int, step: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
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
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, sample_numbers: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
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
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, first_sample_nr: int, last_sample_nr: int, step: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
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
def approximate_ranges(sample_interval_s: float, sound_velocity_m_s: float, sample_numbers: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
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
def compute_cw_range_correction(ranges_m: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m: float | None, tvg_factor: float | None) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
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
def compute_cw_range_correction(ranges_m: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m: float | None, tvg_factor: float | None) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def compute_cw_range_correction_per_beam(ranges_m: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], tvg_factor: float | None, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
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
def compute_cw_range_correction_per_beam(ranges_m: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], tvg_factor: float | None, mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

@overload
def apply_beam_sample_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
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
def apply_beam_sample_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

@overload
def apply_beam_sample_correction_with_absorption(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges_m: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
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
def apply_beam_sample_correction_with_absorption(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges_m: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

@overload
def apply_beam_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

@overload
def apply_beam_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

@overload
def apply_sample_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

@overload
def apply_sample_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

@overload
def apply_system_offset(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], system_offset: float, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

@overload
def apply_system_offset(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], system_offset: float, mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

@overload
def inplace_beam_sample_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_beam_sample_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_beam_sample_correction_with_absorption(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges_m: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
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
def inplace_beam_sample_correction_with_absorption(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges_m: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_sample_correction_with_absorption(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges_m: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
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
def inplace_sample_correction_with_absorption(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges_m: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_beam_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_beam_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_sample_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_sample_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_system_offset(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], system_offset: float, min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def inplace_system_offset(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], system_offset: float, min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def compute_nanmean_across_beams(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
    """
    Compute the mean value across all beams for each sample position,
    ignoring NaN.

    For a WCI tensor of shape (n_beams x n_samples), this computes the
    NaN-aware mean along axis 0 (beams), producing a 1D tensor of shape
    (n_samples).

    This is the first step of the SRSN sidelobe correction: computing the
    average signal level across all beams at each range/sample position.

    NaN values are excluded from the mean (equivalent to MATLAB
    mean(...,'omitnan')). If all beams at a sample position are NaN, the
    result for that sample is NaN.

    Args:
        wci: The input 2D WCI tensor (beams x samples).
        mp_cores: The number of cores to use for parallel processing
                  (default is 1).

    Template Args:
        t_xtensor_2d: Type of the 2D input tensor (beams x samples).
        t_xtensor_1d: Type of the 1D output tensor (samples).

    Returns:
        A 1D tensor of shape (n_samples) with the NaN-aware mean across
        beams.
    """

@overload
def compute_nanmean_across_beams(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def compute_nanmedian_across_beams(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
    """
    Compute the median value across all beams for each sample position,
    ignoring NaN.

    For a WCI tensor of shape (n_beams x n_samples), this computes the
    NaN-aware median along axis 0 (beams), producing a 1D tensor of shape
    (n_samples).

    The median is more robust to outliers than the mean, which can be
    useful when strong targets (e.g., fish schools) are present in a few
    beams.

    NaN values are excluded before computing the median (equivalent to
    MATLAB median(...,'omitnan')). If all beams at a sample position are
    NaN, the result for that sample is NaN.

    Uses std::nth_element for O(n) average complexity per sample. The
    computation across samples is parallelized with OpenMP.

    Args:
        wci: The input 2D WCI tensor (beams x samples).
        mp_cores: The number of cores to use for parallel processing
                  (default is 1).

    Template Args:
        t_xtensor_2d: Type of the 2D input tensor (beams x samples).
        t_xtensor_1d: Type of the 1D output tensor (samples).

    Returns:
        A 1D tensor of shape (n_samples) with the NaN-aware median across
        beams.
    """

@overload
def compute_nanmedian_across_beams(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def compute_reference_nanmean(wci_region: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]) -> float:
    """
    Compute a reference level as the NaN-aware mean of all elements in a
    2D WCI region.

    This is used in the SRSN algorithm to compute a reference level from
    the "clean" water column (e.g., data above the minimum slant range).
    The caller should extract the appropriate sub-region before calling
    this function.

    NaN values are excluded from the computation.

    Args:
        wci_region: A 2D tensor representing the reference region (e.g.,
                    clean WC above bottom).

    Template Args:
        t_xtensor_2d: Type of the 2D tensor.

    Returns:
        The NaN-aware mean of all elements as a scalar.
    """

@overload
def compute_reference_nanmean(wci_region: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]) -> float: ...

@overload
def compute_reference_nanpercentile(wci_region: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], percentile: float) -> float:
    """
    Compute a reference level as a NaN-aware percentile of all elements in
    a 2D WCI region.

    This is used in the SRSN algorithm to compute a reference level from
    the "clean" water column. Common choices are the 25th percentile
    (default in Schimel et al., 2020), 5th, 10th percentile, or 50th
    percentile (median).

    NaN values are excluded before computing the percentile.

    Args:
        wci_region: A 2D tensor representing the reference region (e.g.,
                    clean WC above bottom).
        percentile: The percentile to compute, in range [0, 100]. E.g., 25
                    for 25th percentile.

    Template Args:
        t_xtensor_2d: Type of the 2D tensor.

    Returns:
        The NaN-aware percentile of all elements as a scalar.
    """

@overload
def compute_reference_nanpercentile(wci_region: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], percentile: float) -> float: ...

@overload
def apply_wci_sidelobe_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_sample_average: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], reference_level: float, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
    """
    Apply SRSN sidelobe correction to a WCI tensor.

    Applies the Slant Range Signal Normalization by subtracting the per-
    sample average across beams and adding a reference level:

      result[beam, sample] = wci[beam, sample] -
      per_sample_average[sample] + reference_level

    The per_sample_average should be precomputed using
    compute_nanmean_across_beams or compute_nanmedian_across_beams. The
    reference_level is a scalar that re-anchors the corrected data to a
    meaningful dB range (e.g., computed via compute_reference_nanmean or
    compute_reference_nanpercentile).

    Reference: Schimel, A.C.G. et al. (2020). "Multibeam Sonar Backscatter
               Data
    Processing." Remote Sensing, 12(9), 1371.

    Args:
        wci: The input 2D WCI tensor (beams x samples).
        per_sample_average: A 1D tensor (n_samples) with the average
                            across beams.
        reference_level: A scalar reference level (dB) to re-anchor the
                         data.
        mp_cores: The number of cores to use for parallel processing
                  (default is 1).

    Template Args:
        t_xtensor_2d: Type of the 2D tensor (beams x samples).
        t_xtensor_1d: Type of the 1D tensor (samples).

    Returns:
        A 2D tensor with the sidelobe correction applied.
    """

@overload
def apply_wci_sidelobe_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_sample_average: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], reference_level: float, mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

@overload
def inplace_wci_sidelobe_correction(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_sample_average: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], reference_level: float, min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None:
    """
    Inplace apply SRSN sidelobe correction to a WCI tensor.

    Applies the Slant Range Signal Normalization in-place:

      wci[beam, sample] += reference_level - per_sample_average[sample]

    Optionally limits correction to a beam index range [min_beam_index,
    max_beam_index].

    Args:
        wci: The 2D WCI tensor to correct in-place (beams x samples).
        per_sample_average: A 1D tensor (n_samples) with the average
                            across beams.
        reference_level: A scalar reference level (dB) to re-anchor the
                         data.
        min_beam_index: Optional minimum beam index to start correction
                        from.
        max_beam_index: Optional maximum beam index to end correction at.
        mp_cores: The number of cores to use for parallel processing
                  (default is 1).

    Template Args:
        t_xtensor_2d: Type of the 2D tensor (beams x samples).
        t_xtensor_1d: Type of the 1D tensor (samples).
    """

@overload
def inplace_wci_sidelobe_correction(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_sample_average: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], reference_level: float, min_beam_index: int | None = None, max_beam_index: int | None = None, mp_cores: int = 1) -> None: ...

@overload
def apply_beam_sample_correction_loop(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

@overload
def apply_beam_sample_correction_loop(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

@overload
def apply_beam_sample_correction_xtensor2(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

@overload
def apply_beam_sample_correction_xtensor2(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

@overload
def apply_beam_sample_correction_xtensor3(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

@overload
def apply_beam_sample_correction_xtensor3(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

@overload
def apply_beam_sample_correction_xsimd(wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

@overload
def apply_beam_sample_correction_xsimd(wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], per_beam_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], per_sample_offset: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...
