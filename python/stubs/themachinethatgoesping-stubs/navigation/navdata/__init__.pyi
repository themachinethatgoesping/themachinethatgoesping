"""Submodule that contains navdata that store navigation data or navigation sensor input"""
from __future__ import annotations
import themachinethatgoesping.navigation.navdata
import typing

__all__ = [
    "GeoLocation",
    "GeoLocationLatLon",
    "GeoLocationLocal",
    "GeoLocationUTM",
    "PositionalOffsets",
    "SensorData",
    "SensorDataLatLon",
    "SensorDataLocal",
    "SensorDataUTM"
]


class GeoLocation():
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) This structure does not store any coordinates except the depth
    (z)
    """
    def __copy__(self) -> GeoLocation: ...
    def __eq__(self, rhs: GeoLocation) -> bool: 
        """
        Check if two GeoLocation objects are equal

        Parameter ``rhs``:
            $Returns:

        true if equal

        Returns:
            false if not equal
        """
    def __getstate__(self) -> bytes: ...
    @staticmethod
    @typing.overload
    def __init__(*args, **kwargs) -> typing.Any: 
        """
        Construct a new Position object

        Construct a new Position object

        Construct a new Position object

        Construct a new GeoLocation object

        Parameter ``z``:
            in m, positive downwards

        Parameter ``yaw``:
            in °, 0° is north, 90° is east

        Parameter ``pitch``:
            in °, positive means bow up

        Parameter ``roll``:
            in °, positive means port up
        """
    @typing.overload
    def __init__(self, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> GeoLocation: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeoLocation: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self) -> str: 
        """
        Return object information as string
        """
    def print(self) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def pitch(self) -> float:
        """
        < in °, positive means bow up

        :type: float
        """
    @pitch.setter
    def pitch(self, arg0: float) -> None:
        """
        < in °, positive means bow up
        """
    @property
    def roll(self) -> float:
        """
        < in °, positive means port up

        :type: float
        """
    @roll.setter
    def roll(self, arg0: float) -> None:
        """
        < in °, positive means port up
        """
    @property
    def yaw(self) -> float:
        """
        < in °, 0° is north, 90° is east

        :type: float
        """
    @yaw.setter
    def yaw(self, arg0: float) -> None:
        """
        < in °, 0° is north, 90° is east
        """
    @property
    def z(self) -> float:
        """
        < in m, positive downwards

        :type: float
        """
    @z.setter
    def z(self, arg0: float) -> None:
        """
        < in m, positive downwards
        """
    __hash__ = None
    pass
class GeoLocationLatLon(GeoLocation):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) Unlike the base GeoLocation object, this also stores latitude
    and longitude coordinates
    """
    def __copy__(self) -> GeoLocationLatLon: ...
    def __eq__(self, rhs: GeoLocationLatLon) -> bool: 
        """
        Check if two GeoLocationLatLon objects are equal

        Parameter ``rhs``:
            $Returns:

        true if equal

        Returns:
            false if not equal
        """
    def __getstate__(self) -> bytes: ...
    @staticmethod
    @typing.overload
    def __init__(*args, **kwargs) -> typing.Any: 
        """
        Construct a new Sensor Data Lat Lon object using a base sensor data
        object

        Parameter ``location``:
            $Parameter ``latitude``:

        in °, positive northwards

        Parameter ``longitude``:
            in °, positive eastwards

        Construct an GeoLocationLatLon object from an existing GeoLocationUTM
        object (this allows for implicit conversion from GeoLocationUTM class)

        Construct a new GeoLocationLatLon object

        Parameter ``latitude``:
            in °, positive northwards

        Parameter ``longitude``:
            in °, positive eastwards

        Parameter ``z``:
            in m, positive downwards

        Parameter ``yaw``:
            in °, 0° is north, 90° is east

        Parameter ``pitch``:
            in °, positive means bow up

        Parameter ``roll``:
            in °, positive means port up
        """
    @typing.overload
    def __init__(self, latitude: float = 0, longitude: float = 0, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None: ...
    @typing.overload
    def __init__(self, location: GeoLocation, latitude: float, longitude: float) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> GeoLocationLatLon: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeoLocationLatLon: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self) -> str: 
        """
        Return object information as string
        """
    def print(self) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def latitude(self) -> float:
        """
        < in °, positive northwards

        :type: float
        """
    @latitude.setter
    def latitude(self, arg0: float) -> None:
        """
        < in °, positive northwards
        """
    @property
    def longitude(self) -> float:
        """
        < in °, positive eastwards

        :type: float
        """
    @longitude.setter
    def longitude(self, arg0: float) -> None:
        """
        < in °, positive eastwards
        """
    __hash__ = None
    pass
