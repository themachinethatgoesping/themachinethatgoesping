"""
Submodule that holds datastructures that hold the signal processing input/results
"""
from __future__ import annotations
import enum
import typing
__all__: list[str] = ['CWSignalParameters', 'FMSignalParameters', 'GenericSignalParameters', 'o_TxSignalType', 't_TxSignalType']
class CWSignalParameters:
    """
    @class CWSignalParameters Class representing information about a
    continuous wave signal.
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> CWSignalParameters:
        ...
    def __deepcopy__(self, arg: dict) -> CWSignalParameters:
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
    def __setstate__(self, arg: bytes) -> None:
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
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> FMSignalParameters:
        ...
    def __deepcopy__(self, arg: dict) -> FMSignalParameters:
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
    def __init__(self, center_frequency: float, bandwidth: float, effective_pulse_duration: float, up_sweep: bool) -> None:
        """
        __init__(self, center_frequency: float, bandwidth: float, effective_pulse_duration: float, tx_signal_type: themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.t_TxSignalType) -> None
        
        Default constructor.
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
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
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> GenericSignalParameters:
        ...
    def __deepcopy__(self, arg: dict) -> GenericSignalParameters:
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
    def __setstate__(self, arg: bytes) -> None:
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
class o_TxSignalType:
    """
    Helper class to convert between strings and enum values of type 't_TxSignalType'
    """
    __default_value__: typing.ClassVar[t_TxSignalType]  # value = t_TxSignalType.CW
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> o_TxSignalType:
        ...
    def __deepcopy__(self, arg: dict) -> o_TxSignalType:
        ...
    def __eq__(self, arg: o_TxSignalType) -> bool:
        """
        __eq__(self, arg: themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.t_TxSignalType, /) -> bool
        __eq__(self, arg: int, /) -> bool
        __eq__(self, arg: str, /) -> bool
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, value: t_TxSignalType = ...) -> None:
        """
        __init__(self, value: str) -> None
        __init__(self, value: int) -> None
        
        Overloaded function.
        
        1. ``__init__(self, value: themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.t_TxSignalType = t_TxSignalType.CW) -> None``
        
        Construct from enum value
        
        2. ``__init__(self, value: str) -> None``
        
        Construct from string
        
        3. ``__init__(self, value: int) -> None``
        
        Construct from string
        """
    def __repr__(self) -> str:
        """
        __repr__(self) -> None
        
        Overloaded function.
        
        1. ``__repr__(self) -> str``
        
        Return object information as string
        
        2. ``__repr__(self) -> None``
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        __str__(self) -> str
        
        Overloaded function.
        
        1. ``__str__(self) -> str``
        
        
        2. ``__str__(self) -> str``
        
        Return object information as string
        """
    def copy(self) -> o_TxSignalType:
        """
        return a copy using the c++ default copy constructor
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
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def value(self) -> t_TxSignalType:
        """
        enum value
        """
    @value.setter
    def value(self, arg: t_TxSignalType) -> None:
        """
        enum value
        """
class t_TxSignalType(enum.Enum):
    """
    """
    CW: typing.ClassVar[t_TxSignalType]  # value = t_TxSignalType.CW
    FM_DOWN_SWEEP: typing.ClassVar[t_TxSignalType]  # value = t_TxSignalType.FM_DOWN_SWEEP
    FM_UP_SWEEP: typing.ClassVar[t_TxSignalType]  # value = t_TxSignalType.FM_UP_SWEEP
    UNKNOWN: typing.ClassVar[t_TxSignalType]  # value = t_TxSignalType.UNKNOWN
