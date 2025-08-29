"""
Functions used for Simrad RAW water column calibration
"""
from __future__ import annotations
import numpy
import typing
__all__: list[str] = ['compute_effective_pulse_duration_cw', 'create_linear_chirp_signal_d', 'create_linear_chirp_signal_f', 'filter_and_decimate_pulse', 'generate_transmit_pulse_d', 'generate_transmit_pulse_f', 'hann_d', 'hann_f']
@typing.overload
def compute_effective_pulse_duration_cw(pulse_amplitudes: numpy.ndarray[numpy.complex64], sample_interval: float, round_to_full_samples: bool = True) -> float:
    ...
@typing.overload
def compute_effective_pulse_duration_cw(pulse_amplitudes: numpy.ndarray[numpy.complex64], pulse_times: numpy.ndarray[numpy.float32]) -> float:
    ...
@typing.overload
def compute_effective_pulse_duration_cw(pulse_amplitudes: numpy.ndarray[numpy.complex128], sample_interval: float, round_to_full_samples: bool = True) -> float:
    ...
@typing.overload
def compute_effective_pulse_duration_cw(pulse_amplitudes: numpy.ndarray[numpy.complex128], pulse_times: numpy.ndarray[numpy.float64]) -> float:
    ...
def create_linear_chirp_signal_d(f0: float, f1: float, pulse_duration: float, sampling_frequency: float = 1500000, start_phase_degrees: float = 90) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
    """
    Create a sampled linear chirp signal and its time vector.
    
    Template parameter ``t_xtensor_val``:
        1D xtensor-like container to hold times and samples (value_type is
        float/double)
    
    Parameter ``f0``:
        Start frequency [Hz]
    
    Parameter ``f1``:
        End frequency [Hz]
    
    Parameter ``pulse_duration``:
        Pulse duration τ [s]
    
    Parameter ``sampling_frequency``:
        Sampling frequency fs [Hz] (default 1.5 MHz)
    
    Parameter ``start_phase_degrees``:
        Start phase in degrees (converted internally to radians, default
        0)
    
    Returns:
        std::pair<t_xtensor_val, t_xtensor_val> First: times t [s], shape
        {nsamples} Second: amplitudes y = sin(phi(t)), shape {nsamples}
    """
def create_linear_chirp_signal_f(f0: float, f1: float, pulse_duration: float, sampling_frequency: float = 1500000, start_phase_degrees: float = 90) -> tuple[numpy.ndarray[numpy.float32], numpy.ndarray[numpy.float32]]:
    """
    Create a sampled linear chirp signal and its time vector.
    
    Template parameter ``t_xtensor_val``:
        1D xtensor-like container to hold times and samples (value_type is
        float/double)
    
    Parameter ``f0``:
        Start frequency [Hz]
    
    Parameter ``f1``:
        End frequency [Hz]
    
    Parameter ``pulse_duration``:
        Pulse duration τ [s]
    
    Parameter ``sampling_frequency``:
        Sampling frequency fs [Hz] (default 1.5 MHz)
    
    Parameter ``start_phase_degrees``:
        Start phase in degrees (converted internally to radians, default
        0)
    
    Returns:
        std::pair<t_xtensor_val, t_xtensor_val> First: times t [s], shape
        {nsamples} Second: amplitudes y = sin(phi(t)), shape {nsamples}
    """
@typing.overload
def filter_and_decimate_pulse(pulse_amplitudes: numpy.ndarray[numpy.float32], stage1_decimation_factor: int, stage1_filter_coefficients: numpy.ndarray[numpy.complex64], stage2_decimation_factor: int, stage2_filter_coefficients: numpy.ndarray[numpy.complex64], sampling_frequency: float = 1500000) -> tuple[numpy.ndarray[numpy.float32], numpy.ndarray[numpy.complex64]]:
    ...
@typing.overload
def filter_and_decimate_pulse(pulse_amplitudes: numpy.ndarray[numpy.float64], stage1_decimation_factor: int, stage1_filter_coefficients: numpy.ndarray[numpy.complex128], stage2_decimation_factor: int, stage2_filter_coefficients: numpy.ndarray[numpy.complex128], sampling_frequency: float = 1500000) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.complex128]]:
    ...
