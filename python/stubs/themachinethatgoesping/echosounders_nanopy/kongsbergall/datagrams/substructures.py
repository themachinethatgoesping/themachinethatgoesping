"""
Kongsberg KongsbergAll datagram substructures. These are substuctures of existing datagrams (repeated cycles, e.g. beams)
"""
from __future__ import annotations
import collections.abc
import enum
import numpy
import themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures
import typing
__all__: list[str] = ['AttitudeDatagramAttitude', 'ExtraDetectionsDetectionClasses', 'ExtraDetectionsExtraDetections', 'NetworkAttitudeVelocityDatagramAttitude', 'RawRangeAndAngleBeam', 'RawRangeAndAngleTransmitSector', 'SampleAmplitudesStructure_int16_t', 'SeabedImageDataBeam', 'WatercolumnDatagramBeam', 'WatercolumnDatagramTransmitSector', 'XYZDatagramBeam', 'XYZDatagramBeam_t_DetectionType', 'o_XYZDatagramBeam_t_DetectionType']
class AttitudeDatagramAttitude:
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> AttitudeDatagramAttitude:
        ...
    def __deepcopy__(self, arg: dict) -> AttitudeDatagramAttitude:
        ...
    def __eq__(self, other: AttitudeDatagramAttitude) -> bool:
        ...
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> AttitudeDatagramAttitude:
        """
        return a copy using the c++ default copy constructor
        """
    def get_heading(self) -> int:
        """
        < in 0.01°
        """
    def get_heading_in_degrees(self) -> float:
        """
        Returns the heading in degrees.
        
        Returns:
            _heading * 0.01f (float)
        """
    def get_heave(self) -> int:
        """
        < in cm
        """
    def get_heave_in_meters(self) -> float:
        """
        Returns the heave in meters.
        
        Returns:
            _heave * 0.01f (float)
        """
    def get_pitch(self) -> int:
        """
        < in 0.01°
        """
    def get_pitch_in_degrees(self) -> float:
        """
        Returns the pitch in degrees.
        
        Returns:
            _pitch * 0.01f (float)
        """
    def get_roll(self) -> int:
        """
        < in 0.01°
        """
    def get_roll_in_degrees(self) -> float:
        """
        Returns the roll in degrees.
        
        Returns:
            _roll * 0.01f (float)
        """
    def get_sensor_status(self) -> int:
        ...
    def get_time(self) -> float:
        """
        < in_milliseconds_since_record_start
        """
    def get_time_in_seconds(self) -> float:
        """
        Returns the time in seconds since record start.
        
        Returns:
            _time * 0.001f (float)
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_heading(self, arg: int) -> None:
        """
        < in 0.01°
        """
    def set_heave(self, arg: int) -> None:
        """
        < in cm
        """
    def set_pitch(self, arg: int) -> None:
        """
        < in 0.01°
        """
    def set_roll(self, arg: int) -> None:
        """
        < in 0.01°
        """
    def set_sensor_status(self, arg: int) -> None:
        ...
    def set_time(self, arg: int) -> None:
        """
        < in_milliseconds_since_record_start
        """
class ExtraDetectionsDetectionClasses:
    """
    Extra Detections Detection Classes
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> ExtraDetectionsDetectionClasses:
        ...
    def __deepcopy__(self, arg: dict) -> ExtraDetectionsDetectionClasses:
        ...
    def __eq__(self, other: ExtraDetectionsDetectionClasses) -> bool:
        ...
    def __init__(self) -> None:
        ...
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_alarm_flag_1(self, arg: int) -> None:
        """
        < 0: (no alarm) 1:Number of extra detections are above Alarm
        threshold.
        """
    def set_alarm_threshold(self, arg: int) -> None:
        """
        < number of extra det. required (1-99 0=off)
        """
    def set_bs_threshold(self, arg: int) -> None:
        """
        < dB (-10 - 60)
        """
    def set_number_of_extra_detections(self, arg: int) -> None:
        """
        <
        """
    def set_qf_threshold_100(self, arg: int) -> None:
        """
        < 100 * QF threshold (1-100)
        """
    def set_show_class(self, arg: bool) -> None:
        """
        < 0-1
        """
    def set_snr_threshold(self, arg: int) -> None:
        """
        < 5-15
        """
    def set_start_depth(self, arg: int) -> None:
        """
        < % of depth (0-300)
        """
    def set_stop_depth(self, arg: int) -> None:
        """
        < % of depth (1-300)
        """
