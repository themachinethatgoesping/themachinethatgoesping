"""EM3000 EK60 and EK80 file data types"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000.filetypes
import typing
import numpy
import themachinethatgoesping.echosounders.em3000
import themachinethatgoesping.echosounders.em3000.datagrams
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
    def get_beam_numbers(self) -> typing.List[int]: ...
    def get_beam_pointing_angles(self) -> typing.List[float]: ...
    def get_detected_range_in_samples(self) -> typing.List[int]: ...
    def get_first_sample_ensemble(self) -> int: ...
    def get_number_of_beams(self) -> int: ...
    def get_number_of_samples_ensemble(self) -> int: ...
    def get_number_of_samples_per_beam(self) -> typing.List[int]: ...
    def get_number_of_selected_beams(self) -> int: ...
    def get_runtime_parameters(self) -> themachinethatgoesping.echosounders.em3000.datagrams.RuntimeParameters: ...
    @staticmethod
    def get_sample_positions(*args, **kwargs) -> typing.Any: ...
    def get_selected_beam_numbers(self) -> typing.List[int]: ...
    def get_selected_beam_pointing_angles(self) -> typing.List[float]: ...
    def get_selected_first_sample_per_beam(self) -> typing.List[int]: ...
    def get_selected_number_of_samples_per_beam(self) -> typing.List[int]: ...
    def get_start_range_sample_numbers(self) -> typing.List[int]: ...
    def get_timestamp_first(self) -> float: ...
    def get_transmit_sector_number(self) -> typing.List[int]: ...
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
    def read_merged_watercolumndatagram(self, skip_data: bool = False) -> themachinethatgoesping.echosounders.em3000.datagrams.WaterColumnDatagram: ...
    def read_selected_samples(self) -> numpy.ndarray[numpy.float32]: 
        """
        read the selected samples from the selected beams and convert them to
        float

        Returns:
            xt::xtensor<float, 2>
        """
    def select_beams_by_angle(self, min_angle: float, max_angle: float) -> None: 
        """
        select the beams to be read from the water column datagram

        Parameter ``min_beam_angle``:
            Minimum beam angle in degrees

        Parameter ``max_beam_angle``:
            Maximum beam angle in degrees
        """
    def select_beams_by_number(self, beam_numbers: typing.List[int]) -> None: 
        """
        select the beams to be read from the water column datagram

        Parameter ``selected_beam_numbers``:
        """
    def select_samples_by_first_last(self, first_sample: int, last_sample: int) -> None: 
        """
        select the samples to be read from the water column datagram

        Parameter ``first_sample``:
            first sample number in the datagram

        Parameter ``last_sample``:
            last sample number in the datagram
        """
    def select_samples_by_range(self, first_sample: int, number_of_samples: int) -> None: 
        """
        select the samples to be read from the water column datagram

        Parameter ``first_sample``:
            First sample number in the datagram

        Parameter ``number_of_samples``:
            Number of samples to read
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
    def datagrams(self, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier, skip_data: bool = False) -> object: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    @typing.overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders.em3000.t_EM3000DatagramIdentifier) -> object: ...
    def get_beam_numbers(self) -> typing.List[int]: ...
    def get_beam_pointing_angles(self) -> typing.List[float]: ...
    def get_detected_range_in_samples(self) -> typing.List[int]: ...
    def get_first_sample_ensemble(self) -> int: ...
    def get_number_of_beams(self) -> int: ...
    def get_number_of_samples_ensemble(self) -> int: ...
    def get_number_of_samples_per_beam(self) -> typing.List[int]: ...
    def get_number_of_selected_beams(self) -> int: ...
    def get_runtime_parameters(self) -> themachinethatgoesping.echosounders.em3000.datagrams.RuntimeParameters: ...
    @staticmethod
    def get_sample_positions(*args, **kwargs) -> typing.Any: ...
    def get_selected_beam_numbers(self) -> typing.List[int]: ...
    def get_selected_beam_pointing_angles(self) -> typing.List[float]: ...
    def get_selected_first_sample_per_beam(self) -> typing.List[int]: ...
    def get_selected_number_of_samples_per_beam(self) -> typing.List[int]: ...
    def get_start_range_sample_numbers(self) -> typing.List[int]: ...
    def get_timestamp_first(self) -> float: ...
    def get_transmit_sector_number(self) -> typing.List[int]: ...
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
    def read_merged_watercolumndatagram(self, skip_data: bool = False) -> themachinethatgoesping.echosounders.em3000.datagrams.WaterColumnDatagram: ...
    def read_selected_samples(self) -> numpy.ndarray[numpy.float32]: 
        """
        read the selected samples from the selected beams and convert them to
        float

        Returns:
            xt::xtensor<float, 2>
        """
    def select_beams_by_angle(self, min_angle: float, max_angle: float) -> None: 
        """
        select the beams to be read from the water column datagram

        Parameter ``min_beam_angle``:
            Minimum beam angle in degrees

        Parameter ``max_beam_angle``:
            Maximum beam angle in degrees
        """
    def select_beams_by_number(self, beam_numbers: typing.List[int]) -> None: 
        """
        select the beams to be read from the water column datagram

        Parameter ``selected_beam_numbers``:
        """
    def select_samples_by_first_last(self, first_sample: int, last_sample: int) -> None: 
        """
        select the samples to be read from the water column datagram

        Parameter ``first_sample``:
            first sample number in the datagram

        Parameter ``last_sample``:
            last sample number in the datagram
        """
    def select_samples_by_range(self, first_sample: int, number_of_samples: int) -> None: 
        """
        select the samples to be read from the water column datagram

        Parameter ``first_sample``:
            First sample number in the datagram

        Parameter ``number_of_samples``:
            Number of samples to read
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
