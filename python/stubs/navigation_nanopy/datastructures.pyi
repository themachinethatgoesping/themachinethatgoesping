"""
Submodule that contains datastructures that store navigation data or navigation sensor input
"""

from collections.abc import Sequence
from typing import overload


class PositionalOffsets:
    """
    A structure to store positional offsets (e.g. of a sensor) relative to
    the vessel coordinate system
    """

    def __init__(self, name: str = '', x: float = 0.0, y: float = 0.0, z: float = 0.0, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Construct a new PositionalOffsets object

        Args:
            name: The name of the sensor
            x: in m, positive forward
            y: in m, positive starboard
            z: in m, positive downwards
            yaw: positive means clockwise rotation
            pitch: in °, positive means bow up
            roll: in °, positive means port up
        """

    @staticmethod
    def from_txrx(tx: PositionalOffsets, rx: PositionalOffsets, name: str) -> PositionalOffsets:
        """
        Construct a new PositionalOffsets object from a transmitter and
        receiver unit

        Args:
            tx: Multibeam transmitter offsets
            rx: Multibeam receiver offsets
            name: Name of the newly constructed transceiver offsets

        Returns:
            Transceiver PositionalOffsets
        """

    def __eq__(self, other: PositionalOffsets) -> bool: ...

    @property
    def name(self) -> str:
        """The name of the sensor"""

    @name.setter
    def name(self, arg: str, /) -> None: ...

    @property
    def x(self) -> float:
        """in m, positive forward"""

    @x.setter
    def x(self, arg: float, /) -> None: ...

    @property
    def y(self) -> float:
        """in m, positive starboard"""

    @y.setter
    def y(self, arg: float, /) -> None: ...

    @property
    def z(self) -> float:
        """in m, positive downwards"""

    @z.setter
    def z(self, arg: float, /) -> None: ...

    @property
    def yaw(self) -> float:
        """in °, positive means clockwise rotation"""

    @yaw.setter
    def yaw(self, arg: float, /) -> None: ...

    @property
    def pitch(self) -> float:
        """in °, positive means bow up"""

    @pitch.setter
    def pitch(self, arg: float, /) -> None: ...

    @property
    def roll(self) -> float:
        """in °, positive means port up"""

    @roll.setter
    def roll(self, arg: float, /) -> None: ...

    def copy(self) -> PositionalOffsets:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> PositionalOffsets: ...

    def __deepcopy__(self, arg: dict, /) -> PositionalOffsets: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> PositionalOffsets:
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

class Geolocation:
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) This structure does not store any coordinates except the depth
    (z)
    """

    @overload
    def __init__(self, geolocation_latlon: GeolocationLatLon) -> None:
        """Construct a new Position object"""

    @overload
    def __init__(self, geolocation_local: GeolocationLocal) -> None:
        """Construct a new Position object"""

    @overload
    def __init__(self, geolocation_utm: GeolocationUTM) -> None:
        """Construct a new Position object"""

    @overload
    def __init__(self, z: float = 0, yaw: float = 0, pitch: float = 0, roll: float = 0) -> None:
        """
        Construct a new Geolocation object

        Args:
            z: in m, positive downwards
            yaw: in °, 0° is north, 90° is east
            pitch: in °, positive means bow up
            roll: in °, positive means port up
        """

    def __eq__(self, other: Geolocation) -> bool:
        """
        Check if two Geolocation objects are equal

        Args:
            rhs: 

        Returns:
            true if equal false if not equal
        """

    @property
    def z(self) -> float:
        """in m, positive downwards"""

    @z.setter
    def z(self, arg: float, /) -> None: ...

    @property
    def yaw(self) -> float:
        """in °, 0° is north, 90° is east"""

    @yaw.setter
    def yaw(self, arg: float, /) -> None: ...

    @property
    def pitch(self) -> float:
        """in °, positive means bow up"""

    @pitch.setter
    def pitch(self, arg: float, /) -> None: ...

    @property
    def roll(self) -> float:
        """in °, positive means port up"""

    @roll.setter
    def roll(self, arg: float, /) -> None: ...

    def copy(self) -> Geolocation:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> Geolocation: ...

    def __deepcopy__(self, arg: dict, /) -> Geolocation: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Geolocation:
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

class GeolocationLocal(Geolocation):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) unlike the default Geolocation structure, this object stores
    local northing and easting coordinates. These coordinates can be
    converted to UTM coordinates if the zone and hemisphere are known.
    """

    @overload
    def __init__(self, geolocationutm: GeolocationUTM) -> None:
        """Construct a new Sensor Position object (all offsets set to 0)"""

    @overload
    def __init__(self, geolocation: Geolocation, northing: float, easting: float) -> None:
        """
        Construct a new GeolocationLocal object

        Args:
            location: 
            northing: in m, positive northwards
            easting: in m, positive eastwards
        """

    @overload
    def __init__(self, northing: float = 0.0, easting: float = 0.0, z: float = 0.0, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Construct a new GeolocationLocal object

        Args:
            northing: in m, positive northwards
            easting: in m, positive eastwards
            z: in m, positive downwards
            yaw: in °, 0° is north, 90° is east
            pitch: in °, positive means bow up
            roll: in °, positive means port up
        """

    def __eq__(self, other: GeolocationLocal) -> bool: ...

    @property
    def northing(self) -> float:
        """in m, positive northwards"""

    @northing.setter
    def northing(self, arg: float, /) -> None: ...

    @property
    def easting(self) -> float:
        """in m, positive eastwards"""

    @easting.setter
    def easting(self, arg: float, /) -> None: ...

    def copy(self) -> GeolocationLocal:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> GeolocationLocal: ...

    def __deepcopy__(self, arg: dict, /) -> GeolocationLocal: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeolocationLocal:
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