class ExtraDetectionsExtraDetections:
    """
    Extra Detections in the extra detections datagram
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> ExtraDetectionsExtraDetections:
        ...
    def __deepcopy__(self, arg: dict) -> ExtraDetectionsExtraDetections:
        ...
    def __eq__(self, other: ExtraDetectionsExtraDetections) -> bool:
        ...
    def __init__(self) -> None:
        ...
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
    def get_beam_crosstrack_angle(self) -> float:
        """
        < deg. re array
        """
    def get_beam_incidence_angle_adjustment(self) -> int:
        """
        < IBA in 0.1°
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
    def get_detection_info(self) -> int:
        ...
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
    def get_detection_type(self) -> o_XYZDatagramBeam_t_DetectionType:
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
    def get_spare(self) -> int:
        ...
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
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_across(self, arg: float) -> None:
        """
        < y in m
        """
    def set_along(self, arg: float) -> None:
        """
        < x in m
        """
    def set_applied_pointing_angle_correction(self, arg: float) -> None:
        """
        <
        """
    def set_applied_two_way_travel_time_corrections(self, arg: float) -> None:
        """
        < seconds, f.ex. Doppler correction
        """
    def set_backscatter(self, arg: int) -> None:
        """
        < 0.1 dB
        """
    def set_beam_angle_across(self, arg: float) -> None:
        """
        < re vertical °
        """
    def set_beam_crosstrack_angle(self, arg: float) -> None:
        """
        < deg. re array
        """
    def set_beam_incidence_angle_adjustment(self, arg: int) -> None:
        """
        < IBA in 0.1°
        """
    def set_confidence_level(self, arg: int) -> None:
        """
        <
        """
    def set_delta_latitude(self, arg: float) -> None:
        """
        < °
        """
    def set_delta_longitude(self, arg: float) -> None:
        """
        < °
        """
    def set_depth(self, arg: float) -> None:
        """
        < z in m
        """
    def set_detected_range(self, arg: int) -> None:
        """
        < in (WCsr) samples
        """
    def set_detection_class_number(self, arg: int) -> None:
        """
        <
        """
    def set_detection_info(self, arg: int) -> None:
        ...
    def set_detection_window_length(self, arg: int) -> None:
        """
        <
        """
    def set_number_of_raw_amplitude_samples(self, arg: int) -> None:
        """
        < NS
        """
    def set_qf_10(self, arg: int) -> None:
        """
        < Ifremer Quality factor * 10
        """
    def set_quality_factor_old(self, arg: int) -> None:
        """
        <
        """
    def set_range_factor(self, arg: int) -> None:
        """
        < in %
        """
    def set_real_time_cleaning_info(self, arg: int) -> None:
        """
        <
        """
    def set_spare(self, arg: int) -> None:
        ...
    def set_two_way_travel_time(self, arg: float) -> None:
        """
        < s
        """
    def set_tx_sector_number(self, arg: int) -> None:
        """
        < or TX array index
        """
    def set_water_column_beam_number(self, arg: int) -> None:
        """
        <
        """
