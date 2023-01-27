"""Simrad EK60 and EK80 file data types"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad.filetypes
import typing
import numpy
import themachinethatgoesping.echosounders.simrad.datagrams.XML0_datagrams
import themachinethatgoesping.echosounders.simrad.datagrams.raw3datatypes
import themachinethatgoesping.navigation.datastructures
_Shape = typing.Tuple[int, ...]

__all__ = [
    "SimradPing",
    "SimradPingRawData",
    "SimradPingRawData_mapped",
    "SimradPing_mapped"
]


class SimradPing():
    def __copy__(self) -> SimradPing: ...
    def __deepcopy__(self, arg0: dict) -> SimradPing: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> SimradPing: 
        """
        return a copy using the c++ default copy constructor
        """
    def feature_string(self, has_features: bool = True) -> str: ...
    def get_angle(self) -> numpy.ndarray[numpy.float32]: 
        """
        Returns the single target detection launch angle for each sample.

        This function calls: ping.raw_data.get_sample_data().get_angle()

        Throws:
            exception-object if angle data is not available for the specific
            datagram type

        Returns:
            xt::xtensor<float, 2>

        Compute the launch angle of the (sinle) target within each sample. If
        you see this comment, this function was not implemented for the
        current ping type.

        Returns:
            xt::xtensor<float, 2>
        """
    def get_file_nr(self) -> int: ...
    def get_file_path(self) -> str: ...
    def get_geolocation(self) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: 
        """
        < Geolocation of the transducer (object that hold lat,lon and attitude
        of
        """
    def get_number_of_samples(self) -> int: ...
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
        Compute volume backscattering strength (Sv) from raw data.

        This function calls: ping.raw_data.get_sample_data().get_power(dB)

        For single beam systems, this function returns the same value as
        get_sv_stacked (since there is only one beam to stack) However, the
        return type is a 2D matrix with one column, to be consistent with the
        multibeam case.

        Throws:
            exception-object if power data is not available for the specific
            datagram type

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 2>

        Compute volume backscattering. If you see this comment, this function
        was not implemented for the current ping type.

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 2>
        """
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
        Compute volume backscattering strength (Sv) from raw data.

        This function calls: ping.raw_data.get_sample_data().get_power(dB)

        For single beam systems, this function returns the same value as
        get_sv (since there is only one beam to stack) However, the return
        type is a 1D vector opposed to a one-column 2D matrix returned by
        get_sv

        Throws:
            exception-object if power data is not available for the specific
            datagram type

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 1>

        Compute stacked volume backscattering (sum over all beams). If you see
        this comment, this function was not implemented for the current ping
        type.

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 1>
        """
    def get_timestamp(self) -> float: 
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    def has_angle(self) -> bool: ...
    def has_sv(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_channel_id(self, channel_id: str) -> None: 
        """
        < channel id of the transducer
        """
    def set_geolocation(self, geolocation_latlon: themachinethatgoesping.navigation.datastructures.GeoLocationLatLon) -> None: 
        """
        < Geolocation of the transducer (object that hold lat,lon and attitude
        of
        """
    def set_timestamp(self, timestamp: float) -> None: 
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    @property
    def get_channel_id(self) -> str:
        """
        < channel id of the transducer

        :type: str
        """
    @property
    def raw_data(self) -> SimradPingRawData:
        """
        :type: SimradPingRawData
        """
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
class SimradPing_mapped():
    def __copy__(self) -> SimradPing_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradPing_mapped: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> SimradPing_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def feature_string(self, has_features: bool = True) -> str: ...
    def get_angle(self) -> numpy.ndarray[numpy.float32]: 
        """
        Returns the single target detection launch angle for each sample.

        This function calls: ping.raw_data.get_sample_data().get_angle()

        Throws:
            exception-object if angle data is not available for the specific
            datagram type

        Returns:
            xt::xtensor<float, 2>

        Compute the launch angle of the (sinle) target within each sample. If
        you see this comment, this function was not implemented for the
        current ping type.

        Returns:
            xt::xtensor<float, 2>
        """
    def get_file_nr(self) -> int: ...
    def get_file_path(self) -> str: ...
    def get_geolocation(self) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: 
        """
        < Geolocation of the transducer (object that hold lat,lon and attitude
        of
        """
    def get_number_of_samples(self) -> int: ...
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
        Compute volume backscattering strength (Sv) from raw data.

        This function calls: ping.raw_data.get_sample_data().get_power(dB)

        For single beam systems, this function returns the same value as
        get_sv_stacked (since there is only one beam to stack) However, the
        return type is a 2D matrix with one column, to be consistent with the
        multibeam case.

        Throws:
            exception-object if power data is not available for the specific
            datagram type

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 2>

        Compute volume backscattering. If you see this comment, this function
        was not implemented for the current ping type.

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 2>
        """
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
        Compute volume backscattering strength (Sv) from raw data.

        This function calls: ping.raw_data.get_sample_data().get_power(dB)

        For single beam systems, this function returns the same value as
        get_sv (since there is only one beam to stack) However, the return
        type is a 1D vector opposed to a one-column 2D matrix returned by
        get_sv

        Throws:
            exception-object if power data is not available for the specific
            datagram type

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 1>

        Compute stacked volume backscattering (sum over all beams). If you see
        this comment, this function was not implemented for the current ping
        type.

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 1>
        """
    def get_timestamp(self) -> float: 
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    def has_angle(self) -> bool: ...
    def has_sv(self) -> bool: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_channel_id(self, channel_id: str) -> None: 
        """
        < channel id of the transducer
        """
    def set_geolocation(self, geolocation_latlon: themachinethatgoesping.navigation.datastructures.GeoLocationLatLon) -> None: 
        """
        < Geolocation of the transducer (object that hold lat,lon and attitude
        of
        """
    def set_timestamp(self, timestamp: float) -> None: 
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    @property
    def get_channel_id(self) -> str:
        """
        < channel id of the transducer

        :type: str
        """
    @property
    def raw_data(self) -> SimradPingRawData_mapped:
        """
        :type: SimradPingRawData_mapped
        """
    pass
