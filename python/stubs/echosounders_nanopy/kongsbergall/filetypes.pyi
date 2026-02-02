"""KongsbergAll EK60 and EK80 file data types"""
import typing

from collections.abc import Sequence
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

import themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures
import themachinethatgoesping.echosounders_nanopy
import themachinethatgoesping.echosounders_nanopy.filetemplates
import themachinethatgoesping.echosounders_nanopy.kongsbergall
import themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams
import themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces
import themachinethatgoesping.echosounders_nanopy.pingtools


class KongsbergAllWaterColumnCalibration(themachinethatgoesping.echosounders_nanopy.filetemplates.WaterColumnCalibration):
    def __init__(self, sound_velocity: float, effective_pulse_duration: float, system_gain_offset: float, tvg_absorption_db_m: float, tvg_factor: float) -> None: ...

    def modify_kongsberg_em_calibrations(self, sound_velocity: float | None = None, effective_pulse_duration: float | None = None, system_gain_offset: float | None = None, tvg_absorption_db_m: float | None = None, tvg_factor: float | None = None) -> None: ...

    def get_sound_velocity(self) -> float: ...

    def get_effective_pulse_duration(self) -> float: ...

    def get_system_gain_offset(self) -> float: ...

    def initialized(self) -> bool: ...

    def check_initialized(self) -> None: ...

    def check_initialization(self) -> None: ...

    def pre_hashed(self) -> KongsbergAllMultiSectorWaterColumnCalibration_flyweight:
        """
        Return this class as a flyweight with computed hash. This faster when updating the ping calibration.
        """

    def __eq__(self, other: KongsbergAllWaterColumnCalibration) -> bool: ...

    def copy(self) -> KongsbergAllWaterColumnCalibration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllWaterColumnCalibration: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllWaterColumnCalibration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> KongsbergAllWaterColumnCalibration:
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

class KongsbergAllMultiSectorWaterColumnCalibration_flyweight:
    """Flyweight wrapper around the MultiSectorCalibration class."""

    def __init__(self, other: KongsbergAllMultiSectorWaterColumnCalibration) -> None:
        """Create a flyweight from a MultiSectorCalibration object."""

    def get(self) -> KongsbergAllMultiSectorWaterColumnCalibration:
        """Get the underlying T_MultiSectorCalibration object."""

