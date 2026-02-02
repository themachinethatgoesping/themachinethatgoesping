"""
Classes related to Kongsberg KongsbergAll data files (old Kongsberg .all / .wcd format, used until SIS 4.0)
"""

from collections.abc import Mapping, Sequence
import enum
from typing import overload

from . import (
    datagrams as datagrams,
    filedatacontainers as filedatacontainers,
    filedatainterfaces as filedatainterfaces,
    filetypes as filetypes
)
import themachinethatgoesping.tools_nanopy.progressbars


class t_KongsbergAllDatagramIdentifier(enum.Enum):
    XYZDatagram = 88

    ExtraDetections = 108

    RawRangeAndAngle = 78

    SeabedImageData = 89

    WatercolumnDatagram = 107

    QualityFactorDatagram = 79

    AttitudeDatagram = 65

    NetworkAttitudeVelocityDatagram = 110

    ClockDatagram = 67

    DepthOrHeightDatagram = 104

    HeadingDatagram = 72

    PositionDatagram = 80

    SingleBeamEchoSounderDepth = 69

    SurfaceSoundSpeedDatagram = 71

    SoundSpeedProfileDatagram = 85

    InstallationParametersStart = 73

    InstallationParametersStop = 105

    RuntimeParameters = 82

    ExtraParameters = 51

    PUStatusOutput = 49

    PUIDOutput = 48

    unspecified = 0

class t_KongsbergAllActiveSensor(enum.Enum):
    """
    This enum is used to identify the active sensor in the
    InstallationParameters datagram
    """

    PositionSystem3 = 0
    """UDP2 or COM4"""

    PositionSystem1 = 1
    """COM1"""

    PositionSystem2 = 32

    MotionSensor1 = 2
    """COM2"""

    MotionSensor2 = 3
    """COM3"""

    MultiCast1 = 5

    MultiCast2 = 6

    MultiCast3 = 7

    AttitudeVelocitySensor1 = 8
    """UDP5"""

    AttitudeVelocitySensor2 = 9
    """UDP6"""

    NotSet = -1
    """this is not a valid value"""

class t_KongsbergAllSystemTransducerConfiguration(enum.Enum):
    """
    This enum is used to identify the transducer configuration (STC field)
    in the InstallationParameters datagram
    """

    SingleTXSingleRX = 0
    """EM122, EM302, EM710, EM2040 Single"""

    SingleHead = 1
    """EM3002 Single Head, EM2040C Single Head"""

    DualHead = 2
    """EM3002 Dual Head, EM2040C Dual Head"""

    SingleTXDualRX = 3
    """EM2040 Dual RX"""

    DualTXDualRX = 4
    """EM2040 Dual TX"""

    PortableSingleHead = 5
    """EM2040P"""

    Modular = 6
    """EM2040M"""

def datagram_type_to_string(datagram_type: t_KongsbergAllDatagramIdentifier) -> str: ...

def KongsbergAllDatagram_type_from_string(datagram_type: str) -> t_KongsbergAllDatagramIdentifier: ...

class KongsbergAllFileHandler_stream:
    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None: ...

    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None: ...

    @overload
    def __init__(self, file_path: Sequence[str], index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None: ...

    @overload
    def __init__(self, file_paths: Sequence[str], index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None: ...

    def get_index_paths(self) -> dict[str, str]: ...

    @overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None: ...

    @overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None: ...

    @property
    def datagram_interface(self) -> filedatainterfaces.KongsbergAllDatagramInterface_stream: ...

    @property
    def datagramdata_interface(self) -> filedatainterfaces.KongsbergAllDatagramDataInterface_stream: ...

    @property
    def configuration_interface(self) -> filedatainterfaces.KongsbergAllConfigurationDataInterface_stream: ...

    @property
    def navigation_interface(self) -> filedatainterfaces.KongsbergAllNavigationDataInterface_stream: ...

    @property
    def environment_interface(self) -> filedatainterfaces.KongsbergAllEnvironmentDataInterface_stream: ...

    @property
    def otherfiledata_interface(self) -> filedatainterfaces.KongsbergAllOtherFileDataInterface_stream: ...

    @property
    def ping_interface(self) -> filedatainterfaces.KongsbergAllPingDataInterface_stream: ...

    def get_pings(self, sorted_by_time: bool = True) -> filedatacontainers.KongsbergAllPingContainer_stream: ...

    def get_channel_ids(self) -> list[str]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class KongsbergAllFileHandler:
    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None: ...

    @overload
    def __init__(self, file_path: str, index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None: ...

    @overload
    def __init__(self, file_path: Sequence[str], index_paths: Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None: ...

    @overload
    def __init__(self, file_paths: Sequence[str], index_paths: Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None: ...

    def get_index_paths(self) -> dict[str, str]: ...

    @overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None: ...

    @overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None: ...

    @property
    def datagram_interface(self) -> filedatainterfaces.KongsbergAllDatagramInterface: ...

    @property
    def datagramdata_interface(self) -> filedatainterfaces.KongsbergAllDatagramDataInterface: ...

    @property
    def configuration_interface(self) -> filedatainterfaces.KongsbergAllConfigurationDataInterface: ...

    @property
    def navigation_interface(self) -> filedatainterfaces.KongsbergAllNavigationDataInterface: ...

    @property
    def environment_interface(self) -> filedatainterfaces.KongsbergAllEnvironmentDataInterface: ...

    @property
    def otherfiledata_interface(self) -> filedatainterfaces.KongsbergAllOtherFileDataInterface: ...

    @property
    def ping_interface(self) -> filedatainterfaces.KongsbergAllPingDataInterface: ...

    def get_pings(self, sorted_by_time: bool = True) -> filedatacontainers.KongsbergAllPingContainer: ...

    def get_channel_ids(self) -> list[str]: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
