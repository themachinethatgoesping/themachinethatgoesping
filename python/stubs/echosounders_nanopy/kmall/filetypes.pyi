"""KMALL EK60 and EK80 file data types"""
import typing

from collections.abc import Sequence
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

import themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures
import themachinethatgoesping.echosounders_nanopy.filetemplates
import themachinethatgoesping.echosounders_nanopy.kmall
import themachinethatgoesping.echosounders_nanopy.kmall.datagrams
import themachinethatgoesping.echosounders_nanopy.kmall.filedatainterfaces
import themachinethatgoesping.echosounders_nanopy.pingtools


class KMALLWaterColumnCalibration(themachinethatgoesping.echosounders_nanopy.filetemplates.WaterColumnCalibration):
    def __init__(self, sound_velocity: float, effective_pulse_duration: float, system_gain_offset: float, tvg_absorption_db_m: float, tvg_factor: float) -> None: ...

    def __eq__(self, other: KMALLWaterColumnCalibration) -> bool: ...

    def copy(self) -> KMALLWaterColumnCalibration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLWaterColumnCalibration: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLWaterColumnCalibration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> KMALLWaterColumnCalibration:
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

class KMALLMultiSectorWaterColumnCalibration_flyweight:
    """Flyweight wrapper around the MultiSectorCalibration class."""

    def __init__(self, other: KMALLMultiSectorWaterColumnCalibration) -> None:
        """Create a flyweight from a MultiSectorCalibration object."""

    def get(self) -> KMALLMultiSectorWaterColumnCalibration:
        """Get the underlying T_MultiSectorCalibration object."""

class KMALLMultiSectorWaterColumnCalibration:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, calibration_per_sector: Sequence[KMALLWaterColumnCalibration]) -> None: ...

    @overload
    def __init__(self, other: KMALLMultiSectorWaterColumnCalibration) -> None: ...

    def has_power_calibration(self) -> bool: ...

    def has_ap_calibration(self) -> bool: ...

    def has_av_calibration(self) -> bool: ...

    def has_sp_calibration(self) -> bool: ...

    def has_sv_calibration(self) -> bool: ...

    def has_valid_absorption_db_m(self) -> bool: ...

    def get_number_of_sectors(self) -> int: ...

    def __len__(self) -> int: ...

    def get_calibrations(self) -> list[KMALLWaterColumnCalibration]: ...

    def pre_hashed(self) -> KMALLMultiSectorWaterColumnCalibration_flyweight:
        """
        Return this class as a flyweight with computed hash. This faster when updating the ping calibration.
        """

    def __eq__(self, other: KMALLMultiSectorWaterColumnCalibration) -> bool: ...

    def copy(self) -> KMALLMultiSectorWaterColumnCalibration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLMultiSectorWaterColumnCalibration: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLMultiSectorWaterColumnCalibration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> KMALLMultiSectorWaterColumnCalibration:
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
    def apply_beam_sample_correction_pp_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply pp calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_pp_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_pv_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply pv calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_pv_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_ap_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply ap calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_ap_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply av calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sp_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply sp calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_sp_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def apply_beam_sample_correction_sv_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]:
        """Apply sv calibration with per-beam absorption coefficients."""

    @overload
    def apply_beam_sample_correction_sv_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

    @overload
    def inplace_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None:
        """Inplace apply av calibration with per-beam absorption coefficients."""

    @overload
    def inplace_beam_sample_correction_av_per_beam(self, wci: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], beam_angles: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], ranges: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], absorption_db_m_per_beam: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], beam_numbers_per_tx_sector: Sequence[Sequence[int]], mp_cores: int = 1) -> None: ...

class FilePackageIndex_kmall_FilePackageIndex:
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
    def datagram_info_data(self) -> list["themachinethatgoesping::echosounders::filetemplates::datatypes::DatagramInfoData_themachinethatgoesping_echosounders_kmall_t_KMALLDatagramIdentifier"]:
        """all datagrams"""

    @datagram_info_data.setter
    def datagram_info_data(self, arg: Sequence["themachinethatgoesping::echosounders::filetemplates::datatypes::DatagramInfoData_themachinethatgoesping_echosounders_kmall_t_KMALLDatagramIdentifier"], /) -> None: ...

    def __eq__(self, other: FilePackageIndex_kmall_FilePackageIndex) -> bool: ...

    def copy(self) -> FilePackageIndex_kmall_FilePackageIndex:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> FilePackageIndex_kmall_FilePackageIndex: ...

    def __deepcopy__(self, arg: dict, /) -> FilePackageIndex_kmall_FilePackageIndex: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FilePackageIndex_kmall_FilePackageIndex:
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

class KMALLPingFileData_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingFileData):
    def set_runtime_parameters(self, runtime_parameters: "boost::flyweights::flyweight_themachinethatgoesping_echosounders_kmall_datagrams_IOpRuntime_boost_parameter_void__boost_parameter_void__boost_parameter_void__boost_parameter_void__boost_parameter_void_") -> None: ...

    def get_runtime_parameters(self) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IOpRuntime: ...

    def init_watercolumn_calibration(self, arg: bool, /) -> None: ...

    def has_watercolumn_calibration(self) -> bool: ...

    @overload
    def set_watercolumn_calibration(self, calibration: KMALLWaterColumnCalibration) -> None: ...

    @overload
    def set_watercolumn_calibration(self, calibrations: Sequence[KMALLWaterColumnCalibration]) -> None: ...

    @overload
    def get_watercolumn_calibration(self, tx_sector: int) -> KMALLWaterColumnCalibration: ...

    @overload
    def get_watercolumn_calibration(self) -> KMALLWaterColumnCalibration: ...

    def get_multisector_calibration(self) -> KMALLMultiSectorWaterColumnCalibration: ...

    def set_multisector_calibration(self, calibration: KMALLMultiSectorWaterColumnCalibration) -> None: ...

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

    def copy(self) -> KMALLPingFileData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLPingFileData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLPingFileData_stream: ...

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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.filedatainterfaces.KMALLDatagramInterface_stream]: ...

