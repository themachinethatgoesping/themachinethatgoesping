from __future__ import annotations
from themachinethatgoesping.pingprocessing_cppy import ostream_redirect
from . import core
from . import filter_pings
from . import group_pings
from . import overview
from . import split_pings
from . import testing
from . import watercolumn
from . import widgets
__all__ = ['core', 'filter_pings', 'group_pings', 'ostream_redirect', 'overview', 'split_pings', 'testing', 'watercolumn', 'watercolumn_ext', 'widgets']
__version__: str = '@PROJECT_VERSION@'
watercolumn_ext = watercolumn
