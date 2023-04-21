"""EM3000 EK60 and EK80 file data types"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000.filetypes
import typing
import numpy
import themachinethatgoesping.echosounders.em3000
import themachinethatgoesping.navigation.datastructures
_Shape = typing.Tuple[int, ...]

__all__ = [
    "EM3000Ping",
    "EM3000PingRawData",
    "EM3000PingRawData_mapped",
    "EM3000Ping_mapped"
]


class EM3000Ping():
    def __copy__(self) -> EM3000Ping: ...
    def __deepcopy__(self, arg0: dict) -> EM3000Ping: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> EM3000Ping: 
        """
        return a copy using the c++ default copy constructor
        """
    def feature_string(self, has_features: bool = True) -> str: ...
    def get_angle(self) -> numpy.ndarray[numpy.float32]: 
        """
        Compute the launch angle of the (sinle) target within each sample. If
        you see this comment, this function was not implemented for the
        current ping type.

        Returns:
            xt::xtensor<float, 2>
        """
    def get_file_nr(self) -> int: ...
    def get_file_path(self) -> str: ...
    def get_geolocation(self, transducer_id: str) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: 
        """
        < Geolocation of the transducer with the specified transducer_id. A
        """
    def get_number_of_samples(self) -> int: ...
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
        Compute volume backscattering. If you see this comment, this function
        was not implemented for the current ping type.

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 2>
        """
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
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
    def is_dual_rx(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_channel_id(self, channel_id: str) -> None: 
        """
        < channel id of the transducer
        """
    def set_geolocation(self, transducer_id: str, geolocation_latlon: themachinethatgoesping.navigation.datastructures.GeoLocationLatLon) -> None: 
        """
        < Geolocation of the transducer with the specified transducer_id. A
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
    def raw_data(self) -> EM3000PingRawData:
        """
        :type: EM3000PingRawData
        """
    pass
class EM3000PingRawData():
    def __copy__(self) -> EM3000PingRawData: ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingRawData: ...
    def __repr__(self) -> str: 
        """
        Return object information as string

        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string

        Return object information as string
        """
    def copy(self) -> EM3000PingRawData: 
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    def get_timestamp_first(self) -> float: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string

        Return object information as string
        """
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information

        Print object information
        """
    pass
class EM3000PingRawData_mapped():
    def __copy__(self) -> EM3000PingRawData_mapped: ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingRawData_mapped: ...
    def __repr__(self) -> str: 
        """
        Return object information as string

        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string

        Return object information as string
        """
    def copy(self) -> EM3000PingRawData_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def datagram_headers(self) -> object: ...
    @typing.overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    def get_timestamp_first(self) -> float: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string

        Return object information as string
        """
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information

        Print object information
        """
    pass
class EM3000Ping_mapped():
    def __copy__(self) -> EM3000Ping_mapped: ...
    def __deepcopy__(self, arg0: dict) -> EM3000Ping_mapped: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> EM3000Ping_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def feature_string(self, has_features: bool = True) -> str: ...
    def get_angle(self) -> numpy.ndarray[numpy.float32]: 
        """
        Compute the launch angle of the (sinle) target within each sample. If
        you see this comment, this function was not implemented for the
        current ping type.

        Returns:
            xt::xtensor<float, 2>
        """
    def get_file_nr(self) -> int: ...
    def get_file_path(self) -> str: ...
    def get_geolocation(self, transducer_id: str) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: 
        """
        < Geolocation of the transducer with the specified transducer_id. A
        """
    def get_number_of_samples(self) -> int: ...
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
        Compute volume backscattering. If you see this comment, this function
        was not implemented for the current ping type.

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 2>
        """
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
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
    def is_dual_rx(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_channel_id(self, channel_id: str) -> None: 
        """
        < channel id of the transducer
        """
    def set_geolocation(self, transducer_id: str, geolocation_latlon: themachinethatgoesping.navigation.datastructures.GeoLocationLatLon) -> None: 
        """
        < Geolocation of the transducer with the specified transducer_id. A
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
    def raw_data(self) -> EM3000PingRawData_mapped:
        """
        :type: EM3000PingRawData_mapped
        """
    pass
