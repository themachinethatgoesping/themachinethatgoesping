import typing
from collections.abc import Sequence
import enum
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

from . import substructures as substructures
import themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures
import themachinethatgoesping.echosounders_nanopy
import themachinethatgoesping.echosounders_nanopy.kongsbergall
import themachinethatgoesping.navigation_nanopy.datastructures


class KongsbergAllDatagram:
    def __init__(self) -> None: ...

    def get_bytes(self) -> int:
        """
        number of bytes in the datagram (not including the _bytes field
        itself)
        """

    def set_bytes(self, arg: int, /) -> None:
        """
        number of bytes in the datagram (not including the _bytes field
        itself)
        """

    def get_stx(self) -> int:
        """(start identifier)"""

    def set_stx(self, arg: int, /) -> None:
        """(start identifier)"""

    def get_datagram_identifier(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier:
        """KongsbergAll datagram identifier"""

    def set_datagram_identifier(self, arg: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, /) -> None:
        """KongsbergAll datagram identifier"""

    def get_model_number(self) -> int:
        """KongsbergAll model number (example: EM 3002 = 3002)"""

    def set_model_number(self, arg: int, /) -> None:
        """KongsbergAll model number (example: EM 3002 = 3002)"""

    def get_date(self) -> int:
        """year*1000 + month*100 + day(Example:Jun 27, 2020 = 20200627)"""

    def set_date(self, arg: int, /) -> None:
        """year*1000 + month*100 + day(Example:Jun 27, 2020 = 20200627)"""

    def get_time_since_midnight(self) -> int: ...

    def set_time_since_midnight(self, arg: int, /) -> None: ...

    def get_timestamp(self) -> float:
        """
        convert the date and time_since_midnight field to a unix timestamp

        Returns:
            unixtime as double
        """

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

    def get_model_number_as_string(self) -> str:
        """
        Get the model number as string EM+model_number, except 2045 which is
        EM2040C

        Returns:
            std::string
        """

    def __eq__(self, other: KongsbergAllDatagram) -> bool: ...

    def copy(self) -> KongsbergAllDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> KongsbergAllDatagram:
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

class KongsbergAllUnknown(KongsbergAllDatagram):
    def __init__(self) -> None: ...

    def get_raw_content(self) -> str: ...

    def set_raw_content(self, arg: str, /) -> None: ...

    def get_etx(self) -> int: ...

    def set_etx(self, arg: int, /) -> None: ...

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: KongsbergAllUnknown) -> bool: ...

    def copy(self) -> KongsbergAllUnknown:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllUnknown: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllUnknown: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> KongsbergAllUnknown:
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

class XYZDatagram(KongsbergAllDatagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
     122, EM
    302 and ME70BO. All receiver beams are included, check detection info
    and real time cleaning for beam status (note 4 and 5).
    """

    def __init__(self) -> None: ...

    @overload
    def get_xyz(self) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1:
        """
        Convert the XYZDatagramBeams to a XYZ structure

        Returns:
            algorithms::geoprocessing::datastructures::XYZ_1
        """

    @overload
    def get_xyz(self, beam_numbers: Sequence[int]) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1:
        """
        Convert the XYZDatagramBeams for a given beam_number vector to a XYZ
        structure
        Note: if a beam number is not found, the corresponding XYZ value will
              be NaN

        Args:
            beam_numbers:  

        Returns:
            algorithms::geoprocessing::datastructures::XYZ_1
        """

    def set_ping_counter(self, arg: int, /) -> None:
        """0-65535 ping number (in this file)"""

    def get_ping_counter(self) -> int:
        """0-65535 ping number (in this file)"""

    def set_system_serial_number(self, arg: int, /) -> None:
        """100 -"""

    def get_system_serial_number(self) -> int:
        """100 -"""

    def set_heading(self, arg: int, /) -> None:
        """(at TX time) in 0.01 degree"""

    def get_heading(self) -> int:
        """(at TX time) in 0.01 degree"""

    def set_sound_speed(self, arg: int, /) -> None:
        """at transducer in dm/s"""

    def get_sound_speed(self) -> int:
        """at transducer in dm/s"""

    def set_transmit_transducer_depth(self, arg: float, /) -> None:
        """in meter relative water level at time of ping"""

    def get_transmit_transducer_depth(self) -> float:
        """in meter relative water level at time of ping"""

    def set_number_of_beams(self, arg: int, /) -> None:
        """in Datagram"""

    def get_number_of_beams(self) -> int:
        """in Datagram"""

    def set_number_of_valid_detections(self, arg: int, /) -> None: ...

    def get_number_of_valid_detections(self) -> int: ...

    def set_sampling_frequency(self, arg: float, /) -> None:
        """in Hz"""

    def get_sampling_frequency(self) -> float:
        """in Hz"""

    def set_scanning_info(self, arg: int, /) -> None:
        """only used by em2040. 0 means scanning is not used."""

    def get_scanning_info(self) -> int:
        """only used by em2040. 0 means scanning is not used."""

    def get_beams(self) -> list[substructures.XYZDatagramBeam]:
        """beam detection information"""

    def set_beams(self, arg: Sequence[substructures.XYZDatagramBeam], /) -> None:
        """beam detection information"""

    def beams(self) -> list[substructures.XYZDatagramBeam]:
        """beam detection information"""

    def get_heading_in_degrees(self) -> float:
        """
        Get the vessel heading in degrees

        Returns:
            heading * 0.01 degrees (double)
        """

    def get_sound_speed_in_m_per_s(self) -> float:
        """
        Get the sound speed in meters per seconds

        Returns:
            sound_speed * 0.1 meters per seconds (double)
        """

    def get_spare_byte(self) -> int: ...

    def set_spare_byte(self, arg: int, /) -> None: ...

    def get_spare_bytes(self) -> typing.Any: ...

    def set_spare_bytes(self, arg: typing.Any, /) -> None: ...

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: XYZDatagram) -> bool: ...

    def copy(self) -> XYZDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> XYZDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> XYZDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> XYZDatagram:
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

class ExtraDetections(KongsbergAllDatagram):
    """
    This datagram is used for the models EM 2040 and EM 2040C with Slim
    Processing Unit.
    """

    def __init__(self) -> None: ...

    def set_ping_counter(self, arg: int, /) -> None: ...

    def get_ping_counter(self) -> int: ...

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_datagram_counter(self, arg: int, /) -> None: ...

    def get_datagram_counter(self) -> int: ...

    def set_datagram_version_id(self, arg: int, /) -> None: ...

    def get_datagram_version_id(self) -> int: ...

    def set_swath_counter(self, arg: int, /) -> None: ...

    def get_swath_counter(self) -> int: ...

    def set_swath_index(self, arg: int, /) -> None: ...

    def get_swath_index(self) -> int: ...

    def set_heading(self, arg: int, /) -> None:
        """0.01°"""

    def get_heading(self) -> int:
        """0.01°"""

    def set_sound_speed(self, arg: int, /) -> None:
        """dm/s"""

    def get_sound_speed(self) -> int:
        """dm/s"""

    def set_depth_of_reference_point(self, arg: float, /) -> None:
        """m"""

    def get_depth_of_reference_point(self) -> float:
        """m"""

    def set_water_column_sample_rate(self, arg: float, /) -> None:
        """(WCsr)"""

    def get_water_column_sample_rate(self) -> float:
        """(WCsr)"""

    def set_raw_amplitude_sample_rate(self, arg: float, /) -> None:
        """(SIsr)"""

    def get_raw_amplitude_sample_rate(self) -> float:
        """(SIsr)"""

    def set_rx_transducer_index(self, arg: int, /) -> None: ...

    def get_rx_transducer_index(self) -> int: ...

    def set_number_of_extra_detections(self, arg: int, /) -> None:
        """Nd"""

    def get_number_of_extra_detections(self) -> int:
        """Nd"""

    def set_number_of_detection_classes(self, arg: int, /) -> None: ...

    def get_number_of_detection_classes(self) -> int: ...

    def set_number_of_bytes_per_class(self, arg: int, /) -> None: ...

    def get_number_of_bytes_per_class(self) -> int: ...

    def set_number_of_alarm_flags(self, arg: int, /) -> None: ...

    def get_number_of_alarm_flags(self) -> int: ...

    def set_number_of_bytes_per_detection(self, arg: int, /) -> None: ...

    def get_number_of_bytes_per_detection(self) -> int: ...

    def set_detection_classes(self, arg: Sequence[substructures.ExtraDetectionsDetectionClasses], /) -> None:
        """substructure 1"""

    def get_detection_classes(self) -> list[substructures.ExtraDetectionsDetectionClasses]:
        """substructure 1"""

    def detection_classes(self) -> list[substructures.ExtraDetectionsDetectionClasses]: ...

    def set_extra_detections(self, arg: Sequence[substructures.ExtraDetectionsExtraDetections], /) -> None:
        """substructure 2"""

    def get_extra_detections(self) -> list[substructures.ExtraDetectionsExtraDetections]:
        """substructure 2"""

    def extra_detections(self) -> list[substructures.ExtraDetectionsExtraDetections]: ...

    def set_raw_amplitude_samples(self, arg: substructures.SampleAmplitudesStructure_int16_t, /) -> None:
        """0.1 dB"""

    def get_raw_amplitude_samples(self) -> substructures.SampleAmplitudesStructure_int16_t:
        """0.1 dB"""

    def raw_amplitude_samples(self) -> substructures.SampleAmplitudesStructure_int16_t: ...

    def get_heading_in_degrees(self) -> float:
        """
        Get heading in degrees

        Returns:
            _heading * 0.01° (double)
        """

    def get_sound_speed_in_m_per_s(self) -> float:
        """
        Get sound velocity in m/s

        Returns:
            _sound_speed * 0.1 m/s (double)
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: ExtraDetections) -> bool: ...

    def copy(self) -> ExtraDetections:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ExtraDetections: ...

    def __deepcopy__(self, arg: dict, /) -> ExtraDetections: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ExtraDetections:
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

