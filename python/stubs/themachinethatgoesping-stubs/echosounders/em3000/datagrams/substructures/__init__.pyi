"""Kongsberg EM3000 datagram substructures. These are substuctures of existing datagrams (repeated cycles, e.g. beams)"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000.datagrams.substructures
import typing

__all__ = [
    "AmplitudeDetect",
    "Estimated",
    "ExtraDetectionsDetectionClasses",
    "ExtraDetectionsExtraDetections",
    "Interpolated",
    "Invalid",
    "InvalidNormalDetection",
    "NoDetection",
    "PhaseDetect",
    "RawRangeAndAngleBeam",
    "RawRangeAndAngleTransmitSector",
    "Rejected",
    "XYZDatagramBeam",
    "XYZDatagramBeam_t_DetectionType"
]


class ExtraDetectionsDetectionClasses():
    """
    Extra Detections Detection Classes
    """
    def __copy__(self) -> ExtraDetectionsDetectionClasses: ...
    def __deepcopy__(self, arg0: dict) -> ExtraDetectionsDetectionClasses: ...
    def __eq__(self, other: ExtraDetectionsDetectionClasses) -> bool: ...
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> ExtraDetectionsDetectionClasses: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_alarm_flag_1(self) -> int: 
        """
        < 0: (no alarm) 1:Number of extra detections are above Alarm
        threshold.
        """
    def get_alarm_threshold(self) -> int: 
        """
        < number of extra det. required (1-99 0=off)
        """
    def get_bs_threshold(self) -> int: 
        """
        < dB (-10 - 60)
        """
    def get_number_of_extra_detections(self) -> int: 
        """
        <
        """
    def get_qf_threshold(self) -> float: 
        """
        Get the ifremer QF threshold The Ifremer Quality factor is used to
        estimate the relative depth error. QF threshold equal to 0.1 means a
        0.1% depth error threshold. At 100 m depth this the depth error
        threshold would be 10 cm. Valid range is 0.01 to 1 %.

        Returns:
            qf_threshold_100 * 0.01 (double)
        """
    def get_qf_threshold_100(self) -> int: 
        """
        < 100 * QF threshold (1-100)
        """
    def get_show_class(self) -> bool: 
        """
        < 0-1
        """
    def get_snr_threshold(self) -> int: 
        """
        < 5-15
        """
    def get_start_depth(self) -> int: 
        """
        < % of depth (0-300)
        """
    def get_stop_depth(self) -> int: 
        """
        < % of depth (1-300)
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_alarm_flag_1(self, arg0: int) -> None: 
        """
        < 0: (no alarm) 1:Number of extra detections are above Alarm
        threshold.
        """
    def set_alarm_threshold(self, arg0: int) -> None: 
        """
        < number of extra det. required (1-99 0=off)
        """
    def set_bs_threshold(self, arg0: int) -> None: 
        """
        < dB (-10 - 60)
        """
    def set_number_of_extra_detections(self, arg0: int) -> None: 
        """
        <
        """
    def set_qf_threshold_100(self, arg0: int) -> None: 
        """
        < 100 * QF threshold (1-100)
        """
    def set_show_class(self, arg0: bool) -> None: 
        """
        < 0-1
        """
    def set_snr_threshold(self, arg0: int) -> None: 
        """
        < 5-15
        """
    def set_start_depth(self, arg0: int) -> None: 
        """
        < % of depth (0-300)
        """
    def set_stop_depth(self, arg0: int) -> None: 
        """
        < % of depth (1-300)
        """
    __hash__ = None
    pass