class NetworkAttitudeVelocityDatagramAttitude:
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> NetworkAttitudeVelocityDatagramAttitude:
        ...
    def __deepcopy__(self, arg: dict) -> NetworkAttitudeVelocityDatagramAttitude:
        ...
    def __eq__(self, other: NetworkAttitudeVelocityDatagramAttitude) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> NetworkAttitudeVelocityDatagramAttitude:
        """
        return a copy using the c++ default copy constructor
        """
    def get_heading(self) -> int:
        """
        < in 0.01°
        """
    def get_heading_in_degrees(self) -> float:
        """
        Returns the heading in degrees.
        
        Returns:
            _heading * 0.01f (float)
        """
    def get_heave(self) -> int:
        """
        < in cm
        """
    def get_heave_in_meters(self) -> float:
        """
        Returns the heave in meters.
        
        Returns:
            _heave * 0.01f (float)
        """
    def get_input_datagram(self) -> bytes:
        """
        < as received from the network
        """
    def get_number_of_bytes_in_input_datagram(self) -> int:
        """
        < Nx
        """
    def get_pitch(self) -> int:
        """
        < in 0.01°
        """
    def get_pitch_in_degrees(self) -> float:
        """
        Returns the pitch in degrees.
        
        Returns:
            _pitch * 0.01f (float)
        """
    def get_roll(self) -> int:
        """
        < in 0.01°
        """
    def get_roll_in_degrees(self) -> float:
        """
        Returns the roll in degrees.
        
        Returns:
            _roll * 0.01f (float)
        """
    def get_time(self) -> float:
        """
        < in_milliseconds_since_record_start
        """
    def get_time_in_seconds(self) -> float:
        """
        Returns the time in seconds since record start.
        
        Returns:
            _time * 0.001f (float)
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_heading(self, arg: int) -> None:
        """
        < in 0.01°
        """
    def set_heave(self, arg: int) -> None:
        """
        < in cm
        """
    def set_input_datagram(self, arg: str) -> None:
        """
        < as received from the network
        """
    def set_number_of_bytes_in_input_datagram(self, arg: int) -> None:
        """
        < Nx
        """
    def set_pitch(self, arg: int) -> None:
        """
        < in 0.01°
        """
    def set_roll(self, arg: int) -> None:
        """
        < in 0.01°
        """
    def set_time(self, arg: int) -> None:
        """
        < in_milliseconds_since_record_start
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class RawRangeAndAngleBeam:
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> RawRangeAndAngleBeam:
        ...
    def __deepcopy__(self, arg: dict) -> RawRangeAndAngleBeam:
        ...
    def __eq__(self, other: RawRangeAndAngleBeam) -> bool:
        ...
    def __init__(self) -> None:
        ...
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
    def get_beam_crosstrack_angle(self) -> int:
        ...
    def get_beam_crosstrack_angle_in_degrees(self) -> float:
        """
        Get the beam crosstrack angle in °
        
        Returns:
            _beam_crosstrack_angle * 0.01 (float)
        """
    def get_d_corr(self) -> int:
        ...
    def get_detection_info(self) -> int:
        ...
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
    def get_detection_type(self) -> o_XYZDatagramBeam_t_DetectionType:
        """
        This function evaluates the detection information flag. The first 3
        bits indicate the type of detection.
        
        Returns:
            t_DetectionType
        """
    def get_detection_window_length_in_samples(self) -> int:
        ...
    def get_quality_factor(self) -> int:
        ...
    def get_realtime_cleaning_info(self) -> int:
        ...
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
    def get_spare(self) -> int:
        ...
    def get_transmit_sector_number(self) -> int:
        """
        M relative RX array in 0.01°
        """
    def get_two_way_travel_time(self) -> float:
        """
        < in s
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_beam_crosstrack_angle(self, arg: int) -> None:
        ...
    def set_d_corr(self, arg: int) -> None:
        ...
    def set_detection_info(self, arg: int) -> None:
        ...
    def set_detection_window_length_in_samples(self, arg: int) -> None:
        ...
    def set_quality_factor(self, arg: int) -> None:
        ...
    def set_realtime_cleaning_info(self, arg: int) -> None:
        ...
    def set_reflectivity(self, arg: int) -> None:
        """
        < in 0.1 dB resolution
        """
    def set_spare(self, arg: int) -> None:
        ...
    def set_transmit_sector_number(self, arg: int) -> None:
        """
        M relative RX array in 0.01°
        """
    def set_two_way_travel_time(self, arg: float) -> None:
        """
        < in s
        """
class RawRangeAndAngleTransmitSector:
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> RawRangeAndAngleTransmitSector:
        ...
    def __deepcopy__(self, arg: dict) -> RawRangeAndAngleTransmitSector:
        ...
    def __eq__(self, other: RawRangeAndAngleTransmitSector) -> bool:
        ...
    def __init__(self) -> None:
        ...
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
    def get_center_frequency(self) -> float:
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
    def get_signal_waveform_identifier(self) -> int:
        ...
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
    def get_transmit_sector_number(self) -> int:
        ...
    def get_tx_signal_type(self) -> themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.t_TxSignalType:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_center_frequency(self, arg: float) -> None:
        """
        < in Hz
        """
    def set_focus_range(self, arg: int) -> None:
        """
        < in 0.1m 0 = no focus applied
        """
    def set_mean_absorption_coefficient(self, arg: int) -> None:
        """
        < in 0.01 dB/km
        """
    def set_sector_transmit_delay(self, arg: float) -> None:
        """
        < relative first TX pulse, in s
        """
    def set_signal_bandwidth(self, arg: float) -> None:
        """
        < in Hz
        """
    def set_signal_length(self, arg: float) -> None:
        """
        < in s
        """
    def set_signal_waveform_identifier(self, arg: int) -> None:
        ...
    def set_tilt_angle(self, arg: int) -> None:
        """
        < re TX array in 0.01°
        """
    def set_transmit_sector_number(self, arg: int) -> None:
        ...
class SampleAmplitudesStructure_int16_t:
    """
    A structure to store the sample amplitudes of multiple beams in a
    single array. Each beam may have a different number of samples. One of
    the main reasons behind this structure is read/write performance and
    the possibility to use xsimd on the data (stored as xtensor).
    
    Template parameter ``t_sample``:
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleAmplitudesStructure_int16_t:
        ...
    def __deepcopy__(self, arg: dict) -> SampleAmplitudesStructure_int16_t:
        ...
    def __eq__(self, other: SampleAmplitudesStructure_int16_t) -> bool:
        ...
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SampleAmplitudesStructure_int16_t:
        """
        return a copy using the c++ default copy constructor
        """
    def get_beam(self, arg: int) -> numpy.ndarray[dtype=int16, ..., order='C']:
        """
        return a view of the sample amplitudes of a single beam
        
        Parameter ``beam_index``:
            $Returns:
        
        xt::xtensor<t_sample, 1>
        """
    def get_beam_in_db(self, arg: int) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        return a xtensor of the sample amplitudes of a single beam converted
        to db
        
        Parameter ``mp_cores``:
            number of cores to use for parallelization (default 1)
        
        Parameter ``beam_index``:
            $Returns:
        
        xt::xtensor<float, 1>
        """
    def get_sample_amplitudes(self) -> numpy.ndarray[dtype=int16, ..., order='C']:
        """
        < in db steps
        """
    def get_sample_amplitudes_in_db(self) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        Convert the sample amplitudes to db using _db_step_size.
        
        Returns:
            xt::xtensor<float, 1>
        """
    def get_sample_amplitudes_per_beam(self, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get all sample amplitude values of all beams in a single xtensor
        
        Returns:
            xt::xtensor<float, 1>
        """
    def get_sample_amplitudes_per_beam_in_db(self, mp_cores: int = 1) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        get all sample amplitude valuesof all beams in a single xtensor in db
        Convert the sample amplitudes to db using _db_step_size.
        
        Parameter ``mp_cores``:
            number of cores to use for parallelization (default 1)
        
        Returns:
            xt::xtensor<float, 1>
        """
    def get_samples_per_beam(self) -> list[int]:
        ...
    def get_start_index_per_beam(self) -> list[int]:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_sample_amplitudes(self, arg: numpy.ndarray[dtype=int16, ..., order='C']) -> None:
        """
        < in db steps
        """
    def set_samples_per_beam(self, arg: collections.abc.Sequence[int]) -> None:
        ...
    def set_start_index_per_beam(self, arg: collections.abc.Sequence[int]) -> None:
        ...
    def size(self) -> int:
        """
        size(self, beam_index: int) -> int
        """
class SeabedImageDataBeam:
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SeabedImageDataBeam:
        ...
    def __deepcopy__(self, arg: dict) -> SeabedImageDataBeam:
        ...
    def __eq__(self, other: SeabedImageDataBeam) -> bool:
        ...
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SeabedImageDataBeam:
        """
        return a copy using the c++ default copy constructor
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
    def get_centre_sample_number(self) -> int:
        ...
    def get_detection_info(self) -> int:
        ...
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
    def get_detection_type(self) -> o_XYZDatagramBeam_t_DetectionType:
        """
        This function evaluates the detection information flag. The first 3
        bits indicate the type of detection.
        
        Returns:
            t_DetectionType
        """
    def get_number_of_samples(self) -> int:
        """
        < per beam
        """
    def get_sorting_direction(self) -> int:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_centre_sample_number(self, arg: int) -> None:
        ...
    def set_detection_info(self, arg: int) -> None:
        ...
    def set_number_of_samples(self, arg: int) -> None:
        """
        < per beam
        """
    def set_sorting_direction(self, arg: int) -> None:
        ...
class WatercolumnDatagramBeam:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> WatercolumnDatagramBeam:
        ...
    def __deepcopy__(self, arg: dict) -> WatercolumnDatagramBeam:
        ...
    def __eq__(self, other: WatercolumnDatagramBeam) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> WatercolumnDatagramBeam:
        """
        return a copy using the c++ default copy constructor
        """
    def get_beam_crosstrack_angle(self) -> int:
        """
        < re vertical in 0.01 steps°
        """
    def get_beam_crosstrack_angle_in_degrees(self) -> float:
        """
        get the tilt angle in °
        
        Returns:
            _beam_crosstrack_angle * 0.1° (float)
        """
    def get_beam_number(self) -> int:
        """
        < redundant info, max 255 even if more beams exist
        """
    def get_detected_range_in_samples(self) -> int:
        ...
    def get_number_of_samples(self) -> int:
        ...
    def get_samples(self) -> numpy.ndarray[dtype=int8, ..., order='C']:
        ...
    def get_samples_are_skipped(self) -> bool:
        """
        < in 0.5 dB steps
        """
    def get_samples_in_db(self, arg: float) -> numpy.ndarray[dtype=float32, ..., order='C']:
        ...
    def get_start_range_sample_number(self) -> int:
        ...
    def get_transmit_sector_number(self) -> int:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def samples(self) -> numpy.ndarray[dtype=int8, ..., order='C']:
        ...
    def set_beam_crosstrack_angle(self, arg: int) -> None:
        """
        < re vertical in 0.01 steps°
        """
    def set_beam_number(self, arg: int) -> None:
        """
        < redundant info, max 255 even if more beams exist
        """
    def set_detected_range_in_samples(self, arg: int) -> None:
        ...
    def set_number_of_samples(self, arg: int) -> None:
        ...
    def set_samples(self, arg: numpy.ndarray[dtype=int8, ..., order='C']) -> None:
        ...
    def set_start_range_sample_number(self, arg: int) -> None:
        ...
    def set_transmit_sector_number(self, arg: int) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class WatercolumnDatagramTransmitSector:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> WatercolumnDatagramTransmitSector:
        ...
    def __deepcopy__(self, arg: dict) -> WatercolumnDatagramTransmitSector:
        ...
    def __eq__(self, other: WatercolumnDatagramTransmitSector) -> bool:
        ...
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> WatercolumnDatagramTransmitSector:
        """
        return a copy using the c++ default copy constructor
        """
    def get_center_frequency(self) -> int:
        """
        < in 10 Hz
        """
    def get_center_frequency_in_hz(self) -> float:
        """
        get the center frequency in Hz
        
        Returns:
            _center_frequency * 10 Hz (float)
        """
    def get_spare(self) -> int:
        ...
    def get_tilt_angle(self) -> int:
        """
        < in 0.01°
        """
    def get_tilt_angle_in_degrees(self) -> float:
        """
        get the tilt angle in °
        
        Returns:
            _tilt_angle * 0.01° (float)
        """
    def get_transmit_sector_number(self) -> int:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_center_frequency(self, arg: int) -> None:
        """
        < in 10 Hz
        """
    def set_spare(self, arg: int) -> None:
        ...
    def set_tilt_angle(self, arg: int) -> None:
        """
        < in 0.01°
        """
    def set_transmit_sector_number(self, arg: int) -> None:
        ...
class XYZDatagramBeam:
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> XYZDatagramBeam:
        ...
    def __deepcopy__(self, arg: dict) -> XYZDatagramBeam:
        ...
    def __eq__(self, other: XYZDatagramBeam) -> bool:
        ...
    def __init__(self) -> None:
        ...
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
    def get_detection_type(self) -> o_XYZDatagramBeam_t_DetectionType:
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
    def get_reflectivity(self) -> int:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_acrosstrack_distance(self, arg: float) -> None:
        """
        < distance (y) in meter
        """
    def set_alongtrack_distance(self, arg: float) -> None:
        """
        < distance (x) in meter
        """
    def set_beam_incidence_angle_adjustment(self, arg: float) -> None:
        """
        < (IBA) in 0.1 degree
        """
    def set_depth(self, arg: float) -> None:
        """
        < (Z) from transmit transducer in meter
        """
    def set_detection_info(self, arg: int) -> None:
        """
        < Flag that indicates the type and validity of detection
        """
    def set_detection_window_length(self, arg: int) -> None:
        """
        < in samples
        """
    def set_quality_factor(self, arg: int) -> None:
        """
        < 0-254 Scaled standard deviation (sd) of the range detection <
        divided by the detected range (dr) (qf = 250*sd/sr)
        """
    def set_realtime_cleaning_information(self, arg: int) -> None:
        """
        < Flag that indicates if the beam was flagged by real < time cleaning
        (negative values indicate that this < beam is flagged out)
        """
    def set_reflectivity(self, arg: int) -> None:
        ...
class XYZDatagramBeam_t_DetectionType(enum.Enum):
    """
    The detection_info flag (uint8_t) is used in XYZDatagramBeam and
    ExtraDectionsExtraDetections to indicate the type of detection.
    """
    AmplitudeDetect: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = XYZDatagramBeam_t_DetectionType.AmplitudeDetect
    Estimated: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = XYZDatagramBeam_t_DetectionType.Estimated
    Interpolated: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = XYZDatagramBeam_t_DetectionType.Interpolated
    Invalid: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = XYZDatagramBeam_t_DetectionType.Invalid
    InvalidNormalDetection: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = XYZDatagramBeam_t_DetectionType.InvalidNormalDetection
    NoDetection: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = XYZDatagramBeam_t_DetectionType.NoDetection
    PhaseDetect: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = XYZDatagramBeam_t_DetectionType.PhaseDetect
    Rejected: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = XYZDatagramBeam_t_DetectionType.Rejected
class o_XYZDatagramBeam_t_DetectionType:
    """
    Helper class to convert between strings and enum values of type 't_DetectionType'
    """
    __default_value__: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = XYZDatagramBeam_t_DetectionType.AmplitudeDetect
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> o_XYZDatagramBeam_t_DetectionType:
        ...
    def __deepcopy__(self, arg: dict) -> o_XYZDatagramBeam_t_DetectionType:
        ...
    def __eq__(self, arg: o_XYZDatagramBeam_t_DetectionType) -> bool:
        """
        __eq__(self, arg: themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.substructures.XYZDatagramBeam_t_DetectionType, /) -> bool
        __eq__(self, arg: int, /) -> bool
        __eq__(self, arg: str, /) -> bool
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, value: XYZDatagramBeam_t_DetectionType = ...) -> None:
        """
        __init__(self, value: str) -> None
        __init__(self, value: int) -> None
        
        Overloaded function.
        
        1. ``__init__(self, value: themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.substructures.XYZDatagramBeam_t_DetectionType = XYZDatagramBeam_t_DetectionType.AmplitudeDetect) -> None``
        
        Construct from enum value
        
        2. ``__init__(self, value: str) -> None``
        
        Construct from string
        
        3. ``__init__(self, value: int) -> None``
        
        Construct from string
        """
    def __repr__(self) -> str:
        """
        __repr__(self) -> None
        
        Overloaded function.
        
        1. ``__repr__(self) -> str``
        
        Return object information as string
        
        2. ``__repr__(self) -> None``
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        __str__(self) -> str
        
        Overloaded function.
        
        1. ``__str__(self) -> str``
        
        
        2. ``__str__(self) -> str``
        
        Return object information as string
        """
    def copy(self) -> o_XYZDatagramBeam_t_DetectionType:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def value(self) -> XYZDatagramBeam_t_DetectionType:
        """
        enum value
        """
    @value.setter
    def value(self, arg: XYZDatagramBeam_t_DetectionType) -> None:
        """
        enum value
        """
