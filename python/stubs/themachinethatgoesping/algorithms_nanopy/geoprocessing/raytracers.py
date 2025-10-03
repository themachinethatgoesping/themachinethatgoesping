"""
Submodule for raytracing echo sounder sample locations
"""
from __future__ import annotations
import themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures
import themachinethatgoesping.navigation_nanopy.datastructures
import typing
__all__: list[str] = ['I_Raytracer', 'RTConstantSVP']
class I_Raytracer:
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def trace_beam(*args, **kwargs) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1:
        """
        trace_beam(self, first_sample_number: int, number_of_samples: int, sample_step: int, sampling_time: float, sampling_time_offset: float, alongtrack_angle: float, crosstrack_angle: float) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1
        
        Overloaded function.
        
        1. ``trace_beam(self, sample_numbers: xt::xtensor_container<xt::uvector<unsigned int, xsimd::aligned_allocator<unsigned int, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, sampling_time: float, sampling_time_offset: float, alongtrack_angle: float, crosstrack_angle: float) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1``
        
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
            datastructures::RaytraceResults<1>
        
        2. ``trace_beam(self, first_sample_number: int, number_of_samples: int, sample_step: int, sampling_time: float, sampling_time_offset: float, alongtrack_angle: float, crosstrack_angle: float) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1``
        
        Trace the sample locations of a single beam.
        
        Parameter ``first_sample_number``:
            First sample number to trace
        
        Parameter ``number_of_samples``:
            Number of samples to trace
        
        Parameter ``sample_step``:
            Step between samples
        
        Parameter ``sampling_time``:
            Time betweens samples in s
        
        Parameter ``sampling_time_offset``:
            Time offset for sample number 0 in s
        
        Parameter ``alongtrack_angle``:
            Along track angle in °
        
        Parameter ``crosstrack_angle``:
            Across track angle in °
        
        Returns:
            datastructures::RaytraceResults<1>
        """
    @staticmethod
    def trace_points(*args, **kwargs) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1:
        """
        trace_points(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsTime_1, mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1
        
        Overloaded function.
        
        1. ``trace_points(self, two_way_travel_times: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, alongtrack_angles: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angles: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1``
        
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
            datastructures::RaytraceResult
        
        2. ``trace_points(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsTime_1, mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1``
        
        Trace the location of a set of points.
        
        Parameter ``sampledirections``:
            One dimensional sample directions array
        
        Parameter ``mp_cores``:
            Number of cores to use for parallelization
        
        Returns:
            datastructures::RaytraceResult
        """
    @staticmethod
    def trace_swath(*args, **kwargs) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_2:
        """
        trace_swath(self, first_sample_number: int, number_of_samples: int, sample_step: int, sampling_time: float, sampling_time_offset: float, alongtrack_angles: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angles: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_2
        
        Overloaded function.
        
        1. ``trace_swath(self, sample_numbers: xt::xtensor_container<xt::uvector<unsigned int, xsimd::aligned_allocator<unsigned int, 16ul> >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>, sampling_time: float, sampling_time_offset: float, alongtrack_angle: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angles: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_2``
        
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
            datastructures::RaytraceResults<2>
        
        2. ``trace_swath(self, first_sample_number: int, number_of_samples: int, sample_step: int, sampling_time: float, sampling_time_offset: float, alongtrack_angles: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, crosstrack_angles: xt::xtensor_container<xt::uvector<float, xsimd::aligned_allocator<float, 16ul> >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>, mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_2``
        
        Trace the sample locations of a multiple beams in a swath. Note: The
        number of beams is controlled by the dimension of crosstrack_angles
        
        Parameter ``first_sample_number``:
            First sample number to trace
        
        Parameter ``number_of_samples``:
            Number of samples to trace
        
        Parameter ``sample_step``:
            Step between samples
        
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
            datastructures::RaytraceResults<2>
        """
    def __copy__(self) -> I_Raytracer:
        ...
    def __deepcopy__(self, arg: dict) -> I_Raytracer:
        ...
    def __eq__(self, other: I_Raytracer) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, sensor_location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, raytracer_name: str) -> None:
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
    def copy(self) -> I_Raytracer:
        """
        return a copy using the c++ default copy constructor
        """
    def get_sensor_location(self) -> themachinethatgoesping.navigation_nanopy.datastructures.Geolocation:
        ...
    def get_sensor_orientation_quat_ypr(self) -> ...:
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
    def set_sensor_location(self, sensor_location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    def trace_point(self, two_way_travel_time: float, alongtrack_angle: float, crosstrack_angle: float) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResult:
        """
        Trace the location of a single point.
        
        Parameter ``two_way_travel_time``:
            Two way travel time in s
        
        Parameter ``alongtrack_angle``:
            Along track angle in °
        
        Parameter ``crosstrack_angle``:
            Across track angle in °
        
        Returns:
            datastructures::RaytraceResult
        """
class RTConstantSVP(I_Raytracer):
    """
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def scale_beam(*args, **kwargs) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1:
        """
        Compute the sample locations of a single beam by scaling between the
        transducer location and a known target location
        
        Parameter ``sample_numbers``:
            Sample numbers to trace (starting from 0)
        
        Parameter ``sampling_time``:
            Time betweens samples in s
        
        Parameter ``sampling_time_offset``:
            Time offset for sample number 0 in s
        
        Parameter ``scale_x``:
            known target x position at scale_time
        
        Parameter ``scale_y``:
            known target y position at scale_time
        
        Parameter ``scale_z``:
            known target z position at scale_time
        
        Parameter ``scale_true_range``:
            known target range at scale_time
        
        Parameter ``scale_time``:
            known target two way travel time
        
        Returns:
            datastructures::RaytraceResults<1>
        """
    @staticmethod
    def scale_swath(*args, **kwargs) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_2:
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
            datastructures::RaytraceResults<1>
        """
    def __copy__(self) -> RTConstantSVP:
        ...
    def __deepcopy__(self, arg: dict) -> RTConstantSVP:
        ...
    def __eq__(self, other: RTConstantSVP) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, sensor_location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, sound_velocity: float) -> None:
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
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> RTConstantSVP:
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
