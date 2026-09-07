"""Teledyne RESON .s7k (7k) datagram (record) classes"""

from collections.abc import Iterable, Iterator, Sequence
import enum
from typing import Annotated, Final, overload

import numpy
from numpy.typing import NDArray

import themachinethatgoesping.echosounders_nanopy.s7k


class S7KDatagram:
    """
    The Data Record Frame (DRF) is the header/wrapper that precedes every
    7k record.

    This class implements the fixed 64-byte DRF header as defined in the
    "7k Data Format Definition" specification (v3.12, April 2020), Table
    5. All multibyte fields are stored in little-endian byte order. A
    record consists of: DRF header + record type header (RTH) + (optional)
    record data + (optional) optional data + checksum.
    """

    def __init__(self) -> None: ...

    def get_protocol_version(self) -> int:
        """offset 0: protocol version of this frame (e.g. 5)"""

    def get_offset(self) -> int:
        """offset 2: bytes from start of sync pattern to RTH"""

    def get_sync_pattern(self) -> int:
        """offset 4: 0x0000FFFF"""

    def get_size(self) -> int:
        """
        offset 8: total record size (version field to end of checksum,
        including embedded data)
        """

    def get_optional_data_offset(self) -> int:
        """offset 12: byte offset to optional data (0 = none)"""

    def get_optional_data_identifier(self) -> int:
        """offset 16: identifier for the optional data field"""

    def get_year(self) -> int:
        """offset 20: UTC year (all four digits, e.g. 2023)"""

    def get_day(self) -> int:
        """offset 22: UTC day of year (1-366)"""

    def get_seconds(self) -> float:
        """offset 24: UTC seconds (0.0 - 60.0)"""

    def get_hours(self) -> int:
        """offset 28: UTC hours (0-23)"""

    def get_minutes(self) -> int:
        """offset 29: UTC minutes (0-59)"""

    def get_record_version(self) -> int:
        """offset 30: record version (currently 1)"""

    def get_record_type_identifier(self) -> int: ...

    def get_device_identifier(self) -> int:
        """offset 36: device identifier"""

    def get_system_enumerator(self) -> int:
        """offset 42: enumerator differentiating devices with same id"""

    def get_flags(self) -> int:
        """offset 48: bit field (bit 0: checksum valid, bit 15: recorded data)"""

    def get_flag_checksum_is_valued(self) -> bool:
        """Test if the flags field indicates a valid checksum (bit 0)."""

    def get_flag_data_live_or_recorded(self) -> bool:
        """Test if the flags field indicates live or recorded data (bit 15)."""

    def drf_sync_pattern_is_valid(self) -> bool:
        """Test if the DRF sync pattern is valid."""

    def get_datagram_identifier(self) -> themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier: ...

    def compute_size_content(self) -> int:
        """
        Number of bytes of the record following the DRF header (RTH + data +
        checksum).
        """

    def get_timestamp(self) -> float:
        """
        Get the record timestamp as unix time (seconds since 1970-01-01 UTC).
        Returns:
            Unix timestamp, or NaN if no time is available (all 7KTIME fields
            zero).
        """

    def get_datetime(self, timezone_offset_hours: float = 0.0) -> object:
        """Return the timestamp as datetime object"""

    def get_date_string(self, fractional_seconds_digits: int = 2, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str:
        """
        Get the timestamp as a formatted date string.
        Args:
            fractionalSecondsDigits: number of fractional-second digits
            format: date format string

        Returns:
            Formatted date string.
        """

    @staticmethod
    def compute_checksum_static(arg: bytes, /) -> int:
        """
        Compute the 7k record checksum of a serialized datagram (debugging
        aid).

        Pass the full serialized record (e.g. the result of to_binary()). The
        last four bytes are treated as the stored checksum and are excluded
        from the sum.

        Args:
            buffer: Serialized record bytes (DRF + RTH + data + checksum).

        Returns:
            Computed 32-bit checksum (sum of all bytes except the trailing
            four).
        """

    def compute_checksum(self) -> int:
        """
        Compute the 7k record checksum of a serialized datagram (debugging
        aid).

        Pass the full serialized record (e.g. the result of to_binary()). The
        last four bytes are treated as the stored checksum and are excluded
        from the sum.

        Args:
            buffer: Serialized record bytes (DRF + RTH + data + checksum).

        Returns:
            Computed 32-bit checksum (sum of all bytes except the trailing
            four).
        """

    @staticmethod
    def checksum_is_correct_static(arg: bytes, /) -> bool:
        """
        Check whether the stored checksum of a serialized record matches its
        computed checksum (debugging aid).

        Args:
            buffer: Serialized record bytes (DRF + RTH + data + checksum).

        Returns:
            true if compute_checksum(buffer) == read_checksum(buffer).
        """

    def test_checksum_is_correct(self) -> bool:
        """
        Check whether the stored checksum of a serialized record matches its
        computed checksum (debugging aid).

        Args:
            buffer: Serialized record bytes (DRF + RTH + data + checksum).

        Returns:
            true if compute_checksum(buffer) == read_checksum(buffer).
        """

    def __eq__(self, other: S7KDatagram) -> bool: ...

    def copy(self) -> S7KDatagram:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagram: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagram: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> S7KDatagram:
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

class S7KUnknown(S7KDatagram):
    """
    A generic 7k datagram that stores the raw (unparsed) content of a
    record.

    This is used to represent any 7k record whose specific record type is
    not (yet) implemented. It holds the DRF header (via the S7KDatagram
    base) and the raw bytes of the record content (record type header +
    record data + optional data + checksum).
    """

    def __init__(self) -> None: ...

    def get_raw_content(self) -> str:
        """raw bytes of the record following the DRF header"""

    def set_raw_content(self, value: str) -> None:
        """raw bytes of the record following the DRF header"""

    def __eq__(self, other: S7KUnknown) -> bool: ...

    def copy(self) -> S7KUnknown:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KUnknown: ...

    def __deepcopy__(self, arg: dict, /) -> S7KUnknown: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> S7KUnknown:
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

class SnippetDataBeam:
    def __init__(self) -> None: ...

    def get_beam_descriptor(self) -> int: ...

    def set_beam_descriptor(self, val: int) -> None: ...

    def get_snippet_start(self) -> int: ...

    def set_snippet_start(self, val: int) -> None: ...

    def get_detection_sample(self) -> int: ...

    def set_detection_sample(self, val: int) -> None: ...

    def get_snippet_end(self) -> int: ...

    def set_snippet_end(self, val: int) -> None: ...

    def get_number_of_samples(self) -> int:
        """
        number of intensity samples in this beam's snippet (snippet_end -
        snippet_start + 1)
        """

    def __eq__(self, other: SnippetDataBeam) -> bool: ...

    def copy(self) -> SnippetDataBeam:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SnippetDataBeam: ...

    def __deepcopy__(self, arg: dict, /) -> SnippetDataBeam: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SnippetDataBeams_vector:
    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, arg: SnippetDataBeams_vector, /) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, arg: Iterable[SnippetDataBeam], /) -> None:
        """Construct from an iterable object"""

    def __len__(self) -> int: ...

    def __bool__(self) -> bool:
        """Check whether the vector is nonempty"""

    def __repr__(self) -> str: ...

    def __iter__(self) -> Iterator[SnippetDataBeam]: ...

    @overload
    def __getitem__(self, arg: int, /) -> SnippetDataBeam: ...

    @overload
    def __getitem__(self, arg: slice, /) -> SnippetDataBeams_vector: ...

    def clear(self) -> None:
        """Remove all items from list."""

    def append(self, arg: SnippetDataBeam, /) -> None:
        """Append ``arg`` to the end of the list."""

    def insert(self, arg0: int, arg1: SnippetDataBeam, /) -> None:
        """Insert object ``arg1`` before index ``arg0``."""

    def pop(self, index: int = -1) -> SnippetDataBeam:
        """Remove and return item at ``index`` (default last)."""

    def extend(self, arg: SnippetDataBeams_vector, /) -> None:
        """Extend ``self`` by appending elements from ``arg``."""

    @overload
    def __setitem__(self, arg0: int, arg1: SnippetDataBeam, /) -> None: ...

    @overload
    def __setitem__(self, arg0: slice, arg1: SnippetDataBeams_vector, /) -> None: ...

    @overload
    def __delitem__(self, arg: int, /) -> None: ...

    @overload
    def __delitem__(self, arg: slice, /) -> None: ...

    def __eq__(self, arg: object, /) -> bool: ...

    def __ne__(self, arg: object, /) -> bool: ...

    @overload
    def __contains__(self, arg: SnippetDataBeam, /) -> bool: ...

    @overload
    def __contains__(self, arg: object, /) -> bool: ...

    def count(self, arg: SnippetDataBeam, /) -> int:
        """Return number of occurrences of ``arg``."""

    def remove(self, arg: SnippetDataBeam, /) -> None:
        """Remove first occurrence of ``arg``."""