class GeoLocationLocal(GeoLocation):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) unlike the default GeoLocation structure, this object stores
    local northing and easting coordinates. These coordinates can be
    converted to UTM coordinates if the zone and hemisphere are known.
    """
    def __copy__(self) -> GeoLocationLocal: ...
    def __eq__(self, rhs: GeoLocationLocal) -> bool: ...
    def __getstate__(self) -> bytes: ...
    @staticmethod
    @typing.overload
    def __init__(*args, **kwargs) -> typing.Any: 
        """
        Construct a new Sensor Position object (all offsets set to 0)

        Construct a new GeoLocationLocal object

        Parameter ``location``:
            $Parameter ``northing``:

        in m, positive northwards

        Parameter ``easting``:
            in m, positive eastwards

        Construct a new GeoLocationLocal object

        Parameter ``northing``:
            in m, positive northwards

        Parameter ``easting``:
            in m, positive eastwards

        Parameter ``z``:
            in m, positive downwards

        Parameter ``yaw``:
            in °, 0° is north, 90° is east

        Parameter ``pitch``:
            in °, positive means bow up

        Parameter ``roll``:
            in °, positive means port up
        """
    @typing.overload
    def __init__(self, geolocation: GeoLocation, northing: float, easting: float) -> None: ...
    @typing.overload
    def __init__(self, northing: float = 0, easting: float = 0, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> GeoLocationLocal: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeoLocationLocal: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self) -> str: 
        """
        Return object information as string
        """
    def print(self) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def easting(self) -> float:
        """
        < in m, positive eastwards

        :type: float
        """
    @easting.setter
    def easting(self, arg0: float) -> None:
        """
        < in m, positive eastwards
        """
    @property
    def northing(self) -> float:
        """
        < in m, positive northwards

        :type: float
        """
    @northing.setter
    def northing(self, arg0: float) -> None:
        """
        < in m, positive northwards
        """
    __hash__ = None
    pass
class GeoLocationUTM(GeoLocationLocal, GeoLocation):
    def __copy__(self) -> GeoLocationUTM: ...
    def __eq__(self, rhs: GeoLocationUTM) -> bool: ...
    def __getstate__(self) -> bytes: ...
    @typing.overload
    def __init__(self, geolocationlatlon: GeoLocationLatLon, setzone: int = -1) -> None: 
        """
        Construct an GeoLocationUTM object from an existing GeoLocationLocal
        object (using a known zone and hemisphere)

        Parameter ``location_local``:
            $Parameter ``zone``:

        UTM/UPS zone number

        Parameter ``northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere

        Construct an GeoLocationUTM object from an existing GeoLocationLatLon
        object (this allows for implicit conversion from GeoLocationLatLon
        class)

        Construct a new GeoLocationUTM object

        Parameter ``northing``:
            in m, positive northwards

        Parameter ``easting``:
            in m, positive eastwards

        Parameter ``zone``:
            UTM/UPS zone number

        Parameter ``northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere

        Parameter ``z``:
            in m, positive downwards

        Parameter ``yaw``:
            in °, 0° is north, 90° is east

        Parameter ``pitch``:
            in °, positive means bow up

        Parameter ``roll``:
            in °, positive means port up
        """
    @typing.overload
    def __init__(self, geolocationlatlon: GeoLocationLocal, zone: int, northern_hemisphere: bool) -> None: ...
    @typing.overload
    def __init__(self, northing: float = 0, easting: float = 0, zone: int = 0, northern_hemisphere: bool = True, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> GeoLocationUTM: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeoLocationUTM: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self) -> str: 
        """
        Return object information as string
        """
    def print(self) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def northern_hemisphere(self) -> bool:
        """
        < if true: northern hemisphere, else: southern hemisphere

        :type: bool
        """
    @northern_hemisphere.setter
    def northern_hemisphere(self, arg0: bool) -> None:
        """
        < if true: northern hemisphere, else: southern hemisphere
        """
    @property
    def zone(self) -> int:
        """
        < UTM/UPS zone number

        :type: int
        """
    @zone.setter
    def zone(self, arg0: int) -> None:
        """
        < UTM/UPS zone number
        """
    __hash__ = None
    pass
class PositionalOffsets():
    """
    A structure to store positional offsets (e.g. of a sensor) relative to
    the vessel coordinate system
    """
    def __copy__(self) -> PositionalOffsets: ...
    def __eq__(self, other: PositionalOffsets) -> bool: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None: 
        """
        Construct a new PositionalOffsets object

        Parameter ``x``:
            in m, positive forward

        Parameter ``y``:
            in m, positive starboard

        Parameter ``z``:
            in m, positive downwards

        Parameter ``yaw``:
            in °, 0° is north, 90° is east

        Parameter ``pitch``:
            in °, positive means bow up

        Parameter ``roll``:
            in °, positive means port up
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
    def copy(self) -> PositionalOffsets: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> PositionalOffsets: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self) -> str: 
        """
        Return object information as string
        """
    def print(self) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def pitch(self) -> float:
        """
        < in °, positive means bow up

        :type: float
        """
    @pitch.setter
    def pitch(self, arg0: float) -> None:
        """
        < in °, positive means bow up
        """
    @property
    def roll(self) -> float:
        """
        < in °, positive means port up

        :type: float
        """
    @roll.setter
    def roll(self, arg0: float) -> None:
        """
        < in °, positive means port up
        """
    @property
    def x(self) -> float:
        """
        < in m, positive forward

        :type: float
        """
    @x.setter
    def x(self, arg0: float) -> None:
        """
        < in m, positive forward
        """
    @property
    def y(self) -> float:
        """
        < in m, positive starboard

        :type: float
        """
    @y.setter
    def y(self, arg0: float) -> None:
        """
        < in m, positive starboard
        """
    @property
    def yaw(self) -> float:
        """
        < in °, 0° is north, 90° is east

        :type: float
        """
    @yaw.setter
    def yaw(self, arg0: float) -> None:
        """
        < in °, 0° is north, 90° is east
        """
    @property
    def z(self) -> float:
        """
        < in m, positive downwards

        :type: float
        """
    @z.setter
    def z(self, arg0: float) -> None:
        """
        < in m, positive downwards
        """
    __hash__ = None
    pass
