navtools
########

Simple conversion functions from lat/lon to string

Example usage
=============

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fnavigation%2Fnavtools.ipynb

.. code-block:: python
   
   # import this module
   from themachinethatgoesping.navigation import navtools as nt
    
   print("[degrees] 123.45678° ->",nt.latitude_to_string(123.45678,"degrees",2))
   print("[minutes] 123.45678° ->",nt.latitude_to_string(123.45678,"minutes",2))
   print("[seconds] 123.45678° ->",nt.latitude_to_string(123.45678,"seconds",2))
   print()
   print("[degrees] -123.45678° ->",nt.latitude_to_string(-123.45678,"degrees",2))
   print("[minutes] -123.45678° ->",nt.latitude_to_string(-123.45678,"minutes",2))
   print("[seconds] -123.45678° ->",nt.latitude_to_string(-123.45678,"seconds",2))
   print()
   print("[degrees] -123.45678° ->",nt.longitude_to_string( 123.45678,"degrees",2))
   print("[minutes] -123.45678° ->",nt.longitude_to_string( 123.45678,"minutes",2))
   print("[seconds] -123.45678° ->",nt.longitude_to_string(-123.45678,"seconds",3))

   # [degrees] 123.45678° -> 123.46°N
   # [minutes] 123.45678° -> 123°27.41'N
   # [seconds] 123.45678° -> 123°27'24.41"N

   # [degrees] -123.45678° -> 123.46°E
   # [minutes] -123.45678° -> 123°27.41'S
   # [seconds] -123.45678° -> 123°27'24.41"S

   # [degrees] 123.45678° -> 123.46°E
   # [minutes] 123.45678° -> 123°27.41'E
   # [seconds] -123.45678° -> 123°27'24.408"W

Module API
==========
   
.. automodule:: themachinethatgoesping.navigation.navtools
   :members:
