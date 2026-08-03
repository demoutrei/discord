from .._dataclass import dataclass
from ..objects import Activity, ClientStatus, User
from ..snowflake import Snowflake


@dataclass
class PresenceUpdateEvent:
  activities: list[Activity]
  """User's current activities."""

  client_status: ClientStatus
  """User's platform-dependent status."""
  
  guild_id: Snowflake
  """ID of the guild."""

  status: str
  """Either "idle", "dnd", "online", or "offline"."""
  
  user: User
  """User whose presence is being updated."""