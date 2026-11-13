"""Teledyne RESON .s7k (7k) file data types"""
import typing

from collections.abc import Sequence
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

import themachinethatgoesping.algorithms_nanopy.pingtools
import themachinethatgoesping.echosounders_nanopy.s7k
import themachinethatgoesping.echosounders_nanopy.s7k.filedatainterfaces
import themachinethatgoesping.pingprocessing_nanopy.datatypes


class S7KWaterColumnCalibration(themachinethatgoesping.pingprocessing_nanopy.datatypes.WaterColumnCalibration):
    """
    Water column calibration for Teledyne RESON 7k (and Norbit) systems.

    This is a first, uncalibrated setup. The power/ap/av calibrations
    carry the per-ping system gain offset (transmit source level "power
    selection" + receiver "gain selection") and, for av, the volume-
    scattering conversion factor derived from the effective pulse duration
    and sound velocity. For CW the effective pulse duration is the nominal
    transmit pulse width; for a linear chirp (FM) it is the matched-filter
    compressed duration (~ 1 / bandwidth), because the water column is the
    compressed envelope. av is therefore an uncalibrated Sv (a first guess
    of Sv); the remaining fixed calibration constant (equivalent beam
    angle, beam pattern, electronics offset) still has to be added via a
    dedicated calibration before the result may be called a true Sv.
    """

    def __init__(self, sound_velocity: float, effective_pulse_duration: float, system_gain_offset: float, tvg_absorption_db_m: float, tvg_factor: float, is_fm: bool = False) -> None: ...

    def modify_s7k_calibrations(self, sound_velocity: float | None = None, effective_pulse_duration: float | None = None, system_gain_offset: float | None = None, tvg_absorption_db_m: float | None = None, tvg_factor: float | None = None, is_fm: bool | None = None) -> None:
        """
        Modify individual calibration parameters and recompute the power/ap/av
        calibrations.

        Only the supplied (non-nullopt) parameters are changed; the rest keep
        their current value. This mirrors the kmall modify_* updater and is
        the supported way to tweak the (immutable) base calibrations.
        """

    def get_sound_velocity(self) -> float: ...

    def get_effective_pulse_duration(self) -> float: ...

    def get_system_gain_offset(self) -> float: ...

    def is_fm(self) -> bool:
        """whether the transmit pulse is a linear chirp (FM) rather than CW"""

    def initialized(self) -> bool: ...

    def check_initialized(self) -> None: ...

    def pre_hashed(self) -> S7KMultiSectorWaterColumnCalibration_flyweight:
        """
        Return this class as a flyweight with computed hash. This is faster when updating the ping calibration.
        """

    def __eq__(self, other: S7KWaterColumnCalibration) -> bool: ...

    def copy(self) -> S7KWaterColumnCalibration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KWaterColumnCalibration: ...

    def __deepcopy__(self, arg: dict, /) -> S7KWaterColumnCalibration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> S7KWaterColumnCalibration:
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

class S7KMultiSectorWaterColumnCalibration_flyweight:
    """Flyweight wrapper around the MultiSectorCalibration class."""

    def __init__(self, other: S7KMultiSectorWaterColumnCalibration) -> None:
        """Create a flyweight from a MultiSectorCalibration object."""

    def get(self) -> S7KMultiSectorWaterColumnCalibration:
        """Get the underlying T_MultiSectorCalibration object."""