class GeolocationLatLon(Geolocation):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) Unlike the base Geolocation object, this also stores latitude
    and longitude coordinates
    """

    @overload
    def __init__(self, location: Geolocation, latitude: float, longitude: float) -> None:
        """
        Construct a new Sensor Data Lat Lon object using a base sensor data
        object

        Args:
            location: 
            latitude: in °, positive northwards
            longitude: in °, positive eastwards
        """

    @overload
    def __init__(self, geolocationlatlon_utm: GeolocationUTM) -> None:
        """
        Construct an GeolocationLatLon object from an existing GeolocationUTM
        object (this allows for explicit conversion from GeolocationUTM class)
        """

    @overload
    def __init__(self, latitude: float = 0, longitude: float = 0, z: float = 0.0, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Construct a new GeolocationLatLon object

        Args:
            latitude: in °, positive northwards
            longitude: in °, positive eastwards
            z: in m, positive downwards
            yaw: in °, 0° is north, 90° is east
            pitch: in °, positive means bow up
            roll: in °, positive means port up
        """

    def __eq__(self, other: GeolocationLatLon) -> bool:
        """
        Check if two GeolocationLatLon objects are equal

        Args:
            rhs: 

        Returns:
            true if equal false if not equal
        """

    @property
    def latitude(self) -> float:
        """in °, positive northwards"""

    @latitude.setter
    def latitude(self, arg: float, /) -> None: ...

    @property
    def longitude(self) -> float:
        """in °, positive eastwards"""

    @longitude.setter
    def longitude(self, arg: float, /) -> None: ...

    def copy(self) -> GeolocationLatLon:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> GeolocationLatLon: ...

    def __deepcopy__(self, arg: dict, /) -> GeolocationLatLon: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeolocationLatLon:
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

