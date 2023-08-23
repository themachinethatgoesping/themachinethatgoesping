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
    "algorithms",
    "echosounders",
    "gridding",
    "modules",
    "navigation",
    "pingprocessing",
    "pydev_install_module_paths",
    "pydev_install_modules",
    "pydev_install_src_path",
    "tools",
    "tools_ext",
    "version"
]


__modules_installed__ = [('tools', '0.19.3'), ('algorithms', '0.1.10'), ('navigation', '0.11.0'), ('echosounders', '0.19.2'), ('pingprocessing', '0.1.0'), ('gridding', '@PROJECT_VERSION@')]
__submodule = '../'
__version__ = '0.7.1'
pydev_install_module_paths = ['/home/ssd/local/lib/python3.11/site-packages/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//tools/python/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//gridding/python/themachinethatgoesping']
pydev_install_modules = ['tools', 'navigation', 'gridding', '../']
pydev_install_src_path = '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/../'
__extend_path__ = pkgutil.extend_path