class SensorData():
    """
    A structure to store a georeferenced location and attitude data from
    different sensors (e.g. IMU, etc.) No gps coordinates are stored in
    this structure (only depth).
    """
    def __copy__(self) -> SensorData: ...
    def __eq__(self, other: SensorData) -> bool: 
        """
        Check if two SensorData objects are equal

        Parameter ``rhs``:
            $Returns:

        true if equal

        Returns:
            false if not equal
        """
    def __getstate__(self) -> bytes: ...
    @staticmethod
    @typing.overload
    def __init__(*args, **kwargs) -> typing.Any: 
        """
        Construct a new SensorData object

        Construct a new SensorData object

        Construct a new SensorData object

        Construct a new SensorData object

        Parameter ``gps_z``:
            in m, positive downwards

        Parameter ``heave_heave``:
            from heave sensor, will be added to gps_z in m, positive upwards

        Parameter ``compass_heading``:
            from compass, replaces imu_yaw if not NAN, in °, 0° is north, 90°
            is east

        Parameter ``imu_yaw``:
            in °, 0° is north, 90° is east

        Parameter ``imu_pitch``:
            in °, positive means bow up

        Parameter ``imu_roll``:
            in °, positive means port up
        """
    @typing.overload
    def __init__(self, gps_z: float = 0, heave_heave: float = 0, compass_heading: float = 0, imu_yaw: float = 0, imu_pitch: float = 0, imu_roll: float = 0) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> SensorData: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensorData: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self) -> str: 
        """
        Return object information as string
        """
    def print(self) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def compass_heading(self) -> float:
        """
        :type: float
        """
    @compass_heading.setter
    def compass_heading(self, arg0: float) -> None:
        pass
    @property
    def gps_z(self) -> float:
        """
        < in m, positive downwards

        :type: float
        """
    @gps_z.setter
    def gps_z(self, arg0: float) -> None:
        """
        < in m, positive downwards
        """
    @property
    def heave_heave(self) -> float:
        """
        < from heave sensor, will be added to gps_z in m, positive upwards

        :type: float
        """
    @heave_heave.setter
    def heave_heave(self, arg0: float) -> None:
        """
        < from heave sensor, will be added to gps_z in m, positive upwards
        """
    @property
    def imu_pitch(self) -> float:
        """
        < from motion sensor, in °, positive means bow up

        :type: float
        """
    @imu_pitch.setter
    def imu_pitch(self, arg0: float) -> None:
        """
        < from motion sensor, in °, positive means bow up
        """
    @property
    def imu_roll(self) -> float:
        """
        < from motion sensor, in °, positive means port up

        :type: float
        """
    @imu_roll.setter
    def imu_roll(self, arg0: float) -> None:
        """
        < from motion sensor, in °, positive means port up
        """
    @property
    def imu_yaw(self) -> float:
        """
        < from motion sensor, in °, 0° is north, 90° is east

        :type: float
        """
    @imu_yaw.setter
    def imu_yaw(self, arg0: float) -> None:
        """
        < from motion sensor, in °, 0° is north, 90° is east
        """
    __hash__ = None
    pass
