"""Classes related to Teledyne RESON .s7k (7k) data files"""
import typing

from collections.abc import Mapping, Sequence
import enum
from typing import Annotated, Final, overload

import numpy
from numpy.typing import NDArray

import themachinethatgoesping.tools_nanopy.progressbars
import themachinethatgoesping.tools_nanopy.pyhelper


class t_S7KDatagramIdentifier(enum.Enum):
    """
    7k record type identifiers (the "record type" field of the Data Record
    Frame).

    The underlying value is the numeric record type as defined by the 7k
    specification. The enum only lists the record types that are
    known/named; unknown record types are still representable because the
    underlying type can hold any 32-bit value.
    """

    ReferencePoint = 1000
    """1000 - Reference point"""

    SensorOffsetPosition = 1001
    """1001 - Sensor offset position"""

    SensorOffsetPositionCalibrated = 1002
    """1002 - Sensor offset position calibrated"""

    Position = 1003
    """1003 - Position"""

    CustomAttitudeInformation = 1004
    """1004 - Custom attitude information"""

    Tide = 1005
    """1005 - Tide"""

    Altitude = 1006
    """1006 - Altitude"""

    MotionOverGround = 1007
    """1007 - Motion over ground"""

    Depth = 1008
    """1008 - Depth"""

    SoundVelocityProfile = 1009
    """1009 - Sound velocity profile"""

    CTD = 1010
    """1010 - CTD"""

    Geodesy = 1011
    """1011 - Geodesy"""

    RollPitchHeave = 1012
    """1012 - Roll pitch heave"""

    Heading = 1013
    """1013 - Heading"""

    SurveyLine = 1014
    """1014 - Survey line"""

    Navigation = 1015
    """1015 - Navigation"""

    Attitude = 1016
    """1016 - Attitude"""

    PanTilt = 1017
    """1017 - Pan tilt"""

    SonarInstallationIdentifiers = 1020
    """1020 - Sonar installation identifiers"""

    SonarPipeEnvironment = 2004
    """2004 - Sonar pipe environment"""

    ContactOutput = 3001
    """3001 - Contact output"""

    SonarSettings = 7000
    """7000 - 7k sonar settings"""

    Configuration = 7001
    """7001 - 7k configuration"""

    MatchFilter = 7002
    """7002 - 7k match filter"""

    FirmwareAndHardwareConfiguration = 7003
    """7003 - 7k firmware and hardware configuration"""

    BeamGeometry = 7004
    """7004 - 7k beam geometry"""

    BathymetricData = 7006
    """7006 - 7k bathymetric data (deprecated, superseded by 7027)"""

    SideScanData = 7007
    """7007 - 7k side-scan data"""

    GenericWaterColumnData = 7008
    """
    7008 - 7k generic water column data (deprecated, superseded by 7018/7028)
    """

    VerticalDepth = 7009
    """7009 - Vertical depth"""

    TVGValues = 7010
    """7010 - TVG values"""

    ImageData = 7011
    """7011 - 7k image data"""

    PingMotionData = 7012
    """7012 - 7k ping motion data"""

    AdaptiveGate = 7014
    """7014 - 7k adaptive gate"""

    DetectionDataSetup = 7017
    """7017 - 7k detection data setup (deprecated)"""

    BeamformedData = 7018
    """7018 - 7k beamformed data (water column magnitude & phase)"""

    BuiltInTestEnvironmentData = 7021
    """7021 - 7k built-in test environment data (BITE)"""

    SonarSourceVersion = 7022
    """7022 - 7k sonar source version"""

    WetEndVersion8k = 7023
    """7023 - 8k wet end version"""

    DetectionData = 7026
    """7026 - 7k detection data"""

    RawDetectionData = 7027
    """7027 - 7k raw detection data (bathymetry, preferred)"""

    SnippetData = 7028
    """7028 - 7k snippet data (water column)"""

    VernierProcessingDataFiltered = 7029
    """7029 - Vernier processing data (filtered)"""

    SonarInstallationParameters = 7030
    """7030 - Sonar installation parameters"""

    BuiltInTestEnvironmentDataSummary = 7031
    """7031 - 7k built-in test environment data (summary)"""

    CompressedBeamformedIntensityData = 7041
    """7041 - Compressed beamformed intensity data"""

    CompressedWaterColumnData = 7042
    """7042 - Compressed water column data"""

    SegmentedRawDetectionData = 7047
    """7047 - 7k segmented raw detection data"""

    CalibratedBeamData = 7048
    """7048 - 7k calibrated beam data"""

    SystemEvents = 7050
    """7050 - 7k system events"""

    SystemEventMessage = 7051
    """7051 - 7k system event message"""

    RDRRecordingStatus = 7052
    """7052 - RDR recording status"""

    Subscriptions = 7053
    """7053 - 7k subscriptions"""

    NormalizationStatus = 7055
    """7055 - Normalization status"""

    CalibratedSideScanData = 7057
    """7057 - Calibrated side-scan data"""

    SnippetBackscatteringStrength = 7058
    """7058 - Snippet backscattering strength"""

    MB2SpecificStatus = 7059
    """7059 - MB2 specific status"""

    FileHeader = 7200
    """7200 - 7k file header"""

    FileCatalogRecord = 7300
    """7300 - 7k file catalogue record"""

    TimeMessage = 7400
    """7400 - 7k time message"""

    RemoteControl = 7500
    """7500 - 7k remote control"""

    RemoteControlAcknowledge = 7501
    """7501 - 7k remote control acknowledge"""

    RemoteControlNotAcknowledge = 7502
    """7502 - 7k remote control not acknowledge"""

    RemoteControlSonarSettings = 7503
    """7503 - 7k remote control sonar settings"""

    SensorSettings7P = 7504
    """7504 - 7P sensor settings"""

    SVFiltering = 7510
    """7510 - SV filtering"""

    SystemLockStatus = 7511
    """7511 - System lock status"""

    Timestamp = 7515
    """7515 - Timestamp"""

    SoundVelocity = 7610
    """7610 - 7k sound velocity"""

    AbsorptionLoss = 7611
    """7611 - 7k absorption loss"""

    SpreadingLoss = 7612
    """7612 - 7k spreading loss"""

    ProfileAverageSalinity = 7613
    """7613 - Profile average salinity"""

    ProfileAverageTemperature = 7614
    """7614 - Profile average temperature"""

    FillerRecord = 7777
    """7777 - Filler record (used when repairing corrupt files)"""

    Sonar8kSeriesData = 8100
    """8100 - 8k series sonar data"""

    unspecified = 4294967295
    """unknown record type"""

