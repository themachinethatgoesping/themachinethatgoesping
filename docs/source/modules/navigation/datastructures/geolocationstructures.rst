Geolocation structures
######################

Simple structures to store georeferenced locations and attitudes. 
Geolocation which records lat/lon can be implicitly converted to and from GeolocationUTM which stores utm coordinates.

Example usage
=============

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fnavigation%2Fgeolocation.ipynb

.. code-block:: python

    # import this module# import this module
   from themachinethatgoesping.navigation.datastructures import GeolocationLatLon, GeolocationUTM
    
   location = GeolocationUTM(
      5427745.995,  # northing
      314082.699, # easting
      60, #utm zone
      False, #northern_hemisphere
      3, #depth
      10, #yaw
      20, #pitch
      30) #roll

      print(location)

      # GeolocationUTM
      # **************
      # - northing:            5427746.00 [positive northwards, m]
      # - easting:             314082.70  [positive eastwards, m]
      # - zone:                60         
      # - northern_hemisphere: false      
      # - z:                   3.00       [positive downwards, m]
      # - yaw:                 10.00      [90 ° at east]
      # - pitch:               20.00      [° positive bow up]
      # - roll:                30.00      [° positive port up]

      # conversion to latlon location (works in both directions)
      location_latlon = Geolocation(location)

      print(location_latlon)

      # Geolocation
      # ***********
      #   latitude:  41°16'49.2"S  [ddd°mm',ss.s''N/S]
      # - longitude: 41°16'49.2"W  [ddd°mm',ss.s''E/W]
      # - z:         3.00   [positive downwards, m]
      # - yaw:       10.00  [90 ° at east]
      # - pitch:     20.00  [° positive bow up]
      # - roll:      30.00  [° positive port up]

Data structures
===============

.. autoclass:: themachinethatgoesping.navigation.datastructures.GeolocationLatLon
   :members:
   :special-members: __init__

.. autoclass:: themachinethatgoesping.navigation.datastructures.GeolocationUTM
   :members:
   :special-members: __init__

.. autoclass:: themachinethatgoesping.navigation.datastructures.GeolocationLocal
   :members:
   :special-members: __init__

.. autoclass:: themachinethatgoesping.navigation.datastructures.Geolocation
   :members:
   :special-members: __init__