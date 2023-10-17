"""

This module extends the tools.timeconv with some functions implemented in pure python

"""
from __future__ import annotations
from datetime import datetime
from themachinethatgoesping.tools_cppy.timeconv import datestring_to_unixtime
from themachinethatgoesping.tools_cppy.timeconv import unixtime_to_datestring
from themachinethatgoesping.tools_cppy.timeconv import year_month_day_to_unixtime
__all__ = ['datestring_to_datetime', 'datestring_to_unixtime', 'datetime', 'datetime_to_datestring', 'unixtime_to_datestring', 'year_month_day_to_unixtime']
def datestring_to_datetime(datestring: str, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> datetime:
    """
    Converting date strings to python datetime objects
    
        Parameters
        ----------
        datestring : str
            DateString to be converted. Must fit format string.
        format : _type_, optional
            %z__%d-%m-%Y__%H:%M:%S" see: https://m.cplusplus.com/reference/ctime/strftime/,
            https://themachinethatgoesping.readthedocs.io/en/latest/modules/tools/timeconv.html#format-string
            by default '%z__%d-%m-%Y__%H:%M:%S'
    
        Returns
        -------
        datetime
            python datetime object
        
    """
def datetime_to_datestring(dt: datetime, fractionalSecondsDigits: int = 0, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str:
    """
    Converting python datetime objects to datestrings
    
        Parameters
        ----------
        dt : datetime
            datetime to be converted
        fractionalSecondsDigits : int, optional
            How many digits to use for the split seconds.
            Minimum is 0 (second resolution)
            Maximum is 6 (microsecond resolution), by default 0
        format : _type_, optional
            %z__%d-%m-%Y__%H:%M:%S" see: https://m.cplusplus.com/reference/ctime/strftime/,
            https://themachinethatgoesping.readthedocs.io/en/latest/modules/tools/timeconv.html#format-string
            by default '%z__%d-%m-%Y__%H:%M:%S'
    
        Returns
        -------
        str
            DateString that fits to the specified format
        
    """
