:py:class:`ForwardGridder <themachinethatgoesping.gridding.forwardgridder.ForwardGridder>`
##########################################################################################

This modules provides a class to create 3D numpy grids from scatter points using a selection of forward mapping functions.



Example usage
*************

.. code-block:: python
    
   import numpy as np

   # import this module
   from themachinethatgoesping.gridding.forwardgridder import ForwardGridder

   # test date
   size=1000000

   sx = np.random.random(size)*100
   sy = np.random.random(size)*100
   sz = np.random.random(size)*100
   sv = np.random.random(size)*1

   # create new grid (auto determine min/max x,y,z)
   grd_res = 1
   gridder = grd.:ForwardGridder:.from_data(grd_res,sx,sy,sz)

   #create 3D numpy array using block mean (fast)
   ival, iweight = gridder.interpolate_block_mean(sx,sy,sz,sv)
   #ival: sum per voxel
   #iweight: num per voxel

   #create 3D numpy array using weighted mean (slower)
   ival, iweight = gridder.interpolate_weighted_mean(sx,sy,sz,sv)

   #compuate total value
   iavg = np.zeros(ival.shape)
   iavg[imagenums > 0] = ival[iweight > 0] / iweight[iweight > 0]
   TotalValue = np.nansum(iavg) * (gridder.xres*gridder.yres*gridder.zres)
  

Class: ForwardGridder
*********************

.. autoclass:: themachinethatgoesping.gridding.forwardgridder.ForwardGridder
   :members:

   .. automethod:: __init__
   

