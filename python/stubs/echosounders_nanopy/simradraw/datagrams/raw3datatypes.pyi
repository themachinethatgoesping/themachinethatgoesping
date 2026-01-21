import enum
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray


class t_RAW3DataType(enum.Enum):
    """This flag is used in the RAW3 datagram to indicate the type of data"""

    Power = 1

    Angle = 2

    PowerAndAngle = 3

    ComplexFloat16 = 4

    ComplexFloat32 = 8

Power: t_RAW3DataType = t_RAW3DataType.Power

Angle: t_RAW3DataType = t_RAW3DataType.Angle

PowerAndAngle: t_RAW3DataType = t_RAW3DataType.PowerAndAngle

ComplexFloat16: t_RAW3DataType = t_RAW3DataType.ComplexFloat16

ComplexFloat32: t_RAW3DataType = t_RAW3DataType.ComplexFloat32

class i_RAW3Data:
    """
    Interface class for all RAW3 datatypes The RAW3 datagram contains a
    number of different data types.
     - power - angle - power and angle - complex float 32 - ...
    """

    def __init__(self, name: str) -> None: ...

    def class_name(self) -> str: ...

    def has_power(self) -> bool: ...

    def has_angle(self) -> bool: ...

    def get_power(self, dB: bool = False) -> "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>": ...

    def get_angle(self) -> "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>": ...

class RAW3DataComplexFloat32(i_RAW3Data):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, complex_samples: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]) -> None: ...

    def __eq__(self, other: RAW3DataComplexFloat32) -> bool: ...

    def get_complex_samples_bfloat16(self, max_samples: int) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None, None, None), order='C')]: ...

    def get_power(self, dB: bool = False) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_coherent_sum(self, dB: bool = False) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_incoherent_sum(self, dB: bool = False) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_angle(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    def get_power_xtensor(self, dB: bool = False) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_incoherent_sum_xtensor(self, dB: bool = False) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @property
    def complex_samples(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]:
        """Sample data"""

    @complex_samples.setter
    def complex_samples(self, arg: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], /) -> None: ...

    def copy(self) -> RAW3DataComplexFloat32:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RAW3DataComplexFloat32: ...

    def __deepcopy__(self, arg: dict, /) -> RAW3DataComplexFloat32: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class RAW3DataPowerAndAngle(i_RAW3Data):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, power: Annotated[NDArray[numpy.int16], dict(shape=(None,), order='C')], angle: Annotated[NDArray[numpy.uint8], dict(shape=(None, None), order='C')]) -> None: ...

    def __eq__(self, other: RAW3DataPowerAndAngle) -> bool: ...

    def get_power(self, dB: bool = False) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_angle(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @property
    def power(self) -> Annotated[NDArray[numpy.int16], dict(shape=(None,), order='C')]:
        """Sample data"""

    @power.setter
    def power(self, arg: Annotated[NDArray[numpy.int16], dict(shape=(None,), order='C')], /) -> None: ...

    @property
    def angle(self) -> Annotated[NDArray[numpy.int8], dict(shape=(None, None), order='C')]:
        """[along, athwart] 180/128 electrical degrees"""

    @angle.setter
    def angle(self, arg: Annotated[NDArray[numpy.int8], dict(shape=(None, None), order='C')], /) -> None: ...

    def copy(self) -> RAW3DataPowerAndAngle:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RAW3DataPowerAndAngle: ...

    def __deepcopy__(self, arg: dict, /) -> RAW3DataPowerAndAngle: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class RAW3DataPower(i_RAW3Data):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, power_and_angle: Annotated[NDArray[numpy.int16], dict(shape=(None,), order='C')]) -> None: ...

    def __eq__(self, other: RAW3DataPower) -> bool: ...

    def get_power(self, dB: bool = False) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @property
    def power(self) -> Annotated[NDArray[numpy.int16], dict(shape=(None,), order='C')]:
        """Sample data"""

    @power.setter
    def power(self, arg: Annotated[NDArray[numpy.int16], dict(shape=(None,), order='C')], /) -> None: ...

    def copy(self) -> RAW3DataPower:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RAW3DataPower: ...

    def __deepcopy__(self, arg: dict, /) -> RAW3DataPower: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class RAW3DataAngle(i_RAW3Data):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, angle: Annotated[NDArray[numpy.uint8], dict(shape=(None, None), order='C')]) -> None: ...

    def __eq__(self, other: RAW3DataAngle) -> bool: ...

    def get_angle(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    @property
    def angle(self) -> Annotated[NDArray[numpy.int8], dict(shape=(None, None), order='C')]:
        """Sample data"""

    @angle.setter
    def angle(self, arg: Annotated[NDArray[numpy.int8], dict(shape=(None, None), order='C')], /) -> None: ...

    def copy(self) -> RAW3DataAngle:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RAW3DataAngle: ...

    def __deepcopy__(self, arg: dict, /) -> RAW3DataAngle: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class RAW3DataSkipped(i_RAW3Data):
    """
    This class represents a pseudo data type that is used to skip the raw3
    data in the stream. It is used to load the RAW3 datagram info without
    the samples.
    """

    def __init__(self) -> None: ...

    def __eq__(self, other: RAW3DataSkipped) -> bool: ...

    def copy(self) -> RAW3DataSkipped:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RAW3DataSkipped: ...

    def __deepcopy__(self, arg: dict, /) -> RAW3DataSkipped: ...

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
