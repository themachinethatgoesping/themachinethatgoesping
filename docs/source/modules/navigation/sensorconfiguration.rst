SensorConfiguration
###################

A simple coordinate system that allows for storing sensor and target offsets.

Supported sensors are: 

* compass: Affects :any:`SensorData.compass_heading<themachinethatgoesping.navigation.datastructures.SensorData>` with yaw offset
* position system: Affects SensorData gps variables with x,y and z offset
* depth sensor: Affects SensorData.gps_z variables with x,y and z offset
* attitude system: Affects SensorData imu variables with yaw, pitch and roll offset

The class allows for registering multiple targets (e.g. "MBES" and "SBES") with respective PositionOffsets.
Once targets are registered, the system can be used to compute the georeferenced of the targets using a SensorData object. (see usage below)

Note 1: The returned GeoLocation object type depends on the input SensorData object. 

* A :any:`datastructures.SensorDataUTM<themachinethatgoesping.navigation.datastructures.SensorDataUTM>` object will cause compute_target_position to return :any:`datastructures.GeoLocationUTM<themachinethatgoesping.navigation.datastructures.GeoLocationUTM>`
* A :any:`datastructures.SensorDataLatLon<themachinethatgoesping.navigation.datastructures.SensorDataLatLon>` will cause compute_target_position to return :any:`datastructures.GeoLocationLatLon<themachinethatgoesping.navigation.datastructures.GeoLocationLatLon>`
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
   scs.set_offsets_compass(yaw=9)
   scs.set_offsets_depth_sensor(0, 0, 1)
   scs.set_offsets_position_system(1, 2, 3)
   scs.set_offsets_attitude_sensor(10, -10, -30)

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
   sensor_data = nav.datastructures.SensorDataLatLon(
      gps_latitude = 53, 
      gps_longitude = 10, 
      gps_z = 3, 
      heave_heave = -1,
      compass_heading = 45,
      imu_yaw = 0,
      imu_roll = 2,
      imu_pitch = -3)

   # compute target position from the specified sensor data
   target_position = scs.compute_target_position("mbes", sensor_data)

   #print georeferenced target position
   print(target_position)

   # GeoLocationLatLon
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