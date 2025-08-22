"""
Functions for creating waterolumn images.
"""
from __future__ import annotations
import numpy
import themachinethatgoesping.echosounders_cppy.filetemplates
__all__: list[str] = ['make_wci']
def make_wci(ping: themachinethatgoesping.echosounders_cppy.filetemplates.I_Ping) -> numpy.ndarray[numpy.float32]:
    ...
