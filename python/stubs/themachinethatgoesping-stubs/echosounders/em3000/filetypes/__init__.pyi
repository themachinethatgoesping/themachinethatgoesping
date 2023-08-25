"""EM3000 EK60 and EK80 file data types"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000.filetypes
import typing
import numpy
import themachinethatgoesping.algorithms.geoprocessing.datastructures
import themachinethatgoesping.echosounders.em3000
import themachinethatgoesping.echosounders.em3000.datagrams
import themachinethatgoesping.echosounders.filetemplates
import themachinethatgoesping.echosounders.pingtools
_Shape = typing.Tuple[int, ...]

__all__ = [
    "EM3000Ping",
    "EM3000PingBottom",
    "EM3000PingBottom_mapped",
    "EM3000PingCommon",
    "EM3000PingCommon_mapped",
    "EM3000PingRawData",
    "EM3000PingRawData_mapped",
    "EM3000Ping_mapped"
]


class EM3000PingCommon(themachinethatgoesping.echosounders.filetemplates.I_PingCommon):
    def __copy__(self) -> EM3000PingCommon: ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingCommon: ...
    def copy(self) -> EM3000PingCommon: 
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def raw_data(self) -> EM3000PingRawData:
        """
        :type: EM3000PingRawData
        """
    pass
class EM3000PingBottom(themachinethatgoesping.echosounders.filetemplates.I_PingBottom, EM3000PingCommon, themachinethatgoesping.echosounders.filetemplates.I_PingCommon):
    def __copy__(self) -> EM3000PingBottom: ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingBottom: ...
    def copy(self) -> EM3000PingBottom: 
        """
        return a copy using the c++ default copy constructor
        """
    pass
class EM3000PingCommon_mapped(themachinethatgoesping.echosounders.filetemplates.I_PingCommon):
    def __copy__(self) -> EM3000PingCommon_mapped: ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingCommon_mapped: ...
    def copy(self) -> EM3000PingCommon_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    @property
    def raw_data(self) -> EM3000PingRawData_mapped:
        """
        :type: EM3000PingRawData_mapped
        """
    pass
class EM3000Ping(themachinethatgoesping.echosounders.filetemplates.I_Ping, EM3000PingCommon, themachinethatgoesping.echosounders.filetemplates.I_PingCommon):
    def __copy__(self) -> EM3000Ping: ...
    def __deepcopy__(self, arg0: dict) -> EM3000Ping: ...
    def copy(self) -> EM3000Ping: 
        """
        return a copy using the c++ default copy constructor
        """
    def load_datagrams(self, skip_data: bool = True) -> None: ...
    pass
class EM3000PingBottom_mapped(themachinethatgoesping.echosounders.filetemplates.I_PingBottom, EM3000PingCommon_mapped, themachinethatgoesping.echosounders.filetemplates.I_PingCommon):
    def __copy__(self) -> EM3000PingBottom_mapped: ...
    def __deepcopy__(self, arg0: dict) -> EM3000PingBottom_mapped: ...
    def copy(self) -> EM3000PingBottom_mapped: 
        """
        return a copy using the c++ default copy constructor
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
    def get_water_column_datagram(self) -> themachinethatgoesping.echosounders.em3000.datagrams.WaterColumnDatagram: ...
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
    @typing.overload
    def read_xyz(self) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1: 
        """
        read XYZ for the bottom detection datagram

        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>

        read XYZ for the specified beams from the bottom detection datagram
        Note: if the beam numbers from the beam selection exceed the number of
        beams in the datagram, the corresponding XYZ values will be NaN

        Parameter ``bs``:
            beam selection

        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>
        """
    @typing.overload
    def read_xyz(self, selection: themachinethatgoesping.echosounders.pingtools.BeamSelection) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1: ...
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
    def get_water_column_datagram(self) -> themachinethatgoesping.echosounders.em3000.datagrams.WaterColumnDatagram: ...
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
    @typing.overload
    def read_xyz(self) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1: 
        """
        read XYZ for the bottom detection datagram

        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>

        read XYZ for the specified beams from the bottom detection datagram
        Note: if the beam numbers from the beam selection exceed the number of
        beams in the datagram, the corresponding XYZ values will be NaN

        Parameter ``bs``:
            beam selection

        Returns:
            algorithms::geoprocessing::datastructures::XYZ<1>
        """
    @typing.overload
    def read_xyz(self, selection: themachinethatgoesping.echosounders.pingtools.BeamSelection) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.XYZ_1: ...
    pass
class EM3000Ping_mapped(themachinethatgoesping.echosounders.filetemplates.I_Ping, EM3000PingCommon_mapped, themachinethatgoesping.echosounders.filetemplates.I_PingCommon):
    def __copy__(self) -> EM3000Ping_mapped: ...
    def __deepcopy__(self, arg0: dict) -> EM3000Ping_mapped: ...
    def copy(self) -> EM3000Ping_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def load_datagrams(self, skip_data: bool = True) -> None: ...
    pass
