"""
Backend-agnostic core for the combined viewer.

Thin registry that manages a flat list of viewer entries.  Each entry
wraps an existing viewer instance (created with ``embedded=True``) and
carries a layout hint.  Backends resolve the hints into concrete
layouts.

Cross-wiring between viewers is intentionally left to the user — call
the viewers' own ``connect_*`` or ``core.connect_*`` methods directly.
"""

import dataclasses


class ViewerEntry:
    """One viewer inside the combined window."""

    position: str = 'auto'

    uid: int = 0

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, viewer: Any, name: str, position: str = 'auto', uid: int = 0) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ('viewer', 'name', 'position', 'uid')

class CombinedViewerCore:
    """
    Backend-agnostic list of viewer entries.

    Usage::

        core = CombinedViewerCore()
        entry = core.add(viewer_instance, name="WCI", position="top-left")
    """

    def __init__(self) -> None: ...

    def add(self, viewer: Any, name: str = '', position: str = 'auto') -> ViewerEntry:
        """Register *viewer* and return its :class:`ViewerEntry`."""

    def remove(self, entry: ViewerEntry) -> None:
        """Unregister *entry*."""

    @property
    def entries(self) -> List[ViewerEntry]: ...