class SnippetDataBeamContainer:
    def __init__(self) -> None: ...

    @property
    def beams(self) -> list[SnippetDataBeam]: ...

    @beams.setter
    def beams(self, arg: Sequence[SnippetDataBeam], /) -> None: ...

    def get_beam_descriptor_tensor(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]: ...

    def get_snippet_start_tensor(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_detection_sample_tensor(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_snippet_end_tensor(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_number_of_samples_tensor(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_number_of_beams(self) -> int: ...

    def get_total_number_of_samples(self) -> int: ...

    def __eq__(self, other: SnippetDataBeamContainer) -> bool: ...

    def copy(self) -> SnippetDataBeamContainer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SnippetDataBeamContainer: ...

    def __deepcopy__(self, arg: dict, /) -> SnippetDataBeamContainer: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SnippetDataAmplitudes:
    def __init__(self) -> None: ...

    def get_samples_are_32bit(self) -> bool:
        """
        true if the intensity samples are stored as 32-bit values (else
        16-bit)
        """

    def get_number_of_beams(self) -> int: ...

    def get_total_number_of_samples(self) -> int: ...

    def get_samples_are_skipped(self) -> bool: ...

    def get_sample_position(self) -> int:
        """
        file position of the first sample byte (only valid if the samples were
        skipped)
        """

    def get_samples(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')] | Annotated[NDArray[numpy.uint32], dict(order='C')]:
        """flat samples of all beams (16- or 32-bit, concatenated over all beams)"""

    def get_beam_offsets(self) -> Annotated[NDArray[numpy.uint64], dict(order='C')]:
        """
        per-beam start offsets into the flat sample array (size =
        number_of_beams + 1)
        """

    def get_beam(self, beam_index: int) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        intensity samples of a single beam (as float, in the raw amplitude
        scale)
        """

    def get_beams(self) -> list[Annotated[NDArray[numpy.float32], dict(order='C')]]:
        """
        intensity samples of all beams as a list of arrays (one per beam, as float)
        """

    def get_beam_in_db(self, beam_index: int, db_offset: float = 0.0) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        intensity samples of a single beam in relative dB (20*log10(amplitude)
        + db_offset)
        """

    def get_beams_in_db(self, db_offset: float = 0.0) -> list[Annotated[NDArray[numpy.float32], dict(order='C')]]:
        """
        intensity samples of all beams in relative dB (20*log10(amplitude) + db_offset), one array per beam
        """

    def set_samples(self, samples: Annotated[NDArray[numpy.uint16], dict(order='C')] | Annotated[NDArray[numpy.uint32], dict(order='C')]) -> None: ...

    def set_beam_offsets(self, beam_offsets: Annotated[NDArray[numpy.uint64], dict(order='C')]) -> None: ...

    def __eq__(self, other: SnippetDataAmplitudes) -> bool: ...

    def copy(self) -> SnippetDataAmplitudes:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SnippetDataAmplitudes: ...

    def __deepcopy__(self, arg: dict, /) -> SnippetDataAmplitudes: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class RawDetectionBeam:
    def __init__(self) -> None: ...

    def get_beam_descriptor(self) -> int: ...

    def set_beam_descriptor(self, val: int) -> None: ...

    def get_detection_point(self) -> float: ...

    def set_detection_point(self, val: float) -> None: ...

    def get_rx_angle(self) -> float: ...

    def set_rx_angle(self, val: float) -> None: ...

    def get_flags(self) -> int: ...

    def set_flags(self, val: int) -> None: ...

    def get_quality(self) -> int: ...

    def set_quality(self, val: int) -> None: ...

    def get_uncertainty(self) -> float: ...

    def set_uncertainty(self, val: float) -> None: ...

    def get_signal_strength(self) -> float: ...

    def set_signal_strength(self, val: float) -> None: ...

    def get_min_limit(self) -> float: ...

    def set_min_limit(self, val: float) -> None: ...

    def get_max_limit(self) -> float: ...

    def set_max_limit(self, val: float) -> None: ...

    def __eq__(self, other: RawDetectionBeam) -> bool: ...

    def copy(self) -> RawDetectionBeam:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RawDetectionBeam: ...

    def __deepcopy__(self, arg: dict, /) -> RawDetectionBeam: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class RawDetectionBeams_vector:
    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, arg: RawDetectionBeams_vector, /) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, arg: Iterable[RawDetectionBeam], /) -> None:
        """Construct from an iterable object"""

    def __len__(self) -> int: ...

    def __bool__(self) -> bool:
        """Check whether the vector is nonempty"""

    def __repr__(self) -> str: ...

    def __iter__(self) -> Iterator[RawDetectionBeam]: ...

    @overload
    def __getitem__(self, arg: int, /) -> RawDetectionBeam: ...

    @overload
    def __getitem__(self, arg: slice, /) -> RawDetectionBeams_vector: ...

    def clear(self) -> None:
        """Remove all items from list."""

    def append(self, arg: RawDetectionBeam, /) -> None:
        """Append ``arg`` to the end of the list."""

    def insert(self, arg0: int, arg1: RawDetectionBeam, /) -> None:
        """Insert object ``arg1`` before index ``arg0``."""

    def pop(self, index: int = -1) -> RawDetectionBeam:
        """Remove and return item at ``index`` (default last)."""

    def extend(self, arg: RawDetectionBeams_vector, /) -> None:
        """Extend ``self`` by appending elements from ``arg``."""

    @overload
    def __setitem__(self, arg0: int, arg1: RawDetectionBeam, /) -> None: ...

    @overload
    def __setitem__(self, arg0: slice, arg1: RawDetectionBeams_vector, /) -> None: ...

    @overload
    def __delitem__(self, arg: int, /) -> None: ...

    @overload
    def __delitem__(self, arg: slice, /) -> None: ...

    def __eq__(self, arg: object, /) -> bool: ...

    def __ne__(self, arg: object, /) -> bool: ...

    @overload
    def __contains__(self, arg: RawDetectionBeam, /) -> bool: ...

    @overload
    def __contains__(self, arg: object, /) -> bool: ...

    def count(self, arg: RawDetectionBeam, /) -> int:
        """Return number of occurrences of ``arg``."""

    def remove(self, arg: RawDetectionBeam, /) -> None:
        """Remove first occurrence of ``arg``."""

class RawDetectionBeamContainer:
    def __init__(self) -> None: ...

    @property
    def beams(self) -> list[RawDetectionBeam]: ...

    @beams.setter
    def beams(self, arg: Sequence[RawDetectionBeam], /) -> None: ...

    def get_beam_descriptor_tensor(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]: ...

    def get_detection_point_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_rx_angle_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_flags_tensor(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_quality_tensor(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_uncertainty_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_signal_strength_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_min_limit_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_max_limit_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_rx_angle_in_degrees_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        receive steering angle of all beams in degrees (converted from
        radians)
        """

    def get_number_of_beams(self) -> int: ...

    def __eq__(self, other: RawDetectionBeamContainer) -> bool: ...

    def copy(self) -> RawDetectionBeamContainer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RawDetectionBeamContainer: ...

    def __deepcopy__(self, arg: dict, /) -> RawDetectionBeamContainer: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class AttitudeSample:
    def __init__(self) -> None: ...

    def get_delta_time(self) -> int: ...

    def set_delta_time(self, val: int) -> None: ...

    def get_roll(self) -> float: ...

    def set_roll(self, val: float) -> None: ...

    def get_pitch(self) -> float: ...

    def set_pitch(self, val: float) -> None: ...

    def get_heave(self) -> float: ...

    def set_heave(self, val: float) -> None: ...

    def get_heading(self) -> float: ...

    def set_heading(self, val: float) -> None: ...

    def __eq__(self, other: AttitudeSample) -> bool: ...

    def copy(self) -> AttitudeSample:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> AttitudeSample: ...

    def __deepcopy__(self, arg: dict, /) -> AttitudeSample: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class AttitudeSamples_vector:
    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, arg: AttitudeSamples_vector, /) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, arg: Iterable[AttitudeSample], /) -> None:
        """Construct from an iterable object"""

    def __len__(self) -> int: ...

    def __bool__(self) -> bool:
        """Check whether the vector is nonempty"""

    def __repr__(self) -> str: ...

    def __iter__(self) -> Iterator[AttitudeSample]: ...

    @overload
    def __getitem__(self, arg: int, /) -> AttitudeSample: ...

    @overload
    def __getitem__(self, arg: slice, /) -> AttitudeSamples_vector: ...

    def clear(self) -> None:
        """Remove all items from list."""

    def append(self, arg: AttitudeSample, /) -> None:
        """Append ``arg`` to the end of the list."""

    def insert(self, arg0: int, arg1: AttitudeSample, /) -> None:
        """Insert object ``arg1`` before index ``arg0``."""

    def pop(self, index: int = -1) -> AttitudeSample:
        """Remove and return item at ``index`` (default last)."""

    def extend(self, arg: AttitudeSamples_vector, /) -> None:
        """Extend ``self`` by appending elements from ``arg``."""

    @overload
    def __setitem__(self, arg0: int, arg1: AttitudeSample, /) -> None: ...

    @overload
    def __setitem__(self, arg0: slice, arg1: AttitudeSamples_vector, /) -> None: ...

    @overload
    def __delitem__(self, arg: int, /) -> None: ...

    @overload
    def __delitem__(self, arg: slice, /) -> None: ...

    def __eq__(self, arg: object, /) -> bool: ...

    def __ne__(self, arg: object, /) -> bool: ...

    @overload
    def __contains__(self, arg: AttitudeSample, /) -> bool: ...

    @overload
    def __contains__(self, arg: object, /) -> bool: ...

    def count(self, arg: AttitudeSample, /) -> int:
        """Return number of occurrences of ``arg``."""

    def remove(self, arg: AttitudeSample, /) -> None:
        """Remove first occurrence of ``arg``."""

class AttitudeSampleContainer:
    def __init__(self) -> None: ...

    @property
    def attitudes(self) -> list[AttitudeSample]: ...

    @attitudes.setter
    def attitudes(self, arg: Sequence[AttitudeSample], /) -> None: ...

    def get_delta_time_tensor(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]: ...

    def get_roll_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_pitch_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_heave_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_heading_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_number_of_attitudes(self) -> int: ...

    def get_delta_time_in_seconds_tensor(self) -> Annotated[NDArray[numpy.float64], dict(order='C')]: ...

    def get_heading_in_degrees_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_roll_in_degrees_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_pitch_in_degrees_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def __eq__(self, other: AttitudeSampleContainer) -> bool: ...

    def copy(self) -> AttitudeSampleContainer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> AttitudeSampleContainer: ...

    def __deepcopy__(self, arg: dict, /) -> AttitudeSampleContainer: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class FileHeaderDeviceInfo:
    def __init__(self) -> None: ...

    def get_device_identifier(self) -> int: ...

    def set_device_identifier(self, val: int) -> None: ...

    def get_system_enumerator(self) -> int: ...

    def set_system_enumerator(self, val: int) -> None: ...

    def __eq__(self, other: FileHeaderDeviceInfo) -> bool: ...

    def copy(self) -> FileHeaderDeviceInfo:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> FileHeaderDeviceInfo: ...

    def __deepcopy__(self, arg: dict, /) -> FileHeaderDeviceInfo: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class FileHeaderDeviceInfos_vector:
    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, arg: FileHeaderDeviceInfos_vector, /) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, arg: Iterable[FileHeaderDeviceInfo], /) -> None:
        """Construct from an iterable object"""

    def __len__(self) -> int: ...

    def __bool__(self) -> bool:
        """Check whether the vector is nonempty"""

    def __repr__(self) -> str: ...

    def __iter__(self) -> Iterator[FileHeaderDeviceInfo]: ...

    @overload
    def __getitem__(self, arg: int, /) -> FileHeaderDeviceInfo: ...

    @overload
    def __getitem__(self, arg: slice, /) -> FileHeaderDeviceInfos_vector: ...

    def clear(self) -> None:
        """Remove all items from list."""

    def append(self, arg: FileHeaderDeviceInfo, /) -> None:
        """Append ``arg`` to the end of the list."""

    def insert(self, arg0: int, arg1: FileHeaderDeviceInfo, /) -> None:
        """Insert object ``arg1`` before index ``arg0``."""

    def pop(self, index: int = -1) -> FileHeaderDeviceInfo:
        """Remove and return item at ``index`` (default last)."""

    def extend(self, arg: FileHeaderDeviceInfos_vector, /) -> None:
        """Extend ``self`` by appending elements from ``arg``."""

    @overload
    def __setitem__(self, arg0: int, arg1: FileHeaderDeviceInfo, /) -> None: ...

    @overload
    def __setitem__(self, arg0: slice, arg1: FileHeaderDeviceInfos_vector, /) -> None: ...

    @overload
    def __delitem__(self, arg: int, /) -> None: ...

    @overload
    def __delitem__(self, arg: slice, /) -> None: ...

    def __eq__(self, arg: object, /) -> bool: ...

    def __ne__(self, arg: object, /) -> bool: ...

    @overload
    def __contains__(self, arg: FileHeaderDeviceInfo, /) -> bool: ...

    @overload
    def __contains__(self, arg: object, /) -> bool: ...

    def count(self, arg: FileHeaderDeviceInfo, /) -> int:
        """Return number of occurrences of ``arg``."""

    def remove(self, arg: FileHeaderDeviceInfo, /) -> None:
        """Remove first occurrence of ``arg``."""

class FileHeaderDeviceInfoContainer:
    def __init__(self) -> None: ...

    @property
    def devices(self) -> list[FileHeaderDeviceInfo]: ...

    @devices.setter
    def devices(self, arg: Sequence[FileHeaderDeviceInfo], /) -> None: ...

    def get_device_identifier_tensor(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_system_enumerator_tensor(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]: ...

    def get_number_of_devices(self) -> int: ...

    def __eq__(self, other: FileHeaderDeviceInfoContainer) -> bool: ...

    def copy(self) -> FileHeaderDeviceInfoContainer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> FileHeaderDeviceInfoContainer: ...

    def __deepcopy__(self, arg: dict, /) -> FileHeaderDeviceInfoContainer: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class CompressedWaterColumnBeam:
    def __init__(self) -> None: ...

    def get_beam_number(self) -> int: ...

    def set_beam_number(self, val: int) -> None: ...

    def get_segment_number(self) -> int: ...

    def set_segment_number(self, val: int) -> None: ...

    def get_sample_count(self) -> int: ...

    def set_sample_count(self, val: int) -> None: ...

    def has_phase(self) -> bool:
        """whether this beam holds phase data"""

    def get_raw_magnitude(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]:
        """magnitude samples in their raw (unconverted) values, widened to uint32"""

    def get_raw_phase(self) -> Annotated[NDArray[numpy.int16], dict(order='C')]:
        """
        phase samples in their raw (unconverted) int16 values (empty if there
        is no phase)
        """

    def __eq__(self, other: CompressedWaterColumnBeam) -> bool: ...

    def copy(self) -> CompressedWaterColumnBeam:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> CompressedWaterColumnBeam: ...

    def __deepcopy__(self, arg: dict, /) -> CompressedWaterColumnBeam: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class CompressedWaterColumnBeams_vector:
    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, arg: CompressedWaterColumnBeams_vector, /) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, arg: Iterable[CompressedWaterColumnBeam], /) -> None:
        """Construct from an iterable object"""

    def __len__(self) -> int: ...

    def __bool__(self) -> bool:
        """Check whether the vector is nonempty"""

    def __repr__(self) -> str: ...

    def __iter__(self) -> Iterator[CompressedWaterColumnBeam]: ...

    @overload
    def __getitem__(self, arg: int, /) -> CompressedWaterColumnBeam: ...

    @overload
    def __getitem__(self, arg: slice, /) -> CompressedWaterColumnBeams_vector: ...

    def clear(self) -> None:
        """Remove all items from list."""

    def append(self, arg: CompressedWaterColumnBeam, /) -> None:
        """Append ``arg`` to the end of the list."""

    def insert(self, arg0: int, arg1: CompressedWaterColumnBeam, /) -> None:
        """Insert object ``arg1`` before index ``arg0``."""

    def pop(self, index: int = -1) -> CompressedWaterColumnBeam:
        """Remove and return item at ``index`` (default last)."""

    def extend(self, arg: CompressedWaterColumnBeams_vector, /) -> None:
        """Extend ``self`` by appending elements from ``arg``."""

    @overload
    def __setitem__(self, arg0: int, arg1: CompressedWaterColumnBeam, /) -> None: ...

    @overload
    def __setitem__(self, arg0: slice, arg1: CompressedWaterColumnBeams_vector, /) -> None: ...

    @overload
    def __delitem__(self, arg: int, /) -> None: ...

    @overload
    def __delitem__(self, arg: slice, /) -> None: ...

    def __eq__(self, arg: object, /) -> bool: ...

    def __ne__(self, arg: object, /) -> bool: ...

    @overload
    def __contains__(self, arg: CompressedWaterColumnBeam, /) -> bool: ...

    @overload
    def __contains__(self, arg: object, /) -> bool: ...

    def count(self, arg: CompressedWaterColumnBeam, /) -> int:
        """Return number of occurrences of ``arg``."""

    def remove(self, arg: CompressedWaterColumnBeam, /) -> None:
        """Remove first occurrence of ``arg``."""

class CompressedWaterColumnBeamContainer:
    def __init__(self) -> None: ...

    @property
    def beams(self) -> list[CompressedWaterColumnBeam]: ...

    @beams.setter
    def beams(self, arg: Sequence[CompressedWaterColumnBeam], /) -> None: ...

    def get_magnitude_bytes(self) -> int: ...

    def get_has_phase(self) -> bool: ...

    def get_magnitude_is_db(self) -> bool: ...

    def get_magnitude_is_32bit(self) -> bool: ...

    def get_beam_number_tensor(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]: ...

    def get_segment_number_tensor(self) -> Annotated[NDArray[numpy.uint8], dict(order='C')]: ...

    def get_sample_count_tensor(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_magnitude(self, beam_index: int) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """magnitude of a beam (raw values as float, not dB)"""

    def get_phase(self, beam_index: int) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """phase of a beam in radians (empty if there is no phase)"""

    def get_magnitude_in_db(self, beam_index: int) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        magnitude of a beam in dB (already-dB values pass through, else
        20*log10(mag/full_scale))
        """

    def get_phase_in_degrees(self, beam_index: int) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """phase of a beam in degrees (empty if there is no phase)"""

    def get_magnitudes(self) -> list[Annotated[NDArray[numpy.float32], dict(order='C')]]:
        """magnitude arrays, one per beam (dB if get_magnitude_is_db(), else raw)"""

    def get_phases(self) -> list[Annotated[NDArray[numpy.float32], dict(order='C')]]:
        """
        phase arrays in radians, one per beam (empty beams if there is no phase)
        """

    def get_magnitudes_in_db(self) -> list[Annotated[NDArray[numpy.float32], dict(order='C')]]:
        """magnitude in dB, one array per beam (see get_magnitude_in_db)"""

    def get_number_of_beams(self) -> int: ...

    def get_total_number_of_samples(self) -> int: ...

    def get_samples_are_skipped(self) -> bool: ...

    def get_sample_position(self) -> int: ...

    def __eq__(self, other: CompressedWaterColumnBeamContainer) -> bool: ...

    def copy(self) -> CompressedWaterColumnBeamContainer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> CompressedWaterColumnBeamContainer: ...

    def __deepcopy__(self, arg: dict, /) -> CompressedWaterColumnBeamContainer: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class ReferencePoint(S7KDatagram):
    """7k record ReferencePoint"""

    def __init__(self) -> None: ...

    def get_offset_x(self) -> float:
        """vehicle reference X offset to center of gravity (meters)"""

    def set_offset_x(self, val: float) -> None:
        """vehicle reference X offset to center of gravity (meters)"""

    def get_offset_y(self) -> float:
        """vehicle reference Y offset to center of gravity (meters)"""

    def set_offset_y(self, val: float) -> None:
        """vehicle reference Y offset to center of gravity (meters)"""

    def get_offset_z(self) -> float:
        """vehicle reference Z offset to center of gravity (meters)"""

    def set_offset_z(self, val: float) -> None:
        """vehicle reference Z offset to center of gravity (meters)"""

    def get_water_z(self) -> float:
        """water level Z offset to center of gravity (meters)"""

    def set_water_z(self, val: float) -> None:
        """water level Z offset to center of gravity (meters)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, val: int) -> None: ...

    def __eq__(self, other: ReferencePoint) -> bool: ...

    def copy(self) -> ReferencePoint:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ReferencePoint: ...

    def __deepcopy__(self, arg: dict, /) -> ReferencePoint: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ReferencePoint:
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

class Position_t_position_type_flag(enum.Enum):
    """position type flag (7k DFD Table 15)"""

    geographic = 0
    """geographical coordinates (latitude/longitude in radians)"""

    grid = 1
    """grid coordinates (northing/easting in meters)"""

class Position_o_position_type_flag:
    """
    Helper class to convert between strings and enum values of type 't_position_type_flag'
    """

    @overload
    def __init__(self, value: Position_t_position_type_flag = Position_t_position_type_flag.geographic) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None: ...

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> Position_t_position_type_flag:
        """enum value"""

    @value.setter
    def value(self, arg: Position_t_position_type_flag, /) -> None: ...

    __default_value__: Final[Position_t_position_type_flag] = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: Position_o_position_type_flag, /) -> bool: ...

    @overload
    def __eq__(self, arg: Position_t_position_type_flag, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> Position_o_position_type_flag:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> Position_o_position_type_flag: ...

    def __deepcopy__(self, arg: dict, /) -> Position_o_position_type_flag: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Position_o_position_type_flag:
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

class Position_t_quality_flag(enum.Enum):
    """position quality flag (7k DFD Table 15)"""

    navigation = 0
    """navigation data"""

    dead_reckoning = 1
    """dead-reckoning"""

class Position_o_quality_flag:
    """
    Helper class to convert between strings and enum values of type 't_quality_flag'
    """

    @overload
    def __init__(self, value: Position_t_quality_flag = Position_t_quality_flag.navigation) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None: ...

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> Position_t_quality_flag:
        """enum value"""

    @value.setter
    def value(self, arg: Position_t_quality_flag, /) -> None: ...

    __default_value__: Final[Position_t_quality_flag] = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: Position_o_quality_flag, /) -> bool: ...

    @overload
    def __eq__(self, arg: Position_t_quality_flag, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> Position_o_quality_flag:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> Position_o_quality_flag: ...

    def __deepcopy__(self, arg: dict, /) -> Position_o_quality_flag: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Position_o_quality_flag:
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

class Position_t_position_method(enum.Enum):
    """positioning method (7k DFD Table 15)"""

    gps = 0
    """GPS"""

    dgps = 1
    """DGPS"""

    inertial_start_from_gps = 2
    """start of inertial positioning system from GPS"""

    inertial_start_from_dgps = 3
    """start of inertial positioning system from DGPS"""

    inertial_start_from_bottom_correlation = 4
    """start of inertial positioning system from bottom correlation"""

    inertial_start_from_bottom_object = 5
    """start of inertial positioning from bottom object"""

    inertial_start_from_inertial = 6
    """start of inertial positioning from inertial positioning"""

    inertial_start_from_optional_data = 7
    """start of inertial positioning from optional data"""

    inertial_stop_to_gps = 8
    """stop of inertial positioning system to GPS"""

    inertial_stop_to_dgps = 9
    """stop of inertial positioning system to DGPS"""

    inertial_stop_to_bottom_correlation = 10
    """stop of inertial positioning system to bottom correlation"""

    inertial_stop_to_bottom_object = 11
    """stop of inertial positioning to bottom object"""

    inertial_start_to_inertial = 12
    """start of inertial positioning to inertial positioning"""

    inertial_start_to_optional_data = 13
    """start of inertial positioning to optional data"""

    user_defined = 14
    """user defined"""

    rtk_fixed = 15
    """RTK fixed"""

    rtk_float = 16
    """RTK float"""

class Position_o_position_method:
    """
    Helper class to convert between strings and enum values of type 't_position_method'
    """

    @overload
    def __init__(self, value: Position_t_position_method = Position_t_position_method.gps) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None: ...

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> Position_t_position_method:
        """enum value"""

    @value.setter
    def value(self, arg: Position_t_position_method, /) -> None: ...

    __default_value__: Final[Position_t_position_method] = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: Position_o_position_method, /) -> bool: ...

    @overload
    def __eq__(self, arg: Position_t_position_method, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> Position_o_position_method:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> Position_o_position_method: ...

    def __deepcopy__(self, arg: dict, /) -> Position_o_position_method: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Position_o_position_method:
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

class Position(S7KDatagram):
    """
    7k Position Record (1003) used in conjunction with Record Type 1011
    (Geodesy).
    """

    def __init__(self) -> None: ...

    def get_datum_identifier(self) -> int:
        """datum identifier (0 = WGS84, >0 = reserved)"""

    def set_datum_identifier(self, val: int) -> None:
        """datum identifier (0 = WGS84, >0 = reserved)"""

    def get_latency(self) -> float:
        """positioning latency in seconds (0 for 7k sonar / PDS)"""

    def set_latency(self, val: float) -> None:
        """positioning latency in seconds (0 for 7k sonar / PDS)"""

    def get_latitude_or_northing(self) -> float: ...

    def set_latitude_or_northing(self, val: float) -> None: ...

    def get_longitude_or_easting(self) -> float: ...

    def set_longitude_or_easting(self, val: float) -> None: ...

    def get_height(self) -> float:
        """height relative to datum in meters"""

    def set_height(self, val: float) -> None:
        """height relative to datum in meters"""

    def get_position_type_flag(self) -> Position_o_position_type_flag:
        """0 = geographical, 1 = grid coordinates"""

    def set_position_type_flag(self, val: Position_o_position_type_flag) -> None:
        """0 = geographical, 1 = grid coordinates"""

    def get_utm_zone(self) -> int:
        """UTM zone (if grid coordinates)"""

    def set_utm_zone(self, val: int) -> None:
        """UTM zone (if grid coordinates)"""

    def get_quality_flag(self) -> Position_o_quality_flag:
        """0 = navigation data, 1 = dead-reckoning"""

    def set_quality_flag(self, val: Position_o_quality_flag) -> None:
        """0 = navigation data, 1 = dead-reckoning"""

    def get_position_method(self) -> Position_o_position_method:
        """positioning method (GPS/DGPS/RTK/inertial)"""

    def set_position_method(self, val: Position_o_position_method) -> None:
        """positioning method (GPS/DGPS/RTK/inertial)"""

    def get_number_of_satellites(self) -> int:
        """number of satellites (optional)"""

    def set_number_of_satellites(self, val: int) -> None:
        """number of satellites (optional)"""

    def get_checksum(self) -> int:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def set_checksum(self, val: int) -> None:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def get_latitude_in_degrees(self) -> float:
        """
        Get the latitude in degrees (only meaningful for geographical
        coordinates).
        Returns:
            latitude_or_northing converted from radians to degrees.
        """

    def get_longitude_in_degrees(self) -> float:
        """
        Get the longitude in degrees (only meaningful for geographical
        coordinates).
        Returns:
            longitude_or_easting converted from radians to degrees.
        """

    def __eq__(self, other: Position) -> bool: ...

    def copy(self) -> Position:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> Position: ...

    def __deepcopy__(self, arg: dict, /) -> Position: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Position:
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

class RollPitchHeave(S7KDatagram):
    """7k record RollPitchHeave"""

    def __init__(self) -> None: ...

    def get_roll(self) -> float:
        """vessel roll in radians"""

    def set_roll(self, val: float) -> None:
        """vessel roll in radians"""

    def get_pitch(self) -> float:
        """vessel pitch in radians"""

    def set_pitch(self, val: float) -> None:
        """vessel pitch in radians"""

    def get_heave(self) -> float:
        """vessel heave in meters"""

    def set_heave(self, val: float) -> None:
        """vessel heave in meters"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, val: int) -> None: ...

    def get_roll_in_degrees(self) -> float:
        """Get the vessel roll in degrees (converted from radians)."""

    def get_pitch_in_degrees(self) -> float:
        """Get the vessel pitch in degrees (converted from radians)."""

    def __eq__(self, other: RollPitchHeave) -> bool: ...

    def copy(self) -> RollPitchHeave:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RollPitchHeave: ...

    def __deepcopy__(self, arg: dict, /) -> RollPitchHeave: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RollPitchHeave:
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

class Heading(S7KDatagram):
    """7k record Heading"""

    def __init__(self) -> None: ...

    def get_heading(self) -> float:
        """vessel heading in radians"""

    def set_heading(self, val: float) -> None:
        """vessel heading in radians"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, val: int) -> None: ...

    def get_heading_in_degrees(self) -> float:
        """Get the vessel heading in degrees (converted from radians)."""

    def __eq__(self, other: Heading) -> bool: ...

    def copy(self) -> Heading:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> Heading: ...

    def __deepcopy__(self, arg: dict, /) -> Heading: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Heading:
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

class Navigation_t_vertical_reference(enum.Enum):
    """vertical reference (7k DFD 1015)"""

    ellipsoid = 1
    """ellipsoid"""

    geoid = 2
    """geoid"""

    chart_datum = 3
    """chart datum"""

class Navigation_o_vertical_reference:
    """
    Helper class to convert between strings and enum values of type 't_vertical_reference'
    """

    @overload
    def __init__(self, value: Navigation_t_vertical_reference = Navigation_t_vertical_reference.ellipsoid) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None: ...

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> Navigation_t_vertical_reference:
        """enum value"""

    @value.setter
    def value(self, arg: Navigation_t_vertical_reference, /) -> None: ...

    __default_value__: Final[Navigation_t_vertical_reference] = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: Navigation_o_vertical_reference, /) -> bool: ...

    @overload
    def __eq__(self, arg: Navigation_t_vertical_reference, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> Navigation_o_vertical_reference:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> Navigation_o_vertical_reference: ...

    def __deepcopy__(self, arg: dict, /) -> Navigation_o_vertical_reference: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Navigation_o_vertical_reference:
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

class Navigation(S7KDatagram):
    """7k record Navigation"""

    def __init__(self) -> None: ...

    def get_vertical_reference(self) -> Navigation_o_vertical_reference:
        """1 = ellipsoid, 2 = geoid, 3 = chart datum"""

    def set_vertical_reference(self, val: Navigation_o_vertical_reference) -> None:
        """1 = ellipsoid, 2 = geoid, 3 = chart datum"""

    def get_latitude(self) -> float:
        """latitude in radians (-pi/2 .. +pi/2)"""

    def set_latitude(self, val: float) -> None:
        """latitude in radians (-pi/2 .. +pi/2)"""

    def get_longitude(self) -> float:
        """longitude in radians (-pi .. +pi)"""

    def set_longitude(self, val: float) -> None:
        """longitude in radians (-pi .. +pi)"""

    def get_position_accuracy(self) -> float:
        """horizontal position accuracy in meters"""

    def set_position_accuracy(self, val: float) -> None:
        """horizontal position accuracy in meters"""

    def get_height(self) -> float:
        """height of vessel reference point above vertical reference (meters)"""

    def set_height(self, val: float) -> None:
        """height of vessel reference point above vertical reference (meters)"""

    def get_height_accuracy(self) -> float:
        """height accuracy in meters"""

    def set_height_accuracy(self, val: float) -> None:
        """height accuracy in meters"""

    def get_speed(self) -> float:
        """speed over ground in meters per second"""

    def set_speed(self, val: float) -> None:
        """speed over ground in meters per second"""

    def get_course(self) -> float:
        """course over ground in radians"""

    def set_course(self, val: float) -> None:
        """course over ground in radians"""

    def get_heading(self) -> float:
        """heading in radians"""

    def set_heading(self, val: float) -> None:
        """heading in radians"""

    def get_checksum(self) -> int:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def set_checksum(self, val: int) -> None:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def get_latitude_in_degrees(self) -> float:
        """Get the latitude in degrees (converted from radians)."""

    def get_longitude_in_degrees(self) -> float:
        """Get the longitude in degrees (converted from radians)."""

    def get_course_in_degrees(self) -> float:
        """Get the course over ground in degrees (converted from radians)."""

    def get_heading_in_degrees(self) -> float:
        """Get the heading in degrees (converted from radians)."""

    def __eq__(self, other: Navigation) -> bool: ...

    def copy(self) -> Navigation:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> Navigation: ...

    def __deepcopy__(self, arg: dict, /) -> Navigation: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Navigation:
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

class SonarSettings_t_tx_pulse_type(enum.Enum):
    """transmit pulse type"""

    cw = 0
    """CW"""

    chirp = 1
    """linear chirp (FM)"""

class SonarSettings_o_tx_pulse_type:
    """
    Helper class to convert between strings and enum values of type 't_tx_pulse_type'
    """

    @overload
    def __init__(self, value: SonarSettings_t_tx_pulse_type = SonarSettings_t_tx_pulse_type.cw) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None: ...

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> SonarSettings_t_tx_pulse_type:
        """enum value"""

    @value.setter
    def value(self, arg: SonarSettings_t_tx_pulse_type, /) -> None: ...

    __default_value__: Final[SonarSettings_t_tx_pulse_type] = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: SonarSettings_o_tx_pulse_type, /) -> bool: ...

    @overload
    def __eq__(self, arg: SonarSettings_t_tx_pulse_type, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> SonarSettings_o_tx_pulse_type:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SonarSettings_o_tx_pulse_type: ...

    def __deepcopy__(self, arg: dict, /) -> SonarSettings_o_tx_pulse_type: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SonarSettings_o_tx_pulse_type:
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

class SonarSettings_t_tx_pulse_envelope(enum.Enum):
    """transmit pulse envelope"""

    tapered_rectangular = 0
    """tapered rectangular"""

    tukey = 1
    """Tukey"""

    hamming = 2
    """Hamming"""

    han = 3
    """Han"""

    rectangular = 4
    """rectangular"""

class SonarSettings_o_tx_pulse_envelope:
    """
    Helper class to convert between strings and enum values of type 't_tx_pulse_envelope'
    """

    @overload
    def __init__(self, value: SonarSettings_t_tx_pulse_envelope = SonarSettings_t_tx_pulse_envelope.tapered_rectangular) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None: ...

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> SonarSettings_t_tx_pulse_envelope:
        """enum value"""

    @value.setter
    def value(self, arg: SonarSettings_t_tx_pulse_envelope, /) -> None: ...

    __default_value__: Final[SonarSettings_t_tx_pulse_envelope] = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: SonarSettings_o_tx_pulse_envelope, /) -> bool: ...

    @overload
    def __eq__(self, arg: SonarSettings_t_tx_pulse_envelope, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> SonarSettings_o_tx_pulse_envelope:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SonarSettings_o_tx_pulse_envelope: ...

    def __deepcopy__(self, arg: dict, /) -> SonarSettings_o_tx_pulse_envelope: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SonarSettings_o_tx_pulse_envelope:
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

class SonarSettings_t_tx_pulse_mode(enum.Enum):
    """transmit pulse mode"""

    undefined = 0
    """undefined"""

    single_ping = 1
    """single ping"""

    multi_ping_2 = 2
    """multi-ping 2"""

    multi_ping_3 = 3
    """multi-ping 3"""

    multi_ping_4 = 4
    """multi-ping 4"""

class SonarSettings_o_tx_pulse_mode:
    """
    Helper class to convert between strings and enum values of type 't_tx_pulse_mode'
    """

    @overload
    def __init__(self, value: SonarSettings_t_tx_pulse_mode = SonarSettings_t_tx_pulse_mode.undefined) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None: ...

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> SonarSettings_t_tx_pulse_mode:
        """enum value"""

    @value.setter
    def value(self, arg: SonarSettings_t_tx_pulse_mode, /) -> None: ...

    __default_value__: Final[SonarSettings_t_tx_pulse_mode] = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: SonarSettings_o_tx_pulse_mode, /) -> bool: ...

    @overload
    def __eq__(self, arg: SonarSettings_t_tx_pulse_mode, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> SonarSettings_o_tx_pulse_mode:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SonarSettings_o_tx_pulse_mode: ...

    def __deepcopy__(self, arg: dict, /) -> SonarSettings_o_tx_pulse_mode: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SonarSettings_o_tx_pulse_mode:
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

class SonarSettings_t_projector_weighting(enum.Enum):
    """projector beam weighting window type"""

    rectangular = 0
    """rectangular"""

    chebychev = 1
    """Chebychev"""

    gauss = 2
    """Gauss"""

class SonarSettings_o_projector_weighting:
    """
    Helper class to convert between strings and enum values of type 't_projector_weighting'
    """

    @overload
    def __init__(self, value: SonarSettings_t_projector_weighting = SonarSettings_t_projector_weighting.rectangular) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None: ...

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> SonarSettings_t_projector_weighting:
        """enum value"""

    @value.setter
    def value(self, arg: SonarSettings_t_projector_weighting, /) -> None: ...

    __default_value__: Final[SonarSettings_t_projector_weighting] = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: SonarSettings_o_projector_weighting, /) -> bool: ...

    @overload
    def __eq__(self, arg: SonarSettings_t_projector_weighting, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> SonarSettings_o_projector_weighting:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SonarSettings_o_projector_weighting: ...

    def __deepcopy__(self, arg: dict, /) -> SonarSettings_o_projector_weighting: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SonarSettings_o_projector_weighting:
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

class SonarSettings_t_rx_weighting(enum.Enum):
    """receive beam weighting window"""

    chebychev = 0
    """Chebychev"""

    kaiser = 1
    """Kaiser"""

class SonarSettings_o_rx_weighting:
    """
    Helper class to convert between strings and enum values of type 't_rx_weighting'
    """

    @overload
    def __init__(self, value: SonarSettings_t_rx_weighting = SonarSettings_t_rx_weighting.chebychev) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None: ...

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> SonarSettings_t_rx_weighting:
        """enum value"""

    @value.setter
    def value(self, arg: SonarSettings_t_rx_weighting, /) -> None: ...

    __default_value__: Final[SonarSettings_t_rx_weighting] = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: SonarSettings_o_rx_weighting, /) -> bool: ...

    @overload
    def __eq__(self, arg: SonarSettings_t_rx_weighting, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> SonarSettings_o_rx_weighting:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SonarSettings_o_rx_weighting: ...

    def __deepcopy__(self, arg: dict, /) -> SonarSettings_o_rx_weighting: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SonarSettings_o_rx_weighting:
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

class SonarSettings(S7KDatagram):
    """7k record SonarSettings"""

    def __init__(self) -> None: ...

    def get_serial_number(self) -> int:
        """sonar serial number"""

    def set_serial_number(self, val: int) -> None:
        """sonar serial number"""

    def get_ping_number(self) -> int:
        """sequential ping number"""

    def set_ping_number(self, val: int) -> None:
        """sequential ping number"""

    def get_multi_ping(self) -> int:
        """0 = single ping, else multi-ping seq"""

    def set_multi_ping(self, val: int) -> None:
        """0 = single ping, else multi-ping seq"""

    def get_frequency(self) -> float:
        """transmit frequency in Hz"""

    def set_frequency(self, val: float) -> None:
        """transmit frequency in Hz"""

    def get_sample_rate(self) -> float:
        """sample rate in Hz"""

    def set_sample_rate(self, val: float) -> None:
        """sample rate in Hz"""

    def get_receiver_bandwidth(self) -> float:
        """receiver bandwidth in Hz"""

    def set_receiver_bandwidth(self, val: float) -> None:
        """receiver bandwidth in Hz"""

    def get_tx_pulse_width(self) -> float:
        """transmit pulse length in seconds"""

    def set_tx_pulse_width(self, val: float) -> None:
        """transmit pulse length in seconds"""

    def get_tx_pulse_type(self) -> SonarSettings_o_tx_pulse_type:
        """0 = CW, 1 = chirp"""

    def set_tx_pulse_type(self, val: SonarSettings_o_tx_pulse_type) -> None:
        """0 = CW, 1 = chirp"""

    def get_tx_pulse_envelope(self) -> SonarSettings_o_tx_pulse_envelope:
        """envelope/window type (0-4)"""

    def set_tx_pulse_envelope(self, val: SonarSettings_o_tx_pulse_envelope) -> None:
        """envelope/window type (0-4)"""

    def get_tx_pulse_envelope_parameter(self) -> float:
        """envelope parameter"""

    def set_tx_pulse_envelope_parameter(self, val: float) -> None:
        """envelope parameter"""

    def get_tx_pulse_mode(self) -> SonarSettings_o_tx_pulse_mode:
        """1-4 (single/multi-ping mode)"""

    def set_tx_pulse_mode(self, val: SonarSettings_o_tx_pulse_mode) -> None:
        """1-4 (single/multi-ping mode)"""

    def get_max_ping_rate(self) -> float:
        """maximum ping rate in pings per second"""

    def set_max_ping_rate(self, val: float) -> None:
        """maximum ping rate in pings per second"""

    def get_ping_period(self) -> float:
        """seconds since previous ping"""

    def set_ping_period(self, val: float) -> None:
        """seconds since previous ping"""

    def get_range_selection(self) -> float:
        """range selection in meters"""

    def set_range_selection(self, val: float) -> None:
        """range selection in meters"""

    def get_power_selection(self) -> float:
        """power selection in dB re 1 uPa"""

    def set_power_selection(self, val: float) -> None:
        """power selection in dB re 1 uPa"""

    def get_gain_selection(self) -> float:
        """gain selection in dB"""

    def set_gain_selection(self, val: float) -> None:
        """gain selection in dB"""

    def get_control_flags(self) -> int:
        """control flags bit field (7k DFD Tbl 42)"""

    def set_control_flags(self, val: int) -> None:
        """control flags bit field (7k DFD Tbl 42)"""

    def get_projector_id(self) -> int:
        """transmit projector identifier"""

    def set_projector_id(self, val: int) -> None:
        """transmit projector identifier"""

    def get_steering_vertical(self) -> float:
        """transmit steering angle vertical (rad)"""

    def set_steering_vertical(self, val: float) -> None:
        """transmit steering angle vertical (rad)"""

    def get_steering_horizontal(self) -> float:
        """transmit steering angle horizontal (rad)"""

    def set_steering_horizontal(self, val: float) -> None:
        """transmit steering angle horizontal (rad)"""

    def get_beamwidth_vertical(self) -> float:
        """transmit -3dB beam width vertical (rad)"""

    def set_beamwidth_vertical(self, val: float) -> None:
        """transmit -3dB beam width vertical (rad)"""

    def get_beamwidth_horizontal(self) -> float:
        """transmit -3dB beam width horizontal (rad)"""

    def set_beamwidth_horizontal(self, val: float) -> None:
        """transmit -3dB beam width horizontal (rad)"""

    def get_focal_point(self) -> float:
        """transmit focal point in meters"""

    def set_focal_point(self, val: float) -> None:
        """transmit focal point in meters"""

    def get_projector_weighting(self) -> SonarSettings_o_projector_weighting:
        """projector weighting window type (0-2)"""

    def set_projector_weighting(self, val: SonarSettings_o_projector_weighting) -> None:
        """projector weighting window type (0-2)"""

    def get_projector_weighting_parameter(self) -> float:
        """projector weighting parameter"""

    def set_projector_weighting_parameter(self, val: float) -> None:
        """projector weighting parameter"""

    def get_transmit_flags(self) -> int:
        """transmit flags bit field (7k DFD Tbl 42)"""

    def set_transmit_flags(self, val: int) -> None:
        """transmit flags bit field (7k DFD Tbl 42)"""

    def get_hydrophone_id(self) -> int:
        """receiver hydrophone identifier"""

    def set_hydrophone_id(self, val: int) -> None:
        """receiver hydrophone identifier"""

    def get_rx_weighting(self) -> SonarSettings_o_rx_weighting:
        """receiver weighting window type (0-1)"""

    def set_rx_weighting(self, val: SonarSettings_o_rx_weighting) -> None:
        """receiver weighting window type (0-1)"""

    def get_rx_weighting_parameter(self) -> float:
        """receiver weighting parameter"""

    def set_rx_weighting_parameter(self, val: float) -> None:
        """receiver weighting parameter"""

    def get_rx_flags(self) -> int:
        """receiver flags bit field (7k DFD Tbl 42)"""

    def set_rx_flags(self, val: int) -> None:
        """receiver flags bit field (7k DFD Tbl 42)"""

    def get_rx_width(self) -> float:
        """receiver beam width in radians"""

    def set_rx_width(self, val: float) -> None:
        """receiver beam width in radians"""

    def get_range_minimum(self) -> float:
        """bottom detection minimum range (m)"""

    def set_range_minimum(self, val: float) -> None:
        """bottom detection minimum range (m)"""

    def get_range_maximum(self) -> float:
        """bottom detection maximum range (m)"""

    def set_range_maximum(self, val: float) -> None:
        """bottom detection maximum range (m)"""

    def get_depth_minimum(self) -> float:
        """bottom detection minimum depth (m)"""

    def set_depth_minimum(self, val: float) -> None:
        """bottom detection minimum depth (m)"""

    def get_depth_maximum(self) -> float:
        """bottom detection maximum depth (m)"""

    def set_depth_maximum(self, val: float) -> None:
        """bottom detection maximum depth (m)"""

    def get_absorption(self) -> float:
        """absorption"""

    def set_absorption(self, val: float) -> None:
        """absorption"""

    def get_sound_velocity(self) -> float:
        """sound velocity"""

    def set_sound_velocity(self, val: float) -> None:
        """sound velocity"""

    def get_spreading(self) -> float:
        """spreading loss"""

    def set_spreading(self, val: float) -> None:
        """spreading loss"""

    def get_checksum(self) -> int:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def set_checksum(self, val: int) -> None:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def get_steering_vertical_in_degrees(self) -> float:
        """
        Get the transmit steering angle vertical in degrees (converted from
        radians).
        """

    def get_steering_horizontal_in_degrees(self) -> float:
        """
        Get the transmit steering angle horizontal in degrees (converted from
        radians).
        """

    def get_beamwidth_vertical_in_degrees(self) -> float:
        """
        Get the transmit -3dB beam width vertical in degrees (converted from
        radians).
        """

    def get_beamwidth_horizontal_in_degrees(self) -> float:
        """
        Get the transmit -3dB beam width horizontal in degrees (converted from
        radians).
        """

    def get_rx_width_in_degrees(self) -> float:
        """Get the receiver beam width in degrees (converted from radians)."""

    def __eq__(self, other: SonarSettings) -> bool: ...

    def copy(self) -> SonarSettings:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SonarSettings: ...

    def __deepcopy__(self, arg: dict, /) -> SonarSettings: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SonarSettings:
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

class MatchFilter_t_operation(enum.Enum):
    """match filter operation (7k DFD Table 43)"""

    off = 0
    """off"""

    on = 1
    """on"""

class MatchFilter_o_operation:
    """
    Helper class to convert between strings and enum values of type 't_operation'
    """

    @overload
    def __init__(self, value: MatchFilter_t_operation = MatchFilter_t_operation.off) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None: ...

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> MatchFilter_t_operation:
        """enum value"""

    @value.setter
    def value(self, arg: MatchFilter_t_operation, /) -> None: ...

    __default_value__: Final[MatchFilter_t_operation] = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: MatchFilter_o_operation, /) -> bool: ...

    @overload
    def __eq__(self, arg: MatchFilter_t_operation, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> MatchFilter_o_operation:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MatchFilter_o_operation: ...

    def __deepcopy__(self, arg: dict, /) -> MatchFilter_o_operation: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> MatchFilter_o_operation:
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

class MatchFilter_t_window_type(enum.Enum):
    """match filter window type (7k DFD Table 43)"""

    rectangular = 0
    """rectangular"""

    kaiser = 1
    """Kaiser"""

    hamming = 2
    """Hamming"""

    blackmann = 3
    """Blackmann"""

    triangular = 4
    """triangular"""

    taylor = 5
    """X (Taylor)"""

class MatchFilter_o_window_type:
    """
    Helper class to convert between strings and enum values of type 't_window_type'
    """

    @overload
    def __init__(self, value: MatchFilter_t_window_type = MatchFilter_t_window_type.rectangular) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None: ...

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> MatchFilter_t_window_type:
        """enum value"""

    @value.setter
    def value(self, arg: MatchFilter_t_window_type, /) -> None: ...

    __default_value__: Final[MatchFilter_t_window_type] = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: MatchFilter_o_window_type, /) -> bool: ...

    @overload
    def __eq__(self, arg: MatchFilter_t_window_type, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> MatchFilter_o_window_type:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MatchFilter_o_window_type: ...

    def __deepcopy__(self, arg: dict, /) -> MatchFilter_o_window_type: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> MatchFilter_o_window_type:
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

class MatchFilter(S7KDatagram):
    """7k record MatchFilter"""

    def __init__(self) -> None: ...

    def get_serial_number(self) -> int:
        """sonar serial number"""

    def set_serial_number(self, val: int) -> None:
        """sonar serial number"""

    def get_ping_number(self) -> int:
        """sequential ping number"""

    def set_ping_number(self, val: int) -> None:
        """sequential ping number"""

    def get_operation(self) -> MatchFilter_o_operation:
        """0 = off, 1 = on"""

    def set_operation(self, val: MatchFilter_o_operation) -> None:
        """0 = off, 1 = on"""

    def get_start_frequency(self) -> float:
        """start frequency in Hz"""

    def set_start_frequency(self, val: float) -> None:
        """start frequency in Hz"""

    def get_end_frequency(self) -> float:
        """stop frequency in Hz"""

    def set_end_frequency(self, val: float) -> None:
        """stop frequency in Hz"""

    def get_window_type(self) -> MatchFilter_o_window_type:
        """match filter window type (0-5)"""

    def set_window_type(self, val: MatchFilter_o_window_type) -> None:
        """match filter window type (0-5)"""

    def get_shading(self) -> float:
        """shading value"""

    def set_shading(self, val: float) -> None:
        """shading value"""

    def get_effective_pulse_width(self) -> float:
        """effective pulse width after FM compression (s)"""

    def set_effective_pulse_width(self, val: float) -> None:
        """effective pulse width after FM compression (s)"""

    def get_checksum(self) -> int:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def set_checksum(self, val: int) -> None:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def __eq__(self, other: MatchFilter) -> bool: ...

    def copy(self) -> MatchFilter:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> MatchFilter: ...

    def __deepcopy__(self, arg: dict, /) -> MatchFilter: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> MatchFilter:
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

class SoundVelocity(S7KDatagram):
    """7k record SoundVelocity"""

    def __init__(self) -> None: ...

    def get_sound_velocity(self) -> float:
        """water sound velocity in meters per second"""

    def set_sound_velocity(self, val: float) -> None:
        """water sound velocity in meters per second"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, val: int) -> None: ...

    def __eq__(self, other: SoundVelocity) -> bool: ...

    def copy(self) -> SoundVelocity:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SoundVelocity: ...

    def __deepcopy__(self, arg: dict, /) -> SoundVelocity: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SoundVelocity:
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

class AbsorptionLoss(S7KDatagram):
    """7k record AbsorptionLoss"""

    def __init__(self) -> None: ...

    def get_absorption_loss(self) -> float:
        """absorption loss in dB/km"""

    def set_absorption_loss(self, val: float) -> None:
        """absorption loss in dB/km"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, val: int) -> None: ...

    def __eq__(self, other: AbsorptionLoss) -> bool: ...

    def copy(self) -> AbsorptionLoss:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> AbsorptionLoss: ...

    def __deepcopy__(self, arg: dict, /) -> AbsorptionLoss: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> AbsorptionLoss:
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

class SpreadingLoss(S7KDatagram):
    """7k record SpreadingLoss"""

    def __init__(self) -> None: ...

    def get_spreading_loss(self) -> float:
        """spreading loss in dB (0-60)"""

    def set_spreading_loss(self, val: float) -> None:
        """spreading loss in dB (0-60)"""

    def get_checksum(self) -> int: ...

    def set_checksum(self, val: int) -> None: ...

    def __eq__(self, other: SpreadingLoss) -> bool: ...

    def copy(self) -> SpreadingLoss:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SpreadingLoss: ...

    def __deepcopy__(self, arg: dict, /) -> SpreadingLoss: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SpreadingLoss:
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

class RawDetection(S7KDatagram):
    """
    7k record RawDetectionData: raw bottom detections (bathymetry) per
    beam.

    This is the preferred bathymetry record (replaces the deprecated
    7006). It holds, per beam, the detection point (fractional sample
    number), the receive steering angle and detection quality.
    """

    def __init__(self) -> None: ...

    def get_serial_number(self) -> int:
        """sonar serial number"""

    def set_serial_number(self, val: int) -> None:
        """sonar serial number"""

    def get_ping_number(self) -> int:
        """sequential ping number"""

    def set_ping_number(self, val: int) -> None:
        """sequential ping number"""

    def get_multi_ping(self) -> int:
        """0 = single ping, else multi-ping sequence number"""

    def set_multi_ping(self, val: int) -> None:
        """0 = single ping, else multi-ping sequence number"""

    def get_number_beams(self) -> int:
        """number of detection points (beams)"""

    def set_number_beams(self, val: int) -> None:
        """number of detection points (beams)"""

    def get_data_field_size(self) -> int:
        """size in bytes of each per-beam detection record"""

    def set_data_field_size(self, val: int) -> None:
        """size in bytes of each per-beam detection record"""

    def get_detection_algorithm(self) -> int:
        """detection algorithm (0-7: G1/G2/G3/IF1/PS1/HS1/HS2)"""

    def set_detection_algorithm(self, val: int) -> None:
        """detection algorithm (0-7: G1/G2/G3/IF1/PS1/HS1/HS2)"""

    def get_flags(self) -> int:
        """flags bit field (uncertainty method, multi-detect)"""

    def set_flags(self, val: int) -> None:
        """flags bit field (uncertainty method, multi-detect)"""

    def get_sampling_rate(self) -> float:
        """sample rate (Hz)"""

    def set_sampling_rate(self, val: float) -> None:
        """sample rate (Hz)"""

    def get_tx_angle(self) -> float:
        """transmit steering angle (rad)"""

    def set_tx_angle(self, val: float) -> None:
        """transmit steering angle (rad)"""

    def get_applied_roll(self) -> float:
        """roll applied to the data (rad)"""

    def set_applied_roll(self, val: float) -> None:
        """roll applied to the data (rad)"""

    def get_tx_angle_in_degrees(self) -> float:
        """Get the transmit steering angle in degrees (converted from radians)."""

    def get_applied_roll_in_degrees(self) -> float:
        """Get the roll applied to the data in degrees (converted from radians)."""

    @property
    def beams(self) -> RawDetectionBeamContainer:
        """per-beam raw detections"""

    @beams.setter
    def beams(self, arg: RawDetectionBeamContainer, /) -> None: ...

    def get_checksum(self) -> int:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def set_checksum(self, val: int) -> None:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def __eq__(self, other: RawDetection) -> bool: ...

    def copy(self) -> RawDetection:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RawDetection: ...

    def __deepcopy__(self, arg: dict, /) -> RawDetection: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RawDetection:
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

class SnippetData(S7KDatagram):
    """
    7k record SnippetData (7028): water-column intensity snippets around
    each beam detection.

    The record holds, per beam, a short intensity time series (snippet)
    around the bottom detection. The per-beam descriptors are stored in a
    SnippetDataBeamContainer (read as one bulk block), the intensity
    samples in a SnippetDataAmplitudes container (16- or 32-bit depending
    on bit 0 of the flags field, read as one bulk block). Array/dB
    conversions are computed on demand.
    """

    def __init__(self) -> None: ...

    def get_serial_number(self) -> int:
        """sonar serial number"""

    def set_serial_number(self, val: int) -> None:
        """sonar serial number"""

    def get_ping_number(self) -> int:
        """sequential ping number"""

    def set_ping_number(self, val: int) -> None:
        """sequential ping number"""

    def get_multi_ping(self) -> int:
        """0 = single ping, else multi-ping sequence number"""

    def set_multi_ping(self, val: int) -> None:
        """0 = single ping, else multi-ping sequence number"""

    def get_number_beams(self) -> int:
        """number of detection points (beams)"""

    def set_number_beams(self, val: int) -> None:
        """number of detection points (beams)"""

    def get_error_flag(self) -> int:
        """0 = ok, 6 = bottom detection failed, else error"""

    def set_error_flag(self, val: int) -> None:
        """0 = ok, 6 = bottom detection failed, else error"""

    def get_control_flags(self) -> int:
        """snippet window control flags"""

    def set_control_flags(self, val: int) -> None:
        """snippet window control flags"""

    def get_flags(self) -> int:
        """flags bit field (bit 0: 0 = 16-bit, 1 = 32-bit snippets)"""

    def set_flags(self, val: int) -> None:
        """flags bit field (bit 0: 0 = 16-bit, 1 = 32-bit snippets)"""

    def get_samples_are_32bit(self) -> bool:
        """
        true if the intensity samples are stored as 32-bit values (flags bit
        0)
        """

    @property
    def beams(self) -> SnippetDataBeamContainer:
        """per-beam snippet descriptors"""

    @beams.setter
    def beams(self, arg: SnippetDataBeamContainer, /) -> None: ...

    @property
    def amplitudes(self) -> SnippetDataAmplitudes:
        """per-beam intensity samples"""

    @amplitudes.setter
    def amplitudes(self, arg: SnippetDataAmplitudes, /) -> None: ...

    def get_checksum(self) -> int:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def set_checksum(self, val: int) -> None:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def __eq__(self, other: SnippetData) -> bool: ...

    def copy(self) -> SnippetData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SnippetData: ...

    def __deepcopy__(self, arg: dict, /) -> SnippetData: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SnippetData:
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

class CompressedWaterColumn(S7KDatagram):
    """
    7k record CompressedWaterColumnData: per-beam water-column magnitude
    (and optional phase) time series in a compressed (downsampled and/or
    bit-reduced) form.

    The exact sample encoding (magnitude bit depth, presence of phase,
    downsampling) is controlled by the flags bit field. This class decodes
    the magnitude to float and the phase to radians for convenient access.
    """

    def __init__(self) -> None: ...

    def get_serial_number(self) -> int:
        """sonar serial number"""

    def set_serial_number(self, val: int) -> None:
        """sonar serial number"""

    def get_ping_number(self) -> int:
        """sequential ping number"""

    def set_ping_number(self, val: int) -> None:
        """sequential ping number"""

    def get_multi_ping(self) -> int:
        """0 = single ping, else multi-ping sequence number"""

    def set_multi_ping(self, val: int) -> None:
        """0 = single ping, else multi-ping sequence number"""

    def get_number_beams(self) -> int:
        """number of beams"""

    def set_number_beams(self, val: int) -> None:
        """number of beams"""

    def get_samples(self) -> int:
        """nominal number of samples (based on range)"""

    def set_samples(self, val: int) -> None:
        """nominal number of samples (based on range)"""

    def get_compressed_samples(self) -> int:
        """maximum number of samples over all beams"""

    def set_compressed_samples(self, val: int) -> None:
        """maximum number of samples over all beams"""

    def get_flags(self) -> int:
        """compression control flags bit field"""

    def set_flags(self, val: int) -> None:
        """compression control flags bit field"""

    def get_first_sample(self) -> int:
        """first sample index for each beam"""

    def set_first_sample(self, val: int) -> None:
        """first sample index for each beam"""

    def get_sample_rate(self) -> float:
        """effective sample rate after downsampling (Hz)"""

    def set_sample_rate(self, val: float) -> None:
        """effective sample rate after downsampling (Hz)"""

    def get_compression_factor(self) -> float:
        """magnitude compression factor"""

    def set_compression_factor(self, val: float) -> None:
        """magnitude compression factor"""

    def get_has_phase(self) -> bool:
        """whether the record contains phase data (derived from bit 1)"""

    def get_magnitude_is_db(self) -> bool:
        """
        whether the magnitude is stored as 8-bit dB values (derived from bit
        2)
        """

    def get_magnitude_bytes(self) -> int:
        """number of bytes per magnitude sample as stored on disk (1, 2 or 4)"""

    def get_flag_use_maximum_bottom_detection(self) -> bool:
        """
        Bit 0: water column data is limited to the bottom detection point
        (+10%).
        """

    def get_flag_intensity_only(self) -> bool:
        """Bit 1: only intensity (magnitude) data is included, phase is stripped."""

    def get_flag_magnitude_to_db(self) -> bool:
        """
        Bit 2: magnitude is converted to dB and stored as an 8-bit value
        (phase as 8-bit).
        """

    def get_flag_32bit_data(self) -> bool:
        """Bit 12: magnitude is stored as 32-bit values."""

    def get_flag_compression_factor_available(self) -> bool:
        """
        Bit 13: a custom compression factor is available (else a factor of 40
        is used).
        """

    def get_flag_segment_numbers_available(self) -> bool:
        """Bit 14: per-beam segment numbers are available."""

    def get_flag_first_sample_is_rxdelay(self) -> bool:
        """Bit 15: the first sample contains the RxDelay value."""

    def get_downsampling_divisor(self) -> int:
        """Bits 4-7: downsampling divisor (1 means no downsampling)."""

    def get_downsampling_type(self) -> int:
        """Bits 8-11: downsampling type (0 none, 1 middle, 2 peak, 3 average)."""

    @property
    def beams(self) -> CompressedWaterColumnBeamContainer:
        """per-beam magnitude/phase data"""

    @beams.setter
    def beams(self, arg: CompressedWaterColumnBeamContainer, /) -> None: ...

    def get_checksum(self) -> int:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def set_checksum(self, val: int) -> None:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def __eq__(self, other: CompressedWaterColumn) -> bool: ...

    def copy(self) -> CompressedWaterColumn:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> CompressedWaterColumn: ...

    def __deepcopy__(self, arg: dict, /) -> CompressedWaterColumn: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> CompressedWaterColumn:
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

class BeamGeometry(S7KDatagram):
    """
    7k record BeamGeometry: per-beam transmit/receive angles and beam
    widths.
    """

    def __init__(self) -> None: ...

    def get_serial_number(self) -> int:
        """sonar serial number"""

    def set_serial_number(self, val: int) -> None:
        """sonar serial number"""

    def get_number_beams(self) -> int:
        """number of beams"""

    def set_number_beams(self, val: int) -> None:
        """number of beams"""

    def get_beam_vertical_angle(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_beam_horizontal_angle(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_beamwidth_vertical(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_beamwidth_horizontal(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_beam_vertical_angle_in_degrees(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Get the along-track (vertical) beam angles in degrees (converted from
        radians).
        """

    def get_beam_horizontal_angle_in_degrees(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Get the across-track (horizontal) beam angles in degrees (converted
        from radians).
        """

    def get_beamwidth_vertical_in_degrees(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Get the along-track (vertical) -3dB beam widths in degrees (converted
        from radians).
        """

    def get_beamwidth_horizontal_in_degrees(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Get the across-track (horizontal) -3dB beam widths in degrees (from
        radians).
        """

    def get_has_tx_delay(self) -> bool: ...

    def get_tx_delay(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_checksum(self) -> int:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def set_checksum(self, val: int) -> None:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def __eq__(self, other: BeamGeometry) -> bool: ...

    def copy(self) -> BeamGeometry:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BeamGeometry: ...

    def __deepcopy__(self, arg: dict, /) -> BeamGeometry: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BeamGeometry:
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

class Attitude(S7KDatagram):
    """
    7k record Attitude: This record will be output at the input motion
    sensor rate.
    """

    def __init__(self) -> None: ...

    def get_number_of_attitudes(self) -> int: ...

    @property
    def attitudes(self) -> AttitudeSampleContainer:
        """attitude attitudes"""

    @attitudes.setter
    def attitudes(self, arg: AttitudeSampleContainer, /) -> None: ...

    def get_checksum(self) -> int:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def set_checksum(self, val: int) -> None:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def __eq__(self, other: Attitude) -> bool: ...

    def copy(self) -> Attitude:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> Attitude: ...

    def __deepcopy__(self, arg: dict, /) -> Attitude: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Attitude:
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

class FileHeader(S7KDatagram):
    """
    7k record FileHeader (7200): the first record of a .s7k file.
    Describes the file (recording program, session, notes) and lists the
    devices contained in the file.
    """

    def __init__(self) -> None: ...

    def get_version(self) -> int:
        """file format version"""

    def get_record_data_size(self) -> int:
        """size of record data (0 if not set)"""

    def get_number_devices(self) -> int:
        """number of devices described in this file"""

    def get_recording_name(self) -> str: ...

    def get_recording_version(self) -> str: ...

    def get_user_defined_name(self) -> str: ...

    def get_notes(self) -> str: ...

    @property
    def devices(self) -> FileHeaderDeviceInfoContainer:
        """device entries"""

    @devices.setter
    def devices(self, arg: FileHeaderDeviceInfoContainer, /) -> None: ...

    def get_checksum(self) -> int:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def set_checksum(self, val: int) -> None:
        """record checksum (last 4 bytes; see S7KDatagram, debugging only)"""

    def __eq__(self, other: FileHeader) -> bool: ...

    def copy(self) -> FileHeader:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> FileHeader: ...

    def __deepcopy__(self, arg: dict, /) -> FileHeader: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FileHeader:
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