class GeolocationLatLonVector:
    """
    A class to store a vector of GeolocationLatLon elements with timestamps.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, timestamps: Sequence[float], data: Sequence[GeolocationLatLon]) -> None: ...

    def __len__(self) -> int: ...

    def size(self) -> int: ...

    def empty(self) -> bool: ...

    @property
    def timestamps(self) -> list[float]:
        """Timestamps in seconds since epoch (read/write)"""

    @timestamps.setter
    def timestamps(self, arg: Sequence[float], /) -> None: ...

    @property
    def data(self) -> list[GeolocationLatLon]:
        """GeolocationLatLon data elements (read/write)"""

    @data.setter
    def data(self, arg: Sequence[GeolocationLatLon], /) -> None: ...

    def __getitem__(self, index: int) -> GeolocationLatLon: ...

    def at(self, index: int) -> GeolocationLatLon: ...

    def timestamp_at(self, index: int) -> float: ...

    def reserve(self, n: int) -> None: ...

    def clear(self) -> None: ...

    def resize(self, n: int) -> None: ...

    def get_latitudes(self) -> list[float]: ...

    def get_longitudes(self) -> list[float]: ...

    def get_z(self) -> list[float]: ...

    def get_yaw(self) -> list[float]: ...

    def get_pitch(self) -> list[float]: ...

    def get_roll(self) -> list[float]: ...

    def __eq__(self, other: "themachinethatgoesping::navigation::datastructures::DataVector_themachinethatgoesping_navigation_datastructures_GeolocationLatLon_themachinethatgoesping_navigation_datastructures_GeolocationLatLonVector") -> bool: ...

    def copy(self) -> GeolocationLatLonVector:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> GeolocationLatLonVector: ...

    def __deepcopy__(self, arg: dict, /) -> GeolocationLatLonVector: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeolocationLatLonVector:
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

class GeolocationUTM(GeolocationLocal):
    """
    A structure to store a georeferenced location and attitude (e.g. of a
    sensor) unlike the default Geolocation structure, this object stores
    utm coordinates
    """

    @overload
    def __init__(self, geolocationlocal: GeolocationLocal, utm_zone: int, northern_hemisphere: bool) -> None:
        """
        Construct an GeolocationUTM object from an existing GeolocationLocal
        object (using a known zone and hemisphere)

        Args:
            location_local: 
            utm_zone: UTM/UPS zone number
            northern_hemisphere: if true: northern hemisphere, else: southern
                                 hemisphere
        """

    @overload
    def __init__(self, geolocationlatlon: GeolocationLatLon, setzone: int = -1) -> None:
        """
        Construct an GeolocationUTM object from an existing GeolocationLatLon
        object (this allows for explicit conversion from GeolocationLatLon
        class)
        """

    @overload
    def __init__(self, northing: float = 0, easting: float = 0, utm_zone: int = 0, northern_hemisphere: bool = True, z: float = 0.0, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Construct a new GeolocationUTM object

        Args:
            northing: in m, positive northwards
            easting: in m, positive eastwards
            utm_zone: UTM/UPS zone number
            northern_hemisphere: if true: northern hemisphere, else: southern
                                 hemisphere
            z: in m, positive downwards
            yaw: in °, 0° is north, 90° is east
            pitch: in °, positive means bow up
            roll: in °, positive means port up
        """

    def __eq__(self, other: GeolocationUTM) -> bool: ...

    @property
    def utm_zone(self) -> int:
        """UTM/UPS zone number"""

    @utm_zone.setter
    def utm_zone(self, arg: int, /) -> None: ...

    @property
    def northern_hemisphere(self) -> bool: ...

    @northern_hemisphere.setter
    def northern_hemisphere(self, arg: bool, /) -> None: ...

    def copy(self) -> GeolocationUTM:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> GeolocationUTM: ...

    def __deepcopy__(self, arg: dict, /) -> GeolocationUTM: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeolocationUTM:
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

