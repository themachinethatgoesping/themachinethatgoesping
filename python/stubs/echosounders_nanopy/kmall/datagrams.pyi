from collections.abc import Iterable, Iterator, Sequence
import enum
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

import themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures
import themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures
import themachinethatgoesping.echosounders_nanopy.kmall
import themachinethatgoesping.navigation_nanopy.datastructures


class MRZPingInfo:
    def __init__(self) -> None: ...

    def get_bytes_content(self) -> int: ...

    def get_padding_0(self) -> int: ...

    def get_ping_rate_hz(self) -> float: ...

    def get_beam_spacing(self) -> int: ...

    def get_depth_mode(self) -> int: ...

    def get_sub_depth_mode(self) -> int: ...

    def get_distance_btw_swath(self) -> int: ...

    def get_detection_mode(self) -> int: ...

    def get_pulse_form(self) -> int: ...

    def get_fixed_gain_control(self) -> int: ...

    def get_padding_1(self) -> int: ...

    def get_frequency_mode_hz(self) -> float: ...

    def get_frequency_range_low_Limit_hz(self) -> float: ...

    def get_frequency_range_high_Limit_hz(self) -> float: ...

    def get_max_total_tx_pulse_length_sec(self) -> float: ...

    def get_max_eff_tx_pulse_length_sec(self) -> float: ...

    def get_max_eff_tx_band_width_hz(self) -> float: ...

    def get_abs_coeff_db_per_km(self) -> float: ...

    def get_port_sector_edge_deg(self) -> float: ...

    def get_starboard_sector_edge_deg(self) -> float: ...

    def get_port_mean_coverage_deg(self) -> float: ...

    def get_starboard_mean_coverage_deg(self) -> float: ...

    def get_port_mean_coverage_m(self) -> int: ...

    def get_starboard_mean_coverage_m(self) -> int: ...

    def get_mode_and_stabilisation(self) -> int: ...

    def get_runtime_filter_1(self) -> int: ...

    def get_runtime_filter_2(self) -> int: ...

    def get_pipe_tracking_status(self) -> int: ...

    def get_tx_array_size_used_deg(self) -> float: ...

    def get_rx_array_size_used_deg(self) -> float: ...

    def get_tx_power_db(self) -> float: ...

    def get_sl_ramp_up_time_remaining(self) -> int: ...

    def get_padding_2(self) -> int: ...

    def get_yaw_angle_deg(self) -> float: ...

    def get_number_of_tx_sectors(self) -> int: ...

    def get_number_of_bytes_per_tx_Sector(self) -> int: ...

    def get_heading_vessel_deg(self) -> float: ...

    def get_sound_speed_at_tx_depth_m_per_sec(self) -> float: ...

    def get_tx_transducer_depth_m(self) -> float: ...

    def get_z_water_level_re_ref_point_m(self) -> float: ...

    def get_x_kmall_to_all_m(self) -> float: ...

    def get_y_kmall_to_all_m(self) -> float: ...

    def get_lat_long_info(self) -> int: ...

    def get_position_sensor_status(self) -> int: ...

    def get_attitude_sensor_status(self) -> int: ...

    def get_padding_3(self) -> int: ...

    def get_latitude_deg(self) -> float: ...

    def get_longitude_deg(self) -> float: ...

    def get_ellipsoid_height_re_ref_point_m(self) -> float: ...

    def get_bs_correction_offset_db(self) -> float: ...

    def get_lamberts_law_applied(self) -> int: ...

    def get_ice_window(self) -> int: ...

    def get_active_modes(self) -> int: ...

    def set_bytes_content(self, val: int) -> None: ...

    def set_padding_0(self, val: int) -> None: ...

    def set_ping_rate_hz(self, val: float) -> None: ...

    def set_beam_spacing(self, val: int) -> None: ...

    def set_depth_mode(self, val: int) -> None: ...

    def set_sub_depth_mode(self, val: int) -> None: ...

    def set_distance_btw_swath(self, val: int) -> None: ...

    def set_detection_mode(self, val: int) -> None: ...

    def set_pulse_form(self, val: int) -> None: ...

    def set_fixed_gain_control(self, val: int) -> None: ...

    def set_padding_1(self, val: int) -> None: ...

    def set_frequency_mode_hz(self, val: float) -> None: ...

    def set_frequency_range_low_Limit_hz(self, val: float) -> None: ...

    def set_frequency_range_high_Limit_hz(self, val: float) -> None: ...

    def set_max_total_tx_pulse_length_sec(self, val: float) -> None: ...

    def set_max_eff_tx_pulse_length_sec(self, val: float) -> None: ...

    def set_max_eff_tx_band_width_hz(self, val: float) -> None: ...

    def set_abs_coeff_db_per_km(self, val: float) -> None: ...

    def set_port_sector_edge_deg(self, val: float) -> None: ...

    def set_starboard_sector_edge_deg(self, val: float) -> None: ...

    def set_port_mean_coverage_deg(self, val: float) -> None: ...

    def set_starboard_mean_coverage_deg(self, val: float) -> None: ...

    def set_port_mean_coverage_m(self, val: int) -> None: ...

    def set_starboard_mean_coverage_m(self, val: int) -> None: ...

    def set_mode_and_stabilisation(self, val: int) -> None: ...

    def set_runtime_filter_1(self, val: int) -> None: ...

    def set_runtime_filter_2(self, val: int) -> None: ...

    def set_pipe_tracking_status(self, val: int) -> None: ...

    def set_tx_array_size_used_deg(self, val: float) -> None: ...

    def set_rx_array_size_used_deg(self, val: float) -> None: ...

    def set_tx_power_db(self, val: float) -> None: ...

    def set_sl_ramp_up_time_remaining(self, val: int) -> None: ...

    def set_padding_2(self, val: int) -> None: ...

    def set_yaw_angle_deg(self, val: float) -> None: ...

    def set_number_of_tx_sectors(self, val: int) -> None: ...

    def set_number_of_bytes_per_tx_Sector(self, val: int) -> None: ...

    def set_heading_vessel_deg(self, val: float) -> None: ...

    def set_sound_speed_at_tx_depth_m_per_sec(self, val: float) -> None: ...

    def set_tx_transducer_depth_m(self, val: float) -> None: ...

    def set_z_water_level_re_ref_point_m(self, val: float) -> None: ...

    def set_x_kmall_to_all_m(self, val: float) -> None: ...

    def set_y_kmall_to_all_m(self, val: float) -> None: ...

    def set_lat_long_info(self, val: int) -> None: ...

    def set_position_sensor_status(self, val: int) -> None: ...

    def set_attitude_sensor_status(self, val: int) -> None: ...

    def set_padding_3(self, val: int) -> None: ...

    def set_latitude_deg(self, val: float) -> None: ...

    def set_longitude_deg(self, val: float) -> None: ...

    def set_ellipsoid_height_re_ref_point_m(self, val: float) -> None: ...

    def set_bs_correction_offset_db(self, val: float) -> None: ...

    def set_lamberts_law_applied(self, val: int) -> None: ...

    def set_ice_window(self, val: int) -> None: ...

    def set_active_modes(self, val: int) -> None: ...

    def __eq__(self, other: MRZPingInfo) -> bool: ...

    def copy(self) -> MRZPingInfo:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MRZPingInfo: ...

    def __deepcopy__(self, arg: dict, /) -> MRZPingInfo: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class MRZRxInfo:
    def __init__(self) -> None: ...

    def get_bytes_content(self) -> int: ...

    def set_bytes_content(self, val: int) -> None: ...

    def get_number_of_soundings_max_main(self) -> int: ...

    def set_number_of_soundings_max_main(self, val: int) -> None: ...

    def get_number_of_soundings_valid_main(self) -> int: ...

    def set_number_of_soundings_valid_main(self, val: int) -> None: ...

    def get_number_of_bytes_per_sounding(self) -> int: ...

    def set_number_of_bytes_per_sounding(self, val: int) -> None: ...

    def get_wc_sample_rate(self) -> float: ...

    def set_wc_sample_rate(self, val: float) -> None: ...

    def get_seabed_image_sample_rate(self) -> float: ...

    def set_seabed_image_sample_rate(self, val: float) -> None: ...

    def get_bs_normal_db(self) -> float: ...

    def set_bs_normal_db(self, val: float) -> None: ...

    def get_bs_oblique_db(self) -> float: ...

    def set_bs_oblique_db(self, val: float) -> None: ...

    def get_extra_detection_alarm_flag(self) -> int: ...

    def set_extra_detection_alarm_flag(self, val: int) -> None: ...

    def get_number_of_extra_detections(self) -> int: ...

    def set_number_of_extra_detections(self, val: int) -> None: ...

    def get_number_of_extra_detection_classes(self) -> int: ...

    def set_number_of_extra_detection_classes(self, val: int) -> None: ...

    def get_number_of_bytes_per_class(self) -> int: ...

    def set_number_of_bytes_per_class(self, val: int) -> None: ...

    def __eq__(self, other: MRZRxInfo) -> bool: ...

    def copy(self) -> MRZRxInfo:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MRZRxInfo: ...

    def __deepcopy__(self, arg: dict, /) -> MRZRxInfo: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class MRZSectorInfo:
    def __init__(self) -> None: ...

    def get_tx_sector_number(self) -> int: ...

    def set_tx_sector_number(self, val: int) -> None: ...

    def get_tx_arrary_number(self) -> int: ...

    def set_tx_arrary_number(self, val: int) -> None: ...

    def get_tx_sub_array(self) -> int: ...

    def set_tx_sub_array(self, val: int) -> None: ...

    def get_padding_0(self) -> int: ...

    def set_padding_0(self, val: int) -> None: ...

    def get_sector_transmit_delay_sec(self) -> float: ...

    def set_sector_transmit_delay_sec(self, val: float) -> None: ...

    def get_tilt_angle_re_tx_deg(self) -> float: ...

    def set_tilt_angle_re_tx_deg(self, val: float) -> None: ...

    def get_tx_nominal_source_level_db(self) -> float: ...

    def set_tx_nominal_source_level_db(self, val: float) -> None: ...

    def get_tx_focus_range_m(self) -> float: ...

    def set_tx_focus_range_m(self, val: float) -> None: ...

    def get_centre_frequency_hz(self) -> float: ...

    def set_centre_frequency_hz(self, val: float) -> None: ...

    def get_signal_band_width_hz(self) -> float: ...

    def set_signal_band_width_hz(self, val: float) -> None: ...

    def get_total_signal_length_sec(self) -> float: ...

    def set_total_signal_length_sec(self, val: float) -> None: ...

    def get_pulse_shading(self) -> int: ...

    def set_pulse_shading(self, val: int) -> None: ...

    def get_signal_wave_form(self) -> int: ...

    def set_signal_wave_form(self, val: int) -> None: ...

    def get_padding_1(self) -> int: ...

    def set_padding_1(self, val: int) -> None: ...

    def get_high_voltage_level_db(self) -> float: ...

    def set_high_voltage_level_db(self, val: float) -> None: ...

    def get_sector_tracking_corr_db(self) -> float: ...

    def set_sector_tracking_corr_db(self, val: float) -> None: ...

    def get_effective_signal_length_sec(self) -> float: ...

    def set_effective_signal_length_sec(self, val: float) -> None: ...

    def get_tx_signal_type(self) -> themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.o_TxSignalType: ...

    def __eq__(self, other: MRZSectorInfo) -> bool: ...

    def copy(self) -> MRZSectorInfo:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MRZSectorInfo: ...

    def __deepcopy__(self, arg: dict, /) -> MRZSectorInfo: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class MRZSectorInfoVector:
    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, arg: MRZSectorInfoVector) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, arg: Iterable[MRZSectorInfo], /) -> None:
        """Construct from an iterable object"""

    def __len__(self) -> int: ...

    def __bool__(self) -> bool:
        """Check whether the vector is nonempty"""

    def __repr__(self) -> str: ...

    def __iter__(self) -> Iterator[MRZSectorInfo]: ...

    @overload
    def __getitem__(self, arg: int, /) -> MRZSectorInfo: ...

    @overload
    def __getitem__(self, arg: slice, /) -> MRZSectorInfoVector: ...

    def clear(self) -> None:
        """Remove all items from list."""

    def append(self, arg: MRZSectorInfo, /) -> None:
        """Append `arg` to the end of the list."""

    def insert(self, arg0: int, arg1: MRZSectorInfo, /) -> None:
        """Insert object `arg1` before index `arg0`."""

    def pop(self, index: int = -1) -> MRZSectorInfo:
        """Remove and return item at `index` (default last)."""

    def extend(self, arg: MRZSectorInfoVector, /) -> None:
        """Extend `self` by appending elements from `arg`."""

    @overload
    def __setitem__(self, arg0: int, arg1: MRZSectorInfo, /) -> None: ...

    @overload
    def __setitem__(self, arg0: slice, arg1: MRZSectorInfoVector, /) -> None: ...

    @overload
    def __delitem__(self, arg: int, /) -> None: ...

    @overload
    def __delitem__(self, arg: slice, /) -> None: ...

    def __eq__(self, arg: object, /) -> bool: ...

    def __ne__(self, arg: object, /) -> bool: ...

    @overload
    def __contains__(self, arg: MRZSectorInfo, /) -> bool: ...

    @overload
    def __contains__(self, arg: object, /) -> bool: ...

    def count(self, arg: MRZSectorInfo, /) -> int:
        """Return number of occurrences of `arg`."""

    def remove(self, arg: MRZSectorInfo, /) -> None:
        """Remove first occurrence of `arg`."""

