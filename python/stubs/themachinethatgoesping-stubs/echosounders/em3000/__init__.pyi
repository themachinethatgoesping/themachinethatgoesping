"""Classes related to Kongsberg EM3000 data files (old Kongsberg .all / .wcd format, used until SIS 4.0)"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000
import typing
import themachinethatgoesping.tools.progressbars

__all__ = [
    "AttitudeDatagram",
    "ClockDatagram",
    "CombinedWaterColumnDatagram",
    "DepthOrHeightDatagram",
    "EM3000Datagram_type_from_string",
    "ExtraDetections",
    "ExtraParameters",
    "FileEM3000",
    "FileEM3000_mapped",
    "HeadingDatagram",
    "InstallationParameterStart",
    "InstallationParameterStop",
    "NetworkAttitudeVelocityDatagram",
    "PUIDOutput",
    "PositionDatagram",
    "PuStatusOutput",
    "QualityFactorDatagram",
    "RawRangeAndAngle",
    "RuntimeParameters",
    "SeabedImageData",
    "SingleBeamEchoSounderDepth",
    "SoundSpeedProfileDatagram",
    "SurfaceSoundSpeedDatagram",
    "WaterColumnDatagram",
    "XYZDatagram",
    "datagram_type_to_string",
    "datagrams",
    "filedataInterfaces",
    "filedatacontainers",
    "t_EM3000DatagramIdentifier",
    "unspecified"
]


class FileEM3000():
    @typing.overload
    def __init__(self, file_path: str, init: bool = True, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_path: str, init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def __init__(self, file_path: typing.List[str], init: bool = True, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_paths: typing.List[str], init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def datagram_interface(self) -> filedataInterfaces.EM3000DatagramInterface:
        """
        :type: filedataInterfaces.EM3000DatagramInterface
        """
    pass
class FileEM3000_mapped():
    @typing.overload
    def __init__(self, file_path: str, init: bool = True, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_path: str, init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def __init__(self, file_path: typing.List[str], init: bool = True, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_paths: typing.List[str], init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def datagram_interface(self) -> filedataInterfaces.EM3000DatagramInterface_mapped:
        """
        :type: filedataInterfaces.EM3000DatagramInterface_mapped
        """
    pass
class t_EM3000DatagramIdentifier():
    """
    Members:

      XYZDatagram : 

      ExtraDetections : 

      RawRangeAndAngle : 

      SeabedImageData : 

      WaterColumnDatagram : 

      CombinedWaterColumnDatagram : 

      QualityFactorDatagram : < TODO: implement!

      AttitudeDatagram : 

      NetworkAttitudeVelocityDatagram : < TODO: implement!

      ClockDatagram : 

      DepthOrHeightDatagram : 

      HeadingDatagram : < TODO: implement!

      PositionDatagram : 

      SingleBeamEchoSounderDepth : < TODO: implement!

      SurfaceSoundSpeedDatagram : 

      SoundSpeedProfileDatagram : 

      InstallationParameterStart : 

      InstallationParameterStop : 

      RuntimeParameters : 

      ExtraParameters : 

      PuStatusOutput : 

      PUIDOutput : 

      unspecified : 
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    @typing.overload
    def __init__(self, str: str) -> None: 
        """
        Construct this enum type from string
        """
    @typing.overload
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    def str(self) -> str: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    AttitudeDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.AttitudeDatagram: 65>
    ClockDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.ClockDatagram: 67>
    CombinedWaterColumnDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.CombinedWaterColumnDatagram: 106>
    DepthOrHeightDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.DepthOrHeightDatagram: 104>
    ExtraDetections: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.ExtraDetections: 108>
    ExtraParameters: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.ExtraParameters: 51>
    HeadingDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.HeadingDatagram: 72>
    InstallationParameterStart: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.InstallationParameterStart: 73>
    InstallationParameterStop: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.InstallationParameterStop: 105>
    NetworkAttitudeVelocityDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.NetworkAttitudeVelocityDatagram: 110>
    PUIDOutput: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.PUIDOutput: 48>
    PositionDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.PositionDatagram: 80>
    PuStatusOutput: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.PuStatusOutput: 49>
    QualityFactorDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.QualityFactorDatagram: 79>
    RawRangeAndAngle: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.RawRangeAndAngle: 78>
    RuntimeParameters: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.RuntimeParameters: 82>
    SeabedImageData: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.SeabedImageData: 89>
    SingleBeamEchoSounderDepth: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.SingleBeamEchoSounderDepth: 69>
    SoundSpeedProfileDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.SoundSpeedProfileDatagram: 85>
    SurfaceSoundSpeedDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.SurfaceSoundSpeedDatagram: 71>
    WaterColumnDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.WaterColumnDatagram: 107>
    XYZDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.XYZDatagram: 88>
    __members__: dict # value = {'XYZDatagram': <t_EM3000DatagramIdentifier.XYZDatagram: 88>, 'ExtraDetections': <t_EM3000DatagramIdentifier.ExtraDetections: 108>, 'RawRangeAndAngle': <t_EM3000DatagramIdentifier.RawRangeAndAngle: 78>, 'SeabedImageData': <t_EM3000DatagramIdentifier.SeabedImageData: 89>, 'WaterColumnDatagram': <t_EM3000DatagramIdentifier.WaterColumnDatagram: 107>, 'CombinedWaterColumnDatagram': <t_EM3000DatagramIdentifier.CombinedWaterColumnDatagram: 106>, 'QualityFactorDatagram': <t_EM3000DatagramIdentifier.QualityFactorDatagram: 79>, 'AttitudeDatagram': <t_EM3000DatagramIdentifier.AttitudeDatagram: 65>, 'NetworkAttitudeVelocityDatagram': <t_EM3000DatagramIdentifier.NetworkAttitudeVelocityDatagram: 110>, 'ClockDatagram': <t_EM3000DatagramIdentifier.ClockDatagram: 67>, 'DepthOrHeightDatagram': <t_EM3000DatagramIdentifier.DepthOrHeightDatagram: 104>, 'HeadingDatagram': <t_EM3000DatagramIdentifier.HeadingDatagram: 72>, 'PositionDatagram': <t_EM3000DatagramIdentifier.PositionDatagram: 80>, 'SingleBeamEchoSounderDepth': <t_EM3000DatagramIdentifier.SingleBeamEchoSounderDepth: 69>, 'SurfaceSoundSpeedDatagram': <t_EM3000DatagramIdentifier.SurfaceSoundSpeedDatagram: 71>, 'SoundSpeedProfileDatagram': <t_EM3000DatagramIdentifier.SoundSpeedProfileDatagram: 85>, 'InstallationParameterStart': <t_EM3000DatagramIdentifier.InstallationParameterStart: 73>, 'InstallationParameterStop': <t_EM3000DatagramIdentifier.InstallationParameterStop: 105>, 'RuntimeParameters': <t_EM3000DatagramIdentifier.RuntimeParameters: 82>, 'ExtraParameters': <t_EM3000DatagramIdentifier.ExtraParameters: 51>, 'PuStatusOutput': <t_EM3000DatagramIdentifier.PuStatusOutput: 49>, 'PUIDOutput': <t_EM3000DatagramIdentifier.PUIDOutput: 48>, 'unspecified': <t_EM3000DatagramIdentifier.unspecified: 0>}
    unspecified: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.unspecified: 0>
    pass
