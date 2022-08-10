Navigation Data Processing
##########################

Introduction
============

Georeferencing echosounder samples (e.g. using raytracing routines) requires the precise knowledge of the position and attitude of the acoustic array at the time of transmission.
To get these data, surveyors often use a variety of different digital sensors. For example a compass to get the vessels heading, a GPS to get the vessel position and an IMU to get the vessels attitude.

These sensors typically record the data asynchronous, i.e. at different times than the echo sounder pings. Additionally, the the data is only valid for a specific position on the sensor. Typically the position of the sensor and not the position of the echo sounder.
To gain the position and attitude of the sensor, the data must thus be rotated and interpolated to the time of the echo sounder pings.

Many sonar manufactures include this transformation into the software and the sonar data format. 
For other formats, or if the data must be corrected (e.g. to correct offsets or use smoothed navigation) this must be done manually.

Themachinethatgoesping provides two powerful classes to archive the interpolation and rotation of the data for common cases. It supports the following sensors:

- Position source: provides latitude and longitudes in ° or northing and easting in m
- Attitude source: provides roll, pitch in °
- Heading source: provides heading in °
- Heave source: provides measurements for the ship's heave (will be added to depth)
- Depth source: provides measurements for the ship's depth (e.g. GPS RTK signal)

For the interpolation we use the vector interpolation classes from themachinethatgoesping.tools.vectorinterpolators.

- Positions, depth and heave data is interpolated using a modified akima spline (boost::makima)
- yaw, pitch, roll and heading are as quaternions using eigen::slerp interpolation

1) Set up the sensor offsets
============================

Prior to transforming and interpolating, the user must create a SensorConfiguration object that stores the offsets of all used sensors. 

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fusage%2Fnavigation_data_processing.ipynb

.. code-block:: python
   
   # import the navigation module
   import themachinethatgoesping.navigation as nav

   # initialize
   scs = nav.SensorConfiguration()

   # add sensor offsets
   scs.set_offsets_heading_source(9)               # yaw
   scs.set_offsets_depth_source(0, 0, 1)           # x, y, z
   scs.set_offsets_position_source(1, 2, 3)        # x, y, z
   scs.set_offsets_attitude_source(10, -10, -30)   # yaw, pitch, roll

   # add a target sensor with offsets
   scs.add_target(
      target_id = "mbes",
      x = 1,     # in m, positive forward
      y = 2,     # in m, positive starboard
      z = 3,     # in m, positive down
      yaw   = 0, # in degrees, positive clockwise
      pitch = 0, # in degrees, positive bow up
      roll  = 0) # in degrees, positive port up

   # Note: The offsets are relative to the origin of the vessels coordinate system.

2) Set navigation data
======================

First a NavigationInterpolator object must be initialized.

The user has two options:

    NavigationInterpolatorLocal stores northing and easting (in meter)
    NavigationInterpolatorLatLon stores and interpolates latitudes and longitudes (in °)

In this example we use latitude and longitude.

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fusage%2Fnavigation_data_processing.ipynb

.. code-block:: python
   
   # initialize the NavigationInterpolator using the previously created SensorConfiguration
   navi = nav.NavigationInterpolatorLatLon(scs)

   # add data
   navi.set_data_position(timestamps_possys, latitude, longitude)
   navi.set_data_attitude(timestamps_attitude, pitch, roll)
   navi.set_data_heading(timestamps_attitude, yaw)

Note: data that are not set are assumed to be 0.0 (e.g depth in the above example)

3) Get echo sounder position for random ping time points
========================================================

The user can now retrieve the position and attitude of the registered target sensors (add_target) as GeoLocation object. 

The returned type of GeoLocation (GeoLocationLocal or GeoLocationLatLon) is determined by the type of the navigation interpolator (NavigationInterpolatorLocal or NavigationInterpolatorLatLon)

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fusage%2Fnavigation_data_processing.ipynb

.. code-block:: python
   
   # get the location of the "mbes" at timestamp 25 (seconds since 1970)
   location_mbes = navi.compute_target_position("mbes",timestamp=25)

   print(location_mbes)

.. code-block:: python
   
   # output:
   # GeoLocationLatLon
   # #################
   # - latitude:  54°9'0.0"N   [ddd°mm',ss.s''N/S]
   # - longitude: 10°8'60.0"E  [ddd°mm',ss.s''E/W]
   # - z:         2.37         [positive downwards, m]
   # - yaw:       4.88         [90 ° at east]
   # - pitch:     15.01        [° positive bow up]
   # - roll:      29.51        [° positive port up]

Note: the compute_target_position time stamps can exceed the time stamps of data inside the NavigationInterpolator. 
The behavior is then determined by the extrapolation mode parameter (navi.set_extrapolation_mode()).
This parameter can be:

1. "extrapolate" (default): The data is extrapolated (linear continuation of the used akima spline)
2. "nearest": The last (or respective first) data point is used
3. "fail": An exception is thrown if the time stamp is outside the data range

4) UTM/LatLon conversion
========================

The NavigationInterpolatorLatLon object computes GeoLocationLatLon objects.
This stores latitude and longitude values in °.

The NavigationInterpolatorLocal object computes GeoLocationLocal objects.
This stores northing and easting values in m (without zone or hemisphere information)

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fusage%2Fnavigation_data_processing.ipynb

.. code-block:: python

   #location_mbes is a GeoLocationLatLon object
   print(location_mbes)

.. code-block:: python

   # output (location of mbes in Lat):
   # GeoLocationLatLon
   # #################
   # - latitude:  54°9'0.0"N   [ddd°mm',ss.s''N/S]
   # - longitude: 10°8'60.0"E  [ddd°mm',ss.s''E/W]
   # - z:         2.37         [positive downwards, m]
   # - yaw:       4.88         [90 ° at east]
   # - pitch:     15.01        [° positive bow up]
   # - roll:      29.51        [° positive port up]

The GeoLocation objects are part of the 'datastructures' name space and allow for implicit conversion.

GeoLocationLatLon can be converted to GeoLocationUTM:

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fusage%2Fnavigation_data_processing.ipynb

.. code-block:: python

   # convert this object to UTM
   location_mbes_utm = nav.datastructures.GeoLocationUTM(location_mbes)
   print(location_mbes_utm)

.. code-block:: python

   # output (location of mbes in UTM):
   # GeoLocationUTM
   # ##############
   # - northing:            6000821.95 [positive northwards, m]
   # - easting:             575109.14  [positive eastwards, m]
   # - zone:                32         
   # - northern_hemisphere: true       
   # - z:                   2.37       [positive downwards, m]
   # - yaw:                 4.88       [90 ° at east]
   # - pitch:               15.01      [° positive bow up]
   # - roll:                29.51      [° positive port up]

Other conversion e.g. to/from GeoLocationLocal are also possible. See the GeoLocation module Api for details