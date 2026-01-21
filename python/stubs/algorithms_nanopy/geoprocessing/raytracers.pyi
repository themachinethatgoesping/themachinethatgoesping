from typing import overload

import themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures
import themachinethatgoesping.navigation_nanopy.datastructures


class I_Raytracer:
    def __init__(self, sensor_location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, raytracer_name: str) -> None: ...

    def __eq__(self, other: I_Raytracer) -> bool: ...

    def trace_point(self, two_way_travel_time: float, alongtrack_angle: float, crosstrack_angle: float) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResult:
        """
        Trace the location of a single point.

        Args:
            two_way_travel_time: Two way travel time in s
            alongtrack_angle: Along track angle in °
            crosstrack_angle: Across track angle in °

        Returns:
            datastructures::RaytraceResult
        """

    @overload
    def trace_points(self, two_way_travel_times: "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>", alongtrack_angles: "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>", crosstrack_angles: "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>", mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1:
        """
        Trace the location of a set of points.

        Args:
            two_way_travel_time: Two way travel time in s
            alongtrack_angle: Along track angle in °
            crosstrack_angles: Across track angle in °
            mp_cores: Number of cores to use for parallelization

        Returns:
            datastructures::RaytraceResult
        """

    @overload
    def trace_points(self, sample_directions: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.SampleDirectionsTime_1, mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1:
        """
        Trace the location of a set of points.

        Args:
            sampledirections: One dimensional sample directions array
            mp_cores: Number of cores to use for parallelization

        Returns:
            datastructures::RaytraceResult
        """

    @overload
    def trace_beam(self, sample_numbers: "xt::xtensor_container_xt_uvector<unsignedint_xsimd_aligned_allocator<unsignedint_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>", sampling_time: float, sampling_time_offset: float, alongtrack_angle: float, crosstrack_angle: float) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1:
        """
        Trace the sample locations of a single beam.

        Args:
            sample_numbers: Sample numbers to trace (starting from 0)
            sampling_time: Time betweens samples in s
            sampling_time_offset: Time offset for sample number 0 in s
            alongtrack_angle: Along track angle in °
            crosstrack_angle: Across track angle in °

        Returns:
            datastructures::RaytraceResults_1
        """

    @overload
    def trace_beam(self, first_sample_number: int, number_of_samples: int, sample_step: int, sampling_time: float, sampling_time_offset: float, alongtrack_angle: float, crosstrack_angle: float) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1:
        """
        Trace the sample locations of a single beam.

        Args:
            first_sample_number: First sample number to trace
            number_of_samples: Number of samples to trace
            sample_step: Step between samples
            sampling_time: Time betweens samples in s
            sampling_time_offset: Time offset for sample number 0 in s
            alongtrack_angle: Along track angle in °
            crosstrack_angle: Across track angle in °

        Returns:
            datastructures::RaytraceResults_1
        """

    @overload
    def trace_swath(self, sample_numbers: "xt::xtensor_container_xt_uvector<unsignedint_xsimd_aligned_allocator<unsignedint_16ul >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>", sampling_time: float, sampling_time_offset: float, alongtrack_angle: "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>", crosstrack_angles: "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>", mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_2:
        """
        Trace the sample locations of a multiple beams in a swath.
        Note: a 2d Array for sample numbers is expected where the first
              dimension is the beam and the
        second dimension is the sample number. The beam dimension must be the
        same as for "crosstrack_angles"

        Args:
            sample_numbers: Sample numbers to trace (starting from 0)
            sampling_time: Time betweens samples in s
            sampling_time_offset: Time offset for sample number 0 in s
            alongtrack_angle: Along track angle of the swath in °
            crosstrack_angles: Across track angle of each beam in °
            mp_cores: Number of cores to use for parallelization

        Returns:
            datastructures::RaytraceResults_2
        """

    @overload
    def trace_swath(self, first_sample_number: int, number_of_samples: int, sample_step: int, sampling_time: float, sampling_time_offset: float, alongtrack_angles: "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>", crosstrack_angles: "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>", mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_2:
        """
        Trace the sample locations of a multiple beams in a swath.
        Note: The number of beams is controlled by the dimension of
              crosstrack_angles

        Args:
            first_sample_number: First sample number to trace
            number_of_samples: Number of samples to trace
            sample_step: Step between samples
            sampling_time: Time betweens samples in s
            sampling_time_offset: Time offset for sample number 0 in s
            alongtrack_angle: Along track angle of the swath in °
            crosstrack_angles: Across track angle of each beam in °
            mp_cores: Number of cores to use for parallelization

        Returns:
            datastructures::RaytraceResults_2
        """

    def set_sensor_location(self, sensor_location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation) -> None: ...

    def get_sensor_location(self) -> themachinethatgoesping.navigation_nanopy.datastructures.Geolocation: ...

    def get_sensor_orientation_quat_ypr(self) -> list[float]: ...

    def copy(self) -> I_Raytracer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> I_Raytracer: ...

    def __deepcopy__(self, arg: dict, /) -> I_Raytracer: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> I_Raytracer:
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

class RTConstantSVP(I_Raytracer):
    def __init__(self, sensor_location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, sound_velocity: float) -> None:
        """
        Construct a new RTConstantSVP object

        Args:
            sensor_location: Orientation and depth of the echo sounder
            sound_velocity: Sound velocity in m/s
        """

    def __eq__(self, other: RTConstantSVP) -> bool: ...

    def scale_beam(self, sample_numbers: "xt::xtensor_container_xt_uvector<unsignedint_xsimd_aligned_allocator<unsignedint_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>", sampling_time: float, sampling_time_offset: float, scale_x: float, scale_y: float, scale_z: float, scale_true_range: float, scale_time: float) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1:
        """
        Compute the sample locations of a single beam by scaling between the
        transducer location and a known target location

        Args:
            sample_numbers: Sample numbers to trace (starting from 0)
            sampling_time: Time betweens samples in s
            sampling_time_offset: Time offset for sample number 0 in s
            scale_x: known target x position at scale_time
            scale_y: known target y position at scale_time
            scale_z: known target z position at scale_time
            scale_true_range: known target range at scale_time
            scale_time: known target two way travel time

        Returns:
            datastructures::RaytraceResults_1
        """

    def scale_swath(self, sample_numbers: "xt::xtensor_container_xt_uvector<unsignedint_xsimd_aligned_allocator<unsignedint_16ul >, 2ul, (xt::layout_type)1, xt::xtensor_expression_tag>", sampling_time: float, sampling_time_offset: float, scale_targets: themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_1, scale_times: "xt::xtensor_container_xt_uvector<float_xsimd_aligned_allocator<float_16ul >, 1ul, (xt::layout_type)1, xt::xtensor_expression_tag>", mp_cores: int = 1) -> themachinethatgoesping.algorithms_nanopy.geoprocessing.datastructures.RaytraceResults_2:
        """
        Compute the sample locations of a swath by scaling between the
        transducer location and known target locations

        Args:
            sample_numbers: Sample numbers to trace (starting from 0)
            sampling_time: Time betweens samples in s
            sampling_time_offset: Time offset for sample number 0 in s
            scale_target: known target location at scale_time
            scale_time: two way travel time for the known target location
            mp_cores: number of cores to use for parallelization

        Returns:
            datastructures::RaytraceResults_1
        """

    def copy(self) -> RTConstantSVP:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> RTConstantSVP: ...

    def __deepcopy__(self, arg: dict, /) -> RTConstantSVP: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> RTConstantSVP:
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
