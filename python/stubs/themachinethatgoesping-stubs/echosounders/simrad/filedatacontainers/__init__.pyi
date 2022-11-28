"""Simrad EK60 and EK80 file data container classes"""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad.filedatacontainers
import typing
import themachinethatgoesping.echosounders.simrad.filetypes
import themachinethatgoesping.tools.pyhelper

__all__ = [
    "SimradPingContainer",
    "SimradPingContainer_mapped"
]


class SimradPingContainer():
    @typing.overload
    def __call__(self, channel_id: str) -> SimradPingContainer: ...
    @typing.overload
    def __call__(self, channel_ids: typing.List[str]) -> SimradPingContainer: ...
    def __copy__(self) -> SimradPingContainer: ...
    def __deepcopy__(self, arg0: dict) -> SimradPingContainer: ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.filetypes.SimradPing: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradPingContainer: ...
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new empty PingContainer object

        Construct a new empty PingContainer object
        """
    @typing.overload
    def __init__(self, arg0: typing.List[themachinethatgoesping.echosounders.simrad.filetypes.SimradPing]) -> None: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradPingContainer: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradPingContainer]: ...
    def copy(self) -> SimradPingContainer: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_pings_per_channel_id(self) -> typing.Dict[str, int]: ...
    def find_channel_ids(self) -> typing.List[str]: ...
    def get_pings(self) -> typing.List[themachinethatgoesping.echosounders.simrad.filetypes.SimradPing]: ...
    def get_sorted_by_time(self) -> SimradPingContainer: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def max_number_of_samples(self) -> int: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
class SimradPingContainer_mapped():
    @typing.overload
    def __call__(self, channel_id: str) -> SimradPingContainer_mapped: ...
    @typing.overload
    def __call__(self, channel_ids: typing.List[str]) -> SimradPingContainer_mapped: ...
    def __copy__(self) -> SimradPingContainer_mapped: ...
    def __deepcopy__(self, arg0: dict) -> SimradPingContainer_mapped: ...
    @typing.overload
    def __getitem__(self, index: int) -> themachinethatgoesping.echosounders.simrad.filetypes.SimradPing_mapped: ...
    @typing.overload
    def __getitem__(self, slice: themachinethatgoesping.tools.pyhelper.PyIndexerSlice) -> SimradPingContainer_mapped: ...
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new empty PingContainer object

        Construct a new empty PingContainer object
        """
    @typing.overload
    def __init__(self, arg0: typing.List[themachinethatgoesping.echosounders.simrad.filetypes.SimradPing_mapped]) -> None: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __reversed__(self) -> SimradPingContainer_mapped: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def break_by_time_diff(self, max_time_diff_seconds: float) -> typing.List[SimradPingContainer_mapped]: ...
    def copy(self) -> SimradPingContainer_mapped: 
        """
        return a copy using the c++ default copy constructor
        """
    def count_pings_per_channel_id(self) -> typing.Dict[str, int]: ...
    def find_channel_ids(self) -> typing.List[str]: ...
    def get_pings(self) -> typing.List[themachinethatgoesping.echosounders.simrad.filetypes.SimradPing_mapped]: ...
    def get_sorted_by_time(self) -> SimradPingContainer_mapped: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def max_number_of_samples(self) -> int: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def size(self) -> int: ...
    pass
