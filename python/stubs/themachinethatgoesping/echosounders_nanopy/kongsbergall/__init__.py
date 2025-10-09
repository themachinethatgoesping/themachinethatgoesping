"""
Classes related to Kongsberg KongsbergAll data files (old Kongsberg .all / .wcd format, used until SIS 4.0)
"""
from __future__ import annotations
import collections.abc
import enum
import typing
from . import datagrams
from . import filedatacontainers
from . import filedatainterfaces
from . import filetypes
__all__: list[str] = ['KongsbergAllDatagram_type_from_string', 'KongsbergAllFileHandler', 'KongsbergAllFileHandler_stream', 'datagram_type_to_string', 'datagrams', 'filedatacontainers', 'filedatainterfaces', 'filetypes', 't_KongsbergAllActiveSensor', 't_KongsbergAllDatagramIdentifier', 't_KongsbergAllSystemTransducerConfiguration']
class KongsbergAllFileHandler:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        """
        __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        __init__(self, file_path: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None
        __init__(self, file_paths: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def get_channel_ids(self) -> list[str]:
        ...
    def get_index_paths(self) -> dict[str, str]:
        ...
    def get_pings(self, sorted_by_time: bool = True) -> filedatacontainers.KongsbergAllPingContainer:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        """
        init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> filedatainterfaces.KongsbergAllAnnotationDataInterface:
        ...
    @property
    def configuration_interface(self) -> filedatainterfaces.KongsbergAllConfigurationDataInterface:
        ...
    @property
    def datagram_interface(self) -> filedatainterfaces.KongsbergAllDatagramInterface:
        ...
    @property
    def datagramdata_interface(self) -> filedatainterfaces.KongsbergAllDatagramDataInterface:
        ...
    @property
    def environment_interface(self) -> filedatainterfaces.KongsbergAllEnvironmentDataInterface:
        ...
    @property
    def navigation_interface(self) -> filedatainterfaces.KongsbergAllNavigationDataInterface:
        ...
    @property
    def otherfiledata_interface(self) -> filedatainterfaces.KongsbergAllOtherFileDataInterface:
        ...
    @property
    def ping_interface(self) -> filedatainterfaces.KongsbergAllPingDataInterface:
        ...
class KongsbergAllFileHandler_stream:
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        """
        __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        __init__(self, file_path: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None
        __init__(self, file_paths: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def get_channel_ids(self) -> list[str]:
        ...
    def get_index_paths(self) -> dict[str, str]:
        ...
    def get_pings(self, sorted_by_time: bool = True) -> filedatacontainers.KongsbergAllPingContainer_stream:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        """
        init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_nanopy.progressbars.I_ProgressBar) -> None
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> filedatainterfaces.KongsbergAllAnnotationDataInterface_stream:
        ...
    @property
    def configuration_interface(self) -> filedatainterfaces.KongsbergAllConfigurationDataInterface_stream:
        ...
    @property
    def datagram_interface(self) -> filedatainterfaces.KongsbergAllDatagramInterface_stream:
        ...
    @property
    def datagramdata_interface(self) -> filedatainterfaces.KongsbergAllDatagramDataInterface_stream:
        ...
    @property
    def environment_interface(self) -> filedatainterfaces.KongsbergAllEnvironmentDataInterface_stream:
        ...
    @property
    def navigation_interface(self) -> filedatainterfaces.KongsbergAllNavigationDataInterface_stream:
        ...
    @property
    def otherfiledata_interface(self) -> filedatainterfaces.KongsbergAllOtherFileDataInterface_stream:
        ...
    @property
    def ping_interface(self) -> filedatainterfaces.KongsbergAllPingDataInterface_stream:
        ...
class t_KongsbergAllActiveSensor(enum.Enum):
    """
    This enum is used to identify the active sensor in the
    InstallationParameters datagram
    """
    AttitudeVelocitySensor1: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = t_KongsbergAllActiveSensor.AttitudeVelocitySensor1
    AttitudeVelocitySensor2: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = t_KongsbergAllActiveSensor.AttitudeVelocitySensor2
    MotionSensor1: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = t_KongsbergAllActiveSensor.MotionSensor1
    MotionSensor2: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = t_KongsbergAllActiveSensor.MotionSensor2
    MultiCast1: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = t_KongsbergAllActiveSensor.MultiCast1
    MultiCast2: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = t_KongsbergAllActiveSensor.MultiCast2
    MultiCast3: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = t_KongsbergAllActiveSensor.MultiCast3
    NotSet: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = t_KongsbergAllActiveSensor.NotSet
    PositionSystem1: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = t_KongsbergAllActiveSensor.PositionSystem1
    PositionSystem2: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = t_KongsbergAllActiveSensor.PositionSystem2
    PositionSystem3: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = t_KongsbergAllActiveSensor.PositionSystem3
class t_KongsbergAllDatagramIdentifier(enum.Enum):
    """
    """
    AttitudeDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.AttitudeDatagram
    ClockDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.ClockDatagram
    DepthOrHeightDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.DepthOrHeightDatagram
    ExtraDetections: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.ExtraDetections
    ExtraParameters: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.ExtraParameters
    HeadingDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.HeadingDatagram
    InstallationParametersStart: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.InstallationParametersStart
    InstallationParametersStop: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.InstallationParametersStop
    NetworkAttitudeVelocityDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.NetworkAttitudeVelocityDatagram
    PUIDOutput: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.PUIDOutput
    PUStatusOutput: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.PUStatusOutput
    PositionDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.PositionDatagram
    QualityFactorDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.QualityFactorDatagram
    RawRangeAndAngle: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.RawRangeAndAngle
    RuntimeParameters: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.RuntimeParameters
    SeabedImageData: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.SeabedImageData
    SingleBeamEchoSounderDepth: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.SingleBeamEchoSounderDepth
    SoundSpeedProfileDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.SoundSpeedProfileDatagram
    SurfaceSoundSpeedDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.SurfaceSoundSpeedDatagram
    WatercolumnDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.WatercolumnDatagram
    XYZDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.XYZDatagram
    unspecified: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.unspecified
class t_KongsbergAllSystemTransducerConfiguration(enum.Enum):
    """
    This enum is used to identify the transducer configuration (STC field)
    in the InstallationParameters datagram
    """
    DualHead: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = t_KongsbergAllSystemTransducerConfiguration.DualHead
    DualTXDualRX: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = t_KongsbergAllSystemTransducerConfiguration.DualTXDualRX
    Modular: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = t_KongsbergAllSystemTransducerConfiguration.Modular
    PortableSingleHead: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = t_KongsbergAllSystemTransducerConfiguration.PortableSingleHead
    SingleHead: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = t_KongsbergAllSystemTransducerConfiguration.SingleHead
    SingleTXDualRX: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = t_KongsbergAllSystemTransducerConfiguration.SingleTXDualRX
    SingleTXSingleRX: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = t_KongsbergAllSystemTransducerConfiguration.SingleTXSingleRX
KongsbergAllDatagram_type_from_string: nanobind.nb_func  # value = <nanobind.nb_func object>
datagram_type_to_string: nanobind.nb_func  # value = <nanobind.nb_func object>
