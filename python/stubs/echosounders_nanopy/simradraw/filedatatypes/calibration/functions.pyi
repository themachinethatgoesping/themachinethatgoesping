"""Functions used for Simrad RAW water column calibration"""
import typing

from typing import Annotated, overload

import numpy
from numpy.typing import NDArray


def hann_f(length: int) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]:
    """
    Generate Hann window weights of a given length.

    Implements the symmetric Hann window
      w[n] = 0.5 * (1 - cos(2*pi*n/(L-1))), n = 0..L-1

    Special cases:
    - length <= 0: returns an empty tensor - length == 1: returns a single
      value {1}

    Args:
        length:  Number of samples L in the window [1]

    Template Args:
        t_xtensor_val:  1D xtensor-like container with nested value_type
                        (e.g., xt::xtensor_float_1)

    Returns:
        t_xtensor_val Window weights of shape {L} in range [0, 1]
    """

def create_linear_chirp_signal_f(f0: float, f1: float, pulse_duration: float, sampling_frequency: float = 1500000, start_phase_degrees: float = 90) -> typing.Any:
    """
    Create a sampled linear chirp signal and its time vector.

    Args:
        f0:  Start frequency [Hz]
        f1:  End frequency [Hz]
        pulse_duration:  Pulse duration τ [s]
        sampling_frequency:  Sampling frequency fs [Hz] (default 1.5 MHz)
        start_phase_degrees:  Start phase in degrees (converted internally
                              to radians, default 0)

    Template Args:
        t_xtensor_val:  1D xtensor-like container to hold times and
                        samples (value_type is float/double)

    Returns:
        std::pair_t_xtensor_val_t_xtensor_val First: times t [s], shape
            {nsamples} Second: amplitudes y = sin(phi(t)), shape
            {nsamples}
    """

def generate_transmit_pulse_f(f0: float, f1: float, pulse_duration: float, slope_factor: float, sampling_frequency: float = 1500000, start_phase_degrees: float = 0) -> typing.Any:
    """
    Generate a windowed transmit pulse from a linear chirp.

    This function first creates a linear chirp using
    create_linear_chirp_signal and then applies a Hann window to the start
    and end of the pulse.

    Args:
        f0:  Start frequency [Hz]
        f1:  End frequency [Hz]
        pulse_duration:  Pulse duration τ [s]
        slope_factor:  Proportion of the pulse that is windowed by each
                       half of the window. E.g. slope_factor = 0.5 use the
                       first half to ramp amplitudes up and the second
                       half to ramp them down. slope_factor = 0.1 would
                       use 10% of the pulse duration to ramp up and the
                       last 10% to ramp down.
        sampling_frequency:  Sampling frequency fs [Hz] (default 1.5 Mhz)
        start_phase_degrees:  Start phase in degrees (default 0)

    Template Args:
        t_xtensor_val:  1D xtensor-like container to hold times and
                        samples (value_type is float/double)

    Returns:
        std::pair_t_xtensor_val_t_xtensor_val First: times t [s], shape
            {nsamples} Second: windowed chirp amplitudes y, shape
            {nsamples}



    $See also:

    compute_hann_window_weights


    $See also:

    create_linear_chirp_signal
    """

@overload
def filter_and_decimate_pulse(pulse_amplitudes: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], stage1_decimation_factor: int, stage1_filter_coefficients: Annotated[NDArray[numpy.complex64], dict(shape=(None,), order='A')], stage2_decimation_factor: int, stage2_filter_coefficients: Annotated[NDArray[numpy.complex64], dict(shape=(None,), order='A')], sampling_frequency: float = 1500000) -> typing.Any: ...

@overload
def filter_and_decimate_pulse(pulse_amplitudes: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], stage1_decimation_factor: int, stage1_filter_coefficients: Annotated[NDArray[numpy.complex128], dict(shape=(None,), order='A')], stage2_decimation_factor: int, stage2_filter_coefficients: Annotated[NDArray[numpy.complex128], dict(shape=(None,), order='A')], sampling_frequency: float = 1500000) -> typing.Any: ...

