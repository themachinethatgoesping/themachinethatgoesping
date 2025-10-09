"""
Functions used for Simrad RAW water column calibration
"""
from __future__ import annotations
__all__: list[str] = ['compute_effective_pulse_duration_cw', 'create_linear_chirp_signal_d', 'create_linear_chirp_signal_f', 'filter_and_decimate_pulse', 'generate_transmit_pulse_d', 'generate_transmit_pulse_f', 'hann_d', 'hann_f']
compute_effective_pulse_duration_cw: nanobind.nb_func  # value = <nanobind.nb_func object>
create_linear_chirp_signal_d: nanobind.nb_func  # value = <nanobind.nb_func object>
create_linear_chirp_signal_f: nanobind.nb_func  # value = <nanobind.nb_func object>
filter_and_decimate_pulse: nanobind.nb_func  # value = <nanobind.nb_func object>
generate_transmit_pulse_d: nanobind.nb_func  # value = <nanobind.nb_func object>
generate_transmit_pulse_f: nanobind.nb_func  # value = <nanobind.nb_func object>
hann_d: nanobind.nb_func  # value = <nanobind.nb_func object>
hann_f: nanobind.nb_func  # value = <nanobind.nb_func object>
