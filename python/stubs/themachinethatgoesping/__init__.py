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
__modules_installed__: list = [('tools_cppy', '0.24.1'), ('tools', '@PROJECT_VERSION@'), ('scripts', '@PROJECT_VERSION@'), ('algorithms', '0.8.0'), ('navigation', '0.16.0'), ('echosounders_cppy', '0.39.1'), ('echosounders', '0.39.1'), ('pingprocessing_cppy', '0.8.0'), ('pingprocessing', '@PROJECT_VERSION@'), ('gridding', '0.2.0')]
__version__: str = '0.23.2'
