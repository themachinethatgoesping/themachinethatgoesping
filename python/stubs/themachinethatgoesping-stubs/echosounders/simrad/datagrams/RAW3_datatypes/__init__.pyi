"""Simrad EK80 sample datagram data structures used in RAW3 datagrams)."""
from __future__ import annotations
import themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes
import typing
import numpy
_Shape = typing.Tuple[int, ...]

__all__ = [
    "Angle",
    "ComplexFloat16",
    "ComplexFloat32",
    "Power",
    "PowerAndAngle",
    "RAW3_DataAngle",
    "RAW3_DataComplexFloat32",
    "RAW3_DataPower",
    "RAW3_DataPowerAndAngle",
    "RAW3_DataSkipped",
    "i_RAW3_Data",
    "t_RAW3_DataType"
]


class i_RAW3_Data():
    def __init__(self, name: str) -> None: ...
    @staticmethod
    def get_angle(*args, **kwargs) -> typing.Any: ...
    def get_name(self) -> str: ...
    @staticmethod
    def get_power(*args, **kwargs) -> typing.Any: ...
    def has_angle(self) -> bool: ...
    def has_power(self) -> bool: ...
    pass
class RAW3_DataComplexFloat32(i_RAW3_Data):
    def __copy__(self) -> RAW3_DataComplexFloat32: ...
    def __deepcopy__(self, arg0: dict) -> RAW3_DataComplexFloat32: ...
    def __eq__(self, other: RAW3_DataComplexFloat32) -> bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, complex_samples: numpy.ndarray[numpy.float32]) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> RAW3_DataComplexFloat32: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_angle(self) -> numpy.ndarray[numpy.float32]: ...
    def get_power(self) -> numpy.ndarray[numpy.float32]: ...
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

        :type: numpy.ndarray[numpy.float32]
        """
    @complex_samples.setter
    def complex_samples(self, arg0: numpy.ndarray[numpy.float32]) -> None:
        """
        < Sample data
        """
    __hash__ = None
    pass
class RAW3_DataPower(i_RAW3_Data):
    def __copy__(self) -> RAW3_DataPower: ...
    def __deepcopy__(self, arg0: dict) -> RAW3_DataPower: ...
    def __eq__(self, other: RAW3_DataPower) -> bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, power_and_angle: numpy.ndarray[numpy.int16]) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> RAW3_DataPower: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_power(self) -> numpy.ndarray[numpy.float32]: ...
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

        :type: numpy.ndarray[numpy.int16]
        """
    @power.setter
    def power(self, arg0: numpy.ndarray[numpy.int16]) -> None:
        """
        < Sample data
        """
    __hash__ = None
    pass
class RAW3_DataPowerAndAngle(i_RAW3_Data):
    def __copy__(self) -> RAW3_DataPowerAndAngle: ...
    def __deepcopy__(self, arg0: dict) -> RAW3_DataPowerAndAngle: ...
    def __eq__(self, other: RAW3_DataPowerAndAngle) -> bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, power: numpy.ndarray[numpy.int16], angle: numpy.ndarray[numpy.uint8]) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> RAW3_DataPowerAndAngle: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_angle(self) -> numpy.ndarray[numpy.float32]: ...
    def get_power(self) -> numpy.ndarray[numpy.float32]: ...
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

        :type: numpy.ndarray[numpy.int8]
        """
    @angle.setter
    def angle(self, arg0: numpy.ndarray[numpy.int8]) -> None:
        """
        < [along, athwart] 180/128 electrical degrees
        """
    @property
    def power(self) -> numpy.ndarray[numpy.int16]:
        """
        < Sample data

        :type: numpy.ndarray[numpy.int16]
        """
    @power.setter
    def power(self, arg0: numpy.ndarray[numpy.int16]) -> None:
        """
        < Sample data
        """
    __hash__ = None
    pass
class RAW3_DataSkipped(i_RAW3_Data):
    def __copy__(self) -> RAW3_DataSkipped: ...
    def __deepcopy__(self, arg0: dict) -> RAW3_DataSkipped: ...
    def __eq__(self, other: RAW3_DataSkipped) -> bool: ...
    def __init__(self) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> RAW3_DataSkipped: 
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
    __hash__ = None
    pass
class RAW3_DataAngle(i_RAW3_Data):
    def __copy__(self) -> RAW3_DataAngle: ...
    def __deepcopy__(self, arg0: dict) -> RAW3_DataAngle: ...
    def __eq__(self, other: RAW3_DataAngle) -> bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, angle: numpy.ndarray[numpy.uint8]) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> RAW3_DataAngle: 
        """
        return a copy using the c++ default copy constructor
        """
    def get_angle(self) -> numpy.ndarray[numpy.float32]: ...
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

        :type: numpy.ndarray[numpy.int8]
        """
    @angle.setter
    def angle(self, arg0: numpy.ndarray[numpy.int8]) -> None:
        """
        < Sample data
        """
    __hash__ = None
    pass
class t_RAW3_DataType():
    """
    Members:

      Power : 

      Angle : 

      PowerAndAngle : 

      ComplexFloat16 : 

      ComplexFloat32 : 
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    @typing.overload
    def __init__(self, str: str) -> None: 
        """
        Construct this enum type from string
        """
    @typing.overload
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    def str(self) -> str: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Angle: themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.t_RAW3_DataType # value = <t_RAW3_DataType.Angle: 2>
    ComplexFloat16: themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.t_RAW3_DataType # value = <t_RAW3_DataType.ComplexFloat16: 4>
    ComplexFloat32: themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.t_RAW3_DataType # value = <t_RAW3_DataType.ComplexFloat32: 8>
    Power: themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.t_RAW3_DataType # value = <t_RAW3_DataType.Power: 1>
    PowerAndAngle: themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.t_RAW3_DataType # value = <t_RAW3_DataType.PowerAndAngle: 3>
    __members__: dict # value = {'Power': <t_RAW3_DataType.Power: 1>, 'Angle': <t_RAW3_DataType.Angle: 2>, 'PowerAndAngle': <t_RAW3_DataType.PowerAndAngle: 3>, 'ComplexFloat16': <t_RAW3_DataType.ComplexFloat16: 4>, 'ComplexFloat32': <t_RAW3_DataType.ComplexFloat32: 8>}
    pass
Angle: themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.t_RAW3_DataType # value = <t_RAW3_DataType.Angle: 2>
ComplexFloat16: themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.t_RAW3_DataType # value = <t_RAW3_DataType.ComplexFloat16: 4>
ComplexFloat32: themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.t_RAW3_DataType # value = <t_RAW3_DataType.ComplexFloat32: 8>
Power: themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.t_RAW3_DataType # value = <t_RAW3_DataType.Power: 1>
PowerAndAngle: themachinethatgoesping.echosounders.simrad.datagrams.RAW3_datatypes.t_RAW3_DataType # value = <t_RAW3_DataType.PowerAndAngle: 3>
