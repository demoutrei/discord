from .._dataclass import dataclass
from ..enums import (
  GuildScheduledEventRecurrenceRuleFrequency,
  GuildScheduledEventRecurrenceRuleMonth,
  GuildScheduledEventRecurrenceRuleNWeekday,
  GuildScheduledEventRecurrenceRuleWeekday
)
from ..utils import ISO8601Timestamp, Nullable


@dataclass
class GuildScheduledEventRecurrenceRule:
  """Discord's recurrence rule is a subset of the behaviors `defined in the iCalendar RFC <https://datatracker.ietf.org/doc/html/rfc5545>`_ and implemented by `Python's dateutil rrule <https://dateutil.readthedocs.io/en/stable/rrule.html>`_.

  .. attention::
      There are currently many limitations to this system. See "System limitations" below.
  """

  by_month: Nullable[list[GuildScheduledEventRecurrenceRuleMonth]]
  """Set of specific months to recur on."""

  by_month_day: Nullable[list[int]]
  """Set of specific dates within a month to recur on."""

  by_n_weekday: Nullable[list[GuildScheduledEventRecurrenceRuleNWeekday]]
  """List of specific days within a specific week (1-5) to recur on."""

  by_weekday: Nullable[list[GuildScheduledEventRecurrenceRuleWeekday]]
  """Set of specific days within a week for the event to recur on."""

  by_year_day: Nullable[list[int]]
  """Set of days within a year to recur on (1-364).

  .. note::
      Cannot be set externally currently.
  """

  count: Nullable[int]
  """The total amount of times that the event is allowed to recur before stopping.

  .. note::
      Cannot be set externally currently.
  """

  end: Nullable[ISO8601Timestamp]
  """Ending time of the recurrence interval.

  .. note::
      Cannot be set externally currently.
  """

  frequency: GuildScheduledEventRecurrenceRuleFrequency
  """How often the event occurs."""

  interval: int
  """The spacing between the events, defined by :attr:`~.frequency`. For example, :attr:`~.frequency` of :attr:`~discord.enums.GuildScheduledEventRecurrenceRuleFrequency.WEEKLY` and an interval of :attr:`~.interval` of ``2`` would be "every-other-week"."""

  start: ISO8601Timestamp
  """Starting time of the recurrence interval."""