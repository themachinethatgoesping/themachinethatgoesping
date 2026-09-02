"""Classes related to Teledyne RESON .s7k (7k) data files"""

from collections.abc import Mapping, Sequence
import enum
from typing import Final, overload

from themachinethatgoesping.echosounders_nanopy.s7k import (
    datagrams as datagrams,
    filedatacontainers as filedatacontainers,
    filedatainterfaces as filedatainterfaces
)
import themachinethatgoesping.tools_nanopy.progressbars


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
    def datagram_interface(self) -> filedatainterfaces.S7KDatagramInterface_stream: ...

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
    def datagram_interface(self) -> filedatainterfaces.S7KDatagramInterface: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
