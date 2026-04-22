"""
Qt (native) backend for the declarative control specifications.

Creates Qt widgets from :mod:`.control_spec` dataclasses and wraps
them in :class:`ControlHandle` / :class:`ControlPanel` objects so
:class:`wciviewer_core.WCICore` can be driven from a native Qt application.
"""

from typing import TypeAlias, Union

import QtWidgets

import themachinethatgoesping.pingprocessing.widgets.control_spec
from themachinethatgoesping.pingprocessing.widgets.control_spec import (
    ButtonSpec as ButtonSpec,
    CheckboxSpec as CheckboxSpec,
    ControlHandle as ControlHandle,
    ControlPanel as ControlPanel,
    DropdownSpec as DropdownSpec,
    FloatSliderSpec as FloatSliderSpec,
    FloatTextSpec as FloatTextSpec,
    HTMLSpec as HTMLSpec,
    IntSliderSpec as IntSliderSpec,
    IntTextSpec as IntTextSpec,
    LabelSpec as LabelSpec,
    MultiSelectSpec as MultiSelectSpec,
    TextSpec as TextSpec
)


ControlSpecType: TypeAlias = Union[themachinethatgoesping.pingprocessing.widgets.control_spec.FloatSliderSpec, themachinethatgoesping.pingprocessing.widgets.control_spec.IntSliderSpec, themachinethatgoesping.pingprocessing.widgets.control_spec.DropdownSpec, themachinethatgoesping.pingprocessing.widgets.control_spec.MultiSelectSpec, themachinethatgoesping.pingprocessing.widgets.control_spec.CheckboxSpec, themachinethatgoesping.pingprocessing.widgets.control_spec.IntTextSpec, themachinethatgoesping.pingprocessing.widgets.control_spec.FloatTextSpec, themachinethatgoesping.pingprocessing.widgets.control_spec.ButtonSpec, themachinethatgoesping.pingprocessing.widgets.control_spec.LabelSpec, themachinethatgoesping.pingprocessing.widgets.control_spec.TextSpec, themachinethatgoesping.pingprocessing.widgets.control_spec.HTMLSpec]

class QtControlHandle(themachinethatgoesping.pingprocessing.widgets.control_spec.ControlHandle):
    """
    Wraps a single Qt widget and exposes the unified ControlHandle API.

    Parameters
    ----------
    widget : QWidget
        The outermost widget (may be a labelled container).
    value_getter, value_setter
        Callables to read/write the control value.
    change_signal
        Qt signal emitted when the value changes.
    inner : QWidget, optional
        The actual editable widget inside *widget* (e.g. the QSlider or
        QSpinBox inside a labelled container).  If *None*, *widget* is
        treated as both outer and inner widget.
    """

    def __init__(self, widget: QtWidgets.QWidget, value_getter, value_setter, change_signal=None, *, inner: QtWidgets.QWidget | None = None) -> None: ...

    @property
    def value(self) -> Any: ...

    @value.setter
    def value(self, v: Any) -> None: ...

    def on_change(self, callback: Callable[[Any], None]) -> None: ...

    def on_click(self, callback: Callable) -> None: ...

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

    @property
    def widget(self) -> QtWidgets.QWidget: ...

def create_qt_control(spec: ControlSpecType) -> QtControlHandle:
    """Create a :class:`QtControlHandle` from a specification."""

class QtControlPanel(themachinethatgoesping.pingprocessing.widgets.control_spec.ControlPanel):
    """A :class:`ControlPanel` backed by native Qt widgets."""

    @classmethod
    def from_specs(cls, *spec_lists: List[ControlSpecType]) -> 'QtControlPanel': ...

    def widget(self, name: str) -> QtWidgets.QWidget: ...

    def widgets(self, *names: str) -> List[QtWidgets.QWidget]: ...

    def hbox_widget(self, *names: str) -> QtWidgets.QWidget:
        """Return a QWidget with an HBoxLayout containing the named widgets."""

    def build_tab_widget(self, tab_layouts: Dict[str, List[List[str]]]) -> QtWidgets.QTabWidget:
        """Build a ``QTabWidget`` with the given layout."""