class RawRangeAndAngle(KongsbergAllDatagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
     122, EM
    302 and ME70BO. All receiver beams are included, check detection info
    and real time cleaning for beam status (note 4 and 5).
    """

    def __init__(self) -> None: ...

    @overload
    def get_two_way_travel_times(self) -> "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>":
        """
        Read the two way travel times from the RawRangeAndAngle structure

        Returns:
            xt::xtensor_float_1
        """

    @overload
    def get_two_way_travel_times(self, beam_numbers: Sequence[int]) -> "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>":
        """
        Read the two way travel times for given beam_number vector from the
        RawRangeAndAngle structure Note: if a beam number is not found, the
        corresponding time value will be NaN

        Args:
            beam_numbers:  

        Returns:
            xt::xtensor_float_1
        """

    @overload
    def get_beam_crosstrack_angles(self) -> "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>":
        """
        Read the beam crosstrack angles from the RawRangeAndAngle structure

        Returns:
            xt::xtensor_float_1
        """

    @overload
    def get_beam_crosstrack_angles(self, beam_numbers: Sequence[int]) -> "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>":
        """
        Read the two way travel times for given beam_number vector from the
        RawRangeAndAngle structure Note: if a beam number is not found, the
        corresponding time value will be NaN

        Args:
            beam_numbers:  

        Returns:
            xt::xtensor_float_1
        """

    def set_ping_counter(self, arg: int, /) -> None:
        """sequential number"""

    def get_ping_counter(self) -> int:
        """sequential number"""

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_sound_speed_at_transducer(self, arg: int, /) -> None:
        """in 0.1 m/s"""

    def get_sound_speed_at_transducer(self) -> int:
        """in 0.1 m/s"""

    def set_number_of_transmit_sectors(self, arg: int, /) -> None:
        """ntx"""

    def get_number_of_transmit_sectors(self) -> int:
        """ntx"""

    def set_number_of_receiver_beams(self, arg: int, /) -> None:
        """in Datagram nrx"""

    def get_number_of_receiver_beams(self) -> int:
        """in Datagram nrx"""

    def set_number_of_valid_detections(self, arg: int, /) -> None: ...

    def get_number_of_valid_detections(self) -> int: ...

    def set_sampling_frequency(self, arg: float, /) -> None: ...

    def get_sampling_frequency(self) -> float: ...

    def set_d_scale(self, arg: int, /) -> None: ...

    def get_d_scale(self) -> int: ...

    def set_transmit_sectors(self, arg: Sequence[substructures.RawRangeAndAngleTransmitSector], /) -> None: ...

    def get_transmit_sectors(self) -> list[substructures.RawRangeAndAngleTransmitSector]: ...

    def transmit_sectors(self) -> list[substructures.RawRangeAndAngleTransmitSector]: ...

    def set_beams(self, arg: Sequence[substructures.RawRangeAndAngleBeam], /) -> None: ...

    def get_beams(self) -> list[substructures.RawRangeAndAngleBeam]: ...

    def beams(self) -> list[substructures.RawRangeAndAngleBeam]: ...

    def get_sound_speed_at_transducer_in_m_per_s(self) -> float:
        """
        Get the sound speed at the transducerin meters per seconds

        Returns:
            _sound_speed_at_transducer * 0.1 meters per seconds (float)
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: RawRangeAndAngle) -> bool: ...

    def copy(self) -> RawRangeAndAngle:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RawRangeAndAngle: ...

    def __deepcopy__(self, arg: dict, /) -> RawRangeAndAngle: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RawRangeAndAngle:
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

