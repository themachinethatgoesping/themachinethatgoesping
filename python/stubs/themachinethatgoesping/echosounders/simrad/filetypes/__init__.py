"""Simrad EK60 and EK80 file data types"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad.filetypes
import typing
import numpy
import themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes
import themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams
import themachinethatgoesping.navigation.datastructures
_Shape = typing.Tuple[int, ...]

__all__ = [
    "SimradPing",
    "SimradPing_RawData",
    "SimradPing_mapped",
    "SimradPing_mapped_RawData"
]


class SimradPing():
    def get_angle(self) -> numpy.ndarray[numpy.float32]: ...
    def get_geolocation(self) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: ...
    def get_number_of_samples(self) -> int: ...
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_timestamp(self) -> float: ...
    def set_channel_id(self, channel_id: str) -> None: ...
    def set_geolocation(self, geolocation_latlon: themachinethatgoesping.navigation.datastructures.GeoLocationLatLon) -> None: ...
    def set_timestamp(self, timestamp: float) -> None: ...
    @property
    def get_channel_id(self) -> str:
        """
        :type: str
        """
    @property
    def raw(self) -> SimradPing_RawData:
        """
        :type: SimradPing_RawData
        """
    pass
class SimradPing_RawData():
    def get_parameter(self) -> themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Parameter_Channel: ...
    def get_sample_data(self) -> typing.Union[themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.RAW3_DataSkipped, themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.RAW3_DataComplexFloat32, themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.RAW3_DataPowerAndAngle, themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.RAW3_DataPower, themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.RAW3_DataAngle]: ...
    def load_data(self) -> None: ...
    def release_data(self) -> None: ...
    @property
    def ping_data(self) -> themachinethatgoesping.echosounders.simrad.datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)

        :type: themachinethatgoesping.echosounders.simrad.datagrams.RAW3
        """
    pass
class SimradPing_mapped():
    def get_angle(self) -> numpy.ndarray[numpy.float32]: ...
    def get_geolocation(self) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: ...
    def get_number_of_samples(self) -> int: ...
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_timestamp(self) -> float: ...
    def set_channel_id(self, channel_id: str) -> None: ...
    def set_geolocation(self, geolocation_latlon: themachinethatgoesping.navigation.datastructures.GeoLocationLatLon) -> None: ...
    def set_timestamp(self, timestamp: float) -> None: ...
    @property
    def get_channel_id(self) -> str:
        """
        :type: str
        """
    @property
    def raw(self) -> SimradPing_mapped_RawData:
        """
        :type: SimradPing_mapped_RawData
        """
    pass
class SimradPing_mapped_RawData():
    def get_parameter(self) -> themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Parameter_Channel: ...
    def get_sample_data(self) -> typing.Union[themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.RAW3_DataSkipped, themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.RAW3_DataComplexFloat32, themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.RAW3_DataPowerAndAngle, themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.RAW3_DataPower, themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.RAW3_DataAngle]: ...
    def load_data(self) -> None: ...
    def release_data(self) -> None: ...
    @property
    def ping_data(self) -> themachinethatgoesping.echosounders.simrad.datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)

        :type: themachinethatgoesping.echosounders.simrad.datagrams.RAW3
        """
    pass