class KMALLPingFileData(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingFileData):
    def set_runtime_parameters(self, runtime_parameters: "boost::flyweights::flyweight_themachinethatgoesping_echosounders_kmall_datagrams_IOpRuntime_boost_parameter_void__boost_parameter_void__boost_parameter_void__boost_parameter_void__boost_parameter_void_") -> None: ...

    def get_runtime_parameters(self) -> themachinethatgoesping.echosounders_nanopy.kmall.datagrams.IOpRuntime: ...

    def init_watercolumn_calibration(self, arg: bool, /) -> None: ...

    def has_watercolumn_calibration(self) -> bool: ...

    @overload
    def set_watercolumn_calibration(self, calibration: KMALLWaterColumnCalibration) -> None: ...

    @overload
    def set_watercolumn_calibration(self, calibrations: Sequence[KMALLWaterColumnCalibration]) -> None: ...

    @overload
    def get_watercolumn_calibration(self, tx_sector: int) -> KMALLWaterColumnCalibration: ...

    @overload
    def get_watercolumn_calibration(self) -> KMALLWaterColumnCalibration: ...

    def get_multisector_calibration(self) -> KMALLMultiSectorWaterColumnCalibration: ...

    def set_multisector_calibration(self, calibration: KMALLMultiSectorWaterColumnCalibration) -> None: ...

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

    def copy(self) -> KMALLPingFileData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLPingFileData: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLPingFileData: ...

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

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.t_KMALLDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.kmall.o_KMALLDatagramIdentifier) -> object: ...

    def per_file(self) -> list[themachinethatgoesping.echosounders_nanopy.kmall.filedatainterfaces.KMALLDatagramInterface]: ...

class KMALLPingCommon_stream:
    @property
    def file_data(self) -> KMALLPingFileData_stream: ...

    def copy(self) -> KMALLPingCommon_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLPingCommon_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLPingCommon_stream: ...

class KMALLPingCommon:
    @property
    def file_data(self) -> KMALLPingFileData: ...

    def copy(self) -> KMALLPingCommon:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLPingCommon: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLPingCommon: ...

class KMALLPingBottom_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom):
    def copy(self) -> KMALLPingBottom_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLPingBottom_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLPingBottom_stream: ...

class KMALLPingBottom(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom):
    def copy(self) -> KMALLPingBottom:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLPingBottom: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLPingBottom: ...

class KMALLPingWatercolumn_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn):
    def get_watercolumn_calibration(self) -> KMALLWaterColumnCalibration: ...

    def get_multisectorwatercolumn_calibration(self) -> KMALLMultiSectorWaterColumnCalibration: ...

    def update_calibration(self, calibration_flyweight: KMALLMultiSectorWaterColumnCalibration_flyweight) -> None: ...

    def get_tvg_factor_applied(self) -> int: ...

    def get_tvg_offset(self) -> int: ...

    def has_amplitudes(self) -> bool: ...

    @overload
    def get_raw_amplitudes(self) -> Annotated[NDArray[numpy.int8], dict(order='C')]: ...

    @overload
    def get_raw_amplitudes(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.int8], dict(order='C')]: ...

    @overload
    def get_raw_amplitudes_float(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_raw_amplitudes_float(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def copy(self) -> KMALLPingWatercolumn_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLPingWatercolumn_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLPingWatercolumn_stream: ...

class KMALLPingWatercolumn(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn):
    def get_watercolumn_calibration(self) -> KMALLWaterColumnCalibration: ...

    def get_multisectorwatercolumn_calibration(self) -> KMALLMultiSectorWaterColumnCalibration: ...

    def update_calibration(self, calibration_flyweight: KMALLMultiSectorWaterColumnCalibration_flyweight) -> None: ...

    def get_tvg_factor_applied(self) -> int: ...

    def get_tvg_offset(self) -> int: ...

    def has_amplitudes(self) -> bool: ...

    @overload
    def get_raw_amplitudes(self) -> Annotated[NDArray[numpy.int8], dict(order='C')]: ...

    @overload
    def get_raw_amplitudes(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.int8], dict(order='C')]: ...

    @overload
    def get_raw_amplitudes_float(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    @overload
    def get_raw_amplitudes_float(self, beam_selection: themachinethatgoesping.echosounders_nanopy.pingtools.BeamSampleSelection) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...

    def copy(self) -> KMALLPingWatercolumn:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLPingWatercolumn: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLPingWatercolumn: ...

class KMALLPing_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping):
    @property
    def file_data(self) -> KMALLPingFileData_stream: ...

    def copy(self) -> KMALLPing_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLPing_stream: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLPing_stream: ...

class KMALLPing(themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping):
    @property
    def file_data(self) -> KMALLPingFileData: ...

    def copy(self) -> KMALLPing:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> KMALLPing: ...

    def __deepcopy__(self, arg: dict, /) -> KMALLPing: ...
