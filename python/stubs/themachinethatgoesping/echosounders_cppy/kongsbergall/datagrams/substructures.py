"""
Kongsberg KongsbergAll datagram substructures. These are substuctures of existing datagrams (repeated cycles, e.g. beams)
"""
from __future__ import annotations
import numpy
import themachinethatgoesping.algorithms.signalprocessing.datastructures
import typing
__all__ = ['AmplitudeDetect', 'AttitudeDatagramAttitude', 'Estimated', 'ExtraDetectionsDetectionClasses', 'ExtraDetectionsExtraDetections', 'Interpolated', 'Invalid', 'InvalidNormalDetection', 'NetworkAttitudeVelocityDatagramAttitude', 'NoDetection', 'PhaseDetect', 'RawRangeAndAngleBeam', 'RawRangeAndAngleTransmitSector', 'Rejected', 'SampleAmplitudesStructure_int16_t', 'SeabedImageDataBeam', 'WatercolumnDatagramBeam', 'WatercolumnDatagramTransmitSector', 'XYZDatagramBeam', 'XYZDatagramBeam_t_DetectionType']
class AttitudeDatagramAttitude:
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> AttitudeDatagramAttitude:
        ...
    def __deepcopy__(self, arg0: dict) -> AttitudeDatagramAttitude:
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def set_heading(self, arg0: int) -> None:
        """
        < in 0.01°
        """
    def set_heave(self, arg0: int) -> None:
        """
        < in cm
        """
    def set_pitch(self, arg0: int) -> None:
        """
        < in 0.01°
        """
    def set_roll(self, arg0: int) -> None:
        """
        < in 0.01°
        """
    def set_sensor_status(self, arg0: int) -> None:
        ...
    def set_time(self, arg0: int) -> None:
        """
        < in_milliseconds_since_record_start
        """
class ExtraDetectionsDetectionClasses:
    """
    Extra Detections Detection Classes
    """
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> ExtraDetectionsDetectionClasses:
        ...
    def __deepcopy__(self, arg0: dict) -> ExtraDetectionsDetectionClasses:
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
class ExtraDetectionsExtraDetections:
    """
    Extra Detections in the extra detections datagram
    """
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> ExtraDetectionsExtraDetections:
        ...
    def __deepcopy__(self, arg0: dict) -> ExtraDetectionsExtraDetections:
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
    def set_beam_crosstrack_angle(self, arg0: float) -> None:
        """
        < deg. re array
        """
    def set_beam_incidence_angle_adjustment(self, arg0: int) -> None:
        """
        < IBA in 0.1°
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
    def set_detection_info(self, arg0: int) -> None:
        ...
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
    def set_spare(self, arg0: int) -> None:
        ...
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
class NetworkAttitudeVelocityDatagramAttitude:
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NetworkAttitudeVelocityDatagramAttitude:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> NetworkAttitudeVelocityDatagramAttitude:
        ...
    def __deepcopy__(self, arg0: dict) -> NetworkAttitudeVelocityDatagramAttitude:
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
    def __setstate__(self, arg0: bytes) -> None:
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def set_heading(self, arg0: int) -> None:
        """
        < in 0.01°
        """
    def set_heave(self, arg0: int) -> None:
        """
        < in cm
        """
    def set_input_datagram(self, arg0: str) -> None:
        """
        < as received from the network
        """
    def set_number_of_bytes_in_input_datagram(self, arg0: int) -> None:
        """
        < Nx
        """
    def set_pitch(self, arg0: int) -> None:
        """
        < in 0.01°
        """
    def set_roll(self, arg0: int) -> None:
        """
        < in 0.01°
        """
    def set_time(self, arg0: int) -> None:
        """
        < in_milliseconds_since_record_start
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
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
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> RawRangeAndAngleBeam:
        ...
    def __deepcopy__(self, arg0: dict) -> RawRangeAndAngleBeam:
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
    def get_detection_type(self) -> XYZDatagramBeam_t_DetectionType:
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def set_beam_crosstrack_angle(self, arg0: int) -> None:
        ...
    def set_d_corr(self, arg0: int) -> None:
        ...
    def set_detection_info(self, arg0: int) -> None:
        ...
    def set_detection_window_length_in_samples(self, arg0: int) -> None:
        ...
    def set_quality_factor(self, arg0: int) -> None:
        ...
    def set_realtime_cleaning_info(self, arg0: int) -> None:
        ...
    def set_reflectivity(self, arg0: int) -> None:
        """
        < in 0.1 dB resolution
        """
    def set_spare(self, arg0: int) -> None:
        ...
    def set_transmit_sector_number(self, arg0: int) -> None:
        """
        M relative RX array in 0.01°
        """
    def set_two_way_travel_time(self, arg0: float) -> None:
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
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> RawRangeAndAngleTransmitSector:
        ...
    def __deepcopy__(self, arg0: dict) -> RawRangeAndAngleTransmitSector:
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
    def get_tx_signal_type(self) -> themachinethatgoesping.algorithms.signalprocessing.datastructures.t_TxSignalType:
        ...
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
    def set_signal_waveform_identifier(self, arg0: int) -> None:
        ...
    def set_tilt_angle(self, arg0: int) -> None:
        """
        < re TX array in 0.01°
        """
    def set_transmit_sector_number(self, arg0: int) -> None:
        ...
