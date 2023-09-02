"""
Classes related to Kongsberg EM3000 data files (old Kongsberg .all / .wcd format, used until SIS 4.0)
"""
from __future__ import annotations
import themachinethatgoesping.tools.progressbars
import typing
from . import datagrams
from . import filedatacontainers
from . import filedatainterfaces
from . import filetypes
__all__ = ['AttitudeDatagram', 'AttitudeVelocitySensor1', 'AttitudeVelocitySensor2', 'ClockDatagram', 'DepthOrHeightDatagram', 'DualHead', 'DualTXDualRX', 'EM3000Datagram_type_from_string', 'ExtraDetections', 'ExtraParameters', 'FileEM3000', 'FileEM3000_mapped', 'HeadingDatagram', 'InstallationParametersStart', 'InstallationParametersStop', 'Modular', 'MotionSensor1', 'MotionSensor2', 'MultiCast1', 'MultiCast2', 'MultiCast3', 'NetworkAttitudeVelocityDatagram', 'NotSet', 'PUIDOutput', 'PUStatusOutput', 'PortableSingleHead', 'PositionDatagram', 'PositionSystem1', 'PositionSystem2', 'PositionSystem3', 'QualityFactorDatagram', 'RawRangeAndAngle', 'RuntimeParameters', 'SeabedImageData', 'SingleBeamEchoSounderDepth', 'SingleHead', 'SingleTXDualRX', 'SingleTXSingleRX', 'SoundSpeedProfileDatagram', 'SurfaceSoundSpeedDatagram', 'WatercolumnDatagram', 'XYZDatagram', 'datagram_type_to_string', 'datagrams', 'filedatacontainers', 'filedatainterfaces', 'filetypes', 't_EM3000ActiveSensor', 't_EM3000DatagramIdentifier', 't_EM3000SystemTransducerConfiguration', 'unspecified']
class FileEM3000:
    """
    """
    @typing.overload
    def __init__(self, file_path: str, init: bool = ..., show_progress: bool = ...) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: str, init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: list[str], init: bool = ..., show_progress: bool = ...) -> None:
        ...
    @typing.overload
    def __init__(self, file_paths: list[str], init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def channel_ids(self) -> list[str]:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = ..., show_progress: bool = ...) -> None:
        ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def pings(self) -> filedatacontainers.EM3000PingContainer:
        ...
    @typing.overload
    def pings(self, channel_id: str) -> filedatacontainers.EM3000PingContainer:
        ...
    @typing.overload
    def pings(self, channel_ids: list[str]) -> filedatacontainers.EM3000PingContainer:
        ...
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> filedatainterfaces.EM3000AnnotationDataInterface:
        ...
    @property
    def configuration_interface(self) -> filedatainterfaces.EM3000ConfigurationDataInterface:
        ...
    @property
    def datagram_interface(self) -> filedatainterfaces.EM3000DatagramInterface:
        ...
    @property
    def environment_interface(self) -> filedatainterfaces.EM3000EnvironmentDataInterface:
        ...
    @property
    def navigation_interface(self) -> filedatainterfaces.EM3000NavigationDataInterface:
        ...
    @property
    def otherfiledata_interface(self) -> filedatainterfaces.EM3000OtherFileDataInterface:
        ...
    @property
    def ping_interface(self) -> filedatainterfaces.EM3000PingDataInterface:
        ...
class FileEM3000_mapped:
    """
    """
    @typing.overload
    def __init__(self, file_path: str, init: bool = ..., show_progress: bool = ...) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: str, init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def __init__(self, file_path: list[str], init: bool = ..., show_progress: bool = ...) -> None:
        ...
    @typing.overload
    def __init__(self, file_paths: list[str], init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def channel_ids(self) -> list[str]:
        ...
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = ..., show_progress: bool = ...) -> None:
        ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None:
        ...
    @typing.overload
    def pings(self) -> filedatacontainers.EM3000PingContainer_mapped:
        ...
    @typing.overload
    def pings(self, channel_id: str) -> filedatacontainers.EM3000PingContainer_mapped:
        ...
    @typing.overload
    def pings(self, channel_ids: list[str]) -> filedatacontainers.EM3000PingContainer_mapped:
        ...
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    @property
    def annotation_interface(self) -> filedatainterfaces.EM3000AnnotationDataInterface_mapped:
        ...
    @property
    def configuration_interface(self) -> filedatainterfaces.EM3000ConfigurationDataInterface_mapped:
        ...
    @property
    def datagram_interface(self) -> filedatainterfaces.EM3000DatagramInterface_mapped:
        ...
    @property
    def environment_interface(self) -> filedatainterfaces.EM3000EnvironmentDataInterface_mapped:
        ...
    @property
    def navigation_interface(self) -> filedatainterfaces.EM3000NavigationDataInterface_mapped:
        ...
    @property
    def otherfiledata_interface(self) -> filedatainterfaces.EM3000OtherFileDataInterface_mapped:
        ...
    @property
    def ping_interface(self) -> filedatainterfaces.EM3000PingDataInterface_mapped:
        ...
