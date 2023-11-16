"""

themachinethatgoesping
**********************
Enable quantitative processing of multibeam and singlebeam echosounder systems
"""
from __future__ import annotations
from . import algorithms
from . import echosounders
from . import echosounders_cppy
from . import gridding
from . import navigation
from . import pingprocessing
from . import pingprocessing_cppy
from . import scripts
from . import tools
from . import tools_cppy
__all__ = ['algorithms', 'echosounders', 'echosounders_cppy', 'gridding', 'modules', 'navigation', 'pingprocessing', 'pingprocessing_cppy', 'scripts', 'tools', 'tools_cppy', 'version']
def modules():
    ...
def version():
    ...
__modules_installed__: list = [('tools_cppy', '0.21.4'), ('tools', '@PROJECT_VERSION@'), ('scripts', '@PROJECT_VERSION@'), ('algorithms', '0.5.3'), ('navigation', '0.14.1'), ('echosounders_cppy', '0.31.0'), ('echosounders', '0.31.0'), ('pingprocessing_cppy', '0.3.4'), ('pingprocessing', '@PROJECT_VERSION@'), ('gridding', '0.1.7')]
__version__: str = '0.14.1'
