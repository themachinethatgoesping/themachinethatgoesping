"""
SimradRaw EK80 sample datagram data structures used in RAW3 datagrams).
"""
from __future__ import annotations
import enum
import numpy
import typing
__all__: list[str] = ['Angle', 'ComplexFloat16', 'ComplexFloat32', 'Power', 'PowerAndAngle', 'RAW3DataAngle', 'RAW3DataComplexFloat32', 'RAW3DataPower', 'RAW3DataPowerAndAngle', 'RAW3DataSkipped', 'i_RAW3Data', 't_RAW3DataType']
class RAW3DataAngle(i_RAW3Data):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> RAW3DataAngle:
        ...
    def __deepcopy__(self, arg: dict) -> RAW3DataAngle:
        ...
    def __eq__(self, other: RAW3DataAngle) -> bool:
        ...
    def __init__(self) -> None:
        """
        __init__(self, angle: numpy.ndarray[dtype=uint8, shape=(*, *), order='C']) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> RAW3DataAngle:
        """
        return a copy using the c++ default copy constructor
        """
    def get_angle(self) -> numpy.ndarray[dtype=float32, ..., order='C']:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @property
    def angle(self) -> numpy.ndarray[dtype=int8, ..., order='C']:
        """
        < Sample data
        """
    @angle.setter
    def angle(self, arg: numpy.ndarray[dtype=int8, ..., order='C']) -> None:
        """
        < Sample data
        """
class RAW3DataComplexFloat32(i_RAW3Data):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> RAW3DataComplexFloat32:
        ...
    def __deepcopy__(self, arg: dict) -> RAW3DataComplexFloat32:
        ...
    def __eq__(self, other: RAW3DataComplexFloat32) -> bool:
        ...
    def __init__(self) -> None:
        """
        __init__(self, complex_samples: numpy.ndarray[dtype=float32, shape=(*, *, *), order='C']) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> RAW3DataComplexFloat32:
        """
        return a copy using the c++ default copy constructor
        """
    def get_angle(self) -> numpy.ndarray[dtype=float32, ..., order='C']:
        ...
    def get_coherent_sum(self, dB: bool = False) -> numpy.ndarray[dtype=float32, ..., order='C']:
        ...
    def get_complex_samples_bfloat16(self, max_samples: int) -> numpy.ndarray[dtype=float32, ..., order='C']:
        ...
    def get_incoherent_sum(self, dB: bool = False) -> numpy.ndarray[dtype=float32, ..., order='C']:
        ...
    def get_incoherent_sum_xtensor(self, dB: bool = False) -> numpy.ndarray[dtype=float32, ..., order='C']:
        ...
    def get_power(self, dB: bool = False) -> numpy.ndarray[dtype=float32, ..., order='C']:
        ...
    def get_power_xtensor(self, dB: bool = False) -> numpy.ndarray[dtype=float32, ..., order='C']:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @property
    def complex_samples(self) -> numpy.ndarray[dtype=float32, ..., order='C']:
        """
        < Sample data
        """
    @complex_samples.setter
    def complex_samples(self, arg: numpy.ndarray[dtype=float32, ..., order='C']) -> None:
        """
        < Sample data
        """
class RAW3DataPower(i_RAW3Data):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> RAW3DataPower:
        ...
    def __deepcopy__(self, arg: dict) -> RAW3DataPower:
        ...
    def __eq__(self, other: RAW3DataPower) -> bool:
        ...
    def __init__(self) -> None:
        """
        __init__(self, power_and_angle: numpy.ndarray[dtype=int16, shape=(*), order='C']) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> RAW3DataPower:
        """
        return a copy using the c++ default copy constructor
        """
    def get_power(self, dB: bool = False) -> numpy.ndarray[dtype=float32, ..., order='C']:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @property
    def power(self) -> numpy.ndarray[dtype=int16, ..., order='C']:
        """
        < Sample data
        """
    @power.setter
    def power(self, arg: numpy.ndarray[dtype=int16, ..., order='C']) -> None:
        """
        < Sample data
        """
class RAW3DataPowerAndAngle(i_RAW3Data):
    """
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> RAW3DataPowerAndAngle:
        ...
    def __deepcopy__(self, arg: dict) -> RAW3DataPowerAndAngle:
        ...
    def __eq__(self, other: RAW3DataPowerAndAngle) -> bool:
        ...
    def __init__(self) -> None:
        """
        __init__(self, power: numpy.ndarray[dtype=int16, shape=(*), order='C'], angle: numpy.ndarray[dtype=uint8, shape=(*, *), order='C']) -> None
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> RAW3DataPowerAndAngle:
        """
        return a copy using the c++ default copy constructor
        """
    def get_angle(self) -> numpy.ndarray[dtype=float32, ..., order='C']:
        ...
    def get_power(self, dB: bool = False) -> numpy.ndarray[dtype=float32, ..., order='C']:
        ...
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    @property
    def angle(self) -> numpy.ndarray[dtype=int8, ..., order='C']:
        """
        < [along, athwart] 180/128 electrical degrees
        """
    @angle.setter
    def angle(self, arg: numpy.ndarray[dtype=int8, ..., order='C']) -> None:
        """
        < [along, athwart] 180/128 electrical degrees
        """
    @property
    def power(self) -> numpy.ndarray[dtype=int16, ..., order='C']:
        """
        < Sample data
        """
    @power.setter
    def power(self, arg: numpy.ndarray[dtype=int16, ..., order='C']) -> None:
        """
        < Sample data
        """
class RAW3DataSkipped(i_RAW3Data):
    """
    This class represents a pseudo data type that is used to skip the raw3
    data in the stream. It is used to load the RAW3 datagram info without
    the samples.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> RAW3DataSkipped:
        ...
    def __deepcopy__(self, arg: dict) -> RAW3DataSkipped:
        ...
    def __eq__(self, other: RAW3DataSkipped) -> bool:
        ...
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> RAW3DataSkipped:
        """
        return a copy using the c++ default copy constructor
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
class i_RAW3Data:
    """
    Interface class for all RAW3 datatypes The RAW3 datagram contains a
    number of different data types. - power - angle - power and angle -
    complex float 32 - ...
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __init__(self, name: str) -> None:
        ...
    def class_name(self) -> str:
        ...
    def get_angle(self) -> ...:
        ...
    def get_power(self, dB: bool = False) -> ...:
        ...
    def has_angle(self) -> bool:
        ...
    def has_power(self) -> bool:
        ...
class t_RAW3DataType(enum.Enum):
    """
    This flag is used in the RAW3 datagram to indicate the type of data
    """
    Angle: typing.ClassVar[t_RAW3DataType]  # value = t_RAW3DataType.Angle
    ComplexFloat16: typing.ClassVar[t_RAW3DataType]  # value = t_RAW3DataType.ComplexFloat16
    ComplexFloat32: typing.ClassVar[t_RAW3DataType]  # value = t_RAW3DataType.ComplexFloat32
    Power: typing.ClassVar[t_RAW3DataType]  # value = t_RAW3DataType.Power
    PowerAndAngle: typing.ClassVar[t_RAW3DataType]  # value = t_RAW3DataType.PowerAndAngle
Angle: t_RAW3DataType  # value = t_RAW3DataType.Angle
ComplexFloat16: t_RAW3DataType  # value = t_RAW3DataType.ComplexFloat16
ComplexFloat32: t_RAW3DataType  # value = t_RAW3DataType.ComplexFloat32
Power: t_RAW3DataType  # value = t_RAW3DataType.Power
PowerAndAngle: t_RAW3DataType  # value = t_RAW3DataType.PowerAndAngle
