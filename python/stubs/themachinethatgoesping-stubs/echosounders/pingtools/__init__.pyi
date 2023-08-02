"""Tools for working with ping objects."""
from __future__ import annotations
import themachinethatgoesping.echosounders.pingtools
import typing
import themachinethatgoesping.echosounders.filetemplates

__all__ = [
    "BeamSampleSelection",
    "PingSampleSelection",
    "PingSampleSelector",
    "ReadSampleRange"
]


class BeamSampleSelection():
    """
    A class to hold the selected beams/sample range for a single
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
    @typing.overload
    def __init__(self, sample_step_ensemble: int = 1) -> None: 
        """
        Initialize a beam sample selection from a whole swath

        Parameter ``beam_nr``:
            beam number

        Parameter ``first_sample_number``:
            first sample number to select

        Parameter ``last_sample_number_per_beam``:
            last sample number to select
        """
    @typing.overload
    def __init__(self, first_sample_number_per_beam: typing.List[int], last_sample_number_per_beam: typing.List[int], sample_step_ensemble: int = 1) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def add_beam(self, beam_number: int, first_sample_number: int, max_number_of_samples: int) -> None: 
        """
        Add a beam to the selection

        Parameter ``beam_nr``:
            beam number

        Parameter ``first_sample_number``:
            first sample number to select

        Parameter ``last_sample_number_per_beam``:
            last sample number to select
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
    def get_beam_numbers(self) -> typing.List[int]: 
        """
        Return the beam numbers

        Returns:
            std::vector<uint16_t>
        """
    def get_first_sample_number_ensemble(self) -> int: 
        """
        Return the first sample number of the ensemble

        Returns:
            uint16_t
        """
    def get_first_sample_number_per_beam(self) -> typing.List[int]: 
        """
        Return the first sample number per beam

        Returns:
            std::vector<uint16_t>
        """
    def get_last_sample_number_ensemble(self) -> int: 
        """
        Return the last sample number of the ensemble

        Returns:
            uint16_t
        """
    def get_last_sample_number_per_beam(self) -> typing.List[int]: 
        """
        Return the max number of samples per beam

        Returns:
            std::vector<uint16_t>
        """
    def get_number_of_beams(self) -> int: 
        """
        Return the number of beams

        Returns:
            size_t
        """
    def get_read_sample_range(self, beam_index: int, first_sample_offset_in_beam: int, number_of_samples_in_beam: int) -> ReadSampleRange: 
        """
        Return the read sample range for a given beam

        Parameter ``beam_index``:
            index of the beam within the beam sample selection

        Parameter ``first_sample_offset``:
            offset to the first sample (often 0)

        Parameter ``number_of_samples``:
            number of samples in the real beam structure

        Returns:
            ReadSampleRange read sample range
        """
    def get_sample_step_ensemble(self) -> int: 
        """
        Return the sample step size

        Returns:
            uint16_t
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_first_sample_number_ensemble(self, first_sample_number_ensemble: int) -> None: ...
    def set_last_sample_number_ensemble(self, last_sample_number_ensemble: int) -> None: ...
    def set_sample_step_ensemble(self, sample_step_ensemble: int) -> None: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
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
    def add_beam(self, transducer_id: str, beam_nr: int, first_sample_number: int = 0, max_number_of_samples: int = 65535) -> None: 
        """
        Add a beam to the sample selection

        Parameter ``transducer_id``:
            transducer id of the beam

        Parameter ``beam_nr``:
            beam numer

        Parameter ``first_sample_number``:
            first sample to select (>0)

        Parameter ``last_sample_number``:
            last sample to select (>0)
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
    def get_first_sample_number_ensemble(self) -> int: 
        """
        Return the first sample number in the sample selection

        Returns:
            size_t
        """
    def get_last_sample_number_ensemble(self) -> int: 
        """
        Return the last sample number in the sample selection

        Returns:
            size_t
        """
    def get_number_of_beams(self) -> int: 
        """
        Return the number of beams in the sample selection

        Returns:
            size_t
        """
    def get_number_of_samples_ensemble(self) -> int: 
        """
        Return the number of samples in the sample selection

        Returns:
            size_t
        """
    def get_sample_selections(self) -> typing.Dict[str, BeamSampleSelection]: 
        """
        Return the sample selections for each transducer

        Returns:
            dict of sample selections
        """
    def get_sample_step_ensemble(self) -> int: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_first_sample_number_ensemble(self, set_first_sample_number_ensemble: int) -> None: 
        """
        Set the first sample number for the selection

        Parameter ``first_sample_number_ensemble``:
            First sample number in the selection

        Set the first sample number for the selection

        Parameter ``first_sample_number_ensemble``:
            First sample number in the selection
        """
    def set_last_sample_number_ensemble(self, set_last_sample_number_ensemble: int) -> None: 
        """
        Set the last sample number for the selection

        Parameter ``last_sample_number_ensemble``:
            Last sample number in the selection

        Set the last sample number for the selection

        Parameter ``last_sample_number_ensemble``:
            Last sample number in the selection
        """
    def set_sample_step_ensemble(self, sample_step_ensemble: int) -> None: ...
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
    def apply_selection(self, ping: themachinethatgoesping.echosounders.filetemplates.I_Ping) -> PingSampleSelection: ...
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
        < max beam number to select
        """
    def get_max_sample_number(self) -> typing.Optional[int]: 
        """
        < max sample number to select
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
        < min beam number to select
        """
    def get_min_sample_number(self) -> typing.Optional[int]: 
        """
        < min sample number to select
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
class ReadSampleRange():
    """
    A class to hold range of samples for a single beam
    """
    def __copy__(self) -> ReadSampleRange: ...
    def __deepcopy__(self, arg0: dict) -> ReadSampleRange: ...
    def __eq__(self, other: ReadSampleRange) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    def __init__(self, first_sample_to_read: int, number_of_samples_to_read: int, first_read_sample_offset: int, last_read_sample_offset: int) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> ReadSampleRange: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ReadSampleRange: 
        """
        create T_CLASS object from bytearray
        """
    def get_first_read_sample_offset(self) -> int: ...
    def get_first_sample_to_read(self) -> int: 
        """
        Return the first sample number to read (local to beam sample offset)

        Returns:
            uint16_t
        """
    def get_last_read_sample_offset(self) -> int: ...
    def get_number_of_samples_to_read(self) -> int: ...
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
