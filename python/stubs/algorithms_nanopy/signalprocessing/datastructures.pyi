import enum
from typing import overload


class t_TxSignalType(enum.Enum):
    CW = 0

    FM_UP_SWEEP = 1

    FM_DOWN_SWEEP = 2

    UNKNOWN = 3

class o_TxSignalType:
    """
    Helper class to convert between strings and enum values of type 't_TxSignalType'
    """

    @overload
    def __init__(self, value: t_TxSignalType = t_TxSignalType.CW) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> t_TxSignalType:
        """enum value"""

    @value.setter
    def value(self, arg: t_TxSignalType, /) -> None: ...

    __default_value__: themachinethatgoesping.algorithms_nanopy.signalprocessing.datastructures.t_TxSignalType = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_TxSignalType, /) -> bool: ...

    @overload
    def __eq__(self, arg: t_TxSignalType, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_TxSignalType:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_TxSignalType: ...

    def __deepcopy__(self, arg: dict, /) -> o_TxSignalType: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_TxSignalType:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> None: ...

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class GenericSignalParameters:
    """Class representing information about a generic type."""

    def __init__(self, center_frequency: float, bandwidth: float, effective_pulse_duration: float, tx_signal_type: o_TxSignalType) -> None:
        """Default constructor."""

    def __eq__(self, other: GenericSignalParameters) -> bool:
        """
        Equality operator.
        Args:
            rhs: The right-hand side of the operator.

        Returns:
            True if the objects are equal, false otherwise.
        """

    def get_center_frequency(self) -> float:
        """Center frequency of the signal in Hz."""

    def get_bandwidth(self) -> float:
        """Bandwidth of the signal in Hz."""

    def get_effective_pulse_duration(self) -> float:
        """Effective pulse duration of the signal in seconds."""

    def get_tx_signal_type(self) -> o_TxSignalType: ...

    def set_center_frequency(self, center_frequency: float) -> None:
        """Center frequency of the signal in Hz."""

    def set_bandwidth(self, bandwidth: float) -> None:
        """Bandwidth of the signal in Hz."""

    def set_effective_pulse_duration(self, effective_pulse_duration: float) -> None:
        """Effective pulse duration of the signal in seconds."""

    def set_tx_signal_type(self, tx_signal_type: o_TxSignalType) -> None: ...

    def copy(self) -> GenericSignalParameters:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> GenericSignalParameters: ...

    def __deepcopy__(self, arg: dict, /) -> GenericSignalParameters: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GenericSignalParameters:
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

class CWSignalParameters:
    """Class representing information about a continuous wave signal."""

    def __init__(self, center_frequency: float, bandwidth: float, effective_pulse_duration: float) -> None:
        """Default constructor."""

    def __eq__(self, other: CWSignalParameters) -> bool:
        """
        Equality operator.
        Args:
            rhs: The right-hand side of the operator.

        Returns:
            True if the objects are equal, false otherwise.
        """

    def get_center_frequency(self) -> float:
        """Center frequency of the signal in Hz."""

    def get_bandwidth(self) -> float:
        """Bandwidth of the signal in Hz."""

    def get_effective_pulse_duration(self) -> float:
        """Effective pulse duration of the signal in seconds."""

    def get_tx_signal_type(self) -> o_TxSignalType: ...

    def set_center_frequency(self, center_frequency: float) -> None: ...

    def set_bandwidth(self, bandwidth: float) -> None: ...

    def set_effective_pulse_duration(self, effective_pulse_duration: float) -> None: ...

    def copy(self) -> CWSignalParameters:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> CWSignalParameters: ...

    def __deepcopy__(self, arg: dict, /) -> CWSignalParameters: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> CWSignalParameters:
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

class FMSignalParameters:
    """
    Class representing information about a frequency modulated wave signal
    (chirp).
    """

    @overload
    def __init__(self, center_frequency: float, bandwidth: float, effective_pulse_duration: float, up_sweep: bool) -> None:
        """Default constructor."""

    @overload
    def __init__(self, center_frequency: float, bandwidth: float, effective_pulse_duration: float, tx_signal_type: o_TxSignalType) -> None: ...

    def __eq__(self, other: FMSignalParameters) -> bool:
        """
        Equality operator.
        Args:
            rhs: The right-hand side of the operator.

        Returns:
            True if the objects are equal, false otherwise.
        """

    def get_center_frequency(self) -> float:
        """Center frequency of the signal in Hz."""

    def get_bandwidth(self) -> float:
        """Bandwidth of the signal in Hz."""

    def get_effective_pulse_duration(self) -> float:
        """Effective pulse duration of the signal in seconds."""

    def get_up_sweep(self) -> bool:
        """True if the signal is an up sweep, false otherwise."""

    def get_tx_signal_type(self) -> o_TxSignalType: ...

    def set_center_frequency(self, center_frequency: float) -> None: ...

    def set_bandwidth(self, bandwidth: float) -> None: ...

    def set_effective_pulse_duration(self, effective_pulse_duration: float) -> None: ...

    def set_up_sweep(self, up_sweep: bool) -> None: ...

    def copy(self) -> FMSignalParameters:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> FMSignalParameters: ...

    def __deepcopy__(self, arg: dict, /) -> FMSignalParameters: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FMSignalParameters:
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
