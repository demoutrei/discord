from .._dataclass import dataclass
from ..enums import GuildScheduledEventRecurrenceRuleWeekday


@dataclass
class GuildScheduledEventRecurrenceRuleNWeekday:
  day: GuildScheduledEventRecurrenceRuleWeekday
  """The day within the week to reoccur on."""
  
  n: int
  """The week to reoccur on. 1-5"""