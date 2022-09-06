"""Submodule that contains nmea 0183 datastructures"""
from __future__ import annotations
import themachinethatgoesping.navigation.nmea_0183
import typing

__all__ = [
    "NMEA_Base",
    "NMEA_GGA",
    "NMEA_GLL",
    "NMEA_HDT",
    "NMEA_RMC",
    "NMEA_Unknown",
    "NMEA_VHW",
    "NMEA_VLW",
    "NMEA_VTG",
    "NMEA_ZDA"
]


class NMEA_Base():
    def __copy__(self) -> NMEA_Base: ...
    def __deepcopy__(self, arg0: dict) -> NMEA_Base: ...
    def __eq__(self, other: NMEA_Base) -> bool: ...
    def __getstate__(self) -> bytes: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, sentence: str) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None: ...
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def copy(self) -> NMEA_Base: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NMEA_Base: 
        """
        create T_CLASS object from bytearray
        """
    def get_name(self) -> str: ...
    def get_sender(self) -> str: ...
    def get_sentence(self) -> str: ...
    def get_type(self) -> str: ...
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
    __hash__ = None
    pass
class NMEA_GGA(NMEA_Base):
    """
    The NMEA GGA datagram contains time, position, and fix. Typically
    received from a global navigation satellite system (GNSS device).
    """
    def __copy__(self) -> NMEA_GGA: ...
    def __deepcopy__(self, arg0: dict) -> NMEA_GGA: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self, nmea_base: NMEA_Base, check: bool = True) -> None: 
        """
        Construct a new nmea gga object from an existing NMEA_Base datagram

        Parameter ``base``:
            Underlying NMEA_Base datagram

        Parameter ``check``:
            Check if the NMEA string is valid
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
    def copy(self) -> NMEA_GGA: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NMEA_GGA: 
        """
        create T_CLASS object from bytearray
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
    def age_of_differential_gps_data(self) -> float:
        """
        :type: float
        """
    @property
    def altitude(self) -> float:
        """
        :type: float
        """
    @property
    def coordinated_universal_time(self) -> str:
        """
        :type: str
        """
    @property
    def differential_reference_station_id(self) -> int:
        """
        :type: int
        """
    @property
    def geoidal_separation(self) -> float:
        """
        :type: float
        """
    @property
    def horizontal_dilution_of_precision(self) -> float:
        """
        :type: float
        """
    @property
    def latitude(self) -> float:
        """
        :type: float
        """
    @property
    def longitude(self) -> float:
        """
        :type: float
        """
    @property
    def number_of_satellites(self) -> int:
        """
        :type: int
        """
    @property
    def quality(self) -> int:
        """
        :type: int
        """
    @property
    def quality_explained(self) -> str:
        """
        :type: str
        """
    pass
class NMEA_GLL(NMEA_Base):
    """
    The NMEA GLL datagram contains time, position, and status. Typically
    received from a global navigation satellite system (GNSS device).
    """
    def __copy__(self) -> NMEA_GLL: ...
    def __deepcopy__(self, arg0: dict) -> NMEA_GLL: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self, nmea_base: NMEA_Base, check: bool = True) -> None: 
        """
        Construct a new nmea gll object from an existing NMEA_Base datagram

        Parameter ``base``:
            Underlying NMEA_Base datagram

        Parameter ``check``:
            Check if the NMEA string is valid
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
    def copy(self) -> NMEA_GLL: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NMEA_GLL: 
        """
        create T_CLASS object from bytearray
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
    def coordinated_universal_time(self) -> str:
        """
        :type: str
        """
    @property
    def latitude(self) -> float:
        """
        :type: float
        """
    @property
    def longitude(self) -> float:
        """
        :type: float
        """
    @property
    def mode(self) -> str:
        """
        :type: str
        """
    @property
    def mode_explained(self) -> str:
        """
        :type: str
        """
    @property
    def status(self) -> bool:
        """
        :type: bool
        """
    pass
