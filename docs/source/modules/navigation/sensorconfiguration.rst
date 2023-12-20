SensorConfiguration
###################

A simple coordinate system that allows for storing sensor and target offsets.

Supported sensors are: 

* compass: Affects :any:`Sensordata.heading<themachinethatgoesping.navigation.datastructures.Sensordata>` with yaw offset
* position system: Affects Sensordata gps variables with x,y and z offset
* depth sensor: Affects Sensordata.depth variables with x,y and z offset
* attitude system: Affects Sensordata imu variables with yaw, pitch and roll offset

The class allows for registering multiple targets (e.g. "MBES" and "SBES") with respective PositionOffsets.
Once targets are registered, the system can be used to compute the georeferenced of the targets using a Sensordata object. (see usage below)

Note 1: The returned Geolocation object type depends on the input Sensordata object. 

* A :any:`datastructures.SensordataUTM<themachinethatgoesping.navigation.datastructures.SensordataUTM>` object will cause compute_target_position to return :any:`datastructures.GeolocationUTM<themachinethatgoesping.navigation.datastructures.GeolocationUTM>`
* A :any:`datastructures.SensordataLatLon<themachinethatgoesping.navigation.datastructures.SensordataLatLon>` will cause compute_target_position to return :any:`datastructures.GeolocationLatLon<themachinethatgoesping.navigation.datastructures.GeolocationLatLon>`
* ... and so on

Example usage
=============

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fnavigation%2Fsensorconfiguration.ipynb

.. code-block:: python
   
   # import this module
   import themachinethatgoesping.navigation as nav

   # initialize
   scs = nav.SensorConfiguration()

   # add sensor offsets
   scs.set_heading_source("compass",yaw=9)
   scs.set_depth_source("altimeter",0, 0, 1)
   scs.set_position_source("gps",1, 2, 3)
   scs.set_attitude_source("mru",10, -10, -30)

   # add a target with target offsets
   scs.add_target(
      target_id = "mbes",
      x = 1, 
      y = 2, 
      z = 3, 
      yaw = 0, 
      pitch = 0, 
      roll = 0)

   # create a object that contains sensor data
   sensor_data = nav.datastructures.SensordataLatLon(
      latitude = 53, 
      longitude = 10, 
      depth = 3, 
      heave = -1,
      heading = 45,
      roll = 2,
      pitch = -3)

   # compute target position from the specified sensor data
   target_position = scs.compute_target_position("mbes", sensor_data)

   #print georeferenced target position
   print(target_position)

   # GeolocationLatLon
   # *****************
   # - latitude:  53°0'0.0"N  [ddd°mm',ss.s''N/S]
   # - longitude: 53°0'0.0"E  [ddd°mm',ss.s''E/W]
   # - z:         6.51        [positive downwards, m]
   # - yaw:       36.00       [90 ° at east]
   # - pitch:     10.72       [° positive bow up]
   # - roll:      30.90       [° positive port up]

Module API
==========
   
.. autoclass:: themachinethatgoesping.navigation.SensorConfiguration
   :members:
   :special-members: __init__