

def datestring_to_unixtime(datestring: str, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> float:
    """
    Parses a date/time string to a UNIX timestamp using the specified
    format.
    Args:
        DateString: Date/time string to parse
        format: Format string (default: "%z__%d-%m-%Y__%H:%M:%S")

    Returns:
        UNIX timestamp as double (seconds since 1970-01-01T00:00:00Z)
    """

def year_month_day_to_unixtime(year: int, month: int, day: int, micro_seconds: int = 0) -> float:
    """
    Converts a calendar date (year, month, day) and optional microseconds
    to a UNIX timestamp.
    Args:
        year: Year (e.g. 2024)
        month: Month (1-12)
        day: Day (1-31)
        micro_seconds: Optional microseconds to add

    Returns:
        UNIX timestamp as double (seconds since 1970-01-01T00:00:00Z)
    """

def unixtime_to_datestring(unixtime: float, fractionalSecondsDigits: int = 0, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str:
    """
    Converts a UNIX timestamp to a formatted date/time string.
    Args:
        unixtime: UNIX timestamp as double (seconds since
                  1970-01-01T00:00:00Z)
        fractionalSecondsDigits: Number of digits for fractional seconds
                                 (default: 0)
        format: Format string (default: "%z__%d-%m-%Y__%H:%M:%S")

    Returns:
        Formatted date/time string
    """

def unixtime_to_datetime(unixtime: float, timezone_offset_hours: float = 0.0) -> object:
    """
    Converts a Unix timestamp to a Python datetime object.

    Args:
        timestamp: The Unix timestamp to convert.
        timezone_offset_hours: The timezone offset in hours (default: 0).

    Returns:
        The Python datetime object representing the given timestamp.
    """

def datetime_to_unixtime(datetime: object) -> float:
    """
    Converts a Python datetime object to a Unix timestamp.

    Args:
        datetimeObject: The Python datetime object to convert.

    Returns:
        The Unix timestamp representing the given datetime.
    """

def datestring_to_datetime(unixtime: str, format: str = '%z__%d-%m-%Y__%H:%M:%S', timezone_offset_hours: float = 0.0) -> object:
    """
    Converts a date string to a Python datetime object using the specified
    format.
    """

def datetime_to_datestring(datetime: object, fractionalSecondsDigits: int = 0, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str:
    """
    Converts a Python datetime object to a formatted date string.

    Args:
        datetimeObject: The Python datetime object to convert.
        fractionalSecondsDigits: Number of fractional seconds digits to
                                 include.
        format: The format string to use for conversion.

    Returns:
        The formatted date string.
    """
