"""
Tools for working with ping objects.
"""
from __future__ import annotations
import themachinethatgoesping.echosounders.filetemplates
import typing
__all__ = ['BeamSampleSelection', 'BeamSelection', 'PingSampleSelector', 'ReadSampleRange']
class BeamSampleSelection(BeamSelection):
    """
    A class to hold the selected beams/sample range for a single
    transducer
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> BeamSampleSelection:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> BeamSampleSelection:
        ...
    def __deepcopy__(self, arg0: dict) -> BeamSampleSelection:
        ...
    def __eq__(self, other: BeamSampleSelection) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, sample_step_ensemble: int = ...) -> None:
        ...
    @typing.overload
    def __init__(self, first_sample_number_per_beam: list[int], last_sample_number_per_beam: list[int], sample_step_ensemble: int = ...) -> None:
        """
        Construct a new Beam Sample Selection object
        
        Parameter ``beam_selection``:
        """
    @typing.overload
    def __init__(self, beam_selection: BeamSelection) -> None:
        """
        Initialize a beam sample selection from a whole swath
        
        Parameter ``beam_nr``:
            beam number
        
        Parameter ``first_sample_number``:
            first sample number to select
        
        Parameter ``last_sample_number_per_beam``:
            last sample number to select
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
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
    def get_first_sample_number_ensemble(self) -> int:
        """
        Return the first sample number of the ensemble
        
        Returns:
            uint16_t
        """
    def get_first_sample_number_per_beam(self) -> list[int]:
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
    def get_last_sample_number_per_beam(self) -> list[int]:
        """
        Return the max number of samples per beam
        
        Returns:
            std::vector<uint16_t>
        """
    def get_number_of_samples_ensemble(self) -> int:
        """
        return the number of samples within the ensemble
        
        Returns:
            uint16_t
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
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def set_first_sample_number_ensemble(self, first_sample_number_ensemble: int) -> None:
        ...
    def set_last_sample_number_ensemble(self, last_sample_number_ensemble: int) -> None:
        ...
    def set_sample_step_ensemble(self, sample_step_ensemble: int) -> None:
        ...
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class BeamSelection:
    """
    A class to hold the selected beams/sample range for a single
    transducer
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> BeamSelection:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> BeamSelection:
        ...
    def __deepcopy__(self, arg0: dict) -> BeamSelection:
        ...
    def __eq__(self, other: BeamSelection) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, number_of_beams: int) -> None:
        """
        Initialize a beam sample selection from a whole swath
        
        Parameter ``number_of_beams``:
            number of beams in the swath
        """
    @typing.overload
    def __init__(self, beam_numbers: list[int]) -> None:
        """
        Initialize a beam sample selection from a whole swath
        
        Parameter ``number_of_beams``:
            number of beams in the swath
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def add_beam(self, beam_number: int) -> None:
        """
        Add a beam to the selection
        
        Parameter ``beam_nr``:
            beam number
        
        Parameter ``first_sample_number``:
            first sample number to select
        
        Parameter ``last_sample_number_per_beam``:
            last sample number to select
        """
    def copy(self) -> BeamSelection:
        """
        return a copy using the c++ default copy constructor
        """
    def get_beam_numbers(self) -> list[int]:
        """
        Return the beam numbers
        
        Returns:
            std::vector<uint16_t>
        """
    def get_number_of_beams(self) -> int:
        """
        Return the number of beams
        
        Returns:
            size_t
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class PingSampleSelector:
    """
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> PingSampleSelector:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> PingSampleSelector:
        ...
    def __deepcopy__(self, arg0: dict) -> PingSampleSelector:
        ...
    def __eq__(self, other: PingSampleSelector) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def apply_selection(self, ping: themachinethatgoesping.echosounders.filetemplates.I_Ping) -> BeamSampleSelection:
        ...
    def clear(self) -> None:
        ...
    def clear_beam_angle_range(self) -> None:
        ...
    def clear_beam_number_range(self) -> None:
        ...
    def clear_beam_step(self) -> None:
        ...
    def clear_sample_number_range(self) -> None:
        ...
    def clear_sample_range_range(self) -> None:
        ...
    def clear_sample_step(self) -> None:
        ...
    def copy(self) -> PingSampleSelector:
        """
        return a copy using the c++ default copy constructor
        """
    def get_beam_step(self) -> int:
        """
        < step size for beam numbers
        """
    def get_max_beam_angle(self) -> float | None:
        """
        < max beam angle to select (°)
        """
    def get_max_beam_number(self) -> int | None:
        """
        < max beam number to select
        """
    def get_max_sample_number(self) -> int | None:
        """
        < max sample number to select
        """
    def get_max_sample_range(self) -> float | None:
        """
        < max sample range to select (m)
        """
    def get_min_beam_angle(self) -> float | None:
        """
        < min beam angle to select (°)
        """
    def get_min_beam_number(self) -> int | None:
        """
        < min beam number to select
        """
    def get_min_sample_number(self) -> int | None:
        """
        < min sample number to select
        """
    def get_min_sample_range(self) -> float | None:
        """
        < min sample range to select (m)
        """
    def get_sample_step(self) -> int:
        """
        < step size for sample numbers
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def select_beam_range_by_angles(self, min_beam_angle: float, max_beam_angle: float, beam_step: int | None = ...) -> None:
        ...
    def select_beam_range_by_numbers(self, min_beam_number: int, max_beam_number: int, beam_step: int | None = ...) -> None:
        ...
    def select_sample_range_by_numbers(self, min_sample_number: int, max_sample_number: int, sample_step: int | None = ...) -> None:
        ...
    def select_sample_range_by_ranges(self, min_sample_range: float, max_sample_range: float, sample_step: int | None = ...) -> None:
        ...
    def set_beam_step(self, beam_step: int) -> None:
        ...
    def set_sample_step(self, sample_step: int) -> None:
        ...
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class ReadSampleRange:
    """
    A class to hold range of samples for a single beam
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> ReadSampleRange:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> ReadSampleRange:
        ...
    def __deepcopy__(self, arg0: dict) -> ReadSampleRange:
        ...
    def __eq__(self, other: ReadSampleRange) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, first_sample_to_read: int, number_of_samples_to_read: int, first_read_sample_offset: int, last_read_sample_offset: int) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> ReadSampleRange:
        """
        return a copy using the c++ default copy constructor
        """
    def get_first_read_sample_offset(self) -> int:
        ...
    def get_first_sample_to_read(self) -> int:
        """
        Return the first sample number to read (local to beam sample offset)
        
        Returns:
            uint16_t
        """
    def get_last_read_sample_offset(self) -> int:
        ...
    def get_number_of_samples_to_read(self) -> int:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