class SeabedImageData(KongsbergAllDatagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
     122, EM
    302 and ME70BO. All receiver beams are included, check detection info
    and real time cleaning for beam status (note 4 and 5).
    """

    def __init__(self) -> None: ...

    def set_ping_counter(self, arg: int, /) -> None:
        """sequential number"""

    def get_ping_counter(self) -> int:
        """sequential number"""

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_sampling_frequency(self, arg: float, /) -> None:
        """in Hz"""

    def get_sampling_frequency(self) -> float:
        """in Hz"""

    def set_range_to_normal_incidence(self, arg: int, /) -> None:
        """used to correct sample amplitudes in no. of samples"""

    def get_range_to_normal_incidence(self) -> int:
        """used to correct sample amplitudes in no. of samples"""

    def set_normal_incidence_backscatter(self, arg: int, /) -> None:
        """in 0.01 dB (BSN)"""

    def get_normal_incidence_backscatter(self) -> int:
        """in 0.01 dB (BSN)"""

    def set_oblique_backscatter(self, arg: int, /) -> None:
        """in 0.01 dB (BSO)"""

    def get_oblique_backscatter(self) -> int:
        """in 0.01 dB (BSO)"""

    def set_tx_beamwidth_along(self, arg: int, /) -> None:
        """in 0.1 degree"""

    def get_tx_beamwidth_along(self) -> int:
        """in 0.1 degree"""

    def set_tvg_law_crossover_angle(self, arg: int, /) -> None:
        """in 0.1 degree"""

    def get_tvg_law_crossover_angle(self) -> int:
        """in 0.1 degree"""

    def set_number_of_valid_beams(self, arg: int, /) -> None: ...

    def get_number_of_valid_beams(self) -> int: ...

    def set_spare_byte(self, arg: int, /) -> None: ...

    def get_spare_byte(self) -> int: ...

    def get_beams(self) -> list[substructures.SeabedImageDataBeam]: ...

    def set_beams(self, arg: Sequence[substructures.SeabedImageDataBeam], /) -> None: ...

    def beams(self) -> list[substructures.SeabedImageDataBeam]: ...

    def get_sample_amplitudes(self) -> substructures.SampleAmplitudesStructure_int16_t:
        """in 0.1 dB (size = sum of _Number_of_samples of all Beams"""

    def set_sample_amplitudes(self, arg: substructures.SampleAmplitudesStructure_int16_t, /) -> None:
        """in 0.1 dB (size = sum of _Number_of_samples of all Beams"""

    def sample_amplitudes(self) -> substructures.SampleAmplitudesStructure_int16_t:
        """in 0.1 dB (size = sum of _Number_of_samples of all Beams"""

    def get_normal_incidence_backscatter_in_db(self) -> float:
        """
        Get the normal incidence backscatter in db

        Returns:
            _normal_incidence_backscatter * 0.01f (float)
        """

    def get_oblique_backscatter_in_db(self) -> float:
        """
        Get the oblique backscatter in db

        Returns:
            _oblique_backscatter * 0.01f (float)
        """

    def get_tx_beamwidth_along_in_degrees(self) -> float:
        """
        get the tx beamwidth along in degrees

        Returns:
            _tx_beamwidth_along * 0.1f (float)
        """

    def get_tvg_law_crossover_angle_in_degrees(self) -> float:
        """
        get the tvg law crossover angle in degrees

        Returns:
            _tvg_law_crossover_angle * 0.1f (float)
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: SeabedImageData) -> bool: ...

    def copy(self) -> SeabedImageData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SeabedImageData: ...

    def __deepcopy__(self, arg: dict, /) -> SeabedImageData: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SeabedImageData:
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

class WatercolumnDatagram(KongsbergAllDatagram):
    """
    Used for EM 122, EM 302, EM 710, EM 2040, EM 3002. The receiver beams
    are roll stabilized.
    """

    def __init__(self) -> None: ...

    def get_samples(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    def set_ping_counter(self, arg: int, /) -> None: ...

    def get_ping_counter(self) -> int: ...

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_number_of_datagrams(self, arg: int, /) -> None: ...

    def get_number_of_datagrams(self) -> int: ...

    def set_datagram_number(self, arg: int, /) -> None: ...

    def get_datagram_number(self) -> int: ...

    def set_number_of_transmit_sectors(self, arg: int, /) -> None:
        """Transmit_sector vector of 2 elements"""

    def get_number_of_transmit_sectors(self) -> int:
        """Transmit_sector vector of 2 elements"""

    def set_total_no_of_receive_beams(self, arg: int, /) -> None: ...

    def get_total_no_of_receive_beams(self) -> int: ...

    def set_number_of_beams_in_datagram(self, arg: int, /) -> None:
        """Beam vector of 2 elements"""

    def get_number_of_beams_in_datagram(self) -> int:
        """Beam vector of 2 elements"""

    def set_sound_speed(self, arg: int, /) -> None:
        """in 0.1 m/s"""

    def get_sound_speed(self) -> int:
        """in 0.1 m/s"""

    def set_sampling_frequency(self, arg: int, /) -> None: ...

    def get_sampling_frequency(self) -> int: ...

    def set_tx_time_heave(self, arg: int, /) -> None:
        """in cm"""

    def get_tx_time_heave(self) -> int:
        """in cm"""

    def set_tvg_function_applied(self, arg: int, /) -> None: ...

    def get_tvg_function_applied(self) -> int: ...

    def set_tvg_offset_in_db(self, arg: int, /) -> None: ...

    def get_tvg_offset_in_db(self) -> int: ...

    def set_scanning_info(self, arg: int, /) -> None: ...

    def get_scanning_info(self) -> int: ...

    def set_spare(self, arg: typing.Any, /) -> None: ...

    def get_spare(self) -> typing.Any: ...

    def get_beams(self) -> list[substructures.WatercolumnDatagramBeam]: ...

    def set_beams(self, arg: Sequence[substructures.WatercolumnDatagramBeam], /) -> None: ...

    def beams(self) -> list[substructures.WatercolumnDatagramBeam]: ...

    def get_transmit_sectors(self) -> list[substructures.WatercolumnDatagramTransmitSector]: ...

    def set_transmit_sectors(self, arg: Sequence[substructures.WatercolumnDatagramTransmitSector], /) -> None: ...

    def transmit_sectors(self) -> list[substructures.WatercolumnDatagramTransmitSector]: ...

    def get_sound_speed_m_s(self) -> float:
        """
        Get the sound speed in m/s

        Returns:
            _sound_speed * 0.1 m/s (float)
        """

    def get_sampling_frequency_in_hz(self) -> float:
        """
        Get the sampling frequency in Hz

        Returns:
            _sampling_frequency * 0.01 Hz (float)
        """

    def get_tx_time_heave_in_m(self) -> float:
        """
        Get the transmit time heave in m

        Returns:
            _tx_time_heave * 0.01 m (float)
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: WatercolumnDatagram) -> bool: ...

    def copy(self) -> WatercolumnDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> WatercolumnDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> WatercolumnDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> WatercolumnDatagram:
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

class QualityFactorDatagram(KongsbergAllDatagram):
    """
    The Quality Factor is an estimate of the standard deviation of the
    detected depth. QF = − log(Est(dz)/z) QF = 3.0 means an estimated
    standard deviation of 0.1% of the detected depth. QF = 2.0 means an
    estimated standard deviation of 1.0% of the detected depth. QF = 0
    means that the Quality Factor could not be computed. The Quality
    Factor is calculated by the echo sounder according to formulas
    provided by IFREMER. Used for EM 122, EM 302, EM 710, EM 2040, EM
    2040C, EM 3002 and ME70BO.
    """

    def __init__(self) -> None: ...

    def set_ping_counter(self, arg: int, /) -> None:
        """0-65535 ping number (in this file)"""

    def get_ping_counter(self) -> int:
        """0-65535 ping number (in this file)"""

    def set_system_serial_number(self, arg: int, /) -> None:
        """100 -"""

    def get_system_serial_number(self) -> int:
        """100 -"""

    def set_number_of_receive_beams(self, arg: int, /) -> None:
        """Nrx"""

    def get_number_of_receive_beams(self) -> int:
        """Nrx"""

    def set_number_of_parameters_per_beam(self, arg: int, /) -> None:
        """Npar"""

    def get_number_of_parameters_per_beam(self) -> int:
        """Npar"""

    def set_spare(self, arg: int, /) -> None:
        """always 0"""

    def get_spare(self) -> int:
        """always 0"""

    def get_quality_factors(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """dimension is [Nrx, Npar]"""

    def set_quality_factors(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], /) -> None:
        """dimension is [Nrx, Npar]"""

    def quality_factors(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """dimension is [Nrx, Npar]"""

    def qf_shape(self) -> typing.Any:
        """
        return the shape of the quality factor array Computed as
        [_number_of_receive_beams, _number_of_parameters_per_beam]

        Returns:
            xt::xtensor_float_2::shape_type
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: QualityFactorDatagram) -> bool: ...

    def copy(self) -> QualityFactorDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> QualityFactorDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> QualityFactorDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> QualityFactorDatagram:
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

class AttitudeDatagram(KongsbergAllDatagram):
    """
    This datagram is used for the models EM 2040, EM 2040C, EM 710, EM
     122, EM
    302 and ME70BO. All receiver beams are included, check detection info
    and real time cleaning for beam status (note 4 and 5).
    """

    def __init__(self) -> None: ...

    def set_attitude_counter(self, arg: int, /) -> None: ...

    def get_attitude_counter(self) -> int: ...

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_number_of_entries(self, arg: int, /) -> None:
        """N"""

    def get_number_of_entries(self) -> int:
        """N"""

    def set_sensor_system_descriptor(self, arg: int, /) -> None: ...

    def get_sensor_system_descriptor(self) -> int: ...

    def get_attitudes(self) -> list[substructures.AttitudeDatagramAttitude]:
        """N x Attitude data"""

    def set_attitudes(self, arg: Sequence[substructures.AttitudeDatagramAttitude], /) -> None:
        """N x Attitude data"""

    def attitudes(self) -> list[substructures.AttitudeDatagramAttitude]:
        """N x Attitude data"""

    def get_attitude_sensor_number(self) -> int:
        """
        Get the number of attitude sensor from the sensor system descriptor
        field. xx00 xxxx – attitude sensor number 1 xx01 xxxx – attitude
        sensor number 2

        Returns:
            1 or 2
        """

    def get_heading_sensor_is_active(self) -> bool:
        """
        Evaluate if the heading sensor is active using sensor system
        descriptor field. 0bxxxxxxx1 : heading is active 0bxxxxxxx1 : heading
        is inactive

        Returns:
            bool
        """

    def get_roll_sensor_is_active(self) -> bool:
        """
        Evaluate if the roll sensor is active using sensor system descriptor
        field. 0bxxxxxx1x : roll is active 0bxxxxxx0x : roll is inactive

        Returns:
            bool
        """

    def get_pitch_sensor_is_active(self) -> bool:
        """
        Evaluate if the pitch sensor is active using sensor system descriptor
        field. 0bxxxxx1xx : pitch is active 0bxxxxx0xx : pitch is inactive

        Returns:
            bool
        """

    def get_heave_sensor_is_active(self) -> bool:
        """
        Evaluate if the heave sensor is active using sensor system descriptor
        field. 0bxxxx1xxx : heave is active 0bxxxx0xxx : heave is inactive

        Returns:
            bool
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: AttitudeDatagram) -> bool: ...

    def copy(self) -> AttitudeDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> AttitudeDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> AttitudeDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> AttitudeDatagram:
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

class NetworkAttitudeVelocityDatagram(KongsbergAllDatagram):
    """
    Network attitude velocity datagram 110. This datagram is currently not
    used in the processing because the Attitude datagram already contains
    all necessary information.
    """

    def __init__(self) -> None: ...

    def set_network_attitude_counter(self, arg: int, /) -> None: ...

    def get_network_attitude_counter(self) -> int: ...

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_number_of_entries(self, arg: int, /) -> None:
        """N"""

    def get_number_of_entries(self) -> int:
        """N"""

    def set_sensor_system_descriptor(self, arg: int, /) -> None: ...

    def get_sensor_system_descriptor(self) -> int: ...

    def get_attitudes(self) -> list[substructures.NetworkAttitudeVelocityDatagramAttitude]:
        """N x Attitude data"""

    def set_attitudes(self, arg: Sequence[substructures.NetworkAttitudeVelocityDatagramAttitude], /) -> None:
        """N x Attitude data"""

    def attitudes(self) -> list[substructures.NetworkAttitudeVelocityDatagramAttitude]:
        """N x Attitude data"""

    def get_attitude_velocity_sensor_number(self) -> int:
        """
        Get the number of attitude sensor from the sensor system descriptor
        field. If this field is xx10 xxxx – attitude velocity sensor 1 (UDP5)
        xx11 xxxx – attitude velocity sensor 2 (UDP6)

        Returns:
            1 or 2
        """

    def get_velocity_sensor_is_active(self) -> bool:
        """
        Evaluate if the velocity sensor is active using sensor system
        descriptor field. 0bxxxxxxx1 : velocity is active 0bxxxxxxx1 :
        velocity is inactive

        The exact meaning of this field is currently not clear to us. If this
        field is set to false, the attitude data seems to be exactly the same
        as in the attitude datagram. If it is set to true, the attitude data
        will be a little bit different.

        Returns:
            bool
        """

    def get_heading_sensor_is_active(self) -> bool:
        """
        Evaluate if the heading sensor is active using sensor system
        descriptor field. 0bxxxxxxx1 : heading is active 0bxxxxxxx1 : heading
        is inactive

        Returns:
            bool
        """

    def get_roll_sensor_is_active(self) -> bool:
        """
        Evaluate if the roll sensor is active using sensor system descriptor
        field. 0bxxxxxx1x : roll is active 0bxxxxxx0x : roll is inactive

        Returns:
            bool
        """

    def get_pitch_sensor_is_active(self) -> bool:
        """
        Evaluate if the pitch sensor is active using sensor system descriptor
        field. 0bxxxxx1xx : pitch is active 0bxxxxx0xx : pitch is inactive

        Returns:
            bool
        """

    def get_heave_sensor_is_active(self) -> bool:
        """
        Evaluate if the heave sensor is active using sensor system descriptor
        field. 0bxxxx1xxx : heave is active 0bxxxx0xxx : heave is inactive

        Returns:
            bool
        """

    def get_function_is_used(self) -> bool:
        """
        Evaluate if the function is used. -1 : function is not used

        Returns:
            bool
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def get_spare(self) -> int: ...

    def set_spare(self, arg: int, /) -> None: ...

    def get_spare_align(self) -> int: ...

    def set_spare_align(self, arg: int, /) -> None: ...

    def __eq__(self, other: NetworkAttitudeVelocityDatagram) -> bool: ...

    def copy(self) -> NetworkAttitudeVelocityDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NetworkAttitudeVelocityDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> NetworkAttitudeVelocityDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NetworkAttitudeVelocityDatagram:
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

class ClockDatagram(KongsbergAllDatagram):
    """Clock datagrams"""

    def __init__(self) -> None: ...

    def set_clock_counter(self, arg: int, /) -> None:
        """sequential number"""

    def get_clock_counter(self) -> int:
        """sequential number"""

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_date_external(self, arg: int, /) -> None:
        """
        from external clock input year*1000 + month*100 + day(Example:Jun 27,
        2020 = 20200627)
        """

    def get_date_external(self) -> int:
        """
        from external clock input year*1000 + month*100 + day(Example:Jun 27,
        2020 = 20200627)
        """

    def set_time_since_midnight_external(self, arg: int, /) -> None:
        """in ms from external clock datagram"""

    def get_time_since_midnight_external(self) -> int:
        """in ms from external clock datagram"""

    def set_pps_active(self, arg: int, /) -> None:
        """
        0 = inactive (Shows if the system clock is synchronized to an external
        PPS signal or not)
        """

    def get_pps_active(self) -> int:
        """
        0 = inactive (Shows if the system clock is synchronized to an external
        PPS signal or not)
        """

    def get_timestamp_external(self) -> float:
        """
        convert the date and time_since_midnight field to a unix timestamp

        Returns:
            unixtime as double
        """

    def get_timestamp_offset(self) -> float:
        """
        difference between timestamp and timestamp_external

        Returns:
            timestamp_external - timestamp
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: ClockDatagram) -> bool: ...

    def copy(self) -> ClockDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ClockDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> ClockDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ClockDatagram:
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

class DepthOrHeightDatagram(KongsbergAllDatagram):
    """Depth (pressure) or height datagrams"""

    def __init__(self) -> None: ...

    def set_height_counter(self, arg: int, /) -> None:
        """Sequential Number"""

    def get_height_counter(self) -> int:
        """Sequential Number"""

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_height(self, arg: int, /) -> None:
        """in cm"""

    def get_height(self) -> int:
        """in cm"""

    def set_height_type(self, arg: int, /) -> None:
        """
        0: derived from GGK or GGA, 1-99 ???, 100 depth is taken from the
        DepthOrheight datagram, 200: Input from depth sensor
        """

    def get_height_type(self) -> int:
        """
        0: derived from GGK or GGA, 1-99 ???, 100 depth is taken from the
        DepthOrheight datagram, 200: Input from depth sensor
        """

    def get_height_in_meters(self) -> float:
        """
        Get the height in meters

        Returns:
            _height * 0.01m (float)
        """

    def get_height_type_explained(self) -> str:
        """
        Get a string description of the height_type

        Returns:
            std::string
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: DepthOrHeightDatagram) -> bool: ...

    def copy(self) -> DepthOrHeightDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> DepthOrHeightDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> DepthOrHeightDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> DepthOrHeightDatagram:
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

class HeadingDatagram(KongsbergAllDatagram):
    """Heading datagrams"""

    def __init__(self) -> None: ...

    def set_heading_counter(self, arg: int, /) -> None:
        """Sequential Number"""

    def get_heading_counter(self) -> int:
        """Sequential Number"""

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_number_of_entries(self, arg: int, /) -> None:
        """N"""

    def get_number_of_entries(self) -> int:
        """0 = inactive"""

    def set_heading_indicator(self, arg: int, /) -> None:
        """0 = inactive"""

    def get_heading_indicator(self) -> int:
        """0 = inactive"""

    def get_times_and_headings(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None, None), order='C')]:
        """2xN array of time in ms since record start and heading in 0.01°"""

    def set_times_and_headings(self, arg: Annotated[NDArray[numpy.uint16], dict(shape=(None, None), order='C')], /) -> None:
        """2xN array of time in ms since record start and heading in 0.01°"""

    def times_and_headings(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None, None), order='C')]:
        """2xN array of time in ms since record start and heading in 0.01°"""

    def get_heading_timestamps(self) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        return the times converted to unix timestamps

        Returns:
            np.array([_number_of_entries], dtype = np.float64)
        """

    def get_headings_in_degrees(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        return headings in degrees by multiplying the heading by 0.01

        Returns:
            np.array([_number_of_entries], dtype = np.float32)
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: HeadingDatagram) -> bool: ...

    def copy(self) -> HeadingDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> HeadingDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> HeadingDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> HeadingDatagram:
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

class PositionDatagram(KongsbergAllDatagram):
    """Depth (pressure) or height datagrams"""

    def __init__(self) -> None: ...

    def set_position_counter(self, arg: int, /) -> None: ...

    def get_position_counter(self) -> int: ...

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_latitude(self, arg: int, /) -> None:
        """latitude in 0.00000005° negative if southern hemishpere"""

    def get_latitude(self) -> int:
        """latitude in 0.00000005° negative if southern hemishpere"""

    def set_longitude(self, arg: int, /) -> None:
        """longitude in 0.0000001° negative if western hemishpere"""

    def get_longitude(self) -> int:
        """longitude in 0.0000001° negative if western hemishpere"""

    def set_position_fix_quality(self, arg: int, /) -> None:
        """fix quality in cm;"""

    def get_position_fix_quality(self) -> int:
        """fix quality in cm;"""

    def set_speed(self, arg: int, /) -> None:
        """over ground in cm/s"""

    def get_speed(self) -> int:
        """over ground in cm/s"""

    def set_course(self, arg: int, /) -> None:
        """over ground in 0.01°"""

    def get_course(self) -> int:
        """over ground in 0.01°"""

    def set_heading(self, arg: int, /) -> None:
        """in 0.01°"""

    def get_heading(self) -> int:
        """in 0.01°"""

    def set_position_system_descriptor(self, arg: int, /) -> None: ...

    def get_position_system_descriptor(self) -> int: ...

    def set_size_of_input_datagram(self, arg: int, /) -> None:
        """in input datagram;"""

    def get_size_of_input_datagram(self) -> int:
        """in input datagram;"""

    def set_input_datagram(self, arg: str, /) -> None: ...

    def get_input_datagram(self) -> str: ...

    def get_latitude_in_degrees(self) -> float:
        """
        Get the latitude in degrees

        Returns:
            _latitude * 0.00000005° (double)
        """

    def get_longitude_in_degrees(self) -> float:
        """
        Get the longitude in degrees

        Returns:
            _longitude * 0.0000001° (double)
        """

    def get_position_fix_quality_in_meters(self) -> float:
        """
        Get the position fix quality in meters

        Returns:
            _position_fix_quality * 0.01m (float)
        """

    def get_speed_in_meters_per_second(self) -> float:
        """
        Get the speed of vessel in meter per second

        Returns:
            _speed * 0.01m/s (float)
        """

    def get_course_in_degrees(self) -> float:
        """
        Get the course of vessel in degrees

        Returns:
            _course * 0.01° (float)
        """

    def get_heading_in_degrees(self) -> float:
        """
        Get the heading of vessel in degrees

        Returns:
            _heading * 0.01° (float)
        """

    def get_position_system_number(self) -> int:
        """
        Evaluate if the position_system_descriptor for the used system number

        Returns:
            1, 2 or 3 (uint8_t )
        """

    def get_position_system_SIMRAD90_flag(self) -> bool:
        """
        Evaluate if the position_system_descriptor for the used system number

        xxxx 1xxx – the position may have to be derived from the input
        datagram which is then in SIMRADRAW 90 format.

        Returns:
            true or false (bool)
        """

    def get_position_system_system_time_has_been_used(self) -> bool:
        """
        Evaluate the position_system_descriptor for the used time

        Returns:
            true: system time has been used
            false: input datagram time has been used
        """

    def set_spare(self, arg: int, /) -> None:
        """only if required to make the datagram size even"""

    def get_spare(self) -> int:
        """only if required to make the datagram size even"""

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: PositionDatagram) -> bool: ...

    def copy(self) -> PositionDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> PositionDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> PositionDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> PositionDatagram:
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

class SingleBeamEchoSounderDepth(KongsbergAllDatagram):
    """Single beam echo sounder depth datagram"""

    def __init__(self) -> None: ...

    def set_echo_sounder_counter(self, arg: int, /) -> None:
        """Sequential Number"""

    def get_echo_sounder_counter(self) -> int:
        """Sequential Number"""

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_input_date(self, arg: int, /) -> None:
        """year*10000 + month*100 + day (from input datagram if available)"""

    def get_input_date(self) -> int:
        """year*10000 + month*100 + day (from input datagram if available)"""

    def set_input_time_since_midnight(self, arg: int, /) -> None:
        """time since midnight in milliseconds (from input datagram if available)"""

    def get_input_time_since_midnight(self) -> int:
        """time since midnight in milliseconds (from input datagram if available)"""

    def set_echo_sounder_depth(self, arg: int, /) -> None:
        """from waterline in cm"""

    def get_echo_sounder_depth(self) -> int:
        """from waterline in cm"""

    def set_source_identifier(self, arg: str, /) -> None:
        """'S', 'T', '1', '2' or '3'"""

    def get_source_identifier(self) -> str:
        """'S', 'T', '1', '2' or '3'"""

    def get_input_timestamp(self) -> float:
        """
        convert the date and time_since_midnight field to a unix timestamp

        Returns:
            unixtime as double
        """

    def get_input_date_string(self, arg0: int, arg1: str, /) -> str:
        """
        Get the time as string

        Args:
            fractionalSecondsDigits: 
            format: 

        Returns:
            std::string
        """

    def get_echo_sounder_depth_in_meters(self) -> float:
        """
        Get the echo sounder depth in meters

        Returns:
            _echo_sounder_depth * 0.01f (float)
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: SingleBeamEchoSounderDepth) -> bool: ...

    def copy(self) -> SingleBeamEchoSounderDepth:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SingleBeamEchoSounderDepth: ...

    def __deepcopy__(self, arg: dict, /) -> SingleBeamEchoSounderDepth: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SingleBeamEchoSounderDepth:
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