def generate_transmit_pulse_d(f0: float, f1: float, pulse_duration: float, slope_factor: float, sampling_frequency: float = 1500000, start_phase_degrees: float = 0) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
    """
    Generate a windowed transmit pulse from a linear chirp.
    
    This function first creates a linear chirp using
    create_linear_chirp_signal and then applies a Hann window to the start
    and end of the pulse.
    
    Template parameter ``t_xtensor_val``:
        1D xtensor-like container to hold times and samples (value_type is
        float/double)
    
    Parameter ``f0``:
        Start frequency [Hz]
    
    Parameter ``f1``:
        End frequency [Hz]
    
    Parameter ``pulse_duration``:
        Pulse duration τ [s]
    
    Parameter ``slope_factor``:
        Proportion of the pulse that is windowed by each half of the
        window. E.g. slope_factor = 0.5 use the first half to ramp
        amplitudes up and the second half to ramp them down. slope_factor
        = 0.1 would use 10% of the pulse duration to ramp up and the last
        10% to ramp down.
    
    Parameter ``sampling_frequency``:
        Sampling frequency fs [Hz] (default 1.5 Mhz)
    
    Parameter ``start_phase_degrees``:
        Start phase in degrees (default 0)
    
    Returns:
        std::pair<t_xtensor_val, t_xtensor_val> First: times t [s], shape
        {nsamples} Second: windowed chirp amplitudes y, shape {nsamples}
    
    See also:
        compute_hann_window_weights
    
    See also:
        create_linear_chirp_signal
    """
def generate_transmit_pulse_f(f0: float, f1: float, pulse_duration: float, slope_factor: float, sampling_frequency: float = 1500000, start_phase_degrees: float = 0) -> tuple[numpy.ndarray[numpy.float32], numpy.ndarray[numpy.float32]]:
    """
    Generate a windowed transmit pulse from a linear chirp.
    
    This function first creates a linear chirp using
    create_linear_chirp_signal and then applies a Hann window to the start
    and end of the pulse.
    
    Template parameter ``t_xtensor_val``:
        1D xtensor-like container to hold times and samples (value_type is
        float/double)
    
    Parameter ``f0``:
        Start frequency [Hz]
    
    Parameter ``f1``:
        End frequency [Hz]
    
    Parameter ``pulse_duration``:
        Pulse duration τ [s]
    
    Parameter ``slope_factor``:
        Proportion of the pulse that is windowed by each half of the
        window. E.g. slope_factor = 0.5 use the first half to ramp
        amplitudes up and the second half to ramp them down. slope_factor
        = 0.1 would use 10% of the pulse duration to ramp up and the last
        10% to ramp down.
    
    Parameter ``sampling_frequency``:
        Sampling frequency fs [Hz] (default 1.5 Mhz)
    
    Parameter ``start_phase_degrees``:
        Start phase in degrees (default 0)
    
    Returns:
        std::pair<t_xtensor_val, t_xtensor_val> First: times t [s], shape
        {nsamples} Second: windowed chirp amplitudes y, shape {nsamples}
    
    See also:
        compute_hann_window_weights
    
    See also:
        create_linear_chirp_signal
    """
def hann_d(length: int) -> numpy.ndarray[numpy.float64]:
    """
    Generate Hann window weights of a given length.
    
    Implements the symmetric Hann window w[n] = 0.5 * (1 -
    cos(2*pi*n/(L-1))), n = 0..L-1
    
    Special cases: - length <= 0: returns an empty tensor - length == 1:
    returns a single value {1}
    
    Template parameter ``t_xtensor_val``:
        1D xtensor-like container with nested value_type (e.g.,
        xt::xtensor<float,1>)
    
    Parameter ``length``:
        Number of samples L in the window [1]
    
    Returns:
        t_xtensor_val Window weights of shape {L} in range [0, 1]
    """
def hann_f(length: int) -> numpy.ndarray[numpy.float32]:
    """
    Generate Hann window weights of a given length.
    
    Implements the symmetric Hann window w[n] = 0.5 * (1 -
    cos(2*pi*n/(L-1))), n = 0..L-1
    
    Special cases: - length <= 0: returns an empty tensor - length == 1:
    returns a single value {1}
    
    Template parameter ``t_xtensor_val``:
        1D xtensor-like container with nested value_type (e.g.,
        xt::xtensor<float,1>)
    
    Parameter ``length``:
        Number of samples L in the window [1]
    
    Returns:
        t_xtensor_val Window weights of shape {L} in range [0, 1]
    """
