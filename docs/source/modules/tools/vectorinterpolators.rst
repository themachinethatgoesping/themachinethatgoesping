vectorinterpolators
###################

This modules provides interpolator objects to find interpolated values in lists.
- x generally describes the index value lists
- y descreibes the corresponding values

Example usage
*************

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Ftools%2Finterpolation.ipynb

.. code-block:: python

    # import this module
    import themachinethatgoesping.tools.vectorinterpolators as vip
    
    # create value lists
   timestamps = [100, 150, 300, 400, 950, 1000]
   values     = [10, 50, 30, 500, -30,-20]

   # create interpolator object (here a linear interpolator)
   linear = vip.LinearInterpolator(X=timestamps, Y=values)

   # find interpolated y value for a given x value (e.g. a random timestamp)
   y_value = lip(target_x=125)
   print(y_value) #<< 30.0

   # find extrapolated y value for value outside timestamps boundary
   y_value = linear(target_x=50)
   print(y_value) #<< -30.0

.. image:: images/vectorinterpolators_1.png


Types
*****

.. autoclass:: themachinethatgoesping.tools.vectorinterpolators.t_extr_mode
   :members: 

Class: AkimaInterpolator
*************************

.. autoclass:: themachinethatgoesping.tools.vectorinterpolators.AkimaInterpolator
   :members: __call__, set_data_XY, append, extend, set_extrapolation_mode, get_extrapolation_mode, get_data_X, get_data_Y, copy, to_binary, from_binary, info_string, print

   .. automethod:: __init__

Class: LinearInterpolator
*************************

.. autoclass:: themachinethatgoesping.tools.vectorinterpolators.LinearInterpolator
   :members: __call__, set_data_XY, append, extend, set_extrapolation_mode, get_extrapolation_mode, get_data_X, get_data_Y, copy, to_binary, from_binary, info_string, print

   .. automethod:: __init__

Class: NearestInterpolator
**************************

.. autoclass:: themachinethatgoesping.tools.vectorinterpolators.NearestInterpolator
   :members: __call__, set_data_XY, append, extend, set_extrapolation_mode, get_extrapolation_mode, get_data_X, get_data_Y, copy, to_binary, from_binary, info_string, print

   .. automethod:: __init__

Class: SlerpInterpolator
************************

Example usage
=============

.. code-block:: python

   # import this module
   import themachinethatgoesping.tools.vectorinterpolators as vip

   # create value lists
   timestamps = [100, 150, 1000] #x list, must be sorted, no duplicates
   yaw       = [10, 50, -20]    #yaw values (degrees)
   pitch     = [10, 50, -20]    #yaw values (degrees)
   roll      = [10, 50, -20]    #yaw values (degrees)

   # create interpolator object (here a linear interpolator)
   slerp = vip.SlerpInterpolator(X=timestamps, Yaw=yaw, Pitch = pitch, Roll = roll)

   # find interpolated y value for a given x value (e.g. a random timestamp)
   ypr_value = slerp(target_x=125)
   print(ypr_value) #<< [23.65708869335217, 32.74209962001251, 23.657088693352158]

   # find extrapolated y value for value outside timestamps boundary
   ypr_value = slerp(target_x=50)
   print(ypr_value) #<< [355.97195450327666, -40.17949250447276, -4.0280454967233394]

Class
=====

.. autoclass:: themachinethatgoesping.tools.vectorinterpolators.SlerpInterpolator
   :members: __call__, set_data_XYPR, append, extend, set_extrapolation_mode, get_extrapolation_mode, get_data_X, get_data_YPR, copy, to_binary, from_binary, info_string, print 

   .. automethod:: __init__
