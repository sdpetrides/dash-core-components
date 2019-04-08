# pylint: disable=line-too-long, redefined-builtin, too-many-arguments, too-many-locals, unused-argument, unused-import, too-many-ancestors  # noqa: E501
"""
Autogenerated file
DO NOT EDIT.
"""
import typing

from dash_component_system import (
    DashComponent, UNDEFINED, Undefined, ComponentProp
)


class RadioItems(DashComponent):
    """
    RadioItems is a component that encapsulates several radio item inputs. The
    values and labels of the RadioItems is specified in the `options` property
    and the seleced item is specified with the `value` property. Each radio
    item is rendered as an input with a surrounding label.
    """

    _namespace = 'dash_core_components'
    _typename = 'RadioItems'
    available_wildcard_properties = [

    ]
    id = ComponentProp('id', UNDEFINED, False)
    options = ComponentProp('options', UNDEFINED, False)
    value = ComponentProp('value', UNDEFINED, False)
    style = ComponentProp('style', UNDEFINED, False)
    className = ComponentProp('className', UNDEFINED, False)
    inputStyle = ComponentProp('inputStyle', UNDEFINED, False)
    inputClassName = ComponentProp('inputClassName', '', False)
    labelStyle = ComponentProp('labelStyle', UNDEFINED, False)
    labelClassName = ComponentProp('labelClassName', '', False)
    loading_state = ComponentProp('loading_state', UNDEFINED, False)

    def __init__(
            self,
            id=UNDEFINED,
            options=UNDEFINED,
            value=UNDEFINED,
            style=UNDEFINED,
            className=UNDEFINED,
            inputStyle=UNDEFINED,
            inputClassName='',
            labelStyle=UNDEFINED,
            labelClassName='',
            loading_state=UNDEFINED,
    ):
        # type: (typing.Union[str, Undefined], typing.Union[typing.List[typing.Dict[str, typing.Union[str, bool]]], Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict[str, typing.Union[bool, str]], Undefined]) -> None # noqa: E501
        """
        :param id:
        :param options: An array of options(default=[])
        :param value: The currently selected value
        :param style: The style of the container (div)
        :param className: The class of the container (div)
        :param inputStyle: The style of the <input> radio
            element(default={})
        :param inputClassName: The class of the <input> radio
            element(default='')
        :param labelStyle: The style of the <label> that wraps the radio
            input  and the option's label(default={})
        :param labelClassName: The class of the <label> that wraps the
            radio input  and the option's
            label(default='')
        :param loading_state: Object that holds the loading state object
            coming from dash-renderer
        """
        DashComponent.__init__(self, locals())