class NMEA_HDT(NMEA_Base):
    """
    The NMEA HDT datagram contains the true vessel heading typically
    received from a compass.
    """
    def __copy__(self) -> NMEA_HDT: ...
    def __deepcopy__(self, arg0: dict) -> NMEA_HDT: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self, nmea_base: NMEA_Base, check: bool = True) -> None: 
        """
        Construct a new nmea hdt object from an existing NMEA_Base datagram

        Parameter ``base``:
            Underlying NMEA_Base datagram

        Parameter ``check``:
            Check if the NMEA string is valid
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
    def copy(self) -> NMEA_HDT: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NMEA_HDT: 
        """
        create T_CLASS object from bytearray
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
    def heading_degrees_true(self) -> float:
        """
        :type: float
        """
    pass
class NMEA_RMC(NMEA_Base):
    """
    The NMEA RMC datagram contains time, date, position, course and speed
    data. Typically received from a global navigation satellite system
    (GNSS device).
    """
    def __copy__(self) -> NMEA_RMC: ...
    def __deepcopy__(self, arg0: dict) -> NMEA_RMC: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self, nmea_base: NMEA_Base, check: bool = True) -> None: 
        """
        Construct a new nmea rmc object from an existing NMEA_Base datagram

        Parameter ``base``:
            Underlying NMEA_Base datagram

        Parameter ``check``:
            Check if the NMEA string is valid
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
    def copy(self) -> NMEA_RMC: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NMEA_RMC: 
        """
        create T_CLASS object from bytearray
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
    def to_date_string(self, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str: 
        """
        Convert the datagram into a date time string Note: this function uses
        to_timestamp()

        Parameter ``format``:
            Format string (see https://howardhinnant.github.io/date/date.html#
            to_stream_formatting)

        Returns:
            date time string
        """
    def to_timestamp(self) -> float: 
        """
        Convert the datagram into a unixtime stamp

        Returns:
            unixtime (seconds since 1970-01-01 00:00:00 UTC)
        """
    @property
    def coordinated_universal_time(self) -> str:
        """
        :type: str
        """
    @property
    def course_over_ground_degrees_true(self) -> float:
        """
        :type: float
        """
    @property
    def date(self) -> str:
        """
        :type: str
        """
    @property
    def latitude(self) -> float:
        """
        :type: float
        """
    @property
    def longitude(self) -> float:
        """
        :type: float
        """
    @property
    def magnetic_variation(self) -> float:
        """
        :type: float
        """
    @property
    def mode(self) -> str:
        """
        :type: str
        """
    @property
    def mode_explained(self) -> str:
        """
        :type: str
        """
    @property
    def speed_over_ground_knots(self) -> float:
        """
        :type: float
        """
    @property
    def status(self) -> bool:
        """
        :type: bool
        """
    pass
class NMEA_Unknown(NMEA_Base):
    """
    Thie NMEA datagram was not yet implemented in themachinethatgoesping.
    """
    def __copy__(self) -> NMEA_Unknown: ...
    def __deepcopy__(self, arg0: dict) -> NMEA_Unknown: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self, nmea_base: NMEA_Base, check: bool = True) -> None: 
        """
        Construct a new nmea Unknown object from an existing NMEA_Base
        datagram

        Parameter ``base``:
            Underlying NMEA_Base datagram

        Parameter ``check``:
            Check if the NMEA string is valid
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
    def copy(self) -> NMEA_Unknown: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NMEA_Unknown: 
        """
        create T_CLASS object from bytearray
        """
    def get_field(self, index: int) -> str: ...
    def get_field_as_double(self, index: int) -> float: ...
    def get_field_as_int(self, index: int) -> int: ...
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
    pass
class NMEA_VHW(NMEA_Base):
    """
    The NMEA VHW datagram contains the vessel's compass heading and the
    speed relative to the water.
    """
    def __copy__(self) -> NMEA_VHW: ...
    def __deepcopy__(self, arg0: dict) -> NMEA_VHW: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self, nmea_base: NMEA_Base, check: bool = True) -> None: 
        """
        Construct a new nmea vhw object from an existing NMEA_Base datagram

        Parameter ``base``:
            Underlying NMEA_Base datagram

        Parameter ``check``:
            Check if the NMEA string is valid
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
    def copy(self) -> NMEA_VHW: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NMEA_VHW: 
        """
        create T_CLASS object from bytearray
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
    def speed_over_water_kmh(self) -> float:
        """
        :type: float
        """
    @property
    def speed_over_water_knots(self) -> float:
        """
        :type: float
        """
    @property
    def vessel_heading_magnetic(self) -> float:
        """
        :type: float
        """
    @property
    def vessel_heading_true(self) -> float:
        """
        :type: float
        """
    pass
class NMEA_VLW(NMEA_Base):
    """
    The NMEA VLW datagram contains the distance of the vessel traveled by
    the vessel.
    """
    def __copy__(self) -> NMEA_VLW: ...
    def __deepcopy__(self, arg0: dict) -> NMEA_VLW: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self, nmea_base: NMEA_Base, check: bool = True) -> None: 
        """
        Construct a new nmea vlw object from an existing NMEA_Base datagram

        Parameter ``base``:
            Underlying NMEA_Base datagram

        Parameter ``check``:
            Check if the NMEA string is valid
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
    def copy(self) -> NMEA_VLW: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NMEA_VLW: 
        """
        create T_CLASS object from bytearray
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
    def total_ground_distance_nautical_miles(self) -> float:
        """
        :type: float
        """
    @property
    def total_water_distance_nautical_miles(self) -> float:
        """
        :type: float
        """
    @property
    def trip_ground_distance_nautical_miles(self) -> float:
        """
        :type: float
        """
    @property
    def trip_water_distance_nautical_miles(self) -> float:
        """
        :type: float
        """
    pass
class NMEA_VTG(NMEA_Base):
    """
    The NMEA VBW datagram contains the vessels course and speed over
    ground.
    """
    def __copy__(self) -> NMEA_VTG: ...
    def __deepcopy__(self, arg0: dict) -> NMEA_VTG: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self, nmea_base: NMEA_Base, check: bool = True) -> None: 
        """
        Construct a new nmea vtg object from an existing NMEA_Base datagram

        Parameter ``base``:
            Underlying NMEA_Base datagram

        Parameter ``check``:
            Check if the NMEA string is valid
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
    def copy(self) -> NMEA_VTG: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NMEA_VTG: 
        """
        create T_CLASS object from bytearray
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
    def course_over_ground_degrees_magnetic(self) -> float:
        """
        :type: float
        """
    @property
    def course_over_ground_degrees_true(self) -> float:
        """
        :type: float
        """
    @property
    def speed_over_ground_kmh(self) -> float:
        """
        :type: float
        """
    @property
    def speed_over_ground_knots(self) -> float:
        """
        :type: float
        """
    pass
class NMEA_ZDA(NMEA_Base):
    """
    The NMEA ZDA datagram contains the universal time code (UTC), day,
    month, year and local time zone offsets.
    """
    def __copy__(self) -> NMEA_ZDA: ...
    def __deepcopy__(self, arg0: dict) -> NMEA_ZDA: ...
    def __getstate__(self) -> bytes: ...
    def __init__(self, nmea_base: NMEA_Base, check: bool = True) -> None: 
        """
        Construct a new nmea zda object from an existing NMEA_Base datagram

        Parameter ``base``:
            Underlying NMEA_Base datagram

        Parameter ``check``:
            Check if the NMEA string is valid
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
    def copy(self) -> NMEA_ZDA: 
        """
        return a copy using the c++ default copy constructor
        """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> NMEA_ZDA: 
        """
        create T_CLASS object from bytearray
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
    def to_date_string(self, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str: 
        """
        Convert the datagram into a date time string Note: this function uses
        to_timestamp()

        Parameter ``format``:
            Format string (see https://howardhinnant.github.io/date/date.html#
            to_stream_formatting)

        Returns:
            date time string
        """
    def to_timestamp(self) -> float: 
        """
        Convert the datagram into a unixtime stamp

        Returns:
            unixtime (seconds since 1970-01-01 00:00:00 UTC)
        """
    @property
    def coordinated_universal_time(self) -> str:
        """
        :type: str
        """
    @property
    def day(self) -> int:
        """
        :type: int
        """
    @property
    def local_zone_hours(self) -> int:
        """
        :type: int
        """
    @property
    def local_zone_minutes(self) -> int:
        """
        :type: int
        """
    @property
    def month(self) -> int:
        """
        :type: int
        """
    @property
    def year(self) -> int:
        """
        :type: int
        """
    pass
