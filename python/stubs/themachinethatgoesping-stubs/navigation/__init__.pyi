"""Python module to store, interpolate and transform navigation data"""
from __future__ import annotations
import themachinethatgoesping.navigation
import typing
import themachinethatgoesping.tools.vectorinterpolators

__all__ = [
    "NavigationInterpolatorLatLon",
    "NavigationInterpolatorLocal",
    "SensorConfiguration",
    "datastructures",
    "navtools",
    "nmea_0183",
    "ostream_redirect"
]


class NavigationInterpolatorLatLon():
    """
    The NavInterpolator class: Interpolate navigation (lat/lon) values and
    attitude information and transform the values using the offsets
    specified in the sensor configuration class
    """
    def __call__(self, target_id: str, timestamp: float) -> datastructures.GeoLocationLatLon: 
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
    def __copy__(self) -> NavigationInterpolatorLatLon: ...
    def __deepcopy__(self, arg0: dict) -> NavigationInterpolatorLatLon: ...
    def __eq__(self, other: NavigationInterpolatorLatLon) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self, sensor_configuration: SensorConfiguration, extrapolation_mode: themachinethatgoesping.tools.vectorinterpolators.t_extr_mode = t_extr_mode.extrapolate) -> None: 
        """
        Construct a new i navigationinterpolator interface

        Parameter ``extrapolation_mode``:
            extrapolate, fail or nearest
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
    @typing.overload
    def add_target(self, target_id: str, target_offsets: datastructures.PositionalOffsets) -> None: 
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

        add a target sensor with positional offsets

        Parameter ``target_id``:
            name of the target sensor

        Parameter ``sensor_offsets``:
            structure that contains the sensor position
        """
    @typing.overload
    def add_target(self, target_id: str, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None: ...
    def compute_target_position(self, target_id: str, timestamp: float) -> datastructures.GeoLocationLatLon: 
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
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NavigationInterpolatorLatLon: 
        """
        create T_CLASS object from bytearray
        """
    def get_sensor_data(self, timestamp: float) -> datastructures.SensorDataLatLon: 
        """
        Interpolate the saved sensor data for a specified timestamp stamp

        Parameter ``timestamp``:
            timestamp in seconds since epoch

        Returns:
            data structure that contains the sensor data interpolated for the
            given timestamp stamp
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_data_attitude(self, timestamp: typing.List[float], pitch: typing.List[float], roll: typing.List[float]) -> None: 
        """
        Set the attitude data (no yaw, ythis is set in set_data_heading)

        Parameter ``timestamp``:
            in seconds since epoch

        Parameter ``pitch``:
            in °, positive is bow up

        Parameter ``roll``:
            in °, positive is port up
        """
    def set_data_depth(self, timestamp: typing.List[float], depth: typing.List[float]) -> None: 
        """
        Set the depth data

        Parameter ``timestamp``:
            in seconds since epoch

        Parameter ``depth``:
            in meters, positive downwards
        """
    def set_data_heading(self, timestamp: typing.List[float], heading: typing.List[float]) -> None: 
        """
        Set the compass data

        Parameter ``timestamp``:
            in seconds since epoch

        Parameter ``heading``:
            in °, positive clockwise (north is 0°)
        """
    def set_data_heave(self, timestamp: typing.List[float], heave: typing.List[float]) -> None: 
        """
        Set the heave data

        Parameter ``timestamp``:
            in seconds since epoch

        Parameter ``heave``:
            in meters, positive upwards
        """
    def set_data_position(self, timestamp: typing.List[float], latitude: typing.List[float], longitude: typing.List[float]) -> None: 
        """
        Set the data of the position system (latitude, longitude)

        Parameter ``timestamp``:
            in seconds since epoch

        Parameter ``latitude``:
            latitude in °

        Parameter ``longitude``:
            longitude in °
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools.vectorinterpolators.t_extr_mode = t_extr_mode.extrapolate) -> None: 
        """
        Set the extrapolation mode for all interpolators

        Parameter ``extrapolation_mode``:
            extrapolate, fail or nearest
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def interpolator_attitude(self) -> themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator:
        """
        < interpolator that stores attitude data (pitch and roll)

        :type: themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator
        """
    @interpolator_attitude.setter
    def interpolator_attitude(self, arg1: themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator) -> None:
        """
        < interpolator that stores attitude data (pitch and roll)
        """
    @property
    def interpolator_depth(self) -> themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator that stores depth data (depth, positive downwards) <
        [m]

        :type: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator
        """
    @interpolator_depth.setter
    def interpolator_depth(self, arg1: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator) -> None:
        """
        < interpolator that stores depth data (depth, positive downwards) <
        [m]
        """
    @property
    def interpolator_heading(self) -> themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator:
        """
        < interpolator that stores compass data (yaw/heading) [°]

        :type: themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator
        """
    @interpolator_heading.setter
    def interpolator_heading(self, arg1: themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator) -> None:
        """
        < interpolator that stores compass data (yaw/heading) [°]
        """
    @property
    def interpolator_heave(self) -> themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator that stores heave data (relative change in depth, <
        positive upwards) [m]

        :type: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator
        """
    @interpolator_heave.setter
    def interpolator_heave(self, arg1: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator) -> None:
        """
        < interpolator that stores heave data (relative change in depth, <
        positive upwards) [m]
        """
    @property
    def interpolator_latitude(self) -> themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator for the latitude data

        :type: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator
        """
    @interpolator_latitude.setter
    def interpolator_latitude(self, arg1: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator) -> None:
        """
        < interpolator for the latitude data
        """
    @property
    def interpolator_longitude(self) -> themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator for the longitude data

        :type: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator
        """
    @interpolator_longitude.setter
    def interpolator_longitude(self, arg1: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator) -> None:
        """
        < interpolator for the longitude data
        """
    @property
    def sensor_configuration(self) -> SensorConfiguration:
        """
        < sensor configuration that stores the offsets

        :type: SensorConfiguration
        """
    @sensor_configuration.setter
    def sensor_configuration(self, arg1: SensorConfiguration) -> None:
        """
        < sensor configuration that stores the offsets
        """
    __hash__ = None
    pass
class NavigationInterpolatorLocal():
    """
    The NavInterpolator class: Interpolate navigation (northing/easting no
    zone specified) values and attitude information and transform the
    values using the offsets specified in the sensor configuration class
    """
    def __call__(self, target_id: str, timestamp: float) -> datastructures.GeoLocationLocal: 
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
    def __copy__(self) -> NavigationInterpolatorLocal: ...
    def __deepcopy__(self, arg0: dict) -> NavigationInterpolatorLocal: ...
    def __eq__(self, other: NavigationInterpolatorLocal) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self, sensor_configuration: SensorConfiguration, extrapolation_mode: themachinethatgoesping.tools.vectorinterpolators.t_extr_mode = t_extr_mode.extrapolate) -> None: 
        """
        Construct a new i navigationinterpolator interface

        Parameter ``extrapolation_mode``:
            extrapolate, fail or nearest
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
    @typing.overload
    def add_target(self, target_id: str, target_offsets: datastructures.PositionalOffsets) -> None: 
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

        add a target sensor with positional offsets

        Parameter ``target_id``:
            name of the target sensor

        Parameter ``sensor_offsets``:
            structure that contains the sensor position
        """
    @typing.overload
    def add_target(self, target_id: str, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None: ...
    def compute_target_position(self, target_id: str, timestamp: float) -> datastructures.GeoLocationLocal: 
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
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NavigationInterpolatorLocal: 
        """
        create T_CLASS object from bytearray
        """
    def get_sensor_data(self, timestamp: float) -> datastructures.SensorDataLocal: 
        """
        Interpolate the saved sensor data for a specified timestamp stamp

        Parameter ``timestamp``:
            timestamp in seconds since epoch

        Returns:
            data structure that contains the sensor data interpolated for the
            given timestamp stamp
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    def set_data_attitude(self, timestamp: typing.List[float], pitch: typing.List[float], roll: typing.List[float]) -> None: 
        """
        Set the attitude data (no yaw, ythis is set in set_data_heading)

        Parameter ``timestamp``:
            in seconds since epoch

        Parameter ``pitch``:
            in °, positive is bow up

        Parameter ``roll``:
            in °, positive is port up
        """
    def set_data_depth(self, timestamp: typing.List[float], depth: typing.List[float]) -> None: 
        """
        Set the depth data

        Parameter ``timestamp``:
            in seconds since epoch

        Parameter ``depth``:
            in meters, positive downwards
        """
    def set_data_heading(self, timestamp: typing.List[float], heading: typing.List[float]) -> None: 
        """
        Set the compass data

        Parameter ``timestamp``:
            in seconds since epoch

        Parameter ``heading``:
            in °, positive clockwise (north is 0°)
        """
    def set_data_heave(self, timestamp: typing.List[float], heave: typing.List[float]) -> None: 
        """
        Set the heave data

        Parameter ``timestamp``:
            in seconds since epoch

        Parameter ``heave``:
            in meters, positive upwards
        """
    def set_data_position(self, timestamp: typing.List[float], northing: typing.List[float], easting: typing.List[float]) -> None: 
        """
        Set the data of the position system (northing, easting)

        Parameter ``timestamp``:
            in seconds since epoch

        Parameter ``northing``:
            northing in meters

        Parameter ``easting``:
            easting in meters
        """
    def set_extrapolation_mode(self, extrapolation_mode: themachinethatgoesping.tools.vectorinterpolators.t_extr_mode = t_extr_mode.extrapolate) -> None: 
        """
        Set the extrapolation mode for all interpolators

        Parameter ``extrapolation_mode``:
            extrapolate, fail or nearest
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def interpolator_attitude(self) -> themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator:
        """
        < interpolator that stores attitude data (pitch and roll)

        :type: themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator
        """
    @interpolator_attitude.setter
    def interpolator_attitude(self, arg1: themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator) -> None:
        """
        < interpolator that stores attitude data (pitch and roll)
        """
    @property
    def interpolator_depth(self) -> themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator that stores depth data (depth, positive downwards) <
        [m]

        :type: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator
        """
    @interpolator_depth.setter
    def interpolator_depth(self, arg1: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator) -> None:
        """
        < interpolator that stores depth data (depth, positive downwards) <
        [m]
        """
    @property
    def interpolator_easting(self) -> themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator for the easting data

        :type: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator
        """
    @interpolator_easting.setter
    def interpolator_easting(self, arg1: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator) -> None:
        """
        < interpolator for the easting data
        """
    @property
    def interpolator_heading(self) -> themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator:
        """
        < interpolator that stores compass data (yaw/heading) [°]

        :type: themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator
        """
    @interpolator_heading.setter
    def interpolator_heading(self, arg1: themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator) -> None:
        """
        < interpolator that stores compass data (yaw/heading) [°]
        """
    @property
    def interpolator_heave(self) -> themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator that stores heave data (relative change in depth, <
        positive upwards) [m]

        :type: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator
        """
    @interpolator_heave.setter
    def interpolator_heave(self, arg1: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator) -> None:
        """
        < interpolator that stores heave data (relative change in depth, <
        positive upwards) [m]
        """
    @property
    def interpolator_northing(self) -> themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator:
        """
        < interpolator for the northing data

        :type: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator
        """
    @interpolator_northing.setter
    def interpolator_northing(self, arg1: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator) -> None:
        """
        < interpolator for the northing data
        """
    @property
    def sensor_configuration(self) -> SensorConfiguration:
        """
        < sensor configuration that stores the offsets

        :type: SensorConfiguration
        """
    @sensor_configuration.setter
    def sensor_configuration(self, arg1: SensorConfiguration) -> None:
        """
        < sensor configuration that stores the offsets
        """
    __hash__ = None
    pass
