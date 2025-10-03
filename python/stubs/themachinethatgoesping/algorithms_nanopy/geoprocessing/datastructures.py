"""
Submodule that holds datastructures that hold the raytracers/georeferncing results
"""
from __future__ import annotations
import typing
__all__: list[str] = ['BeamSampleParameters', 'RaytraceResult', 'RaytraceResults_1', 'RaytraceResults_2', 'RaytraceResults_3', 'SampleDirectionsRange_1', 'SampleDirectionsRange_2', 'SampleDirectionsRange_3', 'SampleDirectionsTime_1', 'SampleDirectionsTime_2', 'SampleDirectionsTime_3', 'SampleDirections_1', 'SampleDirections_2', 'SampleDirections_3', 'SampleIndices_1', 'SampleIndices_2', 'SampleIndices_3', 'XYZ_1', 'XYZ_2', 'XYZ_3']
class BeamSampleParameters:
    """
    A structure to store directional parameters of multibeam system.
    Usefull as input for raytracing water column images.
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def set_alongtrack_angles(*args, **kwargs) -> None:
        ...
    @staticmethod
    def set_crosstrack_angles(*args, **kwargs) -> None:
        ...
    @staticmethod
    def set_first_sample_offset(*args, **kwargs) -> None:
        ...
    @staticmethod
    def set_number_of_samples(*args, **kwargs) -> None:
        ...
    @staticmethod
    def set_sample_interval(*args, **kwargs) -> None:
        ...
    def __copy__(self) -> BeamSampleParameters:
        ...
    def __deepcopy__(self, arg: dict) -> BeamSampleParameters:
        ...
    def __eq__(self, other: BeamSampleParameters) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, number_of_beams: int) -> None:
        """
        __init__(self, alongtrack_angles: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angles: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, first_sample_offset: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, sample_interval: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, number_of_samples: xt::xtensor_container<xt::uvector<unsigned int, xsimd::aligned_allocator<unsigned int, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Construct a new BeamSampleParameters object (all values uninitialized)
        
        Parameter ``number_of_beams``:
            number of beams
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
    def copy(self) -> BeamSampleParameters:
        """
        return a copy using the c++ default copy constructor
        """
    def get_alongtrack_angles(self) -> ...:
        ...
    def get_crosstrack_angles(self) -> ...:
        ...
    def get_first_sample_offset(self) -> ...:
        ...
    def get_number_of_samples(self) -> ...:
        ...
    def get_sample_interval(self) -> ...:
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
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class RaytraceResult:
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> RaytraceResult:
        ...
    def __deepcopy__(self, arg: dict) -> RaytraceResult:
        ...
    def __eq__(self, other: RaytraceResult) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, x: float, y: float, z: float, true_range: float) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, x: float, y: float, z: float, true_range: float) -> None``
        
        Construct a new RaytraceResult object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
        
        Parameter ``true_range``:
            in m, accumulated ray path length
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
    def copy(self) -> RaytraceResult:
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
    def true_range(self) -> float:
        """
        < in m, accumulated ray path length
        """
    @true_range.setter
    def true_range(self, arg: float) -> None:
        """
        < in m, accumulated ray path length
        """
    @property
    def x(self) -> float:
        """
        < in m, positive forward
        """
    @x.setter
    def x(self, arg: float) -> None:
        """
        < in m, positive forward
        """
    @property
    def y(self) -> float:
        """
        < in m, positive starboard
        """
    @y.setter
    def y(self, arg: float) -> None:
        """
        < in m, positive starboard
        """
    @property
    def z(self) -> float:
        """
        < in m, positive downwards
        """
    @z.setter
    def z(self, arg: float) -> None:
        """
        < in m, positive downwards
        """