class SurfaceSoundSpeedDatagram(KongsbergAllDatagram):
    """Sound_speed datagrams"""

    def __init__(self) -> None: ...

    def set_sound_speed_counter(self, arg: int, /) -> None:
        """Sequential Number"""

    def get_sound_speed_counter(self) -> int:
        """Sequential Number"""

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_number_of_entries(self, arg: int, /) -> None:
        """N"""

    def get_number_of_entries(self) -> int: ...

    def set_spare(self, arg: int, /) -> None: ...

    def get_spare(self) -> int: ...

    def get_times_and_sound_speeds(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None, None), order='C')]:
        """2xN array of time in ms since record start and sound_speed in dm/s"""

    def set_times_and_sound_speeds(self, arg: Annotated[NDArray[numpy.uint16], dict(shape=(None, None), order='C')], /) -> None:
        """2xN array of time in ms since record start and sound_speed in dm/s"""

    def times_and_sound_speeds(self) -> Annotated[NDArray[numpy.uint16], dict(shape=(None, None), order='C')]:
        """2xN array of time in ms since record start and sound_speed in dm/s"""

    def get_sound_speed_timestamps(self) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        return the times converted to unix timestamps

        Returns:
            np.array([_number_of_entries], dtype = np.float64)
        """

    def get_sound_speeds_in_meters_per_second(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        return sound_speeds in meters by multiplying the surface sound_speed
        by 0.1

        Returns:
            np.array([_number_of_entries], dtype = np.float32)
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: SurfaceSoundSpeedDatagram) -> bool: ...

    def copy(self) -> SurfaceSoundSpeedDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SurfaceSoundSpeedDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> SurfaceSoundSpeedDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SurfaceSoundSpeedDatagram:
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

class SoundSpeedProfileDatagram(KongsbergAllDatagram):
    """
    This datagram will contain the profile actually used in the real time
    raybending calculations to convert range and angle to xyz data. It
    will usually be issued together with the installation parameter
    datagram.
    """

    def __init__(self) -> None: ...

    def set_profile_counter(self, arg: int, /) -> None:
        """Sequential Number"""

    def get_profile_counter(self) -> int:
        """Sequential Number"""

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_profile_date(self, arg: int, /) -> None:
        """year*10000 + month*100 + day (when profile was taken)"""

    def get_profile_date(self) -> int:
        """year*10000 + month*100 + day (when profile was taken)"""

    def set_profile_time_since_midnight(self, arg: int, /) -> None:
        """time since midnight in milliseconds (when profile was taken)"""

    def get_profile_time_since_midnight(self) -> int:
        """time since midnight in milliseconds (when profile was taken)"""

    def set_number_of_entries(self, arg: int, /) -> None:
        """N"""

    def get_number_of_entries(self) -> int: ...

    def set_depth_resolution(self, arg: int, /) -> None:
        """in cm"""

    def get_depth_resolution(self) -> int:
        """in cm"""

    def set_spare(self, arg: int, /) -> None: ...

    def get_spare(self) -> int: ...

    def get_depths_and_sound_speeds(self) -> Annotated[NDArray[numpy.uint32], dict(shape=(None, None), order='C')]:
        """2xN array of depth in cm and sound speed in dm/s"""

    def set_depths_and_sound_speeds(self, arg: Annotated[NDArray[numpy.uint32], dict(shape=(None, None), order='C')], /) -> None:
        """2xN array of depth in cm and sound speed in dm/s"""

    def depths_and_sound_speeds(self) -> Annotated[NDArray[numpy.uint32], dict(shape=(None, None), order='C')]:
        """2xN array of depth in cm and sound speed in dm/s"""

    def get_depth_resolution_in_meters(self) -> float:
        """
        return the depths in meters

        Returns:
            _depth_resolution * 0.01 (float)
        """

    def get_depths_in_meters(self) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]:
        """
        return the depths in meters by multiplying the depths by 0.01

        Returns:
            np.array([_number_of_entries], dtype = np.float64)
        """

    def get_sound_speeds_in_meters_per_second(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
        """
        return sound speeds in meter per second by multiplying the
        sound_speeds by 0.1

        Returns:
            np.array([_number_of_entries], dtype = np.float32)
        """

    def get_profile_timestamp(self) -> float:
        """
        convert the profile date and time_since_midnight field to a unix
        timestamp

        Returns:
            unixtime as double
        """

    def get_profile_date_string(self, arg0: int, arg1: str, /) -> str:
        """
        Get the profile time as string

        Args:
            fractionalSecondsDigits: 
            format: 

        Returns:
            std::string
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: SoundSpeedProfileDatagram) -> bool: ...

    def copy(self) -> SoundSpeedProfileDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SoundSpeedProfileDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> SoundSpeedProfileDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SoundSpeedProfileDatagram:
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

