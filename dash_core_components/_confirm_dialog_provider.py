# pylint: disable=line-too-long, redefined-builtin, too-many-arguments, too-many-locals, unused-argument, unused-import, too-many-ancestors  # noqa: E501
"""
Autogenerated file
DO NOT EDIT.
"""
import typing

from dash_component_system import (
    DashComponent, UNDEFINED, Undefined, ComponentProp
)


class ConfirmDialogProvider(DashComponent):
    """
    A wrapper component that will display a confirmation dialog when its child
    component has been clicked on.  For example: ```
    dcc.ConfirmDialogProvider(     html.Button('click me', id='btn'),
    message='Danger - Are you sure you want to continue.'     id='confirm')
    ```
    """

    _namespace = 'dash_core_components'
    _typename = 'ConfirmDialogProvider'
    available_wildcard_properties = [

    ]
    id = ComponentProp('id', UNDEFINED, False)
    message = ComponentProp('message', UNDEFINED, False)
    submit_n_clicks = ComponentProp('submit_n_clicks', 0, False)
    submit_n_clicks_timestamp = ComponentProp('submit_n_clicks_timestamp', -1, False)  # noqa: E501
    cancel_n_clicks = ComponentProp('cancel_n_clicks', 0, False)
    cancel_n_clicks_timestamp = ComponentProp('cancel_n_clicks_timestamp', -1, False)  # noqa: E501
    displayed = ComponentProp('displayed', UNDEFINED, False)
    children = ComponentProp('children', UNDEFINED, False)
    loading_state = ComponentProp('loading_state', UNDEFINED, False)

    def __init__(
            self,
            children=UNDEFINED,
            id=UNDEFINED,
            message=UNDEFINED,
            submit_n_clicks=0,
            submit_n_clicks_timestamp=-1,
            cancel_n_clicks=0,
            cancel_n_clicks_timestamp=-1,
            displayed=UNDEFINED,
            loading_state=UNDEFINED,
    ):
        # type: (typing.Union[typing.Any, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[bool, Undefined], typing.Union[typing.Dict[str, typing.Union[bool, str]], Undefined]) -> None # noqa: E501
        """
        :param id:
        :param message: Message to show in the popup.
        :param submit_n_clicks: Number of times the submit was
            clicked(default=0)
        :param submit_n_clicks_timestamp: Last time the submit button was
            clicked.(default=-1)
        :param cancel_n_clicks: Number of times the popup was
            canceled.(default=0)
        :param cancel_n_clicks_timestamp: Last time the cancel button was
            clicked.(default=-1)
        :param displayed: Is the modal currently displayed.
        :param children: The children to hijack clicks from and display the
            popup.
        :param loading_state: Object that holds the loading state object
            coming from dash-renderer
        """
        DashComponent.__init__(self, locals())