class ExtraDetectionsExtraDetections():
    """
    Extra Detections in the extra detections datagram
    """
    def __copy__(self) -> ExtraDetectionsExtraDetections: ...
    def __deepcopy__(self, arg0: dict) -> ExtraDetectionsExtraDetections: ...
    def __eq__(self, other: ExtraDetectionsExtraDetections) -> bool: ...
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> ExtraDetectionsExtraDetections: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_across(self) -> float: 
        """
        < y in m
        """
    def get_along(self) -> float: 
        """
        < x in m
        """
    def get_applied_pointing_angle_correction(self) -> float: 
        """
        <
        """
    def get_applied_two_way_travel_time_corrections(self) -> float: 
        """
        < seconds, f.ex. Doppler correction
        """
    def get_backscatter(self) -> int: 
        """
        < 0.1 dB
        """
    def get_backscatter_in_db(self) -> float: 
        """
        Get the backscatter in dB

        Returns:
            _backscatter * 0.1 dB (double)
        """
    def get_backscatter_is_compensated(self) -> bool: 
        """
        This function evaluates the detection information flag. If the 4th bit
        is set to 1, the detection is compensated for beam incident angle. If
        the 4th bit is set to 0, the detection is not compensated for beam
        incident angle.

        Returns:
            true

        Returns:
            false
        """
    def get_beam_angle_across(self) -> float: 
        """
        < re vertical °
        """
    def get_beam_incidence_angle_adjustment(self) -> int: 
        """
        < IBA in 0.1°
        """
    def get_beam_pointing_angle(self) -> float: 
        """
        < deg. re array
        """
    def get_confidence_level(self) -> int: 
        """
        <
        """
    def get_delta_latitude(self) -> float: 
        """
        < °
        """
    def get_delta_longitude(self) -> float: 
        """
        < °
        """
    def get_depth(self) -> float: 
        """
        < z in m
        """
    def get_detected_range(self) -> int: 
        """
        < in (WCsr) samples
        """
    def get_detection_class_number(self) -> int: 
        """
        <
        """
    def get_detection_info(self) -> int: ...
    def get_detection_is_valid(self) -> bool: 
        """
        This function evaluates the detection information flag. If the last
        bit is set to 1, the detection is valid. If the last bit is set to 0,
        the detection is invalid.

        Returns:
            true

        Returns:
            false
        """
    def get_detection_type(self) -> XYZDatagramBeam_t_DetectionType: 
        """
        This function evaluates the detection information flag. The first 3
        bits indicate the type of detection.

        Returns:
            t_DetectionType
        """
    def get_detection_window_length(self) -> int: 
        """
        <
        """
    def get_number_of_raw_amplitude_samples(self) -> int: 
        """
        < NS
        """
    def get_qf_10(self) -> int: 
        """
        < Ifremer Quality factor * 10
        """
    def get_qf_threshold(self) -> float: 
        """
        Get the ifremer QF threshold

        Returns:
            qf_threshold_10 * 0.1 (double)
        """
    def get_quality_factor_old(self) -> int: 
        """
        <
        """
    def get_range_factor(self) -> int: 
        """
        < in %
        """
    def get_real_time_cleaning_info(self) -> int: 
        """
        <
        """
    def get_spare(self) -> int: ...
    def get_two_way_travel_time(self) -> float: 
        """
        < s
        """
    def get_tx_sector_number(self) -> int: 
        """
        < or TX array index
        """
    def get_water_column_beam_number(self) -> int: 
        """
        <
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_across(self, arg0: float) -> None: 
        """
        < y in m
        """
    def set_along(self, arg0: float) -> None: 
        """
        < x in m
        """
    def set_applied_pointing_angle_correction(self, arg0: float) -> None: 
        """
        <
        """
    def set_applied_two_way_travel_time_corrections(self, arg0: float) -> None: 
        """
        < seconds, f.ex. Doppler correction
        """
    def set_backscatter(self, arg0: int) -> None: 
        """
        < 0.1 dB
        """
    def set_beam_angle_across(self, arg0: float) -> None: 
        """
        < re vertical °
        """
    def set_beam_incidence_angle_adjustment(self, arg0: int) -> None: 
        """
        < IBA in 0.1°
        """
    def set_beam_pointing_angle(self, arg0: float) -> None: 
        """
        < deg. re array
        """
    def set_confidence_level(self, arg0: int) -> None: 
        """
        <
        """
    def set_delta_latitude(self, arg0: float) -> None: 
        """
        < °
        """
    def set_delta_longitude(self, arg0: float) -> None: 
        """
        < °
        """
    def set_depth(self, arg0: float) -> None: 
        """
        < z in m
        """
    def set_detected_range(self, arg0: int) -> None: 
        """
        < in (WCsr) samples
        """
    def set_detection_class_number(self, arg0: int) -> None: 
        """
        <
        """
    def set_detection_info(self, arg0: int) -> None: ...
    def set_detection_window_length(self, arg0: int) -> None: 
        """
        <
        """
    def set_number_of_raw_amplitude_samples(self, arg0: int) -> None: 
        """
        < NS
        """
    def set_qf_10(self, arg0: int) -> None: 
        """
        < Ifremer Quality factor * 10
        """
    def set_quality_factor_old(self, arg0: int) -> None: 
        """
        <
        """
    def set_range_factor(self, arg0: int) -> None: 
        """
        < in %
        """
    def set_real_time_cleaning_info(self, arg0: int) -> None: 
        """
        <
        """
    def set_spare(self, arg0: int) -> None: ...
    def set_two_way_travel_time(self, arg0: float) -> None: 
        """
        < s
        """
    def set_tx_sector_number(self, arg0: int) -> None: 
        """
        < or TX array index
        """
    def set_water_column_beam_number(self, arg0: int) -> None: 
        """
        <
        """
    __hash__ = None
    pass
class RawRangeAndAngleBeam():
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    def __copy__(self) -> RawRangeAndAngleBeam: ...
    def __deepcopy__(self, arg0: dict) -> RawRangeAndAngleBeam: ...
    def __eq__(self, other: RawRangeAndAngleBeam) -> bool: ...
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> RawRangeAndAngleBeam: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_beam_pointing_angle(self) -> int: ...
    def get_beam_pointing_angle_in_degrees(self) -> float: 
        """
        Get the beam pointing angle in °

        Returns:
            _beam_pointing_angle * 0.01 (float)
        """
    def get_d_corr(self) -> int: ...
    def get_detection_info(self) -> int: ...
    def get_detection_is_valid(self) -> bool: 
        """
        This function evaluates the detection information flag. If the last
        bit is set to 1, the detection is valid. If the last bit is set to 0,
        the detection is invalid.

        Returns:
            true

        Returns:
            false
        """
    def get_detection_type(self) -> XYZDatagramBeam_t_DetectionType: 
        """
        This function evaluates the detection information flag. The first 3
        bits indicate the type of detection.

        Returns:
            t_DetectionType
        """
    def get_detection_window_length_in_samples(self) -> int: ...
    def get_quality_factor(self) -> int: ...
    def get_realtime_cleaning_info(self) -> int: ...
    def get_reflectivity(self) -> int: 
        """
        < in 0.1 dB resolution
        """
    def get_reflectivity_in_db(self) -> float: 
        """
        Get the reflectivity in db

        Returns:
            _reflectivity * 0.1 (float)
        """
    def get_spare(self) -> int: ...
    def get_transmit_sector_number(self) -> int: 
        """
        M relative RX array in 0.01°
        """
    def get_two_way_travel_time(self) -> float: 
        """
        < in s
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_beam_pointing_angle(self, arg0: int) -> None: ...
    def set_d_corr(self, arg0: int) -> None: ...
    def set_detection_info(self, arg0: int) -> None: ...
    def set_detection_window_length_in_samples(self, arg0: int) -> None: ...
    def set_quality_factor(self, arg0: int) -> None: ...
    def set_realtime_cleaning_info(self, arg0: int) -> None: ...
    def set_reflectivity(self, arg0: int) -> None: 
        """
        < in 0.1 dB resolution
        """
    def set_spare(self, arg0: int) -> None: ...
    def set_transmit_sector_number(self, arg0: int) -> None: 
        """
        M relative RX array in 0.01°
        """
    def set_two_way_travel_time(self, arg0: float) -> None: 
        """
        < in s
        """
    __hash__ = None
    pass
