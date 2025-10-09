"""

themachinethatgoesping
**********************
Enable quantitative processing of multibeam and singlebeam echosounder systems
"""
from __future__ import annotations
from pkgutil import extend_path as __extend_path__
import sys as __internal_module_sys__
from . import algorithms_nanopy
from . import echosounders
from . import echosounders_nanopy
from . import navigation
from . import navigation_nanopy
from . import pingprocessing_cppy
from . import scripts
from . import tools
from . import tools_nanopy
__all__: list[str] = ['algorithms_nanopy', 'echosounders', 'echosounders_nanopy', 'modules', 'navigation', 'navigation_nanopy', 'pingprocessing_cppy', 'pydev_install_module_paths', 'pydev_install_modules', 'pydev_install_src_path', 'scripts', 'tools', 'tools_nanopy', 'version']
def modules():
    ...
def version():
    ...
__modules_installed__: list = [('tools_nanopy', '0.30.0'), ('tools', '@PROJECT_VERSION@'), ('scripts', '@PROJECT_VERSION@'), ('navigation_nanopy', '0.17.7'), ('navigation', '@PROJECT_VERSION@'), ('algorithms_nanopy', '0.9.5'), ('echosounders_nanopy', '0.45.6'), ('echosounders', '0.45.6'), ('pingprocessing_cppy', '0.11.6')]
__submodule: str = '../'
__version__: str = '0.30.5'
pydev_install_module_paths: list = ['/home/peurban/.local/share/mamba/envs/dev/lib/python3.13/site-packages/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//tools/python/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//navigation/python/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//gridding/python/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//echosounders/python/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//pingprocessing/python/themachinethatgoesping']
pydev_install_modules: list = ['tools', 'navigation', 'gridding', 'echosounders', 'pingprocessing', '../']
pydev_install_src_path: str = '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/../'
