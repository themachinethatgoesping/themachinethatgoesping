"""
Classes related to Kongsberg KongsbergAll data files (old Kongsberg .all / .wcd format, used until SIS 4.0)
"""
from __future__ import annotations
import collections.abc
import themachinethatgoesping.tools_cppy.progressbars
import typing
from . import datagrams
from . import filedatacontainers
from . import filedatainterfaces
from . import filetypes
__all__: list[str] = ['AttitudeDatagram', 'AttitudeVelocitySensor1', 'AttitudeVelocitySensor2', 'ClockDatagram', 'DepthOrHeightDatagram', 'DualHead', 'DualTXDualRX', 'ExtraDetections', 'ExtraParameters', 'HeadingDatagram', 'InstallationParametersStart', 'InstallationParametersStop', 'KongsbergAllDatagram_type_from_string', 'KongsbergAllFileHandler', 'KongsbergAllFileHandler_stream', 'Modular', 'MotionSensor1', 'MotionSensor2', 'MultiCast1', 'MultiCast2', 'MultiCast3', 'NetworkAttitudeVelocityDatagram', 'NotSet', 'PUIDOutput', 'PUStatusOutput', 'PortableSingleHead', 'PositionDatagram', 'PositionSystem1', 'PositionSystem2', 'PositionSystem3', 'QualityFactorDatagram', 'RawRangeAndAngle', 'RuntimeParameters', 'SeabedImageData', 'SingleBeamEchoSounderDepth', 'SingleHead', 'SingleTXDualRX', 'SingleTXSingleRX', 'SoundSpeedProfileDatagram', 'SurfaceSoundSpeedDatagram', 'WatercolumnDatagram', 'XYZDatagram', 'datagram_type_to_string', 'datagrams', 'filedatacontainers', 'filedatainterfaces', 'filetypes', 't_KongsbergAllActiveSensor', 't_KongsbergAllDatagramIdentifier', 't_KongsbergAllSystemTransducerConfiguration', 'unspecified']
class KongsbergAllFileHandler:
    """
    """
    @typing.overload
    def __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_paths: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
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
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
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
    @typing.overload
    def __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: str, index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str] = {}, init: bool = True, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, file_paths: collections.abc.Sequence[str], index_paths: collections.abc.Mapping[str, str], init: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
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
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None:
        ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools_cppy.progressbars.I_ProgressBar) -> None:
        ...
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
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
class t_KongsbergAllActiveSensor:
    """
    This enum is used to identify the active sensor in the
    InstallationParameters datagram
    
    Members:
    
      PositionSystem3 : < UDP2 or COM4
    
      PositionSystem1 : < COM1
    
      PositionSystem2 : 
    
      MotionSensor1 : < COM2
    
      MotionSensor2 : < COM3
    
      MultiCast1 : <
    
      MultiCast2 : <
    
      MultiCast3 : <
    
      AttitudeVelocitySensor1 : < UDP5
    
      AttitudeVelocitySensor2 : < UDP6
    
      NotSet : < this is not a valid value
    """
    AttitudeVelocitySensor1: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = <t_KongsbergAllActiveSensor.AttitudeVelocitySensor1: 8>
    AttitudeVelocitySensor2: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = <t_KongsbergAllActiveSensor.AttitudeVelocitySensor2: 9>
    MotionSensor1: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = <t_KongsbergAllActiveSensor.MotionSensor1: 2>
    MotionSensor2: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = <t_KongsbergAllActiveSensor.MotionSensor2: 3>
    MultiCast1: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = <t_KongsbergAllActiveSensor.MultiCast1: 5>
    MultiCast2: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = <t_KongsbergAllActiveSensor.MultiCast2: 6>
    MultiCast3: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = <t_KongsbergAllActiveSensor.MultiCast3: 7>
    NotSet: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = <t_KongsbergAllActiveSensor.NotSet: -1>
    PositionSystem1: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = <t_KongsbergAllActiveSensor.PositionSystem1: 1>
    PositionSystem2: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = <t_KongsbergAllActiveSensor.PositionSystem2: 32>
    PositionSystem3: typing.ClassVar[t_KongsbergAllActiveSensor]  # value = <t_KongsbergAllActiveSensor.PositionSystem3: 0>
    __members__: typing.ClassVar[dict[str, t_KongsbergAllActiveSensor]]  # value = {'PositionSystem3': <t_KongsbergAllActiveSensor.PositionSystem3: 0>, 'PositionSystem1': <t_KongsbergAllActiveSensor.PositionSystem1: 1>, 'PositionSystem2': <t_KongsbergAllActiveSensor.PositionSystem2: 32>, 'MotionSensor1': <t_KongsbergAllActiveSensor.MotionSensor1: 2>, 'MotionSensor2': <t_KongsbergAllActiveSensor.MotionSensor2: 3>, 'MultiCast1': <t_KongsbergAllActiveSensor.MultiCast1: 5>, 'MultiCast2': <t_KongsbergAllActiveSensor.MultiCast2: 6>, 'MultiCast3': <t_KongsbergAllActiveSensor.MultiCast3: 7>, 'AttitudeVelocitySensor1': <t_KongsbergAllActiveSensor.AttitudeVelocitySensor1: 8>, 'AttitudeVelocitySensor2': <t_KongsbergAllActiveSensor.AttitudeVelocitySensor2: 9>, 'NotSet': <t_KongsbergAllActiveSensor.NotSet: -1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    @typing.overload
    def __init__(self, value: typing.SupportsInt) -> None:
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
    def __setstate__(self, state: typing.SupportsInt) -> None:
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
class t_KongsbergAllDatagramIdentifier:
    """
    
    
    Members:
    
      XYZDatagram : 
    
      ExtraDetections : 
    
      RawRangeAndAngle : 
    
      SeabedImageData : 
    
      WatercolumnDatagram : 
    
      QualityFactorDatagram : 
    
      AttitudeDatagram : 
    
      NetworkAttitudeVelocityDatagram : 
    
      ClockDatagram : 
    
      DepthOrHeightDatagram : 
    
      HeadingDatagram : 
    
      PositionDatagram : 
    
      SingleBeamEchoSounderDepth : 
    
      SurfaceSoundSpeedDatagram : 
    
      SoundSpeedProfileDatagram : 
    
      InstallationParametersStart : 
    
      InstallationParametersStop : 
    
      RuntimeParameters : 
    
      ExtraParameters : 
    
      PUStatusOutput : 
    
      PUIDOutput : 
    
      unspecified : 
    """
    AttitudeDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.AttitudeDatagram: 65>
    ClockDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.ClockDatagram: 67>
    DepthOrHeightDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.DepthOrHeightDatagram: 104>
    ExtraDetections: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.ExtraDetections: 108>
    ExtraParameters: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.ExtraParameters: 51>
    HeadingDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.HeadingDatagram: 72>
    InstallationParametersStart: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.InstallationParametersStart: 73>
    InstallationParametersStop: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.InstallationParametersStop: 105>
    NetworkAttitudeVelocityDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.NetworkAttitudeVelocityDatagram: 110>
    PUIDOutput: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.PUIDOutput: 48>
    PUStatusOutput: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.PUStatusOutput: 49>
    PositionDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.PositionDatagram: 80>
    QualityFactorDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.QualityFactorDatagram: 79>
    RawRangeAndAngle: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.RawRangeAndAngle: 78>
    RuntimeParameters: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.RuntimeParameters: 82>
    SeabedImageData: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.SeabedImageData: 89>
    SingleBeamEchoSounderDepth: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.SingleBeamEchoSounderDepth: 69>
    SoundSpeedProfileDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.SoundSpeedProfileDatagram: 85>
    SurfaceSoundSpeedDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.SurfaceSoundSpeedDatagram: 71>
    WatercolumnDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.WatercolumnDatagram: 107>
    XYZDatagram: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.XYZDatagram: 88>
    __members__: typing.ClassVar[dict[str, t_KongsbergAllDatagramIdentifier]]  # value = {'XYZDatagram': <t_KongsbergAllDatagramIdentifier.XYZDatagram: 88>, 'ExtraDetections': <t_KongsbergAllDatagramIdentifier.ExtraDetections: 108>, 'RawRangeAndAngle': <t_KongsbergAllDatagramIdentifier.RawRangeAndAngle: 78>, 'SeabedImageData': <t_KongsbergAllDatagramIdentifier.SeabedImageData: 89>, 'WatercolumnDatagram': <t_KongsbergAllDatagramIdentifier.WatercolumnDatagram: 107>, 'QualityFactorDatagram': <t_KongsbergAllDatagramIdentifier.QualityFactorDatagram: 79>, 'AttitudeDatagram': <t_KongsbergAllDatagramIdentifier.AttitudeDatagram: 65>, 'NetworkAttitudeVelocityDatagram': <t_KongsbergAllDatagramIdentifier.NetworkAttitudeVelocityDatagram: 110>, 'ClockDatagram': <t_KongsbergAllDatagramIdentifier.ClockDatagram: 67>, 'DepthOrHeightDatagram': <t_KongsbergAllDatagramIdentifier.DepthOrHeightDatagram: 104>, 'HeadingDatagram': <t_KongsbergAllDatagramIdentifier.HeadingDatagram: 72>, 'PositionDatagram': <t_KongsbergAllDatagramIdentifier.PositionDatagram: 80>, 'SingleBeamEchoSounderDepth': <t_KongsbergAllDatagramIdentifier.SingleBeamEchoSounderDepth: 69>, 'SurfaceSoundSpeedDatagram': <t_KongsbergAllDatagramIdentifier.SurfaceSoundSpeedDatagram: 71>, 'SoundSpeedProfileDatagram': <t_KongsbergAllDatagramIdentifier.SoundSpeedProfileDatagram: 85>, 'InstallationParametersStart': <t_KongsbergAllDatagramIdentifier.InstallationParametersStart: 73>, 'InstallationParametersStop': <t_KongsbergAllDatagramIdentifier.InstallationParametersStop: 105>, 'RuntimeParameters': <t_KongsbergAllDatagramIdentifier.RuntimeParameters: 82>, 'ExtraParameters': <t_KongsbergAllDatagramIdentifier.ExtraParameters: 51>, 'PUStatusOutput': <t_KongsbergAllDatagramIdentifier.PUStatusOutput: 49>, 'PUIDOutput': <t_KongsbergAllDatagramIdentifier.PUIDOutput: 48>, 'unspecified': <t_KongsbergAllDatagramIdentifier.unspecified: 0>}
    unspecified: typing.ClassVar[t_KongsbergAllDatagramIdentifier]  # value = <t_KongsbergAllDatagramIdentifier.unspecified: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    @typing.overload
    def __init__(self, value: typing.SupportsInt) -> None:
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
    def __setstate__(self, state: typing.SupportsInt) -> None:
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
class t_KongsbergAllSystemTransducerConfiguration:
    """
    This enum is used to identify the transducer configuration (STC field)
    in the InstallationParameters datagram
    
    Members:
    
      SingleTXSingleRX : < EM122, EM302, EM710, EM2040 Single
    
      SingleHead : < EM3002 Single Head, EM2040C Single Head
    
      DualHead : < EM3002 Dual Head, EM2040C Dual Head
    
      SingleTXDualRX : < EM2040 Dual RX
    
      DualTXDualRX : < EM2040 Dual TX
    
      PortableSingleHead : < EM2040P
    
      Modular : < EM2040M
    """
    DualHead: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = <t_KongsbergAllSystemTransducerConfiguration.DualHead: 2>
    DualTXDualRX: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = <t_KongsbergAllSystemTransducerConfiguration.DualTXDualRX: 4>
    Modular: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = <t_KongsbergAllSystemTransducerConfiguration.Modular: 6>
    PortableSingleHead: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = <t_KongsbergAllSystemTransducerConfiguration.PortableSingleHead: 5>
    SingleHead: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = <t_KongsbergAllSystemTransducerConfiguration.SingleHead: 1>
    SingleTXDualRX: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = <t_KongsbergAllSystemTransducerConfiguration.SingleTXDualRX: 3>
    SingleTXSingleRX: typing.ClassVar[t_KongsbergAllSystemTransducerConfiguration]  # value = <t_KongsbergAllSystemTransducerConfiguration.SingleTXSingleRX: 0>
    __members__: typing.ClassVar[dict[str, t_KongsbergAllSystemTransducerConfiguration]]  # value = {'SingleTXSingleRX': <t_KongsbergAllSystemTransducerConfiguration.SingleTXSingleRX: 0>, 'SingleHead': <t_KongsbergAllSystemTransducerConfiguration.SingleHead: 1>, 'DualHead': <t_KongsbergAllSystemTransducerConfiguration.DualHead: 2>, 'SingleTXDualRX': <t_KongsbergAllSystemTransducerConfiguration.SingleTXDualRX: 3>, 'DualTXDualRX': <t_KongsbergAllSystemTransducerConfiguration.DualTXDualRX: 4>, 'PortableSingleHead': <t_KongsbergAllSystemTransducerConfiguration.PortableSingleHead: 5>, 'Modular': <t_KongsbergAllSystemTransducerConfiguration.Modular: 6>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    @typing.overload
    def __init__(self, value: typing.SupportsInt) -> None:
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
    def __setstate__(self, state: typing.SupportsInt) -> None:
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
def KongsbergAllDatagram_type_from_string(datagram_type: str) -> t_KongsbergAllDatagramIdentifier:
    ...