class InstallationParameters(KongsbergAllDatagram):
    """
    This datagram is an ASCII datagram except for the header which is
    formatted as in all other output datagrams. The datagram is issued as
    a start datagram when logging is switched on and as a stop datagram
    when logging is turned off, i.e. at the start and end of a survey
    line. It may also be sent to a remote port as an information datagram.
    It is usually followed by a sound speed profile datagram. In the
    datagram all ASCII fields start with a unique three character
    identifier followed by "=". This should be used when searching for a
    specific field as the position of a field within the datagram is not
    guaranteed. The number or character part following is in a variable
    format with a minus sign and decimal point if needed, and with "," as
    the field delimiter. The format may at any time later be expanded with
    the addition of new fields at any place in the datagram.
    """

    def __init__(self) -> None: ...

    def set_installation_parameters_counter(self, arg: int, /) -> None:
        """Sequential Number"""

    def read_installation_parameters_counter(self) -> int:
        """Sequential Number"""

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_secondary_system_serial_number(self, arg: int, /) -> None: ...

    def get_secondary_system_serial_number(self) -> int: ...

    def read_installation_parameters(self) -> str: ...

    def set_installation_parameters(self, arg: str, /) -> None: ...

    def read_installation_parameters_parsed(self) -> dict[str, str]: ...

    def reparse_installation_parameters(self) -> None:
        """
        parse the installation parameters string into a map This happens when
        the datagram is read from a file, but must be called manually when the
        installation parameters string is changed manually.
        """

    @staticmethod
    def merge(datagram_1: InstallationParameters, datagram_2: InstallationParameters) -> InstallationParameters:
        """
        Merge two InstallationParameters datagrams into one If the datagrams
        differ because an uncritical key does not exist in one of them, the
        uncritical key will be added to the resulting datagram.

        Args:
            first: 
            second: 

        Returns:
            InstallationParameters
        """

    def get_compass_offsets(self) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
        """
        Get the compass sensor offsets (Gyrocompass) Includes heading offset
        only

        Returns:
            navigation::datastructures::PositionalOffsets
        """

    def get_depth_sensor_offsets(self) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
        """
        Get the depth sensor offsets

        Returns:
            navigation::datastructures::PositionalOffsets
        """

    @overload
    def get_attitude_sensor_offsets(self, sensor_number: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
        """
        Get the attitude sensor offsets of sensor 1 or 2

        Args:
            sensor_number: o_KongsbergAllActiveSensor (enum)

        Returns:
            navigation::datastructures::PositionalOffsets
        """

    @overload
    def get_attitude_sensor_offsets(self, sensor: int) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets: ...

    def get_position_system_offsets(self, position_system_number: int) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
        """
        Get the position system offsets of system 1, 2 or 3

        Args:
            position_system_number: must be 1, 2 or 3

        Returns:
            navigation::datastructures::PositionalOffsets
        """

    def get_transducer_offsets(self, transducer_number: int, transducer_name: str = '') -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
        """
        Get the transducer offsets of transducer 0, 1, 2 or 3

        Args:
            position_system_number: must be 0, 1, 2 or 3

        Returns:
            navigation::datastructures::PositionalOffsets
        """

    def get_active_pitch_roll_sensor(self) -> themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor:
        """
        Get the active roll pitch sensor (2, 3, 8 or 9) here returned as an
        enum

        Returns:
            o_KongsbergAllActiveSensor
        """

    def get_active_position_system_number(self) -> int:
        """
        Get the active position system number (APS + 1)
        Returns:
            uint8_t
        """

    def get_active_attitude_velocity_sensor(self) -> int:
        """
        Get the active attitude velocity sensor (not active, 1 or 2)
        0: not used
        1: Attitude Velocity Sensor 1 (assumed to be physical equal to
           Attitude sensor 1)
        2: Attitude Velocity Sensor 2 (assumed to be physical equal to
           Attitude sensor 2)

        Returns:
            o_KongsbergAllActiveSensor
        """

    def get_active_heave_sensor(self) -> themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor:
        """
        Get the active heave sensor (2, 3, 8 or 9) here returned as an enum

        Returns:
            o_KongsbergAllActiveSensor
        """

    def get_active_heading_sensor(self) -> themachinethatgoesping.echosounders_nanopy.o_KongsbergAllActiveSensor:
        """
        Get the active heading sensor (0-9) here returned as an enum

        Returns:
            o_KongsbergAllActiveSensor
        """

    def get_sensor_offsets(self, sensor_name: str, sensor_prefix: str, has_xyz: bool = True, has_ypr: bool = True) -> themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets:
        """
        Internal function to get the sensor offsets from the installation
        parameters. Possible sensor prefixes are:
        - MS for attitude sensor 1 - NS for attitude sensor 2 - P1 for
          position system 1 - P2 for position system 2 - P3 for position
          system 3 - S1 for transducer 1 - S2 for transducer 2 - S3 for
          transducer 3 - DS for depth (pressure) sensor

        Args:
            sensor_name: e.g. Attitude sensor 1
            sensor_prefix: see above
            has_xyz: sensor has xyz offsets
            has_ypr: sensor has yaw pitch roll offsets

        Returns:
            PositionalOffsets
        """

    def get_water_line_vertical_location_in_meters(self) -> float: ...

    def get_system_main_head_serial_number(self) -> int: ...

    def get_tx_serial_number(self) -> int: ...

    def get_tx2_serial_number(self) -> int: ...

    def get_rx1_serial_number(self) -> int: ...

    def get_rx2_serial_number(self) -> int: ...

    def get_system_transducer_configuration(self) -> themachinethatgoesping.echosounders_nanopy.o_KongsbergAllSystemTransducerConfiguration: ...

    def get_tx_array_size(self) -> str: ...

    def get_rx_array_size(self) -> str: ...

    def is_dual_rx(self) -> bool: ...

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: InstallationParameters) -> bool: ...

    def copy(self) -> InstallationParameters:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> InstallationParameters: ...

    def __deepcopy__(self, arg: dict, /) -> InstallationParameters: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> InstallationParameters:
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

