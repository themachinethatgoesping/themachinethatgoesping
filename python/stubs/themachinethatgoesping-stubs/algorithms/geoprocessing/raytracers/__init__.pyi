"""Submodule for raytracing echo sounder sample locations"""
from __future__ import annotations
import themachinethatgoesping.algorithms.geoprocessing.raytracers
import typing
import numpy
import pybind11_stubgen.typing_ext
import themachinethatgoesping.algorithms.geoprocessing.datastructures
_Shape = typing.Tuple[int, ...]

__all__ = [
    "I_Raytracer",
    "RTConstantSVP"
]


class I_Raytracer():
    def __copy__(self) -> I_Raytracer: ...
    def __deepcopy__(self, arg0: dict) -> I_Raytracer: ...
    def __eq__(self, other: I_Raytracer) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @staticmethod
    def __init__(*args, **kwargs) -> typing.Any: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> I_Raytracer: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> I_Raytracer: 
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def get_sensor_location(*args, **kwargs) -> typing.Any: ...
    def get_sensor_orientation_quat_ypr(self) -> typing.Annotated[typing.List[float], pybind11_stubgen.typing_ext.FixedSize(3)]: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @staticmethod
    def set_sensor_location(*args, **kwargs) -> typing.Any: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @typing.overload
    def trace_beam(self, sample_numbers: numpy.ndarray[numpy.uint32], sampling_time: float, sampling_time_offset: float, alongtrack_angle: float, crosstrack_angle: float) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleLocationsLocal_1: 
        """
        Trace the sample locations of a single beam.

        Parameter ``sample_numbers``:
            Sample numbers to trace (starting from 0)

        Parameter ``sampling_time``:
            Time betweens samples in s

        Parameter ``sampling_time_offset``:
            Time offset for sample number 0 in s

        Parameter ``alongtrack_angle``:
            Along track angle in °

        Parameter ``crosstrack_angle``:
            Across track angle in °

        Returns:
            datastructures::SamplelocationsLocal<1>

        Trace the sample locations of a single beam.

        Parameter ``sample_numbers``:
            Sample numbers to trace (starting from 0)

        Parameter ``sampling_time``:
            Time betweens samples in s

        Parameter ``sampling_time_offset``:
            Time offset for sample number 0 in s

        Parameter ``alongtrack_angle``:
            Along track angle in °

        Parameter ``crosstrack_angle``:
            Across track angle in °

        Returns:
            datastructures::SamplelocationsLocal<1>
        """
    @typing.overload
    def trace_beam(self, first_sample_number: int, number_of_samples: int, sample_step: int, sampling_time: float, sampling_time_offset: float, alongtrack_angle: float, crosstrack_angle: float) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleLocationsLocal_1: ...
    def trace_point(self, two_way_travel_time: float, alongtrack_angle: float, crosstrack_angle: float) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleLocationLocal: 
        """
        Trace the location of a single point.

        Parameter ``two_way_travel_time``:
            Two way travel time in s

        Parameter ``alongtrack_angle``:
            Along track angle in °

        Parameter ``crosstrack_angle``:
            Across track angle in °

        Returns:
            datastructures::SampleLocationLocal
        """
    @typing.overload
    def trace_points(self, two_way_travel_times: numpy.ndarray[numpy.float32], alongtrack_angles: numpy.ndarray[numpy.float32], crosstrack_angles: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleLocationsLocal_1: 
        """
        Trace the location of a set of points.

        Parameter ``two_way_travel_time``:
            Two way travel time in s

        Parameter ``alongtrack_angle``:
            Along track angle in °

        Parameter ``crosstrack_angles``:
            Across track angle in °

        Parameter ``mp_cores``:
            Number of cores to use for parallelization

        Returns:
            datastructures::SampleLocationLocal

        Trace the location of a set of points.

        Parameter ``two_way_travel_time``:
            Two way travel time in s

        Parameter ``alongtrack_angle``:
            Along track angle of all beams in °

        Parameter ``crosstrack_angles``:
            Across track angle in °

        Parameter ``mp_cores``:
            Number of cores to use for parallelization

        Returns:
            datastructures::SampleLocationLocal
        """
    @typing.overload
    def trace_points(self, two_way_travel_times: numpy.ndarray[numpy.float32], alongtrack_angle: float, crosstrack_angles: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleLocationsLocal_1: ...
    @typing.overload
    def trace_swath(self, sample_numbers: numpy.ndarray[numpy.uint32], sampling_time: float, sampling_time_offset: float, alongtrack_angle: float, crosstrack_angles: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleLocationsLocal_2: 
        """
        Trace the sample locations of a multiple beams in a swath. Note: a 2d
        Array for sample numbers is expected where the first dimension is the
        beam and the second dimension is the sample number. The beam dimension
        must be the same as for "crosstrack_angles"

        Parameter ``sample_numbers``:
            Sample numbers to trace (starting from 0)

        Parameter ``sampling_time``:
            Time betweens samples in s

        Parameter ``sampling_time_offset``:
            Time offset for sample number 0 in s

        Parameter ``alongtrack_angle``:
            Along track angle of the swath in °

        Parameter ``crosstrack_angles``:
            Across track angle of each beam in °

        Parameter ``mp_cores``:
            Number of cores to use for parallelization

        Returns:
            datastructures::SamplelocationsLocal<2>

        Trace the sample locations of a multiple beams in a swath. Note: a 2d
        Array for sample numbers is expected where the first dimension is the
        beam and the second dimension is the sample number. The beam dimension
        must be the same as for "crosstrack_angles"

        Parameter ``sample_numbers``:
            Sample numbers to trace (starting from 0)

        Parameter ``sampling_time``:
            Time betweens samples in s

        Parameter ``sampling_time_offset``:
            Time offset for sample number 0 in s

        Parameter ``alongtrack_angle``:
            Along track angle of the swath in °

        Parameter ``crosstrack_angles``:
            Across track angle of each beam in °

        Parameter ``mp_cores``:
            Number of cores to use for parallelization

        Returns:
            datastructures::SamplelocationsLocal<2>
        """
    @typing.overload
    def trace_swath(self, first_sample_number: int, number_of_samples: int, sample_step: int, sampling_time: float, sampling_time_offset: float, alongtrack_angle: float, crosstrack_angles: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleLocationsLocal_2: ...
    pass
class RTConstantSVP(I_Raytracer):
    def __copy__(self) -> RTConstantSVP: ...
    def __deepcopy__(self, arg0: dict) -> RTConstantSVP: ...
    def __eq__(self, other: RTConstantSVP) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __hash__(self) -> int: 
        """
        hash function implemented using slow_hash
        """
    @staticmethod
    def __init__(*args, **kwargs) -> typing.Any: 
        """
        Construct a new RTConstantSVP object

        Parameter ``sensor_location``:
            Orientation and depth of the echo sounder

        Parameter ``sound_velocity``:
            Sound velocity in m/s
        """
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> RTConstantSVP: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RTConstantSVP: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @typing.overload
    def scale_beam(self, sample_numbers: numpy.ndarray[numpy.uint32], sampling_time: float, sampling_time_offset: float, scale_true_range: float, scale_x: float, scale_y: float, scale_z: float, scale_time: float) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleLocationsLocal_1: 
        """
        Compute the sample locations of a single beam by scaling between the
        transducer location and a known target location

        Parameter ``sample_numbers``:
            Sample numbers to trace (starting from 0)

        Parameter ``sampling_time``:
            Time betweens samples in s

        Parameter ``sampling_time_offset``:
            Time offset for sample number 0 in s

        Parameter ``scale_true_range``:
            known target range at scale_time

        Parameter ``scale_x``:
            known target x position at scale_time

        Parameter ``scale_y``:
            known target y position at scale_time

        Parameter ``scale_z``:
            known target z position at scale_time

        Parameter ``scale_time``:
            known target two way travel time

        Returns:
            datastructures::SamplelocationsLocal<1>

        Compute the sample locations of a single beam by scaling between the
        transducer location and a known target location

        Parameter ``sample_numbers``:
            Sample numbers to trace (starting from 0)

        Parameter ``sampling_time``:
            Time betweens samples in s

        Parameter ``sampling_time_offset``:
            Time offset for sample number 0 in s

        Parameter ``scale_target``:
            known target location at scale_time

        Parameter ``scale_time``:
            known target two way travel time

        Returns:
            datastructures::SamplelocationsLocal<1>
        """
    @typing.overload
    def scale_beam(self, sample_numbers: numpy.ndarray[numpy.uint32], sampling_time: float, sampling_time_offset: float, scale_target: themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleLocationLocal, scale_time: float) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleLocationsLocal_1: ...
    def scale_swath(self, sample_numbers: numpy.ndarray[numpy.uint32], sampling_time: float, sampling_time_offset: float, scale_target: themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleLocationsLocal_1, scale_time: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> themachinethatgoesping.algorithms.geoprocessing.datastructures.SampleLocationsLocal_2: 
        """
        Compute the sample locations of a swath by scaling between the
        transducer location and known target locations

        Parameter ``sample_numbers``:
            Sample numbers to trace (starting from 0)

        Parameter ``sampling_time``:
            Time betweens samples in s

        Parameter ``sampling_time_offset``:
            Time offset for sample number 0 in s

        Parameter ``scale_target``:
            known target location at scale_time

        Parameter ``scale_time``:
            two way travel time for the known target location

        Parameter ``mp_cores``:
            number of cores to use for parallelization

        Returns:
            datastructures::SamplelocationsLocal<1>
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    pass
