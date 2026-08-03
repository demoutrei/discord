from .._dataclass import dataclass
from ..snowflake import Snowflake


@dataclass
class GuildRoleDeleteEvent:
  guild_id: Snowflake
  """ID of the guild."""

  role_id: Snowflake
  """ID of the role."""