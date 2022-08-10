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
    "gridding",
    "modules_installed",
    "navigation",
    "pydev_install_module_paths",
    "pydev_install_modules",
    "pydev_install_src_path",
    "tools",
    "tools_ext"
]


__submodule = '../'
modules_installed = ['tools', 'tools_ext', 'navigation', 'gridding']
pydev_install_module_paths = ['/ssd/local/lib/python3/dist-packages/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//tools/python/themachinethatgoesping', '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/..//gridding/python/themachinethatgoesping']
pydev_install_modules = ['tools', 'navigation', 'gridding', '../']
pydev_install_src_path = '/ssd/src/themachinethatgoesping/themachinethatgoesping/subprojects/meta/../'