def EM3000Datagram_type_from_string(datagram_type: str) -> t_EM3000DatagramIdentifier:
    pass
def datagram_type_to_string(datagram_type: t_EM3000DatagramIdentifier) -> str:
    pass
AttitudeDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.AttitudeDatagram: 65>
ClockDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.ClockDatagram: 67>
CombinedWaterColumnDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.CombinedWaterColumnDatagram: 106>
DepthOrHeightDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.DepthOrHeightDatagram: 104>
ExtraDetections: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.ExtraDetections: 108>
ExtraParameters: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.ExtraParameters: 51>
HeadingDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.HeadingDatagram: 72>
InstallationParameterStart: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.InstallationParameterStart: 73>
InstallationParameterStop: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.InstallationParameterStop: 105>
NetworkAttitudeVelocityDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.NetworkAttitudeVelocityDatagram: 110>
PUIDOutput: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.PUIDOutput: 48>
PositionDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.PositionDatagram: 80>
PuStatusOutput: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.PuStatusOutput: 49>
QualityFactorDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.QualityFactorDatagram: 79>
RawRangeAndAngle: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.RawRangeAndAngle: 78>
RuntimeParameters: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.RuntimeParameters: 82>
SeabedImageData: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.SeabedImageData: 89>
SingleBeamEchoSounderDepth: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.SingleBeamEchoSounderDepth: 69>
SoundSpeedProfileDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.SoundSpeedProfileDatagram: 85>
SurfaceSoundSpeedDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.SurfaceSoundSpeedDatagram: 71>
WaterColumnDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.WaterColumnDatagram: 107>
XYZDatagram: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.XYZDatagram: 88>
unspecified: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier # value = <t_EM3000DatagramIdentifier.unspecified: 0>