class RuntimeParameters(KongsbergAllDatagram):
    """Runtime parameters datagrams"""

    def __init__(self) -> None: ...

    def set_ping_counter(self, arg: int, /) -> None: ...

    def get_ping_counter(self) -> int: ...

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_operator_station_status(self, arg: int, /) -> None: ...

    def get_operator_station_status(self) -> int: ...

    def set_processing_unit_status(self, arg: int, /) -> None: ...

    def get_processing_unit_status(self) -> int: ...

    def set_bsp_status(self, arg: int, /) -> None: ...

    def get_bsp_status(self) -> int: ...

    def set_sonar_head_or_transceiver_status(self, arg: int, /) -> None: ...

    def get_sonar_head_or_transceiver_status(self) -> int: ...

    def set_mode(self, arg: int, /) -> None: ...

    def get_mode(self) -> int: ...

    def set_filter_identifier(self, arg: int, /) -> None: ...

    def get_filter_identifier(self) -> int: ...

    def set_minimum_depth(self, arg: int, /) -> None:
        """in meter"""

    def get_minimum_depth(self) -> int:
        """in meter"""

    def set_maximum_depth(self, arg: int, /) -> None:
        """in meter"""

    def get_maximum_depth(self) -> int:
        """in meter"""

    def set_absorption_coefficient(self, arg: int, /) -> None:
        """in 0.01 dB/km"""

    def get_absorption_coefficient(self) -> int:
        """in 0.01 dB/km"""

    def set_transmit_pulse_length(self, arg: int, /) -> None:
        """in μs"""

    def get_transmit_pulse_length(self) -> int:
        """in μs"""

    def set_transmit_beamwidth(self, arg: int, /) -> None:
        """in 0.1 degrees"""

    def get_transmit_beamwidth(self) -> int:
        """in 0.1 degrees"""

    def set_transmit_power_relative_maximum(self, arg: int, /) -> None:
        """in dB"""

    def get_transmit_power_relative_maximum(self) -> int:
        """in dB"""

    def set_receive_beamwidth_degree(self, arg: int, /) -> None:
        """in 0.1 degrees"""

    def get_receive_beamwidth_degree(self) -> int:
        """in 0.1 degrees"""

    def set_receive_bandwidth_50hz(self, arg: int, /) -> None:
        """in 50 Hz resolution"""

    def get_receive_bandwidth_50hz(self) -> int:
        """in 50 Hz resolution"""

    def set_mode2_or_receiver_fixed_gain_setting(self, arg: int, /) -> None:
        """in dB"""

    def get_mode2_or_receiver_fixed_gain_setting(self) -> int:
        """in dB"""

    def set_tvg_law_crossover_angle(self, arg: int, /) -> None:
        """in degrees"""

    def get_tvg_law_crossover_angle(self) -> int:
        """in degrees"""

    def set_source_of_sound_speed_at_transducer(self, arg: int, /) -> None: ...

    def get_source_of_sound_speed_at_transducer(self) -> int: ...

    def set_maximum_port_swath_width(self, arg: int, /) -> None:
        """in meter"""

    def get_maximum_port_swath_width(self) -> int:
        """in meter"""

    def set_beam_spacing(self, arg: int, /) -> None: ...

    def get_beam_spacing(self) -> int: ...

    def set_maximum_port_coverage(self, arg: int, /) -> None:
        """in degrees"""

    def get_maximum_port_coverage(self) -> int:
        """in degrees"""

    def set_yaw_and_pitch_stabilization_mode(self, arg: int, /) -> None: ...

    def get_yaw_and_pitch_stabilization_mode(self) -> int: ...

    def set_maximum_starboard_coverage(self, arg: int, /) -> None:
        """in degrees"""

    def get_maximum_starboard_coverage(self) -> int:
        """in degrees"""

    def set_maximum_starboard_swath_width(self, arg: int, /) -> None:
        """in meter"""

    def get_maximum_starboard_swath_width(self) -> int:
        """in meter"""

    def set_transmit_along_tilt(self, arg: int, /) -> None:
        """in 0.1 degree"""

    def get_transmit_along_tilt(self) -> int:
        """in 0.1 degree"""

    def set_filter_identifier2(self, arg: int, /) -> None: ...

    def get_filter_identifier2(self) -> int: ...

    def get_absorption_coefficient_in_db_per_meter(self) -> float:
        """
        Get the absorption coefficient in db per meter

        Returns:
            _absorption_coefficient * 0.00001f (float)
        """

    def get_transmit_pulse_length_in_seconds(self) -> float:
        """
        Get the transmit pulse length in seconds

        Returns:
            _transmit_pulse_length * 0.000001f (float)
        """

    def get_transmit_beamwidth_in_degrees(self) -> float:
        """
        Get the transmit beamwidth in degrees

        Returns:
            _transmit_beamwidth * 0.1f (float)
        """

    def get_receive_beamwidth_in_degrees(self) -> float:
        """
        Get the receive beamwidth in degrees

        Returns:
            _receive_beamwidth_degree * 0.1f (float)
        """

    def get_receive_bandwidth_in_hertz(self) -> float:
        """
        Get the receive bandwidth in Hz

        Returns:
            _receive_bandwidth_50hz * 50.f (float)
        """

    def get_transmit_along_tilt_in_degrees(self) -> float:
        """
        Get the transmit along tilt in degrees

        Returns:
            _transmit_along_tilt * 0.1f (float)
        """

    def get_mode_as_ping_mode(self, unhandled_message: str | None = None) -> str | None:
        """
        Retrieves Ping mode decoded in the 'mode' variable.

        The decoding is EM model specific. See datagram format specification
        for details.

        Args:
            unhandled_message: If provided, this message is used as the return
                               value if the mode is not handled for the
                               specific system. Otherwise: None is returned

        Returns:
            A string representing Ping mode as encoded by 'mode'
        """

    def get_mode_as_tx_pulse_form(self, unhandled_message: str | None = None) -> str | None:
        """
        Retrieves Tx pulse form encoded in the mode variable

        The decoding is EM model specific. See datagram format specification
        for details.

        Args:
            unhandled_message: If provided, this message is used as the return
                               value if the mode is not handled for the
                               specific system. Otherwise: None is returned.

        Returns:
            A string representing Tx pulse form as encoded by 'mode'
        """

    def get_mode_as_dual_swath_mode(self, unhandled_message: str | None = None) -> str | None:
        """
        Retrieves Dual swath mode encoded in the mode variable

        The decoding is EM model specific. See datagram format specification
        for details.

        Args:
            unhandled_message: If provided, this message is used as the return
                               value if the mode is not handled for the
                               specific system. Otherwise: None is returned

        Returns:
            A string representing Tx pulse form as encoded by 'mode'
        """

    def get_mode2_as_rx_or_sonar_head_use(self, unhandled_message: str | None = None) -> str | None:
        """
        Retrieves Rx array/ sonar head encoded in the mode2 variable

        The decoding is EM model specific. Currently only outputs sensefull
        values for EM2040 and EM2040C. See datagram format specification for
        details.

        Args:
            unhandled_message: If provided, this message is used as the return
                               value if the mode is not handled for the
                               specific system. Otherwise: 'None' is returned

        Returns:
            A string representing Rx array / Sonar head use as encoded by
            'mode2'
        """

    def get_mode2_as_pulselength(self, unhandled_message: str | None = None) -> str | None:
        """
        Retrieves Pulselength encoded in the mode2 variable

        The decoding is EM model specific. Currently only outputs sensefull
        values for EM2040 and EM2040C. See datagram format specification for
        details.

        Args:
            unhandled_message: If provided, this message is used as the return
                               value if the mode is not handled for the
                               specific system. Otherwise: 'Sonar head use
                               unhandled' is returned

        Returns:
            A string representing Pulselength as encoded by 'mode2'
        """

    def get_mode2_as_receive_fixed_gain_setting_dB(self, unhandled_value: int | None = None) -> int | None:
        """
        Retrieves receiver fixed gain setting encoded in the mode2 variable

        The decoding is EM model specific. This only outputs sensefull values
        for EM2000, EM1002, EM3000, EM3002, EM300, EM120. See datagram format
        specification for details.

        Args:
            unhandled_value: If provided, this value is used as the return
                             value if the mode is not handled for the specific
                             system. Otherwise: 'None' is returned

        Returns:
            A uint8_t representing receiver fixed gain setting use as encoded
            by 'mode2'
        """

    def get_filter_identifier_as_spike_filter(self) -> str:
        """
        Retrieves spike filter setup encoded in the filter_identifier variable

        Returns:
            A string representing the spike filter setup as encoded by
            'filter_identifier'
        """

    def get_filter_identifier_as_slope_filter(self) -> str:
        """
        Retrieves slope filter status encoded in the filter_identifier
        variable

        Returns:
            A string representing the slope filter status (On or Off) as
            encoded by 'filter_identifier'
        """

    def get_filter_identifier_as_range_gates_size(self, unhandled_message: str | None = None) -> str | None:
        """
        Retrieves Range gates size encoded in the mode variable

        Args:
            unhandled_message: If provided, this message is used as the return
                               value if the range gates size is not handled by
                               the function. Otherwise: 'None' is returned

        Returns:
            A string representing Range gates size as encoded by 'mode'
        """

    def get_filter_identifier_as_aeration_filter(self) -> str:
        """
        Retrieves the Aearation filter status encoded in the filter_identifier
        variable

        Returns:
            A string representing the Aeration filter status (On or Off) as
            encoded by 'filter_identifier'
        """

    def get_filter_identifier_as_interference_filter(self) -> str:
        """
        Retrieves the Interference filter status encoded in the
        filter_identifier variable

        Returns:
            A string representing the Interference filter status (On or Off)
            as encoded by 'filter_identifier'
        """

    def get_filter_identifier2_as_penetration_filter(self) -> str:
        """
        Retrieves penetration filter setup encoded in the filter_identifier2
        variable

        Returns:
            A string representing the penetration filter setup as encoded by
            'filter_identifier2'
        """

    def get_filter_identifier2_as_detect_mode(self) -> str:
        """
        Retrieves detect mode encoded in the filter_identifier2 variable

        Returns:
            A string representing the detect mode as encoded by
            'filter_identifier2'
        """

    def get_filter_identifier2_as_phase_ramp(self, unhandled_message: str | None = None) -> str | None:
        """
        Retrieves phase ramp encoded in the filter_identifier2 variable

        Args:
            unhandled_message: If provided, this message is used as the return
                               value if the value is not handled by the
                               function. Otherwise: 'None' is returned

        Returns:
            A string representing the phase ramp encoded by
            'filter_identifier2'
        """

    def get_filter_identifier2_as_special_tvg(self) -> str:
        """
        Retrieves the Special TVG mode encoded in the filter_identifier2
        variable

        Returns:
            A string representing the Special TVG mode (Normal/Special) as
            encoded by 'filter_identifier2'
        """

    def get_filter_identifier2_as_special_amp_detect(self) -> str:
        """
        Retrieves the Special amp detect mode encoded in the
        filter_identifier2 variable

        EM3002 soft sediment detection = special amp detect

        Returns:
            A string representing the Special amp detect mode (Normal/Special)
            as encoded by 'filter_identifier2'
        """

    def get_source_of_sound_speed_at_transducer_as_string(self, unhandled_message: str | None = None) -> str | None:
        """
        Retrieves the source of sound speed at transducer encoded in the
        'source of sound speed at transducer' variable

        Args:
            unhandled_message: If provided, this message is used as the return
                               value if the source of sound speed at
                               transducer mode specified is not handled.

        Returns:
            A string representing the source of sound speed at transducer as
            encoded by the 'source of sound speed at transducer' variable
        """

    @overload
    def get_sonar_mode_enabled(self) -> bool:
        """
        Retrieves the Sonar mode option (On/Off) encoded in the 'source of
        sound speed at transducer' variable

        Returns:
            True if the Sonar mode option is enabled, false otherwise
        """

    @overload
    def get_sonar_mode_enabled(self) -> bool: ...

    def get_passive_mode_enabled(self) -> bool:
        """
        Retrieves the Passive mode option (On/Off) encoded in the 'source of
        sound speed at transducer' variable

        Returns:
            True if the Passive mode option is enabled, false otherwise
        """

    def get_3d_scanning_enabled(self) -> bool:
        """
        Retrieves the 3D scanning option (On/Off) encoded in the 'source of
        sound speed at transducer' variable

        Returns:
            True if the 3D scanning option is enabled, false otherwise
        """

    def get_beam_spacing_as_string(self, unhandled_message: str | None = None) -> str | None:
        """
        Retrieves beamspacing mode encoded in the beamspacing variable

        The decoding is EM model specific. Currently only outputs sensefull
        values for EM2040 and EM2040C. See datagram format specification for
        details.

        Args:
            unhandled_message: If provided, this message is used as the return
                               value if the mode is not handled for the
                               specific system. Otherwise: 'None' is returned

        Returns:
            A string representing beamspacing as encoded by 'beamspacing'
        """

    def get_yaw_and_pitch_stabilization_mode_as_yaw_stabilization(self) -> str:
        """
        Retrieves yaw and pitch stabilization mode encoded in the
        yaw_and_pitch_stabilization_mode variable

        Returns:
            A string representing yaw_and_pitch_stabilization_mode as encoded
            by 'yaw_and_pitch_stabilization_mode'
        """

    def get_yaw_and_pitch_stabilization_mode_as_heading_filter(self, unhandled_message: str | None = None) -> str | None:
        """
        Retrieves heading filter mode encoded in the
        yaw_and_pitch_stabilization_mode variable

        Args:
            unhandled_message: If provided, this message is used as the return
                               value if the mode is not handled by the
                               function. Otherwise: 'None' is returned

        Returns:
            A string representing heading filter mode as encoded by
            'yaw_and_pitch_stabilization_mode'
        """

    def get_yaw_and_pitch_stabilization_mode_as_pitch_stibilization(self) -> str:
        """
        Retrieves pitch stabilization mode (on/off) encoded in the
        yaw_and_pitch_stabilization_mode variable

        Returns:
            A string representing pitch stabilization mode as encoded by
            'yaw_and_pitch_stabilization_mode'
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: RuntimeParameters) -> bool: ...

    def hash_content_only(self) -> int: ...

    def copy(self) -> RuntimeParameters:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RuntimeParameters: ...

    def __deepcopy__(self, arg: dict, /) -> RuntimeParameters: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RuntimeParameters:
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

class ExtraParameters_t_ContentIdentifier(enum.Enum):
    CalibTxt = 1
    """Calib.txt file for angle offset"""

    LogAllHeights = 2
    """Log of all heights"""

    SoundVelocityAtTransducer = 3
    """Sound velocity at transducer"""

    SoundVelocityProfile = 4
    """Sound velocity profile"""

    MultiCastInputStatus = 5
    """Multicast input status"""

    Bscorr = 6
    """Bscorr.txt file"""

class o_ExtraParameters_t_ContentIdentifier:
    """
    Helper class to convert between strings and enum values of type 't_ContentIdentifier'
    """

    @overload
    def __init__(self, value: ExtraParameters_t_ContentIdentifier = ExtraParameters_t_ContentIdentifier.CalibTxt) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> ExtraParameters_t_ContentIdentifier:
        """enum value"""

    @value.setter
    def value(self, arg: ExtraParameters_t_ContentIdentifier, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.ExtraParameters_t_ContentIdentifier = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_ExtraParameters_t_ContentIdentifier, /) -> bool: ...

    @overload
    def __eq__(self, arg: ExtraParameters_t_ContentIdentifier, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_ExtraParameters_t_ContentIdentifier:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_ExtraParameters_t_ContentIdentifier: ...

    def __deepcopy__(self, arg: dict, /) -> o_ExtraParameters_t_ContentIdentifier: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_ExtraParameters_t_ContentIdentifier:
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

class ExtraParameters(KongsbergAllDatagram):
    def __init__(self) -> None: ...

    def set_ping_counter(self, arg: int, /) -> None: ...

    def get_ping_counter(self) -> int: ...

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_content_identifier(self, arg: ExtraParameters_t_ContentIdentifier, /) -> None: ...

    def get_content_identifier(self) -> ExtraParameters_t_ContentIdentifier: ...

    def set_raw_content(self, arg: str, /) -> None:
        """depends on the content identifier"""

    def get_raw_content(self) -> str:
        """depends on the content identifier"""

    def get_spare(self) -> int: ...

    def set_spare(self, arg: int, /) -> None: ...

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: ExtraParameters) -> bool: ...

    def copy(self) -> ExtraParameters:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ExtraParameters: ...

    def __deepcopy__(self, arg: dict, /) -> ExtraParameters: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ExtraParameters:
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

class PUStatusOutput(KongsbergAllDatagram):
    """
    The PU Status datagram is sent out every second if requested by the
    host processor. It has two functions, to indicate that the system is
    alive and receiving sensor data, and to give sensor data regularly for
    a potential screen update.
    """

    def __init__(self) -> None: ...

    def set_status_datagram_counter(self, arg: int, /) -> None: ...

    def get_status_datagram_counter(self) -> int: ...

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_ping_rate(self, arg: int, /) -> None:
        """in 0.01 Hz"""

    def get_ping_rate(self) -> int:
        """in 0.01 Hz"""

    def set_ping_counter(self, arg: int, /) -> None:
        """of latest ping"""

    def get_ping_counter(self) -> int:
        """of latest ping"""

    def set_distance_between_swath(self, arg: int, /) -> None:
        """in 10%"""

    def get_distance_between_swath(self) -> int:
        """in 10%"""

    def set_sensor_input_status_udp_port_2(self, arg: int, /) -> None: ...

    def get_sensor_input_status_udp_port_2(self) -> int: ...

    def set_sensor_input_status_serial_port_1(self, arg: int, /) -> None: ...

    def get_sensor_input_status_serial_port_1(self) -> int: ...

    def set_sensor_input_status_serial_port_2(self, arg: int, /) -> None: ...

    def get_sensor_input_status_serial_port_2(self) -> int: ...

    def set_sensor_input_status_serial_port_3(self, arg: int, /) -> None: ...

    def get_sensor_input_status_serial_port_3(self) -> int: ...

    def set_sensor_input_status_serial_port_4(self, arg: int, /) -> None: ...

    def get_sensor_input_status_serial_port_4(self) -> int: ...

    def set_pps_status(self, arg: int, /) -> None: ...

    def get_pps_status(self) -> int: ...

    def set_position_status(self, arg: int, /) -> None: ...

    def get_position_status(self) -> int: ...

    def set_attitude_status(self, arg: int, /) -> None: ...

    def get_attitude_status(self) -> int: ...

    def set_clock_status(self, arg: int, /) -> None: ...

    def get_clock_status(self) -> int: ...

    def set_heading_status(self, arg: int, /) -> None: ...

    def get_heading_status(self) -> int: ...

    def set_pu_status(self, arg: int, /) -> None: ...

    def get_pu_status(self) -> int: ...

    def set_last_received_heading(self, arg: int, /) -> None:
        """in 0.01 degree"""

    def get_last_received_heading(self) -> int:
        """in 0.01 degree"""

    def set_last_received_roll(self, arg: int, /) -> None:
        """in 0.01 degree"""

    def get_last_received_roll(self) -> int:
        """in 0.01 degree"""

    def set_last_received_pitch(self, arg: int, /) -> None:
        """in 0.01 degree"""

    def get_last_received_pitch(self) -> int:
        """in 0.01 degree"""

    def set_last_received_heave_at_sonar_head(self, arg: int, /) -> None:
        """in cm"""

    def get_last_received_heave_at_sonar_head(self) -> int:
        """in cm"""

    def set_sound_speed_at_transducer(self, arg: int, /) -> None:
        """in dm/s"""

    def get_sound_speed_at_transducer(self) -> int:
        """in dm/s"""

    def set_last_received_depth(self, arg: int, /) -> None:
        """in cm"""

    def get_last_received_depth(self) -> int:
        """in cm"""

    def set_along_ship_velocity(self, arg: int, /) -> None:
        """in cm/s"""

    def get_along_ship_velocity(self) -> int:
        """in cm/s"""

    def set_attitude_velocity_sensor_status(self, arg: int, /) -> None: ...

    def get_attitude_velocity_sensor_status(self) -> int: ...

    def set_mammal_protection_ramp(self, arg: int, /) -> None: ...

    def get_mammal_protection_ramp(self) -> int: ...

    def set_backscatter_at_oblique_angle(self, arg: int, /) -> None:
        """in dB"""

    def get_backscatter_at_oblique_angle(self) -> int:
        """in dB"""

    def set_backscatter_at_normal_incidence(self, arg: int, /) -> None:
        """in dB"""

    def get_backscatter_at_normal_incidence(self) -> int:
        """in dB"""

    def set_fixed_gain(self, arg: int, /) -> None:
        """in dB"""

    def get_fixed_gain(self) -> int:
        """in dB"""

    def set_depth_to_normal_incidence(self, arg: int, /) -> None:
        """in m"""

    def get_depth_to_normal_incidence(self) -> int:
        """in m"""

    def set_range_to_normal_incidence(self, arg: int, /) -> None:
        """in m"""

    def get_range_to_normal_incidence(self) -> int:
        """in m"""

    def set_port_coverage(self, arg: int, /) -> None:
        """in degrees"""

    def get_port_coverage(self) -> int:
        """in degrees"""

    def set_starboard_coverage(self, arg: int, /) -> None:
        """in degrees"""

    def get_starboard_coverage(self) -> int:
        """in degrees"""

    def set_sound_speed_at_transducer_from_profile(self, arg: int, /) -> None:
        """in dm/s"""

    def get_sound_speed_at_transducer_from_profile(self) -> int:
        """in dm/s"""

    def set_yaw_stabilization_angle(self, arg: int, /) -> None:
        """in 0.01 degree, or tilt used at 3D scanning"""

    def get_yaw_stabilization_angle(self) -> int:
        """in 0.01 degree, or tilt used at 3D scanning"""

    def set_across_ship_velocity(self, arg: int, /) -> None:
        """in cm/s (or port coverage or spare)"""

    def get_across_ship_velocity(self) -> int:
        """in cm/s (or port coverage or spare)"""

    def set_downward_velocity(self, arg: int, /) -> None:
        """in cm/s (or starboard coverage or spare)"""

    def get_downward_velocity(self) -> int:
        """in cm/s (or starboard coverage or spare)"""

    def set_em2040_cpu_temperature(self, arg: int, /) -> None:
        """in degree Celsius (or spare)"""

    def get_em2040_cpu_temperature(self) -> int:
        """in degree Celsius (or spare)"""

    def get_ping_rate_hertz(self) -> float:
        """
        Get the ping rate in Hz

        Returns:
            _ping_rate * 0.01 Hz (float)
        """

    def get_distance_between_swath_in_percent(self) -> float:
        """
        Get the distance between swath in percent

        Returns:
            _distance_between_swath * 0.1f (float )
        """

    def get_last_received_heading_in_degrees(self) -> float:
        """
        Get the last received heading in degrees

        Returns:
            _last_received_heading * 0.01f (float )
        """

    def get_last_received_roll_in_degrees(self) -> float:
        """
        Get the last received roll in degrees

        Returns:
            _last_received_roll * 0.01f (float )
        """

    def get_last_received_pitch_in_degrees(self) -> float:
        """
        Get the last received pitch in degrees

        Returns:
            _last_received_pitch * 0.01f (float )
        """

    def get_sound_speed_at_transducer_in_meters_per_second(self) -> float:
        """
        Get the last received heave at sonar head in meters per second

        Returns:
            _sound_speed_at_transducer * 0.1f (float )
        """

    def get_last_received_depth_in_meters(self) -> float:
        """
        Get the last received depth in meters

        Returns:
            _last_received_depth * 0.01f (float )
        """

    def get_along_ship_velocity_in_meters_per_second(self) -> float:
        """
        Get the along ship velocity in m/s

        Returns:
            _along_ship_velocity * 0.01f (float )
        """

    def get_sound_speed_at_transducer_from_profile_in_meters_per_second(self) -> float:
        """
        Get the sound speed at transducer (derived from profile) in m/s

        Returns:
            _sound_speed_at_transducer_from_profile * 0.1f (float )
        """

    def get_yaw_stabilization_angle_in_degrees(self) -> float:
        """
        Get the yaw stabilization angle in degrees

        Returns:
            _yaw_stabilization_angle * 0.01f (float )
        """

    def get_across_ship_velocity_in_meters_per_second(self) -> float:
        """
        Get the across ship velocity in m/s

        Returns:
            _across_ship_velocity * 0.01f (float )
        """

    def get_downward_velocity_in_meters_per_second(self) -> float:
        """
        Get the downward velocity in m/s

        Returns:
            _downward_velocity * 0.01f (float )
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: PUStatusOutput) -> bool: ...

    def copy(self) -> PUStatusOutput:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> PUStatusOutput: ...

    def __deepcopy__(self, arg: dict, /) -> PUStatusOutput: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> PUStatusOutput:
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

