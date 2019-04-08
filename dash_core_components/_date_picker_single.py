# pylint: disable=line-too-long, redefined-builtin, too-many-arguments, too-many-locals, unused-argument, unused-import, too-many-ancestors  # noqa: E501
"""
Autogenerated file
DO NOT EDIT.
"""
import typing

from dash_component_system import (
    DashComponent, UNDEFINED, Undefined, ComponentProp
)


class DatePickerSingle(DashComponent):
    """
    DatePickerSingle is a tailor made component designed for selecting a
    single day off of a calendar.  The DatePicker integrates well with the
    Python datetime module with the startDate and endDate being returned in a
    string format suitable for creating datetime objects.  This component is
    based off of Airbnb's react-dates react component which can be found here:
    https://github.com/airbnb/react-dates
    """

    _namespace = 'dash_core_components'
    _typename = 'DatePickerSingle'
    available_wildcard_properties = [

    ]
    id = ComponentProp('id', UNDEFINED, False)
    date = ComponentProp('date', UNDEFINED, False)
    min_date_allowed = ComponentProp('min_date_allowed', UNDEFINED, False)
    max_date_allowed = ComponentProp('max_date_allowed', UNDEFINED, False)
    initial_visible_month = ComponentProp('initial_visible_month', UNDEFINED, False)  # noqa: E501
    day_size = ComponentProp('day_size', 39, False)
    calendar_orientation = ComponentProp('calendar_orientation', "'horizontal'", False)  # noqa: E501
    is_RTL = ComponentProp('is_RTL', False, False)
    placeholder = ComponentProp('placeholder', UNDEFINED, False)
    reopen_calendar_on_clear = ComponentProp('reopen_calendar_on_clear', False, False)  # noqa: E501
    number_of_months_shown = ComponentProp('number_of_months_shown', 1, False)
    with_portal = ComponentProp('with_portal', False, False)
    with_full_screen_portal = ComponentProp('with_full_screen_portal', False, False)  # noqa: E501
    first_day_of_week = ComponentProp('first_day_of_week', "0", False)
    stay_open_on_select = ComponentProp('stay_open_on_select', False, False)
    show_outside_days = ComponentProp('show_outside_days', True, False)
    month_format = ComponentProp('month_format', UNDEFINED, False)
    display_format = ComponentProp('display_format', UNDEFINED, False)
    disabled = ComponentProp('disabled', False, False)
    clearable = ComponentProp('clearable', False, False)
    style = ComponentProp('style', UNDEFINED, False)
    className = ComponentProp('className', UNDEFINED, False)
    loading_state = ComponentProp('loading_state', UNDEFINED, False)

    def __init__(
            self,
            id=UNDEFINED,
            date=UNDEFINED,
            min_date_allowed=UNDEFINED,
            max_date_allowed=UNDEFINED,
            initial_visible_month=UNDEFINED,
            day_size=39,
            calendar_orientation="'horizontal'",
            is_RTL=False,
            placeholder=UNDEFINED,
            reopen_calendar_on_clear=False,
            number_of_months_shown=1,
            with_portal=False,
            with_full_screen_portal=False,
            first_day_of_week="0",
            stay_open_on_select=False,
            show_outside_days=True,
            month_format=UNDEFINED,
            display_format=UNDEFINED,
            disabled=False,
            clearable=False,
            style=UNDEFINED,
            className=UNDEFINED,
            loading_state=UNDEFINED,
    ):
        # type: (typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[typing.Any, Undefined], typing.Union[bool, Undefined], typing.Union[str, Undefined], typing.Union[bool, Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[bool, Undefined], typing.Union[bool, Undefined], typing.Union[typing.Any, Undefined], typing.Union[bool, Undefined], typing.Union[bool, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[bool, Undefined], typing.Union[bool, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict[str, typing.Union[bool, str]], Undefined]) -> None # noqa: E501
        """
        :param id:
        :param date: Specifies the starting date for the component, best
            practice is to pass value via datetime object
        :param min_date_allowed: Specifies the lowest selectable date for
            the component. Accepts datetime.datetime
            objects or strings in the format 'YYYY-MM-
            DD'
        :param max_date_allowed: Specifies the highest selectable date for
            the component. Accepts datetime.datetime
            objects or strings in the format 'YYYY-MM-
            DD'
        :param initial_visible_month: Specifies the month that is initially
            presented when the user opens the
            calendar. Accepts datetime.datetime
            objects or strings in the format
            'YYYY-MM-DD'
        :param day_size: Size of rendered calendar days, higher number
            means bigger day size and larger calendar
            overall(default=39)
        :param calendar_orientation: Orientation of calendar, either
            vertical or horizontal. Valid options
            are 'vertical' or
            'horizontal'.(Possible values:
            'vertical',
            'horizontal')(default='horizontal')
        :param is_RTL: Determines whether the calendar and days operate
            from left to right or from right to
            left(default=false)
        :param placeholder: Text that will be displayed in the input box of
            the date picker when no date is selected.
            Default value is 'Start Date'
        :param reopen_calendar_on_clear: If True, the calendar will
            automatically open when
            cleared(default=false)
        :param number_of_months_shown: Number of calendar months that are
            shown when calendar is
            opened(default=1)
        :param with_portal: If True, calendar will open in a screen overlay
            portal, not supported on vertical
            calendar(default=false)
        :param with_full_screen_portal: If True, calendar will open in a
            full screen overlay portal, will
            take precedent over 'withPortal' if
            both are set to True, not supported
            on vertical calendar(default=false)
        :param first_day_of_week: Specifies what day is the first day of
            the week, values must be from [0, ..., 6]
            with 0 denoting Sunday and 6 denoting
            Saturday(Possible values: 0, 1, 2, 3, 4,
            5, 6)(default=0)
        :param stay_open_on_select: If True the calendar will not close
            when the user has selected a value and
            will wait until the user clicks off the
            calendar(default=false)
        :param show_outside_days: If True the calendar will display days
            that rollover into the next
            month(default=true)
        :param month_format: Specifies the format that the month will be
            displayed in the calendar, valid formats are
            variations of "MM YY". For example: "MM YY"
            renders as '05 97' for May 1997 "MMMM, YYYY"
            renders as 'May, 1997' for May 1997 "MMM, YY"
            renders as 'Sep, 97' for September 1997
        :param display_format: Specifies the format that the selected dates
            will be displayed valid formats are
            variations of "MM YY DD". For example: "MM
            YY DD" renders as '05 10 97' for May 10th
            1997 "MMMM, YY" renders as 'May, 1997' for
            May 10th 1997 "M, D, YYYY" renders as '07,
            10, 1997' for September 10th 1997 "MMMM"
            renders as 'May' for May 10 1997
        :param disabled: If True, no dates can be selected.(default=false)
        :param clearable: Whether or not the dropdown is "clearable", that
            is, whether or not a small "x" appears on the
            right of the dropdown that removes the selected
            value.(default=false)
        :param style: CSS styles appended to wrapper div
        :param className: Appends a CSS class to the wrapper div component.
        :param loading_state: Object that holds the loading state object
            coming from dash-renderer
        """
        DashComponent.__init__(self, locals())
