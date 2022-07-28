PositionalOffsets
#################

Simple structures to store sensor position offsets

Example usage
=============

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fnavigation%2Fpositionaloffsets.ipynb

.. code-block:: python

   # import this module# import this module
   from themachinethatgoesping.navigation.datastructures import PositionalOffsets

   sensor_offsets = PositionalOffsets(
   10, # x (in m, positive forward)
   -3, # y (in m, positive starboard)
   3,  # z (in m, positive downwards)
   10, # yaw    (in °, positive is clockwise rotation)
   20, # pitch  (in °, positive is bow up)
   30) # roll   (in °, positive is port up)

   print(sensor_offsets)
   # PositionalOffsets
   # *****************
   # - x:     10.00 [positive forwards, m]
   # - y:     -3.00 [positive starboard, m]
   # - z:     3.00  [positive downwards, m]
   # - yaw:   10.00 [° positive means clockwise rotation]
   # - pitch: 20.00 [° positive means bow up]
   # - roll:  30.00 [° positive means port up]
   
Structure api
=============

.. autoclass:: themachinethatgoesping.navigation.datastructures.PositionalOffsets
   :members:
   :special-members: __init__
