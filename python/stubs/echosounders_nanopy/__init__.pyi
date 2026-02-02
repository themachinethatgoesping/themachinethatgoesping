"""
Python module to read, write and process single- and multibeam echosounder data formats
"""

from typing import overload

from . import (
    filetemplates as filetemplates,
    gsf as gsf,
    kmall as kmall,
    kongsbergall as kongsbergall,
    pingtools as pingtools,
    simradraw as simradraw
)


class o_KongsbergAllDatagramIdentifier:
    """
    Helper class to convert between strings and enum values of type 't_KongsbergAllDatagramIdentifier'
    """

    @overload
    def __init__(self, value: kongsbergall.t_KongsbergAllDatagramIdentifier = kongsbergall.t_KongsbergAllDatagramIdentifier.unspecified) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> kongsbergall.t_KongsbergAllDatagramIdentifier:
        """enum value"""

    @value.setter
    def value(self, arg: kongsbergall.t_KongsbergAllDatagramIdentifier, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_KongsbergAllDatagramIdentifier, /) -> bool: ...

    @overload
    def __eq__(self, arg: kongsbergall.t_KongsbergAllDatagramIdentifier, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_KongsbergAllDatagramIdentifier:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_KongsbergAllDatagramIdentifier: ...

    def __deepcopy__(self, arg: dict, /) -> o_KongsbergAllDatagramIdentifier: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_KongsbergAllDatagramIdentifier:
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

class o_KongsbergAllActiveSensor:
    """
    Helper class to convert between strings and enum values of type 't_KongsbergAllActiveSensor'
    """

    @overload
    def __init__(self, value: kongsbergall.t_KongsbergAllActiveSensor = kongsbergall.t_KongsbergAllActiveSensor.NotSet) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> kongsbergall.t_KongsbergAllActiveSensor:
        """enum value"""

    @value.setter
    def value(self, arg: kongsbergall.t_KongsbergAllActiveSensor, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_KongsbergAllActiveSensor, /) -> bool: ...

    @overload
    def __eq__(self, arg: kongsbergall.t_KongsbergAllActiveSensor, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_KongsbergAllActiveSensor:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_KongsbergAllActiveSensor: ...

    def __deepcopy__(self, arg: dict, /) -> o_KongsbergAllActiveSensor: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_KongsbergAllActiveSensor:
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

class o_KongsbergAllSystemTransducerConfiguration:
    """
    Helper class to convert between strings and enum values of type 't_KongsbergAllSystemTransducerConfiguration'
    """

    @overload
    def __init__(self, value: kongsbergall.t_KongsbergAllSystemTransducerConfiguration = kongsbergall.t_KongsbergAllSystemTransducerConfiguration.SingleTXSingleRX) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> kongsbergall.t_KongsbergAllSystemTransducerConfiguration:
        """enum value"""

    @value.setter
    def value(self, arg: kongsbergall.t_KongsbergAllSystemTransducerConfiguration, /) -> None: ...

    __default_value__: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllSystemTransducerConfiguration = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_KongsbergAllSystemTransducerConfiguration, /) -> bool: ...

    @overload
    def __eq__(self, arg: kongsbergall.t_KongsbergAllSystemTransducerConfiguration, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_KongsbergAllSystemTransducerConfiguration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_KongsbergAllSystemTransducerConfiguration: ...

    def __deepcopy__(self, arg: dict, /) -> o_KongsbergAllSystemTransducerConfiguration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_KongsbergAllSystemTransducerConfiguration:
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
