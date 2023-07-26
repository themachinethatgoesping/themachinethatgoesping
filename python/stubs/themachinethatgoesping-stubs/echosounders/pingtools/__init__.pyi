"""Tools for working with ping objects."""
from __future__ import annotations
import themachinethatgoesping.echosounders.pingtools
import typing
import themachinethatgoesping.echosounders.filetemplates

__all__ = [
    "BeamSampleSelection",
    "PingSampleSelection",
    "PingSampleSelector"
]


class BeamSampleSelection():
    """
    A struct to hold the selected beams/sample range for a single
    transducer
    """
    def __copy__(self) -> BeamSampleSelection: ...
    def __deepcopy__(self, arg0: dict) -> BeamSampleSelection: ...
    def __eq__(self, other: BeamSampleSelection) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self) -> None: 
        """
        A struct to hold the selected beams/sample range for a single
        transducer
        """
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> BeamSampleSelection: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BeamSampleSelection: 
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
    @property
    def beam_numbers(self) -> typing.List[int]:
        """
        < selected beam numbers

        :type: typing.List[int]
        """
    @beam_numbers.setter
    def beam_numbers(self, arg0: typing.List[int]) -> None:
        """
        < selected beam numbers
        """
    @property
    def first_sample_number_per_beam(self) -> typing.List[int]:
        """
        < first sample number per beam

        :type: typing.List[int]
        """
    @first_sample_number_per_beam.setter
    def first_sample_number_per_beam(self, arg0: typing.List[int]) -> None:
        """
        < first sample number per beam
        """
    @property
    def max_number_of_samples_per_beam(self) -> typing.List[int]:
        """
        < max number of samples per beam

        :type: typing.List[int]
        """
    @max_number_of_samples_per_beam.setter
    def max_number_of_samples_per_beam(self, arg0: typing.List[int]) -> None:
        """
        < max number of samples per beam
        """
    @property
    def sample_step_ensemble(self) -> int:
        """
        < sample step size (same for the entire ensemble)

        :type: int
        """
    @sample_step_ensemble.setter
    def sample_step_ensemble(self, arg0: int) -> None:
        """
        < sample step size (same for the entire ensemble)
        """
    pass
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
    def get_sample_selections(self) -> typing.Dict[str, BeamSampleSelection]: 
        """
        Return the sample selections for each transducer

        Returns:
            dict of sample selections
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
    def transducer_ids(self) -> typing.Set[str]: 
        """
        Return the names of the transducers

        Returns:
            std::set<std::string>
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
    def apply_selection(self, ping: themachinethatgoesping.echosounders.filetemplates.I_Ping) -> typing.Set[str]: ...
    def clear(self) -> None: ...
    def clear_beam_angle_range(self) -> None: ...
    def clear_beam_number_range(self) -> None: ...
    def clear_beam_step(self) -> None: ...
    def clear_ignored_transducer_ids(self) -> None: ...
    def clear_sample_number_range(self) -> None: ...
    def clear_sample_range_range(self) -> None: ...
    def clear_sample_step(self) -> None: ...
    def clear_transducer_ids(self) -> None: ...
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
    def get_ignored_transducer_ids(self) -> typing.Optional[typing.Set[str]]: ...
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
    def get_transducer_ids(self) -> typing.Optional[typing.Set[str]]: ...
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
    def select_ignored_transducer_ids(self, ignored_transducer_ids: typing.Set[str]) -> None: ...
    def select_sample_range_by_numbers(self, min_sample_number: int, max_sample_number: int, sample_step: typing.Optional[int] = None) -> None: ...
    def select_sample_range_by_ranges(self, min_sample_range: float, max_sample_range: float, sample_step: typing.Optional[int] = None) -> None: ...
    def select_transducer_ids(self, transducer_ids: typing.Set[str]) -> None: ...
    def set_beam_step(self, beam_step: int) -> None: ...
    def set_sample_step(self, sample_step: int) -> None: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
