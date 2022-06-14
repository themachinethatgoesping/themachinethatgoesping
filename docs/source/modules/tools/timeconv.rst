timeconv
########

This modules provides functions to convert between a datestring format and unixtime timestamp (double).
The unixtimestamp is defined in seconds since 1970 UTC time.
The datestring object will also be UTC by default.

Example usage
=============

.. code-block:: python

    # import this module
    from time import time # default pyhon module
    from themachinethatgoesping.tools import timeconv
    
    unixtime   = time.time() # create a unixtimestamp in python
    datestring = timeconv.unixtime_to_datestring(time()) # convert to datestring
    print(datestring)

    unixtime = timeconv.datestring_to_unixtime(datestring) # convert datestring to unixtimestamp
    print(unixtime)

Format string
=============
.. list-table:: date_string format
    :widths: 1 50
    :header-rows: 1
    
    * - Format
      - Meaning
    * - %z:
      - | zone (in hhmm (as hours/minuts east of utc)
        | z may only be at the beginning of the string!
        | If no z is given the string will be interpreted as utc 0
    * - %d:
      - day as   int dd
    * - %m:
      - month as int mm
    * - %b:
      - month as string bb
    * - %Y:
      - year is  int YYYY
    * - %H:
      - hours as int HH
    * - %M:
      - Minutes as int mm
    * - %S:
      - Seconds as int SS
   

Functions (c++ module)
======================

.. code-block:: python

    # import this module
    from themachinethatgoesping.tools import timeconv
   
.. automodule:: themachinethatgoesping.tools.timeconv
   :members:

Functions (python extendet)
===========================


.. code-block:: python

    # import this extended module
    from themachinethatgoesping.tools_ext import timeconv

.. automodule:: themachinethatgoesping.tools_ext.timeconv_ext
   :members:
