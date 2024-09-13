"""
Submodule that contains datastructures that store navigation data or navigation sensor input
"""
from __future__ import annotations
import typing
__all__ = ['Geolocation', 'GeolocationLatLon', 'GeolocationLocal', 'GeolocationUTM', 'PositionalOffsets', 'Sensordata', 'SensordataLatLon', 'SensordataLocal', 'SensordataUTM']
class Geolocation:
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) This structure does not store any coordinates except the depth
    (z)
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Geolocation:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> Geolocation:
        ...
    def __deepcopy__(self, arg0: dict) -> Geolocation:
        ...
    def __eq__(self, other: Geolocation) -> bool:
        """
        Check if two Geolocation objects are equal
        
        Parameter ``rhs``:
            $Returns:
        
        true if equal
        
        Returns:
            false if not equal
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, geolocation_latlon: ...) -> None:
        """
        Construct a new Position object
        """
    @typing.overload
    def __init__(self, geolocation_local: ...) -> None:
        """
        Construct a new Position object
        """
    @typing.overload
    def __init__(self, geolocation_utm: ...) -> None:
        """
        Construct a new Position object
        """
    @typing.overload
    def __init__(self, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None:
        """
        Construct a new Geolocation object
        
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> Geolocation:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
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
        """
    @pitch.setter
    def pitch(self, arg0: float) -> None:
        ...
    @property
    def roll(self) -> float:
        """
        < in °, positive means port up
        """
    @roll.setter
    def roll(self, arg0: float) -> None:
        ...
    @property
    def yaw(self) -> float:
        """
        < in °, 0° is north, 90° is east
        """
    @yaw.setter
    def yaw(self, arg0: float) -> None:
        ...
    @property
    def z(self) -> float:
        """
        < in m, positive downwards
        """
    @z.setter
    def z(self, arg0: float) -> None:
        ...
class GeolocationLatLon(Geolocation):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) Unlike the base Geolocation object, this also stores latitude
    and longitude coordinates
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeolocationLatLon:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> GeolocationLatLon:
        ...
    def __deepcopy__(self, arg0: dict) -> GeolocationLatLon:
        ...
    def __eq__(self, other: GeolocationLatLon) -> bool:
        """
        Check if two GeolocationLatLon objects are equal
        
        Parameter ``rhs``:
            $Returns:
        
        true if equal
        
        Returns:
            false if not equal
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, location: Geolocation, latitude: float, longitude: float) -> None:
        """
        Construct a new Sensor Data Lat Lon object using a base sensor data
        object
        
        Parameter ``location``:
            $Parameter ``latitude``:
        
        in °, positive northwards
        
        Parameter ``longitude``:
            in °, positive eastwards
        """
    @typing.overload
    def __init__(self, geolocationlatlon_utm: ...) -> None:
        """
        Construct an GeolocationLatLon object from an existing GeolocationUTM
        object (this allows for explicit conversion from GeolocationUTM class)
        """
    @typing.overload
    def __init__(self, latitude: float = 0, longitude: float = 0, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None:
        """
        Construct a new GeolocationLatLon object
        
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
    def copy(self) -> GeolocationLatLon:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
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
        """
    @latitude.setter
    def latitude(self, arg0: float) -> None:
        ...
    @property
    def longitude(self) -> float:
        """
        < in °, positive eastwards
        """
    @longitude.setter
    def longitude(self, arg0: float) -> None:
        ...
class GeolocationLocal(Geolocation):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) unlike the default Geolocation structure, this object stores
    local northing and easting coordinates. These coordinates can be
    converted to UTM coordinates if the zone and hemisphere are known.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeolocationLocal:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> GeolocationLocal:
        ...
    def __deepcopy__(self, arg0: dict) -> GeolocationLocal:
        ...
    def __eq__(self, other: GeolocationLocal) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, geolocationutm: ...) -> None:
        """
        Construct a new Sensor Position object (all offsets set to 0)
        """
    @typing.overload
    def __init__(self, geolocation: Geolocation, northing: float, easting: float) -> None:
        """
        Construct a new GeolocationLocal object
        
        Parameter ``location``:
            $Parameter ``northing``:
        
        in m, positive northwards
        
        Parameter ``easting``:
            in m, positive eastwards
        """
    @typing.overload
    def __init__(self, northing: float = 0, easting: float = 0, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None:
        """
        Construct a new GeolocationLocal object
        
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
    def copy(self) -> GeolocationLocal:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
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
        """
    @easting.setter
    def easting(self, arg0: float) -> None:
        ...
    @property
    def northing(self) -> float:
        """
        < in m, positive northwards
        """
    @northing.setter
    def northing(self, arg0: float) -> None:
        ...
class GeolocationUTM(GeolocationLocal):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) unlike the default Geolocation structure, this object stores
    utm coordinates
    """
    northern_hemisphere: bool
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeolocationUTM:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> GeolocationUTM:
        ...
    def __deepcopy__(self, arg0: dict) -> GeolocationUTM:
        ...
    def __eq__(self, other: GeolocationUTM) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, geolocationlocal: GeolocationLocal, utm_zone: int, northern_hemisphere: bool) -> None:
        """
        Construct an GeolocationUTM object from an existing GeolocationLocal
        object (using a known zone and hemisphere)
        
        Parameter ``location_local``:
            $Parameter ``utm_zone``:
        
        UTM/UPS zone number
        
        Parameter ``northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere
        """
    @typing.overload
    def __init__(self, geolocationlatlon: GeolocationLatLon, setzone: int = -1) -> None:
        """
        Construct an GeolocationUTM object from an existing GeolocationLatLon
        object (this allows for explicit conversion from GeolocationLatLon
        class)
        """
    @typing.overload
    def __init__(self, northing: float = 0, easting: float = 0, utm_zone: int = 0, northern_hemisphere: bool = True, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None:
        """
        Construct a new GeolocationUTM object
        
        Parameter ``northing``:
            in m, positive northwards
        
        Parameter ``easting``:
            in m, positive eastwards
        
        Parameter ``utm_zone``:
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
    def copy(self) -> GeolocationUTM:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def utm_zone(self) -> int:
        """
        < UTM/UPS zone number
        """
    @utm_zone.setter
    def utm_zone(self, arg0: int) -> None:
        ...
