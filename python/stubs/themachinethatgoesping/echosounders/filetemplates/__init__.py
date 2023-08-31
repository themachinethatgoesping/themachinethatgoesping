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
    "I_PingCommon",
    "I_PingWatercolumn"
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
    def load(self) -> None: ...
    def loaded(self) -> bool: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def release(self) -> None: ...
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
    def get_timestamp(self) -> float: 
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    def has_bottom(self) -> bool: ...
    def has_watercolumn(self) -> bool: ...
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
    @property
    def watercolumn(self) -> I_PingWatercolumn:
        """
        :type: I_PingWatercolumn
        """
    pass
class I_PingWatercolumn(I_PingCommon):
    """
    Interface for all ping watercolumn functions
    """
    def __copy__(self) -> I_PingWatercolumn: ...
    def __deepcopy__(self, arg0: dict) -> I_PingWatercolumn: ...
    def copy(self) -> I_PingWatercolumn: 
        """
        return a copy using the c++ default copy constructor
        """
    @typing.overload
    def get_amplitudes(self) -> numpy.ndarray[numpy.float32]: 
        """
        Get tha raw water amplitude data converted to float(32bit)

        Returns:
            xt::xtensor<float,2>

        Get tha raw water amplitude data converted to float(32bit)

        Returns:
            xt::xtensor<float,2>
        """
    @staticmethod
    @typing.overload
    def get_amplitudes(*args, **kwargs) -> typing.Any: ...
    def has_amplitudes(self) -> bool: 
        """
        Check this pings supports AMPLITUDES data

        Returns:
            true

        Returns:
            false
        """
    pass
