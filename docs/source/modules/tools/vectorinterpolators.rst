vectorinterpolators
###################

This modules provides interpolator objects to find interpolated values in lists.
- x generally describes the index value lists
- y descreibes the corresponding values

Example usage
*************

.. code-block:: python

    # import this module
    import themachinethatgoesping.tools.vectorinterpolators as vip
    
    # create value lists
    timestamps = [100, 150, 1000] #x list, must be sorted, no duplicates
    values     = [10, 50, -20]    #y list, same size as x list

    # create interpolator object (here a linear interpolator)
    nearest = vip.LinearInterpolator(X=timestamps, Y=values)

    # find interpolated y value for a given x value (e.g. a random timestamp)
    y_value = nearest.interpolate(target_x=125)
    print(y_value) #<< 30.0

    # find extrapolated y value for value outside timestamps boundary
    y_value = nearest.interpolate(target_x=50)
    print(y_value) #<< -30.0

  

Types
*****

.. autoclass:: themachinethatgoesping.tools.vectorinterpolators.t_extr_mode
   :members:

Class: LinearInterpolator
*************************

.. autoclass:: themachinethatgoesping.tools.vectorinterpolators.LinearInterpolator
   :members:

Class: NearestInterpolator
**************************

.. autoclass:: themachinethatgoesping.tools.vectorinterpolators.NearestInterpolator
   :members:
