SensorPositionOffsets
#####################

Store sensor offsets

Example usage
=============

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fnavigation%2Fsensorpositionoffsets.ipynb

.. code-block:: python

    # import this module
    from themachinethatgoesping.navigation import SensorPositionOffsets
    
    offsets = SensorPositionOffsets(1,2,3,10,20,30)
    print(offsets)

    # SensorPositionOffsets
    # *********************
    # - x:     1.00  [m]
    # - y:     2.00  [m]
    # - z:     3.00  [m]
    # - yaw:   10.00 [°]
    # - pitch: 20.00 [°]
    # - roll:  30.00 [°]


Class
=====
   
.. autoclass:: themachinethatgoesping.navigation.SensorPositionOffsets
   :members:

   .. automethod:: __init__

