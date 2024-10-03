"""
Submodule that holds datastructures that hold the signal processing input/results
"""
from __future__ import annotations
import typing
__all__ = ['CW', 'CWSignalParameters', 'FMSignalParameters', 'FM_DOWN_SWEEP', 'FM_UP_SWEEP', 'GenericSignalParameters', 'UNKNOWN', 't_TxSignalType']
class CWSignalParameters:
    """
    @class CWSignalParameters Class representing information about a
    continuous wave signal.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> CWSignalParameters:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> CWSignalParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> CWSignalParameters:
        ...
    def __eq__(self, other: CWSignalParameters) -> bool:
        """
        Equality operator.
        
        Parameter ``rhs``:
            The right-hand side of the operator.
        
        Returns:
            True if the objects are equal, false otherwise.
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, center_frequency: float, bandwidth: float, effective_pulse_duration: float) -> None:
        """
        Default constructor.
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
    def copy(self) -> CWSignalParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def get_bandwidth(self) -> float:
        """
        < Bandwidth of the signal in Hz.
        """
    def get_center_frequency(self) -> float:
        """
        < Center frequency of the signal in Hz.
        """
    def get_effective_pulse_duration(self) -> float:
        """
        < Effective pulse duration of the signal in seconds.
        """
    def get_tx_signal_type(self) -> t_TxSignalType:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_bandwidth(self, bandwidth: float) -> None:
        ...
    def set_center_frequency(self, center_frequency: float) -> None:
        ...
    def set_effective_pulse_duration(self, effective_pulse_duration: float) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class FMSignalParameters:
    """
    @class FMSignalParameters Class representing information about a
    frequency modulated wave signal (chirp).
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FMSignalParameters:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> FMSignalParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> FMSignalParameters:
        ...
    def __eq__(self, other: FMSignalParameters) -> bool:
        """
        Equality operator.
        
        Parameter ``rhs``:
            The right-hand side of the operator.
        
        Returns:
            True if the objects are equal, false otherwise.
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, center_frequency: float, bandwidth: float, effective_pulse_duration: float, up_sweep: bool) -> None:
        """
        Default constructor.
        """
    @typing.overload
    def __init__(self, center_frequency: float, bandwidth: float, effective_pulse_duration: float, tx_signal_type: t_TxSignalType) -> None:
        """
        Default constructor.
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
    def copy(self) -> FMSignalParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def get_bandwidth(self) -> float:
        """
        < Bandwidth of the signal in Hz.
        """
    def get_center_frequency(self) -> float:
        """
        < Center frequency of the signal in Hz.
        """
    def get_effective_pulse_duration(self) -> float:
        """
        < Effective pulse duration of the signal in seconds.
        """
    def get_tx_signal_type(self) -> t_TxSignalType:
        ...
    def get_up_sweep(self) -> bool:
        """
        < True if the signal is an up sweep, false otherwise.
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_bandwidth(self, bandwidth: float) -> None:
        ...
    def set_center_frequency(self, center_frequency: float) -> None:
        ...
    def set_effective_pulse_duration(self, effective_pulse_duration: float) -> None:
        ...
    def set_up_sweep(self, up_sweep: bool) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class GenericSignalParameters:
    """
    @class GenericSignalParameters Class representing information about a
    generic type.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GenericSignalParameters:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> GenericSignalParameters:
        ...
    def __deepcopy__(self, arg0: dict) -> GenericSignalParameters:
        ...
    def __eq__(self, other: GenericSignalParameters) -> bool:
        """
        Equality operator.
        
        Parameter ``rhs``:
            The right-hand side of the operator.
        
        Returns:
            True if the objects are equal, false otherwise.
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, center_frequency: float, bandwidth: float, effective_pulse_duration: float, tx_signal_type: t_TxSignalType) -> None:
        """
        Default constructor.
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
    def copy(self) -> GenericSignalParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def get_bandwidth(self) -> float:
        """
        < Bandwidth of the signal in Hz.
        """
    def get_center_frequency(self) -> float:
        """
        < Center frequency of the signal in Hz.
        """
    def get_effective_pulse_duration(self) -> float:
        """
        < Effective pulse duration of the signal in seconds.
        """
    def get_tx_signal_type(self) -> t_TxSignalType:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_bandwidth(self, bandwidth: float) -> None:
        """
        < Bandwidth of the signal in Hz.
        """
    def set_center_frequency(self, center_frequency: float) -> None:
        """
        < Center frequency of the signal in Hz.
        """
    def set_effective_pulse_duration(self, effective_pulse_duration: float) -> None:
        """
        < Effective pulse duration of the signal in seconds.
        """
    def set_tx_signal_type(self, tx_signal_type: t_TxSignalType) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class t_TxSignalType:
    """
    
    
    Members:
    
      CW
    
      FM_UP_SWEEP
    
      FM_DOWN_SWEEP
    
      UNKNOWN
    """
    CW: typing.ClassVar[t_TxSignalType]  # value = <t_TxSignalType.CW: 0>
    FM_DOWN_SWEEP: typing.ClassVar[t_TxSignalType]  # value = <t_TxSignalType.FM_DOWN_SWEEP: 2>
    FM_UP_SWEEP: typing.ClassVar[t_TxSignalType]  # value = <t_TxSignalType.FM_UP_SWEEP: 1>
    UNKNOWN: typing.ClassVar[t_TxSignalType]  # value = <t_TxSignalType.UNKNOWN: 3>
    __members__: typing.ClassVar[dict[str, t_TxSignalType]]  # value = {'CW': <t_TxSignalType.CW: 0>, 'FM_UP_SWEEP': <t_TxSignalType.FM_UP_SWEEP: 1>, 'FM_DOWN_SWEEP': <t_TxSignalType.FM_DOWN_SWEEP: 2>, 'UNKNOWN': <t_TxSignalType.UNKNOWN: 3>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    @typing.overload
    def __init__(self, value: int) -> None:
        ...
    @typing.overload
    def __init__(self, str: str) -> None:
        """
        Construct this enum type from string
        """
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def str(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
CW: t_TxSignalType  # value = <t_TxSignalType.CW: 0>
FM_DOWN_SWEEP: t_TxSignalType  # value = <t_TxSignalType.FM_DOWN_SWEEP: 2>
FM_UP_SWEEP: t_TxSignalType  # value = <t_TxSignalType.FM_UP_SWEEP: 1>
UNKNOWN: t_TxSignalType  # value = <t_TxSignalType.UNKNOWN: 3>