class S7KMultiSectorWaterColumnCalibration:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, calibration_per_sector: Sequence[S7KWaterColumnCalibration]) -> None: ...

    @overload
    def __init__(self, other: S7KMultiSectorWaterColumnCalibration) -> None: ...

    def has_power_calibration(self) -> bool: ...

    def has_ap_calibration(self) -> bool: ...

    def has_av_calibration(self) -> bool: ...

    def has_sp_calibration(self) -> bool: ...

    def has_sv_calibration(self) -> bool: ...

    def has_valid_absorption_db_m(self) -> bool: ...

    def get_number_of_sectors(self) -> int: ...

    def __len__(self) -> int: ...

    def get_calibrations(self) -> list[S7KWaterColumnCalibration]: ...

    def pre_hashed(self) -> S7KMultiSectorWaterColumnCalibration_flyweight:
        """
        Return this class as a flyweight with computed hash. This faster when updating the ping calibration.
        """

    def __eq__(self, other: S7KMultiSectorWaterColumnCalibration) -> bool: ...

    def copy(self) -> S7KMultiSectorWaterColumnCalibration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KMultiSectorWaterColumnCalibration: ...

    def __deepcopy__(self, arg: dict, /) -> S7KMultiSectorWaterColumnCalibration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> S7KMultiSectorWaterColumnCalibration:
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

    @overload
    def apply_beam_sample_correction_power(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_power(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pp(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pp(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pv(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pv(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_ap(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_ap(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sp(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sp(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sv(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sv(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def inplace_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None: ...

    @overload
    def inplace_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None: ...

    @overload
    def apply_beam_sample_correction_pp_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pp_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]:
        """Apply pp calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_pv_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pv_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]:
        """Apply pv calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_ap_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_ap_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]:
        """Apply ap calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]:
        """Apply av calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_sp_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sp_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]:
        """Apply sp calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_sv_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sv_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]:
        """Apply sv calibration with per-beam absorption coefficients."""

    @overload
    def inplace_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None: ...

    @overload
    def inplace_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None:
        """Inplace apply av calibration with per-beam absorption coefficients."""

class S7KPingFileData_stream(themachinethatgoesping.pingprocessing_nanopy.datatypes.I_PingFileData):
    """
    Raw file data of a single s7k ping. Holds the datagram index of the
    ping (via the S7KDatagramInterface base) and provides raw access to
    the ping's datagrams.

    Template Args:
        t_ifstream: 

    Note:
        The datagram-processing functions are not implemented yet. This
        class currently only provides the structure so it can be filled in
        in a later step.
    """

    def init_watercolumn_calibration(self, force: bool = False) -> None: ...

    def has_watercolumn_calibration(self) -> bool: ...

    @overload
    def set_watercolumn_calibration(self, calibration: S7KWaterColumnCalibration) -> None: ...

    @overload
    def set_watercolumn_calibration(self, calibrations: Sequence[S7KWaterColumnCalibration]) -> None: ...

    @overload
    def get_watercolumn_calibration(self, tx_sector: int) -> S7KWaterColumnCalibration: ...

    @overload
    def get_watercolumn_calibration(self) -> S7KWaterColumnCalibration: ...

    def get_multisector_calibration(self) -> S7KMultiSectorWaterColumnCalibration: ...

    def set_multisector_calibration(self, calibration: S7KMultiSectorWaterColumnCalibration) -> None: ...

    def update_calibration(self, calibration: S7KMultiSectorWaterColumnCalibration_flyweight) -> None: ...

    def copy(self) -> S7KPingFileData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingFileData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingFileData_stream: ...

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str: ...

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None: ...

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.filedatainterfaces.S7KDatagramInterface_stream]: ...

class S7KPingFileData(themachinethatgoesping.pingprocessing_nanopy.datatypes.I_PingFileData):
    """
    Raw file data of a single s7k ping. Holds the datagram index of the
    ping (via the S7KDatagramInterface base) and provides raw access to
    the ping's datagrams.

    Template Args:
        t_ifstream: 

    Note:
        The datagram-processing functions are not implemented yet. This
        class currently only provides the structure so it can be filled in
        in a later step.
    """

    def init_watercolumn_calibration(self, force: bool = False) -> None: ...

    def has_watercolumn_calibration(self) -> bool: ...

    @overload
    def set_watercolumn_calibration(self, calibration: S7KWaterColumnCalibration) -> None: ...

    @overload
    def set_watercolumn_calibration(self, calibrations: Sequence[S7KWaterColumnCalibration]) -> None: ...

    @overload
    def get_watercolumn_calibration(self, tx_sector: int) -> S7KWaterColumnCalibration: ...

    @overload
    def get_watercolumn_calibration(self) -> S7KWaterColumnCalibration: ...

    def get_multisector_calibration(self) -> S7KMultiSectorWaterColumnCalibration: ...

    def set_multisector_calibration(self, calibration: S7KMultiSectorWaterColumnCalibration) -> None: ...

    def update_calibration(self, calibration: S7KMultiSectorWaterColumnCalibration_flyweight) -> None: ...

    def copy(self) -> S7KPingFileData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingFileData: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingFileData: ...

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str: ...

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None: ...

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.filedatainterfaces.S7KDatagramInterface]: ...

class S7KPingCommon_stream:
    """
    Common base for the s7k ping (and its bottom / watercolumn sub-
    objects). Holds the shared S7KPingFileData (the raw file data /
    datagram index of the ping).

    Template Args:
        t_ifstream:
    """

    @property
    def file_data(self) -> S7KPingFileData_stream: ...

    def copy(self) -> S7KPingCommon_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingCommon_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingCommon_stream: ...

class S7KPingCommon:
    """
    Common base for the s7k ping (and its bottom / watercolumn sub-
    objects). Holds the shared S7KPingFileData (the raw file data /
    datagram index of the ping).

    Template Args:
        t_ifstream:
    """

    @property
    def file_data(self) -> S7KPingFileData: ...

    def copy(self) -> S7KPingCommon:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingCommon: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingCommon: ...

class S7KPingBottom_stream(themachinethatgoesping.pingprocessing_nanopy.datatypes.I_PingBottom):
    """
    Bottom detection (bathymetry) accessor of an s7k ping.

    The bottom detections come from the 7027 RawDetection record. s7k raw
    detections do not carry a ready-made XYZ position (has_xyz() is
    false); the per-beam receive angles and two-way travel times are
    provided as best guesses so the bottom can be raytraced later.

    Template Args:
        t_ifstream:
    """

    def copy(self) -> S7KPingBottom_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingBottom_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingBottom_stream: ...

class S7KPingBottom(themachinethatgoesping.pingprocessing_nanopy.datatypes.I_PingBottom):
    """
    Bottom detection (bathymetry) accessor of an s7k ping.

    The bottom detections come from the 7027 RawDetection record. s7k raw
    detections do not carry a ready-made XYZ position (has_xyz() is
    false); the per-beam receive angles and two-way travel times are
    provided as best guesses so the bottom can be raytraced later.

    Template Args:
        t_ifstream:
    """

    def copy(self) -> S7KPingBottom:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingBottom: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingBottom: ...

class S7KPingWatercolumn_stream(themachinethatgoesping.pingprocessing_nanopy.datatypes.I_PingWatercolumn):
    """
    Water column accessor of an s7k ping.

    The water-column amplitudes come from the 7042 CompressedWaterColumn
    record; the per-beam receive angles and the detected bottom sample
    come from the 7027 RawDetection record; the sample interval and sound
    velocity come from the 7000 SonarSettings record. This first version
    assumes a single transmit sector and a contiguous beam numbering
    (water-column beam i == detection beam i).

    Template Args:
        t_ifstream:
    """

    @overload
    def get_raw_amplitudes(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    @overload
    def get_raw_amplitudes(self, beam_selection: themachinethatgoesping.algorithms_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.uint32], dict(order='C')]:
        """
        Water column amplitudes (magnitude) in their raw, unconverted values
        (uint32).

        The values are returned as stored on disk (widened to uint32; 16 bit
        records keep their 0..65535 range). No dB conversion is applied - see
        get_amplitudes for dB. Missing beams/samples are 0.
        """

    @overload
    def get_raw_phase(self) -> Annotated[NDArray[numpy.int16], dict(order='C')]: ...

    @overload
    def get_raw_phase(self, beam_selection: themachinethatgoesping.algorithms_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.int16], dict(order='C')]:
        """
        Water column phase in its raw, unconverted int16 values (radians =
        value / 10430).

        All-zero if the record contains no phase. Missing beams/samples are 0.
        """

    @overload
    def get_phase(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_phase(self, beam_selection: themachinethatgoesping.algorithms_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Water column phase in degrees (NaN for missing beams/samples, all-NaN
        if the record contains no phase).
        """

    def copy(self) -> S7KPingWatercolumn_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingWatercolumn_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingWatercolumn_stream: ...

    def get_watercolumn_calibration(self) -> S7KWaterColumnCalibration: ...

    def get_multisectorwatercolumn_calibration(self) -> S7KMultiSectorWaterColumnCalibration: ...

    def update_calibration(self, calibration: S7KMultiSectorWaterColumnCalibration_flyweight) -> None:
        """
        Replace the ping's calibration with the given (deduplicated) multi-sector calibration.
        """

class S7KPingWatercolumn(themachinethatgoesping.pingprocessing_nanopy.datatypes.I_PingWatercolumn):
    """
    Water column accessor of an s7k ping.

    The water-column amplitudes come from the 7042 CompressedWaterColumn
    record; the per-beam receive angles and the detected bottom sample
    come from the 7027 RawDetection record; the sample interval and sound
    velocity come from the 7000 SonarSettings record. This first version
    assumes a single transmit sector and a contiguous beam numbering
    (water-column beam i == detection beam i).

    Template Args:
        t_ifstream:
    """

    @overload
    def get_raw_amplitudes(self) -> Annotated[NDArray[numpy.uint32], dict(order='C')]: ...

    @overload
    def get_raw_amplitudes(self, beam_selection: themachinethatgoesping.algorithms_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.uint32], dict(order='C')]:
        """
        Water column amplitudes (magnitude) in their raw, unconverted values
        (uint32).

        The values are returned as stored on disk (widened to uint32; 16 bit
        records keep their 0..65535 range). No dB conversion is applied - see
        get_amplitudes for dB. Missing beams/samples are 0.
        """

    @overload
    def get_raw_phase(self) -> Annotated[NDArray[numpy.int16], dict(order='C')]: ...

    @overload
    def get_raw_phase(self, beam_selection: themachinethatgoesping.algorithms_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.int16], dict(order='C')]:
        """
        Water column phase in its raw, unconverted int16 values (radians =
        value / 10430).

        All-zero if the record contains no phase. Missing beams/samples are 0.
        """

    @overload
    def get_phase(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_phase(self, beam_selection: themachinethatgoesping.algorithms_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Water column phase in degrees (NaN for missing beams/samples, all-NaN
        if the record contains no phase).
        """

    def copy(self) -> S7KPingWatercolumn:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingWatercolumn: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingWatercolumn: ...

    def get_watercolumn_calibration(self) -> S7KWaterColumnCalibration: ...

    def get_multisectorwatercolumn_calibration(self) -> S7KMultiSectorWaterColumnCalibration: ...

    def update_calibration(self, calibration: S7KMultiSectorWaterColumnCalibration_flyweight) -> None:
        """
        Replace the ping's calibration with the given (deduplicated) multi-sector calibration.
        """

class S7KPing_stream(themachinethatgoesping.pingprocessing_nanopy.datatypes.I_Ping):
    """
    A single ping of an s7k file. Groups all datagrams (sonar settings,
    bathymetry, water column) that belong to the same ping and exposes
    them via the bottom() and watercolumn() sub-objects.

    Template Args:
        t_ifstream: 

    Note:
        The datagram-processing functions are not implemented yet. This
        class currently only provides the structure so the ping can be
        filled in in a later step.
    """

    @property
    def file_data(self) -> S7KPingFileData_stream: ...

    def copy(self) -> S7KPing_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPing_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPing_stream: ...

class S7KPing(themachinethatgoesping.pingprocessing_nanopy.datatypes.I_Ping):
    """
    A single ping of an s7k file. Groups all datagrams (sonar settings,
    bathymetry, water column) that belong to the same ping and exposes
    them via the bottom() and watercolumn() sub-objects.

    Template Args:
        t_ifstream: 

    Note:
        The datagram-processing functions are not implemented yet. This
        class currently only provides the structure so the ping can be
        filled in in a later step.
    """

    @property
    def file_data(self) -> S7KPingFileData: ...

    def copy(self) -> S7KPing:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPing: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPing: ...
