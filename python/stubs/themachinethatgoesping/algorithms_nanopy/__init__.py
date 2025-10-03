"""
Python module process ping data, e.g. apply absorption, spreading loss, compute range/depth, raytrace ...
"""
from __future__ import annotations
from . import amplitudecorrection
from . import featuremapping
from . import geoprocessing
from . import gridding
from . import imageprocessing
from . import pointprocessing
from . import signalprocessing
__all__: list[str] = ['amplitudecorrection', 'featuremapping', 'geoprocessing', 'gridding', 'imageprocessing', 'pointprocessing', 'signalprocessing']
__version__: str = '0.9.5'
