"""Teledyne RESON .s7k (7k) datagram (record) classes"""

from collections.abc import Iterable, Iterator, Sequence
from typing import Annotated, overload

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

    def get_datagram_identifier(self) -> themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier: ...

    def compute_size_content(self) -> int:
        """
        Number of bytes of the record following the DRF header (RTH + data +
        checksum).
        """

    def is_valid(self) -> bool:
        """Test if the DRF sync pattern is valid."""

    def get_checksum_valid(self) -> bool:
        """Test if the flags field indicates a valid checksum (bit 0)."""

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
    def samples(self) -> list[AttitudeSample]: ...

    @samples.setter
    def samples(self, arg: Sequence[AttitudeSample], /) -> None: ...

    def get_delta_time_tensor(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]: ...

    def get_roll_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_pitch_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_heave_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_heading_tensor(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_number_of_samples(self) -> int: ...

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

    def get_raw_samples(self) -> bytes: ...

    def set_raw_samples(self, raw_samples: bytes) -> None: ...

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

    def get_phase_8bit(self) -> bool: ...

    def get_magnitude_is_db(self) -> bool: ...

    def get_magnitude_is_32bit_float(self) -> bool: ...

    def get_sample_stride(self) -> int:
        """number of on-disk bytes per sample (magnitude + optional phase)"""

    def get_beam_number_tensor(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]: ...

    def get_segment_number_tensor(self) -> Annotated[NDArray[numpy.uint8], dict(order='C')]: ...

    def get_sample_count_tensor(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_magnitude(self, beam_index: int) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """magnitude of a beam (raw value, or dB if get_magnitude_is_db())"""

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
        """vehicle reference X offset to center of gravity"""

    def set_offset_x(self, val: float) -> None:
        """vehicle reference X offset to center of gravity"""

    def get_offset_y(self) -> float:
        """vehicle reference Y offset to center of gravity"""

    def set_offset_y(self, val: float) -> None:
        """vehicle reference Y offset to center of gravity"""

    def get_offset_z(self) -> float:
        """vehicle reference Z offset to center of gravity"""

    def set_offset_z(self, val: float) -> None:
        """vehicle reference Z offset to center of gravity"""

    def get_water_z(self) -> float:
        """water level Z offset to center of gravity"""

    def set_water_z(self, val: float) -> None:
        """water level Z offset to center of gravity"""

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

class Position(S7KDatagram):
    """7k record Position"""

    def __init__(self) -> None: ...

    def get_datum(self) -> int:
        """datum identifier (0 = WGS84)"""

    def set_datum(self, val: int) -> None:
        """datum identifier (0 = WGS84)"""

    def get_latency(self) -> float:
        """position latency"""

    def set_latency(self, val: float) -> None:
        """position latency"""

    def get_latitude_northing(self) -> float:
        """latitude (rad) if geographic, else northing (m)"""

    def set_latitude_northing(self, val: float) -> None:
        """latitude (rad) if geographic, else northing (m)"""

    def get_longitude_easting(self) -> float:
        """longitude (rad) if geographic, else easting (m)"""

    def set_longitude_easting(self, val: float) -> None:
        """longitude (rad) if geographic, else easting (m)"""

    def get_height(self) -> float:
        """height relative to datum"""

    def set_height(self, val: float) -> None:
        """height relative to datum"""

    def get_position_type(self) -> int:
        """0 = geographic, 1 = grid coordinates"""

    def set_position_type(self, val: int) -> None:
        """0 = geographic, 1 = grid coordinates"""

    def get_utm_zone(self) -> int:
        """UTM zone (if grid)"""

    def set_utm_zone(self, val: int) -> None:
        """UTM zone (if grid)"""

    def get_quality(self) -> int:
        """0 = navigation, 1 = dead reckoning"""

    def set_quality(self, val: int) -> None:
        """0 = navigation, 1 = dead reckoning"""

    def get_position_method(self) -> int:
        """positioning method (GPS/DGPS/RTK/... 0-16)"""

    def set_position_method(self, val: int) -> None:
        """positioning method (GPS/DGPS/RTK/... 0-16)"""

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
        """vessel roll"""

    def set_roll(self, val: float) -> None:
        """vessel roll"""

    def get_pitch(self) -> float:
        """vessel pitch"""

    def set_pitch(self, val: float) -> None:
        """vessel pitch"""

    def get_heave(self) -> float:
        """vessel heave"""

    def set_heave(self, val: float) -> None:
        """vessel heave"""

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
        """vessel heading"""

    def set_heading(self, val: float) -> None:
        """vessel heading"""

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

class Navigation(S7KDatagram):
    """7k record Navigation"""

    def __init__(self) -> None: ...

    def get_vertical_reference(self) -> int:
        """1 = ellipsoid, 2 = geoid, 3 = chart datum"""

    def set_vertical_reference(self, val: int) -> None:
        """1 = ellipsoid, 2 = geoid, 3 = chart datum"""

    def get_latitude(self) -> float:
        """latitude (-pi/2 .. +pi/2)"""

    def set_latitude(self, val: float) -> None:
        """latitude (-pi/2 .. +pi/2)"""

    def get_longitude(self) -> float:
        """longitude (-pi .. +pi)"""

    def set_longitude(self, val: float) -> None:
        """longitude (-pi .. +pi)"""

    def get_position_accuracy(self) -> float:
        """horizontal position accuracy"""

    def set_position_accuracy(self, val: float) -> None:
        """horizontal position accuracy"""

    def get_height(self) -> float:
        """height of vessel reference point above vertical reference"""

    def set_height(self, val: float) -> None:
        """height of vessel reference point above vertical reference"""

    def get_height_accuracy(self) -> float:
        """height accuracy"""

    def set_height_accuracy(self, val: float) -> None:
        """height accuracy"""

    def get_speed(self) -> float:
        """speed over ground"""

    def set_speed(self, val: float) -> None:
        """speed over ground"""

    def get_course(self) -> float:
        """course over ground"""

    def set_course(self, val: float) -> None:
        """course over ground"""

    def get_heading(self) -> float:
        """heading"""

    def set_heading(self, val: float) -> None:
        """heading"""

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
        """0 = single ping, else multi-ping sequence number"""

    def set_multi_ping(self, val: int) -> None:
        """0 = single ping, else multi-ping sequence number"""

    def get_frequency(self) -> float:
        """transmit frequency"""

    def set_frequency(self, val: float) -> None:
        """transmit frequency"""

    def get_sample_rate(self) -> float:
        """sample rate"""

    def set_sample_rate(self, val: float) -> None:
        """sample rate"""

    def get_receiver_bandwidth(self) -> float:
        """receiver bandwidth"""

    def set_receiver_bandwidth(self, val: float) -> None:
        """receiver bandwidth"""

    def get_tx_pulse_width(self) -> float:
        """transmit pulse length"""

    def set_tx_pulse_width(self, val: float) -> None:
        """transmit pulse length"""

    def get_tx_pulse_type(self) -> int:
        """0 = CW, 1 = chirp"""

    def set_tx_pulse_type(self, val: int) -> None:
        """0 = CW, 1 = chirp"""

    def get_tx_pulse_envelope(self) -> int:
        """envelope/window type (0-4)"""

    def set_tx_pulse_envelope(self, val: int) -> None:
        """envelope/window type (0-4)"""

    def get_tx_pulse_envelope_parameter(self) -> float:
        """envelope parameter"""

    def set_tx_pulse_envelope_parameter(self, val: float) -> None:
        """envelope parameter"""

    def get_tx_pulse_mode(self) -> int:
        """1-4 (single/multi-ping mode)"""

    def set_tx_pulse_mode(self, val: int) -> None:
        """1-4 (single/multi-ping mode)"""

    def get_max_ping_rate(self) -> float:
        """maximum ping rate"""

    def set_max_ping_rate(self, val: float) -> None:
        """maximum ping rate"""

    def get_ping_period(self) -> float:
        """time since previous ping"""

    def set_ping_period(self, val: float) -> None:
        """time since previous ping"""

    def get_range_selection(self) -> float:
        """range selection"""

    def set_range_selection(self, val: float) -> None:
        """range selection"""

    def get_power_selection(self) -> float:
        """power selection (dB re 1 uPa)"""

    def set_power_selection(self, val: float) -> None:
        """power selection (dB re 1 uPa)"""

    def get_gain_selection(self) -> float:
        """gain selection"""

    def set_gain_selection(self, val: float) -> None:
        """gain selection"""

    def get_control_flags(self) -> int:
        """control flags bit field"""

    def set_control_flags(self, val: int) -> None:
        """control flags bit field"""

    def get_projector_id(self) -> int:
        """transmit projector identifier"""

    def set_projector_id(self, val: int) -> None:
        """transmit projector identifier"""

    def get_steering_vertical(self) -> float:
        """transmit steering angle vertical"""

    def set_steering_vertical(self, val: float) -> None:
        """transmit steering angle vertical"""

    def get_steering_horizontal(self) -> float:
        """transmit steering angle horizontal"""

    def set_steering_horizontal(self, val: float) -> None:
        """transmit steering angle horizontal"""

    def get_beamwidth_vertical(self) -> float:
        """transmit -3dB beam width vertical"""

    def set_beamwidth_vertical(self, val: float) -> None:
        """transmit -3dB beam width vertical"""

    def get_beamwidth_horizontal(self) -> float:
        """transmit -3dB beam width horizontal"""

    def set_beamwidth_horizontal(self, val: float) -> None:
        """transmit -3dB beam width horizontal"""

    def get_focal_point(self) -> float:
        """transmit focal point"""

    def set_focal_point(self, val: float) -> None:
        """transmit focal point"""

    def get_projector_weighting(self) -> int:
        """projector weighting window type (0-2)"""

    def set_projector_weighting(self, val: int) -> None:
        """projector weighting window type (0-2)"""

    def get_projector_weighting_parameter(self) -> float:
        """projector weighting parameter"""

    def set_projector_weighting_parameter(self, val: float) -> None:
        """projector weighting parameter"""

    def get_transmit_flags(self) -> int:
        """transmit flags bit field"""

    def set_transmit_flags(self, val: int) -> None:
        """transmit flags bit field"""

    def get_hydrophone_id(self) -> int:
        """receiver hydrophone identifier"""

    def set_hydrophone_id(self, val: int) -> None:
        """receiver hydrophone identifier"""

    def get_rx_weighting(self) -> int:
        """receiver weighting window type (0-1)"""

    def set_rx_weighting(self, val: int) -> None:
        """receiver weighting window type (0-1)"""

    def get_rx_weighting_parameter(self) -> float:
        """receiver weighting parameter"""

    def set_rx_weighting_parameter(self, val: float) -> None:
        """receiver weighting parameter"""

    def get_rx_flags(self) -> int:
        """receiver flags bit field"""

    def set_rx_flags(self, val: int) -> None:
        """receiver flags bit field"""

    def get_rx_width(self) -> float:
        """receiver beam width"""

    def set_rx_width(self, val: float) -> None:
        """receiver beam width"""

    def get_range_minimum(self) -> float:
        """bottom detection minimum range"""

    def set_range_minimum(self, val: float) -> None:
        """bottom detection minimum range"""

    def get_range_maximum(self) -> float:
        """bottom detection maximum range"""

    def set_range_maximum(self, val: float) -> None:
        """bottom detection maximum range"""

    def get_depth_minimum(self) -> float:
        """bottom detection minimum depth"""

    def set_depth_minimum(self, val: float) -> None:
        """bottom detection minimum depth"""

    def get_depth_maximum(self) -> float:
        """bottom detection maximum depth"""

    def set_depth_maximum(self, val: float) -> None:
        """bottom detection maximum depth"""

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

    def get_operation(self) -> int:
        """0 = off, 1 = on"""

    def set_operation(self, val: int) -> None:
        """0 = off, 1 = on"""

    def get_start_frequency(self) -> float:
        """start frequency"""

    def set_start_frequency(self, val: float) -> None:
        """start frequency"""

    def get_end_frequency(self) -> float:
        """end frequency"""

    def set_end_frequency(self, val: float) -> None:
        """end frequency"""

    def get_window_type(self) -> int:
        """window type (0-5)"""

    def set_window_type(self, val: int) -> None:
        """window type (0-5)"""

    def get_shading(self) -> float:
        """shading value"""

    def set_shading(self, val: float) -> None:
        """shading value"""

    def get_effective_pulse_width(self) -> float:
        """post-compression effective pulse width"""

    def set_effective_pulse_width(self, val: float) -> None:
        """post-compression effective pulse width"""

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
        """water sound velocity"""

    def set_sound_velocity(self, val: float) -> None:
        """water sound velocity"""

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
        """absorption loss"""

    def set_absorption_loss(self, val: float) -> None:
        """absorption loss"""

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
        """spreading loss (0-60)"""

    def set_spreading_loss(self, val: float) -> None:
        """spreading loss (0-60)"""

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
        """flags bit field (uncertainty method, multi-detect, ...)"""

    def set_flags(self, val: int) -> None:
        """flags bit field (uncertainty method, multi-detect, ...)"""

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

    @property
    def beams(self) -> RawDetectionBeamContainer:
        """per-beam raw detections"""

    @beams.setter
    def beams(self, arg: RawDetectionBeamContainer, /) -> None: ...

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

    def get_has_phase(self) -> bool: ...

    def get_magnitude_is_db(self) -> bool: ...

    def get_magnitude_bytes(self) -> int:
        """number of bytes per magnitude sample as stored on disk (1, 2 or 4)"""

    @property
    def beams(self) -> CompressedWaterColumnBeamContainer:
        """per-beam magnitude/phase data"""

    @beams.setter
    def beams(self, arg: CompressedWaterColumnBeamContainer, /) -> None: ...

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

    def get_has_tx_delay(self) -> bool: ...

    def get_tx_delay(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

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
    7k record Attitude: a set of attitude samples (roll, pitch, heave,
    heading) with a time offset relative to the record timestamp. Used by
    modern systems (e.g. R2Sonic) instead of separate 1012/1013 records.
    """

    def __init__(self) -> None: ...

    def get_number_of_samples(self) -> int: ...

    @property
    def samples(self) -> AttitudeSampleContainer:
        """attitude samples"""

    @samples.setter
    def samples(self, arg: AttitudeSampleContainer, /) -> None: ...

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