class PositionalOffsets:
    """
    A structure to store positional offsets (e.g. of a sensor) relative to
    the vessel coordinate system
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> PositionalOffsets:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def from_txrx(tx: PositionalOffsets, rx: PositionalOffsets, name: str) -> PositionalOffsets:
        """
        Construct a new PositionalOffsets object from a transmitter and
        receiver unit
        
        Parameter ``tx``:
            Multibeam transmitter offsets
        
        Parameter ``rx``:
            Multibeam receiver offsets
        
        Parameter ``name``:
            Name of the newly constructed transceiver offsets
        
        Returns:
            Transceiver PositionalOffsets
        """
    def __copy__(self) -> PositionalOffsets:
        ...
    def __deepcopy__(self, arg0: dict) -> PositionalOffsets:
        ...
    def __eq__(self, other: PositionalOffsets) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, name: str = '', x: float = 0, y: float = 0, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None:
        """
        Construct a new PositionalOffsets object
        
        Parameter ``name``:
            The name of the sensor
        
        Parameter ``x``:
            in m, positive forward
        
        Parameter ``y``:
            in m, positive starboard
        
        Parameter ``z``:
            in m, positive downwards
        
        Parameter ``yaw``:
            positive means clockwise rotation
        
        Parameter ``pitch``:
            in °, positive means bow up
        
        Parameter ``roll``:
            in °, positive means port up
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
    def copy(self) -> PositionalOffsets:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def name(self) -> str:
        """
        < The name of the sensor
        """
    @name.setter
    def name(self, arg0: str) -> None:
        ...
    @property
    def pitch(self) -> float:
        """
        < in °, positive means bow up
        """
    @pitch.setter
    def pitch(self, arg0: float) -> None:
        ...
    @property
    def roll(self) -> float:
        """
        < in °, positive means port up
        """
    @roll.setter
    def roll(self, arg0: float) -> None:
        ...
    @property
    def x(self) -> float:
        """
        < in m, positive forward
        """
    @x.setter
    def x(self, arg0: float) -> None:
        ...
    @property
    def y(self) -> float:
        """
        < in m, positive starboard
        """
    @y.setter
    def y(self, arg0: float) -> None:
        ...
    @property
    def yaw(self) -> float:
        """
        < in °, positive means clockwise rotation
        """
    @yaw.setter
    def yaw(self, arg0: float) -> None:
        ...
    @property
    def z(self) -> float:
        """
        < in m, positive downwards
        """
    @z.setter
    def z(self, arg0: float) -> None:
        ...
