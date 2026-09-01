"""Classes related to Teledyne RESON .s7k (7k) data files"""
import typing

from collections.abc import Mapping, Sequence
import enum
from typing import Final, overload

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

    R1000_ReferencePoint = 1000
    """1000 - Reference point"""

    R1001_SensorOffsetPosition = 1001
    """1001 - Sensor offset position"""

    R1002_SensorOffsetPositionCalibrated = 1002
    """1002 - Sensor offset position calibrated"""

    R1003_Position = 1003
    """1003 - Position"""

    R1004_CustomAttitudeInformation = 1004
    """1004 - Custom attitude information"""

    R1005_Tide = 1005
    """1005 - Tide"""

    R1006_Altitude = 1006
    """1006 - Altitude"""

    R1007_MotionOverGround = 1007
    """1007 - Motion over ground"""

    R1008_Depth = 1008
    """1008 - Depth"""

    R1009_SoundVelocityProfile = 1009
    """1009 - Sound velocity profile"""

    R1010_CTD = 1010
    """1010 - CTD"""

    R1011_Geodesy = 1011
    """1011 - Geodesy"""

    R1012_RollPitchHeave = 1012
    """1012 - Roll pitch heave"""

    R1013_Heading = 1013
    """1013 - Heading"""

    R1014_SurveyLine = 1014
    """1014 - Survey line"""

    R1015_Navigation = 1015
    """1015 - Navigation"""

    R1016_Attitude = 1016
    """1016 - Attitude"""

    R1017_PanTilt = 1017
    """1017 - Pan tilt"""

    R1020_SonarInstallationIdentifiers = 1020
    """1020 - Sonar installation identifiers"""

    R2004_SonarPipeEnvironment = 2004
    """2004 - Sonar pipe environment"""

    R3001_ContactOutput = 3001
    """3001 - Contact output"""

    R7000_SonarSettings = 7000
    """7000 - 7k sonar settings"""

    R7001_Configuration = 7001
    """7001 - 7k configuration"""

    R7002_MatchFilter = 7002
    """7002 - 7k match filter"""

    R7003_FirmwareAndHardwareConfiguration = 7003
    """7003 - 7k firmware and hardware configuration"""

    R7004_BeamGeometry = 7004
    """7004 - 7k beam geometry"""

    R7006_BathymetricData = 7006
    """7006 - 7k bathymetric data (deprecated, superseded by 7027)"""

    R7007_SideScanData = 7007
    """7007 - 7k side-scan data"""

    R7008_GenericWaterColumnData = 7008
    """
    7008 - 7k generic water column data (deprecated, superseded by 7018/7028)
    """

    R7009_VerticalDepth = 7009
    """7009 - Vertical depth"""

    R7010_TVGValues = 7010
    """7010 - TVG values"""

    R7011_ImageData = 7011
    """7011 - 7k image data"""

    R7012_PingMotionData = 7012
    """7012 - 7k ping motion data"""

    R7014_AdaptiveGate = 7014
    """7014 - 7k adaptive gate"""

    R7017_DetectionDataSetup = 7017
    """7017 - 7k detection data setup (deprecated)"""

    R7018_BeamformedData = 7018
    """7018 - 7k beamformed data (water column magnitude & phase)"""

    R7021_BuiltInTestEnvironmentData = 7021
    """7021 - 7k built-in test environment data (BITE)"""

    R7022_SonarSourceVersion = 7022
    """7022 - 7k sonar source version"""

    R7023_WetEndVersion8k = 7023
    """7023 - 8k wet end version"""

    R7026_DetectionData = 7026
    """7026 - 7k detection data"""

    R7027_RawDetectionData = 7027
    """7027 - 7k raw detection data (bathymetry, preferred)"""

    R7028_SnippetData = 7028
    """7028 - 7k snippet data (water column)"""

    R7029_VernierProcessingDataFiltered = 7029
    """7029 - Vernier processing data (filtered)"""

    R7030_SonarInstallationParameters = 7030
    """7030 - Sonar installation parameters"""

    R7031_BuiltInTestEnvironmentDataSummary = 7031
    """7031 - 7k built-in test environment data (summary)"""

    R7041_CompressedBeamformedIntensityData = 7041
    """7041 - Compressed beamformed intensity data"""

    R7042_CompressedWaterColumnData = 7042
    """7042 - Compressed water column data"""

    R7047_SegmentedRawDetectionData = 7047
    """7047 - 7k segmented raw detection data"""

    R7048_CalibratedBeamData = 7048
    """7048 - 7k calibrated beam data"""

    R7050_SystemEvents = 7050
    """7050 - 7k system events"""

    R7051_SystemEventMessage = 7051
    """7051 - 7k system event message"""

    R7052_RDRRecordingStatus = 7052
    """7052 - RDR recording status"""

    R7053_Subscriptions = 7053
    """7053 - 7k subscriptions"""

    R7055_NormalizationStatus = 7055
    """7055 - Normalization status"""

    R7057_CalibratedSideScanData = 7057
    """7057 - Calibrated side-scan data"""

    R7058_SnippetBackscatteringStrength = 7058
    """7058 - Snippet backscattering strength"""

    R7059_MB2SpecificStatus = 7059
    """7059 - MB2 specific status"""

    R7200_FileHeader = 7200
    """7200 - 7k file header"""

    R7300_FileCatalogRecord = 7300
    """7300 - 7k file catalogue record"""

    R7400_TimeMessage = 7400
    """7400 - 7k time message"""

    R7500_RemoteControl = 7500
    """7500 - 7k remote control"""

    R7501_RemoteControlAcknowledge = 7501
    """7501 - 7k remote control acknowledge"""

    R7502_RemoteControlNotAcknowledge = 7502
    """7502 - 7k remote control not acknowledge"""

    R7503_RemoteControlSonarSettings = 7503
    """7503 - 7k remote control sonar settings"""

    R7504_SensorSettings7P = 7504
    """7504 - 7P sensor settings"""

    R7510_SVFiltering = 7510
    """7510 - SV filtering"""

    R7511_SystemLockStatus = 7511
    """7511 - System lock status"""

    R7515_Timestamp = 7515
    """7515 - Timestamp"""

    R7610_SoundVelocity = 7610
    """7610 - 7k sound velocity"""

    R7611_AbsorptionLoss = 7611
    """7611 - 7k absorption loss"""

    R7612_SpreadingLoss = 7612
    """7612 - 7k spreading loss"""

    R7613_ProfileAverageSalinity = 7613
    """7613 - Profile average salinity"""

    R7614_ProfileAverageTemperature = 7614
    """7614 - Profile average temperature"""

    R7777_FillerRecord = 7777
    """7777 - Filler record (used when repairing corrupt files)"""

    R8100_Sonar8kSeriesData = 8100
    """8100 - 8k series sonar data"""

    unspecified = 4294967295
    """unknown record type"""

class o_S7KDatagramIdentifier:
    """
    Helper class to convert between strings and enum values of type 't_S7KDatagramIdentifier'
    """

    @overload
    def __init__(self, value: t_S7KDatagramIdentifier = t_S7KDatagramIdentifier.R1000_ReferencePoint) -> None:
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
        The record type name (e.g. "R7027_RawDetectionData") or "unknown"
        if not a named type.
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

    def get_datagram_identifier(self) -> t_S7KDatagramIdentifier: ...

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
    def datagrams_raw(self, datagram_type: t_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: t_S7KDatagramIdentifier) -> object: ...

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
    def datagrams_raw(self, datagram_type: t_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: t_S7KDatagramIdentifier) -> object: ...

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