class MRZExtraDetClassInfo:
    def __init__(self) -> None: ...

    def get_num_extra_det_in_class(self) -> int: ...

    def set_num_extra_det_in_class(self, val: int) -> None: ...

    def get_padding(self) -> int: ...

    def set_padding(self, val: int) -> None: ...

    def get_alarm_flag(self) -> int: ...

    def set_alarm_flag(self, val: int) -> None: ...

    def __eq__(self, other: MRZExtraDetClassInfo) -> bool: ...

    def copy(self) -> MRZExtraDetClassInfo:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MRZExtraDetClassInfo: ...

    def __deepcopy__(self, arg: dict, /) -> MRZExtraDetClassInfo: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class MRZExtraDetClassInfoVector:
    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, arg: MRZExtraDetClassInfoVector) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, arg: Iterable[MRZExtraDetClassInfo], /) -> None:
        """Construct from an iterable object"""

    def __len__(self) -> int: ...

    def __bool__(self) -> bool:
        """Check whether the vector is nonempty"""

    def __repr__(self) -> str: ...

    def __iter__(self) -> Iterator[MRZExtraDetClassInfo]: ...

    @overload
    def __getitem__(self, arg: int, /) -> MRZExtraDetClassInfo: ...

    @overload
    def __getitem__(self, arg: slice, /) -> MRZExtraDetClassInfoVector: ...

    def clear(self) -> None:
        """Remove all items from list."""

    def append(self, arg: MRZExtraDetClassInfo, /) -> None:
        """Append `arg` to the end of the list."""

    def insert(self, arg0: int, arg1: MRZExtraDetClassInfo, /) -> None:
        """Insert object `arg1` before index `arg0`."""

    def pop(self, index: int = -1) -> MRZExtraDetClassInfo:
        """Remove and return item at `index` (default last)."""

    def extend(self, arg: MRZExtraDetClassInfoVector, /) -> None:
        """Extend `self` by appending elements from `arg`."""

    @overload
    def __setitem__(self, arg0: int, arg1: MRZExtraDetClassInfo, /) -> None: ...

    @overload
    def __setitem__(self, arg0: slice, arg1: MRZExtraDetClassInfoVector, /) -> None: ...

    @overload
    def __delitem__(self, arg: int, /) -> None: ...

    @overload
    def __delitem__(self, arg: slice, /) -> None: ...

    def __eq__(self, arg: object, /) -> bool: ...

    def __ne__(self, arg: object, /) -> bool: ...

    @overload
    def __contains__(self, arg: MRZExtraDetClassInfo, /) -> bool: ...

    @overload
    def __contains__(self, arg: object, /) -> bool: ...

    def count(self, arg: MRZExtraDetClassInfo, /) -> int:
        """Return number of occurrences of `arg`."""

    def remove(self, arg: MRZExtraDetClassInfo, /) -> None:
        """Remove first occurrence of `arg`."""

