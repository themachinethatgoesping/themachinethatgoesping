"""
Python module to read, write and process single- and multibeam echosounder data formats
"""
from __future__ import annotations
import typing
from . import filetemplates
from . import gsf
from . import kongsbergall
from . import pingtools
from . import simradraw
__all__: list[str] = ['filetemplates', 'gsf', 'kongsbergall', 'o_KongsbergAllActiveSensor', 'o_KongsbergAllDatagramIdentifier', 'o_KongsbergAllSystemTransducerConfiguration', 'pingtools', 'simradraw']
class o_KongsbergAllActiveSensor:
    """
    Helper class to convert between strings and enum values of type 't_KongsbergAllActiveSensor'
    """
    __default_value__: typing.ClassVar[kongsbergall.t_KongsbergAllActiveSensor]  # value = t_KongsbergAllActiveSensor.NotSet
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> o_KongsbergAllActiveSensor:
        ...
    def __deepcopy__(self, arg: dict) -> o_KongsbergAllActiveSensor:
        ...
    def __eq__(self, arg: o_KongsbergAllActiveSensor) -> bool:
        """
        __eq__(self, arg: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor, /) -> bool
        __eq__(self, arg: int, /) -> bool
        __eq__(self, arg: str, /) -> bool
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, value: kongsbergall.t_KongsbergAllActiveSensor = ...) -> None:
        """
        __init__(self, value: str) -> None
        __init__(self, value: int) -> None
        
        Overloaded function.
        
        1. ``__init__(self, value: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllActiveSensor = t_KongsbergAllActiveSensor.NotSet) -> None``
        
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
    def copy(self) -> o_KongsbergAllActiveSensor:
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
    def value(self) -> kongsbergall.t_KongsbergAllActiveSensor:
        """
        enum value
        """
    @value.setter
    def value(self, arg: kongsbergall.t_KongsbergAllActiveSensor) -> None:
        """
        enum value
        """
class o_KongsbergAllDatagramIdentifier:
    """
    Helper class to convert between strings and enum values of type 't_KongsbergAllDatagramIdentifier'
    """
    __default_value__: typing.ClassVar[kongsbergall.t_KongsbergAllDatagramIdentifier]  # value = t_KongsbergAllDatagramIdentifier.unspecified
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> o_KongsbergAllDatagramIdentifier:
        ...
    def __deepcopy__(self, arg: dict) -> o_KongsbergAllDatagramIdentifier:
        ...
    def __eq__(self, arg: o_KongsbergAllDatagramIdentifier) -> bool:
        """
        __eq__(self, arg: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier, /) -> bool
        __eq__(self, arg: int, /) -> bool
        __eq__(self, arg: str, /) -> bool
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, value: kongsbergall.t_KongsbergAllDatagramIdentifier = ...) -> None:
        """
        __init__(self, value: str) -> None
        __init__(self, value: int) -> None
        
        Overloaded function.
        
        1. ``__init__(self, value: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllDatagramIdentifier = t_KongsbergAllDatagramIdentifier.unspecified) -> None``
        
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
    def copy(self) -> o_KongsbergAllDatagramIdentifier:
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
    def value(self) -> kongsbergall.t_KongsbergAllDatagramIdentifier:
        """
        enum value
        """
    @value.setter
    def value(self, arg: kongsbergall.t_KongsbergAllDatagramIdentifier) -> None:
        """
        enum value
        """
class o_KongsbergAllSystemTransducerConfiguration:
    """
    Helper class to convert between strings and enum values of type 't_KongsbergAllSystemTransducerConfiguration'
    """
    __default_value__: typing.ClassVar[kongsbergall.t_KongsbergAllSystemTransducerConfiguration]  # value = t_KongsbergAllSystemTransducerConfiguration.SingleTXSingleRX
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> o_KongsbergAllSystemTransducerConfiguration:
        ...
    def __deepcopy__(self, arg: dict) -> o_KongsbergAllSystemTransducerConfiguration:
        ...
    def __eq__(self, arg: o_KongsbergAllSystemTransducerConfiguration) -> bool:
        """
        __eq__(self, arg: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllSystemTransducerConfiguration, /) -> bool
        __eq__(self, arg: int, /) -> bool
        __eq__(self, arg: str, /) -> bool
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, value: kongsbergall.t_KongsbergAllSystemTransducerConfiguration = ...) -> None:
        """
        __init__(self, value: str) -> None
        __init__(self, value: int) -> None
        
        Overloaded function.
        
        1. ``__init__(self, value: themachinethatgoesping.echosounders_nanopy.kongsbergall.t_KongsbergAllSystemTransducerConfiguration = t_KongsbergAllSystemTransducerConfiguration.SingleTXSingleRX) -> None``
        
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
    def copy(self) -> o_KongsbergAllSystemTransducerConfiguration:
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
    def value(self) -> kongsbergall.t_KongsbergAllSystemTransducerConfiguration:
        """
        enum value
        """
    @value.setter
    def value(self, arg: kongsbergall.t_KongsbergAllSystemTransducerConfiguration) -> None:
        """
        enum value
        """
__version__: str = '0.45.6'