class PUIDOutput(KongsbergAllDatagram):
    """
    The PU Status datagram is sent out every second if requested by the
    host processor. It has two functions, to indicate that the system is
    alive and receiving sensor data, and to give sensor data regularly for
    a potential screen update.
    """

    def __init__(self) -> None: ...

    def set_byte_order_flag(self, arg: int, /) -> None: ...

    def get_byte_order_flag(self) -> int: ...

    def set_system_serial_number(self, arg: int, /) -> None: ...

    def get_system_serial_number(self) -> int: ...

    def set_udp_port_no_1(self, arg: int, /) -> None: ...

    def get_udp_port_no_1(self) -> int: ...

    def set_udp_port_no_2(self, arg: int, /) -> None: ...

    def get_udp_port_no_2(self) -> int: ...

    def set_udp_port_no_3(self, arg: int, /) -> None: ...

    def get_udp_port_no_3(self) -> int: ...

    def set_udp_port_no_4(self, arg: int, /) -> None: ...

    def get_udp_port_no_4(self) -> int: ...

    def set_system_descriptor(self, arg: int, /) -> None: ...

    def get_system_descriptor(self) -> int: ...

    def set_pu_software_version(self, arg: str, /) -> None: ...

    def get_pu_software_version(self) -> str: ...

    def set_bsp_software_date(self, arg: str, /) -> None: ...

    def get_bsp_software_date(self) -> str: ...

    def set_sonar_transceiver_1_software_version(self, arg: str, /) -> None: ...

    def get_sonar_transceiver_1_software_version(self) -> str: ...

    def set_sonar_transceiver_2_software_version(self, arg: str, /) -> None: ...

    def get_sonar_transceiver_2_software_version(self) -> str: ...

    def set_host_ip_address(self, arg: typing.Any, /) -> None: ...

    def get_host_ip_address(self) -> typing.Any: ...

    def set_tx_opening_angle(self, arg: int, /) -> None: ...

    def get_tx_opening_angle(self) -> int: ...

    def set_rx_opening_angle(self, arg: int, /) -> None: ...

    def get_rx_opening_angle(self) -> int: ...

    def set_spare(self, arg: typing.Any, /) -> None: ...

    def get_spare(self) -> typing.Any: ...

    def get_host_ip_address_as_string(self) -> str:
        """
        Get the host ip address as string

        Returns:
            std::string
        """

    def get_cpu_configuration(self) -> str:
        """
        Convert the system descriptor flag to a cpu configuration

        Returns:
            std::string
        """

    def get_has_dual_head(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system is a
        dual head system

        Returns:
            true false
        """

    def get_has_dual_swath(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system is a
        dual swath system

        Returns:
            true false
        """

    def get_has_bsp67B(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system is a
        BSP67B system

        This means it is not a CBMF system

        Returns:
            true false
        """

    def get_has_cbmf(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system is a
        CBMF system

        This means it is not a BSP67B system

        Returns:
            true false
        """

    def get_has_ptp_support(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system is a
        PTP (IEEE 1588 clock sync) support

        Returns:
            true false
        """

    def get_has_deep_water_sonar_head(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system has a
        deep water sonar head

        Returns:
            true (deep water sonar head) false (shallow water sonar head)s
        """

    def get_has_shallow_water_sonar_head(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system has a
        shallow water sonar head

        Returns:
            true (shallow water sonar head) false (deep water sonar head)
        """

    def get_has_extra_detections_support(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system has
        extra detections support

        Returns:
            true false
        """

    def get_has_rs422_support(self) -> bool:
        """
        Evaluate the system_descriptor flag to determine if the system has
        RS422 serial lines support

        Returns:
            true false
        """

    def get_which_em2040(self) -> str:
        """
        Evaluate the system_descriptor flag to determine the em2040 flag

        Returns:
            true false
        """

    def get_which_em710(self) -> str:
        """
        Evaluate the system_descriptor flag to determine the EM710 flag

        Returns:
            true false
        """

    def get_which_old_sounder(self) -> str:
        """
        Evaluate the system_descriptor flag to determine the old sounder flag

        Returns:
            true false
        """

    def get_etx(self) -> int:
        """end identifier (always 0x03)"""

    def set_etx(self, arg: int, /) -> None:
        """end identifier (always 0x03)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, arg: int, /) -> None: ...

    def __eq__(self, other: PUIDOutput) -> bool: ...

    def copy(self) -> PUIDOutput:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> PUIDOutput: ...

    def __deepcopy__(self, arg: dict, /) -> PUIDOutput: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> PUIDOutput:
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
