"""
ipywidgets backend for the declarative control specifications.

Creates ipywidgets from :mod:`.control_spec` dataclasses and wraps
them in :class:`ControlHandle` / :class:`ControlPanel` objects so the
WCI core can read / write controls without knowing about ipywidgets.
"""

from typing import TypeAlias, Union

import ipywidgets

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

class JupyterControlHandle(themachinethatgoesping.widgets.control_spec.ControlHandle):
    """Wraps a single ipywidgets widget."""

    def __init__(self, widget: ipywidgets.Widget) -> None: ...

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
    def widget(self) -> ipywidgets.Widget:
        """The underlying ipywidgets widget (useful for layout assembly)."""

def create_jupyter_control(spec: ControlSpecType) -> JupyterControlHandle:
    """Create a :class:`JupyterControlHandle` from a specification."""

class JupyterControlPanel(themachinethatgoesping.widgets.control_spec.ControlPanel):
    """
    A :class:`ControlPanel` backed by ipywidgets.

    After construction every registered control can be accessed by name
    through ``panel["name"]``.  The underlying ipywidgets widget for
    layout assembly is available via ``panel["name"].widget``.
    """

    @classmethod
    def from_specs(cls, *spec_lists: List[ControlSpecType]) -> 'JupyterControlPanel':
        """Build a panel from one or more flat lists of specs."""

    def widget(self, name: str) -> ipywidgets.Widget:
        """Short-hand: return the underlying ipywidgets.Widget by control name."""

    def widgets(self, *names: str) -> List[ipywidgets.Widget]:
        """Return a list of underlying ipywidgets.Widgets."""

    def hbox(self, *names: str) -> ipywidgets.HBox:
        """Return an HBox containing the named widgets."""

    def vbox(self, *names: str) -> ipywidgets.VBox:
        """Return a VBox containing the named widgets."""

    def build_tabs(self, tab_layouts: Dict[str, List[List[str]]]) -> ipywidgets.Tab:
        """
        Build an ``ipywidgets.Tab`` widget.

        Parameters
        ----------
        tab_layouts
            ``{tab_name: [[row0_ctrl_names], [row1_ctrl_names], ...]}``
        """