@overload
def compute_effective_pulse_duration_cw(pulse_amplitudes: Annotated[NDArray[numpy.complex64], dict(shape=(None,), order='A')], sample_interval: float, round_to_full_samples: bool = True) -> float: ...

@overload
def compute_effective_pulse_duration_cw(pulse_amplitudes: Annotated[NDArray[numpy.complex64], dict(shape=(None,), order='A')], pulse_times: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> float: ...

@overload
def compute_effective_pulse_duration_cw(pulse_amplitudes: Annotated[NDArray[numpy.complex128], dict(shape=(None,), order='A')], sample_interval: float, round_to_full_samples: bool = True) -> float: ...

@overload
def compute_effective_pulse_duration_cw(pulse_amplitudes: Annotated[NDArray[numpy.complex128], dict(shape=(None,), order='A')], pulse_times: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> float: ...

def hann_d(length: int) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]:
    """
    Generate Hann window weights of a given length.

    Implements the symmetric Hann window
      w[n] = 0.5 * (1 - cos(2*pi*n/(L-1))), n = 0..L-1

    Special cases:
    - length <= 0: returns an empty tensor - length == 1: returns a single
      value {1}

    Args:
        length:  Number of samples L in the window [1]

    Template Args:
        t_xtensor_val:  1D xtensor-like container with nested value_type
                        (e.g., xt::xtensor_float_1)

    Returns:
        t_xtensor_val Window weights of shape {L} in range [0, 1]
    """

def create_linear_chirp_signal_d(f0: float, f1: float, pulse_duration: float, sampling_frequency: float = 1500000, start_phase_degrees: float = 90) -> typing.Any:
    """
    Create a sampled linear chirp signal and its time vector.

    Args:
        f0:  Start frequency [Hz]
        f1:  End frequency [Hz]
        pulse_duration:  Pulse duration τ [s]
        sampling_frequency:  Sampling frequency fs [Hz] (default 1.5 MHz)
        start_phase_degrees:  Start phase in degrees (converted internally
                              to radians, default 0)

    Template Args:
        t_xtensor_val:  1D xtensor-like container to hold times and
                        samples (value_type is float/double)

    Returns:
        std::pair_t_xtensor_val_t_xtensor_val First: times t [s], shape
            {nsamples} Second: amplitudes y = sin(phi(t)), shape
            {nsamples}
    """

def generate_transmit_pulse_d(f0: float, f1: float, pulse_duration: float, slope_factor: float, sampling_frequency: float = 1500000, start_phase_degrees: float = 0) -> typing.Any:
    """
    Generate a windowed transmit pulse from a linear chirp.

    This function first creates a linear chirp using
    create_linear_chirp_signal and then applies a Hann window to the start
    and end of the pulse.

    Args:
        f0:  Start frequency [Hz]
        f1:  End frequency [Hz]
        pulse_duration:  Pulse duration τ [s]
        slope_factor:  Proportion of the pulse that is windowed by each
                       half of the window. E.g. slope_factor = 0.5 use the
                       first half to ramp amplitudes up and the second
                       half to ramp them down. slope_factor = 0.1 would
                       use 10% of the pulse duration to ramp up and the
                       last 10% to ramp down.
        sampling_frequency:  Sampling frequency fs [Hz] (default 1.5 Mhz)
        start_phase_degrees:  Start phase in degrees (default 0)

    Template Args:
        t_xtensor_val:  1D xtensor-like container to hold times and
                        samples (value_type is float/double)

    Returns:
        std::pair_t_xtensor_val_t_xtensor_val First: times t [s], shape
            {nsamples} Second: windowed chirp amplitudes y, shape
            {nsamples}



    $See also:

    compute_hann_window_weights


    $See also:

    create_linear_chirp_signal
    """
