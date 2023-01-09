"""Convenient functions for converting time strings."""
from __future__ import annotations
import themachinethatgoesping.tools.timeconv
import typing

__all__ = [
    "datestring_to_unixtime",
    "unixtime_to_datestring",
    "year_month_day_to_unixtime"
]


def datestring_to_unixtime(unixtime: str, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> float:
    """
    Converting between date strings and unixtime stamps (ref 1970)

    Parameter ``DateString:``:
        DateString to be converted. Must fit format string.

    Parameter ``format:``:
        Format string to convert Date string. Default Format:
        "%z__%d-%m-%Y__%H:%M:%S" see
        https://m.cplusplus.com/reference/ctime/strftime/ * https://themac
        hinethatgoesping.readthedocs.io/en/latest/modules/tools/timeconv.h
        tml#format-string

    Returns:
        unixtime as double (seconds since 01.01.1970)
    """
def unixtime_to_datestring(unixtime: float, fractionalSecondsDigits: int = 0, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str:
    """
    Converting between date strings and unixtime stamps (ref 1970)

    Parameter ``unixtime:``:
        seconds since 01.01.1970 as double

    Parameter ``fractionalSecondsDigits:``:
        How many digits to use for the split seconds. Minimum is 0 (second
        resolution) Maximum is 6 (microsecond resolution)

    Parameter ``format:``:
        Format string to convert Date string. Default Format:
        "%z__%d-%m-%Y__%H:%M:%S" see:
        https://m.cplusplus.com/reference/ctime/strftime/ * https://themac
        hinethatgoesping.readthedocs.io/en/latest/modules/tools/timeconv.h
        tml#format-string

    Returns:
        DateString that fits to the specified format
    """
def year_month_day_to_unixtime(year: int, month: int, day: int, micro_seconds: int = 0) -> float:
    """
    Convert a year, month and day to a unixtime stamp (ref 1970)

    Parameter ``year``:
        $Parameter ``month``:

    Parameter ``day``:
        $Parameter ``micro_seconds``:

    microseconds since midnight

    Returns:
        double
    """