class SampleAmplitudesStructure_int16_t:
    """
    A structure to store the sample amplitudes of multiple beams in a
    single array. Each beam may have a different number of samples. One of
    the main reasons behind this structure is read/write performance and
    the possibility to use xsimd on the data (stored as xtensor).
    
    Template parameter ``t_sample``:
    """
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> SampleAmplitudesStructure_int16_t:
        ...
    def __deepcopy__(self, arg0: dict) -> SampleAmplitudesStructure_int16_t:
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
    def get_beam(self, arg0: int) -> numpy.ndarray[numpy.int16]:
        """
        return a view of the sample amplitudes of a single beam
        
        Parameter ``beam_index``:
            $Returns:
        
        xt::xtensor<t_sample, 1>
        """
    def get_beam_in_db(self, arg0: int) -> numpy.ndarray[numpy.float32]:
        """
        return a xtensor of the sample amplitudes of a single beam converted
        to db
        
        Parameter ``beam_index``:
            $Returns:
        
        xt::xtensor<float, 1>
        """
    def get_sample_amplitudes(self) -> numpy.ndarray[numpy.int16]:
        """
        < in db steps
        """
    def get_sample_amplitudes_in_db(self) -> numpy.ndarray[numpy.float32]:
        """
        Convert the sample amplitudes to db using _db_step_size.
        
        Returns:
            xt::xtensor<float, 1>
        """
    def get_samples_per_beam(self) -> list[int]:
        ...
    def get_start_index_per_beam(self) -> list[int]:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def set_sample_amplitudes(self, arg0: numpy.ndarray[numpy.int16]) -> None:
        """
        < in db steps
        """
    def set_samples_per_beam(self, arg0: list[int]) -> None:
        ...
    def set_start_index_per_beam(self, arg0: list[int]) -> None:
        ...
    @typing.overload
    def size(self) -> int:
        ...
    @typing.overload
    def size(self, beam_index: int) -> int:
        ...
class SeabedImageDataBeam:
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> SeabedImageDataBeam:
        ...
    def __deepcopy__(self, arg0: dict) -> SeabedImageDataBeam:
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
    def get_detection_type(self) -> XYZDatagramBeam_t_DetectionType:
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def set_centre_sample_number(self, arg0: int) -> None:
        ...
    def set_detection_info(self, arg0: int) -> None:
        ...
    def set_number_of_samples(self, arg0: int) -> None:
        """
        < per beam
        """
    def set_sorting_direction(self, arg0: int) -> None:
        ...
class WatercolumnDatagramBeam:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> WatercolumnDatagramBeam:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> WatercolumnDatagramBeam:
        ...
    def __deepcopy__(self, arg0: dict) -> WatercolumnDatagramBeam:
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
    def __setstate__(self, arg0: bytes) -> None:
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
    def get_samples(self) -> numpy.ndarray[numpy.int8]:
        ...
    def get_samples_are_skipped(self) -> bool:
        """
        < in 0.5 dB steps
        """
    def get_samples_in_db(self, arg0: float) -> numpy.ndarray[numpy.float32]:
        ...
    def get_start_range_sample_number(self) -> int:
        ...
    def get_transmit_sector_number(self) -> int:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def samples(self) -> numpy.ndarray[numpy.int8]:
        ...
    def set_beam_crosstrack_angle(self, arg0: int) -> None:
        """
        < re vertical in 0.01 steps°
        """
    def set_beam_number(self, arg0: int) -> None:
        """
        < redundant info, max 255 even if more beams exist
        """
    def set_detected_range_in_samples(self, arg0: int) -> None:
        ...
    def set_number_of_samples(self, arg0: int) -> None:
        ...
    def set_samples(self, arg0: numpy.ndarray[numpy.int8]) -> None:
        ...
    def set_start_range_sample_number(self, arg0: int) -> None:
        ...
    def set_transmit_sector_number(self, arg0: int) -> None:
        ...
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class WatercolumnDatagramTransmitSector:
    """
    """
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> WatercolumnDatagramTransmitSector:
        ...
    def __deepcopy__(self, arg0: dict) -> WatercolumnDatagramTransmitSector:
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def set_center_frequency(self, arg0: int) -> None:
        """
        < in 10 Hz
        """
    def set_spare(self, arg0: int) -> None:
        ...
    def set_tilt_angle(self, arg0: int) -> None:
        """
        < in 0.01°
        """
    def set_transmit_sector_number(self, arg0: int) -> None:
        ...
