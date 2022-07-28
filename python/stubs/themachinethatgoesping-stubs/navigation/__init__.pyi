"""Python module to store, interpolate and transform navigation data"""
from __future__ import annotations
import themachinethatgoesping.navigation
import typing

__all__ = [
    "SensorCoordinateSystem",
    "navdata",
    "navtools",
    "ostream_redirect"
]


class SensorCoordinateSystem():
    """
    A coordinate system that allows for specifying sensor offsets (e.g.
    gps antenna and motion sensor) and target offsets (e.g. MBES). Call
    the class and specify target_id and current sensor data to derive the
    geolocation and attitude of the specified targets
    """
    @typing.overload
    def __call__(self, target_id: str, sensor_data: navdata.SensorData) -> navdata.GeoLocationLocal: 
        """
        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"

        Parameter ``target_id``:
            name of the target (e.g. "MBES")

        Parameter ``sensor_data``:
            SensorDataLatLon / this structure includes latitude and longitude
            informatoin

        Returns:
            navdata::GeoLocationLatLon / this structure includes latitude and
            longitude informatoin

        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"

        Parameter ``target_id``:
            name of the target (e.g. "MBES")

        Parameter ``sensor_data``:
            SensorDataUTM / this structure includes northing/easting and utm
            zone or hemisphere informatoin

        Returns:
            navdata::GeoLocationUTM / this structure includes northing/easting
            and utm zone or hemisphere informatoin

        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"

        Parameter ``target_id``:
            name of the target (e.g. "MBES")

        Parameter ``sensor_data``:
            SensorDataLocal / this structure includes northing/easting but no
            zone or hemisphere informatoin

        Returns:
            navdata::GeoLocationLocal / this structure includes
            northing/easting but no zone or hemisphere informatoin

        Compute the position of the target "target_id" based on the sensor
        data "sensor_data"

        Parameter ``target_id``:
            name of the target (e.g. "MBES")

        Parameter ``sensor_data``:
            SensorData / this structure includes no coordinate information

        Returns:
            navdata::GeoLocationLocal / this structure includes northing and
            east, which are set relative to the sensor coordinate system
            center
        """
    @typing.overload
    def __call__(self, target_id: str, sensor_data: navdata.SensorDataLatLon) -> navdata.GeoLocationLatLon: ...
    @typing.overload
    def __call__(self, target_id: str, sensor_data: navdata.SensorDataLocal) -> navdata.GeoLocationLocal: ...
    @typing.overload
    def __call__(self, target_id: str, sensor_data: navdata.SensorDataUTM) -> navdata.GeoLocationUTM: ...
    def __copy__(self) -> SensorCoordinateSystem: ...
    def __eq__(self, other: SensorCoordinateSystem) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self) -> None: 
        """
        Construct a new, empty Sensor Coordinate System object After
        construction: add sensor offsets and targets (offstes) Then compute
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
    def copy(self) -> SensorCoordinateSystem: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensorCoordinateSystem: 
        """
        create T_CLASS object from bytearray
        """
    def get_compass_offsets(self) -> navdata.PositionalOffsets: 
        """
        Get the registered compass offsets

        Returns:
            const navdata::PositionalOffsets& offsets of the compass
        """
    def get_depth_sensor_offsets(self) -> navdata.PositionalOffsets: 
        """
        Get the registered depth sensor offsets

        Returns:
            const navdata::PositionalOffsets& offsets of the depth sensor
        """
    def get_motion_sensor_offsets(self) -> navdata.PositionalOffsets: 
        """
        Get the motion sensor offsets

        Returns:
            const navdata::PositionalOffsets& offsets of the motion sensor
        """
    def get_position_system_offsets(self) -> navdata.PositionalOffsets: 
        """
        Get the registered position system offsets

        Returns:
            const navdata::PositionalOffsets& offsets of the position system
        """
    def get_target_offsets(self, target_id: str) -> navdata.PositionalOffsets: 
        """
        Get stored target offsets of a specified target

        Parameter ``target_id``:
            name of the registered target

        Returns:
            const navdata::PositionalOffsets& offsets of the target
        """
    def info_string(self) -> str: 
        """
        Return object information as string
        """
    def print(self) -> None: 
        """
        Print object information
        """
    @typing.overload
    def register_target(self, target_id: str, target_offsets: navdata.PositionalOffsets) -> None: 
        """
        register a target (e.g. MBES) with offsets to the sensor position
        system

        Parameter ``target_id``:
            name of the target for reference

        Parameter ``x``:
            x-offset of the target (in meters, positive forward)

        Parameter ``y``:
            y-offset of the target (in meters, positive starboard)

        Parameter ``z``:
            z-offset of the target (in meters, positive down)

        Parameter ``yaw``:
            yaw offset of the target (righthanded around the z-axis) (in
            degrees, 90° = east)

        Parameter ``pitch``:
            pitch offset of the target (righthanded around the y-axis) (in
            degrees, positive = bow up)

        Parameter ``roll``:
            roll offset of the target (righthanded around the x-axis) (in
            degrees, positive = port up)

        register a target (e.g. MBES) with offsets to the sensor position
        system

        Parameter ``target_id``:
            name of the target for reference

        Parameter ``target_offsets``:
            mounting offsets of the target
        """
    @typing.overload
    def register_target(self, target_id: str, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None: ...
    @typing.overload
    def set_compass_offsets(self, sensor_offsets: navdata.PositionalOffsets) -> None: 
        """
        Set the compass offsets

        Parameter ``yaw``:
            yaw offset of the compass (righthanded around the z-axis) (in
            degrees, 90° = east)

        Set the compass offsets

        Parameter ``sensor_offsets``:
            offsets structure (only yaw is used)
        """
    @typing.overload
    def set_compass_offsets(self, yaw: float) -> None: ...
    @typing.overload
    def set_depth_sensor_offsets(self, sensor_offsets: navdata.PositionalOffsets) -> None: 
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
    def set_depth_sensor_offsets(self, x: float, y: float, z: float) -> None: ...
    @typing.overload
    def set_motion_sensor_offsets(self, sensor_offsets: navdata.PositionalOffsets) -> None: 
        """
        Set the motion sensor offsets

        Parameter ``sensor_offsets``:
            offsets structure (only yaw, pitch and roll are used)

        Set the motion sensor offsets

        Parameter ``yaw``:
            yaw offset of the motion sensor (righthanded around the z-axis)
            (in degrees, 90° = east)

        Parameter ``pitch``:
            pitch offset of the motion sensor (righthanded around the y-axis)
            (in degrees, positive = bow up)

        Parameter ``roll``:
            roll offset of the motion sensor (righthanded around the x-axis)
            (in degrees, positive = port up)
        """
    @typing.overload
    def set_motion_sensor_offsets(self, yaw: float, pitch: float, roll: float) -> None: ...
    @typing.overload
    def set_position_system_offsets(self, sensor_offsets: navdata.PositionalOffsets) -> None: 
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
    def set_position_system_offsets(self, x: float, y: float, z: float) -> None: ...
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