class RaytraceResults_1(XYZ_1):
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    concat: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> RaytraceResults_1:
        ...
    def __deepcopy__(self, arg: dict) -> RaytraceResults_1:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, x: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, y: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, z: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, true_range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, x: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, y: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, z: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, true_range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new RaytraceResults object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
        
        Parameter ``true_range``:
            in m, accumulated ray path length
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
    def copy(self) -> RaytraceResults_1:
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
    def true_range(self) -> ...:
        """
        < in m, accumulated ray path length
        """
    @true_range.setter
    def true_range(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in m, accumulated ray path length
        """
class RaytraceResults_2(XYZ_2):
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    concat: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> RaytraceResults_2:
        ...
    def __deepcopy__(self, arg: dict) -> RaytraceResults_2:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, x: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, y: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, z: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, true_range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, x: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, y: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, z: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, true_range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new RaytraceResults object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
        
        Parameter ``true_range``:
            in m, accumulated ray path length
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
    def copy(self) -> RaytraceResults_2:
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
    def true_range(self) -> ...:
        """
        < in m, accumulated ray path length
        """
    @true_range.setter
    def true_range(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in m, accumulated ray path length
        """
class RaytraceResults_3(XYZ_3):
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) depth and true range.
    These coordinates can be converted to UTM or Lat/Lon if a reference
    position (for coordinate 0) is known.
    """
    concat: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> RaytraceResults_3:
        ...
    def __deepcopy__(self, arg: dict) -> RaytraceResults_3:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, x: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, y: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, z: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, true_range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, x: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, y: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, z: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, true_range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new RaytraceResults object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
        
        Parameter ``true_range``:
            in m, accumulated ray path length
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
    def copy(self) -> RaytraceResults_3:
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
    def true_range(self) -> ...:
        """
        < in m, accumulated ray path length
        """
    @true_range.setter
    def true_range(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in m, accumulated ray path length
        """
