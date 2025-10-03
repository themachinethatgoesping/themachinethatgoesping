"""
Submodule for backtracing echo sounder sample locations to beamangle and twoway traveltime
"""
from __future__ import annotations
import themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures
import themachinethatgoesping.navigation_nanopy.datastructures
import themachinethatgoesping.tools_nanopy.vectorinterpolators
import typing
__all__: list[str] = ['BTConstantSVP', 'BacktracedWCI', 'I_Backtracer']
class BTConstantSVP(I_Backtracer):
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> BTConstantSVP:
        ...
    def __deepcopy__(self, arg: dict) -> BTConstantSVP:
        ...
    def __eq__(self, other: BTConstantSVP) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, sensor_location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, sensor_x: float, sensor_y: float) -> None:
        """
        Construct a new BTConstantSVP object
        
        Parameter ``sensor_location``:
            Orientation and depth of the echo sounder
        
        Parameter ``sound_velocity``:
            Sound velocity in m/s
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
    def copy(self) -> BTConstantSVP:
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
class BacktracedWCI:
    """
    A structure to store a watercolumn image together with the necessary
    informations for raytracing.
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __init__(*args, **kwargs) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))
        
        Parameter ``wci``:
            Water column image, shape: len(beam_reference_directions) x does
            not matter
        
        Parameter ``beam_reference_directions``:
            beam reference directions: reference points that describe beam
            angle and reference range for each beam
        """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> BacktracedWCI:
        ...
    def __deepcopy__(self, arg: dict) -> BacktracedWCI:
        ...
    def __eq__(self, other: BacktracedWCI) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
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
    def copy(self) -> BacktracedWCI:
        """
        return a copy using the c++ default copy constructor
        """
    def get_angle_beamnumber_interpolator(self) -> ...:
        ...
    def get_max_angle(self) -> float:
        ...
    def get_min_angle(self) -> float:
        ...
    def get_range_samplenumber_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolatorF]:
        ...
    def get_wci(self) -> ...:
        ...
    def get_wci_first_sample_number(self) -> int:
        ...
    def get_wci_first_sample_number_internal(self) -> int:
        """
        Get the internally saved wci first sample number. Internally: the
        first_sample_number of the image is divided by sample_number_step
        
        Returns:
            uint16_t
        """
    def get_wci_sample_number_step(self) -> int:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def lookup(self, beam_angle: float, range: float) -> float:
        ...
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def shape(self) -> ...:
        ...
    def size(self) -> int:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class I_Backtracer:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def backtrace_image(*args, **kwargs) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_2:
        """
        Backtrace the location of an image specified by two coordinate vectors
        x is assumed to be 0
        
        Parameter ``y_coordinates``:
            in m, positive starboard
        
        Parameter ``z_coordinates``:
            in m, positive downwards
        
        Parameter ``mp_cores``:
            Number of cores to use for parallelization
        
        Returns:
            datastructures::SampleDirectionsRange<2>, shape is
            (y_coordinates.size(), z_coordinates.size())
        """
    @staticmethod
    def backtrace_points(*args, **kwargs) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_1:
        """
        backtrace_points(self, xyz: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1, mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_1
        
        Backtrace the location of a set of points.
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
        
        Parameter ``mp_cores``:
            Number of cores to use for parallelization
        
        Returns:
            datastructures::SampleDirectionsRange
        """
    @staticmethod
    def lookup(*args, **kwargs) -> ...:
        ...
    def __copy__(self) -> I_Backtracer:
        ...
    def __deepcopy__(self, arg: dict) -> I_Backtracer:
        ...
    def __eq__(self, other: I_Backtracer) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, sensor_location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, sensor_x: float, sensor_y: float, backtracer_name: str) -> None:
        ...
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
    def copy(self) -> I_Backtracer:
        """
        return a copy using the c++ default copy constructor
        """
    def get_sensor_location(self) -> themachinethatgoesping.navigation_nanopy.datastructures.Geolocation:
        ...
    def get_sensor_orientation_quat_ypr(self) -> ...:
        ...
    def get_sensor_x(self) -> float:
        ...
    def get_sensor_y(self) -> float:
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
    def set_sensor_location(self, sensor_location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, sensor_x: float, sensor_y: float) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