class GeolocationVector:
    """A class to store a vector of Geolocation elements with timestamps."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, timestamps: Sequence[float], data: Sequence[Geolocation]) -> None: ...

    def __len__(self) -> int: ...

    def size(self) -> int: ...

    def empty(self) -> bool: ...

    @property
    def timestamps(self) -> list[float]:
        """Timestamps in seconds since epoch (read/write)"""

    @timestamps.setter
    def timestamps(self, arg: Sequence[float], /) -> None: ...

    @property
    def data(self) -> list[Geolocation]:
        """Geolocation data elements (read/write)"""

    @data.setter
    def data(self, arg: Sequence[Geolocation], /) -> None: ...

    def __getitem__(self, index: int) -> Geolocation: ...

    def at(self, index: int) -> Geolocation: ...

    def timestamp_at(self, index: int) -> float: ...

    def reserve(self, n: int) -> None: ...

    def clear(self) -> None: ...

    def resize(self, n: int) -> None: ...

    def get_z(self) -> list[float]: ...

    def get_yaw(self) -> list[float]: ...

    def get_pitch(self) -> list[float]: ...

    def get_roll(self) -> list[float]: ...

    def __eq__(self, other: "themachinethatgoesping::navigation::datastructures::DataVector_themachinethatgoesping_navigation_datastructures_Geolocation_themachinethatgoesping_navigation_datastructures_GeolocationVector") -> bool: ...

    def copy(self) -> GeolocationVector:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> GeolocationVector: ...

    def __deepcopy__(self, arg: dict, /) -> GeolocationVector: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeolocationVector:
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

class GeolocationLocalVector:
    """
    A class to store a vector of GeolocationLocal elements with timestamps.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, timestamps: Sequence[float], data: Sequence[GeolocationLocal]) -> None: ...

    def __len__(self) -> int: ...

    def size(self) -> int: ...

    def empty(self) -> bool: ...

    @property
    def timestamps(self) -> list[float]:
        """Timestamps in seconds since epoch (read/write)"""

    @timestamps.setter
    def timestamps(self, arg: Sequence[float], /) -> None: ...

    @property
    def data(self) -> list[GeolocationLocal]:
        """GeolocationLocal data elements (read/write)"""

    @data.setter
    def data(self, arg: Sequence[GeolocationLocal], /) -> None: ...

    def __getitem__(self, index: int) -> GeolocationLocal: ...

    def at(self, index: int) -> GeolocationLocal: ...

    def timestamp_at(self, index: int) -> float: ...

    def reserve(self, n: int) -> None: ...

    def clear(self) -> None: ...

    def resize(self, n: int) -> None: ...

    def get_northings(self) -> list[float]: ...

    def get_eastings(self) -> list[float]: ...

    def get_z(self) -> list[float]: ...

    def get_yaw(self) -> list[float]: ...

    def get_pitch(self) -> list[float]: ...

    def get_roll(self) -> list[float]: ...

    def __eq__(self, other: "themachinethatgoesping::navigation::datastructures::DataVector_themachinethatgoesping_navigation_datastructures_GeolocationLocal_themachinethatgoesping_navigation_datastructures_GeolocationLocalVector") -> bool: ...

    def copy(self) -> GeolocationLocalVector:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> GeolocationLocalVector: ...

    def __deepcopy__(self, arg: dict, /) -> GeolocationLocalVector: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeolocationLocalVector:
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