class RawRangeAndAngleTransmitSector():
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    def __copy__(self) -> RawRangeAndAngleTransmitSector: ...
    def __deepcopy__(self, arg0: dict) -> RawRangeAndAngleTransmitSector: ...
    def __eq__(self, other: RawRangeAndAngleTransmitSector) -> bool: ...
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> RawRangeAndAngleTransmitSector: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_centre_frequency(self) -> float: 
        """
        < in Hz
        """
    def get_focus_range(self) -> int: 
        """
        < in 0.1m 0 = no focus applied
        """
    def get_focus_range_in_m(self) -> float: 
        """
        Get the focus range in m

        Returns:
            _focus_range * 0.1 (float)
        """
    def get_mean_absorption_coefficient(self) -> int: 
        """
        < in 0.01 dB/km
        """
    def get_mean_absorption_coefficient_in_dB_per_m(self) -> float: 
        """
        Get the mean absorption coefficient in dB/m

        Returns:
            _mean_absorption_coefficient * 10 (float)
        """
    def get_sector_transmit_delay(self) -> float: 
        """
        < relative first TX pulse, in s
        """
    def get_signal_bandwidth(self) -> float: 
        """
        < in Hz
        """
    def get_signal_length(self) -> float: 
        """
        < in s
        """
    def get_signal_waveform_identifier(self) -> int: ...
    def get_tilt_angle(self) -> int: 
        """
        < re TX array in 0.01°
        """
    def get_tilt_angle_in_degrees(self) -> float: 
        """
        Get the tilt angle in °

        Returns:
            _tilt_angle * 0.01 (float)
        """
    def get_transmit_sector_number(self) -> int: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_centre_frequency(self, arg0: float) -> None: 
        """
        < in Hz
        """
    def set_focus_range(self, arg0: int) -> None: 
        """
        < in 0.1m 0 = no focus applied
        """
    def set_mean_absorption_coefficient(self, arg0: int) -> None: 
        """
        < in 0.01 dB/km
        """
    def set_sector_transmit_delay(self, arg0: float) -> None: 
        """
        < relative first TX pulse, in s
        """
    def set_signal_bandwidth(self, arg0: float) -> None: 
        """
        < in Hz
        """
    def set_signal_length(self, arg0: float) -> None: 
        """
        < in s
        """
    def set_signal_waveform_identifier(self, arg0: int) -> None: ...
    def set_tilt_angle(self, arg0: int) -> None: 
        """
        < re TX array in 0.01°
        """
    def set_transmit_sector_number(self, arg0: int) -> None: ...
    __hash__ = None
    pass
