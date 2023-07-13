"""Tools for working with ping objects."""
from __future__ import annotations
import themachinethatgoesping.echosounders.pingtools
import typing

__all__ = [
    "PingSampleSelection",
    "PingSampleSelector"
]


class PingSampleSelection():
    def __copy__(self) -> PingSampleSelection: ...
    def __deepcopy__(self, arg0: dict) -> PingSampleSelection: ...
    def __eq__(self, other: PingSampleSelection) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> PingSampleSelection: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> PingSampleSelection: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
class PingSampleSelector():
    def __copy__(self) -> PingSampleSelector: ...
    def __deepcopy__(self, arg0: dict) -> PingSampleSelector: ...
    def __eq__(self, other: PingSampleSelector) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def clear(self) -> None: ...
    def clear_beam_angle_range(self) -> None: ...
    def clear_beam_number_range(self) -> None: ...
    def clear_beam_step(self) -> None: ...
    def clear_sample_number_range(self) -> None: ...
    def clear_sample_range_range(self) -> None: ...
    def clear_sample_step(self) -> None: ...
    def copy(self) -> PingSampleSelector: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> PingSampleSelector: 
        """
        create T_CLASS object from bytearray
        """
    def get_beam_step(self) -> int: 
        """
        < step size for beam numbers (negative numbers reverse beam order)
        """
    def get_max_beam_angle(self) -> typing.Optional[float]: 
        """
        < max beam angle to select (°)
        """
    def get_max_beam_number(self) -> typing.Optional[int]: 
        """
        < max beam number to select (negative numbers count from end)
        """
    def get_max_sample_number(self) -> typing.Optional[int]: 
        """
        < max sample number to select (negative numbers count from end)
        """
    def get_max_sample_range(self) -> typing.Optional[float]: 
        """
        < max sample range to select (m)
        """
    def get_min_beam_angle(self) -> typing.Optional[float]: 
        """
        < min beam angle to select (°)
        """
    def get_min_beam_number(self) -> typing.Optional[int]: 
        """
        < min beam number to select (negative numbers count from end)
        """
    def get_min_sample_number(self) -> typing.Optional[int]: 
        """
        < min sample number to select (negative numbers count from end)
        """
    def get_min_sample_range(self) -> typing.Optional[float]: 
        """
        < min sample range to select (m)
        """
    def get_sample_step(self) -> int: 
        """
        < step size for sample numbers (negative numbers reverse sample order)
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def select_beam_range_by_angles(self, min_beam_angle: float, max_beam_angle: float, beam_step: typing.Optional[int] = None) -> None: ...
    def select_beam_range_by_numbers(self, min_beam_number: int, max_beam_number: int, beam_step: typing.Optional[int] = None) -> None: ...
    def select_sample_range_by_numbers(self, min_sample_number: int, max_sample_number: int, sample_step: typing.Optional[int] = None) -> None: ...
    def select_sample_range_by_ranges(self, min_sample_range: float, max_sample_range: float, sample_step: typing.Optional[int] = None) -> None: ...
    def set_beam_step(self, beam_step: int) -> None: ...
    def set_sample_step(self, sample_step: int) -> None: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
