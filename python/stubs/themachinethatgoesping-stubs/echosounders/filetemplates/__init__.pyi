"""Trampoline classes for abstract file template classes"""
from __future__ import annotations
import themachinethatgoesping.echosounders.filetemplates
import typing
import numpy
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import themachinethatgoesping.navigation.datastructures
_Shape = typing.Tuple[int, ...]

__all__ = [
    "I_Ping",
    "I_PingBottom",
    "I_PingCommon"
]


class I_PingCommon():
    def __copy__(self) -> I_PingCommon: ...
    def __deepcopy__(self, arg0: dict) -> I_PingCommon: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> I_PingCommon: 
        """
        return a copy using the c++ default copy constructor
        """
    def feature_string(self, has_features: bool = True) -> str: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class I_PingBottom(I_PingCommon):
    """
    Interface for all ping bottom detection functions
    """
    def __copy__(self) -> I_PingBottom: ...
    def __deepcopy__(self, arg0: dict) -> I_PingBottom: ...
    def copy(self) -> I_PingBottom: 
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def get_two_way_travel_times(self) -> numpy.ndarray[numpy.float32]: 
        """
        Get the two way travel times of the bottom detection samples

        Returns:
            xt::xtensor<float, 1>

        Get the two way travel times of the bottom detection samples

        Returns:
            xt::xtensor<float, 1>
        """
    @staticmethod
    @typing.overload
    def get_two_way_travel_times(*args, **kwargs) -> typing.Any: ...
    @typing.overload
    def get_xyz(self) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1: 
        """
        Get an XYZ object containing the XYZ position of the bottom detection
        Note: XYZ is in the local coordinate system of the ping! To convert it
        use algorithms::geoprocessing::georeferencer class or - Use
        get_xyz_utm() to get the bottom detection in UTM coordinates - Use
        get_xyz_latlon() to get the bottom detection in Latitude/Longitude
        coordinates

        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>

        Get an XYZ object containing the XYZ position of the bottom detection
        Note: XYZ is in the local coordinate system of the ping! To convert it
        use algorithms::geoprocessing::georeferencer class or - Use
        get_xyz_utm() to get the bottom detection in UTM coordinates - Use
        get_xyz_latlon() to get the bottom detection in Latitude/Longitude
        coordinates

        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>
        """
    @staticmethod
    @typing.overload
    def get_xyz(*args, **kwargs) -> typing.Any: ...
    def has_xyz(self) -> bool: 
        """
        Check this pings supports XYZ data

        Returns:
            true

        Returns:
            false
        """
    pass
class I_Ping(I_PingCommon):
    def __copy__(self) -> I_Ping: ...
    def __deepcopy__(self, arg0: dict) -> I_Ping: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> I_Ping: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_angle(self) -> numpy.ndarray[numpy.float32]: 
        """
        Compute the launch angle of the (single) target within each sample. If
        you see this comment, this function was not implemented for the
        current ping type.

        Returns:
            xt::xtensor<float, 2>
        """
    @typing.overload
    def get_beam_pointing_angles(self) -> numpy.ndarray[numpy.float32]: 
        """
        Get the beam pointing angles in °.

        Returns:
            xt::xtensor<float, 1> in °

        Get the beam pointing angles in ° when specifying the beams and
        samples to select.

        Parameter ``selection:``:
            Structure containing information about which beams and samples to
            select.

        Returns:
            xt::xtensor<float, 1> in °
        """
    @staticmethod
    @typing.overload
    def get_beam_pointing_angles(*args, **kwargs) -> typing.Any: ...
    def get_channel_id(self) -> str: 
        """
        < channel id of the transducer
        """
    def get_file_nr(self) -> int: ...
    def get_file_path(self) -> str: ...
    def get_geolocation(self) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: 
        """
        Get the geolocation of the transducer.

        Returns:
            const navigation::datastructures::GeoLocationLatLon&
        """
    @typing.overload
    def get_number_of_beams(self) -> int: 
        """
        Get the number of beams

        Returns:
            size_t

        Get the number of beams when specifying the beams and samples to
        select. Note: this function just returns
        selection.get_number_of_beams()

        Parameter ``selection:``:
            Structure containing information about which beams and samples to
            select.

        Returns:
            size_t
        """
    @staticmethod
    @typing.overload
    def get_number_of_beams(*args, **kwargs) -> typing.Any: ...
    @typing.overload
    def get_number_of_samples_per_beam(self) -> numpy.ndarray[numpy.uint16]: 
        """
        Get the number of samples per beam

        Returns:
            xt::xtensor<uint16_t, 1>

        Get the number of samples per beam when specifying the beams and
        samples to select. Note: this function just returns an array of
        selection.get_number_of_samples_ensemble()

        Parameter ``selection:``:
            Structure containing information about which beams and samples to
            select.

        Returns:
            xt::xtensor<uint16_t, 1>
        """
    @staticmethod
    @typing.overload
    def get_number_of_samples_per_beam(*args, **kwargs) -> typing.Any: ...
    @typing.overload
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
        Compute volume backscattering. If you see this comment, this function
        was not implemented for the current ping type.

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 2>

        Compute volume backscattering. If you see this comment, this function
        was not implemented for the current ping type.

        Parameter ``selection``:
            structure with selected beams/samples considered for this function

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 1>
        """
    @staticmethod
    @typing.overload
    def get_sv(*args, **kwargs) -> typing.Any: ...
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
        Compute stacked volume backscattering (sum over all beams). If you see
        this comment, this function was not implemented for the current ping
        type.

        Parameter ``selection``:
            structure with selected beams/samples considered for this function

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
        Get the geolocation of the transducer.

        Returns:
            const navigation::datastructures::GeoLocationLatLon&
        """
    def set_timestamp(self, timestamp: float) -> None: 
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    @property
    def bottom(self) -> I_PingBottom:
        """
        :type: I_PingBottom
        """
    pass
