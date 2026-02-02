"""
Submodule for backtracing echo sounder sample locations to beamangle and twoway traveltime
"""

from collections.abc import Sequence
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

import themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures
import themachinethatgoesping.navigation_nanopy.datastructures
import themachinethatgoesping.tools_nanopy.vectorinterpolators


class BacktracedWCI:
    """
    A structure to store a watercolumn image together with the necessary
    informations for raytracing.
    """

    def __init__(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_reference_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_1, beam_reference_sample_numbers: Sequence[int], wci_first_sample_number: int, wci_sample_number_step: int = 1) -> None:
        """
        Construct a new sample location object (initialize all tensors using
        the specified shape (empty))

        Args:
            wci: Water column image, shape: len(beam_reference_directions) x
                 does not matter
            beam_reference_directions: beam reference directions: reference
                                       points that describe beam angle and
                                       reference range for each beam
        """

    def __eq__(self, other: BacktracedWCI) -> bool: ...

    def lookup(self, beam_angle: float, range: float) -> float: ...

    def size(self) -> int: ...

    def shape(self) -> list[int]: ...

    def get_wci(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    def get_angle_beamnumber_interpolator(self) -> "themachinethatgoesping::tools::vectorinterpolators::NearestInterpolator_float_unsignedshort": ...

    def get_range_samplenumber_interpolators(self) -> list[themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolatorF]: ...

    def get_min_angle(self) -> float: ...

    def get_max_angle(self) -> float: ...

    def get_wci_first_sample_number(self) -> int: ...

    def get_wci_first_sample_number_internal(self) -> int:
        """
        Get the internally saved wci first sample number.
               Internally: the first_sample_number of the image is divided by
                           sample_number_step

        Returns:
            uint16_t
        """

    def get_wci_sample_number_step(self) -> int: ...

    def copy(self) -> BacktracedWCI:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BacktracedWCI: ...

    def __deepcopy__(self, arg: dict, /) -> BacktracedWCI: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BacktracedWCI:
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

class I_Backtracer:
    def __init__(self, sensor_location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, sensor_x: float, sensor_y: float, backtracer_name: str) -> None: ...

    def __eq__(self, other: I_Backtracer) -> bool: ...

    @overload
    def backtrace_points(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_1:
        """
        Backtrace the location of a set of points.

        Args:
            x: in m, positive forward
            y: in m, positive starboard
            z: in m, positive downwards
            mp_cores: Number of cores to use for parallelization

        Returns:
            datastructures::SampleDirectionsRange
        """

    @overload
    def backtrace_points(self, xyz: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.XYZ_1, mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_1: ...

    def backtrace_image(self, y_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], z_coordinates: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_2:
        """
        Backtrace the location of an image specified by two coordinate vectors
        x is assumed to be 0

        Args:
            y_coordinates: in m, positive starboard
            z_coordinates: in m, positive downwards
            mp_cores: Number of cores to use for parallelization

        Returns:
            datastructures::SampleDirectionsRange_2, shape is
                           (y_coordinates.size(), z_coordinates.size())
        """

    def lookup(self, wci: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], beam_reference_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_1, beam_reference_sample_numbers: Sequence[int], target_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsRange_2, wci_first_sample_number: int, wci_sample_number_step: int = 1, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]: ...

    def set_sensor_location(self, sensor_location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, sensor_x: float, sensor_y: float) -> None: ...

    def get_sensor_x(self) -> float: ...

    def get_sensor_y(self) -> float: ...

    def get_sensor_location(self) -> themachinethatgoesping.navigation_nanopy.datastructures.Geolocation: ...

    def get_sensor_orientation_quat_ypr(self) -> list[float]: ...

    def copy(self) -> I_Backtracer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> I_Backtracer: ...

    def __deepcopy__(self, arg: dict, /) -> I_Backtracer: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> I_Backtracer:
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

class BTConstantSVP(I_Backtracer):
    def __init__(self, sensor_location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, sensor_x: float, sensor_y: float) -> None:
        """
        Construct a new BTConstantSVP object

        Args:
            sensor_location: Orientation and depth of the echo sounder
            sound_velocity: Sound velocity in m/s
        """

    def __eq__(self, other: BTConstantSVP) -> bool: ...

    def copy(self) -> BTConstantSVP:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BTConstantSVP: ...

    def __deepcopy__(self, arg: dict, /) -> BTConstantSVP: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BTConstantSVP:
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
