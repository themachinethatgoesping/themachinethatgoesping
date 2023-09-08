"""
Submodule that contains datastructures that store navigation data or navigation sensor input
"""
from __future__ import annotations
import typing
__all__ = ['GeoLocation', 'GeoLocationLatLon', 'GeoLocationLocal', 'GeoLocationUTM', 'PositionalOffsets', 'SensorData', 'SensorDataLatLon', 'SensorDataLocal', 'SensorDataUTM']
class GeoLocation:
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) This structure does not store any coordinates except the depth
    (z)
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> GeoLocation:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> GeoLocation:
        ...
    def __deepcopy__(self, arg0: dict) -> GeoLocation:
        ...
    def __eq__(self, other: GeoLocation) -> bool:
        """
        Check if two GeoLocation objects are equal
        
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
    def __init__(self, z: float = ..., yaw: float = ..., pitch: float = ..., roll: float = ...) -> None:
        """
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
    def copy(self) -> GeoLocation:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
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
class GeoLocationLatLon(GeoLocation):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) Unlike the base GeoLocation object, this also stores latitude
    and longitude coordinates
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> GeoLocationLatLon:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> GeoLocationLatLon:
        ...
    def __deepcopy__(self, arg0: dict) -> GeoLocationLatLon:
        ...
    def __eq__(self, other: GeoLocationLatLon) -> bool:
        """
        Check if two GeoLocationLatLon objects are equal
        
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
    def __init__(self, location: GeoLocation, latitude: float, longitude: float) -> None:
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
        Construct an GeoLocationLatLon object from an existing GeoLocationUTM
        object (this allows for explicit conversion from GeoLocationUTM class)
        """
    @typing.overload
    def __init__(self, latitude: float = ..., longitude: float = ..., z: float = ..., yaw: float = ..., pitch: float = ..., roll: float = ...) -> None:
        """
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
    def copy(self) -> GeoLocationLatLon:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
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
class GeoLocationLocal(GeoLocation):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) unlike the default GeoLocation structure, this object stores
    local northing and easting coordinates. These coordinates can be
    converted to UTM coordinates if the zone and hemisphere are known.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> GeoLocationLocal:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> GeoLocationLocal:
        ...
    def __deepcopy__(self, arg0: dict) -> GeoLocationLocal:
        ...
    def __eq__(self, other: GeoLocationLocal) -> bool:
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
    def __init__(self, geolocation: GeoLocation, northing: float, easting: float) -> None:
        """
        Construct a new GeoLocationLocal object
        
        Parameter ``location``:
            $Parameter ``northing``:
        
        in m, positive northwards
        
        Parameter ``easting``:
            in m, positive eastwards
        """
    @typing.overload
    def __init__(self, northing: float = ..., easting: float = ..., z: float = ..., yaw: float = ..., pitch: float = ..., roll: float = ...) -> None:
        """
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
    def copy(self) -> GeoLocationLocal:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
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
class GeoLocationUTM(GeoLocationLocal):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) unlike the default GeoLocation structure, this object stores
    utm coordinates
    """
    utm_northern_hemisphere: bool
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> GeoLocationUTM:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> GeoLocationUTM:
        ...
    def __deepcopy__(self, arg0: dict) -> GeoLocationUTM:
        ...
    def __eq__(self, other: GeoLocationUTM) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    @typing.overload
    def __init__(self, geolocationlatlon: GeoLocationLocal, utm_zone: int, utm_northern_hemisphere: bool) -> None:
        """
        Construct an GeoLocationUTM object from an existing GeoLocationLocal
        object (using a known zone and hemisphere)
        
        Parameter ``location_local``:
            $Parameter ``utm_zone``:
        
        UTM/UPS zone number
        
        Parameter ``utm_northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere
        """
    @typing.overload
    def __init__(self, geolocationlatlon: GeoLocationLatLon, setzone: int = ...) -> None:
        """
        Construct an GeoLocationUTM object from an existing GeoLocationLatLon
        object (this allows for explicit conversion from GeoLocationLatLon
        class)
        """
    @typing.overload
    def __init__(self, northing: float = ..., easting: float = ..., utm_zone: int = ..., utm_northern_hemisphere: bool = ..., z: float = ..., yaw: float = ..., pitch: float = ..., roll: float = ...) -> None:
        """
        Construct a new GeoLocationUTM object
        
        Parameter ``northing``:
            in m, positive northwards
        
        Parameter ``easting``:
            in m, positive eastwards
        
        Parameter ``utm_zone``:
            UTM/UPS zone number
        
        Parameter ``utm_northern_hemisphere``:
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
    def copy(self) -> GeoLocationUTM:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
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
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> PositionalOffsets:
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
    def __init__(self, name: str = ..., x: float = ..., y: float = ..., z: float = ..., yaw: float = ..., pitch: float = ..., roll: float = ...) -> None:
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
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
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
class SensorData:
    """
    A structure to store a georeferenced location and attitude data from
    different sensors (e.g. IMU, etc.) No gps coordinates are stored in
    this structure (only depth).
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> SensorData:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SensorData:
        ...
    def __deepcopy__(self, arg0: dict) -> SensorData:
        ...
    def __eq__(self, other: SensorData) -> bool:
        """
        Check if two SensorData objects are equal
        
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
        Construct a new SensorData object
        """
    @typing.overload
    def __init__(self, arg0: ...) -> None:
        """
        Construct a new SensorData object
        """
    @typing.overload
    def __init__(self, arg0: ...) -> None:
        """
        Construct a new SensorData object
        """
    @typing.overload
    def __init__(self, depth: float = ..., heave: float = ..., heading: float = ..., pitch: float = ..., roll: float = ...) -> None:
        """
        Construct a new SensorData object
        
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
    def copy(self) -> SensorData:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
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
class SensorDataLatLon(SensorData):
    """
    A structure to store a georeferenced location and attitude data from
    different sensors (e.g. GPS, IMU, etc.)
    """
    latitude: float
    longitude: float
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> SensorDataLatLon:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SensorDataLatLon:
        ...
    def __deepcopy__(self, arg0: dict) -> SensorDataLatLon:
        ...
    def __eq__(self, other: SensorDataLatLon) -> bool:
        """
        Check if two SensorDataLatLon objects are equal
        
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
    def __init__(self, sensordata: SensorData, latitude: float, longitude: float) -> None:
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
        Construct an SensorDataLatLon object from an existing SensorDataUTM
        object (this allows for explicit conversion from SensorDataUTM class)
        """
    @typing.overload
    def __init__(self, latitude: float = ..., longitude: float = ..., depth: float = ..., heave: float = ..., heading: float = ..., pitch: float = ..., roll: float = ...) -> None:
        """
        Construct a new SensorDataLatLon object
        
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
    def copy(self) -> SensorDataLatLon:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
        """
        convert object to bytearray
        """
class SensorDataLocal(SensorData):
    """
    A structure to store a georeferenced data and attitude data from
    different sensors (e.g. GPS, IMU, etc.) Unlike SensorDataUTM, this
    structure stores coordinates without zone and hemisphere information.
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> SensorDataLocal:
        """
        create T_CLASS object from bytearray
        """
    def __copy__(self) -> SensorDataLocal:
        ...
    def __deepcopy__(self, arg0: dict) -> SensorDataLocal:
        ...
    def __eq__(self, other: SensorDataLocal) -> bool:
        """
        Check if two SensorDataLocal objects are equal
        
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
    def __init__(self, sensordata: SensorData, northing: float, easting: float) -> None:
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
    def __init__(self, northing: float = ..., easting: float = ..., depth: float = ..., heave: float = ..., heading: float = ..., pitch: float = ..., roll: float = ...) -> None:
        """
        Construct a new SensorDataLocal object
        
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
    def copy(self) -> SensorDataLocal:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
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
class SensorDataUTM(SensorDataLocal):
    """
    A structure to store a georeferenced data and attitude data from
    different sensors (e.g. GPS, IMU, etc.) Unlike SensorDataLatLon, this
    structure stores UTM coordinates.
    """
    utm_northern_hemisphere: bool
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = ...) -> SensorDataUTM:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def from_sensordata(sensordatalatlon: SensorDataLatLon, setutm_zone: int = ...) -> SensorDataUTM:
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
    @staticmethod
    def to_sensordata(sensordata_utm: SensorDataUTM) -> SensorDataLatLon:
        """
        Convert a utm sensordatalatlon to an unprojected data
        
        Parameter ``data_utm``:
            $Returns:
        
        SensorDataLatLon
        """
    def __copy__(self) -> SensorDataUTM:
        ...
    def __deepcopy__(self, arg0: dict) -> SensorDataUTM:
        ...
    def __eq__(self, other: SensorDataUTM) -> bool:
        """
        Check if two SensorDataUTM objects are equal
        
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
    def __init__(self, sensordatalatlon: SensorData, northing: float, easting: float, utm_zone: int, utm_northern_hemisphere: bool) -> None:
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
        
        Parameter ``utm_northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere
        """
    @typing.overload
    def __init__(self, sensordata_local: SensorDataLocal, utm_zone: int, utm_northern_hemisphere: bool) -> None:
        """
        Construct an SensorDataUTM object from an existing SensorDataLocal
        object (using a known zone and hemisphere)
        
        Parameter ``data_local``:
            $Parameter ``utm_zone``:
        
        UTM/UPS zone number
        
        Parameter ``utm_northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere
        """
    @typing.overload
    def __init__(self, sensordatalatlon: SensorDataLatLon, setutm_zone: int = ...) -> None:
        """
        Construct an SensorDataUTM object from an existing SensorDataLatLon
        object (this allows for explicit conversion from SensorDataLatLon
        class)
        """
    @typing.overload
    def __init__(self, northing: float = ..., easting: float = ..., utm_zone: int = ..., utm_northern_hemisphere: bool = ..., depth: float = ..., heave: float = ..., heading: float = ..., pitch: float = ..., roll: float = ...) -> None:
        """
        Construct a new SensorDataUTM object
        
        Parameter ``northing``:
            in m, positive northwards
        
        Parameter ``easting``:
            in m, positive eastwards
        
        Parameter ``utm_zone``:
            UTM/UPS zone number
        
        Parameter ``utm_northern_hemisphere``:
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
    def copy(self) -> SensorDataUTM:
        """
        return a copy using the c++ default copy constructor
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = ...) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = ...) -> None:
        """
        Print object information
        """
    def slow_hash(self) -> int:
        """
        hash function implemented using slow_hash
        """
    def to_binary(self, resize_buffer: bool = ...) -> bytes:
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
