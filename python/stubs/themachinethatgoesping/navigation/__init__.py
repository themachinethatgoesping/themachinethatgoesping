"""
Python module to store, interpolate and transform navigation data
"""
from __future__ import annotations
import themachinethatgoesping.tools_cppy.vectorinterpolators
import typing
from . import datastructures
from . import navtools
from . import nmea_0183
__all__ = ['NavigationInterpolatorLatLon', 'NavigationInterpolatorLocal', 'SensorConfiguration', 'datastructures', 'navtools', 'nmea_0183', 'ostream_redirect']
class NavigationInterpolatorLatLon:
    """
    The NavInterpolator class: Interpolate navigation (lat/lon) values and
    attitude information and transform the values using the offsets
    specified in the sensor configuration class
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NavigationInterpolatorLatLon:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, target_id: str, timestamp: float) -> datastructures.GeolocationLatLon:
        """
        Compute the position of the target "target_id" based on the sensor
        data for the given timestamp stamp
        
        Parameter ``target_id``:
            name of the target (e.g. "MBES")
        
        Parameter ``timestamp``:
            timestamp in seconds since epoch
        
        Returns:
            data structure that contains the position of the target in the
            world coordinate system
        """
    def __copy__(self) -> NavigationInterpolatorLatLon:
        ...
    def __deepcopy__(self, arg0: dict) -> NavigationInterpolatorLatLon:
        ...
    def __eq__(self, other: NavigationInterpolatorLatLon) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, sensor_configuration: SensorConfiguration, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        """
        Construct a new i navigationinterpolator interface
        
        Parameter ``sensor_configuration``:
            sensor configuration used for this navigation interpolator
        
        Parameter ``extrapolation_mode``:
            extrapolate, fail or nearest
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def add_target(self, target_id: str, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None:
        """
        add a target sensor with positional offsets
        
        Parameter ``target_id``:
            name of the target sensor
        
        Parameter ``x``:
            x position of the sensor in m, positive forward
        
        Parameter ``y``:
            y position of the sensor in m, positive starboard
        
        Parameter ``z``:
            z position of the sensor in m, positive down
        
        Parameter ``yaw``:
            yaw angle of the sensor in °, positive clockwise
        
        Parameter ``pitch``:
            pitch angle of the sensor in °, positive is bow up
        
        Parameter ``roll``:
            roll angle of the sensor in °, positive is port up
        """
    @typing.overload
    def add_target(self, target_id: str, target_offsets: datastructures.PositionalOffsets) -> None:
        """
        add a target sensor with positional offsets
        
        Parameter ``target_id``:
            name of the target sensor
        
        Parameter ``sensor_offsets``:
            structure that contains the sensor position
        """
    def compute_target_position(self, target_id: str, timestamp: float) -> datastructures.GeolocationLatLon:
        """
        Compute the position of the target "target_id" based on the sensor
        data for the given timestamp stamp
        
        Parameter ``target_id``:
            name of the target (e.g. "MBES")
        
        Parameter ``timestamp``:
            timestamp in seconds since epoch
        
        Returns:
            data structure that contains the position of the target in the
            world coordinate system
        """
    def copy(self) -> NavigationInterpolatorLatLon:
        """
        return a copy using the c++ default copy constructor
        """
    def get_sensor_configuration(self) -> SensorConfiguration:
        """
        direct reference to the sensor configuration
        
        Returns:
            SensorConfiguration&
        """
    def get_sensor_data(self, timestamp: float) -> datastructures.SensordataLatLon:
        """
        Interpolate the saved sensor data for a specified timestamp stamp
        
        Parameter ``timestamp``:
            timestamp in seconds since epoch
        
        Returns:
            data structure that contains the sensor data interpolated for the
            given timestamp stamp
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def merge(self, other: NavigationInterpolatorLatLon) -> None:
        """
        Merge data from another interpolator. Only works of the
        SensorConfiguration is compatible.
        
        Parameter ``other``:
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_attitude(self, timestamp: list[float], pitch: list[float], roll: list[float]) -> None:
        """
        Set the attitude data (no yaw, this is set in set_data_heading)
        
        Parameter ``timestamp``:
            in seconds since epoch
        
        Parameter ``pitch``:
            in °, positive is bow up
        
        Parameter ``roll``:
            in °, positive is port up
        """
    def set_data_depth(self, timestamp: list[float], depth: list[float]) -> None:
        """
        Set the depth data
        
        Parameter ``timestamp``:
            in seconds since epoch
        
        Parameter ``depth``:
            in meters, positive downwards
        """
    def set_data_heading(self, timestamp: list[float], heading: list[float]) -> None:
        """
        Set the compass data
        
        Parameter ``timestamp``:
            in seconds since epoch
        
        Parameter ``heading``:
            in °, positive clockwise (north is 0°)
        """
    def set_data_heave(self, timestamp: list[float], heave: list[float]) -> None:
        """
        Set the heave data
        
        Parameter ``timestamp``:
            in seconds since epoch
        
        Parameter ``heave``:
            in meters, positive upwards
        """
    def set_data_position(self, timestamp: list[float], latitude: list[float], longitude: list[float]) -> None:
        """
        Set the data of the position system (latitude, longitude)
        
        Parameter ``timestamp``:
            in seconds since epoch
        
        Parameter ``latitude``:
            latitude in °
        
        Parameter ``longitude``:
            longitude in °
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        """
        Set the extrapolation mode for all interpolators
        
        Parameter ``extrapolation_mode``:
            extrapolate, fail or nearest
        """
    def set_sensor_configuration(self, sensor_configuration: SensorConfiguration) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def interpolator_attitude(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.SlerpInterpolatorDF:
        """
        < interpolator that stores attitude data (pitch and roll)
        """
    @interpolator_attitude.setter
    def interpolator_attitude(self, arg1: themachinethatgoesping.tools_cppy.vectorinterpolators.SlerpInterpolatorDF) -> None:
        ...
    @property
    def interpolator_depth(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.LinearInterpolatorDF:
        """
        < interpolator that stores depth data (depth, positive downwards) <
        [m]
        """
    @interpolator_depth.setter
    def interpolator_depth(self, arg1: themachinethatgoesping.tools_cppy.vectorinterpolators.LinearInterpolatorDF) -> None:
        ...
    @property
    def interpolator_heading(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.SlerpInterpolatorDF:
        """
        < interpolator that stores compass data (yaw/heading) [°]
        """
    @interpolator_heading.setter
    def interpolator_heading(self, arg1: themachinethatgoesping.tools_cppy.vectorinterpolators.SlerpInterpolatorDF) -> None:
        ...
    @property
    def interpolator_heave(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator that stores heave data (relative change in depth, <
        positive upwards) [m]
        """
    @interpolator_heave.setter
    def interpolator_heave(self, arg1: themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator) -> None:
        ...
    @property
    def interpolator_latitude(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator for the latitude data
        """
    @interpolator_latitude.setter
    def interpolator_latitude(self, arg1: themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator) -> None:
        ...
    @property
    def interpolator_longitude(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator for the longitude data
        """
    @interpolator_longitude.setter
    def interpolator_longitude(self, arg1: themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator) -> None:
        ...
class NavigationInterpolatorLocal:
    """
    The NavInterpolator class: Interpolate navigation (northing/easting no
    zone specified) values and attitude information and transform the
    values using the offsets specified in the sensor configuration class
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NavigationInterpolatorLocal:
        """
        create T_CLASS object from bytearray
        """
    def __call__(self, target_id: str, timestamp: float) -> datastructures.GeolocationLocal:
        """
        Compute the position of the target "target_id" based on the sensor
        data for the given timestamp stamp
        
        Parameter ``target_id``:
            name of the target (e.g. "MBES")
        
        Parameter ``timestamp``:
            timestamp in seconds since epoch
        
        Returns:
            data structure that contains the position of the target in the
            world coordinate system
        """
    def __copy__(self) -> NavigationInterpolatorLocal:
        ...
    def __deepcopy__(self, arg0: dict) -> NavigationInterpolatorLocal:
        ...
    def __eq__(self, other: NavigationInterpolatorLocal) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, sensor_configuration: SensorConfiguration, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        """
        Construct a new i navigationinterpolator interface
        
        Parameter ``sensor_configuration``:
            sensor configuration used for this navigation interpolator
        
        Parameter ``extrapolation_mode``:
            extrapolate, fail or nearest
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def add_target(self, target_id: str, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None:
        """
        add a target sensor with positional offsets
        
        Parameter ``target_id``:
            name of the target sensor
        
        Parameter ``x``:
            x position of the sensor in m, positive forward
        
        Parameter ``y``:
            y position of the sensor in m, positive starboard
        
        Parameter ``z``:
            z position of the sensor in m, positive down
        
        Parameter ``yaw``:
            yaw angle of the sensor in °, positive clockwise
        
        Parameter ``pitch``:
            pitch angle of the sensor in °, positive is bow up
        
        Parameter ``roll``:
            roll angle of the sensor in °, positive is port up
        """
    @typing.overload
    def add_target(self, target_id: str, target_offsets: datastructures.PositionalOffsets) -> None:
        """
        add a target sensor with positional offsets
        
        Parameter ``target_id``:
            name of the target sensor
        
        Parameter ``sensor_offsets``:
            structure that contains the sensor position
        """
    def compute_target_position(self, target_id: str, timestamp: float) -> datastructures.GeolocationLocal:
        """
        Compute the position of the target "target_id" based on the sensor
        data for the given timestamp stamp
        
        Parameter ``target_id``:
            name of the target (e.g. "MBES")
        
        Parameter ``timestamp``:
            timestamp in seconds since epoch
        
        Returns:
            data structure that contains the position of the target in the
            world coordinate system
        """
    def copy(self) -> NavigationInterpolatorLocal:
        """
        return a copy using the c++ default copy constructor
        """
    def get_sensor_configuration(self) -> SensorConfiguration:
        """
        direct reference to the sensor configuration
        
        Returns:
            SensorConfiguration&
        """
    def get_sensor_data(self, timestamp: float) -> datastructures.SensordataLocal:
        """
        Interpolate the saved sensor data for a specified timestamp stamp
        
        Parameter ``timestamp``:
            timestamp in seconds since epoch
        
        Returns:
            data structure that contains the sensor data interpolated for the
            given timestamp stamp
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def merge(self, other: NavigationInterpolatorLocal) -> None:
        """
        Merge data from another interpolator. Only works of the
        SensorConfiguration is compatible.
        
        Parameter ``other``:
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def set_data_attitude(self, timestamp: list[float], pitch: list[float], roll: list[float]) -> None:
        """
        Set the attitude data (no yaw, this is set in set_data_heading)
        
        Parameter ``timestamp``:
            in seconds since epoch
        
        Parameter ``pitch``:
            in °, positive is bow up
        
        Parameter ``roll``:
            in °, positive is port up
        """
    def set_data_depth(self, timestamp: list[float], depth: list[float]) -> None:
        """
        Set the depth data
        
        Parameter ``timestamp``:
            in seconds since epoch
        
        Parameter ``depth``:
            in meters, positive downwards
        """
    def set_data_heading(self, timestamp: list[float], heading: list[float]) -> None:
        """
        Set the compass data
        
        Parameter ``timestamp``:
            in seconds since epoch
        
        Parameter ``heading``:
            in °, positive clockwise (north is 0°)
        """
    def set_data_heave(self, timestamp: list[float], heave: list[float]) -> None:
        """
        Set the heave data
        
        Parameter ``timestamp``:
            in seconds since epoch
        
        Parameter ``heave``:
            in meters, positive upwards
        """
    def set_data_position(self, timestamp: list[float], northing: list[float], easting: list[float]) -> None:
        """
        Set the data of the position system (northing, easting)
        
        Parameter ``timestamp``:
            in seconds since epoch
        
        Parameter ``northing``:
            northing in meters
        
        Parameter ``easting``:
            easting in meters
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools_cppy.vectorinterpolators.t_extr_mode = ...) -> None:
        """
        Set the extrapolation mode for all interpolators
        
        Parameter ``extrapolation_mode``:
            extrapolate, fail or nearest
        """
    def set_sensor_configuration(self, sensor_configuration: SensorConfiguration) -> None:
        ...
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def interpolator_attitude(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.SlerpInterpolatorDF:
        """
        < interpolator that stores attitude data (pitch and roll)
        """
    @interpolator_attitude.setter
    def interpolator_attitude(self, arg1: themachinethatgoesping.tools_cppy.vectorinterpolators.SlerpInterpolatorDF) -> None:
        ...
    @property
    def interpolator_depth(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.LinearInterpolatorDF:
        """
        < interpolator that stores depth data (depth, positive downwards) <
        [m]
        """
    @interpolator_depth.setter
    def interpolator_depth(self, arg1: themachinethatgoesping.tools_cppy.vectorinterpolators.LinearInterpolatorDF) -> None:
        ...
    @property
    def interpolator_easting(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator for the easting data
        """
    @interpolator_easting.setter
    def interpolator_easting(self, arg1: themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator) -> None:
        ...
    @property
    def interpolator_heading(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.SlerpInterpolatorDF:
        """
        < interpolator that stores compass data (yaw/heading) [°]
        """
    @interpolator_heading.setter
    def interpolator_heading(self, arg1: themachinethatgoesping.tools_cppy.vectorinterpolators.SlerpInterpolatorDF) -> None:
        ...
    @property
    def interpolator_heave(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator that stores heave data (relative change in depth, <
        positive upwards) [m]
        """
    @interpolator_heave.setter
    def interpolator_heave(self, arg1: themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator) -> None:
        ...
    @property
    def interpolator_northing(self) -> themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator for the northing data
        """
    @interpolator_northing.setter
    def interpolator_northing(self, arg1: themachinethatgoesping.tools_cppy.vectorinterpolators.AkimaInterpolator) -> None:
        ...
class SensorConfiguration:
    """
    A coordinate system that allows for specifying sensor offsets (e.g.
    gps antenna and attitude sensor) and target offsets (e.g. MBES). Call
    the class and specify target_id and current sensor data to derive the
    geolocation and attitude of the specified targets
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensorConfiguration:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SensorConfiguration:
        ...
    def __deepcopy__(self, arg0: dict) -> SensorConfiguration:
        ...
    def __eq__(self, other: SensorConfiguration) -> bool:
        """
        Compare two SensorConfiguration objects for equality
        
        Parameter ``other``:
            SensorConfiguration object to compare to
        
        Returns:
            true
        
        Returns:
            false
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, default_sensor_name: str = 'zero-referenced') -> None:
        """
        Construct a new, empty Sensor Coordinate System object After
        construction: add sensor offsets and targets (offsets) Then compute
        target positions for sensor data
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    @typing.overload
    def add_target(self, target_id: str, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None:
        """
        add a target (e.g. MBES) with offsets to the sensor position system
        
        Parameter ``target_id``:
            name of the target for reference
        
        Parameter ``x``:
            x-offset of the target (in meters, positive forward)
        
        Parameter ``y``:
            y-offset of the target (in meters, positive starboard)
        
        Parameter ``z``:
            z-offset of the target (in meters, positive down)
        
        Parameter ``yaw``:
            yaw offset of the target (right-handed around the z-axis) (in
            degrees, 90° = east)
        
        Parameter ``pitch``:
            pitch offset of the target (right-handed around the y-axis) (in
            degrees, positive = bow up)
        
        Parameter ``roll``:
            roll offset of the target (right-handed around the x-axis) (in
            degrees, positive = port up)
        """
    @typing.overload
    def add_target(self, target_id: str, target_offsets: datastructures.PositionalOffsets) -> None:
        """
        add a target (e.g. MBES) with offsets to the sensor position system
        
        Parameter ``target_id``:
            name of the target for reference
        
        Parameter ``target_offsets``:
            mounting offsets of the target
        """
    def add_targets(self, targets: dict[str, datastructures.PositionalOffsets]) -> None:
        """
        add targets (e.g. MBES) with given target_ids and offsets to the
        sensor position system
        
        Parameter ``targets``:
            map<target_id, target_offsets> of target offsets
        """
    def can_merge_targets_with(self, other: SensorConfiguration) -> bool:
        """
        Check if the given SensorConfiguration includes a target (offsets)
        that is incompatible with the given SensorConfiguration targets
        
        Returns:
            false if the same target_id is registered with different offsets,
            true otherwise
        """
    @typing.overload
    def compute_target_position(self, target_id: str, sensor_data: datastructures.SensordataLatLon) -> datastructures.GeolocationLatLon:
        """
        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"
        
        Parameter ``target_id``:
            name of the target (e.g. "MBES")
        
        Parameter ``sensor_data``:
            SensordataLatLon / this structure includes latitude and longitude
            information
        
        Returns:
            datastructures::GeolocationLatLon / this structure includes
            latitude and longitude information
        """
    @typing.overload
    def compute_target_position(self, target_id: str, sensor_data: datastructures.SensordataUTM) -> datastructures.GeolocationUTM:
        """
        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"
        
        Parameter ``target_id``:
            name of the target (e.g. "MBES")
        
        Parameter ``sensor_data``:
            SensordataUTM / this structure includes northing/easting and utm
            zone or hemisphere information
        
        Returns:
            datastructures::GeolocationUTM / this structure includes
            northing/easting and utm zone or hemisphere information
        """
    @typing.overload
    def compute_target_position(self, target_id: str, sensor_data: datastructures.SensordataLocal) -> datastructures.GeolocationLocal:
        """
        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"
        
        Parameter ``target_id``:
            name of the target (e.g. "MBES")
        
        Parameter ``sensor_data``:
            SensordataLocal / this structure includes northing/easting but no
            zone or hemisphere information
        
        Returns:
            datastructures::GeolocationLocal / this structure includes
            northing/easting but no zone or hemisphere information
        """
    @typing.overload
    def compute_target_position(self, target_id: str, sensor_data: datastructures.Sensordata) -> datastructures.GeolocationLocal:
        """
        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"
        
        Parameter ``target_id``:
            name of the target (e.g. "MBES")
        
        Parameter ``sensor_data``:
            Sensordata / this structure includes no coordinate information
        
        Returns:
            datastructures::GeolocationLocal / this structure includes
            northing and east, which are set relative to the sensor coordinate
            system center
        """
    def copy(self) -> SensorConfiguration:
        """
        return a copy using the c++ default copy constructor
        """
    def get_attitude_source(self) -> datastructures.PositionalOffsets:
        """
        Get the attitude sensor offsets
        
        Returns:
            const datastructures::PositionalOffsets& offsets of the attitude
            sensor
        """
    def get_depth_source(self) -> datastructures.PositionalOffsets:
        """
        Get the registered depth sensor offsets
        
        Returns:
            const datastructures::PositionalOffsets& offsets of the depth
            sensor
        """
    def get_heading_source(self) -> datastructures.PositionalOffsets:
        """
        Get the registered compass offsets
        
        Returns:
            const datastructures::PositionalOffsets& offsets of the compass
        """
    def get_position_source(self) -> datastructures.PositionalOffsets:
        """
        Get the registered position system offsets
        
        Returns:
            const datastructures::PositionalOffsets& offsets of the position
            system
        """
    def get_target(self, target_id: str) -> datastructures.PositionalOffsets:
        """
        Get stored target offsets of a specified target
        
        Parameter ``target_id``:
            name of the registered target
        
        Returns:
            const datastructures::PositionalOffsets& offsets of the target
        """
    def get_target_ids(self) -> list[str]:
        """
        Get the ids of the registered targets
        
        Returns:
            std::vector<std::string_view>
        """
    def get_targets(self) -> dict[str, datastructures.PositionalOffsets]:
        """
        Get the map of stored target offsets objects
        
        Returns:
            const std::unordered_map<std::string,
            datastructures::PositionalOffsets>&
        """
    def get_waterline_offset(self) -> float:
        """
        Get the waterline offset Negative waterline offset means that z=0 is
        below the waterline
        
        Returns:
            waterline_offset
        """
    def has_target(self, target_id: str) -> bool:
        """
        Checks if the sensor configuration has a target with the specified ID.
        
        Parameter ``target_id``:
            The ID of the target to check for.
        
        Returns:
            True if the sensor configuration has the target, false otherwise.
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
    def remove_target(self, target_id: str) -> None:
        """
        Remove the target with the specified target_id
        
        Parameter ``target_id``:
            name of the registered target
        """
    def remove_targets(self) -> None:
        """
        Remove all stored targets
        """
    @typing.overload
    def set_attitude_source(self, name: str, yaw: float, pitch: float, roll: float) -> None:
        """
        Set the attitude sensor offsets
        
        Parameter ``sensor_offsets``:
            offsets structure (only yaw, pitch and roll are used)
        """
    @typing.overload
    def set_attitude_source(self, sensor_offsets: datastructures.PositionalOffsets) -> None:
        """
        Set the attitude sensor offsets
        
        Parameter ``yaw``:
            yaw offset of the attitude sensor (right-handed around the z-axis)
            (in degrees, 90° = east)
        
        Parameter ``pitch``:
            pitch offset of the attitude sensor (right-handed around the
            y-axis) (in degrees, positive = bow up)
        
        Parameter ``roll``:
            roll offset of the attitude sensor (right-handed around the
            x-axis) (in degrees, positive = port up)
        """
    @typing.overload
    def set_depth_source(self, name: str, x: float, y: float, z: float) -> None:
        """
        Set the depth sensor offsets
        
        Parameter ``x``:
            x-offset of the depth sensor (in meters, positive forward)
        
        Parameter ``y``:
            y-offset of the depth sensor (in meters, positive starboard)
        
        Parameter ``z``:
            z-offset of the depth sensor (in meters, positive down)
        """
    @typing.overload
    def set_depth_source(self, sensor_offsets: datastructures.PositionalOffsets) -> None:
        """
        Set the depth sensor offsets
        
        Parameter ``sensor_offsets``:
            offsets structure (only x, y and z are used)
        """
    @typing.overload
    def set_heading_source(self, name: str, yaw: float) -> None:
        """
        Set the compass offsets
        
        Parameter ``yaw``:
            yaw offset of the compass (right-handed around the z-axis) (in
            degrees, 90° = east)
        """
    @typing.overload
    def set_heading_source(self, sensor_offsets: datastructures.PositionalOffsets) -> None:
        """
        Set the compass offsets
        
        Parameter ``sensor_offsets``:
            offsets structure (only yaw is used)
        """
    @typing.overload
    def set_position_source(self, name: str, x: float, y: float, z: float) -> None:
        """
        Set the position system offsets
        
        Parameter ``x``:
            x-offset of the depth sensor (in meters, positive forward)
        
        Parameter ``y``:
            y-offset of the depth sensor (in meters, positive starboard)
        
        Parameter ``z``:
            z-offset of the depth sensor (in meters, positive down)
        """
    @typing.overload
    def set_position_source(self, sensor_offsets: datastructures.PositionalOffsets) -> None:
        """
        Set the position system offsets
        
        Parameter ``sensor_offsets``:
            offsets structure (only x, y and z are used)
        """
    def set_waterline_offset(self, z: float) -> None:
        """
        Set the waterline offset Negative waterline offset means that z=0 is
        below the waterline
        
        Parameter ``waterline_offset``:
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    def without_targets(self) -> SensorConfiguration:
        """
        Return the SensorConfiguration object without registered targets
        
        Returns:
            SensorConfiguration
        """
class ostream_redirect:
    def __enter__(self) -> None:
        ...
    def __exit__(self, *args) -> None:
        ...
    def __init__(self, stdout: bool = True, stderr: bool = True) -> None:
        ...
__version__: str = '0.17.5'
