"""Python module to store, interpolate and transform navigation data"""
from __future__ import annotations
import themachinethatgoesping.navigation
import typing

__all__ = [
    "SensorConfiguration",
    "datastructures",
    "navtools",
    "ostream_redirect"
]


class SensorConfiguration():
    """
    A coordinate system that allows for specifying sensor offsets (e.g.
    gps antenna and motion sensor) and target offsets (e.g. MBES). Call
    the class and specify target_id and current sensor data to derive the
    geolocation and attitude of the specified targets
    """
    def __copy__(self) -> SensorConfiguration: ...
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
    def get_compass_offsets(self) -> datastructures.PositionalOffsets: 
        """
        Get the registered compass offsets

        Returns:
            const datastructures::PositionalOffsets& offsets of the compass
        """
    def get_depth_sensor_offsets(self) -> datastructures.PositionalOffsets: 
        """
        Get the registered depth sensor offsets

        Returns:
            const datastructures::PositionalOffsets& offsets of the depth
            sensor
        """
    def get_motion_sensor_offsets(self) -> datastructures.PositionalOffsets: 
        """
        Get the motion sensor offsets

        Returns:
            const datastructures::PositionalOffsets& offsets of the motion
            sensor
        """
    def get_position_system_offsets(self) -> datastructures.PositionalOffsets: 
        """
        Get the registered position system offsets

        Returns:
            const datastructures::PositionalOffsets& offsets of the position
            system
        """
    def get_target_offsets(self, target_id: str) -> datastructures.PositionalOffsets: 
        """
        Get stored target offsets of a specified target

        Parameter ``target_id``:
            name of the registered target

        Returns:
            const datastructures::PositionalOffsets& offsets of the target
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
    def set_compass_offsets(self, sensor_offsets: datastructures.PositionalOffsets) -> None: 
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
    def set_compass_offsets(self, yaw: float) -> None: ...
    @typing.overload
    def set_depth_sensor_offsets(self, sensor_offsets: datastructures.PositionalOffsets) -> None: 
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
    def set_motion_sensor_offsets(self, sensor_offsets: datastructures.PositionalOffsets) -> None: 
        """
        Set the motion sensor offsets

        Parameter ``sensor_offsets``:
            offsets structure (only yaw, pitch and roll are used)

        Set the motion sensor offsets

        Parameter ``yaw``:
            yaw offset of the motion sensor (right-handed around the z-axis)
            (in degrees, 90° = east)

        Parameter ``pitch``:
            pitch offset of the motion sensor (right-handed around the y-axis)
            (in degrees, positive = bow up)

        Parameter ``roll``:
            roll offset of the motion sensor (right-handed around the x-axis)
            (in degrees, positive = port up)
        """
    @typing.overload
    def set_motion_sensor_offsets(self, yaw: float, pitch: float, roll: float) -> None: ...
    @typing.overload
    def set_position_system_offsets(self, sensor_offsets: datastructures.PositionalOffsets) -> None: 
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
