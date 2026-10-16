"""Ping-aware tools (e.g. PingSampleSelector)."""

from collections.abc import Sequence
from typing import overload

import themachinethatgoesping.algorithms_nanopy.pingtools
import themachinethatgoesping.pingprocessing_nanopy.datatypes


class PingSampleSelector:
    def __init__(self) -> None: ...

    @overload
    def apply_selection(self, ping_watercolumn: themachinethatgoesping.pingprocessing_nanopy.datatypes.I_PingWatercolumn) -> themachinethatgoesping.algorithms_nanopy.pingtools.BeamSampleSelection: ...

    @overload
    def apply_selection(self, ping_bottom: themachinethatgoesping.pingprocessing_nanopy.datatypes.I_PingBottom) -> themachinethatgoesping.algorithms_nanopy.pingtools.BeamSelection: ...

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

    def get_min_minslant_range_percent(self) -> float | None:
        """min samples after minslant to consider (%)"""

    def get_max_minslant_range_percent(self) -> float | None:
        """max samples before minslant to consider (%)"""

    def get_min_bottom_range_percent(self) -> float | None:
        """max samples before bottom detection to consider (%)"""

    def get_max_bottom_range_percent(self) -> float | None:
        """max samples before bottom detection to consider (%)"""

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

    def set_sample_step(self, sample_step: int) -> None:
        """step size for sample numbers"""

    def set_beam_step(self, beam_step: int) -> None:
        """step size for beam numbers"""

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
