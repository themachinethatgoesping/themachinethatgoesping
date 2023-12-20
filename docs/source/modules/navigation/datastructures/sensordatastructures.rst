Sensordata structures
#####################

Simple structures to store sensor data from IMU, compass, position system, depth sensor (e.g rtk signal) and heave sensor
SensordataLatLon which records lat/lon can be implicitly converted to and from SensordataUTM which stores utm coordinates.

Example usage
=============

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fnavigation%2Fsensordata.ipynb

.. code-block:: python

    # import this module# import this module
   from themachinethatgoesping.navigation.datastructures import SensordataLatLon, SensordataUTM

   data_utm = SensordataUTM(
      5427745.995,  # northing
      314082.699,   # easting
      60,    # utm zone
      False, # northern_hemisphere
      3,  # depth
      -2, # heave,
      45, # compass heading
      10, # yaw
      20, # pitch
      30) # roll

   print(data_utm)

   # SensordataUTM
   # *************
   # - northing:            5427746.00 [positive northwards, m]
   # - easting:             314082.70  [positive eastwards, m]
   # - utm_zone:                60         
   # - northern_hemisphere: false      
   # - depth:                   3.00       [positive downwards, m]
   # - heave:             -2.00      [positive upwards, m]
   # - heading:         45.00      [90 ° at east]
   # - pitch:               20.00      [° positive bow up]
   # - roll:                30.00      [° positive port up]

   # conversion to latlon data (works in both directions)
   data_latlot = SensordataLatLon(data_utm)

   print()
   print(data_latlot)

   # SensordataLatLon
   # ****************
   # - latitude:    41°16'49.2"S  [ddd°mm',ss.s''N/S]
   # - longitude:   41°16'49.2"W  [ddd°mm',ss.s''E/W]
   # - depth:           3.00          [positive downwards, m]
   # - heave:     -2.00         [positive upwards, m]
   # - heading: 45.00         [90 ° at east]
   # - pitch:       20.00         [° positive bow up]
   # - roll:        30.00         [° positive port up]

Data structures
===============

.. autoclass:: themachinethatgoesping.navigation.datastructures.SensordataLatLon
   :members:
   :special-members: __init__

.. autoclass:: themachinethatgoesping.navigation.datastructures.SensordataUTM
   :members:
   :special-members: __init__

.. autoclass:: themachinethatgoesping.navigation.datastructures.SensordataLocal
   :members:
   :special-members: __init__

.. autoclass:: themachinethatgoesping.navigation.datastructures.Sensordata
   :members:
   :special-members: __init__