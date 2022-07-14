GeoLocation
###########

Simple structures to store georeferenced sensor locations and attitudes. 
GeoLocation which records lat/lon can be implicitely converted to and from GeoLocationUTM which stores utm coordinates.

Example usage
=============

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fnavigation%2Fgeolocation.ipynb

.. code-block:: python

    # import this module# import this module
   from themachinethatgoesping.navigation import GeoLocation, GeoLocationUTM
    
   location = GeoLocationUTM(
      5427745.995,  # northing
      314082.699, # easting
      60, #utm zone
      False, #northern_hemisphere
      3, #depth
      10, #yaw
      20, #pitch
      30) #roll

      print(location)

      # GeoLocationUTM
      # **************
      # - northing:            5427746.00 [positive northwards, m]
      # - easting:             314082.70  [positive eastwards, m]
      # - zone:                60         
      # - northern_hemisphere: false      
      # - z:                   3.00       [positive downwards, m]
      # - yaw:                 10.00      [90 ° at east]
      # - pitch:               20.00      [° positve bow up]
      # - roll:                30.00      [° positive port up]

      # conversion to latlon location (works in both directions)
      location_latlon = GeoLocation(location)

      print(location_latlon)

      # GeoLocation
      # ***********
      #   latitude:  41°16'49.2"S  [ddd°mm',ss.s''N/S]
      # - longitude: 41°16'49.2"W  [ddd°mm',ss.s''E/W]
      # - z:         3.00   [positive downwards, m]
      # - yaw:       10.00  [90 ° at east]
      # - pitch:     20.00  [° positve bow up]
      # - roll:      30.00  [° positive port up]

Classes
=======
   
.. autoclass:: themachinethatgoesping.navigation.GeoLocation
   :members:

   .. automethod:: __init__


.. autoclass:: themachinethatgoesping.navigation.GeoLocationUTM
   :members:

   .. automethod:: __init__