class Sensordata:
    """
    A structure to store a georeferenced location and attitude data from
    different sensors (e.g. IMU, etc.) No gps coordinates are stored in
    this structure (only depth).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Sensordata:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> Sensordata:
        ...
    def __deepcopy__(self, arg0: dict) -> Sensordata:
        ...
    def __eq__(self, other: Sensordata) -> bool:
        """
        Check if two Sensordata objects are equal
        
        Parameter ``rhs``:
            $Returns:
        
        true if equal
        
        Returns:
            false if not equal
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, arg0: ...) -> None:
        """
        Construct a new Sensordata object
        """
    @typing.overload
    def __init__(self, arg0: ...) -> None:
        """
        Construct a new Sensordata object
        """
    @typing.overload
    def __init__(self, arg0: ...) -> None:
        """
        Construct a new Sensordata object
        """
    @typing.overload
    def __init__(self, depth: float = 0, heave: float = 0, heading: float = 0, pitch: float = 0, roll: float = 0) -> None:
        """
        Construct a new Sensordata object
        
        Parameter ``depth``:
            from depth source, in m, positive downwards
        
        Parameter ``heave``:
            from heave sensor, will be added to depth in m, positive upwards
        
        Parameter ``heading``:
            from heading source, in °, 0° is north, 90° is east
        
        Parameter ``pitch``:
            from attitude source, in °, positive means bow up
        
        Parameter ``roll``:
            from attitude source, in °, positive means port up
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
    def copy(self) -> Sensordata:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def depth(self) -> float:
        """
        < in m, positive downwards
        """
    @depth.setter
    def depth(self, arg0: float) -> None:
        ...
    @property
    def heading(self) -> float:
        """
        < from heading source in °, 0° is north, 90° is east
        """
    @heading.setter
    def heading(self, arg0: float) -> None:
        ...
    @property
    def heave(self) -> float:
        """
        < from heave source, will be added to depth in m, positive upwards
        """
    @heave.setter
    def heave(self, arg0: float) -> None:
        ...
    @property
    def pitch(self) -> float:
        """
        < from attitude source, in °, positive means bow up
        """
    @pitch.setter
    def pitch(self, arg0: float) -> None:
        ...
    @property
    def roll(self) -> float:
        """
        < from attitude source, in °, positive means port up
        """
    @roll.setter
    def roll(self, arg0: float) -> None:
        ...
class SensordataLatLon(Sensordata):
    """
    A structure to store a georeferenced location and attitude data from
    different sensors (e.g. GPS, IMU, etc.)
    """
    latitude: float
    longitude: float
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensordataLatLon:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SensordataLatLon:
        ...
    def __deepcopy__(self, arg0: dict) -> SensordataLatLon:
        ...
    def __eq__(self, other: SensordataLatLon) -> bool:
        """
        Check if two SensordataLatLon objects are equal
        
        Parameter ``rhs``:
            $Returns:
        
        true if equal
        
        Returns:
            false if not equal
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, sensordata: Sensordata, latitude: float, longitude: float) -> None:
        """
        Construct a new Sensor Data Lat Lon object using a base sensor data
        object
        
        Parameter ``data``:
            $Parameter ``latitude``:
        
        in °, positive northwards
        
        Parameter ``longitude``:
            in °, positive eastwards
        """
    @typing.overload
    def __init__(self, sensordata_utm: ...) -> None:
        """
        Construct an SensordataLatLon object from an existing SensordataUTM
        object (this allows for explicit conversion from SensordataUTM class)
        """
    @typing.overload
    def __init__(self, latitude: float = 0, longitude: float = 0, depth: float = 0, heave: float = 0, heading: float = 0, pitch: float = 0, roll: float = 0) -> None:
        """
        Construct a new SensordataLatLon object
        
        Parameter ``latitude``:
            in °, positive northwards
        
        Parameter ``longitude``:
            in °, positive eastwards
        
        Parameter ``depth``:
            in m, positive downwards
        
        Parameter ``heave``:
            from heave sensor, will be added to depth in m, positive upwards
        
        Parameter ``heading``:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SensordataLatLon:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class SensordataLocal(Sensordata):
    """
    A structure to store a georeferenced data and attitude data from
    different sensors (e.g. GPS, IMU, etc.) Unlike SensordataUTM, this
    structure stores coordinates without zone and hemisphere information.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensordataLocal:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SensordataLocal:
        ...
    def __deepcopy__(self, arg0: dict) -> SensordataLocal:
        ...
    def __eq__(self, other: SensordataLocal) -> bool:
        """
        Check if two SensordataLocal objects are equal
        
        Parameter ``rhs``:
            $Returns:
        
        true if equal
        
        Returns:
            false if not equal
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, sensordatautm: ...) -> None:
        """
        Construct a new Sensor Position object (all offsets set to 0)
        """
    @typing.overload
    def __init__(self, sensordata: Sensordata, northing: float, easting: float) -> None:
        """
        Construct a new Sensor Data Local object using a base sensor data
        object
        
        Parameter ``data``:
            $Parameter ``northing``:
        
        in m, positive northwards
        
        Parameter ``easting``:
            in m, positive eastwards
        """
    @typing.overload
    def __init__(self, northing: float = 0, easting: float = 0, depth: float = 0, heave: float = 0, heading: float = 0, pitch: float = 0, roll: float = 0) -> None:
        """
        Construct a new SensordataLocal object
        
        Parameter ``northing``:
            in m, positive northwards
        
        Parameter ``easting``:
            in m, positive eastwards
        
        Parameter ``depth``:
            in m, positive downwards
        
        Parameter ``heave``:
            from heave sensor, will be added to depth in m, positive upwards
        
        Parameter ``heading``:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SensordataLocal:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
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
        """
    @easting.setter
    def easting(self, arg0: float) -> None:
        ...
    @property
    def northing(self) -> float:
        """
        < in m, positive northwards
        """
    @northing.setter
    def northing(self, arg0: float) -> None:
        ...
class SensordataUTM(SensordataLocal):
    """
    A structure to store a georeferenced data and attitude data from
    different sensors (e.g. GPS, IMU, etc.) Unlike SensordataLatLon, this
    structure stores UTM coordinates.
    """
    northern_hemisphere: bool
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensordataUTM:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def from_sensordata(sensordatalatlon: SensordataLatLon, setutm_zone: int = -1) -> SensordataUTM:
        """
        Construct convert a SensordataLatLon Object to UTM
        
        Parameter ``data``:
            valid SensordataLatLon object
        
        Parameter ``setzone``:
            set a preferred UTM zone negative means automatic, zero means UPS,
            positive means a particular UTM zone
        
        Returns:
            SensordataUTM
        """
    @staticmethod
    def to_sensordata(sensordata_utm: SensordataUTM) -> SensordataLatLon:
        """
        Convert a utm sensordatalatlon to an unprojected data
        
        Parameter ``data_utm``:
            $Returns:
        
        SensordataLatLon
        """
    def __copy__(self) -> SensordataUTM:
        ...
    def __deepcopy__(self, arg0: dict) -> SensordataUTM:
        ...
    def __eq__(self, other: SensordataUTM) -> bool:
        """
        Check if two SensordataUTM objects are equal
        
        Parameter ``rhs``:
            $Returns:
        
        true if equal
        
        Returns:
            false if not equal
        """
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, sensordatalatlon: Sensordata, northing: float, easting: float, utm_zone: int, northern_hemisphere: bool) -> None:
        """
        Construct a new Sensor Data Local object using a base sensor data
        object
        
        Parameter ``data``:
            $Parameter ``northing``:
        
        in m, positive northwards
        
        Parameter ``easting``:
            in m, positive eastwards
        
        Parameter ``utm_zone``:
            UTM/UPS zone number
        
        Parameter ``northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere
        """
    @typing.overload
    def __init__(self, sensordata_local: SensordataLocal, utm_zone: int, northern_hemisphere: bool) -> None:
        """
        Construct an SensordataUTM object from an existing SensordataLocal
        object (using a known zone and hemisphere)
        
        Parameter ``data_local``:
            $Parameter ``utm_zone``:
        
        UTM/UPS zone number
        
        Parameter ``northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere
        """
    @typing.overload
    def __init__(self, sensordatalatlon: SensordataLatLon, setutm_zone: int = -1) -> None:
        """
        Construct an SensordataUTM object from an existing SensordataLatLon
        object (this allows for explicit conversion from SensordataLatLon
        class)
        """
    @typing.overload
    def __init__(self, northing: float = 0, easting: float = 0, utm_zone: int = 0, northern_hemisphere: bool = True, depth: float = 0, heave: float = 0, heading: float = 0, pitch: float = 0, roll: float = 0) -> None:
        """
        Construct a new SensordataUTM object
        
        Parameter ``northing``:
            in m, positive northwards
        
        Parameter ``easting``:
            in m, positive eastwards
        
        Parameter ``utm_zone``:
            UTM/UPS zone number
        
        Parameter ``northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere
        
        Parameter ``depth``:
            in m, positive downwards
        
        Parameter ``heave``:
            is added to depth in m, positive upwards
        
        Parameter ``heading``:
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
    def __setstate__(self, arg0: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> SensordataUTM:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 2) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
    @property
    def utm_zone(self) -> int:
        """
        < UTM/UPS zone number
        """
    @utm_zone.setter
    def utm_zone(self, arg0: int) -> None:
        ...