class XYZDatagramBeam():
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    def __copy__(self) -> XYZDatagramBeam: ...
    def __deepcopy__(self, arg0: dict) -> XYZDatagramBeam: ...
    def __eq__(self, other: XYZDatagramBeam) -> bool: ...
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> XYZDatagramBeam: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_acrosstrack_distance(self) -> float: 
        """
        < distance (y) in meter
        """
    def get_alongtrack_distance(self) -> float: 
        """
        < distance (x) in meter
        """
    def get_backscatter(self) -> float: 
        """
        convert reflectivity to backscatter (_reflectivity * 0.1 dB)

        Returns:
            double
        """
    def get_backscatter_is_compensated(self) -> bool: 
        """
        This function evaluates the detection information flag. If the 4th bit
        is set to 1, the detection is compensated for beam incident angle. If
        the 4th bit is set to 0, the detection is not compensated for beam
        incident angle.

        Returns:
            true

        Returns:
            false
        """
    def get_beam_incidence_angle_adjustment(self) -> int: 
        """
        < (IBA) in 0.1 degree
        """
    def get_beam_incidence_angle_adjustment_in_degrees(self) -> float: 
        """
        Returns the beam incidence angle adjustment in degrees. (IBA * 0.1
        degree)

        Returns:
            double
        """
    def get_depth(self) -> float: 
        """
        < (Z) from transmit transducer in meter
        """
    def get_detection_info(self) -> int: 
        """
        < Flag that indicates the type and validity of detection
        """
    def get_detection_type(self) -> XYZDatagramBeam_t_DetectionType: 
        """
        This function evaluates the detection information flag. The first 3
        bits indicate the type of detection.

        Returns:
            t_DetectionType
        """
    def get_detection_window_length(self) -> int: 
        """
        < in samples
        """
    def get_quality_factor(self) -> int: 
        """
        < 0-254 Scaled standard deviation (sd) of the range detection <
        divided by the detected range (dr) (qf = 250*sd/sr)
        """
    def get_realtime_cleaning_information(self) -> int: 
        """
        < Flag that indicates if the beam was flagged by real < time cleaning
        (negative values indicate that this < beam is flagged out)
        """
    def get_reflectivity(self) -> int: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_acrosstrack_distance(self, arg0: float) -> None: 
        """
        < distance (y) in meter
        """
    def set_alongtrack_distance(self, arg0: float) -> None: 
        """
        < distance (x) in meter
        """
    def set_beam_incidence_angle_adjustment(self, arg0: float) -> None: 
        """
        < (IBA) in 0.1 degree
        """
    def set_depth(self, arg0: float) -> None: 
        """
        < (Z) from transmit transducer in meter
        """
    def set_detection_info(self, arg0: int) -> None: 
        """
        < Flag that indicates the type and validity of detection
        """
    def set_detection_window_length(self, arg0: int) -> None: 
        """
        < in samples
        """
    def set_quality_factor(self, arg0: int) -> None: 
        """
        < 0-254 Scaled standard deviation (sd) of the range detection <
        divided by the detected range (dr) (qf = 250*sd/sr)
        """
    def set_realtime_cleaning_information(self, arg0: int) -> None: 
        """
        < Flag that indicates if the beam was flagged by real < time cleaning
        (negative values indicate that this < beam is flagged out)
        """
    def set_reflectivity(self, arg0: int) -> None: ...
    __hash__ = None
    pass
