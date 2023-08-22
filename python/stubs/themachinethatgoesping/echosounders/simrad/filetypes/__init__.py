"""Simrad EK60 and EK80 file data types"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad.filetypes
import typing
import themachinethatgoesping.echosounders.filetemplates
import themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams
import themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes
import themachinethatgoesping.navigation.datastructures

__all__ = [
    "SimradPing",
    "SimradPingRawData",
    "SimradPingRawData_mapped",
    "SimradPing_mapped"
]


class SimradPing(themachinethatgoesping.echosounders.filetemplates.I_Ping):
    def __copy__(self) -> SimradPing: ...
    def __deepcopy__(self, arg0: dict) -> SimradPing: ...
    def copy(self) -> SimradPing: 
        """
        return a copy using the c++ default copy constructor
        """
    def raw_data(self) -> SimradPingRawData: ...
    def set_geolocation(self, geolocation_latlon: themachinethatgoesping.navigation.datastructures.GeoLocationLatLon) -> None: ...
    pass
class SimradPingRawData():
    def __copy__(self) -> SimradPingRawData: ...
    def __deepcopy__(self, arg0: dict) -> SimradPingRawData: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> SimradPingRawData: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_parameter(self) -> themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Parameter_Channel: ...
    def get_sample_data(self) -> typing.Union[themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataSkipped, themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataComplexFloat32, themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataPowerAndAngle, themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataPower, themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataAngle]: ...
    def has_angle(self) -> bool: ...
    def has_power(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def load_data(self) -> None: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def release_data(self) -> None: ...
    @property
    def ping_data(self) -> themachinethatgoesping.echosounders.simrad.datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)

        :type: themachinethatgoesping.echosounders.simrad.datagrams.RAW3
        """
    pass
class SimradPingRawData_mapped():
    def __copy__(self) -> SimradPingRawData_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradPingRawData_mapped: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> SimradPingRawData_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_parameter(self) -> themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams.XML_Parameter_Channel: ...
    def get_sample_data(self) -> typing.Union[themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataSkipped, themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataComplexFloat32, themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataPowerAndAngle, themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataPower, themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes.RAW3DataAngle]: ...
    def has_angle(self) -> bool: ...
    def has_power(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def load_data(self) -> None: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def release_data(self) -> None: ...
    @property
    def ping_data(self) -> themachinethatgoesping.echosounders.simrad.datagrams.RAW3:
        """
        < when implementing EK60, this must become a variant type (RAW3 or
        RAW0)

        :type: themachinethatgoesping.echosounders.simrad.datagrams.RAW3
        """
    pass
class SimradPing_mapped(themachinethatgoesping.echosounders.filetemplates.I_Ping):
    def __copy__(self) -> SimradPing_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradPing_mapped: ...
    def copy(self) -> SimradPing_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def raw_data(self) -> SimradPingRawData_mapped: ...
    def set_geolocation(self, geolocation_latlon: themachinethatgoesping.navigation.datastructures.GeoLocationLatLon) -> None: ...
    pass