class SensorDataLatLon(SensorData):
    """
    A structure to store a georeferenced location and attitude data from
    different sensors (e.g. GPS, IMU, etc.)
    """
    def __copy__(self) -> SensorDataLatLon: ...
    def __eq__(self, other: SensorDataLatLon) -> bool: 
        """
        Check if two SensorDataLatLon objects are equal

        Parameter ``rhs``:
            $Returns:

        true if equal

        Returns:
            false if not equal
        """
    def __getstate__(self) -> bytes: ...
    @staticmethod
    @typing.overload
    def __init__(*args, **kwargs) -> typing.Any: 
        """
        Construct a new Sensor Data Lat Lon object using a base sensor data
        object

        Parameter ``data``:
            $Parameter ``gps_latitude``:

        in °, positive northwards

        Parameter ``gps_longitude``:
            in °, positive eastwards

        Construct an SensorDataLatLon object from an existing SensorDataUTM
        object (this allows for implicit conversion from SensorDataUTM class)

        Construct a new SensorDataLatLon object

        Parameter ``gps_latitude``:
            in °, positive northwards

        Parameter ``gps_longitude``:
            in °, positive eastwards

        Parameter ``gps_z``:
            in m, positive downwards

        Parameter ``heave_heave``:
            from heave sensor, will be added to gps_z in m, positive upwards

        Parameter ``compass_heading``:
            from compass, replaces imu_yaw if not NAN, in °, 0° is north, 90°
            is east

        Parameter ``imu_yaw``:
            in °, 0° is north, 90° is east

        Parameter ``imu_pitch``:
            in °, positive means bow up

        Parameter ``imu_roll``:
            in °, positive means port up
        """
    @typing.overload
    def __init__(self, gps_latitude: float = 0, gps_longitude: float = 0, gps_z: float = 0, heave_heave: float = 0, compass_heading: float = 0, imu_yaw: float = 0, imu_pitch: float = 0, imu_roll: float = 0) -> None: ...
    @typing.overload
    def __init__(self, sensordata: SensorData, latitude: float, longitude: float) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> SensorDataLatLon: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensorDataLatLon: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self) -> str: 
        """
        Return object information as string
        """
    def print(self) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def gps_latitude(self) -> float:
        """
        :type: float
        """
    @gps_latitude.setter
    def gps_latitude(self, arg0: float) -> None:
        pass
    @property
    def gps_longitude(self) -> float:
        """
        :type: float
        """
    @gps_longitude.setter
    def gps_longitude(self, arg0: float) -> None:
        pass
    __hash__ = None
    pass