class o_S7KDatagramIdentifier:
    """
    Helper class to convert between strings and enum values of type 't_S7KDatagramIdentifier'
    """

    @overload
    def __init__(self, value: t_S7KDatagramIdentifier = t_S7KDatagramIdentifier.ReferencePoint) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None: ...

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> t_S7KDatagramIdentifier:
        """enum value"""

    @value.setter
    def value(self, arg: t_S7KDatagramIdentifier, /) -> None: ...

    __default_value__: Final[t_S7KDatagramIdentifier] = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_S7KDatagramIdentifier, /) -> bool: ...

    @overload
    def __eq__(self, arg: t_S7KDatagramIdentifier, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_S7KDatagramIdentifier:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_S7KDatagramIdentifier: ...

    def __deepcopy__(self, arg: dict, /) -> o_S7KDatagramIdentifier: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_S7KDatagramIdentifier:
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

def datagram_type_to_string(datagram_type: t_S7KDatagramIdentifier) -> str:
    """
    Convert a record type identifier to a descriptive name.
    Args:
        value: Record type identifier.

    Returns:
        The record type name (e.g. "RawDetectionData") or "unknown" if not
        a named type.
    """

def S7KDatagram_type_from_string(value: str) -> t_S7KDatagramIdentifier:
    """
    Parse a record type identifier from its numeric string representation.
    Args:
        value: String containing the decimal record number (e.g. "7027").

    Returns:
        Parsed record type identifier.
    """

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

    def get_protocol_version(self) -> int: ...

    def get_offset(self) -> int: ...

    def get_sync_pattern(self) -> int: ...

    def get_size(self) -> int: ...

    def get_optional_data_offset(self) -> int: ...

    def get_optional_data_identifier(self) -> int: ...

    def get_year(self) -> int: ...

    def get_day(self) -> int: ...

    def get_seconds(self) -> float: ...

    def get_hours(self) -> int: ...

    def get_minutes(self) -> int: ...

    def get_record_version(self) -> int: ...

    def get_record_type_identifier(self) -> int: ...

    def get_device_identifier(self) -> int: ...

    def get_system_enumerator(self) -> int: ...

    def get_flags(self) -> int: ...

    def get_datagram_identifier(self) -> o_S7KDatagramIdentifier: ...

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

    def get_raw_content(self) -> str: ...

    def set_raw_content(self, value: str) -> None: ...

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

class ReferencePoint(S7KDatagram):
    """7k record ReferencePoint"""

    def __init__(self) -> None: ...

    def get_offset_x(self) -> float: ...

    def set_offset_x(self, val: float) -> None: ...

    def get_offset_y(self) -> float: ...

    def set_offset_y(self, val: float) -> None: ...

    def get_offset_z(self) -> float: ...

    def set_offset_z(self, val: float) -> None: ...

    def get_water_z(self) -> float: ...

    def set_water_z(self, val: float) -> None: ...

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

    def get_datum(self) -> int: ...

    def set_datum(self, val: int) -> None: ...

    def get_latency(self) -> float: ...

    def set_latency(self, val: float) -> None: ...

    def get_latitude_northing(self) -> float: ...

    def set_latitude_northing(self, val: float) -> None: ...

    def get_longitude_easting(self) -> float: ...

    def set_longitude_easting(self, val: float) -> None: ...

    def get_height(self) -> float: ...

    def set_height(self, val: float) -> None: ...

    def get_position_type(self) -> int: ...

    def set_position_type(self, val: int) -> None: ...

    def get_utm_zone(self) -> int: ...

    def set_utm_zone(self, val: int) -> None: ...

    def get_quality(self) -> int: ...

    def set_quality(self, val: int) -> None: ...

    def get_position_method(self) -> int: ...

    def set_position_method(self, val: int) -> None: ...

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

    def get_roll(self) -> float: ...

    def set_roll(self, val: float) -> None: ...

    def get_pitch(self) -> float: ...

    def set_pitch(self, val: float) -> None: ...

    def get_heave(self) -> float: ...

    def set_heave(self, val: float) -> None: ...

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

    def get_heading(self) -> float: ...

    def set_heading(self, val: float) -> None: ...

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

    def get_vertical_reference(self) -> int: ...

    def set_vertical_reference(self, val: int) -> None: ...

    def get_latitude(self) -> float: ...

    def set_latitude(self, val: float) -> None: ...

    def get_longitude(self) -> float: ...

    def set_longitude(self, val: float) -> None: ...

    def get_position_accuracy(self) -> float: ...

    def set_position_accuracy(self, val: float) -> None: ...

    def get_height(self) -> float: ...

    def set_height(self, val: float) -> None: ...

    def get_height_accuracy(self) -> float: ...

    def set_height_accuracy(self, val: float) -> None: ...

    def get_speed(self) -> float: ...

    def set_speed(self, val: float) -> None: ...

    def get_course(self) -> float: ...

    def set_course(self, val: float) -> None: ...

    def get_heading(self) -> float: ...

    def set_heading(self, val: float) -> None: ...

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

    def get_serial_number(self) -> int: ...

    def set_serial_number(self, val: int) -> None: ...

    def get_ping_number(self) -> int: ...

    def set_ping_number(self, val: int) -> None: ...

    def get_multi_ping(self) -> int: ...

    def set_multi_ping(self, val: int) -> None: ...

    def get_frequency(self) -> float: ...

    def set_frequency(self, val: float) -> None: ...

    def get_sample_rate(self) -> float: ...

    def set_sample_rate(self, val: float) -> None: ...

    def get_receiver_bandwidth(self) -> float: ...

    def set_receiver_bandwidth(self, val: float) -> None: ...

    def get_tx_pulse_width(self) -> float: ...

    def set_tx_pulse_width(self, val: float) -> None: ...

    def get_tx_pulse_type(self) -> int: ...

    def set_tx_pulse_type(self, val: int) -> None: ...

    def get_tx_pulse_envelope(self) -> int: ...

    def set_tx_pulse_envelope(self, val: int) -> None: ...

    def get_tx_pulse_envelope_parameter(self) -> float: ...

    def set_tx_pulse_envelope_parameter(self, val: float) -> None: ...

    def get_tx_pulse_mode(self) -> int: ...

    def set_tx_pulse_mode(self, val: int) -> None: ...

    def get_max_ping_rate(self) -> float: ...

    def set_max_ping_rate(self, val: float) -> None: ...

    def get_ping_period(self) -> float: ...

    def set_ping_period(self, val: float) -> None: ...

    def get_range_selection(self) -> float: ...

    def set_range_selection(self, val: float) -> None: ...

    def get_power_selection(self) -> float: ...

    def set_power_selection(self, val: float) -> None: ...

    def get_gain_selection(self) -> float: ...

    def set_gain_selection(self, val: float) -> None: ...

    def get_control_flags(self) -> int: ...

    def set_control_flags(self, val: int) -> None: ...

    def get_projector_id(self) -> int: ...

    def set_projector_id(self, val: int) -> None: ...

    def get_steering_vertical(self) -> float: ...

    def set_steering_vertical(self, val: float) -> None: ...

    def get_steering_horizontal(self) -> float: ...

    def set_steering_horizontal(self, val: float) -> None: ...

    def get_beamwidth_vertical(self) -> float: ...

    def set_beamwidth_vertical(self, val: float) -> None: ...

    def get_beamwidth_horizontal(self) -> float: ...

    def set_beamwidth_horizontal(self, val: float) -> None: ...

    def get_focal_point(self) -> float: ...

    def set_focal_point(self, val: float) -> None: ...

    def get_projector_weighting(self) -> int: ...

    def set_projector_weighting(self, val: int) -> None: ...

    def get_projector_weighting_parameter(self) -> float: ...

    def set_projector_weighting_parameter(self, val: float) -> None: ...

    def get_transmit_flags(self) -> int: ...

    def set_transmit_flags(self, val: int) -> None: ...

    def get_hydrophone_id(self) -> int: ...

    def set_hydrophone_id(self, val: int) -> None: ...

    def get_rx_weighting(self) -> int: ...

    def set_rx_weighting(self, val: int) -> None: ...

    def get_rx_weighting_parameter(self) -> float: ...

    def set_rx_weighting_parameter(self, val: float) -> None: ...

    def get_rx_flags(self) -> int: ...

    def set_rx_flags(self, val: int) -> None: ...

    def get_rx_width(self) -> float: ...

    def set_rx_width(self, val: float) -> None: ...

    def get_range_minimum(self) -> float: ...

    def set_range_minimum(self, val: float) -> None: ...

    def get_range_maximum(self) -> float: ...

    def set_range_maximum(self, val: float) -> None: ...

    def get_depth_minimum(self) -> float: ...

    def set_depth_minimum(self, val: float) -> None: ...

    def get_depth_maximum(self) -> float: ...

    def set_depth_maximum(self, val: float) -> None: ...

    def get_absorption(self) -> float: ...

    def set_absorption(self, val: float) -> None: ...

    def get_sound_velocity(self) -> float: ...

    def set_sound_velocity(self, val: float) -> None: ...

    def get_spreading(self) -> float: ...

    def set_spreading(self, val: float) -> None: ...

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

    def get_serial_number(self) -> int: ...

    def set_serial_number(self, val: int) -> None: ...

    def get_ping_number(self) -> int: ...

    def set_ping_number(self, val: int) -> None: ...

    def get_operation(self) -> int: ...

    def set_operation(self, val: int) -> None: ...

    def get_start_frequency(self) -> float: ...

    def set_start_frequency(self, val: float) -> None: ...

    def get_end_frequency(self) -> float: ...

    def set_end_frequency(self, val: float) -> None: ...

    def get_window_type(self) -> int: ...

    def set_window_type(self, val: int) -> None: ...

    def get_shading(self) -> float: ...

    def set_shading(self, val: float) -> None: ...

    def get_effective_pulse_width(self) -> float: ...

    def set_effective_pulse_width(self, val: float) -> None: ...

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

    def get_sound_velocity(self) -> float: ...

    def set_sound_velocity(self, val: float) -> None: ...

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

    def get_absorption_loss(self) -> float: ...

    def set_absorption_loss(self, val: float) -> None: ...

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

    def get_spreading_loss(self) -> float: ...

    def set_spreading_loss(self, val: float) -> None: ...

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

    def get_serial_number(self) -> int: ...

    def get_ping_number(self) -> int: ...

    def get_multi_ping(self) -> int: ...

    def get_number_beams(self) -> int: ...

    def get_data_field_size(self) -> int: ...

    def get_detection_algorithm(self) -> int: ...

    def get_flags(self) -> int: ...

    def get_sampling_rate(self) -> float: ...

    def get_tx_angle(self) -> float: ...

    def get_applied_roll(self) -> float: ...

    def get_beam_descriptor(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]: ...

    def get_detection_point(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_rx_angle(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_beam_flags(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_quality(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_uncertainty(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_signal_strength(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_min_limit(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_max_limit(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

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

class Snippet(S7KDatagram):
    """
    7k record SnippetData: water-column intensity snippets around each
    beam detection.

    The record holds, per beam, a short intensity time series (snippet)
    around the bottom detection. The intensity samples are 16- or 32-bit
    depending on bit 0 of the flags field.
    """

    def __init__(self) -> None: ...

    def get_serial_number(self) -> int: ...

    def get_ping_number(self) -> int: ...

    def get_multi_ping(self) -> int: ...

    def get_number_beams(self) -> int: ...

    def get_error_flag(self) -> int: ...

    def get_control_flags(self) -> int: ...

    def get_flags(self) -> int: ...

    def get_samples_are_32bit(self) -> bool:
        """
        true if the intensity samples are stored as 32-bit values (flags bit
        0)
        """

    def get_beam_descriptor(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]: ...

    def get_snippet_start(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_detection_sample(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_snippet_end(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_amplitudes(self) -> list[Annotated[NDArray[numpy.uint32], dict(order='C')]]:
        """intensity snippet arrays (one per beam)"""

    def get_beam_amplitudes(self, beam_index: int) -> Annotated[NDArray[numpy.uint32], dict(order='C')]:
        """intensity snippet of a single beam"""

    def __eq__(self, other: Snippet) -> bool: ...

    def copy(self) -> Snippet:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> Snippet: ...

    def __deepcopy__(self, arg: dict, /) -> Snippet: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Snippet:
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

    def get_serial_number(self) -> int: ...

    def get_ping_number(self) -> int: ...

    def get_multi_ping(self) -> int: ...

    def get_number_beams(self) -> int: ...

    def get_samples(self) -> int: ...

    def get_compressed_samples(self) -> int: ...

    def get_flags(self) -> int: ...

    def get_first_sample(self) -> int: ...

    def get_sample_rate(self) -> float: ...

    def get_compression_factor(self) -> float: ...

    def get_has_phase(self) -> bool: ...

    def get_magnitude_is_db(self) -> bool: ...

    def get_magnitude_bytes(self) -> int:
        """number of bytes per magnitude sample as stored on disk (1, 2 or 4)"""

    def get_beam_number(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]: ...

    def get_segment_number(self) -> Annotated[NDArray[numpy.uint8], dict(order='C')]: ...

    def get_sample_count(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_magnitude(self) -> list[Annotated[NDArray[numpy.float32], dict(order='C')]]:
        """magnitude arrays, one per beam (dB if get_magnitude_is_db(), else raw)"""

    def get_phase(self) -> list[Annotated[NDArray[numpy.float32], dict(order='C')]]:
        """phase arrays in radians, one per beam (empty if magnitude-only)"""

    def get_beam_magnitude(self, beam_index: int) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """magnitude array of a single beam"""

    def get_beam_phase(self, beam_index: int) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """phase array (radians) of a single beam"""

    def get_magnitude_in_db(self) -> list[Annotated[NDArray[numpy.float32], dict(order='C')]]:
        """
        magnitude in dB, one array per beam (already-dB values returned unchanged, else 20*log10(mag/65535); 0 -> -inf)
        """

    def get_phase_in_degrees(self) -> list[Annotated[NDArray[numpy.float32], dict(order='C')]]:
        """phase in degrees, one array per beam (empty if magnitude-only)"""

    def get_beam_magnitude_in_db(self, beam_index: int) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """magnitude of a single beam in dB (see get_magnitude_in_db)"""

    def get_beam_phase_in_degrees(self, beam_index: int) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """phase of a single beam in degrees"""

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

    def get_serial_number(self) -> int: ...

    def get_number_beams(self) -> int: ...

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

    def get_delta_time(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]: ...

    def get_roll(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_pitch(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_heave(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def get_heading(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

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
    7k record FileHeader: the first record of a .s7k file. Describes the
    file (recording program, session, notes) and lists the devices
    contained in the file.
    """

    def __init__(self) -> None: ...

    def get_version(self) -> int: ...

    def get_record_data_size(self) -> int: ...

    def get_number_devices(self) -> int: ...

    def get_recording_name(self) -> str: ...

    def get_recording_version(self) -> str: ...

    def get_user_defined_name(self) -> str: ...

    def get_notes(self) -> str: ...

    def get_device_identifier(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    def get_system_enumerator(self) -> Annotated[NDArray[numpy.uint16], dict(order='C')]: ...

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

class S7KDatagramContainer_Header_stream:
    def copy(self) -> S7KDatagramContainer_Header_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Header_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Header_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Header_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Header_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Header_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Header_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> S7KDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Header_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Header_stream: ...

class S7KDatagramContainer_Header:
    def copy(self) -> S7KDatagramContainer_Header:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Header: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Header: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Header]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Header: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Header: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Header: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> S7KDatagram: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Header: ...

    def __reversed__(self) -> S7KDatagramContainer_Header: ...

class S7KDatagramContainer_Unknown_stream:
    def copy(self) -> S7KDatagramContainer_Unknown_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Unknown_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Unknown_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Unknown_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Unknown_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Unknown_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Unknown_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> S7KUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Unknown_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Unknown_stream: ...

class S7KDatagramContainer_Unknown:
    def copy(self) -> S7KDatagramContainer_Unknown:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Unknown: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Unknown: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Unknown]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Unknown: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Unknown: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Unknown: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> S7KUnknown: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Unknown: ...

    def __reversed__(self) -> S7KDatagramContainer_Unknown: ...

class S7KDatagramContainer_ReferencePoint_stream:
    def copy(self) -> S7KDatagramContainer_ReferencePoint_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_ReferencePoint_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_ReferencePoint_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_ReferencePoint_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_ReferencePoint_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_ReferencePoint_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_ReferencePoint_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> ReferencePoint: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_ReferencePoint_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_ReferencePoint_stream: ...

class S7KDatagramContainer_ReferencePoint:
    def copy(self) -> S7KDatagramContainer_ReferencePoint:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_ReferencePoint: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_ReferencePoint: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_ReferencePoint]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_ReferencePoint: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_ReferencePoint: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_ReferencePoint: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> ReferencePoint: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_ReferencePoint: ...

    def __reversed__(self) -> S7KDatagramContainer_ReferencePoint: ...

class S7KDatagramContainer_Position_stream:
    def copy(self) -> S7KDatagramContainer_Position_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Position_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Position_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Position_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Position_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Position_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Position_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> Position: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Position_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Position_stream: ...

class S7KDatagramContainer_Position:
    def copy(self) -> S7KDatagramContainer_Position:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Position: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Position: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Position]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Position: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Position: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Position: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> Position: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Position: ...

    def __reversed__(self) -> S7KDatagramContainer_Position: ...

class S7KDatagramContainer_RollPitchHeave_stream:
    def copy(self) -> S7KDatagramContainer_RollPitchHeave_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_RollPitchHeave_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_RollPitchHeave_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_RollPitchHeave_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_RollPitchHeave_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_RollPitchHeave_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_RollPitchHeave_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> RollPitchHeave: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_RollPitchHeave_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_RollPitchHeave_stream: ...

class S7KDatagramContainer_RollPitchHeave:
    def copy(self) -> S7KDatagramContainer_RollPitchHeave:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_RollPitchHeave: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_RollPitchHeave: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_RollPitchHeave]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_RollPitchHeave: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_RollPitchHeave: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_RollPitchHeave: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> RollPitchHeave: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_RollPitchHeave: ...

    def __reversed__(self) -> S7KDatagramContainer_RollPitchHeave: ...

class S7KDatagramContainer_Heading_stream:
    def copy(self) -> S7KDatagramContainer_Heading_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Heading_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Heading_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Heading_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Heading_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Heading_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Heading_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> Heading: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Heading_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Heading_stream: ...

class S7KDatagramContainer_Heading:
    def copy(self) -> S7KDatagramContainer_Heading:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Heading: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Heading: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Heading]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Heading: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Heading: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Heading: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> Heading: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Heading: ...

    def __reversed__(self) -> S7KDatagramContainer_Heading: ...

class S7KDatagramContainer_Navigation_stream:
    def copy(self) -> S7KDatagramContainer_Navigation_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Navigation_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Navigation_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Navigation_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Navigation_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Navigation_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Navigation_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> Navigation: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Navigation_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Navigation_stream: ...

class S7KDatagramContainer_Navigation:
    def copy(self) -> S7KDatagramContainer_Navigation:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Navigation: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Navigation: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Navigation]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Navigation: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Navigation: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Navigation: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> Navigation: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Navigation: ...

    def __reversed__(self) -> S7KDatagramContainer_Navigation: ...

class S7KDatagramContainer_SonarSettings_stream:
    def copy(self) -> S7KDatagramContainer_SonarSettings_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_SonarSettings_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_SonarSettings_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_SonarSettings_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_SonarSettings_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_SonarSettings_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_SonarSettings_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> SonarSettings: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_SonarSettings_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_SonarSettings_stream: ...

class S7KDatagramContainer_SonarSettings:
    def copy(self) -> S7KDatagramContainer_SonarSettings:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_SonarSettings: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_SonarSettings: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_SonarSettings]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_SonarSettings: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_SonarSettings: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_SonarSettings: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> SonarSettings: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_SonarSettings: ...

    def __reversed__(self) -> S7KDatagramContainer_SonarSettings: ...

class S7KDatagramContainer_MatchFilter_stream:
    def copy(self) -> S7KDatagramContainer_MatchFilter_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_MatchFilter_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_MatchFilter_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_MatchFilter_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_MatchFilter_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_MatchFilter_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_MatchFilter_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> MatchFilter: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_MatchFilter_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_MatchFilter_stream: ...

class S7KDatagramContainer_MatchFilter:
    def copy(self) -> S7KDatagramContainer_MatchFilter:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_MatchFilter: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_MatchFilter: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_MatchFilter]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_MatchFilter: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_MatchFilter: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_MatchFilter: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> MatchFilter: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_MatchFilter: ...

    def __reversed__(self) -> S7KDatagramContainer_MatchFilter: ...

class S7KDatagramContainer_SoundVelocity_stream:
    def copy(self) -> S7KDatagramContainer_SoundVelocity_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_SoundVelocity_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_SoundVelocity_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_SoundVelocity_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_SoundVelocity_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_SoundVelocity_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_SoundVelocity_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> SoundVelocity: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_SoundVelocity_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_SoundVelocity_stream: ...

class S7KDatagramContainer_SoundVelocity:
    def copy(self) -> S7KDatagramContainer_SoundVelocity:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_SoundVelocity: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_SoundVelocity: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_SoundVelocity]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_SoundVelocity: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_SoundVelocity: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_SoundVelocity: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> SoundVelocity: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_SoundVelocity: ...

    def __reversed__(self) -> S7KDatagramContainer_SoundVelocity: ...

class S7KDatagramContainer_AbsorptionLoss_stream:
    def copy(self) -> S7KDatagramContainer_AbsorptionLoss_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_AbsorptionLoss_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> AbsorptionLoss: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_AbsorptionLoss_stream: ...

class S7KDatagramContainer_AbsorptionLoss:
    def copy(self) -> S7KDatagramContainer_AbsorptionLoss:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_AbsorptionLoss: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_AbsorptionLoss: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_AbsorptionLoss]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_AbsorptionLoss: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_AbsorptionLoss: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_AbsorptionLoss: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> AbsorptionLoss: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_AbsorptionLoss: ...

    def __reversed__(self) -> S7KDatagramContainer_AbsorptionLoss: ...

class S7KDatagramContainer_SpreadingLoss_stream:
    def copy(self) -> S7KDatagramContainer_SpreadingLoss_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_SpreadingLoss_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_SpreadingLoss_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_SpreadingLoss_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_SpreadingLoss_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_SpreadingLoss_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_SpreadingLoss_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> SpreadingLoss: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_SpreadingLoss_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_SpreadingLoss_stream: ...

class S7KDatagramContainer_SpreadingLoss:
    def copy(self) -> S7KDatagramContainer_SpreadingLoss:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_SpreadingLoss: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_SpreadingLoss: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_SpreadingLoss]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_SpreadingLoss: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_SpreadingLoss: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_SpreadingLoss: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> SpreadingLoss: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_SpreadingLoss: ...

    def __reversed__(self) -> S7KDatagramContainer_SpreadingLoss: ...

class S7KDatagramContainer_RawDetection_stream:
    def copy(self) -> S7KDatagramContainer_RawDetection_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_RawDetection_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_RawDetection_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_RawDetection_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_RawDetection_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_RawDetection_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_RawDetection_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> RawDetection: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_RawDetection_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_RawDetection_stream: ...

class S7KDatagramContainer_RawDetection:
    def copy(self) -> S7KDatagramContainer_RawDetection:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_RawDetection: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_RawDetection: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_RawDetection]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_RawDetection: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_RawDetection: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_RawDetection: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> RawDetection: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_RawDetection: ...

    def __reversed__(self) -> S7KDatagramContainer_RawDetection: ...

class S7KDatagramContainer_Snippet_stream:
    def copy(self) -> S7KDatagramContainer_Snippet_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Snippet_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Snippet_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Snippet_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Snippet_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Snippet_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Snippet_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> Snippet: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Snippet_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Snippet_stream: ...

class S7KDatagramContainer_Snippet:
    def copy(self) -> S7KDatagramContainer_Snippet:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Snippet: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Snippet: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Snippet]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Snippet: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Snippet: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Snippet: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> Snippet: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Snippet: ...

    def __reversed__(self) -> S7KDatagramContainer_Snippet: ...

class S7KDatagramContainer_CompressedWaterColumn_stream:
    def copy(self) -> S7KDatagramContainer_CompressedWaterColumn_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_CompressedWaterColumn_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> CompressedWaterColumn: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_CompressedWaterColumn_stream: ...

class S7KDatagramContainer_CompressedWaterColumn:
    def copy(self) -> S7KDatagramContainer_CompressedWaterColumn:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_CompressedWaterColumn: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_CompressedWaterColumn: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_CompressedWaterColumn]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_CompressedWaterColumn: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_CompressedWaterColumn: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_CompressedWaterColumn: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> CompressedWaterColumn: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_CompressedWaterColumn: ...

    def __reversed__(self) -> S7KDatagramContainer_CompressedWaterColumn: ...

class S7KDatagramContainer_BeamGeometry_stream:
    def copy(self) -> S7KDatagramContainer_BeamGeometry_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_BeamGeometry_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_BeamGeometry_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_BeamGeometry_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_BeamGeometry_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_BeamGeometry_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_BeamGeometry_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> BeamGeometry: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_BeamGeometry_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_BeamGeometry_stream: ...

class S7KDatagramContainer_BeamGeometry:
    def copy(self) -> S7KDatagramContainer_BeamGeometry:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_BeamGeometry: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_BeamGeometry: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_BeamGeometry]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_BeamGeometry: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_BeamGeometry: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_BeamGeometry: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> BeamGeometry: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_BeamGeometry: ...

    def __reversed__(self) -> S7KDatagramContainer_BeamGeometry: ...

class S7KDatagramContainer_Attitude_stream:
    def copy(self) -> S7KDatagramContainer_Attitude_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Attitude_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Attitude_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Attitude_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Attitude_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Attitude_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Attitude_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> Attitude: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Attitude_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_Attitude_stream: ...

class S7KDatagramContainer_Attitude:
    def copy(self) -> S7KDatagramContainer_Attitude:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_Attitude: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_Attitude: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_Attitude]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_Attitude: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_Attitude: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_Attitude: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> Attitude: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_Attitude: ...

    def __reversed__(self) -> S7KDatagramContainer_Attitude: ...

class S7KDatagramContainer_FileHeader_stream:
    def copy(self) -> S7KDatagramContainer_FileHeader_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_FileHeader_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_FileHeader_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_FileHeader_stream]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_FileHeader_stream: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_FileHeader_stream: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_FileHeader_stream: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> FileHeader: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_FileHeader_stream: ...

    def __reversed__(self) -> S7KDatagramContainer_FileHeader_stream: ...

class S7KDatagramContainer_FileHeader:
    def copy(self) -> S7KDatagramContainer_FileHeader:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KDatagramContainer_FileHeader: ...

    def __deepcopy__(self, arg: dict, /) -> S7KDatagramContainer_FileHeader: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def split_by_time_diff(self, max_time_diff_seconds: float) -> list[S7KDatagramContainer_FileHeader]:
        """
        Split the data if the time difference between two subsequent datagrams
        is larger than arg Note: for this function to make sense the data
        should be sorted_in_time

        Args:
            max_time_diff_seconds:: maximum time difference between two
                                  subsequent datagrams in seconds

        Returns:
            std::vector_DatagramContainer
        """

    def get_sorted_by_time(self) -> S7KDatagramContainer_FileHeader: ...

    def count_datagrams_per_type(self) -> dict[t_S7KDatagramIdentifier, int]: ...

    def find_datagram_types(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def __call__(self, datagram_identifier: t_S7KDatagramIdentifier) -> S7KDatagramContainer_FileHeader: ...

    @overload
    def __call__(self, datagram_identifiers: Sequence[t_S7KDatagramIdentifier]) -> S7KDatagramContainer_FileHeader: ...

    def size(self) -> int: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, index: int) -> FileHeader: ...

    @overload
    def __getitem__(self, slice: themachinethatgoesping.tools_nanopy.pyhelper.PyIndexerSlice) -> S7KDatagramContainer_FileHeader: ...

    def __reversed__(self) -> S7KDatagramContainer_FileHeader: ...

class S7KDatagramInterface_stream:
    """
    Datagram interface for the .s7k (7k) data format. Holds the datagram
    index (position, timestamp and record type of every datagram) and
    provides access to the raw datagrams.
    """

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: o_S7KDatagramIdentifier) -> object: ...

    def datagrams(self, datagram_type: o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface_stream]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KDatagramInterface:
    """
    Datagram interface for the .s7k (7k) data format. Holds the datagram
    index (position, timestamp and record type of every datagram) and
    provides access to the raw datagrams.
    """

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: o_S7KDatagramIdentifier) -> object: ...

    def datagrams(self, datagram_type: o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[S7KDatagramInterface]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KFileHandler_stream:
    """
    File handler for Teledyne RESON .s7k (7k) data files.

    Indexes all datagrams (Data Record Frames) in the given file(s) and
    provides access to the raw datagrams via the datagram_interface().
    """

    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, mp_cores: int = 1) -> None: ...

    @overload
    def __init__(self, file_path: Sequence[str], index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def __init__(self, file_paths: Sequence[str], index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, mp_cores: int = 1) -> None: ...

    def get_index_paths(self) -> dict[str, str]: ...

    @overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, mp_cores: int = 1) -> None: ...

    @property
    def datagram_interface(self) -> S7KDatagramInterface_stream: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class S7KFileHandler:
    """
    File handler for Teledyne RESON .s7k (7k) data files.

    Indexes all datagrams (Data Record Frames) in the given file(s) and
    provides access to the raw datagrams via the datagram_interface().
    """

    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, mp_cores: int = 1) -> None: ...

    @overload
    def __init__(self, file_path: Sequence[str], index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def __init__(self, file_paths: Sequence[str], index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, mp_cores: int = 1) -> None: ...

    def get_index_paths(self) -> dict[str, str]: ...

    @overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True, mp_cores: int = 1) -> None: ...

    @overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar, mp_cores: int = 1) -> None: ...

    @property
    def datagram_interface(self) -> S7KDatagramInterface: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