class XYZDatagramBeam_t_DetectionType():
    """
    The detection_info flag (uint8_t) is used in XYZDatagramBeam and
    ExtraDectionsExtraDetections to indicate the type of detection.

    Members:

      AmplitudeDetect : < Valid, amplitude detection was used

      PhaseDetect : < Valid, phase detection was used

      InvalidNormalDetection : < Invalid: Normal detection

      Interpolated : < Invalid: Therefor interpolated or extrapolated

      Estimated : < Invalid: Therefor estimated

      Rejected : < Invalid: Therefor rejected

      NoDetection : < Invalid: No detection data is available for this beam

      Invalid : 
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    @typing.overload
    def __init__(self, str: str) -> None: 
        """
        Construct this enum type from string
        """
    @typing.overload
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    def str(self) -> str: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    AmplitudeDetect: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.AmplitudeDetect: 0>
    Estimated: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.Estimated: 130>
    Interpolated: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.Interpolated: 129>
    Invalid: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.Invalid: 133>
    InvalidNormalDetection: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.InvalidNormalDetection: 128>
    NoDetection: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.NoDetection: 132>
    PhaseDetect: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.PhaseDetect: 1>
    Rejected: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.Rejected: 131>
    __members__: dict # value = {'AmplitudeDetect': <XYZDatagramBeam_t_DetectionType.AmplitudeDetect: 0>, 'PhaseDetect': <XYZDatagramBeam_t_DetectionType.PhaseDetect: 1>, 'InvalidNormalDetection': <XYZDatagramBeam_t_DetectionType.InvalidNormalDetection: 128>, 'Interpolated': <XYZDatagramBeam_t_DetectionType.Interpolated: 129>, 'Estimated': <XYZDatagramBeam_t_DetectionType.Estimated: 130>, 'Rejected': <XYZDatagramBeam_t_DetectionType.Rejected: 131>, 'NoDetection': <XYZDatagramBeam_t_DetectionType.NoDetection: 132>, 'Invalid': <XYZDatagramBeam_t_DetectionType.Invalid: 133>}
    pass
AmplitudeDetect: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.AmplitudeDetect: 0>
Estimated: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.Estimated: 130>
Interpolated: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.Interpolated: 129>
Invalid: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.Invalid: 133>
InvalidNormalDetection: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.InvalidNormalDetection: 128>
NoDetection: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.NoDetection: 132>
PhaseDetect: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.PhaseDetect: 1>
Rejected: themachinethatgoesping.echosounders.em3000.datagrams.substructures.XYZDatagramBeam_t_DetectionType # value = <XYZDatagramBeam_t_DetectionType.Rejected: 131>
