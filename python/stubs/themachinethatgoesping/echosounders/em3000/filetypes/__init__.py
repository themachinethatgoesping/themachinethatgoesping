"""EM3000 EK60 and EK80 file data types"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000.filetypes
import typing
import numpy
import themachinethatgoesping.echosounders.em3000
import themachinethatgoesping.echosounders.em3000.datagrams
import themachinethatgoesping.echosounders.filetemplates
import themachinethatgoesping.echosounders.pingtools
import themachinethatgoesping.navigation.datastructures
_Shape = typing.Tuple[int, ...]

__all__ = [
    "EM3000Ping",
    "EM3000PingRawData",
    "EM3000PingRawData_mapped",
    "EM3000Ping_mapped"
]


class EM3000Ping(themachinethatgoesping.echosounders.filetemplates.I_Ping):
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
    def get_transducer_ids(self) -> typing.Set[str]: 
        """
        Get all registered transducer ids (in case multiple transducers are
        associated with a single ping)

        Returns:
            std::set<std::string>
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
    def load_datagrams(self, skip_data: bool = True) -> None: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @typing.overload
    def raw_data(self, transducer_id: str) -> EM3000PingRawData: ...
    @typing.overload
    def raw_data(self) -> EM3000PingRawData: ...
    @typing.overload
    def select_transducer_id(self, transducer_id: str) -> None: 
        """
        Select a transducer id that will be used by default when calling
        functions on this ping. (Useful when multiple transducers are
        associated with a single ping.)

        Parameter ``id``:

        Select a transducer id that will be used by default when calling
        functions on this ping. (Useful when multiple transducers are
        associated with a single ping.)

        Parameter ``id``:
        """
    @typing.overload
    def select_transducer_id(self, transducer_number: int) -> None: ...
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
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def get_beam_pointing_angles(self) -> numpy.ndarray[numpy.float32]: ...
    @typing.overload
    def get_beam_pointing_angles(self, selection: themachinethatgoesping.echosounders.pingtools.BeamSampleSelection) -> numpy.ndarray[numpy.float32]: ...
    def get_detected_range_in_samples(self) -> numpy.ndarray[numpy.uint16]: ...
    def get_number_of_beams(self) -> int: ...
    def get_number_of_samples_per_beam(self) -> numpy.ndarray[numpy.uint16]: ...
    def get_runtime_parameters(self) -> themachinethatgoesping.echosounders.em3000.datagrams.RuntimeParameters: ...
    def get_start_range_sample_numbers(self) -> numpy.ndarray[numpy.uint16]: ...
    def get_timestamp_first(self) -> float: ...
    def get_transmit_sector_numbers(self) -> numpy.ndarray[numpy.uint8]: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string

        Return object information as string
        """
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def load_datagrams(self, skip_data: bool = True) -> None: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information

        Print object information
        """
    def read_all_samples(self) -> numpy.ndarray[numpy.float32]: ...
    def read_merged_watercolumndatagram(self, skip_data: bool = False) -> themachinethatgoesping.echosounders.em3000.datagrams.WaterColumnDatagram: ...
    def read_selected_samples(self, selection: themachinethatgoesping.echosounders.pingtools.BeamSampleSelection) -> numpy.ndarray[numpy.float32]: ...
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
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    @typing.overload
    def get_beam_pointing_angles(self) -> numpy.ndarray[numpy.float32]: ...
    @typing.overload
    def get_beam_pointing_angles(self, selection: themachinethatgoesping.echosounders.pingtools.BeamSampleSelection) -> numpy.ndarray[numpy.float32]: ...
    def get_detected_range_in_samples(self) -> numpy.ndarray[numpy.uint16]: ...
    def get_number_of_beams(self) -> int: ...
    def get_number_of_samples_per_beam(self) -> numpy.ndarray[numpy.uint16]: ...
    def get_runtime_parameters(self) -> themachinethatgoesping.echosounders.em3000.datagrams.RuntimeParameters: ...
    def get_start_range_sample_numbers(self) -> numpy.ndarray[numpy.uint16]: ...
    def get_timestamp_first(self) -> float: ...
    def get_transmit_sector_numbers(self) -> numpy.ndarray[numpy.uint8]: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string

        Return object information as string
        """
    def keys(self) -> typing.List[themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier]: ...
    def load_datagrams(self, skip_data: bool = True) -> None: ...
    @staticmethod
    def per_file(*args, **kwargs) -> typing.Any: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information

        Print object information
        """
    def read_all_samples(self) -> numpy.ndarray[numpy.float32]: ...
    def read_merged_watercolumndatagram(self, skip_data: bool = False) -> themachinethatgoesping.echosounders.em3000.datagrams.WaterColumnDatagram: ...
    def read_selected_samples(self, selection: themachinethatgoesping.echosounders.pingtools.BeamSampleSelection) -> numpy.ndarray[numpy.float32]: ...
    pass
class EM3000Ping_mapped(themachinethatgoesping.echosounders.filetemplates.I_Ping):
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
    def get_transducer_ids(self) -> typing.Set[str]: 
        """
        Get all registered transducer ids (in case multiple transducers are
        associated with a single ping)

        Returns:
            std::set<std::string>
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
    def load_datagrams(self, skip_data: bool = True) -> None: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @typing.overload
    def raw_data(self, transducer_id: str) -> EM3000PingRawData_mapped: ...
    @typing.overload
    def raw_data(self) -> EM3000PingRawData_mapped: ...
    @typing.overload
    def select_transducer_id(self, transducer_id: str) -> None: 
        """
        Select a transducer id that will be used by default when calling
        functions on this ping. (Useful when multiple transducers are
        associated with a single ping.)

        Parameter ``id``:

        Select a transducer id that will be used by default when calling
        functions on this ping. (Useful when multiple transducers are
        associated with a single ping.)

        Parameter ``id``:
        """
    @typing.overload
    def select_transducer_id(self, transducer_number: int) -> None: ...
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