class MRZSoundings:
    def __init__(self) -> None: ...

    def get_sounding_index(self) -> int: ...

    def set_sounding_index(self, val: int) -> None: ...

    def get_tx_sector_number(self) -> int: ...

    def set_tx_sector_number(self, val: int) -> None: ...

    def get_detection_type(self) -> int: ...

    def set_detection_type(self, val: int) -> None: ...

    def get_detection_method(self) -> int: ...

    def set_detection_method(self, val: int) -> None: ...

    def get_rejection_info_1(self) -> int: ...

    def set_rejection_info_1(self, val: int) -> None: ...

    def get_rejection_info_2(self) -> int: ...

    def set_rejection_info_2(self, val: int) -> None: ...

    def get_post_processing_info(self) -> int: ...

    def set_post_processing_info(self, val: int) -> None: ...

    def get_detection_class(self) -> int: ...

    def set_detection_class(self, val: int) -> None: ...

    def get_detection_confidence_level(self) -> int: ...

    def set_detection_confidence_level(self, val: int) -> None: ...

    def get_padding(self) -> int: ...

    def set_padding(self, val: int) -> None: ...

    def get_range_factor(self) -> float: ...

    def set_range_factor(self, val: float) -> None: ...

    def get_quality_factor(self) -> float: ...

    def set_quality_factor(self, val: float) -> None: ...

    def get_detection_uncertainty_ver_m(self) -> float: ...

    def set_detection_uncertainty_ver_m(self, val: float) -> None: ...

    def get_detection_uncertainty_hor_m(self) -> float: ...

    def set_detection_uncertainty_hor_m(self, val: float) -> None: ...

    def get_detection_window_length_sec(self) -> float: ...

    def set_detection_window_length_sec(self, val: float) -> None: ...

    def get_echo_length_sec(self) -> float: ...

    def set_echo_length_sec(self, val: float) -> None: ...

    def get_wc_beam_number(self) -> int: ...

    def set_wc_beam_number(self, val: int) -> None: ...

    def get_wc_range_samples(self) -> int: ...

    def set_wc_range_samples(self, val: int) -> None: ...

    def get_wc_nom_beam_angle_across_deg(self) -> float: ...

    def set_wc_nom_beam_angle_across_deg(self, val: float) -> None: ...

    def get_mean_abs_coeff_db_per_km(self) -> float: ...

    def set_mean_abs_coeff_db_per_km(self, val: float) -> None: ...

    def get_reflectivity_1_db(self) -> float: ...

    def set_reflectivity_1_db(self, val: float) -> None: ...

    def get_reflectivity_2_db(self) -> float: ...

    def set_reflectivity_2_db(self, val: float) -> None: ...

    def get_receiver_sensitivity_applied_db(self) -> float: ...

    def set_receiver_sensitivity_applied_db(self, val: float) -> None: ...

    def get_source_level_applied_db(self) -> float: ...

    def set_source_level_applied_db(self, val: float) -> None: ...

    def get_bs_calibration_db(self) -> float: ...

    def set_bs_calibration_db(self, val: float) -> None: ...

    def get_tvg_db(self) -> float: ...

    def set_tvg_db(self, val: float) -> None: ...

    def get_beam_angle_re_rx_deg(self) -> float: ...

    def set_beam_angle_re_rx_deg(self, val: float) -> None: ...

    def get_beam_angle_correction_deg(self) -> float: ...

    def set_beam_angle_correction_deg(self, val: float) -> None: ...

    def get_two_way_travel_time_sec(self) -> float: ...

    def set_two_way_travel_time_sec(self, val: float) -> None: ...

    def get_two_way_travel_time_correction_sec(self) -> float: ...

    def set_two_way_travel_time_correction_sec(self, val: float) -> None: ...

    def get_delta_latitude_deg(self) -> float: ...

    def set_delta_latitude_deg(self, val: float) -> None: ...

    def get_delta_longitude_deg(self) -> float: ...

    def set_delta_longitude_deg(self, val: float) -> None: ...

    def get_z_re_ref_point_m(self) -> float: ...

    def set_z_re_ref_point_m(self, val: float) -> None: ...

    def get_y_re_ref_point_m(self) -> float: ...

    def set_y_re_ref_point_m(self, val: float) -> None: ...

    def get_x_re_ref_point_m(self) -> float: ...

    def set_x_re_ref_point_m(self, val: float) -> None: ...

    def get_beam_inc_angle_adj_deg(self) -> float: ...

    def set_beam_inc_angle_adj_deg(self, val: float) -> None: ...

    def get_real_time_clean_info(self) -> int: ...

    def set_real_time_clean_info(self, val: int) -> None: ...

    def get_si_start_range_samples(self) -> int: ...

    def set_si_start_range_samples(self, val: int) -> None: ...

    def get_si_centre_sample(self) -> int: ...

    def set_si_centre_sample(self, val: int) -> None: ...

    def get_si_num_samples(self) -> int: ...

    def set_si_num_samples(self, val: int) -> None: ...

    def __eq__(self, other: MRZSoundings) -> bool: ...

    def copy(self) -> MRZSoundings:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MRZSoundings: ...

    def __deepcopy__(self, arg: dict, /) -> MRZSoundings: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class MRZSoundingsVector:
    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, arg: MRZSoundingsVector) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, arg: Iterable[MRZSoundings], /) -> None:
        """Construct from an iterable object"""

    def __len__(self) -> int: ...

    def __bool__(self) -> bool:
        """Check whether the vector is nonempty"""

    def __repr__(self) -> str: ...

    def __iter__(self) -> Iterator[MRZSoundings]: ...

    @overload
    def __getitem__(self, arg: int, /) -> MRZSoundings: ...

    @overload
    def __getitem__(self, arg: slice, /) -> MRZSoundingsVector: ...

    def clear(self) -> None:
        """Remove all items from list."""

    def append(self, arg: MRZSoundings, /) -> None:
        """Append `arg` to the end of the list."""

    def insert(self, arg0: int, arg1: MRZSoundings, /) -> None:
        """Insert object `arg1` before index `arg0`."""

    def pop(self, index: int = -1) -> MRZSoundings:
        """Remove and return item at `index` (default last)."""

    def extend(self, arg: MRZSoundingsVector, /) -> None:
        """Extend `self` by appending elements from `arg`."""

    @overload
    def __setitem__(self, arg0: int, arg1: MRZSoundings, /) -> None: ...

    @overload
    def __setitem__(self, arg0: slice, arg1: MRZSoundingsVector, /) -> None: ...

    @overload
    def __delitem__(self, arg: int, /) -> None: ...

    @overload
    def __delitem__(self, arg: slice, /) -> None: ...

    def __eq__(self, arg: object, /) -> bool: ...

    def __ne__(self, arg: object, /) -> bool: ...

    @overload
    def __contains__(self, arg: MRZSoundings, /) -> bool: ...

    @overload
    def __contains__(self, arg: object, /) -> bool: ...

    def count(self, arg: MRZSoundings, /) -> int:
        """Return number of occurrences of `arg`."""

    def remove(self, arg: MRZSoundings, /) -> None:
        """Remove first occurrence of `arg`."""