class SampleDirectionsRange_1(SampleDirections_1):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleDirectionsRange_1:
        ...
    def __deepcopy__(self, arg: dict) -> SampleDirectionsRange_1:
        ...
    def __eq__(self, other: SampleDirectionsRange_1) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirections_1, range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        __init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new SampleDirections object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirections_1, range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirections object (from a SampleDirections
        object)
        
        Parameter ``range``:
            in m, accumulated ray path time
        
        4. ``__init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirectionsRange object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
        
        Parameter ``range``:
            in m, accumulated ray path length
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
    def copy(self) -> SampleDirectionsRange_1:
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
    def range(self) -> ...:
        """
        < in m, accumulated ray path time
        """
    @range.setter
    def range(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in m, accumulated ray path time
        """
class SampleDirectionsRange_2(SampleDirections_2):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleDirectionsRange_2:
        ...
    def __deepcopy__(self, arg: dict) -> SampleDirectionsRange_2:
        ...
    def __eq__(self, other: SampleDirectionsRange_2) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirections_2, range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        __init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new SampleDirections object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirections_2, range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirections object (from a SampleDirections
        object)
        
        Parameter ``range``:
            in m, accumulated ray path time
        
        4. ``__init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirectionsRange object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
        
        Parameter ``range``:
            in m, accumulated ray path length
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
    def copy(self) -> SampleDirectionsRange_2:
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
    def range(self) -> ...:
        """
        < in m, accumulated ray path time
        """
    @range.setter
    def range(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in m, accumulated ray path time
        """
class SampleDirectionsRange_3(SampleDirections_3):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleDirectionsRange_3:
        ...
    def __deepcopy__(self, arg: dict) -> SampleDirectionsRange_3:
        ...
    def __eq__(self, other: SampleDirectionsRange_3) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirections_3, range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        __init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new SampleDirections object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirections_3, range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirections object (from a SampleDirections
        object)
        
        Parameter ``range``:
            in m, accumulated ray path time
        
        4. ``__init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, range: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirectionsRange object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
        
        Parameter ``range``:
            in m, accumulated ray path length
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
    def copy(self) -> SampleDirectionsRange_3:
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
    def range(self) -> ...:
        """
        < in m, accumulated ray path time
        """
    @range.setter
    def range(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in m, accumulated ray path time
        """
class SampleDirectionsTime_1(SampleDirections_1):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleDirectionsTime_1:
        ...
    def __deepcopy__(self, arg: dict) -> SampleDirectionsTime_1:
        ...
    def __eq__(self, other: SampleDirectionsTime_1) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirections_1, two_way_travel_time: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        __init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, two_way_travel_time: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new SampleDirections object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirections_1, two_way_travel_time: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirections object (from a SampleDirections
        object)
        
        Parameter ``two_way_travel_time``:
            in s, accumulated ray path time
        
        4. ``__init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, two_way_travel_time: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirectionsTime object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
        
        Parameter ``two_way_travel_time``:
            in m, accumulated ray path length
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
    def copy(self) -> SampleDirectionsTime_1:
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
    def two_way_travel_time(self) -> ...:
        """
        < in s, accumulated ray path time
        """
    @two_way_travel_time.setter
    def two_way_travel_time(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in s, accumulated ray path time
        """
class SampleDirectionsTime_2(SampleDirections_2):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleDirectionsTime_2:
        ...
    def __deepcopy__(self, arg: dict) -> SampleDirectionsTime_2:
        ...
    def __eq__(self, other: SampleDirectionsTime_2) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirections_2, two_way_travel_time: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        __init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, two_way_travel_time: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new SampleDirections object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirections_2, two_way_travel_time: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirections object (from a SampleDirections
        object)
        
        Parameter ``two_way_travel_time``:
            in s, accumulated ray path time
        
        4. ``__init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, two_way_travel_time: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirectionsTime object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
        
        Parameter ``two_way_travel_time``:
            in m, accumulated ray path length
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
    def copy(self) -> SampleDirectionsTime_2:
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
    def two_way_travel_time(self) -> ...:
        """
        < in s, accumulated ray path time
        """
    @two_way_travel_time.setter
    def two_way_travel_time(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in s, accumulated ray path time
        """
class SampleDirectionsTime_3(SampleDirections_3):
    """
    A structure to store beamsample directions (along angle, across angle
    and range).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleDirectionsTime_3:
        ...
    def __deepcopy__(self, arg: dict) -> SampleDirectionsTime_3:
        ...
    def __eq__(self, other: SampleDirectionsTime_3) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirections_3, two_way_travel_time: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        __init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, two_way_travel_time: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new SampleDirections object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new SampleDirections object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirections_3, two_way_travel_time: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirections object (from a SampleDirections
        object)
        
        Parameter ``two_way_travel_time``:
            in s, accumulated ray path time
        
        4. ``__init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, two_way_travel_time: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirectionsTime object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
        
        Parameter ``two_way_travel_time``:
            in m, accumulated ray path length
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
    def copy(self) -> SampleDirectionsTime_3:
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
    def two_way_travel_time(self) -> ...:
        """
        < in s, accumulated ray path time
        """
    @two_way_travel_time.setter
    def two_way_travel_time(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in s, accumulated ray path time
        """
class SampleDirections_1:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleDirections_1:
        ...
    def __deepcopy__(self, arg: dict) -> SampleDirections_1:
        ...
    def __eq__(self, other: SampleDirections_1) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirections object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
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
    def check_shape(self) -> None:
        """
        check if the internal variables have the same shape
        """
    def copy(self) -> SampleDirections_1:
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
    def shape(self) -> list[int]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def alongtrack_angle(self) -> ...:
        """
        < in °, positive bow up, 0 == downwards
        """
    @alongtrack_angle.setter
    def alongtrack_angle(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in °, positive bow up, 0 == downwards
        """
    @property
    def crosstrack_angle(self) -> ...:
        """
        < in °, positive starboard up, 0 == downwards
        """
    @crosstrack_angle.setter
    def crosstrack_angle(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in °, positive starboard up, 0 == downwards
        """
class SampleDirections_2:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleDirections_2:
        ...
    def __deepcopy__(self, arg: dict) -> SampleDirections_2:
        ...
    def __eq__(self, other: SampleDirections_2) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirections object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
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
    def check_shape(self) -> None:
        """
        check if the internal variables have the same shape
        """
    def copy(self) -> SampleDirections_2:
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
    def shape(self) -> list[int]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def alongtrack_angle(self) -> ...:
        """
        < in °, positive bow up, 0 == downwards
        """
    @alongtrack_angle.setter
    def alongtrack_angle(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in °, positive bow up, 0 == downwards
        """
    @property
    def crosstrack_angle(self) -> ...:
        """
        < in °, positive starboard up, 0 == downwards
        """
    @crosstrack_angle.setter
    def crosstrack_angle(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in °, positive starboard up, 0 == downwards
        """
class SampleDirections_3:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleDirections_3:
        ...
    def __deepcopy__(self, arg: dict) -> SampleDirections_3:
        ...
    def __eq__(self, other: SampleDirections_3) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleDirections object
        
        Parameter ``alongtrack_angle``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``crosstrack_angle``:
            in °, positive starboard up, 0 == downwards
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
    def check_shape(self) -> None:
        """
        check if the internal variables have the same shape
        """
    def copy(self) -> SampleDirections_3:
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
    def shape(self) -> list[int]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def alongtrack_angle(self) -> ...:
        """
        < in °, positive bow up, 0 == downwards
        """
    @alongtrack_angle.setter
    def alongtrack_angle(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in °, positive bow up, 0 == downwards
        """
    @property
    def crosstrack_angle(self) -> ...:
        """
        < in °, positive starboard up, 0 == downwards
        """
    @crosstrack_angle.setter
    def crosstrack_angle(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < in °, positive starboard up, 0 == downwards
        """
class SampleIndices_1:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleIndices_1:
        ...
    def __deepcopy__(self, arg: dict) -> SampleIndices_1:
        ...
    def __eq__(self, other: SampleIndices_1) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, beam_numbers: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, sample_numbers: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, beam_numbers: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, sample_numbers: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleIndices object
        
        Parameter ``beam_numbers``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``sample_numbers``:
            in °, positive starboard up, 0 == downwards
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
    def check_shape(self) -> None:
        """
        check if the internal variables have the same shape
        """
    def copy(self) -> SampleIndices_1:
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
    def shape(self) -> list[int]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def beam_numbers(self) -> ...:
        """
        < beam number of each sample
        """
    @beam_numbers.setter
    def beam_numbers(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < beam number of each sample
        """
    @property
    def sample_numbers(self) -> ...:
        """
        < sample number of each sample
        """
    @sample_numbers.setter
    def sample_numbers(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < sample number of each sample
        """
class SampleIndices_2:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleIndices_2:
        ...
    def __deepcopy__(self, arg: dict) -> SampleIndices_2:
        ...
    def __eq__(self, other: SampleIndices_2) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, beam_numbers: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, sample_numbers: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, beam_numbers: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, sample_numbers: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleIndices object
        
        Parameter ``beam_numbers``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``sample_numbers``:
            in °, positive starboard up, 0 == downwards
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
    def check_shape(self) -> None:
        """
        check if the internal variables have the same shape
        """
    def copy(self) -> SampleIndices_2:
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
    def shape(self) -> list[int]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def beam_numbers(self) -> ...:
        """
        < beam number of each sample
        """
    @beam_numbers.setter
    def beam_numbers(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < beam number of each sample
        """
    @property
    def sample_numbers(self) -> ...:
        """
        < sample number of each sample
        """
    @sample_numbers.setter
    def sample_numbers(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < sample number of each sample
        """
class SampleIndices_3:
    """
    A structure to store beamsample directions (along angle, across
    angle).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SampleIndices_3:
        ...
    def __deepcopy__(self, arg: dict) -> SampleIndices_3:
        ...
    def __eq__(self, other: SampleIndices_3) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, beam_numbers: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, sample_numbers: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, beam_numbers: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, sample_numbers: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new SampleIndices object
        
        Parameter ``beam_numbers``:
            in °, positive bow up, 0 == downwards
        
        Parameter ``sample_numbers``:
            in °, positive starboard up, 0 == downwards
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
    def check_shape(self) -> None:
        """
        check if the internal variables have the same shape
        """
    def copy(self) -> SampleIndices_3:
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
    def shape(self) -> list[int]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def beam_numbers(self) -> ...:
        """
        < beam number of each sample
        """
    @beam_numbers.setter
    def beam_numbers(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < beam number of each sample
        """
    @property
    def sample_numbers(self) -> ...:
        """
        < sample number of each sample
        """
    @sample_numbers.setter
    def sample_numbers(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<unsigned short, xsimd::aligned_allocator<unsigned short, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < sample number of each sample
        """
class XYZ_1:
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) and z (depth). These
    coordinates can be converted to UTM or Lat/Lon if a reference position
    (for coordinate 0) is known.
    """
    concat: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def rotate(*args, **kwargs) -> None:
        """
        rotate(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None
        
        Overloaded function.
        
        1. ``rotate(self, quat: Eigen::Quaternion<float, 0>) -> None``
        
        Rotate the XYZ object using a quaternion
        
        Parameter ``q``:
            quaternion
        
        2. ``rotate(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None``
        
        Rotate the XYZ object using yaw, pitch, roll in °
        
        Parameter ``yaw``:
            in °
        
        Parameter ``pitch``:
            in °
        
        Parameter ``roll``:
            in °
        """
    def __copy__(self) -> XYZ_1:
        ...
    def __deepcopy__(self, arg: dict) -> XYZ_1:
        ...
    def __eq__(self, other: XYZ_1) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, x: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, y: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, z: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, x: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, y: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, z: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new XYZ object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
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
    def copy(self) -> XYZ_1:
        """
        return a copy using the c++ default copy constructor
        """
    def get_minmax_x(self) -> list[float]:
        ...
    def get_minmax_y(self) -> list[float]:
        ...
    def get_minmax_z(self) -> list[float]:
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
    def shape(self) -> list[int]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    def to_latlon(self, utm_zone: int, northern_hemisphere: bool) -> ...:
        ...
    def translate(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        ...
    @property
    def x(self) -> ...:
        """
        < x coordinate in m, positive forward
        """
    @x.setter
    def x(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < x coordinate in m, positive forward
        """
    @property
    def y(self) -> ...:
        """
        < y coordinate in m, positive starboard
        """
    @y.setter
    def y(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < y coordinate in m, positive starboard
        """
    @property
    def z(self) -> ...:
        """
        < z coordinate in m, positive downwards
        """
    @z.setter
    def z(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < z coordinate in m, positive downwards
        """
class XYZ_2:
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) and z (depth). These
    coordinates can be converted to UTM or Lat/Lon if a reference position
    (for coordinate 0) is known.
    """
    concat: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def rotate(*args, **kwargs) -> None:
        """
        rotate(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None
        
        Overloaded function.
        
        1. ``rotate(self, quat: Eigen::Quaternion<float, 0>) -> None``
        
        Rotate the XYZ object using a quaternion
        
        Parameter ``q``:
            quaternion
        
        2. ``rotate(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None``
        
        Rotate the XYZ object using yaw, pitch, roll in °
        
        Parameter ``yaw``:
            in °
        
        Parameter ``pitch``:
            in °
        
        Parameter ``roll``:
            in °
        """
    def __copy__(self) -> XYZ_2:
        ...
    def __deepcopy__(self, arg: dict) -> XYZ_2:
        ...
    def __eq__(self, other: XYZ_2) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, x: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, y: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, z: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, x: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, y: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, z: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new XYZ object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
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
    def copy(self) -> XYZ_2:
        """
        return a copy using the c++ default copy constructor
        """
    def get_minmax_x(self) -> list[float]:
        ...
    def get_minmax_y(self) -> list[float]:
        ...
    def get_minmax_z(self) -> list[float]:
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
    def shape(self) -> list[int]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    def to_latlon(self, utm_zone: int, northern_hemisphere: bool) -> ...:
        ...
    def translate(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        ...
    @property
    def x(self) -> ...:
        """
        < x coordinate in m, positive forward
        """
    @x.setter
    def x(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < x coordinate in m, positive forward
        """
    @property
    def y(self) -> ...:
        """
        < y coordinate in m, positive starboard
        """
    @y.setter
    def y(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < y coordinate in m, positive starboard
        """
    @property
    def z(self) -> ...:
        """
        < z coordinate in m, positive downwards
        """
    @z.setter
    def z(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < z coordinate in m, positive downwards
        """
class XYZ_3:
    """
    A structure to store a georeferenced sample location. It is used as
    output for the raytracers functions. This object stores local x
    (forward coordinate), y (starboard coordinate) and z (depth). These
    coordinates can be converted to UTM or Lat/Lon if a reference position
    (for coordinate 0) is known.
    """
    concat: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def rotate(*args, **kwargs) -> None:
        """
        rotate(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None
        
        Overloaded function.
        
        1. ``rotate(self, quat: Eigen::Quaternion<float, 0>) -> None``
        
        Rotate the XYZ object using a quaternion
        
        Parameter ``q``:
            quaternion
        
        2. ``rotate(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None``
        
        Rotate the XYZ object using yaw, pitch, roll in °
        
        Parameter ``yaw``:
            in °
        
        Parameter ``pitch``:
            in °
        
        Parameter ``roll``:
            in °
        """
    def __copy__(self) -> XYZ_3:
        ...
    def __deepcopy__(self, arg: dict) -> XYZ_3:
        ...
    def __eq__(self, other: XYZ_3) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self) -> None:
        """
        __init__(self, shape: collections.abc.Sequence[int]) -> None
        __init__(self, x: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, y: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, z: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None
        
        Overloaded function.
        
        1. ``__init__(self) -> None``
        
        Construct a new sample location object (all values set to 0)
        
        2. ``__init__(self, shape: collections.abc.Sequence[int]) -> None``
        
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``shape``:
            shape of the internal tensors
        
        3. ``__init__(self, x: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, y: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, z: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>) -> None``
        
        Construct a new XYZ object
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
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
    def copy(self) -> XYZ_3:
        """
        return a copy using the c++ default copy constructor
        """
    def get_minmax_x(self) -> list[float]:
        ...
    def get_minmax_y(self) -> list[float]:
        ...
    def get_minmax_z(self) -> list[float]:
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
    def shape(self) -> list[int]:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    def to_latlon(self, utm_zone: int, northern_hemisphere: bool) -> ...:
        ...
    def translate(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        ...
    @property
    def x(self) -> ...:
        """
        < x coordinate in m, positive forward
        """
    @x.setter
    def x(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < x coordinate in m, positive forward
        """
    @property
    def y(self) -> ...:
        """
        < y coordinate in m, positive starboard
        """
    @y.setter
    def y(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < y coordinate in m, positive starboard
        """
    @property
    def z(self) -> ...:
        """
        < z coordinate in m, positive downwards
        """
    @z.setter
    def z(*args, **kwargs):
        """
        (self, arg: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 3ul, (xt::layout_type)1, xt::xtensor_expression_tag>, /) -> None
        
        < z coordinate in m, positive downwards
        """
