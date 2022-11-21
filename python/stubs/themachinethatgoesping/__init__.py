"""
themachinethatgoesping
**********************
Enable quantitative processing of multibeam and singlebeam echosounder systems
"""
from __future__ import annotations
import themachinethatgoesping
import typing
import sys

__all__ = [
    "echosounders",
    "gridding",
    "modules",
    "navigation",
    "pydev_install_module_paths",
    "pydev_install_modules",
    "pydev_install_src_path",
    "tools",
    "tools_ext",
    "version"
]


__modules_installed__ = [('tools', '0.13.1'), ('navigation', '0.6.6'), ('echosounders', '0.9.1'), ('gridding', '@PROJECT_VERSION@')]
__submodule = '../'
__version__ = '0.4.2'
pydev_install_module_paths = ['/ssd/local/lib/python3.10/site-packages/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//tools/python/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//gridding/python/themachinethatgoesping']
pydev_install_modules = ['tools', 'navigation', 'gridding', '../']
pydev_install_src_path = '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/../'
