"""
Submodule that contains datastructures that store navigation data or navigation sensor input
"""
from __future__ import annotations
import typing
__all__: list[str] = ['Geolocation', 'GeolocationLatLon', 'GeolocationLocal', 'GeolocationUTM', 'PositionalOffsets', 'Sensordata', 'SensordataLatLon', 'SensordataLocal', 'SensordataUTM']
class Geolocation:
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) This structure does not store any coordinates except the depth
    (z)
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> Geolocation:
        ...
    def __deepcopy__(self, arg: dict) -> Geolocation:
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
    def __init__(self, geolocation_latlon: GeolocationLatLon) -> None:
        """
        __init__(self, geolocation_local: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLocal) -> None
        __init__(self, geolocation_utm: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationUTM) -> None
        __init__(self, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None
        
        Overloaded function.
        
        1. ``__init__(self, geolocation_latlon: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLatLon) -> None``
        
        Construct a new Position object
        
        2. ``__init__(self, geolocation_local: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLocal) -> None``
        
        Construct a new Position object
        
        3. ``__init__(self, geolocation_utm: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationUTM) -> None``
        
        Construct a new Position object
        
        4. ``__init__(self, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None``
        
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
    def __setstate__(self, arg: bytes) -> None:
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
    @property
    def pitch(self) -> float:
        """
        < in °, positive means bow up
        """
    @pitch.setter
    def pitch(self, arg: float) -> None:
        """
        < in °, positive means bow up
        """
    @property
    def roll(self) -> float:
        """
        < in °, positive means port up
        """
    @roll.setter
    def roll(self, arg: float) -> None:
        """
        < in °, positive means port up
        """
    @property
    def yaw(self) -> float:
        """
        < in °, 0° is north, 90° is east
        """
    @yaw.setter
    def yaw(self, arg: float) -> None:
        """
        < in °, 0° is north, 90° is east
        """
    @property
    def z(self) -> float:
        """
        < in m, positive downwards
        """
    @z.setter
    def z(self, arg: float) -> None:
        """
        < in m, positive downwards
        """
class GeolocationLatLon(Geolocation):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) Unlike the base Geolocation object, this also stores latitude
    and longitude coordinates
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> GeolocationLatLon:
        ...
    def __deepcopy__(self, arg: dict) -> GeolocationLatLon:
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
    def __init__(self, location: Geolocation, latitude: float, longitude: float) -> None:
        """
        __init__(self, geolocationlatlon_utm: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationUTM) -> None
        __init__(self, latitude: float = 0, longitude: float = 0, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None
        
        Overloaded function.
        
        1. ``__init__(self, location: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, latitude: float, longitude: float) -> None``
        
        Construct a new Sensor Data Lat Lon object using a base sensor data
        object
        
        Parameter ``location``:
            $Parameter ``latitude``:
        
        in °, positive northwards
        
        Parameter ``longitude``:
            in °, positive eastwards
        
        2. ``__init__(self, geolocationlatlon_utm: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationUTM) -> None``
        
        Construct an GeolocationLatLon object from an existing GeolocationUTM
        object (this allows for explicit conversion from GeolocationUTM class)
        
        3. ``__init__(self, latitude: float = 0, longitude: float = 0, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None``
        
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
    def __setstate__(self, arg: bytes) -> None:
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
    @property
    def latitude(self) -> float:
        """
        < in °, positive northwards
        """
    @latitude.setter
    def latitude(self, arg: float) -> None:
        """
        < in °, positive northwards
        """
    @property
    def longitude(self) -> float:
        """
        < in °, positive eastwards
        """
    @longitude.setter
    def longitude(self, arg: float) -> None:
        """
        < in °, positive eastwards
        """
class GeolocationLocal(Geolocation):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) unlike the default Geolocation structure, this object stores
    local northing and easting coordinates. These coordinates can be
    converted to UTM coordinates if the zone and hemisphere are known.
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> GeolocationLocal:
        ...
    def __deepcopy__(self, arg: dict) -> GeolocationLocal:
        ...
    def __eq__(self, other: GeolocationLocal) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, geolocationutm: GeolocationUTM) -> None:
        """
        __init__(self, geolocation: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, northing: float, easting: float) -> None
        __init__(self, northing: float = 0, easting: float = 0, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None
        
        Overloaded function.
        
        1. ``__init__(self, geolocationutm: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationUTM) -> None``
        
        Construct a new Sensor Position object (all offsets set to 0)
        
        2. ``__init__(self, geolocation: themachinethatgoesping.navigation_nanopy.datastructures.Geolocation, northing: float, easting: float) -> None``
        
        Construct a new GeolocationLocal object
        
        Parameter ``location``:
            $Parameter ``northing``:
        
        in m, positive northwards
        
        Parameter ``easting``:
            in m, positive eastwards
        
        3. ``__init__(self, northing: float = 0, easting: float = 0, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None``
        
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
    def __setstate__(self, arg: bytes) -> None:
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
    @property
    def easting(self) -> float:
        """
        < in m, positive eastwards
        """
    @easting.setter
    def easting(self, arg: float) -> None:
        """
        < in m, positive eastwards
        """
    @property
    def northing(self) -> float:
        """
        < in m, positive northwards
        """
    @northing.setter
    def northing(self, arg: float) -> None:
        """
        < in m, positive northwards
        """
class GeolocationUTM(GeolocationLocal):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) unlike the default Geolocation structure, this object stores
    utm coordinates
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    northern_hemisphere: bool
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> GeolocationUTM:
        ...
    def __deepcopy__(self, arg: dict) -> GeolocationUTM:
        ...
    def __eq__(self, other: GeolocationUTM) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, geolocationlocal: GeolocationLocal, utm_zone: int, northern_hemisphere: bool) -> None:
        """
        __init__(self, geolocationlatlon: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLatLon, setzone: int = -1) -> None
        __init__(self, northing: float = 0, easting: float = 0, utm_zone: int = 0, northern_hemisphere: bool = True, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None
        
        Overloaded function.
        
        1. ``__init__(self, geolocationlocal: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLocal, utm_zone: int, northern_hemisphere: bool) -> None``
        
        Construct an GeolocationUTM object from an existing GeolocationLocal
        object (using a known zone and hemisphere)
        
        Parameter ``location_local``:
            $Parameter ``utm_zone``:
        
        UTM/UPS zone number
        
        Parameter ``northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere
        
        2. ``__init__(self, geolocationlatlon: themachinethatgoesping.navigation_nanopy.datastructures.GeolocationLatLon, setzone: int = -1) -> None``
        
        Construct an GeolocationUTM object from an existing GeolocationLatLon
        object (this allows for explicit conversion from GeolocationLatLon
        class)
        
        3. ``__init__(self, northing: float = 0, easting: float = 0, utm_zone: int = 0, northern_hemisphere: bool = True, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None``
        
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
    def __setstate__(self, arg: bytes) -> None:
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
    @property
    def utm_zone(self) -> int:
        """
        < UTM/UPS zone number
        """
    @utm_zone.setter
    def utm_zone(self, arg: int) -> None:
        """
        < UTM/UPS zone number
        """
class PositionalOffsets:
    """
    A structure to store positional offsets (e.g. of a sensor) relative to
    the vessel coordinate system
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_txrx: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> PositionalOffsets:
        ...
    def __deepcopy__(self, arg: dict) -> PositionalOffsets:
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
    def __setstate__(self, arg: bytes) -> None:
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
    @property
    def name(self) -> str:
        """
        < The name of the sensor
        """
    @name.setter
    def name(self, arg: str) -> None:
        """
        < The name of the sensor
        """
    @property
    def pitch(self) -> float:
        """
        < in °, positive means bow up
        """
    @pitch.setter
    def pitch(self, arg: float) -> None:
        """
        < in °, positive means bow up
        """
    @property
    def roll(self) -> float:
        """
        < in °, positive means port up
        """
    @roll.setter
    def roll(self, arg: float) -> None:
        """
        < in °, positive means port up
        """
    @property
    def x(self) -> float:
        """
        < in m, positive forward
        """
    @x.setter
    def x(self, arg: float) -> None:
        """
        < in m, positive forward
        """
    @property
    def y(self) -> float:
        """
        < in m, positive starboard
        """
    @y.setter
    def y(self, arg: float) -> None:
        """
        < in m, positive starboard
        """
    @property
    def yaw(self) -> float:
        """
        < in °, positive means clockwise rotation
        """
    @yaw.setter
    def yaw(self, arg: float) -> None:
        """
        < in °, positive means clockwise rotation
        """
    @property
    def z(self) -> float:
        """
        < in m, positive downwards
        """
    @z.setter
    def z(self, arg: float) -> None:
        """
        < in m, positive downwards
        """
class Sensordata:
    """
    A structure to store a georeferenced location and attitude data from
    different sensors (e.g. IMU, etc.) No gps coordinates are stored in
    this structure (only depth).
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> Sensordata:
        ...
    def __deepcopy__(self, arg: dict) -> Sensordata:
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
    def __init__(self, arg: SensordataLatLon) -> None:
        """
        __init__(self, arg: themachinethatgoesping.navigation_nanopy.datastructures.SensordataLocal, /) -> None
        __init__(self, arg: themachinethatgoesping.navigation_nanopy.datastructures.SensordataUTM, /) -> None
        __init__(self, depth: float = 0, heave: float = 0, heading: float = 0, pitch: float = 0, roll: float = 0) -> None
        
        Overloaded function.
        
        1. ``__init__(self, arg: themachinethatgoesping.navigation_nanopy.datastructures.SensordataLatLon, /) -> None``
        
        Construct a new Sensordata object
        
        2. ``__init__(self, arg: themachinethatgoesping.navigation_nanopy.datastructures.SensordataLocal, /) -> None``
        
        Construct a new Sensordata object
        
        3. ``__init__(self, arg: themachinethatgoesping.navigation_nanopy.datastructures.SensordataUTM, /) -> None``
        
        Construct a new Sensordata object
        
        4. ``__init__(self, depth: float = 0, heave: float = 0, heading: float = 0, pitch: float = 0, roll: float = 0) -> None``
        
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
    def __setstate__(self, arg: bytes) -> None:
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
    @property
    def depth(self) -> float:
        """
        < in m, positive downwards
        """
    @depth.setter
    def depth(self, arg: float) -> None:
        """
        < in m, positive downwards
        """
    @property
    def heading(self) -> float:
        """
        < from heading source in °, 0° is north, 90° is east
        """
    @heading.setter
    def heading(self, arg: float) -> None:
        """
        < from heading source in °, 0° is north, 90° is east
        """
    @property
    def heave(self) -> float:
        """
        < from heave source, will be added to depth in m, positive upwards
        """
    @heave.setter
    def heave(self, arg: float) -> None:
        """
        < from heave source, will be added to depth in m, positive upwards
        """
    @property
    def pitch(self) -> float:
        """
        < from attitude source, in °, positive means bow up
        """
    @pitch.setter
    def pitch(self, arg: float) -> None:
        """
        < from attitude source, in °, positive means bow up
        """
    @property
    def roll(self) -> float:
        """
        < from attitude source, in °, positive means port up
        """
    @roll.setter
    def roll(self, arg: float) -> None:
        """
        < from attitude source, in °, positive means port up
        """
class SensordataLatLon(Sensordata):
    """
    A structure to store a georeferenced location and attitude data from
    different sensors (e.g. GPS, IMU, etc.)
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    latitude: float
    longitude: float
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SensordataLatLon:
        ...
    def __deepcopy__(self, arg: dict) -> SensordataLatLon:
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
    def __init__(self, sensordata: Sensordata, latitude: float, longitude: float) -> None:
        """
        __init__(self, sensordata_utm: themachinethatgoesping.navigation_nanopy.datastructures.SensordataUTM) -> None
        __init__(self, latitude: float = 0, longitude: float = 0, depth: float = 0, heave: float = 0, heading: float = 0, pitch: float = 0, roll: float = 0) -> None
        
        Overloaded function.
        
        1. ``__init__(self, sensordata: themachinethatgoesping.navigation_nanopy.datastructures.Sensordata, latitude: float, longitude: float) -> None``
        
        Construct a new Sensor Data Lat Lon object using a base sensor data
        object
        
        Parameter ``data``:
            $Parameter ``latitude``:
        
        in °, positive northwards
        
        Parameter ``longitude``:
            in °, positive eastwards
        
        2. ``__init__(self, sensordata_utm: themachinethatgoesping.navigation_nanopy.datastructures.SensordataUTM) -> None``
        
        Construct an SensordataLatLon object from an existing SensordataUTM
        object (this allows for explicit conversion from SensordataUTM class)
        
        3. ``__init__(self, latitude: float = 0, longitude: float = 0, depth: float = 0, heave: float = 0, heading: float = 0, pitch: float = 0, roll: float = 0) -> None``
        
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
    def __setstate__(self, arg: bytes) -> None:
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
class SensordataLocal(Sensordata):
    """
    A structure to store a georeferenced data and attitude data from
    different sensors (e.g. GPS, IMU, etc.) Unlike SensordataUTM, this
    structure stores coordinates without zone and hemisphere information.
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SensordataLocal:
        ...
    def __deepcopy__(self, arg: dict) -> SensordataLocal:
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
    def __init__(self, sensordatautm: SensordataUTM) -> None:
        """
        __init__(self, sensordata: themachinethatgoesping.navigation_nanopy.datastructures.Sensordata, northing: float, easting: float) -> None
        __init__(self, northing: float = 0, easting: float = 0, depth: float = 0, heave: float = 0, heading: float = 0, pitch: float = 0, roll: float = 0) -> None
        
        Overloaded function.
        
        1. ``__init__(self, sensordatautm: themachinethatgoesping.navigation_nanopy.datastructures.SensordataUTM) -> None``
        
        Construct a new Sensor Position object (all offsets set to 0)
        
        2. ``__init__(self, sensordata: themachinethatgoesping.navigation_nanopy.datastructures.Sensordata, northing: float, easting: float) -> None``
        
        Construct a new Sensor Data Local object using a base sensor data
        object
        
        Parameter ``data``:
            $Parameter ``northing``:
        
        in m, positive northwards
        
        Parameter ``easting``:
            in m, positive eastwards
        
        3. ``__init__(self, northing: float = 0, easting: float = 0, depth: float = 0, heave: float = 0, heading: float = 0, pitch: float = 0, roll: float = 0) -> None``
        
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
    def __setstate__(self, arg: bytes) -> None:
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
    @property
    def easting(self) -> float:
        """
        < in m, positive eastwards
        """
    @easting.setter
    def easting(self, arg: float) -> None:
        """
        < in m, positive eastwards
        """
    @property
    def northing(self) -> float:
        """
        < in m, positive northwards
        """
    @northing.setter
    def northing(self, arg: float) -> None:
        """
        < in m, positive northwards
        """
class SensordataUTM(SensordataLocal):
    """
    A structure to store a georeferenced data and attitude data from
    different sensors (e.g. GPS, IMU, etc.) Unlike SensordataLatLon, this
    structure stores UTM coordinates.
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_sensordata: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    to_sensordata: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    northern_hemisphere: bool
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> SensordataUTM:
        ...
    def __deepcopy__(self, arg: dict) -> SensordataUTM:
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
    def __init__(self, sensordatalatlon: Sensordata, northing: float, easting: float, utm_zone: int, northern_hemisphere: bool) -> None:
        """
        __init__(self, sensordata_local: themachinethatgoesping.navigation_nanopy.datastructures.SensordataLocal, utm_zone: int, northern_hemisphere: bool) -> None
        __init__(self, sensordatalatlon: themachinethatgoesping.navigation_nanopy.datastructures.SensordataLatLon, setutm_zone: int = -1) -> None
        __init__(self, northing: float = 0, easting: float = 0, utm_zone: int = 0, northern_hemisphere: bool = True, depth: float = 0, heave: float = 0, heading: float = 0, pitch: float = 0, roll: float = 0) -> None
        
        Overloaded function.
        
        1. ``__init__(self, sensordatalatlon: themachinethatgoesping.navigation_nanopy.datastructures.Sensordata, northing: float, easting: float, utm_zone: int, northern_hemisphere: bool) -> None``
        
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
        
        2. ``__init__(self, sensordata_local: themachinethatgoesping.navigation_nanopy.datastructures.SensordataLocal, utm_zone: int, northern_hemisphere: bool) -> None``
        
        Construct an SensordataUTM object from an existing SensordataLocal
        object (using a known zone and hemisphere)
        
        Parameter ``data_local``:
            $Parameter ``utm_zone``:
        
        UTM/UPS zone number
        
        Parameter ``northern_hemisphere``:
            if true: northern hemisphere, else: southern hemisphere
        
        3. ``__init__(self, sensordatalatlon: themachinethatgoesping.navigation_nanopy.datastructures.SensordataLatLon, setutm_zone: int = -1) -> None``
        
        Construct an SensordataUTM object from an existing SensordataLatLon
        object (this allows for explicit conversion from SensordataLatLon
        class)
        
        4. ``__init__(self, northing: float = 0, easting: float = 0, utm_zone: int = 0, northern_hemisphere: bool = True, depth: float = 0, heave: float = 0, heading: float = 0, pitch: float = 0, roll: float = 0) -> None``
        
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
    def __setstate__(self, arg: bytes) -> None:
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
    @property
    def utm_zone(self) -> int:
        """
        < UTM/UPS zone number
        """
    @utm_zone.setter
    def utm_zone(self, arg: int) -> None:
        """
        < UTM/UPS zone number
        """
