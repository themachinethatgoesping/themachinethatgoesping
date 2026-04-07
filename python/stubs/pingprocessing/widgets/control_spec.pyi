"""
Declarative control specifications for WCI viewer widgets.

Defines dataclasses that describe UI controls (sliders, dropdowns, etc.)
without binding to any specific toolkit.  Factory modules
(``control_jupyter``, ``control_qt``) read these specs and create concrete
widgets.
"""

import dataclasses
from typing import TypeAlias, Union


__conditional_annotations__: set = ...

class FloatSliderSpec:
    """
    FloatSliderSpec(name: 'str', description: 'str', min: 'float' = 0.0, max: 'float' = 100.0, step: 'float' = 1.0, value: 'float' = 0.0, width: 'str' = '220px')
    """

    min: float = 0.0

    max: float = 100.0

    step: float = 1.0

    value: float = 0.0

    width: str = '220px'

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, description: str, min: float = 0.0, max: float = 100.0, step: float = 1.0, value: float = 0.0, width: str = '220px') -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

class IntSliderSpec:
    """
    IntSliderSpec(name: 'str', description: 'str', min: 'int' = 0, max: 'int' = 100, step: 'int' = 1, value: 'int' = 0, width: 'str' = '200px')
    """

    min: int = 0

    max: int = 100

    step: int = 1

    value: int = 0

    width: str = '200px'

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, description: str, min: int = 0, max: int = 100, step: int = 1, value: int = 0, width: str = '200px') -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

class DropdownSpec:
    """
    DropdownSpec(name: 'str', description: 'str', options: 'list' = <factory>, value: 'Any' = None, width: 'str' = '180px')
    """

    value: None = None

    width: str = '180px'

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, description: str, options: list = ..., value: Any = None, width: str = '180px') -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

class CheckboxSpec:
    r"""
    CheckboxSpec(name: 'str', description: 'str', value: 'bool' = False, tooltip: 'str' = \'\')
    """

    value: bool = False

    tooltip: str = ''

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, description: str, value: bool = False, tooltip: str = '') -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ('name', 'description', 'value', 'tooltip')

class IntTextSpec:
    """
    IntTextSpec(name: 'str', description: 'str', value: 'int' = 0, width: 'str' = '140px')
    """

    value: int = 0

    width: str = '140px'

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, description: str, value: int = 0, width: str = '140px') -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ('name', 'description', 'value', 'width')

class FloatTextSpec:
    """
    FloatTextSpec(name: 'str', description: 'str', value: 'float' = 0.0, width: 'str' = '140px')
    """

    value: float = 0.0

    width: str = '140px'

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, description: str, value: float = 0.0, width: str = '140px') -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ('name', 'description', 'value', 'width')

class ButtonSpec:
    r"""
    ButtonSpec(name: 'str', description: 'str', tooltip: 'str' = \'\', width: 'str' = '80px')
    """

    tooltip: str = ''

    width: str = '80px'

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, description: str, tooltip: str = '', width: str = '80px') -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ('name', 'description', 'tooltip', 'width')

class LabelSpec:
    r"""LabelSpec(name: 'str', value: 'str' = \'\', width: 'str' = '100px')"""

    value: str = ''

    width: str = '100px'

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, value: str = '', width: str = '100px') -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ('name', 'value', 'width')

class TextSpec:
    r"""
    TextSpec(name: 'str', description: 'str', value: 'str' = \'\', disabled: 'bool' = False, width: 'str' = '200px')
    """

    value: str = ''

    disabled: bool = False

    width: str = '200px'

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, description: str, value: str = '', disabled: bool = False, width: str = '200px') -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

class HTMLSpec:
    """HTMLSpec(name: 'str', value: 'str' = '&nbsp;')"""

    value: str = '&nbsp;'

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, name: str, value: str = '&nbsp;') -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    __match_args__: tuple = ('name', 'value')

ControlSpecType: TypeAlias = Union[FloatSliderSpec, IntSliderSpec, DropdownSpec, CheckboxSpec, IntTextSpec, FloatTextSpec, ButtonSpec, LabelSpec, TextSpec, HTMLSpec]

class ControlHandle:
    """Base class for a UI-agnostic control handle."""

    @property
    def value(self) -> Any: ...

    @value.setter
    def value(self, v: Any) -> None: ...

    def on_change(self, callback: Callable[[Any], None]) -> None:
        """
        Register a callback for value changes.  *callback* receives the
        new value.
        """

    def on_click(self, callback: Callable) -> None:
        """Register a click handler (buttons only)."""

    @property
    def visible(self) -> bool: ...

    @visible.setter
    def visible(self, v: bool) -> None: ...

    @property
    def max(self) -> Any: ...

    @max.setter
    def max(self, v: Any) -> None: ...

    @property
    def step(self) -> Any: ...

    @step.setter
    def step(self, v: Any) -> None: ...

    @property
    def description(self) -> str: ...

    @description.setter
    def description(self, v: str) -> None: ...

    @property
    def disabled(self) -> bool: ...

    @disabled.setter
    def disabled(self, v: bool) -> None: ...

    @property
    def options(self) -> Any: ...

    @options.setter
    def options(self, v: Any) -> None: ...

class ControlPanel:
    """Container mapping control names to :class:`ControlHandle` objects."""

    def __init__(self) -> None: ...

    def __getitem__(self, name: str) -> ControlHandle: ...

    def __setitem__(self, name: str, handle: ControlHandle) -> None: ...

    def __contains__(self, name: str) -> bool: ...

    def keys(self): ...

WCI_VALUE_CHOICES: list = ...

GRID_LAYOUTS: list = ...

WCI_RENDER_SPECS: list = ...

WCI_STACK_SPECS: list = ...

WCI_TIMING_SPECS: list = ...

WCI_PLAYBACK_SPECS: list = ...

WCI_VIDEO_SPECS: list = ...

WCI_MISC_SPECS: list = ...

WCI_TABS: dict = ...

WCI_TAB_LAYOUT: dict = ...

ECHO_RENDER_SPECS: list = ...

ECHO_NAV_SPECS: list = ...

ECHO_MISC_SPECS: list = ...

ECHO_PARAM_SPECS: list = ...

ECHO_TAB_LAYOUT: dict = ...

MAP_COLORMAPS: list = ...

MAP_NAV_SPECS: list = ...

MAP_MISC_SPECS: list = ...

MAP_MEASURE_SPECS: list = ...

MAP_COLORBAR_SPECS: list = ...

MAP_TAB_LAYOUT: dict = ...