class GeolocationUTMVector:
    """A class to store a vector of GeolocationUTM elements with timestamps."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, timestamps: Sequence[float], data: Sequence[GeolocationUTM]) -> None: ...

    def __len__(self) -> int: ...

    def size(self) -> int: ...

    def empty(self) -> bool: ...

    @property
    def timestamps(self) -> list[float]:
        """Timestamps in seconds since epoch (read/write)"""

    @timestamps.setter
    def timestamps(self, arg: Sequence[float], /) -> None: ...

    @property
    def data(self) -> list[GeolocationUTM]:
        """GeolocationUTM data elements (read/write)"""

    @data.setter
    def data(self, arg: Sequence[GeolocationUTM], /) -> None: ...

    def __getitem__(self, index: int) -> GeolocationUTM: ...

    def at(self, index: int) -> GeolocationUTM: ...

    def timestamp_at(self, index: int) -> float: ...

    def reserve(self, n: int) -> None: ...

    def clear(self) -> None: ...

    def resize(self, n: int) -> None: ...

    def get_northings(self) -> list[float]: ...

    def get_eastings(self) -> list[float]: ...

    def get_utm_zones(self) -> list[int]: ...

    def get_northern_hemispheres(self) -> list[bool]: ...

    def get_z(self) -> list[float]: ...

    def get_yaw(self) -> list[float]: ...

    def get_pitch(self) -> list[float]: ...

    def get_roll(self) -> list[float]: ...

    def __eq__(self, other: "themachinethatgoesping::navigation::datastructures::DataVector_themachinethatgoesping_navigation_datastructures_GeolocationUTM_themachinethatgoesping_navigation_datastructures_GeolocationUTMVector") -> bool: ...

    def copy(self) -> GeolocationUTMVector:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> GeolocationUTMVector: ...

    def __deepcopy__(self, arg: dict, /) -> GeolocationUTMVector: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> GeolocationUTMVector:
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

class Sensordata:
    """
    A structure to store a georeferenced location and attitude data from
    different sensors (e.g. IMU, etc.) No gps coordinates are stored in
    this structure (only depth).
    """

    @overload
    def __init__(self, arg: SensordataLatLon, /) -> None:
        """Construct a new Sensordata object"""

    @overload
    def __init__(self, arg: SensordataLocal, /) -> None:
        """Construct a new Sensordata object"""

    @overload
    def __init__(self, arg: SensordataUTM, /) -> None:
        """Construct a new Sensordata object"""

    @overload
    def __init__(self, depth: float = 0.0, heave: float = 0.0, heading: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Construct a new Sensordata object

        Args:
            depth: from depth source, in m, positive downwards
            heave: from heave sensor, will be added to depth in m, positive
                   upwards
            heading: from heading source, in °, 0° is north, 90° is east
            pitch: from attitude source, in °, positive means bow up
            roll: from attitude source, in °, positive means port up
        """

    def __eq__(self, other: Sensordata) -> bool:
        """
        Check if two Sensordata objects are equal

        Args:
            rhs: 

        Returns:
            true if equal false if not equal
        """

    @property
    def depth(self) -> float:
        """in m, positive downwards"""

    @depth.setter
    def depth(self, arg: float, /) -> None: ...

    @property
    def heave(self) -> float:
        """from heave source, will be added to depth in m, positive upwards"""

    @heave.setter
    def heave(self, arg: float, /) -> None: ...

    @property
    def heading(self) -> float:
        """from heading source in °, 0° is north, 90° is east"""

    @heading.setter
    def heading(self, arg: float, /) -> None: ...

    @property
    def pitch(self) -> float:
        """from attitude source, in °, positive means bow up"""

    @pitch.setter
    def pitch(self, arg: float, /) -> None: ...

    @property
    def roll(self) -> float:
        """from attitude source, in °, positive means port up"""

    @roll.setter
    def roll(self, arg: float, /) -> None: ...

    def copy(self) -> Sensordata:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> Sensordata: ...

    def __deepcopy__(self, arg: dict, /) -> Sensordata: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> Sensordata:
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