class SensorDataLocal(SensorData):
    """
    A structure to store a georeferenced data and attitude data from
    different sensors (e.g. GPS, IMU, etc.) Unlike SensorDataUTM, this
    structure stores coordinates without zone and hemisphere information.
    """
    def __copy__(self) -> SensorDataLocal: ...
    def __eq__(self, rhs: SensorDataLocal) -> bool: 
        """
        Check if two SensorDataLocal objects are equal

        Parameter ``rhs``:
            $Returns:

        true if equal

        Returns:
            false if not equal
        """
    def __getstate__(self) -> bytes: ...
    @staticmethod
    @typing.overload
    def __init__(*args, **kwargs) -> typing.Any: 
        """
        Construct a new Sensor Position object (all offsets set to 0)

        Construct a new Sensor Data Local object using a base sensor data
        object

        Parameter ``data``:
            $Parameter ``gps_northing``:

        in m, positive northwards

        Parameter ``gps_easting``:
            in m, positive eastwards

        Construct a new SensorDataLocal object

        Parameter ``gps_northing``:
            in m, positive northwards

        Parameter ``gpd_easting``:
            in m, positive eastwards

        Parameter ``gps_z``:
            in m, positive downwards

        Parameter ``heave_heave``:
            from heave sensor, will be added to gps_z in m, positive upwards

        Parameter ``compass_heading``:
            from compass, replaces imu_yaw if not NAN, in °, 0° is north, 90°
            is east

        Parameter ``imu_yaw``:
            in °, 0° is north, 90° is east

        Parameter ``imu_pitch``:
            in °, positive means bow up

        Parameter ``imu_roll``:
            in °, positive means port up
        """
    @typing.overload
    def __init__(self, gps_northing: float = 0, gps_easting: float = 0, gps_z: float = 0, heave_heave: float = 0, compass_heading: float = 0, imu_yaw: float = 0, imu_pitch: float = 0, imu_roll: float = 0) -> None: ...
    @typing.overload
    def __init__(self, sensordata: SensorData, gps_northing: float, gps_easting: float) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> SensorDataLocal: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensorDataLocal: 
        """
        create T_CLASS object from bytearray
        """
    def info_string(self) -> str: 
        """
        Return object information as string
        """
    def print(self) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @property
    def gps_easting(self) -> float:
        """
        < in m, positive eastwards

        :type: float
        """
    @gps_easting.setter
    def gps_easting(self, arg0: float) -> None:
        """
        < in m, positive eastwards
        """
    @property
    def gps_northing(self) -> float:
        """
        < in m, positive northwards

        :type: float
        """
    @gps_northing.setter
    def gps_northing(self, arg0: float) -> None:
        """
        < in m, positive northwards
        """
    __hash__ = None
    pass
