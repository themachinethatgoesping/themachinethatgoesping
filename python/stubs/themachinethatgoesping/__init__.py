"""

themachinethatgoesping
**********************
Enable quantitative processing of multibeam and singlebeam echosounder systems
"""
from __future__ import annotations
from pkgutil import extend_path as __extend_path__
import sys as __internal_module_sys__
from . import algorithms
from . import gridding
from . import navigation
from . import pingprocessing_cppy
from . import scripts
from . import tools
from . import tools_cppy
__all__: list[str] = ['algorithms', 'gridding', 'modules', 'navigation', 'pingprocessing_cppy', 'pydev_install_module_paths', 'pydev_install_modules', 'pydev_install_src_path', 'scripts', 'tools', 'tools_cppy', 'version']
def modules():
    ...
def version():
    ...
__modules_installed__: list = [('tools_cppy', '0.29.1'), ('tools', '@PROJECT_VERSION@'), ('scripts', '@PROJECT_VERSION@'), ('algorithms', '0.9.4'), ('navigation', '0.17.7'), ('pingprocessing_cppy', '0.11.5'), ('gridding', '@PROJECT_VERSION@')]
__submodule: str = '../'
__version__: str = '0.30.4'
pydev_install_module_paths: list = ['/home/peurban/.local/share/mamba/envs/dev/lib/python3.13/site-packages/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//tools/python/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//gridding/python/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//echosounders/python/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//pingprocessing/python/themachinethatgoesping']
pydev_install_modules: list = ['tools', 'navigation', 'gridding', 'echosounders', 'pingprocessing', '../']
pydev_install_src_path: str = '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/../'
