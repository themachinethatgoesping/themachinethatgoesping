from __future__ import annotations
import ipywidgets as ipywidgets
from tqdm.notebook import tqdm_notebook as tqdm
import traitlets.traitlets
import typing
__all__ = ['TqdmWidget', 'ipywidgets', 'tqdm']
class TqdmWidget(ipywidgets.widgets.widget_box.HBox):
    _all_trait_default_generators: typing.ClassVar[dict]  # value = {'_display_callbacks': traitlets.traitlets.TraitType.default, '_dom_classes': traitlets.traitlets.TraitType.default, '_model_module': traitlets.traitlets.TraitType.default, '_model_module_version': traitlets.traitlets.TraitType.default, '_model_name': traitlets.traitlets.TraitType.default, '_msg_callbacks': traitlets.traitlets.TraitType.default, '_property_lock': traitlets.traitlets.TraitType.default, '_states_to_send': traitlets.traitlets.TraitType.default, '_view_count': traitlets.traitlets.TraitType.default, '_view_module': traitlets.traitlets.TraitType.default, '_view_module_version': traitlets.traitlets.TraitType.default, '_view_name': traitlets.traitlets.TraitType.default, 'box_style': traitlets.traitlets.TraitType.default, 'children': traitlets.traitlets.TraitType.default, 'comm': traitlets.traitlets.TraitType.default, 'keys': <traitlets.traitlets.DefaultHandler object>, 'layout': traitlets.traitlets.TraitType.default, 'log': <traitlets.traitlets.DefaultHandler object>}
    _descriptors: typing.ClassVar[list]  # value = [<traitlets.traitlets.ObserveHandler object>, <traitlets.traitlets.DefaultHandler object>, <traitlets.traitlets.Instance object>, <ipywidgets.widgets.trait_types.TypedTuple object>, <traitlets.traitlets.DefaultHandler object>, <traitlets.traitlets.Unicode object>, <traitlets.traitlets.Unicode object>, <traitlets.traitlets.Unicode object>, <traitlets.traitlets.Instance object>, <traitlets.traitlets.Dict object>, <traitlets.traitlets.Set object>, <traitlets.traitlets.Int object>, <traitlets.traitlets.Unicode object>, <traitlets.traitlets.Unicode object>, <traitlets.traitlets.Unicode object>, <traitlets.traitlets.CaselessStrEnum object>, <ipywidgets.widgets.trait_types.TypedTuple object>, <traitlets.traitlets.Any object>, <traitlets.traitlets.List object>, <ipywidgets.widgets.trait_types.InstanceDict object>, <traitlets.traitlets.Instance object>]
    _instance_inits: typing.ClassVar[list] = [traitlets.traitlets.ObserveHandler.instance_init, traitlets.traitlets.BaseDescriptor.instance_init, traitlets.traitlets.Instance.instance_init, traitlets.traitlets.BaseDescriptor.instance_init, traitlets.traitlets.Instance.instance_init, traitlets.traitlets.Instance.instance_init, traitlets.traitlets.Instance.instance_init, traitlets.traitlets.Instance.instance_init]
    _static_immutable_initial_values: typing.ClassVar[dict] = {'_model_module': '@jupyter-widgets/controls', '_model_module_version': '1.5.0', '_model_name': 'HBoxModel', '_view_count': None, '_view_module': '@jupyter-widgets/controls', '_view_module_version': '1.5.0', '_view_name': 'HBoxView', 'comm': None}
    _trait_default_generators: typing.ClassVar[dict] = {}
    _traits: typing.ClassVar[dict]  # value = {'_display_callbacks': <traitlets.traitlets.Instance object>, '_dom_classes': <ipywidgets.widgets.trait_types.TypedTuple object>, '_model_module': <traitlets.traitlets.Unicode object>, '_model_module_version': <traitlets.traitlets.Unicode object>, '_model_name': <traitlets.traitlets.Unicode object>, '_msg_callbacks': <traitlets.traitlets.Instance object>, '_property_lock': <traitlets.traitlets.Dict object>, '_states_to_send': <traitlets.traitlets.Set object>, '_view_count': <traitlets.traitlets.Int object>, '_view_module': <traitlets.traitlets.Unicode object>, '_view_module_version': <traitlets.traitlets.Unicode object>, '_view_name': <traitlets.traitlets.Unicode object>, 'box_style': <traitlets.traitlets.CaselessStrEnum object>, 'children': <ipywidgets.widgets.trait_types.TypedTuple object>, 'comm': <traitlets.traitlets.Any object>, 'keys': <traitlets.traitlets.List object>, 'layout': <ipywidgets.widgets.trait_types.InstanceDict object>, 'log': <traitlets.traitlets.Instance object>}
    def __call__(self, list_like, **kwargs):
        ...
    def __init__(self, **kwargs):
        ...
    def __iter__(self):
        ...
    def __len__(self):
        ...
    def __next__(self):
        ...
    def close(self):
        ...
    def set_description(self, desc):
        ...
    def update(self):
        ...
