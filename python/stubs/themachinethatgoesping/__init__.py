"""

themachinethatgoesping
**********************
Enable quantitative processing of multibeam and singlebeam echosounder systems
"""
from __future__ import annotations
from pkgutil import extend_path as __extend_path__
import sys as __internal_module_sysy__
from . import algorithms
from . import echosounders
from . import gridding
from . import navigation
from . import pingprocessing
from . import tools
from . import tools_ext
__all__ = ['algorithms', 'echosounders', 'gridding', 'modules', 'navigation', 'pingprocessing', 'pydev_install_module_paths', 'pydev_install_modules', 'pydev_install_src_path', 'tools', 'tools_ext', 'version']
def modules():
    ...
def version():
    ...
__modules_installed__: list = [('tools', '0.19.5'), ('algorithms', '0.3.0'), ('navigation', '0.11.0'), ('echosounders', '0.22.0'), ('pingprocessing', '0.1.0'), ('gridding', '@PROJECT_VERSION@')]
__submodule: str = '../'
__version__: str = '0.8.0'
pydev_install_module_paths: list = ['/home/ssd/local/lib/python3.11/site-packages/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//tools/python/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//gridding/python/themachinethatgoesping']
pydev_install_modules: list = ['tools', 'navigation', 'gridding', '../']
pydev_install_src_path: str = '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/../'