class SensorConfiguration():
    """
    A coordinate system that allows for specifying sensor offsets (e.g.
    gps antenna and attitude sensor) and target offsets (e.g. MBES). Call
    the class and specify target_id and current sensor data to derive the
    geolocation and attitude of the specified targets
    """
    def __copy__(self) -> SensorConfiguration: ...
    def __deepcopy__(self, arg0: dict) -> SensorConfiguration: ...
    def __eq__(self, other: SensorConfiguration) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self) -> None: 
        """
        Construct a new, empty Sensor Coordinate System object After
        construction: add sensor offsets and targets (offsets) Then compute
        target positions for sensor data
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
    @typing.overload
    def add_target(self, target_id: str, target_offsets: datastructures.PositionalOffsets) -> None: 
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

        add a target (e.g. MBES) with offsets to the sensor position system

        Parameter ``target_id``:
            name of the target for reference

        Parameter ``target_offsets``:
            mounting offsets of the target
        """
    @typing.overload
    def add_target(self, target_id: str, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None: ...
    @typing.overload
    def compute_target_position(self, target_id: str, sensor_data: datastructures.SensorData) -> datastructures.GeoLocationLocal: 
        """
        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"

        Parameter ``target_id``:
            name of the target (e.g. "MBES")

        Parameter ``sensor_data``:
            SensorDataLatLon / this structure includes latitude and longitude
            information

        Returns:
            datastructures::GeoLocationLatLon / this structure includes
            latitude and longitude information

        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"

        Parameter ``target_id``:
            name of the target (e.g. "MBES")

        Parameter ``sensor_data``:
            SensorDataUTM / this structure includes northing/easting and utm
            zone or hemisphere information

        Returns:
            datastructures::GeoLocationUTM / this structure includes
            northing/easting and utm zone or hemisphere information

        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"

        Parameter ``target_id``:
            name of the target (e.g. "MBES")

        Parameter ``sensor_data``:
            SensorDataLocal / this structure includes northing/easting but no
            zone or hemisphere information

        Returns:
            datastructures::GeoLocationLocal / this structure includes
            northing/easting but no zone or hemisphere information

        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"

        Parameter ``target_id``:
            name of the target (e.g. "MBES")

        Parameter ``sensor_data``:
            SensorData / this structure includes no coordinate information

        Returns:
            datastructures::GeoLocationLocal / this structure includes
            northing and east, which are set relative to the sensor coordinate
            system center
        """
    @typing.overload
    def compute_target_position(self, target_id: str, sensor_data: datastructures.SensorDataLatLon) -> datastructures.GeoLocationLatLon: ...
    @typing.overload
    def compute_target_position(self, target_id: str, sensor_data: datastructures.SensorDataLocal) -> datastructures.GeoLocationLocal: ...
    @typing.overload
    def compute_target_position(self, target_id: str, sensor_data: datastructures.SensorDataUTM) -> datastructures.GeoLocationUTM: ...
    def copy(self) -> SensorConfiguration: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensorConfiguration: 
        """
        create T_CLASS object from bytearray
        """
    def get_offsets_attitude_source(self) -> datastructures.PositionalOffsets: 
        """
        Get the attitude sensor offsets

        Returns:
            const datastructures::PositionalOffsets& offsets of the attitude
            sensor
        """
    def get_offsets_depth_source(self) -> datastructures.PositionalOffsets: 
        """
        Get the registered depth sensor offsets

        Returns:
            const datastructures::PositionalOffsets& offsets of the depth
            sensor
        """
    def get_offsets_heading_source(self) -> datastructures.PositionalOffsets: 
        """
        Get the registered compass offsets

        Returns:
            const datastructures::PositionalOffsets& offsets of the compass
        """
    def get_offsets_position_source(self) -> datastructures.PositionalOffsets: 
        """
        Get the registered position system offsets

        Returns:
            const datastructures::PositionalOffsets& offsets of the position
            system
        """
    def get_offsets_target(self, target_id: str) -> datastructures.PositionalOffsets: 
        """
        Get stored target offsets of a specified target

        Parameter ``target_id``:
            name of the registered target

        Returns:
            const datastructures::PositionalOffsets& offsets of the target
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
    def set_offsets_attitude_source(self, sensor_offsets: datastructures.PositionalOffsets) -> None: 
        """
        Set the attitude sensor offsets

        Parameter ``sensor_offsets``:
            offsets structure (only yaw, pitch and roll are used)

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
    def set_offsets_attitude_source(self, yaw: float, pitch: float, roll: float) -> None: ...
    @typing.overload
    def set_offsets_depth_source(self, sensor_offsets: datastructures.PositionalOffsets) -> None: 
        """
        Set the depth sensor offsets

        Parameter ``x``:
            x-offset of the depth sensor (in meters, positive forward)

        Parameter ``y``:
            y-offset of the depth sensor (in meters, positive starboard)

        Parameter ``z``:
            z-offset of the depth sensor (in meters, positive down)

        Set the depth sensor offsets

        Parameter ``sensor_offsets``:
            offsets structure (only x, y and z are used)
        """
    @typing.overload
    def set_offsets_depth_source(self, x: float, y: float, z: float) -> None: ...
    @typing.overload
    def set_offsets_heading_source(self, sensor_offsets: datastructures.PositionalOffsets) -> None: 
        """
        Set the compass offsets

        Parameter ``yaw``:
            yaw offset of the compass (right-handed around the z-axis) (in
            degrees, 90° = east)

        Set the compass offsets

        Parameter ``sensor_offsets``:
            offsets structure (only yaw is used)
        """
    @typing.overload
    def set_offsets_heading_source(self, yaw: float) -> None: ...
    @typing.overload
    def set_offsets_position_source(self, sensor_offsets: datastructures.PositionalOffsets) -> None: 
        """
        Set the position system offsets

        Parameter ``x``:
            x-offset of the depth sensor (in meters, positive forward)

        Parameter ``y``:
            y-offset of the depth sensor (in meters, positive starboard)

        Parameter ``z``:
            z-offset of the depth sensor (in meters, positive down)

        Set the position system offsets

        Parameter ``sensor_offsets``:
            offsets structure (only x, y and z are used)
        """
    @typing.overload
    def set_offsets_position_source(self, x: float, y: float, z: float) -> None: ...
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    __hash__ = None
    pass
class ostream_redirect():
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...
    def __init__(self, stdout: bool = True, stderr: bool = True) -> None: ...
    pass
__version__ = '0.5.7'
