"""Simrad EK60 and EK80 file data types"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad.filetypes
import typing
import numpy
import themachinethatgoesping.echosounders.filetemplates
import themachinethatgoesping.echosounders.pingtools
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


class SimradPing(themachinethatgoesping.echosounders.filetemplates.I_Ping):
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
        Compute the launch angle of the (sinle) target within each sample. If
        you see this comment, this function was not implemented for the
        current ping type.

        Returns:
            xt::xtensor<float, 2>
        """
    @typing.overload
    def get_beam_pointing_angles(self) -> numpy.ndarray[numpy.float32]: 
        """
        Get the beam pointing angles in °.

        Parameter ``transducer_id``:
            $Returns:

        xt::xtensor<float, 1> in °

        Get the beam pointing angles from a specific transducer in °. (Useful
        when multiple transducers are associated with a single ping.)

        Parameter ``transducer_id``:
            $Returns:

        xt::xtensor<float, 1> in °

        Get the beam pointing angles in ° when specifying the beams and
        samples to select.

        Parameter ``selection:``:
            Structure containing information about which beams and samples to
            select.

        Returns:
            xt::xtensor<float, 1> in °
        """
    @typing.overload
    def get_beam_pointing_angles(self, transducer_id: str) -> numpy.ndarray[numpy.float32]: ...
    @typing.overload
    def get_beam_pointing_angles(self, selection: themachinethatgoesping.echosounders.pingtools.PingSampleSelection) -> numpy.ndarray[numpy.float32]: ...
    def get_channel_id(self) -> str: 
        """
        < channel id of the transducer
        """
    def get_file_nr(self) -> int: ...
    def get_file_path(self) -> str: ...
    @typing.overload
    def get_geolocation(self) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: 
        """
        < Geolocation of the transducer with the specified transducer_id. A

        < Geolocation of the transducer with the specified transducer_id. A
        """
    @typing.overload
    def get_geolocation(self, transducer_id: str) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: ...
    @typing.overload
    def get_number_of_beams(self) -> int: 
        """
        Get the number of beams

        Returns:
            size_t

        Get the number of beams from a specific transducer (Useful when
        multiple transducers are associated with a single ping.)

        Parameter ``transducer_id``:
            transducer id

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
    @typing.overload
    def get_number_of_beams(self, transducer_id: str) -> int: ...
    @typing.overload
    def get_number_of_beams(self, selection: themachinethatgoesping.echosounders.pingtools.PingSampleSelection) -> int: ...
    @typing.overload
    def get_number_of_samples_per_beam(self) -> numpy.ndarray[numpy.uint16]: 
        """
        Get the number of samples per beam

        Parameter ``transducer_id``:
            $Returns:

        xt::xtensor<uint16_t, 1>

        Get the number of samples per beam of a specific transducer. (Useful
        when multiple transducers are associated with a single ping.)

        Parameter ``transducer_id:``:
            id of the transducer

        Returns:
            xt::xtensor<uint16_t, 1>

        Get the number of samples per beam of a specific transducer. (Useful
        when multiple transducers are associated with a single ping.)

        Parameter ``transducer_id:``:
            id of the transducer

        Returns:
            xt::xtensor<uint16_t, 1>

        Get the number of samples per beam of a specific transducer. (Useful
        when multiple transducers are associated with a single ping.)

        Parameter ``transducer_id:``:
            id of the transducer

        Returns:
            xt::xtensor<uint16_t, 1>
        """
    @typing.overload
    def get_number_of_samples_per_beam(self, transducer_id: str) -> numpy.ndarray[numpy.uint16]: ...
    @typing.overload
    def get_number_of_samples_per_beam(self, selection: themachinethatgoesping.echosounders.pingtools.PingSampleSelection) -> numpy.ndarray[numpy.uint16]: ...
    @typing.overload
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
        Compute volume backscattering. If you see this comment, this function
        was not implemented for the current ping type.

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 2>

        Compute volume backscattering of a specific transducer. (Useful when
        multiple transducers are associated with a single ping.) If you see
        this comment, this function was not implemented for the current ping
        type.

        Parameter ``transducer_id``:
            transducer id

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 2>

        Compute volume backscattering. If you see this comment, this function
        was not implemented for the current ping type.

        Parameter ``selection``:
            structure with selected transducer_ids/beams/samples considered
            for this function

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 1>
        """
    @typing.overload
    def get_sv(self, transducer_id: str, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    @typing.overload
    def get_sv(self, selection: themachinethatgoesping.echosounders.pingtools.PingSampleSelection, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
        Compute stacked volume backscattering (sum over all beams). If you see
        this comment, this function was not implemented for the current ping
        type.

        Parameter ``selection``:
            structure with selected transducer_ids/beams/samples considered
            for this function

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 1>
        """
    def get_timestamp(self) -> float: 
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    def get_transducer_id(self) -> str: 
        """
        Get the transducer id of the ping. In case multiple transducer ids are
        associated with a single ping, this function will return the one
        selected with the "select_transducer_id" function.
        """
    def get_transducer_ids(self) -> typing.List[str]: 
        """
        Get all registered transducer ids (in case multiple transducers are
        associated with a single ping)

        Returns:
            std::vector<std::string>
        """
    def get_transducer_ids_as_string(self) -> str: 
        """
        Get all register transducer ids as a string (useful for printing)

        Returns:
            std::string
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
    def raw_data(self) -> SimradPingRawData: ...
    def set_channel_id(self, channel_id: str) -> None: 
        """
        < channel id of the transducer
        """
    @typing.overload
    def set_geolocation(self, geolocation_latlon: themachinethatgoesping.navigation.datastructures.GeoLocationLatLon) -> None: 
        """
        < Geolocation of the transducer with the specified transducer_id. A

        < Geolocation of the transducer with the specified transducer_id. A
        """
    @typing.overload
    def set_geolocation(self, transducer_id: str, geolocation_latlon: themachinethatgoesping.navigation.datastructures.GeoLocationLatLon) -> None: ...
    def set_timestamp(self, timestamp: float) -> None: 
        """
        < Unix timestamp in seconds (saved in UTC0)
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
class SimradPing_mapped(themachinethatgoesping.echosounders.filetemplates.I_Ping):
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
        Compute the launch angle of the (sinle) target within each sample. If
        you see this comment, this function was not implemented for the
        current ping type.

        Returns:
            xt::xtensor<float, 2>
        """
    @typing.overload
    def get_beam_pointing_angles(self) -> numpy.ndarray[numpy.float32]: 
        """
        Get the beam pointing angles in °.

        Parameter ``transducer_id``:
            $Returns:

        xt::xtensor<float, 1> in °

        Get the beam pointing angles from a specific transducer in °. (Useful
        when multiple transducers are associated with a single ping.)

        Parameter ``transducer_id``:
            $Returns:

        xt::xtensor<float, 1> in °

        Get the beam pointing angles in ° when specifying the beams and
        samples to select.

        Parameter ``selection:``:
            Structure containing information about which beams and samples to
            select.

        Returns:
            xt::xtensor<float, 1> in °
        """
    @typing.overload
    def get_beam_pointing_angles(self, transducer_id: str) -> numpy.ndarray[numpy.float32]: ...
    @typing.overload
    def get_beam_pointing_angles(self, selection: themachinethatgoesping.echosounders.pingtools.PingSampleSelection) -> numpy.ndarray[numpy.float32]: ...
    def get_channel_id(self) -> str: 
        """
        < channel id of the transducer
        """
    def get_file_nr(self) -> int: ...
    def get_file_path(self) -> str: ...
    @typing.overload
    def get_geolocation(self) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: 
        """
        < Geolocation of the transducer with the specified transducer_id. A

        < Geolocation of the transducer with the specified transducer_id. A
        """
    @typing.overload
    def get_geolocation(self, transducer_id: str) -> themachinethatgoesping.navigation.datastructures.GeoLocationLatLon: ...
    @typing.overload
    def get_number_of_beams(self) -> int: 
        """
        Get the number of beams

        Returns:
            size_t

        Get the number of beams from a specific transducer (Useful when
        multiple transducers are associated with a single ping.)

        Parameter ``transducer_id``:
            transducer id

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
    @typing.overload
    def get_number_of_beams(self, transducer_id: str) -> int: ...
    @typing.overload
    def get_number_of_beams(self, selection: themachinethatgoesping.echosounders.pingtools.PingSampleSelection) -> int: ...
    @typing.overload
    def get_number_of_samples_per_beam(self) -> numpy.ndarray[numpy.uint16]: 
        """
        Get the number of samples per beam

        Parameter ``transducer_id``:
            $Returns:

        xt::xtensor<uint16_t, 1>

        Get the number of samples per beam of a specific transducer. (Useful
        when multiple transducers are associated with a single ping.)

        Parameter ``transducer_id:``:
            id of the transducer

        Returns:
            xt::xtensor<uint16_t, 1>

        Get the number of samples per beam of a specific transducer. (Useful
        when multiple transducers are associated with a single ping.)

        Parameter ``transducer_id:``:
            id of the transducer

        Returns:
            xt::xtensor<uint16_t, 1>

        Get the number of samples per beam of a specific transducer. (Useful
        when multiple transducers are associated with a single ping.)

        Parameter ``transducer_id:``:
            id of the transducer

        Returns:
            xt::xtensor<uint16_t, 1>
        """
    @typing.overload
    def get_number_of_samples_per_beam(self, transducer_id: str) -> numpy.ndarray[numpy.uint16]: ...
    @typing.overload
    def get_number_of_samples_per_beam(self, selection: themachinethatgoesping.echosounders.pingtools.PingSampleSelection) -> numpy.ndarray[numpy.uint16]: ...
    @typing.overload
    def get_sv(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
        Compute volume backscattering. If you see this comment, this function
        was not implemented for the current ping type.

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 2>

        Compute volume backscattering of a specific transducer. (Useful when
        multiple transducers are associated with a single ping.) If you see
        this comment, this function was not implemented for the current ping
        type.

        Parameter ``transducer_id``:
            transducer id

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 2>

        Compute volume backscattering. If you see this comment, this function
        was not implemented for the current ping type.

        Parameter ``selection``:
            structure with selected transducer_ids/beams/samples considered
            for this function

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 1>
        """
    @typing.overload
    def get_sv(self, transducer_id: str, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    @typing.overload
    def get_sv(self, selection: themachinethatgoesping.echosounders.pingtools.PingSampleSelection, dB: bool = False) -> numpy.ndarray[numpy.float32]: ...
    def get_sv_stacked(self, dB: bool = False) -> numpy.ndarray[numpy.float32]: 
        """
        Compute stacked volume backscattering (sum over all beams). If you see
        this comment, this function was not implemented for the current ping
        type.

        Parameter ``selection``:
            structure with selected transducer_ids/beams/samples considered
            for this function

        Parameter ``dB``:
            Output Sv in dB if true, or linear if false (default).

        Returns:
            xt::xtensor<float, 1>
        """
    def get_timestamp(self) -> float: 
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    def get_transducer_id(self) -> str: 
        """
        Get the transducer id of the ping. In case multiple transducer ids are
        associated with a single ping, this function will return the one
        selected with the "select_transducer_id" function.
        """
    def get_transducer_ids(self) -> typing.List[str]: 
        """
        Get all registered transducer ids (in case multiple transducers are
        associated with a single ping)

        Returns:
            std::vector<std::string>
        """
    def get_transducer_ids_as_string(self) -> str: 
        """
        Get all register transducer ids as a string (useful for printing)

        Returns:
            std::string
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
    def raw_data(self) -> SimradPingRawData_mapped: ...
    def set_channel_id(self, channel_id: str) -> None: 
        """
        < channel id of the transducer
        """
    @typing.overload
    def set_geolocation(self, geolocation_latlon: themachinethatgoesping.navigation.datastructures.GeoLocationLatLon) -> None: 
        """
        < Geolocation of the transducer with the specified transducer_id. A

        < Geolocation of the transducer with the specified transducer_id. A
        """
    @typing.overload
    def set_geolocation(self, transducer_id: str, geolocation_latlon: themachinethatgoesping.navigation.datastructures.GeoLocationLatLon) -> None: ...
    def set_timestamp(self, timestamp: float) -> None: 
        """
        < Unix timestamp in seconds (saved in UTC0)
        """
    pass
