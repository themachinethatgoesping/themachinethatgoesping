"""
Qt (native) backend for the declarative control specifications.

Creates Qt widgets from :mod:`.control_spec` dataclasses and wraps
them in :class:`ControlHandle` / :class:`ControlPanel` objects so
:class:`wciviewer_core.WCICore` can be driven from a native Qt application.
"""

from typing import TypeAlias, Union

import QtWidgets

import themachinethatgoesping.widgets.control_spec
from themachinethatgoesping.widgets.control_spec import (
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


ControlSpecType: TypeAlias = Union[themachinethatgoesping.widgets.control_spec.FloatSliderSpec, themachinethatgoesping.widgets.control_spec.IntSliderSpec, themachinethatgoesping.widgets.control_spec.DropdownSpec, themachinethatgoesping.widgets.control_spec.MultiSelectSpec, themachinethatgoesping.widgets.control_spec.CheckboxSpec, themachinethatgoesping.widgets.control_spec.IntTextSpec, themachinethatgoesping.widgets.control_spec.FloatTextSpec, themachinethatgoesping.widgets.control_spec.ButtonSpec, themachinethatgoesping.widgets.control_spec.LabelSpec, themachinethatgoesping.widgets.control_spec.TextSpec, themachinethatgoesping.widgets.control_spec.HTMLSpec]

class QtControlHandle(themachinethatgoesping.widgets.control_spec.ControlHandle):
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

    def set_silent(self, v: Any) -> None:
        """
        Set the value **without** emitting Qt change signals.

        Blocks signals on the inner widget (and any paired spin box) so a
        programmatic write performed during time-synchronisation cannot
        re-enter the ping-change handlers through ``valueChanged``.  Qt
        re-emits ``valueChanged`` synchronously and the ping-slider adapter
        buffers those events, so suppressing the emission here is what breaks
        the synchronisation feedback loop.
        """

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

class QtControlPanel(themachinethatgoesping.widgets.control_spec.ControlPanel):
    """A :class:`ControlPanel` backed by native Qt widgets."""

    @classmethod
    def from_specs(cls, *spec_lists: List[ControlSpecType]) -> 'QtControlPanel': ...

    def widget(self, name: str) -> QtWidgets.QWidget: ...

    def widgets(self, *names: str) -> List[QtWidgets.QWidget]: ...

    def hbox_widget(self, *names: str) -> QtWidgets.QWidget:
        """Return a QWidget with an HBoxLayout containing the named widgets."""

    def build_tab_widget(self, tab_layouts: Dict[str, List[List[str]]]) -> QtWidgets.QTabWidget:
        """Build a ``QTabWidget`` with the given layout."""