class SensordataLatLon(Sensordata):
    """
    A structure to store a georeferenced location and attitude data from
    different sensors (e.g. GPS, IMU, etc.)
    """

    @overload
    def __init__(self, sensordata: Sensordata, latitude: float, longitude: float) -> None:
        """
        Construct a new Sensor Data Lat Lon object using a base sensor data
        object

        Args:
            data: 
            latitude: in °, positive northwards
            longitude: in °, positive eastwards
        """

    @overload
    def __init__(self, sensordata_utm: SensordataUTM) -> None:
        """
        Construct an SensordataLatLon object from an existing SensordataUTM
        object (this allows for explicit conversion from SensordataUTM class)
        """

    @overload
    def __init__(self, latitude: float = 0, longitude: float = 0, depth: float = 0.0, heave: float = 0.0, heading: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Construct a new SensordataLatLon object

        Args:
            latitude: in °, positive northwards
            longitude: in °, positive eastwards
            depth: in m, positive downwards
            heave: from heave sensor, will be added to depth in m, positive
                   upwards
            heading: in °, 0° is north, 90° is east
            pitch: in °, positive means bow up
            roll: in °, positive means port up
        """

    def __eq__(self, other: SensordataLatLon) -> bool:
        """
        Check if two SensordataLatLon objects are equal

        Args:
            rhs: 

        Returns:
            true if equal false if not equal
        """

    @property
    def latitude(self) -> float: ...

    @latitude.setter
    def latitude(self, arg: float, /) -> None: ...

    @property
    def longitude(self) -> float: ...

    @longitude.setter
    def longitude(self, arg: float, /) -> None: ...

    def copy(self) -> SensordataLatLon:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SensordataLatLon: ...

    def __deepcopy__(self, arg: dict, /) -> SensordataLatLon: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensordataLatLon:
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

class SensordataLocal(Sensordata):
    """
    A structure to store a georeferenced data and attitude data from
    different sensors (e.g. GPS, IMU, etc.) Unlike SensordataUTM, this
    structure stores coordinates without zone and hemisphere information.
    """

    @overload
    def __init__(self, sensordatautm: SensordataUTM) -> None:
        """Construct a new Sensor Position object (all offsets set to 0)"""

    @overload
    def __init__(self, sensordata: Sensordata, northing: float, easting: float) -> None:
        """
        Construct a new Sensor Data Local object using a base sensor data
        object

        Args:
            data: 
            northing: in m, positive northwards
            easting: in m, positive eastwards
        """

    @overload
    def __init__(self, northing: float = 0, easting: float = 0, depth: float = 0.0, heave: float = 0.0, heading: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Construct a new SensordataLocal object

        Args:
            northing: in m, positive northwards
            easting: in m, positive eastwards
            depth: in m, positive downwards
            heave: from heave sensor, will be added to depth in m, positive
                   upwards
            heading: in °, 0° is north, 90° is east
            pitch: in °, positive means bow up
            roll: in °, positive means port up
        """

    def __eq__(self, other: SensordataLocal) -> bool:
        """
        Check if two SensordataLocal objects are equal

        Args:
            rhs: 

        Returns:
            true if equal false if not equal
        """

    @property
    def northing(self) -> float:
        """in m, positive northwards"""

    @northing.setter
    def northing(self, arg: float, /) -> None: ...

    @property
    def easting(self) -> float:
        """in m, positive eastwards"""

    @easting.setter
    def easting(self, arg: float, /) -> None: ...

    def copy(self) -> SensordataLocal:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SensordataLocal: ...

    def __deepcopy__(self, arg: dict, /) -> SensordataLocal: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensordataLocal:
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

class SensordataUTM(SensordataLocal):
    """
    A structure to store a georeferenced data and attitude data from
    different sensors (e.g. GPS, IMU, etc.) Unlike SensordataLatLon, this
    structure stores UTM coordinates.
    """

    @overload
    def __init__(self, sensordatalatlon: Sensordata, northing: float, easting: float, utm_zone: int, northern_hemisphere: bool) -> None:
        """
        Construct a new Sensor Data Local object using a base sensor data
        object

        Args:
            data: 
            northing: in m, positive northwards
            easting: in m, positive eastwards
            utm_zone: UTM/UPS zone number
            northern_hemisphere: if true: northern hemisphere, else: southern
                                 hemisphere
        """

    @overload
    def __init__(self, sensordata_local: SensordataLocal, utm_zone: int, northern_hemisphere: bool) -> None:
        """
        Construct an SensordataUTM object from an existing SensordataLocal
        object (using a known zone and hemisphere)

        Args:
            data_local: 
            utm_zone: UTM/UPS zone number
            northern_hemisphere: if true: northern hemisphere, else: southern
                                 hemisphere
        """

    @overload
    def __init__(self, sensordatalatlon: SensordataLatLon, setutm_zone: int = -1) -> None:
        """
        Construct an SensordataUTM object from an existing SensordataLatLon
        object (this allows for explicit conversion from SensordataLatLon
        class)
        """

    @overload
    def __init__(self, northing: float = 0, easting: float = 0, utm_zone: int = 0, northern_hemisphere: bool = True, depth: float = 0.0, heave: float = 0.0, heading: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> None:
        """
        Construct a new SensordataUTM object

        Args:
            northing: in m, positive northwards
            easting: in m, positive eastwards
            utm_zone: UTM/UPS zone number
            northern_hemisphere: if true: northern hemisphere, else: southern
                                 hemisphere
            depth: in m, positive downwards
            heave: is added to depth in m, positive upwards
            heading: in °, 0° is north, 90° is east
            pitch: in °, positive means bow up
            roll: in °, positive means port up
        """

    def __eq__(self, other: SensordataUTM) -> bool:
        """
        Check if two SensordataUTM objects are equal

        Args:
            rhs: 

        Returns:
            true if equal false if not equal
        """

    @property
    def utm_zone(self) -> int:
        """UTM/UPS zone number"""

    @utm_zone.setter
    def utm_zone(self, arg: int, /) -> None: ...

    @property
    def northern_hemisphere(self) -> bool: ...

    @northern_hemisphere.setter
    def northern_hemisphere(self, arg: bool, /) -> None: ...

    @staticmethod
    def to_sensordata(sensordata_utm: SensordataUTM) -> SensordataLatLon:
        """
        Convert a utm sensordatalatlon to an unprojected data

        Args:
            data_utm: 

        Returns:
            SensordataLatLon
        """

    @staticmethod
    def from_sensordata(sensordatalatlon: SensordataLatLon, setutm_zone: int = -1) -> SensordataUTM:
        """
        Construct convert a SensordataLatLon Object to UTM

        Args:
            data: valid SensordataLatLon object
            setzone: set a preferred UTM zone negative means automatic, zero
                     means UPS, positive means a particular UTM zone

        Returns:
            SensordataUTM
        """

    def copy(self) -> SensordataUTM:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SensordataUTM: ...

    def __deepcopy__(self, arg: dict, /) -> SensordataUTM: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensordataUTM:
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

class SensordataVector:
    """A class to store a vector of Sensordata elements with timestamps."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, timestamps: Sequence[float], data: Sequence[Sensordata]) -> None: ...

    def __len__(self) -> int: ...

    def size(self) -> int: ...

    def empty(self) -> bool: ...

    @property
    def timestamps(self) -> list[float]:
        """Timestamps in seconds since epoch (read/write)"""

    @timestamps.setter
    def timestamps(self, arg: Sequence[float], /) -> None: ...

    @property
    def data(self) -> list[Sensordata]:
        """Sensordata data elements (read/write)"""

    @data.setter
    def data(self, arg: Sequence[Sensordata], /) -> None: ...

    def __getitem__(self, index: int) -> Sensordata: ...

    def at(self, index: int) -> Sensordata: ...

    def timestamp_at(self, index: int) -> float: ...

    def reserve(self, n: int) -> None: ...

    def clear(self) -> None: ...

    def resize(self, n: int) -> None: ...

    def get_depths(self) -> list[float]: ...

    def get_heaves(self) -> list[float]: ...

    def get_headings(self) -> list[float]: ...

    def get_pitches(self) -> list[float]: ...

    def get_rolls(self) -> list[float]: ...

    def __eq__(self, other: "themachinethatgoesping::navigation::datastructures::DataVector_themachinethatgoesping_navigation_datastructures_Sensordata_themachinethatgoesping_navigation_datastructures_SensordataVector") -> bool: ...

    def copy(self) -> SensordataVector:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SensordataVector: ...

    def __deepcopy__(self, arg: dict, /) -> SensordataVector: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensordataVector:
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

class SensordataLatLonVector:
    """
    A class to store a vector of SensordataLatLon elements with timestamps.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, timestamps: Sequence[float], data: Sequence[SensordataLatLon]) -> None: ...

    def __len__(self) -> int: ...

    def size(self) -> int: ...

    def empty(self) -> bool: ...

    @property
    def timestamps(self) -> list[float]:
        """Timestamps in seconds since epoch (read/write)"""

    @timestamps.setter
    def timestamps(self, arg: Sequence[float], /) -> None: ...

    @property
    def data(self) -> list[SensordataLatLon]:
        """SensordataLatLon data elements (read/write)"""

    @data.setter
    def data(self, arg: Sequence[SensordataLatLon], /) -> None: ...

    def __getitem__(self, index: int) -> SensordataLatLon: ...

    def at(self, index: int) -> SensordataLatLon: ...

    def timestamp_at(self, index: int) -> float: ...

    def reserve(self, n: int) -> None: ...

    def clear(self) -> None: ...

    def resize(self, n: int) -> None: ...

    def get_latitudes(self) -> list[float]: ...

    def get_longitudes(self) -> list[float]: ...

    def get_depths(self) -> list[float]: ...

    def get_heaves(self) -> list[float]: ...

    def get_headings(self) -> list[float]: ...

    def get_pitches(self) -> list[float]: ...

    def get_rolls(self) -> list[float]: ...

    def __eq__(self, other: "themachinethatgoesping::navigation::datastructures::DataVector_themachinethatgoesping_navigation_datastructures_SensordataLatLon_themachinethatgoesping_navigation_datastructures_SensordataLatLonVector") -> bool: ...

    def copy(self) -> SensordataLatLonVector:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SensordataLatLonVector: ...

    def __deepcopy__(self, arg: dict, /) -> SensordataLatLonVector: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensordataLatLonVector:
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

class SensordataLocalVector:
    """A class to store a vector of SensordataLocal elements with timestamps."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, timestamps: Sequence[float], data: Sequence[SensordataLocal]) -> None: ...

    def __len__(self) -> int: ...

    def size(self) -> int: ...

    def empty(self) -> bool: ...

    @property
    def timestamps(self) -> list[float]:
        """Timestamps in seconds since epoch (read/write)"""

    @timestamps.setter
    def timestamps(self, arg: Sequence[float], /) -> None: ...

    @property
    def data(self) -> list[SensordataLocal]:
        """SensordataLocal data elements (read/write)"""

    @data.setter
    def data(self, arg: Sequence[SensordataLocal], /) -> None: ...

    def __getitem__(self, index: int) -> SensordataLocal: ...

    def at(self, index: int) -> SensordataLocal: ...

    def timestamp_at(self, index: int) -> float: ...

    def reserve(self, n: int) -> None: ...

    def clear(self) -> None: ...

    def resize(self, n: int) -> None: ...

    def get_northings(self) -> list[float]: ...

    def get_eastings(self) -> list[float]: ...

    def get_depths(self) -> list[float]: ...

    def get_heaves(self) -> list[float]: ...

    def get_headings(self) -> list[float]: ...

    def get_pitches(self) -> list[float]: ...

    def get_rolls(self) -> list[float]: ...

    def __eq__(self, other: "themachinethatgoesping::navigation::datastructures::DataVector_themachinethatgoesping_navigation_datastructures_SensordataLocal_themachinethatgoesping_navigation_datastructures_SensordataLocalVector") -> bool: ...

    def copy(self) -> SensordataLocalVector:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SensordataLocalVector: ...

    def __deepcopy__(self, arg: dict, /) -> SensordataLocalVector: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensordataLocalVector:
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

class SensordataUTMVector:
    """A class to store a vector of SensordataUTM elements with timestamps."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, timestamps: Sequence[float], data: Sequence[SensordataUTM]) -> None: ...

    def __len__(self) -> int: ...

    def size(self) -> int: ...

    def empty(self) -> bool: ...

    @property
    def timestamps(self) -> list[float]:
        """Timestamps in seconds since epoch (read/write)"""

    @timestamps.setter
    def timestamps(self, arg: Sequence[float], /) -> None: ...

    @property
    def data(self) -> list[SensordataUTM]:
        """SensordataUTM data elements (read/write)"""

    @data.setter
    def data(self, arg: Sequence[SensordataUTM], /) -> None: ...

    def __getitem__(self, index: int) -> SensordataUTM: ...

    def at(self, index: int) -> SensordataUTM: ...

    def timestamp_at(self, index: int) -> float: ...

    def reserve(self, n: int) -> None: ...

    def clear(self) -> None: ...

    def resize(self, n: int) -> None: ...

    def get_northings(self) -> list[float]: ...

    def get_eastings(self) -> list[float]: ...

    def get_utm_zones(self) -> list[int]: ...

    def get_northern_hemispheres(self) -> list[bool]: ...

    def get_depths(self) -> list[float]: ...

    def get_heaves(self) -> list[float]: ...

    def get_headings(self) -> list[float]: ...

    def get_pitches(self) -> list[float]: ...

    def get_rolls(self) -> list[float]: ...

    def __eq__(self, other: "themachinethatgoesping::navigation::datastructures::DataVector_themachinethatgoesping_navigation_datastructures_SensordataUTM_themachinethatgoesping_navigation_datastructures_SensordataUTMVector") -> bool: ...

    def copy(self) -> SensordataUTMVector:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SensordataUTMVector: ...

    def __deepcopy__(self, arg: dict, /) -> SensordataUTMVector: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SensordataUTMVector:
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
