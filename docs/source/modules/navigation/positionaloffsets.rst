PositionalOffsets
#################

Simple structure to store sensor offsets

Example usage
=============

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/themachinethatgoesping/tutorials/main?urlpath=lab%2Ftree%2Fnavigation%2Fpositionaloffsets.ipynb

.. code-block:: python

    # import this module
    from themachinethatgoesping.navigation import PositionalOffsets
    
    offsets = PositionalOffsets(1,2,3,10,20,30)
    print(offsets)

   # PositionalOffsets
   # *****************
   # - x:     1.00  [positive forwards, m]
   # - y:     2.00  [positive starboard, m]
   # - z:     3.00  [positive downwards, m]
   # - yaw:   10.00 [90 ° at east]
   # - pitch: 20.00 [° positve bow up]
   # - roll:  30.00 [° positive port up]


Class
=====
   
.. autoclass:: themachinethatgoesping.navigation.PositionalOffsets
   :members:

   .. automethod:: __init__

