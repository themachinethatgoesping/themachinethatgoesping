from . import (
    algorithms as algorithms,
    algorithms_nanopy as algorithms_nanopy,
    echosounders as echosounders,
    echosounders_nanopy as echosounders_nanopy,
    gridding as gridding,
    navigation as navigation,
    navigation_nanopy as navigation_nanopy,
    pingprocessing as pingprocessing,
    pingprocessing_nanopy as pingprocessing_nanopy,
    scripts as scripts,
    tools as tools,
    tools_nanopy as tools_nanopy
)


__modules_installed__: list = ...

def version(): ...

def modules(): ...
