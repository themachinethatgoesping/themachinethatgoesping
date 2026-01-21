from collections.abc import Sequence
from typing import overload

import themachinethatgoesping.echosounders_nanopy.filetemplates


class ReadSampleRange:
    """A class to hold range of samples for a single beam"""

    def __init__(self, first_sample_to_read: int, number_of_samples_to_read: int, first_read_sample_offset: int, last_read_sample_offset: int) -> None: ...

    def get_first_sample_to_read(self) -> int:
        """
        Return the first sample number to read (local to beam sample offset)

        Returns:
            uint32_t
        """

    def get_number_of_samples_to_read(self) -> int: ...

    def get_first_read_sample_offset(self) -> int: ...

    def get_last_read_sample_offset(self) -> int: ...

    def __eq__(self, other: ReadSampleRange) -> bool: ...

    def copy(self) -> ReadSampleRange:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ReadSampleRange: ...

    def __deepcopy__(self, arg: dict, /) -> ReadSampleRange: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ReadSampleRange:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class BeamSelection:
    """
    A class to hold the selected beams/sample range for a single
    transducer
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, beam_sample_selection: BeamSampleSelection) -> None: ...

    @overload
    def __init__(self, number_of_beams: int) -> None:
        """
        Initialize a beam sample selection from a whole swath

        Args:
            number_of_beams: number of beams in the swath
        """

    @overload
    def __init__(self, beam_numbers: Sequence[int]) -> None:
        """
        Initialize a beam sample selection from a whole swath

        Args:
            number_of_beams: number of beams in the swath
        """

    def add_beam(self, beam_number: int) -> None:
        """
        Add a beam to the selection

        Args:
            beam_nr: beam number
            first_sample_number: first sample number to select
            last_sample_number_per_beam: last sample number to select
        """

    def get_number_of_beams(self) -> int:
        """
        Return the number of beams

        Returns:
            size_t
        """

    def empty(self) -> bool:
        """
        return if the selection contains beams

        Returns:
            true false
        """

    def get_beam_numbers(self) -> list[int]:
        """
        Return the beam numbers

        Returns:
            std::vector_uint32_t
        """

    def __eq__(self, other: BeamSelection) -> bool: ...

    def copy(self) -> BeamSelection:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BeamSelection: ...

    def __deepcopy__(self, arg: dict, /) -> BeamSelection: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BeamSelection:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class BeamSampleSelection(BeamSelection):
    """
    A class to hold the selected beams/sample range for a single
    transducer
    """

    @overload
    def __init__(self, sample_step_ensemble: int = 1) -> None: ...

    @overload
    def __init__(self, first_sample_number_per_beam: Sequence[int], last_sample_number_per_beam: Sequence[int], sample_step_ensemble: int = 1) -> None:
        """
        Construct a new Beam Sample Selection object

        Args:
            beam_selection:
        """

    @overload
    def __init__(self, beam_selection: BeamSelection) -> None:
        """
        Initialize a beam sample selection from a whole swath

        Args:
            first_sample_number_per_beam: first sample number per beam
            last_sample_number_per_beam: last sample number per beam
            sample_step_ensemble: sample step size (same for the entire
                                  ensemble)
        """

    def get_read_sample_range(self, beam_index: int, first_sample_offset_in_beam: int, number_of_samples_in_beam: int) -> ReadSampleRange:
        """
        Return the read sample range for a given beam

        Args:
            beam_index: index of the beam within the beam sample selection
            first_sample_offset: offset to the first sample (often 0)
            number_of_samples: number of samples in the real beam structure

        Returns:
            ReadSampleRange read sample range
        """

    def get_sample_numbers_ensemble_1d(self) -> "xt::xtensor_container_xt_uvector<unsignedint_xsimd_aligned_allocator<unsignedint_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>": ...

    def get_sample_numbers_ensemble_2d(self) -> "xt::xtensor_container_xt_uvector<unsignedint_xsimd_aligned_allocator<unsignedint_16ul >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>": ...

    def empty(self) -> bool:
        """
        return if the selection contains beams and samples

        Returns:
            true false
        """

    def add_beam(self, beam_number: int, first_sample_number: int, max_number_of_samples: int) -> None:
        """
        Add a beam to the selection

        Args:
            beam_nr: beam number
            first_sample_number: first sample number to select
            last_sample_number: last sample number to select
        """

    def set_sample_step_ensemble(self, sample_step_ensemble: int) -> None: ...

    def set_first_sample_number_ensemble(self, first_sample_number_ensemble: int) -> None: ...

    def set_last_sample_number_ensemble(self, last_sample_number_ensemble: int) -> None: ...

    def get_sample_step_ensemble(self) -> int:
        """
        Return the sample step size

        Returns:
            uint32_t
        """

    def get_first_sample_number_ensemble(self) -> int:
        """
        Return the first sample number of the ensemble

        Returns:
            uint32_t
        """

    def get_last_sample_number_ensemble(self) -> int:
        """
        Return the last sample number of the ensemble

        Returns:
            uint32_t
        """

    def get_number_of_samples_ensemble(self) -> int:
        """
        return the number of samples within the ensemble

        Returns:
            uint32_t
        """

    def get_first_sample_number_per_beam(self) -> list[int]:
        """
        Return the first sample number per beam

        Returns:
            std::vector_uint32_t
        """

    def get_last_sample_number_per_beam(self) -> list[int]:
        """
        Return the max number of samples per beam

        Returns:
            std::vector_uint32_t
        """

    def __eq__(self, other: BeamSampleSelection) -> bool: ...

    def copy(self) -> BeamSampleSelection:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BeamSampleSelection: ...

    def __deepcopy__(self, arg: dict, /) -> BeamSampleSelection: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BeamSampleSelection:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class PingSampleSelector:
    def __init__(self) -> None: ...

    @overload
    def apply_selection(self, ping_watercolumn: themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn) -> BeamSampleSelection: ...

    @overload
    def apply_selection(self, ping_bottom: themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom) -> BeamSelection: ...

    def get_min_beam_number(self) -> int | None:
        """min beam number to select"""

    def get_max_beam_number(self) -> int | None:
        """max beam number to select"""

    def get_min_sample_number(self) -> int | None:
        """min sample number to select"""

    def get_max_sample_number(self) -> int | None:
        """max sample number to select"""

    def get_min_beam_angle(self) -> float | None:
        """min beam angle to select (°)"""

    def get_max_beam_angle(self) -> float | None:
        """max beam angle to select (°)"""

    def get_min_sample_range(self) -> float | None:
        """min sample range to select (m)"""

    def get_max_sample_range(self) -> float | None:
        """max sample range to select (m)"""

    def get_transmit_sectors(self) -> list[int] | None:
        """transmit_sectors to select"""

    def get_transmit_sector_min_beam_angle(self) -> float | None:
        """select transmit sectors with angles >= _transmit_sector_min_beam_angle"""

    def get_transmit_sector_max_beam_angle(self) -> float | None:
        """select transmit sectors with angles <= _transmit_sector_max_beam_angle"""

    def get_beam_step(self) -> int:
        """step size for beam numbers"""

    def get_sample_step(self) -> int:
        """step size for sample numbers"""

    def get_min_minslant_range_percent(self) -> float | None: ...

    def get_max_minslant_range_percent(self) -> float | None: ...

    def get_min_bottom_range_percent(self) -> float | None: ...

    def get_max_bottom_range_percent(self) -> float | None: ...

    def clear_beam_number_range(self) -> None: ...

    def clear_sample_number_range(self) -> None: ...

    def clear_beam_angle_range(self) -> None: ...

    def clear_sample_range_range(self) -> None: ...

    def clear_transmit_sectors(self) -> None: ...

    def clear_transmit_sector_beam_angle_range(self) -> None: ...

    def clear_beam_step(self) -> None: ...

    def clear_sample_step(self) -> None: ...

    def clear_minslant_range(self) -> None: ...

    def clear_bottom_range(self) -> None: ...

    def clear(self) -> None: ...

    def select_beam_range_by_numbers(self, min_beam_number: int | None = None, max_beam_number: int | None = None, beam_step: int | None = None) -> None: ...

    def select_sample_range_by_numbers(self, min_sample_number: int | None = None, max_sample_number: int | None = None, sample_step: int | None = None) -> None: ...

    def select_beam_range_by_angles(self, min_beam_angle: float | None = None, max_beam_angle: float | None = None, beam_step: int | None = None) -> None: ...

    def select_sample_range_by_ranges(self, min_sample_range: float | None = None, max_sample_range: float | None = None, sample_step: int | None = None) -> None: ...

    def select_transmit_sectors(self, transmit_sectors: Sequence[int] | None = None) -> None: ...

    def select_transmit_sectors_by_beam_angles(self, transmit_sector_min_beam_angle: float | None = None, transmit_sector_max_beam_angle: float | None = None) -> None: ...

    def select_min_minslant_range_percent(self, min_minslant_range_percent: float | None = None) -> None: ...

    def select_max_minslant_range_percent(self, max_minslant_range_percent: float | None = None) -> None: ...

    def select_minslant_range_percent(self, min_minslant_range_percent: float | None = None, max_minslant_range_percent: float | None = None) -> None: ...

    def select_min_bottom_range_percent(self, min_bottom_range_percent: float | None = None) -> None: ...

    def select_max_bottom_range_percent(self, max_bottom_range_percent: float | None = None) -> None: ...

    def select_bottom_range_percent(self, min_bottom_range_percent: float | None = None, max_bottom_range_percent: float | None = None) -> None: ...

    def set_sample_step(self, sample_step: int) -> None: ...

    def set_beam_step(self, beam_step: int) -> None: ...

    def __eq__(self, arg: PingSampleSelector, /) -> bool: ...

    def copy(self) -> PingSampleSelector:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> PingSampleSelector: ...

    def __deepcopy__(self, arg: dict, /) -> PingSampleSelector: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> PingSampleSelector:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
