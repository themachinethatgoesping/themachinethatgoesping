"""
Simrad EK80 sample datagram data structures used in RAW3 datagrams).
"""
from __future__ import annotations
import numpy
import typing
__all__ = ['Angle', 'ComplexFloat16', 'ComplexFloat32', 'Power', 'PowerAndAngle', 'RAW3DataAngle', 'RAW3DataComplexFloat32', 'RAW3DataPower', 'RAW3DataPowerAndAngle', 'RAW3DataSkipped', 'i_RAW3Data', 't_RAW3DataType']
class RAW3DataAngle(i_RAW3Data):
    """
    """
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> RAW3DataAngle:
        ...
    def __deepcopy__(self, arg0: dict) -> RAW3DataAngle:
        ...
    def __eq__(self, other: RAW3DataAngle) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, angle: numpy.ndarray[numpy.uint8]) -> None:
        ...
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
    def get_angle(self) -> numpy.ndarray[numpy.float32]:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    @property
    def angle(self) -> numpy.ndarray[numpy.int8]:
        """
        < Sample data
        """
    @angle.setter
    def angle(self, arg0: numpy.ndarray[numpy.int8]) -> None:
        ...
class RAW3DataComplexFloat32(i_RAW3Data):
    """
    """
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> RAW3DataComplexFloat32:
        ...
    def __deepcopy__(self, arg0: dict) -> RAW3DataComplexFloat32:
        ...
    def __eq__(self, other: RAW3DataComplexFloat32) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, complex_samples: numpy.ndarray[numpy.float32]) -> None:
        ...
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
    def get_angle(self) -> numpy.ndarray[numpy.float32]:
        ...
    def get_power(self, dB: bool = False) -> numpy.ndarray[numpy.float32]:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    @property
    def complex_samples(self) -> numpy.ndarray[numpy.float32]:
        """
        < Sample data
        """
    @complex_samples.setter
    def complex_samples(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        ...
class RAW3DataPower(i_RAW3Data):
    """
    """
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> RAW3DataPower:
        ...
    def __deepcopy__(self, arg0: dict) -> RAW3DataPower:
        ...
    def __eq__(self, other: RAW3DataPower) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, power_and_angle: numpy.ndarray[numpy.int16]) -> None:
        ...
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
    def get_power(self, dB: bool = False) -> numpy.ndarray[numpy.float32]:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    @property
    def power(self) -> numpy.ndarray[numpy.int16]:
        """
        < Sample data
        """
    @power.setter
    def power(self, arg0: numpy.ndarray[numpy.int16]) -> None:
        ...
class RAW3DataPowerAndAngle(i_RAW3Data):
    """
    """
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> RAW3DataPowerAndAngle:
        ...
    def __deepcopy__(self, arg0: dict) -> RAW3DataPowerAndAngle:
        ...
    def __eq__(self, other: RAW3DataPowerAndAngle) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, power: numpy.ndarray[numpy.int16], angle: numpy.ndarray[numpy.uint8]) -> None:
        ...
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
    def get_angle(self) -> numpy.ndarray[numpy.float32]:
        ...
    def get_power(self, dB: bool = False) -> numpy.ndarray[numpy.float32]:
        ...
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    @property
    def angle(self) -> numpy.ndarray[numpy.int8]:
        """
        < [along, athwart] 180/128 electrical degrees
        """
    @angle.setter
    def angle(self, arg0: numpy.ndarray[numpy.int8]) -> None:
        ...
    @property
    def power(self) -> numpy.ndarray[numpy.int16]:
        """
        < Sample data
        """
    @power.setter
    def power(self, arg0: numpy.ndarray[numpy.int16]) -> None:
        ...
class RAW3DataSkipped(i_RAW3Data):
    """
    This class represents a pseudo data type that is used to skip the raw3
    data in the stream. It is used to load the RAW3 datagram info without
    the samples.
    """
    __hash__: typing.ClassVar[None] = None
    def __copy__(self) -> RAW3DataSkipped:
        ...
    def __deepcopy__(self, arg0: dict) -> RAW3DataSkipped:
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
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
class i_RAW3Data:
    """
    Interface class for all RAW3 datatypes The RAW3 datagram contains a
    number of different data types. - power - angle - power and angle -
    complex float 32 - ...
    """
    def __init__(self, name: str) -> None:
        ...
    def get_angle(self) -> ...:
        ...
    def get_name(self) -> str:
        ...
    def get_power(self, dB: bool = False) -> ...:
        ...
    def has_angle(self) -> bool:
        ...
    def has_power(self) -> bool:
        ...
class t_RAW3DataType:
    """
    This flag is used in the RAW3 datagram to indicate the type of data
    
    Members:
    
      Power : 
    
      Angle : 
    
      PowerAndAngle : 
    
      ComplexFloat16 : 
    
      ComplexFloat32 : 
    """
    Angle: typing.ClassVar[t_RAW3DataType]  # value = <t_RAW3DataType.Angle: 2>
    ComplexFloat16: typing.ClassVar[t_RAW3DataType]  # value = <t_RAW3DataType.ComplexFloat16: 4>
    ComplexFloat32: typing.ClassVar[t_RAW3DataType]  # value = <t_RAW3DataType.ComplexFloat32: 8>
    Power: typing.ClassVar[t_RAW3DataType]  # value = <t_RAW3DataType.Power: 1>
    PowerAndAngle: typing.ClassVar[t_RAW3DataType]  # value = <t_RAW3DataType.PowerAndAngle: 3>
    __members__: typing.ClassVar[dict[str, t_RAW3DataType]]  # value = {'Power': <t_RAW3DataType.Power: 1>, 'Angle': <t_RAW3DataType.Angle: 2>, 'PowerAndAngle': <t_RAW3DataType.PowerAndAngle: 3>, 'ComplexFloat16': <t_RAW3DataType.ComplexFloat16: 4>, 'ComplexFloat32': <t_RAW3DataType.ComplexFloat32: 8>}
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
Angle: t_RAW3DataType  # value = <t_RAW3DataType.Angle: 2>
ComplexFloat16: t_RAW3DataType  # value = <t_RAW3DataType.ComplexFloat16: 4>
ComplexFloat32: t_RAW3DataType  # value = <t_RAW3DataType.ComplexFloat32: 8>
Power: t_RAW3DataType  # value = <t_RAW3DataType.Power: 1>
PowerAndAngle: t_RAW3DataType  # value = <t_RAW3DataType.PowerAndAngle: 3>
