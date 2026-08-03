from .._dataclass import dataclass
from ..snowflake import Snowflake


@dataclass
class GuildScheduledEventUserRemoveEvent:
  guild_id: Snowflake
  """ID of the guild."""
  
  guild_scheduled_event_id: Snowflake
  """ID of the guild scheduled event."""

  user_id: Snowflake
  """ID of the user."""