def datagram_type_to_string(datagram_type: t_KongsbergAllDatagramIdentifier) -> str:
    ...
AttitudeDatagram: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.AttitudeDatagram: 65>
AttitudeVelocitySensor1: t_KongsbergAllActiveSensor  # value = <t_KongsbergAllActiveSensor.AttitudeVelocitySensor1: 8>
AttitudeVelocitySensor2: t_KongsbergAllActiveSensor  # value = <t_KongsbergAllActiveSensor.AttitudeVelocitySensor2: 9>
ClockDatagram: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.ClockDatagram: 67>
DepthOrHeightDatagram: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.DepthOrHeightDatagram: 104>
DualHead: t_KongsbergAllSystemTransducerConfiguration  # value = <t_KongsbergAllSystemTransducerConfiguration.DualHead: 2>
DualTXDualRX: t_KongsbergAllSystemTransducerConfiguration  # value = <t_KongsbergAllSystemTransducerConfiguration.DualTXDualRX: 4>
ExtraDetections: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.ExtraDetections: 108>
ExtraParameters: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.ExtraParameters: 51>
HeadingDatagram: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.HeadingDatagram: 72>
InstallationParametersStart: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.InstallationParametersStart: 73>
InstallationParametersStop: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.InstallationParametersStop: 105>
Modular: t_KongsbergAllSystemTransducerConfiguration  # value = <t_KongsbergAllSystemTransducerConfiguration.Modular: 6>
MotionSensor1: t_KongsbergAllActiveSensor  # value = <t_KongsbergAllActiveSensor.MotionSensor1: 2>
MotionSensor2: t_KongsbergAllActiveSensor  # value = <t_KongsbergAllActiveSensor.MotionSensor2: 3>
MultiCast1: t_KongsbergAllActiveSensor  # value = <t_KongsbergAllActiveSensor.MultiCast1: 5>
MultiCast2: t_KongsbergAllActiveSensor  # value = <t_KongsbergAllActiveSensor.MultiCast2: 6>
MultiCast3: t_KongsbergAllActiveSensor  # value = <t_KongsbergAllActiveSensor.MultiCast3: 7>
NetworkAttitudeVelocityDatagram: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.NetworkAttitudeVelocityDatagram: 110>
NotSet: t_KongsbergAllActiveSensor  # value = <t_KongsbergAllActiveSensor.NotSet: -1>
PUIDOutput: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.PUIDOutput: 48>
PUStatusOutput: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.PUStatusOutput: 49>
PortableSingleHead: t_KongsbergAllSystemTransducerConfiguration  # value = <t_KongsbergAllSystemTransducerConfiguration.PortableSingleHead: 5>
PositionDatagram: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.PositionDatagram: 80>
PositionSystem1: t_KongsbergAllActiveSensor  # value = <t_KongsbergAllActiveSensor.PositionSystem1: 1>
PositionSystem2: t_KongsbergAllActiveSensor  # value = <t_KongsbergAllActiveSensor.PositionSystem2: 32>
PositionSystem3: t_KongsbergAllActiveSensor  # value = <t_KongsbergAllActiveSensor.PositionSystem3: 0>
QualityFactorDatagram: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.QualityFactorDatagram: 79>
RawRangeAndAngle: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.RawRangeAndAngle: 78>
RuntimeParameters: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.RuntimeParameters: 82>
SeabedImageData: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.SeabedImageData: 89>
SingleBeamEchoSounderDepth: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.SingleBeamEchoSounderDepth: 69>
SingleHead: t_KongsbergAllSystemTransducerConfiguration  # value = <t_KongsbergAllSystemTransducerConfiguration.SingleHead: 1>
SingleTXDualRX: t_KongsbergAllSystemTransducerConfiguration  # value = <t_KongsbergAllSystemTransducerConfiguration.SingleTXDualRX: 3>
SingleTXSingleRX: t_KongsbergAllSystemTransducerConfiguration  # value = <t_KongsbergAllSystemTransducerConfiguration.SingleTXSingleRX: 0>
SoundSpeedProfileDatagram: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.SoundSpeedProfileDatagram: 85>
SurfaceSoundSpeedDatagram: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.SurfaceSoundSpeedDatagram: 71>
WatercolumnDatagram: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.WatercolumnDatagram: 107>
XYZDatagram: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.XYZDatagram: 88>
unspecified: t_KongsbergAllDatagramIdentifier  # value = <t_KongsbergAllDatagramIdentifier.unspecified: 0>
