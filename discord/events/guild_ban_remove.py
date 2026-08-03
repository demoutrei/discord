from .._dataclass import dataclass
from ..objects import User
from ..snowflake import Snowflake


@dataclass
class GuildBanRemoveEvent:
  guild_id: Snowflake
  """ID of the guild."""

  user: User
  """User who was unbanned."""