class MRZSoundingsContainer:
    def __init__(self) -> None: ...

    @property
    def soundings(self) -> list[MRZSoundings]: ...

    @soundings.setter
    def soundings(self, arg: Sequence[MRZSoundings], /) -> None: ...

    def get_sounding_index_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_tx_sector_number_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint8], dict(shape=(None,), order='C')]: ...

    def get_detection_type_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint8], dict(shape=(None,), order='C')]: ...

    def get_detection_method_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint8], dict(shape=(None,), order='C')]: ...

    def get_rejection_info_1_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint8], dict(shape=(None,), order='C')]: ...

    def get_rejection_info_2_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint8], dict(shape=(None,), order='C')]: ...

    def get_post_processing_info_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint8], dict(shape=(None,), order='C')]: ...

    def get_detection_class_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint8], dict(shape=(None,), order='C')]: ...

    def get_detection_confidence_level_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint8], dict(shape=(None,), order='C')]: ...

    def get_padding_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_range_factor_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_quality_factor_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_detection_uncertainty_ver_m_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_detection_uncertainty_hor_m_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_detection_window_length_sec_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_echo_length_sec_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_wc_beam_number_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_wc_range_samples_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_wc_nom_beam_angle_across_deg_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_mean_abs_coeff_db_per_km_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_reflectivity_1_db_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_reflectivity_2_db_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_receiver_sensitivity_applied_db_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_source_level_applied_db_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_bs_calibration_db_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_tvg_db_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_beam_angle_re_rx_deg_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_beam_angle_correction_deg_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_two_way_travel_time_sec_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_two_way_travel_time_correction_sec_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_delta_latitude_deg_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_delta_longitude_deg_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_z_re_ref_point_m_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_y_re_ref_point_m_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_x_re_ref_point_m_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_beam_inc_angle_adj_deg_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_real_time_clean_info_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_si_start_range_samples_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_si_centre_sample_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_si_num_samples_tensor(self, beam_numbers: Sequence[int] = []) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_number_of_soundings(self) -> int: ...

    def get_number_of_seabed_image_samples(self) -> int: ...

    def get_seabed_image_sounding_index_tensor(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_mean_absorption_db_per_m_per_sector(self, number_of_tx_sectors: int) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        Compute the mean absorption coefficient per transmit sector.

        This function computes the mean of the absorption coefficients (dB/m)
        for all soundings belonging to each transmit sector.

        Args:
            number_of_tx_sectors: The number of transmit sectors in the ping

        Returns:
            xt::xtensor_float_1 Mean absorption coefficient in dB/m for each
               sector
        """

    @overload
    def get_xyz(self) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1: ...

    @overload
    def get_xyz(self, beam_numbers: Sequence[int]) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1: ...

    def __eq__(self, other: MRZSoundingsContainer) -> bool: ...

    def copy(self) -> MRZSoundingsContainer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MRZSoundingsContainer: ...

    def __deepcopy__(self, arg: dict, /) -> MRZSoundingsContainer: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class MWCRxBeamData:
    def __init__(self) -> None: ...

    def get_beam_pointing_angle_re_vertical_deg(self) -> float: ...

    def set_beam_pointing_angle_re_vertical_deg(self, val: int) -> None: ...

    def get_start_range_sample_number(self) -> int: ...

    def set_start_range_sample_number(self, val: int) -> None: ...

    def get_detected_range_in_samples(self) -> int: ...

    def set_detected_range_in_samples(self, val: int) -> None: ...

    def get_transmit_sector_number(self) -> int: ...

    def set_transmit_sector_number(self, val: int) -> None: ...

    def get_number_of_samples(self) -> int: ...

    def set_number_of_samples(self, val: int) -> None: ...

    def get_detected_range_in_samples_high_resolution(self) -> float: ...

    def set_detected_range_in_samples_high_resolution(self, val: float) -> None: ...

    def get_sample_amplitudes_in_db(self, db_offset: float = 0.0) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def set_sample_amplitudes_05dB(self, sample_amplitudes: Annotated[NDArray[numpy.int8], dict(shape=(None,), order='C')]) -> None: ...

    def get_sample_amplitudes_05dB(self) -> object: ...

    def set_rx_beam_phase(self, rx_beam_phase: Annotated[NDArray[numpy.int8], dict(shape=(None,), order='C')]) -> None: ...

    def get_rx_beam_phase(self) -> object: ...

    def get_samples_are_skipped(self) -> bool: ...

    def set_sample_are_skipped(self, sample_pos: int) -> None: ...

    def get_sample_position(self) -> int: ...

    def sample_amplitudes_05dB(self) -> Annotated[NDArray[numpy.int8], dict(shape=(None,), order='C')]: ...

    def __eq__(self, other: MWCRxBeamData) -> bool: ...

    def copy(self) -> MWCRxBeamData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MWCRxBeamData: ...

    def __deepcopy__(self, arg: dict, /) -> MWCRxBeamData: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class MWCRxBeamDataContainer:
    def __init__(self) -> None: ...

    @property
    def beams(self) -> list[MWCRxBeamData]: ...

    @beams.setter
    def beams(self, arg: Sequence[MWCRxBeamData], /) -> None: ...

    def get_beams(self) -> list[MWCRxBeamData]: ...

    def set_beams(self, beams: Sequence[MWCRxBeamData]) -> None: ...

    def get_beam_pointing_angle_re_vertical_deg_tensor(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_start_range_sample_number_tensor(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_detected_range_in_samples_tensor(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_transmit_sector_number_tensor(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_number_of_samples_tensor(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None,), order='C')]: ...

    def get_detected_range_in_samples_high_resolution_tensor(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_number_of_beams(self) -> int: ...

    def get_total_number_of_samples(self) -> int: ...

    def __eq__(self, other: MWCRxBeamDataContainer) -> bool: ...

    def copy(self) -> MWCRxBeamDataContainer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MWCRxBeamDataContainer: ...

    def __deepcopy__(self, arg: dict, /) -> MWCRxBeamDataContainer: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class MWCTxInfo:
    def __init__(self) -> None: ...

    def get_bytes_content(self) -> int: ...

    def set_bytes_content(self, val: int) -> None: ...

    def get_number_of_tx_sectors(self) -> int: ...

    def set_number_of_tx_sectors(self, val: int) -> None: ...

    def get_num_bytes_per_tx_sector(self) -> int: ...

    def set_num_bytes_per_tx_sector(self, val: int) -> None: ...

    def get_padding(self) -> int: ...

    def set_padding(self, val: int) -> None: ...

    def get_heave_m(self) -> float: ...

    def set_heave_m(self, val: float) -> None: ...

    def __eq__(self, other: MWCTxInfo) -> bool: ...

    def copy(self) -> MWCTxInfo:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MWCTxInfo: ...

    def __deepcopy__(self, arg: dict, /) -> MWCTxInfo: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class MWCSectorInfo:
    def __init__(self) -> None: ...

    def get_tilt_angle_re_tx_deg(self) -> float: ...

    def set_tilt_angle_re_tx_deg(self, val: float) -> None: ...

    def get_centre_frequency_hz(self) -> float: ...

    def set_centre_frequency_hz(self, val: float) -> None: ...

    def get_tx_beam_width_along_deg(self) -> float: ...

    def set_tx_beam_width_along_deg(self, val: float) -> None: ...

    def get_tx_sector_number(self) -> int: ...

    def set_tx_sector_number(self, val: int) -> None: ...

    def get_padding(self) -> int: ...

    def set_padding(self, val: int) -> None: ...

    def __eq__(self, other: MWCSectorInfo) -> bool: ...

    def copy(self) -> MWCSectorInfo:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MWCSectorInfo: ...

    def __deepcopy__(self, arg: dict, /) -> MWCSectorInfo: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class MWCSectorInfoVector:
    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, arg: MWCSectorInfoVector) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, arg: Iterable[MWCSectorInfo], /) -> None:
        """Construct from an iterable object"""

    def __len__(self) -> int: ...

    def __bool__(self) -> bool:
        """Check whether the vector is nonempty"""

    def __repr__(self) -> str: ...

    def __iter__(self) -> Iterator[MWCSectorInfo]: ...

    @overload
    def __getitem__(self, arg: int, /) -> MWCSectorInfo: ...

    @overload
    def __getitem__(self, arg: slice, /) -> MWCSectorInfoVector: ...

    def clear(self) -> None:
        """Remove all items from list."""

    def append(self, arg: MWCSectorInfo, /) -> None:
        """Append `arg` to the end of the list."""

    def insert(self, arg0: int, arg1: MWCSectorInfo, /) -> None:
        """Insert object `arg1` before index `arg0`."""

    def pop(self, index: int = -1) -> MWCSectorInfo:
        """Remove and return item at `index` (default last)."""

    def extend(self, arg: MWCSectorInfoVector, /) -> None:
        """Extend `self` by appending elements from `arg`."""

    @overload
    def __setitem__(self, arg0: int, arg1: MWCSectorInfo, /) -> None: ...

    @overload
    def __setitem__(self, arg0: slice, arg1: MWCSectorInfoVector, /) -> None: ...

    @overload
    def __delitem__(self, arg: int, /) -> None: ...

    @overload
    def __delitem__(self, arg: slice, /) -> None: ...

    def __eq__(self, arg: object, /) -> bool: ...

    def __ne__(self, arg: object, /) -> bool: ...

    @overload
    def __contains__(self, arg: MWCSectorInfo, /) -> bool: ...

    @overload
    def __contains__(self, arg: object, /) -> bool: ...

    def count(self, arg: MWCSectorInfo, /) -> int:
        """Return number of occurrences of `arg`."""

    def remove(self, arg: MWCSectorInfo, /) -> None:
        """Remove first occurrence of `arg`."""

class MWCRxInfo:
    def __init__(self) -> None: ...

    def get_bytes_content(self) -> int: ...

    def set_bytes_content(self, val: int) -> None: ...

    def get_number_of_beams(self) -> int: ...

    def set_number_of_beams(self, val: int) -> None: ...

    def get_number_bytes_per_beam_entry(self) -> int: ...

    def set_number_bytes_per_beam_entry(self, val: int) -> None: ...

    def get_phase_flag(self) -> int: ...

    def set_phase_flag(self, val: int) -> None: ...

    def get_tvg_function_applied(self) -> int: ...

    def set_tvg_function_applied(self, val: int) -> None: ...

    def get_tvg_offset_db(self) -> int: ...

    def set_tvg_offset_db(self, val: int) -> None: ...

    def get_sample_freq_hz(self) -> float: ...

    def set_sample_freq_hz(self, val: float) -> None: ...

    def get_sound_velocity_m_per_sec(self) -> float: ...

    def set_sound_velocity_m_per_sec(self, val: float) -> None: ...

    def __eq__(self, other: MWCRxInfo) -> bool: ...

    def copy(self) -> MWCRxInfo:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MWCRxInfo: ...

    def __deepcopy__(self, arg: dict, /) -> MWCRxInfo: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMALLDatagram:
    def __init__(self) -> None: ...

    def get_bytes_datagram(self) -> int: ...

    def set_bytes_datagram(self, bytes_datagram: int) -> None: ...

    def get_datagram_version(self) -> int: ...

    def set_datagram_version(self, datagram_version: int) -> None: ...

    def get_system_id(self) -> int: ...

    def set_system_id(self, system_id: int) -> None: ...

    def get_echo_sounder_id(self) -> int: ...

    def set_echo_sounder_id(self, echo_sounder_id: int) -> None: ...

    def get_time_sec(self) -> int: ...

    def set_time_sec(self, time_sec: int) -> None: ...

    def get_time_nanosec(self) -> int: ...

    def set_time_nanosec(self, time_nanosec: int) -> None: ...

    def set_datagram_identifier(self, datagram_identifier: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> None: ...

    def get_datagram_identifier(self) -> themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier: ...

    def compute_size_content(self) -> int: ...

    def get_timestamp(self) -> float: ...

    def get_datetime(self, timezone_offset_hours: float = 0.0) -> object:
        """Return the timestamp as datetime object"""

    def get_date_string(self, fractional_seconds_digits: int = 2, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str:
        """
        Get the time as string

        Args:
            fractionalSecondsDigits: 
            format: 

        Returns:
            std::string
        """

    def __eq__(self, other: KMALLDatagram) -> bool: ...

    def copy(self) -> KMALLDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> KMALLDatagram:
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

class KMALLUnknown(KMALLDatagram):
    def __init__(self) -> None: ...

    def get_raw_content(self) -> bytes: ...

    def set_raw_content(self, arg: str, /) -> None: ...

    def get_bytes_datagram_check(self) -> int: ...

    def __eq__(self, other: KMALLUnknown) -> bool: ...

    def copy(self) -> KMALLUnknown:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLUnknown: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLUnknown: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> KMALLUnknown:
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

class IInstallationParam(KMALLDatagram):
    """Clock datagrams"""

    def __init__(self) -> None: ...

    def get_bytes_content(self) -> int: ...

    def get_info(self) -> int: ...

    def get_status(self) -> int: ...

    def get_install_txt(self) -> str: ...

    def set_info(self, info: int) -> None: ...

    def set_status(self, status: int) -> None: ...

    def set_install_txt(self, install_txt: str) -> None: ...

    def get_bytes_datagram_check(self) -> int: ...

    def get_install_txt_decoded(self) -> dict[str, str]:
        """
        Decode the install_txt string into a key-value map

        This function parses the KMALL installation parameter text format. The
        format contains comma-separated fields with different separators for
        different field types (e.g., ':' for OSCV, '_' for PU, '=' for SN).

        Returns:
            std::map_std_string_std_string Map of parameter names to
                values
        """

    def get_install_txt_decoded_cached(self) -> dict[str, str]: ...

    @staticmethod
    def decode_install_txt(install_txt: str) -> dict[str, str]:
        """
        Decode an install_txt string into a key-value map (static version)

        Args:
            install_txt: The installation parameter text to decode

        Returns:
            std::map_std_string_std_string Map of parameter names to
                values
        """

    @staticmethod
    def get_install_txt_key_info(key: str) -> str:
        """
        Get human-readable explanation for an install_txt key

        Args:
            key: The key to look up (e.g., "OSCV", "EMXV", "PU")

        Returns:
            std::string Human-readable explanation, or "Unknown key" if not
                found
        """

    @staticmethod
    def get_install_txt_key_infos() -> dict[str, str]:
        """
        Get all known install_txt key explanations

        Returns:
            const std::map_std_string_std_string& Map of keys to their
            explanations
        """

    @staticmethod
    def parse_sensor_string(sensor_string: str) -> dict[str, str]:
        """
        Parse a semicolon-separated sensor string into key-value pairs

        For example: "X=0.000;Y=0.000;Z=0.000;R=0.000;P=0.000;H=0.000"

        Args:
            sensor_string: The sensor string to parse

        Returns:
            std::map_std_string_std_string Map of parameter names to
                values
        """

    @overload
    def get_transducer_offsets(self, transducer_key: str) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets: ...

    @overload
    def get_transducer_offsets(self) -> dict[str, themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets]: ...

    def get_position_system_offsets(self, position_system_number: int) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
        """
        Get the position system offsets for a given position system number

        Parses POSI_1, POSI_2, POSI_3, or POSI_4 entries

        Args:
            position_system_number: Position system number (1-4)

        Returns:
            navigation::datastructures::PositionalOffsets
        """

    def get_attitude_sensor_offsets(self, sensor_number: int) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
        """
        Get the attitude sensor offsets for a given sensor number

        Parses ATTI_1, ATTI_2, ATTI_3, or ATTI_4 entries

        Args:
            sensor_number: Sensor number (1-4)

        Returns:
            navigation::datastructures::PositionalOffsets
        """

    def get_depth_sensor_offsets(self) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
        """
        Get the depth sensor offsets

        Parses DPHI entry

        Returns:
            navigation::datastructures::PositionalOffsets
        """

    def get_water_line_vertical_location_in_meters(self) -> float:
        """
        Get the waterline offset (SWLZ from EMXI)

        Returns:
            float Waterline offset in meters
        """

    def get_active_position_system_number(self) -> int:
        """
        Get the active position system number (1-4)

        Reads the U=ACTIVE field from POSI_n entries

        Returns:
            uint8_t Position system number (1-4), or 0 if none active
        """

    def get_active_attitude_sensor_number(self) -> int:
        """
        Get the active attitude sensor number (1-4)

        Reads the U=ACTIVE field from ATTI_n entries

        Returns:
            uint8_t Attitude sensor number (1-4), or 0 if none active
        """

    def get_system_name(self) -> str:
        """
        Get the system name (EMXV field)

        Returns:
            std::string System name (e.g., "EM2040P")
        """

    def get_pu_serial_number(self) -> int:
        """
        Get the PU serial number (SN field)

        Returns:
            int PU serial number
        """

    def get_available_transducer_keys(self) -> list[str]:
        """
        Get a list of available transducer keys present in the installation
        parameters

        Checks for TRAI_HD1, TRAI_TX1, TRAI_TX2, TRAI_RX1, TRAI_RX2

        Returns:
            std::vector_std_string List of available transducer keys
        """

    def has_transducer_key(self, key: str) -> bool:
        """
        Check if a specific transducer key is present

        Args:
            key: Transducer key (e.g., "TRAI_HD1", "TRAI_TX1")

        Returns:
            bool True if the key is present
        """

    def is_dual_rx(self) -> bool: ...

    def get_system_transducer_configuration(self) -> themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLSystemTransducerConfiguration: ...

    def get_transducer_serial_numbers(self) -> dict[str, str]: ...

    def __eq__(self, other: IInstallationParam) -> bool: ...

    def copy(self) -> IInstallationParam:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> IInstallationParam: ...

    def __deepcopy__(self, arg: dict, /) -> IInstallationParam: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> IInstallationParam:
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

class IOpRuntime(KMALLDatagram):
    """Clock datagrams"""

    def __init__(self) -> None: ...

    def get_bytes_content(self) -> int: ...

    def get_info(self) -> int: ...

    def get_status(self) -> int: ...

    def get_runtime_txt(self) -> str: ...

    def set_info(self, info: int) -> None: ...

    def set_status(self, status: int) -> None: ...

    def set_runtime_txt(self, runtime_txt: str) -> None: ...

    def get_bytes_datagram_check(self) -> int: ...

    def get_runtime_txt_decoded(self) -> dict[str, str]:
        """
        Decode the runtime_txt string into a key-value map

        This function parses the KMALL operator runtime parameter text format.
        The format contains newline-separated sections with key: value pairs.

        Returns:
            std::map_std_string_std_string Map of parameter names to
                values
        """

    @staticmethod
    def decode_runtime_txt(runtime_txt: str) -> dict[str, str]:
        """
        Decode a runtime_txt string into a key-value map (static version)

        Args:
            runtime_txt: The runtime parameter text to decode

        Returns:
            std::map_std_string_std_string Map of parameter names to
                values
        """

    @staticmethod
    def get_runtime_txt_key_info(key: str) -> str:
        """
        Get human-readable explanation for a runtime_txt key

        Args:
            key: The key to look up

        Returns:
            std::string Human-readable explanation, or "Unknown key" if not
                found
        """

    @staticmethod
    def get_runtime_txt_key_infos() -> dict[str, str]:
        """
        Get all known runtime_txt key explanations

        Returns:
            const std::map_std_string_std_string& Map of keys to their
            explanations
        """

    def __eq__(self, other: IOpRuntime) -> bool: ...

    def copy(self) -> IOpRuntime:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> IOpRuntime: ...

    def __deepcopy__(self, arg: dict, /) -> IOpRuntime: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> IOpRuntime:
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

class KMALLSensorDatagram(KMALLDatagram):
    """Clock datagrams"""

    def get_bytes_content(self) -> int: ...

    def get_sensor_system(self) -> int: ...

    def get_sensor_status(self) -> int: ...

    def get_padding(self) -> int: ...

    def set_bytes_content(self, value: int) -> None: ...

    def set_sensor_system(self, value: int) -> None: ...

    def set_sensor_status(self, value: int) -> None: ...

    def set_padding(self, value: int) -> None: ...

    def __eq__(self, other: KMALLSensorDatagram) -> bool: ...

class KMALLMultibeamDatagram(KMALLDatagram):
    """Clock datagrams"""

    def get_number_of_datagrams(self) -> int: ...

    def get_datagram_number(self) -> int: ...

    def get_bytes_content(self) -> int: ...

    def get_ping_count(self) -> int: ...

    def get_rx_fans_per_ping(self) -> int: ...

    def get_rx_fan_index(self) -> int: ...

    def get_swaths_per_ping(self) -> int: ...

    def get_swath_along_position(self) -> int: ...

    def get_tx_transducer_ind(self) -> int: ...

    def get_rx_transducer_ind(self) -> int: ...

    def get_number_of_rx_transducers(self) -> int: ...

    def get_algorithm_type(self) -> int: ...

    def set_number_of_datagrams(self, value: int) -> None: ...

    def set_datagram_number(self, value: int) -> None: ...

    def set_bytes_content(self, value: int) -> None: ...

    def set_ping_count(self, value: int) -> None: ...

    def set_rx_fans_per_ping(self, value: int) -> None: ...

    def set_rx_fan_index(self, value: int) -> None: ...

    def set_swaths_per_ping(self, value: int) -> None: ...

    def set_swath_along_position(self, value: int) -> None: ...

    def set_tx_transducer_ind(self, value: int) -> None: ...

    def set_rx_transducer_ind(self, value: int) -> None: ...

    def set_number_of_rx_transducers(self, value: int) -> None: ...

    def set_algorithm_type(self, value: int) -> None: ...

    def __eq__(self, other: KMALLMultibeamDatagram) -> bool: ...

class SPosition(KMALLSensorDatagram):
    """Clock datagrams"""

    def __init__(self) -> None: ...

    def get_time_from_sensor_sec(self) -> int: ...

    def get_time_from_sensor_nanosec(self) -> int: ...

    def get_pos_fix_quality_m(self) -> float: ...

    def get_corrected_lat_deg(self) -> float: ...

    def get_corrected_lon_deg(self) -> float: ...

    def get_speed_over_ground_m_per_sec(self) -> float: ...

    def get_course_over_ground_deg(self) -> float: ...

    def get_ellipsoid_height_re_ref_point_m(self) -> float: ...

    def get_pos_data_from_sensor(self) -> bytes: ...

    def get_pos_data_from_sensor_str(self) -> str: ...

    def get_bytes_datagram_check(self) -> int: ...

    def set_time_from_sensor_sec(self, val: int) -> None: ...

    def set_time_from_sensor_nanosec(self, val: int) -> None: ...

    def set_pos_fix_quality_m(self, val: float) -> None: ...

    def set_corrected_lat_deg(self, val: float) -> None: ...

    def set_corrected_lon_deg(self, val: float) -> None: ...

    def set_speed_over_ground_m_per_sec(self, val: float) -> None: ...

    def set_course_over_ground_deg(self, val: float) -> None: ...

    def set_ellipsoid_height_re_ref_point_m(self, val: float) -> None: ...

    def set_pos_data_from_sensor(self, pos_data: str) -> None: ...

    def set_bytes_datagram_check(self, val: int) -> None: ...

    def get_sensor_timestamp(self) -> float: ...

    def get_sensor_date_string(self, fractionalSecondsDigits: int = 2, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str:
        """
        Get the time as string

        Args:
            fractionalSecondsDigits: 
            format: 

        Returns:
            std::string
        """

    def get_sensor_datetime(self, timezone_offset_hours: float = 0.0) -> object:
        """Return the timestamp as datetime object"""

    def __eq__(self, other: SPosition) -> bool: ...

    def copy(self) -> SPosition:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SPosition: ...

    def __deepcopy__(self, arg: dict, /) -> SPosition: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SPosition:
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

class SPositionError(KMALLSensorDatagram):
    """Clock datagrams"""

    def __init__(self) -> None: ...

    def get_time_from_sensor_sec(self) -> int: ...

    def get_time_from_sensor_nanosec(self) -> int: ...

    def get_range_input_rms(self) -> float: ...

    def get_ellipse_semi_major_axis_error_m(self) -> float: ...

    def get_ellipse_semi_minor_axis_error_m(self) -> float: ...

    def get_ellipse_erientation_error_deg(self) -> float: ...

    def get_latitude_error_m(self) -> float: ...

    def get_longitude_error_m(self) -> float: ...

    def get_height_error_m(self) -> float: ...

    def get_pos_error_data_from_sensor(self) -> bytes: ...

    def get_pos_error_data_from_sensor_str(self) -> str: ...

    def get_bytes_datagram_check(self) -> int: ...

    def set_time_from_sensor_sec(self, val: int) -> None: ...

    def set_time_from_sensor_nanosec(self, val: int) -> None: ...

    def set_range_input_rms(self, val: float) -> None: ...

    def set_ellipse_semi_major_axis_error_m(self, val: float) -> None: ...

    def set_ellipse_semi_minor_axis_error_m(self, val: float) -> None: ...

    def set_ellipse_erientation_error_deg(self, val: float) -> None: ...

    def set_latitude_error_m(self, val: float) -> None: ...

    def set_longitude_error_m(self, val: float) -> None: ...

    def set_height_error_m(self, val: float) -> None: ...

    def set_pos_error_data_from_sensor(self, pos_error_data: str) -> None: ...

    def set_bytes_datagram_check(self, val: int) -> None: ...

    def get_sensor_timestamp(self) -> float: ...

    def get_sensor_date_string(self, fractionalSecondsDigits: int = 2, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str:
        """
        Get the time as string

        Args:
            fractionalSecondsDigits: 
            format: 

        Returns:
            std::string
        """

    def get_sensor_datetime(self, timezone_offset_hours: float = 0.0) -> object:
        """Return the timestamp as datetime object"""

    def __eq__(self, other: SPositionError) -> bool: ...

    def copy(self) -> SPositionError:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SPositionError: ...

    def __deepcopy__(self, arg: dict, /) -> SPositionError: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SPositionError:
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

class SClock(KMALLSensorDatagram):
    """Clock datagrams"""

    def __init__(self) -> None: ...

    def get_offset_sec(self) -> float: ...

    def get_clock_dev_pu_microsec(self) -> int: ...

    def get_clock_data_from_sensor(self) -> bytes: ...

    def get_clock_data_from_sensor_str(self) -> str: ...

    def get_bytes_datagram_check(self) -> int: ...

    def set_offset_sec(self, offset_sec: float) -> None: ...

    def set_clock_dev_pu_microsec(self, clock_dev_pu_microsec: int) -> None: ...

    def set_clock_data_from_sensor(self, pos_data: str) -> None: ...

    def set_bytes_datagram_check(self, val: int) -> None: ...

    def __eq__(self, other: SClock) -> bool: ...

    def copy(self) -> SClock:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SClock: ...

    def __deepcopy__(self, arg: dict, /) -> SClock: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SClock:
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

class SSoundVelocityProfile_t_sensor_format(enum.Enum):
    sound_velocity_profile = 3158099

    ctd_profile = 3223635

class SSoundVelocityProfile_o_sensor_format:
    """
    Helper class to convert between strings and enum values of type 't_sensor_format'
    """

    @overload
    def __init__(self, value: SSoundVelocityProfile_t_sensor_format = SSoundVelocityProfile_t_sensor_format.sound_velocity_profile) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> SSoundVelocityProfile_t_sensor_format:
        """enum value"""

    @value.setter
    def value(self, arg: SSoundVelocityProfile_t_sensor_format, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityProfile_t_sensor_format = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: SSoundVelocityProfile_o_sensor_format, /) -> bool: ...

    @overload
    def __eq__(self, arg: SSoundVelocityProfile_t_sensor_format, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> SSoundVelocityProfile_o_sensor_format:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SSoundVelocityProfile_o_sensor_format: ...

    def __deepcopy__(self, arg: dict, /) -> SSoundVelocityProfile_o_sensor_format: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SSoundVelocityProfile_o_sensor_format:
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

class SVPPoint:
    """Sound velocity profile sample point"""

    def __init__(self) -> None: ...

    @property
    def depth_m(self) -> float: ...

    @depth_m.setter
    def depth_m(self, arg: float, /) -> None: ...

    @property
    def soundVelocity_m_per_sec(self) -> float: ...

    @soundVelocity_m_per_sec.setter
    def soundVelocity_m_per_sec(self, arg: float, /) -> None: ...

    @property
    def padding(self) -> int: ...

    @padding.setter
    def padding(self, arg: int, /) -> None: ...

    @property
    def temp_c(self) -> float: ...

    @temp_c.setter
    def temp_c(self, arg: float, /) -> None: ...

    @property
    def salinity(self) -> float: ...

    @salinity.setter
    def salinity(self, arg: float, /) -> None: ...

    def copy(self) -> SVPPoint:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SVPPoint: ...

    def __deepcopy__(self, arg: dict, /) -> SVPPoint: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SSoundVelocityProfile(KMALLDatagram):
    """Clock datagrams"""

    def __init__(self) -> None: ...

    def get_bytes_content(self) -> int: ...

    def get_number_of_samples(self) -> int: ...

    def get_sensor_format(self) -> SSoundVelocityProfile_o_sensor_format: ...

    def get_svp_time_sec(self) -> int: ...

    def get_latitude_deg(self) -> float: ...

    def get_longitude_deg(self) -> float: ...

    def get_sensor_data(self) -> list[SVPPoint]: ...

    def set_bytes_content(self, value: int) -> None: ...

    def set_number_of_samples(self, value: int) -> None: ...

    def set_sensor_format(self, value: SSoundVelocityProfile_o_sensor_format) -> None: ...

    def set_svp_time_sec(self, value: int) -> None: ...

    def set_latitude_deg(self, value: float) -> None: ...

    def set_longitude_deg(self, value: float) -> None: ...

    def set_sensor_data(self, data: Sequence[SVPPoint]) -> None: ...

    def get_bytes_datagram_check(self) -> int: ...

    def set_bytes_datagram_check(self, value: int) -> None: ...

    def get_svp_depths(self) -> list[float]: ...

    def get_svp_sound_velocities(self) -> list[float]: ...

    def get_svp_sound_velocities_computed(self) -> list[float]: ...

    def get_svp_absorption_computed(self, frequency: float, ph: float = 8) -> list[float]: ...

    def get_svp_salinities(self) -> list[float]: ...

    def get_svp_temperatures(self) -> list[float]: ...

    def __eq__(self, other: SSoundVelocityProfile) -> bool: ...

    def copy(self) -> SSoundVelocityProfile:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SSoundVelocityProfile: ...

    def __deepcopy__(self, arg: dict, /) -> SSoundVelocityProfile: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SSoundVelocityProfile:
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

class SSoundVelocityTransducer_t_sensor_format(enum.Enum):
    AML_NMEA = 1

    AML_SV = 2

    AML_SVT = 3

    AML_SVP = 4

    Micro_SV = 5

    Micro_SVT = 6

    Micro_SVP = 7

    Valeport_MiniSVS = 8

    KSSIS_80 = 9

    KSSIS_43 = 10

    XDR_S = 11

    Valeport_NMEA = 12

class SSoundVelocityTransducer_o_sensor_format:
    """
    Helper class to convert between strings and enum values of type 't_sensor_format'
    """

    @overload
    def __init__(self, value: SSoundVelocityTransducer_t_sensor_format = SSoundVelocityTransducer_t_sensor_format.AML_NMEA) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> SSoundVelocityTransducer_t_sensor_format:
        """enum value"""

    @value.setter
    def value(self, arg: SSoundVelocityTransducer_t_sensor_format, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SSoundVelocityTransducer_t_sensor_format = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: SSoundVelocityTransducer_o_sensor_format, /) -> bool: ...

    @overload
    def __eq__(self, arg: SSoundVelocityTransducer_t_sensor_format, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> SSoundVelocityTransducer_o_sensor_format:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SSoundVelocityTransducer_o_sensor_format: ...

    def __deepcopy__(self, arg: dict, /) -> SSoundVelocityTransducer_o_sensor_format: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SSoundVelocityTransducer_o_sensor_format:
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

class SVTSample:
    """Sound velocity transducer sample point"""

    def __init__(self) -> None: ...

    @property
    def time_sec(self) -> int: ...

    @time_sec.setter
    def time_sec(self, arg: int, /) -> None: ...

    @property
    def time_nanosec(self) -> int: ...

    @time_nanosec.setter
    def time_nanosec(self, arg: int, /) -> None: ...

    @property
    def soundVelocity_m_per_sec(self) -> float: ...

    @soundVelocity_m_per_sec.setter
    def soundVelocity_m_per_sec(self, arg: float, /) -> None: ...

    @property
    def temp_c(self) -> float: ...

    @temp_c.setter
    def temp_c(self, arg: float, /) -> None: ...

    @property
    def pressure_pa(self) -> float: ...

    @pressure_pa.setter
    def pressure_pa(self, arg: float, /) -> None: ...

    @property
    def salinity(self) -> float: ...

    @salinity.setter
    def salinity(self, arg: float, /) -> None: ...

    def copy(self) -> SVTSample:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SVTSample: ...

    def __deepcopy__(self, arg: dict, /) -> SVTSample: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SSoundVelocityTransducer(KMALLDatagram):
    """Clock datagrams"""

    def __init__(self) -> None: ...

    def get_bytes_content(self) -> int: ...

    def get_sensor_status(self) -> int: ...

    def get_sensor_input_format(self) -> SSoundVelocityTransducer_o_sensor_format: ...

    def get_number_of_samples(self) -> int: ...

    def get_number_of_bytes_per_sample(self) -> int: ...

    def get_sensor_data_contents(self) -> int: ...

    def get_filter_time_sec(self) -> float: ...

    def get_sound_velocity_offset_m_per_sec(self) -> float: ...

    def get_sensor_data(self) -> list[SVTSample]: ...

    def set_bytes_content(self, value: int) -> None: ...

    def set_sensor_status(self, value: int) -> None: ...

    def set_sensor_input_format(self, value: SSoundVelocityTransducer_o_sensor_format) -> None: ...

    def set_number_of_samples(self, value: int) -> None: ...

    def set_number_of_bytes_per_sample(self, value: int) -> None: ...

    def set_sensor_data_contents(self, value: int) -> None: ...

    def set_filter_time_sec(self, value: float) -> None: ...

    def set_sound_velocity_offset_m_per_sec(self, value: float) -> None: ...

    def set_sensor_data(self, data: Sequence[SVTSample]) -> None: ...

    def get_bytes_datagram_check(self) -> int: ...

    def set_bytes_datagram_check(self, value: int) -> None: ...

    def get_sound_velocity_active(self) -> bool: ...

    def get_temperature_active(self) -> bool: ...

    def get_pressure_active(self) -> bool: ...

    def get_salinity_active(self) -> bool: ...

    def set_sound_velocity_active(self, active: bool) -> None: ...

    def set_temperature_active(self, active: bool) -> None: ...

    def set_pressure_active(self, active: bool) -> None: ...

    def set_salinity_active(self, active: bool) -> None: ...

    def get_svt_timestamps(self) -> list[float]: ...

    def get_svt_sound_velocities(self) -> list[float]: ...

    def get_svt_temperatures(self) -> list[float]: ...

    def get_svt_pressures(self) -> list[float]: ...

    def get_svt_salinities(self) -> list[float]: ...

    def __eq__(self, other: SSoundVelocityTransducer) -> bool: ...

    def copy(self) -> SSoundVelocityTransducer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SSoundVelocityTransducer: ...

    def __deepcopy__(self, arg: dict, /) -> SSoundVelocityTransducer: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SSoundVelocityTransducer:
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

class SKMBinary_t_sensor_format(enum.Enum):
    KM_binary_Sensor_Input = 1

    EM_3000_data = 2

    Sagem = 3

    Seapath_binary_11 = 4

    Seapath_binary_23 = 5

    Seapath_binary_26 = 6

    POS_M_V_GRP_102_103 = 7

class SKMBinary_o_sensor_format:
    """
    Helper class to convert between strings and enum values of type 't_sensor_format'
    """

    @overload
    def __init__(self, value: SKMBinary_t_sensor_format = SKMBinary_t_sensor_format.KM_binary_Sensor_Input) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> SKMBinary_t_sensor_format:
        """enum value"""

    @value.setter
    def value(self, arg: SKMBinary_t_sensor_format, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.kmall.datagrams.SKMBinary_t_sensor_format = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: SKMBinary_o_sensor_format, /) -> bool: ...

    @overload
    def __eq__(self, arg: SKMBinary_t_sensor_format, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> SKMBinary_o_sensor_format:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SKMBinary_o_sensor_format: ...

    def __deepcopy__(self, arg: dict, /) -> SKMBinary_o_sensor_format: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SKMBinary_o_sensor_format:
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

class KMBinary:
    """Kongsberg KM Binary navigation sample"""

    def __init__(self) -> None: ...

    @property
    def datagram_identifier(self) -> themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier: ...

    @datagram_identifier.setter
    def datagram_identifier(self, arg: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, /) -> None: ...

    @property
    def bytes_content(self) -> int: ...

    @bytes_content.setter
    def bytes_content(self, arg: int, /) -> None: ...

    @property
    def dgm_version(self) -> int: ...

    @dgm_version.setter
    def dgm_version(self, arg: int, /) -> None: ...

    @property
    def time_sec(self) -> int: ...

    @time_sec.setter
    def time_sec(self, arg: int, /) -> None: ...

    @property
    def time_nanosec(self) -> int: ...

    @time_nanosec.setter
    def time_nanosec(self, arg: int, /) -> None: ...

    @property
    def status(self) -> int: ...

    @status.setter
    def status(self, arg: int, /) -> None: ...

    @property
    def latitude_deg(self) -> float: ...

    @latitude_deg.setter
    def latitude_deg(self, arg: float, /) -> None: ...

    @property
    def longitude_deg(self) -> float: ...

    @longitude_deg.setter
    def longitude_deg(self, arg: float, /) -> None: ...

    @property
    def ellipsoid_height_m(self) -> float: ...

    @ellipsoid_height_m.setter
    def ellipsoid_height_m(self, arg: float, /) -> None: ...

    @property
    def roll_deg(self) -> float: ...

    @roll_deg.setter
    def roll_deg(self, arg: float, /) -> None: ...

    @property
    def pitch_deg(self) -> float: ...

    @pitch_deg.setter
    def pitch_deg(self, arg: float, /) -> None: ...

    @property
    def heading_deg(self) -> float: ...

    @heading_deg.setter
    def heading_deg(self, arg: float, /) -> None: ...

    @property
    def heave_m(self) -> float: ...

    @heave_m.setter
    def heave_m(self, arg: float, /) -> None: ...

    @property
    def roll_rate(self) -> float: ...

    @roll_rate.setter
    def roll_rate(self, arg: float, /) -> None: ...

    @property
    def pitch_rate(self) -> float: ...

    @pitch_rate.setter
    def pitch_rate(self, arg: float, /) -> None: ...

    @property
    def yaw_rate(self) -> float: ...

    @yaw_rate.setter
    def yaw_rate(self, arg: float, /) -> None: ...

    @property
    def vel_north(self) -> float: ...

    @vel_north.setter
    def vel_north(self, arg: float, /) -> None: ...

    @property
    def vel_east(self) -> float: ...

    @vel_east.setter
    def vel_east(self, arg: float, /) -> None: ...

    @property
    def vel_down(self) -> float: ...

    @vel_down.setter
    def vel_down(self, arg: float, /) -> None: ...

    @property
    def latitude_error_m(self) -> float: ...

    @latitude_error_m.setter
    def latitude_error_m(self, arg: float, /) -> None: ...

    @property
    def longitude_error_m(self) -> float: ...

    @longitude_error_m.setter
    def longitude_error_m(self, arg: float, /) -> None: ...

    @property
    def ellipsoid_height_error_m(self) -> float: ...

    @ellipsoid_height_error_m.setter
    def ellipsoid_height_error_m(self, arg: float, /) -> None: ...

    @property
    def roll_error_deg(self) -> float: ...

    @roll_error_deg.setter
    def roll_error_deg(self, arg: float, /) -> None: ...

    @property
    def pitch_error_deg(self) -> float: ...

    @pitch_error_deg.setter
    def pitch_error_deg(self, arg: float, /) -> None: ...

    @property
    def heading_error_deg(self) -> float: ...

    @heading_error_deg.setter
    def heading_error_deg(self, arg: float, /) -> None: ...

    @property
    def heave_error_m(self) -> float: ...

    @heave_error_m.setter
    def heave_error_m(self, arg: float, /) -> None: ...

    @property
    def north_acceleration(self) -> float: ...

    @north_acceleration.setter
    def north_acceleration(self, arg: float, /) -> None: ...

    @property
    def east_acceleration(self) -> float: ...

    @east_acceleration.setter
    def east_acceleration(self, arg: float, /) -> None: ...

    @property
    def down_acceleration(self) -> float: ...

    @down_acceleration.setter
    def down_acceleration(self, arg: float, /) -> None: ...

    def get_horizontal_position_and_velocity_valid(self) -> bool: ...

    def get_roll_and_pitch_valid(self) -> bool: ...

    def get_heading_valid(self) -> bool: ...

    def get_heave_valid(self) -> bool: ...

    def get_acceleration_valid(self) -> bool: ...

    def get_delayed_heave1_valid(self) -> bool: ...

    def get_delayed_heave2_valid(self) -> bool: ...

    def get_horizontal_position_and_velocity_reduced_performance(self) -> bool: ...

    def get_roll_and_pitch_reduced_performance(self) -> bool: ...

    def get_heading_reduced_performance(self) -> bool: ...

    def get_heave_reduced_performance(self) -> bool: ...

    def get_acceleration_reduced_performance(self) -> bool: ...

    def get_delayed_heave1_reduced_performance(self) -> bool: ...

    def get_delayed_heave2_reduced_performance(self) -> bool: ...

    def set_horizontal_position_and_velocity_valid(self, valid: bool) -> None: ...

    def set_roll_and_pitch_valid(self, valid: bool) -> None: ...

    def set_heading_valid(self, valid: bool) -> None: ...

    def set_heave_valid(self, valid: bool) -> None: ...

    def set_acceleration_valid(self, valid: bool) -> None: ...

    def set_delayed_heave1_valid(self, valid: bool) -> None: ...

    def set_delayed_heave2_valid(self, valid: bool) -> None: ...

    def set_horizontal_position_and_velocity_reduced_performance(self, reduced_performance: bool) -> None: ...

    def set_roll_and_pitch_reduced_performance(self, reduced_performance: bool) -> None: ...

    def set_heading_reduced_performance(self, reduced_performance: bool) -> None: ...

    def set_heave_reduced_performance(self, reduced_performance: bool) -> None: ...

    def set_acceleration_reduced_performance(self, reduced_performance: bool) -> None: ...

    def set_delayed_heave1_reduced_performance(self, reduced_performance: bool) -> None: ...

    def set_delayed_heave2_reduced_performance(self, reduced_performance: bool) -> None: ...

    def copy(self) -> KMBinary:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMBinary: ...

    def __deepcopy__(self, arg: dict, /) -> KMBinary: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KMDelayedHeave:
    """KM Binary delayed heave sample"""

    def __init__(self) -> None: ...

    @property
    def time_sec(self) -> int: ...

    @time_sec.setter
    def time_sec(self, arg: int, /) -> None: ...

    @property
    def time_nanosec(self) -> int: ...

    @time_nanosec.setter
    def time_nanosec(self, arg: int, /) -> None: ...

    @property
    def delayed_heave_m(self) -> float: ...

    @delayed_heave_m.setter
    def delayed_heave_m(self, arg: float, /) -> None: ...

    def copy(self) -> KMDelayedHeave:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMDelayedHeave: ...

    def __deepcopy__(self, arg: dict, /) -> KMDelayedHeave: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SKMSample:
    """KM Binary composite sample"""

    def __init__(self) -> None: ...

    @property
    def km_binary(self) -> KMBinary: ...

    @km_binary.setter
    def km_binary(self, arg: KMBinary, /) -> None: ...

    @property
    def km_delayed_heave(self) -> KMDelayedHeave: ...

    @km_delayed_heave.setter
    def km_delayed_heave(self, arg: KMDelayedHeave, /) -> None: ...

    def copy(self) -> SKMSample:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SKMSample: ...

    def __deepcopy__(self, arg: dict, /) -> SKMSample: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SKMBinary(KMALLDatagram):
    """Clock datagrams"""

    def __init__(self) -> None: ...

    def get_bytes_content(self) -> int: ...

    def get_sensor_system(self) -> int: ...

    def get_sensor_status(self) -> int: ...

    def get_sensor_format(self) -> SKMBinary_o_sensor_format: ...

    def get_number_of_samples(self) -> int: ...

    def get_number_of_bytes_per_sample(self) -> int: ...

    def get_sensor_data_contents(self) -> int: ...

    def get_sensor_data(self) -> list[SKMSample]: ...

    def get_bytes_datagram_check(self) -> int: ...

    def set_bytes_content(self, value: int) -> None: ...

    def set_sensor_system(self, value: int) -> None: ...

    def set_sensor_status(self, value: int) -> None: ...

    def set_sensor_format(self, value: SKMBinary_o_sensor_format) -> None: ...

    def set_number_of_samples(self, value: int) -> None: ...

    def set_number_of_bytes_per_sample(self, value: int) -> None: ...

    def set_sensor_data_contents(self, value: int) -> None: ...

    def set_sensor_data(self, data: Sequence[SKMSample]) -> None: ...

    def set_bytes_datagram_check(self, value: int) -> None: ...

    def get_horizontal_position_and_velocity_active(self) -> bool: ...

    def get_roll_and_pitch_active(self) -> bool: ...

    def get_heading_active(self) -> bool: ...

    def get_heave_active(self) -> bool: ...

    def get_acceleration_active(self) -> bool: ...

    def get_delayed_heave1_active(self) -> bool: ...

    def get_delayed_heave2_active(self) -> bool: ...

    def set_horizontal_position_and_velocity_active(self, active: bool) -> None: ...

    def set_roll_and_pitch_active(self, active: bool) -> None: ...

    def set_heading_active(self, active: bool) -> None: ...

    def set_heave_active(self, active: bool) -> None: ...

    def set_acceleration_active(self, active: bool) -> None: ...

    def set_delayed_heave1_active(self, active: bool) -> None: ...

    def set_delayed_heave2_active(self, active: bool) -> None: ...

    def __eq__(self, other: SKMBinary) -> bool: ...

    def copy(self) -> SKMBinary:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SKMBinary: ...

    def __deepcopy__(self, arg: dict, /) -> SKMBinary: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SKMBinary:
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

class CPosition(KMALLSensorDatagram):
    """Clock datagrams"""

    def __init__(self) -> None: ...

    def get_time_from_sensor_sec(self) -> int: ...

    def get_time_from_sensor_nanosec(self) -> int: ...

    def get_pos_fix_quality_m(self) -> float: ...

    def get_corrected_lat_deg(self) -> float: ...

    def get_corrected_lon_deg(self) -> float: ...

    def get_speed_over_ground_m_per_sec(self) -> float: ...

    def get_course_over_ground_deg(self) -> float: ...

    def get_ellipsoid_height_re_ref_point_m(self) -> float: ...

    def get_pos_data_from_sensor(self) -> bytes: ...

    def get_pos_data_from_sensor_str(self) -> str: ...

    def get_bytes_datagram_check(self) -> int: ...

    def set_time_from_sensor_sec(self, val: int) -> None: ...

    def set_time_from_sensor_nanosec(self, val: int) -> None: ...

    def set_pos_fix_quality_m(self, val: float) -> None: ...

    def set_corrected_lat_deg(self, val: float) -> None: ...

    def set_corrected_lon_deg(self, val: float) -> None: ...

    def set_speed_over_ground_m_per_sec(self, val: float) -> None: ...

    def set_course_over_ground_deg(self, val: float) -> None: ...

    def set_ellipsoid_height_re_ref_point_m(self, val: float) -> None: ...

    def set_pos_data_from_sensor(self, pos_data: str) -> None: ...

    def set_bytes_datagram_check(self, val: int) -> None: ...

    def get_sensor_timestamp(self) -> float: ...

    def get_sensor_date_string(self, fractionalSecondsDigits: int = 2, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str:
        """
        Get the time as string

        Args:
            fractionalSecondsDigits: 
            format: 

        Returns:
            std::string
        """

    def get_sensor_datetime(self, timezone_offset_hours: float = 0.0) -> object:
        """Return the timestamp as datetime object"""

    def __eq__(self, other: CPosition) -> bool: ...

    def copy(self) -> CPosition:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> CPosition: ...

    def __deepcopy__(self, arg: dict, /) -> CPosition: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> CPosition:
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

class CHeave(KMALLMultibeamDatagram):
    """
    Heave compatibility datagrams

    #CHE - Struct of compatibility heave sensor datagram.

    Used for backward compatibility with .all datagram format. Sent before
    #MWC (water column datagram) datagram if compatibility mode is
    enabled. The multibeam datagram body is common with the #MWC datagram.
    """

    def __init__(self) -> None: ...

    def get_heave_m(self) -> float: ...

    def get_bytes_datagram_check(self) -> int: ...

    def set_heave_m(self, heave_m: float) -> None: ...

    def set_bytes_datagram_check(self, val: int) -> None: ...

    def __eq__(self, other: CHeave) -> bool: ...

    def copy(self) -> CHeave:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> CHeave: ...

    def __deepcopy__(self, arg: dict, /) -> CHeave: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> CHeave:
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

class MRangeAndDepth(KMALLMultibeamDatagram):
    def __init__(self) -> None: ...

    @property
    def ping_info(self) -> MRZPingInfo: ...

    @ping_info.setter
    def ping_info(self, arg: MRZPingInfo, /) -> None: ...

    @property
    def rx_info(self) -> MRZRxInfo: ...

    @rx_info.setter
    def rx_info(self, arg: MRZRxInfo, /) -> None: ...

    @property
    def tx_sectors(self) -> list[MRZSectorInfo]: ...

    @tx_sectors.setter
    def tx_sectors(self, arg: Sequence[MRZSectorInfo], /) -> None: ...

    @property
    def extra_det_class_info(self) -> list[MRZExtraDetClassInfo]: ...

    @extra_det_class_info.setter
    def extra_det_class_info(self, arg: Sequence[MRZExtraDetClassInfo], /) -> None: ...

    @property
    def soundings(self) -> MRZSoundingsContainer: ...

    @soundings.setter
    def soundings(self, arg: MRZSoundingsContainer, /) -> None: ...

    def get_seabed_image_samples_dezi_db(self) -> Annotated[NDArray[numpy.int16], dict(shape=(None,), order='C')]: ...

    def set_seabed_image_samples_dezi_db(self, samples: Annotated[NDArray[numpy.int16], dict(shape=(None,), order='C')]) -> None: ...

    def get_seabed_image_samples_db(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def set_seabed_image_samples_db(self, samples: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None: ...

    def __eq__(self, other: MRangeAndDepth) -> bool: ...

    def copy(self) -> MRangeAndDepth:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MRangeAndDepth: ...

    def __deepcopy__(self, arg: dict, /) -> MRangeAndDepth: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> MRangeAndDepth:
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

class MWaterColumn(KMALLMultibeamDatagram):
    def __init__(self) -> None: ...

    @property
    def tx_info(self) -> MWCTxInfo: ...

    @tx_info.setter
    def tx_info(self, arg: MWCTxInfo, /) -> None: ...

    @property
    def rx_info(self) -> MWCRxInfo: ...

    @rx_info.setter
    def rx_info(self, arg: MWCRxInfo, /) -> None: ...

    @property
    def tx_sectors(self) -> list[MWCSectorInfo]: ...

    @tx_sectors.setter
    def tx_sectors(self, arg: Sequence[MWCSectorInfo], /) -> None: ...

    @property
    def beam_data(self) -> MWCRxBeamDataContainer: ...

    @beam_data.setter
    def beam_data(self, arg: MWCRxBeamDataContainer, /) -> None: ...

    def __eq__(self, other: MWaterColumn) -> bool: ...

    def copy(self) -> MWaterColumn:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MWaterColumn: ...

    def __deepcopy__(self, arg: dict, /) -> MWaterColumn: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> MWaterColumn:
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
