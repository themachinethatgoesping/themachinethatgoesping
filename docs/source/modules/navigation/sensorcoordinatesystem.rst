SensorCoordinateSystem
######################

Simple conversion functions from lat/lon to string

Example usage
=============

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fnavigation%2Fnavtools.ipynb

.. code-block:: python
   
   # import this module
   import themachinethatgoesping.navigation as nav

   # initialize
   scs = nav.SensorCoordinateSystem()

   # add sensor offsets
   scs.set_compass_offsets(yaw=9)
   scs.set_depth_sensor_offsets(0, 0, 1)
   scs.set_position_system_offsets(1, 2, 3)
   scs.set_motion_sensor_offsets(10, -10, -30)

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
   sensor_data = nav.navdata.SensorDataLatLon(
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
   # - pitch:     10.72       [° positve bow up]
   # - roll:      30.90       [° positive port up]

Module API
==========
   
.. autoclass:: themachinethatgoesping.navigation.SensorCoordinateSystem
   :members:
   :special-members: __init__