"""
Convenient functions for converting time strings.
"""
from __future__ import annotations
import typing
__all__: list[str] = ['datestring_to_unixtime', 'datetime_to_unixtime', 'unixtime_to_datestring', 'unixtime_to_datetime', 'year_month_day_to_unixtime']
def datestring_to_unixtime(unixtime: str, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> float:
    """
    Parses a date/time string to a UNIX timestamp using the specified
    format.
    
    Parameter ``DateString``:
        Date/time string to parse
    
    Parameter ``format``:
        Format string (default: "%z__%d-%m-%Y__%H:%M:%S")
    
    Returns:
        UNIX timestamp as double (seconds since 1970-01-01T00:00:00Z)
    """
def datetime_to_unixtime(datetime: typing.Any) -> float:
    """
    Converts a Python datetime object to a Unix timestamp.
    
    Parameter ``datetimeObject``:
        The Python datetime object to convert.
    
    Returns:
        The Unix timestamp representing the given datetime.
    """
def unixtime_to_datestring(unixtime: float, fractionalSecondsDigits: int = 0, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str:
    """
    Converts a UNIX timestamp to a formatted date/time string.
    
    Parameter ``unixtime``:
        UNIX timestamp as double (seconds since 1970-01-01T00:00:00Z)
    
    Parameter ``fractionalSecondsDigits``:
        Number of digits for fractional seconds (default: 0)
    
    Parameter ``format``:
        Format string (default: "%z__%d-%m-%Y__%H:%M:%S")
    
    Returns:
        Formatted date/time string
    """
def unixtime_to_datetime(unixtime: float, timezone_offset_hours: float = 0.0) -> typing.Any:
    """
    Converts a Unix timestamp to a Python datetime object.
    
    Parameter ``timestamp``:
        The Unix timestamp to convert.
    
    Parameter ``timezone_offset_hours``:
        The timezone offset in hours (default: 0).
    
    Returns:
        The Python datetime object representing the given timestamp.
    """
def year_month_day_to_unixtime(year: int, month: int, day: int, micro_seconds: int = 0) -> float:
    """
    Converts a calendar date (year, month, day) and optional microseconds
    to a UNIX timestamp.
    
    Parameter ``year``:
        Year (e.g. 2024)
    
    Parameter ``month``:
        Month (1-12)
    
    Parameter ``day``:
        Day (1-31)
    
    Parameter ``micro_seconds``:
        Optional microseconds to add
    
    Returns:
        UNIX timestamp as double (seconds since 1970-01-01T00:00:00Z)
    """
