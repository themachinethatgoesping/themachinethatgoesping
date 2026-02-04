"""Python module to store, interpolate and transform navigation data"""
import typing

from collections.abc import Sequence, Set
import enum
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

from . import (
    datastructures as datastructures,
    navtools as navtools,
    nmea_0183 as nmea_0183
)
import themachinethatgoesping.tools_nanopy.vectorinterpolators


class t_latlon_format(enum.Enum):
    """lat/lon format specifications"""

    degrees = 0
    """lat/lon will be converted to degrees.degrees°N/S E/W"""

    minutes = 1
    """lat/lon will be converted to degrees°minutes.minutes'E/S E/W"""

    seconds = 2
    r"""
    lat/lon will be converted to degrees°minutes'seconds.seconds\'\'E/S E/W
    """

class o_latlon_format:
    """
    Helper class to convert between strings and enum values of type 't_latlon_format'
    """

    @overload
    def __init__(self, value: t_latlon_format = t_latlon_format.degrees) -> None:
        """Construct from enum value"""

    @overload
    def __init__(self, value: str) -> None:
        """Construct from string"""

    @overload
    def __init__(self, value: int) -> None:
        """Construct from string"""

    @property
    def value(self) -> t_latlon_format:
        """enum value"""

    @value.setter
    def value(self, arg: t_latlon_format, /) -> None: ...

    __default_value__: themachinethatgoesping.navigation_nanopy.t_latlon_format = ...
    """default enum value when constructing without arguments"""

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __eq__(self, arg: o_latlon_format, /) -> bool: ...

    @overload
    def __eq__(self, arg: t_latlon_format, /) -> bool: ...

    @overload
    def __eq__(self, arg: int, /) -> bool: ...

    @overload
    def __eq__(self, arg: str, /) -> bool: ...

    def copy(self) -> o_latlon_format:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> o_latlon_format: ...

    def __deepcopy__(self, arg: dict, /) -> o_latlon_format: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> o_latlon_format:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> None: ...

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class SensorConfiguration:
    """
    A coordinate system that allows for specifying sensor offsets (e.g.
    gps antenna and attitude sensor) and target offsets (e.g. MBES). Call
    the class and specify target_id and current sensor data to derive the
    geolocation and attitude of the specified targets
    """

    def __init__(self, default_sensor_name: str = 'zero-referenced') -> None:
        """
        Construct a new, empty Sensor Coordinate System object After
        construction: add sensor offsets and targets (offsets) Then compute
        target positions for sensor data
        """

    def without_targets(self) -> SensorConfiguration:
        """
        Return the SensorConfiguration object without registered targets

        Returns:
            SensorConfiguration
        """

    def can_merge_targets_with(self, other: SensorConfiguration) -> bool:
        """
        Check if the given SensorConfiguration includes a target (offsets)
        that is incompatible with the given SensorConfiguration targets

        Returns:
            false if the same target_id is registered with different offsets,
            true otherwise
        """

    @overload
    def compute_target_position(self, target_id: str, sensor_data: datastructures.SensordataLatLon) -> datastructures.GeolocationLatLon:
        """
        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"

        Args:
            target_id: name of the target (e.g. "MBES")
            sensor_data: SensordataLatLon / this structure includes latitude
                         and longitude information

        Returns:
            datastructures::GeolocationLatLon  / this structure includes
                           latitude and longitude information
        """

    @overload
    def compute_target_position(self, target_id: str, sensor_data: datastructures.SensordataUTM) -> datastructures.GeolocationUTM:
        """
        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"

        Args:
            target_id: name of the target (e.g. "MBES")
            sensor_data: SensordataUTM / this structure includes
                         northing/easting and utm zone or hemisphere
                         information

        Returns:
            datastructures::GeolocationUTM  / this structure includes
                           northing/easting and utm zone or hemisphere
                           information
        """

    @overload
    def compute_target_position(self, target_id: str, sensor_data: datastructures.SensordataLocal) -> datastructures.GeolocationLocal:
        """
        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"

        Args:
            target_id: name of the target (e.g. "MBES")
            sensor_data: SensordataLocal / this structure includes
                         northing/easting but no zone or hemisphere
                         information

        Returns:
            datastructures::GeolocationLocal  / this structure includes
                           northing/easting but no zone or hemisphere
                           information
        """

    @overload
    def compute_target_position(self, target_id: str, sensor_data: datastructures.Sensordata) -> datastructures.GeolocationLocal:
        """
        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"

        Args:
            target_id: name of the target (e.g. "MBES")
            sensor_data: Sensordata / this structure includes no coordinate
                         information

        Returns:
            datastructures::GeolocationLocal  / this structure includes
                           northing and east, which are set relative to the
                           sensor coordinate system center
        """

    def has_target(self, target_id: str) -> bool:
        """
        Checks if the sensor configuration has a target with the specified ID.

        Args:
            target_id: The ID of the target to check for.

        Returns:
            True if the sensor configuration has the target, false otherwise.
        """

    @overload
    def add_target(self, target_id: str, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None:
        """
        add a target (e.g. MBES) with offsets to the sensor position system

        Args:
            target_id: name of the target for reference
            x: x-offset of the target (in meters, positive forward)
            y: y-offset of the target (in meters, positive starboard)
            z: z-offset of the target (in meters, positive down)
            yaw: yaw offset of the target (right-handed around the z-axis) (in
                 degrees, 90° = east)
            pitch: pitch offset of the target (right-handed around the y-axis)
                   (in degrees, positive = bow up)
            roll: roll offset of the target (right-handed around the x-axis)
                  (in degrees, positive = port up)
        """

    @overload
    def add_target(self, target_id: str, target_offsets: datastructures.PositionalOffsets) -> None:
        """
        add a target (e.g. MBES) with offsets to the sensor position system

        Args:
            target_id: name of the target for reference
            target_offsets: mounting offsets of the target
        """

    def add_targets(self, targets: typing.Any) -> None:
        """
        add targets (e.g. MBES) with given target_ids and offsets to the
        sensor position system

        Args:
            targets: map_target_id_target_offsets of target offsets
        """

    def get_target(self, target_id: str) -> datastructures.PositionalOffsets:
        """
        Get stored target offsets of a specified target

        Args:
            target_id: name of the registered target

        Returns:
            const datastructures::PositionalOffsets& offsets of the target
        """

    def get_targets(self) -> typing.Any:
        """
        Get the map of stored target offsets objects

        Returns:
            const std::unordered_map_std_string_
datastructures_PositionalOffsets&
        """

    def remove_target(self, target_id: str) -> None:
        """
        Remove the target with the specified target_id

        Args:
            target_id: name of the registered target
        """

    def remove_targets(self) -> None:
        """Remove all stored targets"""

    def get_target_ids(self) -> list[str]:
        """
        Get the ids of the registered targets

        Returns:
            std::vector_std_string_view
        """

    @overload
    def set_attitude_source(self, name: str, yaw: float, pitch: float, roll: float) -> None:
        """
        Set the attitude sensor offsets

        Args:
            sensor_offsets: offsets structure (only yaw, pitch and roll are
                            used)
        """

    @overload
    def set_attitude_source(self, sensor_offsets: datastructures.PositionalOffsets) -> None:
        """
        Set the attitude sensor offsets

        Args:
            yaw: yaw offset of the attitude sensor (right-handed around the
                 z-axis) (in degrees, 90° = east)
            pitch: pitch offset of the attitude sensor (right-handed around
                   the y-axis) (in degrees, positive = bow up)
            roll: roll offset of the attitude sensor (right-handed around the
                  x-axis) (in degrees, positive = port up)
        """

    def get_attitude_source(self) -> datastructures.PositionalOffsets:
        """
        Get the attitude sensor offsets

        Returns:
            const datastructures::PositionalOffsets& offsets of the attitude
            sensor
        """

    @overload
    def set_heading_source(self, name: str, yaw: float) -> None:
        """
        Set the compass offsets

        Args:
            yaw: yaw offset of the compass (right-handed around the z-axis)
                 (in degrees, 90° = east)
        """

    @overload
    def set_heading_source(self, sensor_offsets: datastructures.PositionalOffsets) -> None:
        """
        Set the compass offsets

        Args:
            sensor_offsets: offsets structure (only yaw is used)
        """

    def get_heading_source(self) -> datastructures.PositionalOffsets:
        """
        Get the registered compass offsets

        Returns:
            const datastructures::PositionalOffsets& offsets of the compass
        """

    def set_waterline_offset(self, z: float) -> None:
        """
        Set the waterline offset Negative waterline offset means that z=0 is
        below the waterline

        Args:
            waterline_offset:
        """

    def get_waterline_offset(self) -> float:
        """
        Get the waterline offset Negative waterline offset means that z=0 is
        below the waterline

        Returns:
            waterline_offset
        """

    @overload
    def set_depth_source(self, name: str, x: float, y: float, z: float) -> None:
        """
        Set the depth sensor offsets

        Args:
            x: x-offset of the depth sensor (in meters, positive forward)
            y: y-offset of the depth sensor (in meters, positive starboard)
            z: z-offset of the depth sensor (in meters, positive down)
        """

    @overload
    def set_depth_source(self, sensor_offsets: datastructures.PositionalOffsets) -> None:
        """
        Set the depth sensor offsets

        Args:
            sensor_offsets: offsets structure (only x, y and z are used)
        """

    def get_depth_source(self) -> datastructures.PositionalOffsets:
        """
        Get the registered depth sensor offsets

        Returns:
            const datastructures::PositionalOffsets& offsets of the depth
            sensor
        """

    @overload
    def set_position_source(self, name: str, x: float, y: float, z: float) -> None:
        """
        Set the position system offsets

        Args:
            x: x-offset of the depth sensor (in meters, positive forward)
            y: y-offset of the depth sensor (in meters, positive starboard)
            z: z-offset of the depth sensor (in meters, positive down)
        """

    @overload
    def set_position_source(self, sensor_offsets: datastructures.PositionalOffsets) -> None:
        """
        Set the position system offsets

        Args:
            sensor_offsets: offsets structure (only x, y and z are used)
        """

    def get_position_source(self) -> datastructures.PositionalOffsets:
        """
        Get the registered position system offsets

        Returns:
            const datastructures::PositionalOffsets& offsets of the position
            system
        """

    def __eq__(self, other: SensorConfiguration) -> bool:
        """
        Compare two SensorConfiguration objects for equality

        Args:
            other: SensorConfiguration object to compare to

        Returns:
            true false
        """

    def copy(self) -> SensorConfiguration:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SensorConfiguration: ...

    def __deepcopy__(self, arg: dict, /) -> SensorConfiguration: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensorConfiguration:
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

class NavigationInterpolatorLocal:
    """
    The NavInterpolator class: Interpolate navigation (northing/easting no
    zone specified) values and attitude information and transform the
    values using the offsets specified in the sensor configuration class
    """

    def __init__(self, sensor_configuration: SensorConfiguration, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None:
        """
        Construct a new i navigationinterpolator interface

        Args:
            sensor_configuration: sensor configuration used for this
                                  navigation interpolator
            extrapolation_mode: extrapolate, fail or nearest
        """

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None:
        """
        Set the extrapolation mode for all interpolators

        Args:
            extrapolation_mode: extrapolate, fail or nearest
        """

    @overload
    def __call__(self, target_id: str, timestamp: float) -> datastructures.GeolocationLocal:
        """
        Compute the position of the target "target_id" based on the sensor
        data for the given timestamp stamp

        Args:
            target_id: name of the target (e.g. "MBES")
            timestamp: timestamp in seconds since epoch

        Returns:
            data structure that contains the position of the target in the
            world coordinate system
        """

    @overload
    def __call__(self, target_id: str, timestamps: Sequence[float], mp_cores: int = 1) -> datastructures.GeolocationLocalVector:
        """
        Compute the position of the target "target_id" for multiple timestamps
        (vectorized)

        Args:
            target_id: name of the target (e.g. "MBES")
            timestamps: vector of timestamps in seconds since epoch
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1

        Returns:
            GeolocationLocalVector containing positions for all timestamps
        """

    @overload
    def compute_target_position(self, target_id: str, timestamp: float) -> datastructures.GeolocationLocal:
        """
        Compute the position of the target "target_id" based on the sensor
        data for the given timestamp stamp

        Args:
            target_id: name of the target (e.g. "MBES")
            timestamp: timestamp in seconds since epoch

        Returns:
            data structure that contains the position of the target in the
            world coordinate system
        """

    @overload
    def compute_target_position(self, target_id: str, timestamps: Sequence[float], mp_cores: int = 1) -> datastructures.GeolocationLocalVector:
        """
        Compute the position of the target "target_id" for multiple timestamps
        (vectorized)

        Args:
            target_id: name of the target (e.g. "MBES")
            timestamps: vector of timestamps in seconds since epoch
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1

        Returns:
            GeolocationLocalVector containing positions for all timestamps
        """

    @overload
    def get_sensor_data(self, timestamp: float) -> datastructures.SensordataLocal:
        """
        Interpolate the saved sensor data for a specified timestamp stamp

        Args:
            timestamp: timestamp in seconds since epoch

        Returns:
            data structure that contains the sensor data interpolated for the
            given timestamp stamp
        """

    @overload
    def get_sensor_data(self, timestamps: Sequence[float], mp_cores: int = 1) -> datastructures.SensordataLocalVector:
        """
        Interpolate the saved sensor data for multiple timestamps (vectorized)

        Args:
            timestamps: vector of timestamps in seconds since epoch
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1

        Returns:
            SensordataLocalVector containing sensor data for all timestamps
        """

    def get_sampled_timestamps(self, downsample_interval: float = float('nan'), max_gap: float = float('nan'), sensor_names: Set[str] = ...) -> Annotated[NDArray[numpy.float64], dict(order='C')]:
        """
        Get sampled timestamps from the specified sensor interpolators

        This function retrieves timestamps from the specified sensors and
        returns their intersection (timestamps that are common to all
        specified sensors within max_gap).

        Args:
            downsample_interval: Interval for downsampling timestamps. If NaN,
                                 no downsampling
            max_gap: Maximum allowed gap between consecutive timestamps
            sensor_names: Set of sensor names to include. Valid names are:
                          "northing", "easting", "attitude", "heading",
                          "heave", "depth"

        Returns:
            xt::xtensor_double_1 Array of timestamps that are common to all
               specified sensors

        Raises:
            std::invalid_argument: if an unknown sensor name is specified
        """

    def get_sensor_configuration(self) -> SensorConfiguration:
        """
        direct reference to the sensor configuration

        Returns:
            SensorConfiguration&
        """

    def set_sensor_configuration(self, sensor_configuration: SensorConfiguration) -> None: ...

    @overload
    def add_target(self, target_id: str, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None:
        """
        add a target sensor with positional offsets

        Args:
            target_id: name of the target sensor
            x: x position of the sensor in m, positive forward
            y: y position of the sensor in m, positive starboard
            z: z position of the sensor in m, positive down
            yaw: yaw angle of the sensor in °, positive clockwise
            pitch: pitch angle of the sensor in °, positive is bow up
            roll: roll angle of the sensor in °, positive is port up
        """

    @overload
    def add_target(self, target_id: str, target_offsets: datastructures.PositionalOffsets) -> None:
        """
        add a target sensor with positional offsets

        Args:
            target_id: name of the target sensor
            sensor_offsets: structure that contains the sensor position
        """

    def set_data_position(self, timestamp: Sequence[float], northing: Sequence[float], easting: Sequence[float]) -> None:
        """
        Set the data of the position system (northing, easting)

        Args:
            timestamp: in seconds since epoch
            northing: northing in meters
            easting: easting in meters
        """

    def set_data_heave(self, timestamp: Sequence[float], heave: Sequence[float]) -> None:
        """
        Set the heave data

        Args:
            timestamp: in seconds since epoch
            heave: in meters, positive upwards
        """

    def set_data_depth(self, timestamp: Sequence[float], depth: Sequence[float]) -> None:
        """
        Set the depth data

        Args:
            timestamp: in seconds since epoch
            depth: in meters, positive downwards
        """

    def set_data_attitude(self, timestamp: Sequence[float], pitch: Sequence[float], roll: Sequence[float]) -> None:
        """
        Set the attitude data (no yaw, this is set in set_data_heading)

        Args:
            timestamp: in seconds since epoch
            pitch: in °, positive is bow up
            roll: in °, positive is port up
        """

    def set_data_heading(self, timestamp: Sequence[float], heading: Sequence[float]) -> None:
        """
        Set the compass data

        Args:
            timestamp: in seconds since epoch
            heading: in °, positive clockwise (north is 0°)
        """

    @property
    def interpolator_northing(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator:
        """interpolator for the northing data"""

    @interpolator_northing.setter
    def interpolator_northing(self, arg: themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator, /) -> None: ...

    @property
    def interpolator_easting(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator:
        """interpolator for the easting data"""

    @interpolator_easting.setter
    def interpolator_easting(self, arg: themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator, /) -> None: ...

    @property
    def interpolator_heave(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator:
        """
        interpolator that stores heave data (relative change in depth,
        positive upwards) [m]
        """

    @interpolator_heave.setter
    def interpolator_heave(self, arg: themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator, /) -> None: ...

    @property
    def interpolator_depth(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolatorDF:
        """interpolator that stores depth data (depth, positive downwards) [m]"""

    @interpolator_depth.setter
    def interpolator_depth(self, arg: themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolatorDF, /) -> None: ...

    @property
    def interpolator_attitude(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.SlerpInterpolatorDF:
        """interpolator that stores attitude data (pitch and roll)"""

    @interpolator_attitude.setter
    def interpolator_attitude(self, arg: themachinethatgoesping.tools_nanopy.vectorinterpolators.SlerpInterpolatorDF, /) -> None: ...

    @property
    def interpolator_heading(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.SlerpInterpolatorDF:
        """interpolator that stores compass data (yaw/heading) [°]"""

    @interpolator_heading.setter
    def interpolator_heading(self, arg: themachinethatgoesping.tools_nanopy.vectorinterpolators.SlerpInterpolatorDF, /) -> None: ...

    def merge(self, other: NavigationInterpolatorLocal) -> None:
        """
        Merge data from another interpolator. Only works of the
        SensorConfiguration is compatible.

        Args:
            other:
        """

    def __eq__(self, other: NavigationInterpolatorLocal) -> bool: ...

    def copy(self) -> NavigationInterpolatorLocal:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NavigationInterpolatorLocal: ...

    def __deepcopy__(self, arg: dict, /) -> NavigationInterpolatorLocal: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NavigationInterpolatorLocal:
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

class NavigationInterpolatorLatLon:
    """
    The NavInterpolator class: Interpolate navigation (lat/lon) values and
    attitude information and transform the values using the offsets
    specified in the sensor configuration class
    """

    def __init__(self, sensor_configuration: SensorConfiguration, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None:
        """
        Construct a new i navigationinterpolator interface

        Args:
            sensor_configuration: sensor configuration used for this
                                  navigation interpolator
            extrapolation_mode: extrapolate, fail or nearest
        """

    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_nanopy.vectorinterpolators.o_extr_mode = themachinethatgoesping.tools_nanopy.vectorinterpolators.t_extr_mode.extrapolate) -> None:
        """
        Set the extrapolation mode for all interpolators

        Args:
            extrapolation_mode: extrapolate, fail or nearest
        """

    @overload
    def __call__(self, target_id: str, timestamp: float) -> datastructures.GeolocationLatLon:
        """
        Compute the position of the target "target_id" based on the sensor
        data for the given timestamp stamp

        Args:
            target_id: name of the target (e.g. "MBES")
            timestamp: timestamp in seconds since epoch

        Returns:
            data structure that contains the position of the target in the
            world coordinate system
        """

    @overload
    def __call__(self, target_id: str, timestamps: Sequence[float], mp_cores: int = 1) -> datastructures.GeolocationLatLonVector:
        """
        Compute the position of the target "target_id" for multiple timestamps
        (vectorized)

        Args:
            target_id: name of the target (e.g. "MBES")
            timestamps: vector of timestamps in seconds since epoch
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1

        Returns:
            GeolocationLatLonVector containing positions for all timestamps
        """

    @overload
    def compute_target_position(self, target_id: str, timestamp: float) -> datastructures.GeolocationLatLon:
        """
        Compute the position of the target "target_id" based on the sensor
        data for the given timestamp stamp

        Args:
            target_id: name of the target (e.g. "MBES")
            timestamp: timestamp in seconds since epoch

        Returns:
            data structure that contains the position of the target in the
            world coordinate system
        """

    @overload
    def compute_target_position(self, target_id: str, timestamps: Sequence[float], mp_cores: int = 1) -> datastructures.GeolocationLatLonVector:
        """
        Compute the position of the target "target_id" for multiple timestamps
        (vectorized)

        Args:
            target_id: name of the target (e.g. "MBES")
            timestamps: vector of timestamps in seconds since epoch
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1

        Returns:
            GeolocationLatLonVector containing positions for all timestamps
        """

    @overload
    def get_sensor_data(self, timestamp: float) -> datastructures.SensordataLatLon:
        """
        Interpolate the saved sensor data for a specified timestamp stamp

        Args:
            timestamp: timestamp in seconds since epoch

        Returns:
            data structure that contains the sensor data interpolated for the
            given timestamp stamp
        """

    @overload
    def get_sensor_data(self, timestamps: Sequence[float], mp_cores: int = 1) -> datastructures.SensordataLatLonVector:
        """
        Interpolate the saved sensor data for multiple timestamps (vectorized)

        Args:
            timestamps: vector of timestamps in seconds since epoch
            mp_cores: Number of OpenMP threads to use for parallelization.
                      Default is 1

        Returns:
            SensordataLatLonVector containing sensor data for all timestamps
        """

    def get_sampled_timestamps(self, downsample_interval: float = float('nan'), max_gap: float = float('nan'), sensor_names: Set[str] = ...) -> Annotated[NDArray[numpy.float64], dict(order='C')]:
        """
        Get sampled timestamps from the specified sensor interpolators

        This function retrieves timestamps from the specified sensors and
        returns their intersection (timestamps that are common to all
        specified sensors within max_gap).

        Args:
            downsample_interval: Interval for downsampling timestamps. If NaN,
                                 no downsampling
            max_gap: Maximum allowed gap between consecutive timestamps
            sensor_names: Set of sensor names to include. Valid names are:
                          "latitude", "longitude", "attitude", "heading",
                          "heave", "depth"

        Returns:
            xt::xtensor_double_1 Array of timestamps that are common to all
               specified sensors
        """

    def get_sensor_configuration(self) -> SensorConfiguration:
        """
        direct reference to the sensor configuration

        Returns:
            SensorConfiguration&
        """

    def set_sensor_configuration(self, sensor_configuration: SensorConfiguration) -> None: ...

    @overload
    def add_target(self, target_id: str, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None:
        """
        add a target sensor with positional offsets

        Args:
            target_id: name of the target sensor
            x: x position of the sensor in m, positive forward
            y: y position of the sensor in m, positive starboard
            z: z position of the sensor in m, positive down
            yaw: yaw angle of the sensor in °, positive clockwise
            pitch: pitch angle of the sensor in °, positive is bow up
            roll: roll angle of the sensor in °, positive is port up
        """

    @overload
    def add_target(self, target_id: str, target_offsets: datastructures.PositionalOffsets) -> None:
        """
        add a target sensor with positional offsets

        Args:
            target_id: name of the target sensor
            sensor_offsets: structure that contains the sensor position
        """

    def set_data_position(self, timestamp: Sequence[float], latitude: Sequence[float], longitude: Sequence[float]) -> None:
        """
        Set the data of the position system (latitude, longitude)

        Args:
            timestamp: in seconds since epoch
            latitude: latitude in °
            longitude: longitude in °
        """

    def set_data_heave(self, timestamp: Sequence[float], heave: Sequence[float]) -> None:
        """
        Set the heave data

        Args:
            timestamp: in seconds since epoch
            heave: in meters, positive upwards
        """

    def set_data_depth(self, timestamp: Sequence[float], depth: Sequence[float]) -> None:
        """
        Set the depth data

        Args:
            timestamp: in seconds since epoch
            depth: in meters, positive downwards
        """

    def set_data_attitude(self, timestamp: Sequence[float], pitch: Sequence[float], roll: Sequence[float]) -> None:
        """
        Set the attitude data (no yaw, this is set in set_data_heading)

        Args:
            timestamp: in seconds since epoch
            pitch: in °, positive is bow up
            roll: in °, positive is port up
        """

    def set_data_heading(self, timestamp: Sequence[float], heading: Sequence[float]) -> None:
        """
        Set the compass data

        Args:
            timestamp: in seconds since epoch
            heading: in °, positive clockwise (north is 0°)
        """

    @property
    def interpolator_latitude(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator:
        """interpolator for the latitude data"""

    @interpolator_latitude.setter
    def interpolator_latitude(self, arg: themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator, /) -> None: ...

    @property
    def interpolator_longitude(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator:
        """interpolator for the longitude data"""

    @interpolator_longitude.setter
    def interpolator_longitude(self, arg: themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator, /) -> None: ...

    @property
    def interpolator_heave(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator:
        """
        interpolator that stores heave data (relative change in depth,
        positive upwards) [m]
        """

    @interpolator_heave.setter
    def interpolator_heave(self, arg: themachinethatgoesping.tools_nanopy.vectorinterpolators.AkimaInterpolator, /) -> None: ...

    @property
    def interpolator_depth(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolatorDF:
        """interpolator that stores depth data (depth, positive downwards) [m]"""

    @interpolator_depth.setter
    def interpolator_depth(self, arg: themachinethatgoesping.tools_nanopy.vectorinterpolators.LinearInterpolatorDF, /) -> None: ...

    @property
    def interpolator_attitude(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.SlerpInterpolatorDF:
        """interpolator that stores attitude data (pitch and roll)"""

    @interpolator_attitude.setter
    def interpolator_attitude(self, arg: themachinethatgoesping.tools_nanopy.vectorinterpolators.SlerpInterpolatorDF, /) -> None: ...

    @property
    def interpolator_heading(self) -> themachinethatgoesping.tools_nanopy.vectorinterpolators.SlerpInterpolatorDF:
        """interpolator that stores compass data (yaw/heading) [°]"""

    @interpolator_heading.setter
    def interpolator_heading(self, arg: themachinethatgoesping.tools_nanopy.vectorinterpolators.SlerpInterpolatorDF, /) -> None: ...

    def merge(self, other: NavigationInterpolatorLatLon) -> None:
        """
        Merge data from another interpolator. Only works of the
        SensorConfiguration is compatible.

        Args:
            other:
        """

    def __eq__(self, other: NavigationInterpolatorLatLon) -> bool: ...

    def copy(self) -> NavigationInterpolatorLatLon:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> NavigationInterpolatorLatLon: ...

    def __deepcopy__(self, arg: dict, /) -> NavigationInterpolatorLatLon: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NavigationInterpolatorLatLon:
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