class t_EM3000ActiveSensor:
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
    AttitudeVelocitySensor1: typing.ClassVar[t_EM3000ActiveSensor]  # value = <t_EM3000ActiveSensor.AttitudeVelocitySensor1: 8>
    AttitudeVelocitySensor2: typing.ClassVar[t_EM3000ActiveSensor]  # value = <t_EM3000ActiveSensor.AttitudeVelocitySensor2: 9>
    MotionSensor1: typing.ClassVar[t_EM3000ActiveSensor]  # value = <t_EM3000ActiveSensor.MotionSensor1: 2>
    MotionSensor2: typing.ClassVar[t_EM3000ActiveSensor]  # value = <t_EM3000ActiveSensor.MotionSensor2: 3>
    MultiCast1: typing.ClassVar[t_EM3000ActiveSensor]  # value = <t_EM3000ActiveSensor.MultiCast1: 5>
    MultiCast2: typing.ClassVar[t_EM3000ActiveSensor]  # value = <t_EM3000ActiveSensor.MultiCast2: 6>
    MultiCast3: typing.ClassVar[t_EM3000ActiveSensor]  # value = <t_EM3000ActiveSensor.MultiCast3: 7>
    NotSet: typing.ClassVar[t_EM3000ActiveSensor]  # value = <t_EM3000ActiveSensor.NotSet: -1>
    PositionSystem1: typing.ClassVar[t_EM3000ActiveSensor]  # value = <t_EM3000ActiveSensor.PositionSystem1: 1>
    PositionSystem2: typing.ClassVar[t_EM3000ActiveSensor]  # value = <t_EM3000ActiveSensor.PositionSystem2: 32>
    PositionSystem3: typing.ClassVar[t_EM3000ActiveSensor]  # value = <t_EM3000ActiveSensor.PositionSystem3: 0>
    __members__: typing.ClassVar[dict[str, t_EM3000ActiveSensor]]  # value = {'PositionSystem3': <t_EM3000ActiveSensor.PositionSystem3: 0>, 'PositionSystem1': <t_EM3000ActiveSensor.PositionSystem1: 1>, 'PositionSystem2': <t_EM3000ActiveSensor.PositionSystem2: 32>, 'MotionSensor1': <t_EM3000ActiveSensor.MotionSensor1: 2>, 'MotionSensor2': <t_EM3000ActiveSensor.MotionSensor2: 3>, 'MultiCast1': <t_EM3000ActiveSensor.MultiCast1: 5>, 'MultiCast2': <t_EM3000ActiveSensor.MultiCast2: 6>, 'MultiCast3': <t_EM3000ActiveSensor.MultiCast3: 7>, 'AttitudeVelocitySensor1': <t_EM3000ActiveSensor.AttitudeVelocitySensor1: 8>, 'AttitudeVelocitySensor2': <t_EM3000ActiveSensor.AttitudeVelocitySensor2: 9>, 'NotSet': <t_EM3000ActiveSensor.NotSet: -1>}
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
class t_EM3000DatagramIdentifier:
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
    AttitudeDatagram: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.AttitudeDatagram: 65>
    ClockDatagram: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.ClockDatagram: 67>
    DepthOrHeightDatagram: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.DepthOrHeightDatagram: 104>
    ExtraDetections: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.ExtraDetections: 108>
    ExtraParameters: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.ExtraParameters: 51>
    HeadingDatagram: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.HeadingDatagram: 72>
    InstallationParametersStart: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.InstallationParametersStart: 73>
    InstallationParametersStop: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.InstallationParametersStop: 105>
    NetworkAttitudeVelocityDatagram: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.NetworkAttitudeVelocityDatagram: 110>
    PUIDOutput: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.PUIDOutput: 48>
    PUStatusOutput: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.PUStatusOutput: 49>
    PositionDatagram: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.PositionDatagram: 80>
    QualityFactorDatagram: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.QualityFactorDatagram: 79>
    RawRangeAndAngle: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.RawRangeAndAngle: 78>
    RuntimeParameters: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.RuntimeParameters: 82>
    SeabedImageData: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.SeabedImageData: 89>
    SingleBeamEchoSounderDepth: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.SingleBeamEchoSounderDepth: 69>
    SoundSpeedProfileDatagram: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.SoundSpeedProfileDatagram: 85>
    SurfaceSoundSpeedDatagram: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.SurfaceSoundSpeedDatagram: 71>
    WatercolumnDatagram: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.WatercolumnDatagram: 107>
    XYZDatagram: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.XYZDatagram: 88>
    __members__: typing.ClassVar[dict[str, t_EM3000DatagramIdentifier]]  # value = {'XYZDatagram': <t_EM3000DatagramIdentifier.XYZDatagram: 88>, 'ExtraDetections': <t_EM3000DatagramIdentifier.ExtraDetections: 108>, 'RawRangeAndAngle': <t_EM3000DatagramIdentifier.RawRangeAndAngle: 78>, 'SeabedImageData': <t_EM3000DatagramIdentifier.SeabedImageData: 89>, 'WatercolumnDatagram': <t_EM3000DatagramIdentifier.WatercolumnDatagram: 107>, 'QualityFactorDatagram': <t_EM3000DatagramIdentifier.QualityFactorDatagram: 79>, 'AttitudeDatagram': <t_EM3000DatagramIdentifier.AttitudeDatagram: 65>, 'NetworkAttitudeVelocityDatagram': <t_EM3000DatagramIdentifier.NetworkAttitudeVelocityDatagram: 110>, 'ClockDatagram': <t_EM3000DatagramIdentifier.ClockDatagram: 67>, 'DepthOrHeightDatagram': <t_EM3000DatagramIdentifier.DepthOrHeightDatagram: 104>, 'HeadingDatagram': <t_EM3000DatagramIdentifier.HeadingDatagram: 72>, 'PositionDatagram': <t_EM3000DatagramIdentifier.PositionDatagram: 80>, 'SingleBeamEchoSounderDepth': <t_EM3000DatagramIdentifier.SingleBeamEchoSounderDepth: 69>, 'SurfaceSoundSpeedDatagram': <t_EM3000DatagramIdentifier.SurfaceSoundSpeedDatagram: 71>, 'SoundSpeedProfileDatagram': <t_EM3000DatagramIdentifier.SoundSpeedProfileDatagram: 85>, 'InstallationParametersStart': <t_EM3000DatagramIdentifier.InstallationParametersStart: 73>, 'InstallationParametersStop': <t_EM3000DatagramIdentifier.InstallationParametersStop: 105>, 'RuntimeParameters': <t_EM3000DatagramIdentifier.RuntimeParameters: 82>, 'ExtraParameters': <t_EM3000DatagramIdentifier.ExtraParameters: 51>, 'PUStatusOutput': <t_EM3000DatagramIdentifier.PUStatusOutput: 49>, 'PUIDOutput': <t_EM3000DatagramIdentifier.PUIDOutput: 48>, 'unspecified': <t_EM3000DatagramIdentifier.unspecified: 0>}
    unspecified: typing.ClassVar[t_EM3000DatagramIdentifier]  # value = <t_EM3000DatagramIdentifier.unspecified: 0>
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
class t_EM3000SystemTransducerConfiguration:
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
    DualHead: typing.ClassVar[t_EM3000SystemTransducerConfiguration]  # value = <t_EM3000SystemTransducerConfiguration.DualHead: 2>
    DualTXDualRX: typing.ClassVar[t_EM3000SystemTransducerConfiguration]  # value = <t_EM3000SystemTransducerConfiguration.DualTXDualRX: 4>
    Modular: typing.ClassVar[t_EM3000SystemTransducerConfiguration]  # value = <t_EM3000SystemTransducerConfiguration.Modular: 6>
    PortableSingleHead: typing.ClassVar[t_EM3000SystemTransducerConfiguration]  # value = <t_EM3000SystemTransducerConfiguration.PortableSingleHead: 5>
    SingleHead: typing.ClassVar[t_EM3000SystemTransducerConfiguration]  # value = <t_EM3000SystemTransducerConfiguration.SingleHead: 1>
    SingleTXDualRX: typing.ClassVar[t_EM3000SystemTransducerConfiguration]  # value = <t_EM3000SystemTransducerConfiguration.SingleTXDualRX: 3>
    SingleTXSingleRX: typing.ClassVar[t_EM3000SystemTransducerConfiguration]  # value = <t_EM3000SystemTransducerConfiguration.SingleTXSingleRX: 0>
    __members__: typing.ClassVar[dict[str, t_EM3000SystemTransducerConfiguration]]  # value = {'SingleTXSingleRX': <t_EM3000SystemTransducerConfiguration.SingleTXSingleRX: 0>, 'SingleHead': <t_EM3000SystemTransducerConfiguration.SingleHead: 1>, 'DualHead': <t_EM3000SystemTransducerConfiguration.DualHead: 2>, 'SingleTXDualRX': <t_EM3000SystemTransducerConfiguration.SingleTXDualRX: 3>, 'DualTXDualRX': <t_EM3000SystemTransducerConfiguration.DualTXDualRX: 4>, 'PortableSingleHead': <t_EM3000SystemTransducerConfiguration.PortableSingleHead: 5>, 'Modular': <t_EM3000SystemTransducerConfiguration.Modular: 6>}
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
def EM3000Datagram_type_from_string(datagram_type: str) -> t_EM3000DatagramIdentifier:
    ...