class XYZDatagramBeam:
    """
    The beam data are given re the transmit transducer or sonar head depth
    and the horizontal location (x,y) of the active positioning system's
    reference point. Heave, roll, pitch, sound speed at the transducer
    depth and ray bending through the water column have been applied.
    """
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> XYZDatagramBeam:
        ...
    def __deepcopy__(self, arg0: dict) -> XYZDatagramBeam:
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
    def get_reflectivity(self) -> int:
        ...
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
    def set_reflectivity(self, arg0: int) -> None:
        ...
class XYZDatagramBeam_t_DetectionType:
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
    AmplitudeDetect: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = <XYZDatagramBeam_t_DetectionType.AmplitudeDetect: 0>
    Estimated: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = <XYZDatagramBeam_t_DetectionType.Estimated: 130>
    Interpolated: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = <XYZDatagramBeam_t_DetectionType.Interpolated: 129>
    Invalid: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = <XYZDatagramBeam_t_DetectionType.Invalid: 133>
    InvalidNormalDetection: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = <XYZDatagramBeam_t_DetectionType.InvalidNormalDetection: 128>
    NoDetection: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = <XYZDatagramBeam_t_DetectionType.NoDetection: 132>
    PhaseDetect: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = <XYZDatagramBeam_t_DetectionType.PhaseDetect: 1>
    Rejected: typing.ClassVar[XYZDatagramBeam_t_DetectionType]  # value = <XYZDatagramBeam_t_DetectionType.Rejected: 131>
    __members__: typing.ClassVar[dict[str, XYZDatagramBeam_t_DetectionType]]  # value = {'AmplitudeDetect': <XYZDatagramBeam_t_DetectionType.AmplitudeDetect: 0>, 'PhaseDetect': <XYZDatagramBeam_t_DetectionType.PhaseDetect: 1>, 'InvalidNormalDetection': <XYZDatagramBeam_t_DetectionType.InvalidNormalDetection: 128>, 'Interpolated': <XYZDatagramBeam_t_DetectionType.Interpolated: 129>, 'Estimated': <XYZDatagramBeam_t_DetectionType.Estimated: 130>, 'Rejected': <XYZDatagramBeam_t_DetectionType.Rejected: 131>, 'NoDetection': <XYZDatagramBeam_t_DetectionType.NoDetection: 132>, 'Invalid': <XYZDatagramBeam_t_DetectionType.Invalid: 133>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    @typing.overload
    def __init__(self, value: int) -> None:
        ...
    @typing.overload
    def __init__(self, str: str) -> None:
        """
        Construct this enum type from string
        """
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def str(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
AmplitudeDetect: XYZDatagramBeam_t_DetectionType  # value = <XYZDatagramBeam_t_DetectionType.AmplitudeDetect: 0>
Estimated: XYZDatagramBeam_t_DetectionType  # value = <XYZDatagramBeam_t_DetectionType.Estimated: 130>
Interpolated: XYZDatagramBeam_t_DetectionType  # value = <XYZDatagramBeam_t_DetectionType.Interpolated: 129>
Invalid: XYZDatagramBeam_t_DetectionType  # value = <XYZDatagramBeam_t_DetectionType.Invalid: 133>
InvalidNormalDetection: XYZDatagramBeam_t_DetectionType  # value = <XYZDatagramBeam_t_DetectionType.InvalidNormalDetection: 128>
NoDetection: XYZDatagramBeam_t_DetectionType  # value = <XYZDatagramBeam_t_DetectionType.NoDetection: 132>
PhaseDetect: XYZDatagramBeam_t_DetectionType  # value = <XYZDatagramBeam_t_DetectionType.PhaseDetect: 1>
Rejected: XYZDatagramBeam_t_DetectionType  # value = <XYZDatagramBeam_t_DetectionType.Rejected: 131>