class KongsbergAllMultiSectorWaterColumnCalibration:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, calibration_per_sector: Sequence[KongsbergAllWaterColumnCalibration]) -> None: ...

    @overload
    def __init__(self, other: KongsbergAllMultiSectorWaterColumnCalibration) -> None: ...

    def has_power_calibration(self) -> bool: ...

    def has_ap_calibration(self) -> bool: ...

    def has_av_calibration(self) -> bool: ...

    def has_sp_calibration(self) -> bool: ...

    def has_sv_calibration(self) -> bool: ...

    def has_valid_absorption_db_m(self) -> bool: ...

    def get_number_of_sectors(self) -> int: ...

    def __len__(self) -> int: ...

    def get_calibrations(self) -> list[KongsbergAllWaterColumnCalibration]: ...

    def pre_hashed(self) -> KongsbergAllMultiSectorWaterColumnCalibration_flyweight:
        """
        Return this class as a flyweight with computed hash. This faster when updating the ping calibration.
        """

    def __eq__(self, other: KongsbergAllMultiSectorWaterColumnCalibration) -> bool: ...

    def copy(self) -> KongsbergAllMultiSectorWaterColumnCalibration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllMultiSectorWaterColumnCalibration: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllMultiSectorWaterColumnCalibration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> KongsbergAllMultiSectorWaterColumnCalibration:
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
    def apply_beam_sample_correction_power(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_power(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_pp(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_pp(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_pv(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_pv(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_ap(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_ap(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_sp(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_sp(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_sv(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_sv(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def inplace_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None: ...

    @overload
    def inplace_beam_sample_correction_av(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None: ...

    @overload
    def apply_beam_sample_correction_pp_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]:
        """Apply pp calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_pp_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_pv_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]:
        """Apply pv calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_pv_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_ap_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]:
        """Apply ap calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_ap_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]:
        """Apply av calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_sp_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]:
        """Apply sp calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_sp_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def apply_beam_sample_correction_sv_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]:
        """Apply sv calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_sv_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]: ...

    @overload
    def inplace_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None:
        """Inplace apply av calibration with per-beam absorption coefficients."""

    @overload
    def inplace_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None: ...

class FilePackageIndex_kongsbergall_FilePackageIndex:
    def __init__(self) -> None: ...

    @property
    def file_path(self) -> str: ...

    @file_path.setter
    def file_path(self, arg: str, /) -> None: ...

    @property
    def file_size(self) -> int: ...

    @file_size.setter
    def file_size(self, arg: int, /) -> None: ...

    @property
    def datagram_info_data(self) -> list["themachinethatgoesping::echosounders::filetemplates::datatypes::DatagramInfoData_themachinethatgoesping_echosounders_kongsbergall_t_KongsbergAllDatagramIdentifier"]:
        """all datagrams"""

    @datagram_info_data.setter
    def datagram_info_data(self, arg: Sequence["themachinethatgoesping::echosounders::filetemplates::datatypes::DatagramInfoData_themachinethatgoesping_echosounders_kongsbergall_t_KongsbergAllDatagramIdentifier"], /) -> None: ...

    def __eq__(self, other: FilePackageIndex_kongsbergall_FilePackageIndex) -> bool: ...

    def copy(self) -> FilePackageIndex_kongsbergall_FilePackageIndex:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> FilePackageIndex_kongsbergall_FilePackageIndex: ...

    def __deepcopy__(self, arg: dict, /) -> FilePackageIndex_kongsbergall_FilePackageIndex: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FilePackageIndex_kongsbergall_FilePackageIndex:
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

class KongsbergAllPingFileData_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingFileData):
    def set_runtime_parameters(self, runtime_parameters: "boost::flyweights::flyweight_themachinethatgoesping_echosounders_kongsbergall_datagrams_RuntimeParameters_boost_parameter_void__boost_parameter_void__boost_parameter_void__boost_parameter_void__boost_parameter_void_") -> None: ...

    def get_runtime_parameters(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters: ...

    def read_merged_watercolumndatagram(self, skip_data: bool = False) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram: ...

    def init_watercolumn_calibration(self, arg: bool, /) -> None: ...

    def has_watercolumn_calibration(self) -> bool: ...

    @overload
    def set_watercolumn_calibration(self, calibration: KongsbergAllWaterColumnCalibration) -> None: ...

    @overload
    def set_watercolumn_calibration(self, calibrations: Sequence[KongsbergAllWaterColumnCalibration]) -> None: ...

    @overload
    def get_watercolumn_calibration(self, tx_sector: int) -> KongsbergAllWaterColumnCalibration: ...

    @overload
    def get_watercolumn_calibration(self) -> KongsbergAllWaterColumnCalibration: ...

    def get_multisector_calibration(self) -> KongsbergAllMultiSectorWaterColumnCalibration: ...

    def set_multisector_calibration(self, calibration: KongsbergAllMultiSectorWaterColumnCalibration) -> None: ...

    @overload
    def read_xyz(self) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1:
        """
        read XYZ for the bottom detection datagram

        Returns:
            algorithms::geoprocessing::datastructures::XYZ_1
        """

    @overload
    def read_xyz(self, selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1:
        """
        read XYZ for the specified beams from the bottom detection datagram
        Note: if the beam numbers from the beam selection exceed the number of
              beams in the
        datagram, the corresponding XYZ values will be NaN

        Args:
            bs: beam selection

        Returns:
            algorithms::geoprocessing::datastructures::XYZ_1
        """

    def load_wci(self, force: bool = False) -> None: ...

    def load_sys(self, force: bool = False) -> None: ...

    def release_wci(self) -> None: ...

    def release_sys(self) -> None: ...

    def release_multisector_calibration(self) -> None: ...

    def wci_loaded(self) -> bool: ...

    def sys_loaded(self) -> bool: ...

    def multisector_calibration_loaded(self) -> bool: ...

    def copy(self) -> KongsbergAllPingFileData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllPingFileData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllPingFileData_stream: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> str: ...

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str: ...

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllDatagramInterface_stream]: ...

class KongsbergAllPingFileData(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingFileData):
    def set_runtime_parameters(self, runtime_parameters: "boost::flyweights::flyweight_themachinethatgoesping_echosounders_kongsbergall_datagrams_RuntimeParameters_boost_parameter_void__boost_parameter_void__boost_parameter_void__boost_parameter_void__boost_parameter_void_") -> None: ...

    def get_runtime_parameters(self) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.RuntimeParameters: ...

    def read_merged_watercolumndatagram(self, skip_data: bool = False) -> themachinethatgoesping.echosounders_nanopy.kongsbergall.datagrams.WatercolumnDatagram: ...

    def init_watercolumn_calibration(self, arg: bool, /) -> None: ...

    def has_watercolumn_calibration(self) -> bool: ...

    @overload
    def set_watercolumn_calibration(self, calibration: KongsbergAllWaterColumnCalibration) -> None: ...

    @overload
    def set_watercolumn_calibration(self, calibrations: Sequence[KongsbergAllWaterColumnCalibration]) -> None: ...

    @overload
    def get_watercolumn_calibration(self, tx_sector: int) -> KongsbergAllWaterColumnCalibration: ...

    @overload
    def get_watercolumn_calibration(self) -> KongsbergAllWaterColumnCalibration: ...

    def get_multisector_calibration(self) -> KongsbergAllMultiSectorWaterColumnCalibration: ...

    def set_multisector_calibration(self, calibration: KongsbergAllMultiSectorWaterColumnCalibration) -> None: ...

    @overload
    def read_xyz(self) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1:
        """
        read XYZ for the bottom detection datagram

        Returns:
            algorithms::geoprocessing::datastructures::XYZ_1
        """

    @overload
    def read_xyz(self, selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSelection) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1:
        """
        read XYZ for the specified beams from the bottom detection datagram
        Note: if the beam numbers from the beam selection exceed the number of
              beams in the
        datagram, the corresponding XYZ values will be NaN

        Args:
            bs: beam selection

        Returns:
            algorithms::geoprocessing::datastructures::XYZ_1
        """

    def load_wci(self, force: bool = False) -> None: ...

    def load_sys(self, force: bool = False) -> None: ...

    def release_wci(self) -> None: ...

    def release_sys(self) -> None: ...

    def release_multisector_calibration(self) -> None: ...

    def wci_loaded(self) -> bool: ...

    def sys_loaded(self) -> bool: ...

    def multisector_calibration_loaded(self) -> bool: ...

    def copy(self) -> KongsbergAllPingFileData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllPingFileData: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllPingFileData: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> str: ...

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str: ...

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None: ...

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.o_KongsbergAllDatagramIdentifier) -> object: ...

    def per_file(self) -> list[themachinethatgoesping.echosounders_nanopy.kongsbergall.filedatainterfaces.KongsbergAllDatagramInterface]: ...

class KongsbergAllPingCommon_stream:
    @property
    def file_data(self) -> KongsbergAllPingFileData_stream: ...

    def copy(self) -> KongsbergAllPingCommon_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllPingCommon_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllPingCommon_stream: ...

class KongsbergAllPingCommon:
    @property
    def file_data(self) -> KongsbergAllPingFileData: ...

    def copy(self) -> KongsbergAllPingCommon:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllPingCommon: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllPingCommon: ...

class KongsbergAllPingBottom_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom):
    def copy(self) -> KongsbergAllPingBottom_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllPingBottom_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllPingBottom_stream: ...

class KongsbergAllPingBottom(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom):
    def copy(self) -> KongsbergAllPingBottom:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllPingBottom: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllPingBottom: ...

class KongsbergAllPingWatercolumn_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn):
    def get_watercolumn_calibration(self) -> KongsbergAllWaterColumnCalibration: ...

    def get_multisectorwatercolumn_calibration(self) -> KongsbergAllMultiSectorWaterColumnCalibration: ...

    def update_calibration(self, calibration_flyweight: KongsbergAllMultiSectorWaterColumnCalibration_flyweight) -> None: ...

    def get_tvg_factor_applied(self) -> int: ...

    def get_tvg_offset(self) -> int: ...

    def has_amplitudes(self) -> bool: ...

    @overload
    def get_raw_amplitudes(self) -> Annotated[NDArray[numpy.int8], dict(shape=(None, None), order='C')]: ...

    @overload
    def get_raw_amplitudes(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.int8], dict(shape=(None, None), order='C')]: ...

    @overload
    def get_raw_amplitudes_float(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def get_raw_amplitudes_float(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    def copy(self) -> KongsbergAllPingWatercolumn_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllPingWatercolumn_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllPingWatercolumn_stream: ...

class KongsbergAllPingWatercolumn(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn):
    def get_watercolumn_calibration(self) -> KongsbergAllWaterColumnCalibration: ...

    def get_multisectorwatercolumn_calibration(self) -> KongsbergAllMultiSectorWaterColumnCalibration: ...

    def update_calibration(self, calibration_flyweight: KongsbergAllMultiSectorWaterColumnCalibration_flyweight) -> None: ...

    def get_tvg_factor_applied(self) -> int: ...

    def get_tvg_offset(self) -> int: ...

    def has_amplitudes(self) -> bool: ...

    @overload
    def get_raw_amplitudes(self) -> Annotated[NDArray[numpy.int8], dict(shape=(None, None), order='C')]: ...

    @overload
    def get_raw_amplitudes(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.int8], dict(shape=(None, None), order='C')]: ...

    @overload
    def get_raw_amplitudes_float(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @overload
    def get_raw_amplitudes_float(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    def copy(self) -> KongsbergAllPingWatercolumn:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllPingWatercolumn: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllPingWatercolumn: ...

class KongsbergAllPing_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping):
    @property
    def file_data(self) -> KongsbergAllPingFileData_stream: ...

    def copy(self) -> KongsbergAllPing_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllPing_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllPing_stream: ...

class KongsbergAllPing(themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping):
    @property
    def file_data(self) -> KongsbergAllPingFileData: ...

    def copy(self) -> KongsbergAllPing:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KongsbergAllPing: ...

    def __deepcopy__(self, arg: dict, /) -> KongsbergAllPing: ...