def datagram_type_to_string(datagram_type: t_EM3000DatagramIdentifier) -> str:
    ...
AttitudeDatagram: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.AttitudeDatagram: 65>
AttitudeVelocitySensor1: t_EM3000ActiveSensor  # value = <t_EM3000ActiveSensor.AttitudeVelocitySensor1: 8>
AttitudeVelocitySensor2: t_EM3000ActiveSensor  # value = <t_EM3000ActiveSensor.AttitudeVelocitySensor2: 9>
ClockDatagram: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.ClockDatagram: 67>
DepthOrHeightDatagram: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.DepthOrHeightDatagram: 104>
DualHead: t_EM3000SystemTransducerConfiguration  # value = <t_EM3000SystemTransducerConfiguration.DualHead: 2>
DualTXDualRX: t_EM3000SystemTransducerConfiguration  # value = <t_EM3000SystemTransducerConfiguration.DualTXDualRX: 4>
ExtraDetections: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.ExtraDetections: 108>
ExtraParameters: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.ExtraParameters: 51>
HeadingDatagram: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.HeadingDatagram: 72>
InstallationParametersStart: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.InstallationParametersStart: 73>
InstallationParametersStop: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.InstallationParametersStop: 105>
Modular: t_EM3000SystemTransducerConfiguration  # value = <t_EM3000SystemTransducerConfiguration.Modular: 6>
MotionSensor1: t_EM3000ActiveSensor  # value = <t_EM3000ActiveSensor.MotionSensor1: 2>
MotionSensor2: t_EM3000ActiveSensor  # value = <t_EM3000ActiveSensor.MotionSensor2: 3>
MultiCast1: t_EM3000ActiveSensor  # value = <t_EM3000ActiveSensor.MultiCast1: 5>
MultiCast2: t_EM3000ActiveSensor  # value = <t_EM3000ActiveSensor.MultiCast2: 6>
MultiCast3: t_EM3000ActiveSensor  # value = <t_EM3000ActiveSensor.MultiCast3: 7>
NetworkAttitudeVelocityDatagram: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.NetworkAttitudeVelocityDatagram: 110>
NotSet: t_EM3000ActiveSensor  # value = <t_EM3000ActiveSensor.NotSet: -1>
PUIDOutput: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.PUIDOutput: 48>
PUStatusOutput: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.PUStatusOutput: 49>
PortableSingleHead: t_EM3000SystemTransducerConfiguration  # value = <t_EM3000SystemTransducerConfiguration.PortableSingleHead: 5>
PositionDatagram: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.PositionDatagram: 80>
PositionSystem1: t_EM3000ActiveSensor  # value = <t_EM3000ActiveSensor.PositionSystem1: 1>
PositionSystem2: t_EM3000ActiveSensor  # value = <t_EM3000ActiveSensor.PositionSystem2: 32>
PositionSystem3: t_EM3000ActiveSensor  # value = <t_EM3000ActiveSensor.PositionSystem3: 0>
QualityFactorDatagram: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.QualityFactorDatagram: 79>
RawRangeAndAngle: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.RawRangeAndAngle: 78>
RuntimeParameters: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.RuntimeParameters: 82>
SeabedImageData: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.SeabedImageData: 89>
SingleBeamEchoSounderDepth: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.SingleBeamEchoSounderDepth: 69>
SingleHead: t_EM3000SystemTransducerConfiguration  # value = <t_EM3000SystemTransducerConfiguration.SingleHead: 1>
SingleTXDualRX: t_EM3000SystemTransducerConfiguration  # value = <t_EM3000SystemTransducerConfiguration.SingleTXDualRX: 3>
SingleTXSingleRX: t_EM3000SystemTransducerConfiguration  # value = <t_EM3000SystemTransducerConfiguration.SingleTXSingleRX: 0>
SoundSpeedProfileDatagram: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.SoundSpeedProfileDatagram: 85>
SurfaceSoundSpeedDatagram: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.SurfaceSoundSpeedDatagram: 71>
WatercolumnDatagram: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.WatercolumnDatagram: 107>
XYZDatagram: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.XYZDatagram: 88>
unspecified: t_EM3000DatagramIdentifier  # value = <t_EM3000DatagramIdentifier.unspecified: 0>