class SensorDataUTM(SensorDataLocal, SensorData):
    def __copy__(self) -> SensorDataUTM: ...
    def __eq__(self, rhs: SensorDataUTM) -> bool: 
        """
        Check if two SensorDataUTM objects are equal

        Parameter ``rhs``:
            $Returns:

        true if equal

        Returns:
            false if not equal
        """
    def __getstate__(self) -> bytes: ...
    @typing.overload
    def __init__(self, gps_northing: float = 0, gps_easting: float = 0, gps_zone: int = 0, gps_northern_hemisphere: bool = True, gps_z: float = 0, heave_heave: float = 0, compass_heading: float = 0, imu_yaw: float = 0, imu_pitch: float = 0, imu_roll: float = 0) -> None: 
        """
        Construct a new Sensor Data Local object using a base sensor data
        object

        Parameter ``data``:
            $Parameter ``gps_northing``:

        in m, positive northwards

        Parameter ``gps_easting``:
            in m, positive eastwards

        Parameter ``gps_zone``:
            UTM/UPS zone number

        Parameter ``gps_northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere

        Construct an SensorDataUTM object from an existing SensorDataLocal
        object (using a known zone and hemisphere)

        Parameter ``data_local``:
            $Parameter ``gps_zone``:

        UTM/UPS zone number

        Parameter ``gps_northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere

        Construct an SensorDataUTM object from an existing SensorDataLatLon
        object (this allows for implicit conversion from SensorDataLatLon
        class)

        Construct a new SensorDataUTM object

        Parameter ``gps_northing``:
            in m, positive northwards

        Parameter ``gpd_easting``:
            in m, positive eastwards

        Parameter ``gps_zone``:
            UTM/UPS zone number

        Parameter ``gps_northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere

        Parameter ``gps_z``:
            in m, positive downwards

        Parameter ``heave_heave``:
            from heave sensor, will be added to gps_z in m, positive upwards

        Parameter ``compass_heading``:
            from compass, replaces imu_yaw if not NAN, in °, 0° is north, 90°
            is east

        Parameter ``imu_yaw``:
            in °, 0° is north, 90° is east

        Parameter ``imu_pitch``:
            in °, positive means bow up

        Parameter ``imu_roll``:
            in °, positive means port up
        """
    @typing.overload
    def __init__(self, sensordata_local: SensorDataLocal, gps_zone: int, gps_northern_hemisphere: bool) -> None: ...
    @typing.overload
    def __init__(self, sensordatalatlon: SensorData, gps_northing: float, gps_easting: float, gps_zone: int, gps_northern_hemisphere: bool) -> None: ...
    @typing.overload
    def __init__(self, sensordatalatlon: SensorDataLatLon, setgps_zone: int = -1) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> SensorDataUTM: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensorDataUTM: 
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def from_sensordata(sensordatalatlon: SensorDataLatLon, setgps_zone: int = -1) -> SensorDataUTM: 
        """
        Construct convert a SensorDataLatLon Object to UTM

        Parameter ``data``:
            valid SensorDataLatLon object

        Parameter ``setzone``:
            set a preferred UTM zone negative means automatic, zero means UPS,
            positive means a particular UTM zone

        Returns:
            SensorDataUTM
        """
    def info_string(self) -> str: 
        """
        Return object information as string
        """
    def print(self) -> None: 
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes: 
        """
        convert object to bytearray
        """
    @staticmethod
    def to_sensordata(sensordata_utm: SensorDataUTM) -> SensorDataLatLon: 
        """
        Convert a utm sensordatalatlon to an unprojected data

        Parameter ``data_utm``:
            $Returns:

        SensorDataLatLon
        """
    @property
    def gps_northern_hemisphere(self) -> bool:
        """
        :type: bool
        """
    @gps_northern_hemisphere.setter
    def gps_northern_hemisphere(self, arg0: bool) -> None:
        pass
    @property
    def gps_zone(self) -> int:
        """
        < UTM/UPS zone number

        :type: int
        """
    @gps_zone.setter
    def gps_zone(self, arg0: int) -> None:
        """
        < UTM/UPS zone number
        """
    __hash__ = None
    pass
