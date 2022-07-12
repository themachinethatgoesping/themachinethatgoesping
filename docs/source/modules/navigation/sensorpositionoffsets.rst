SensorPositionOffsets
#####################

Store sensor offsets

Example usage
=============

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

