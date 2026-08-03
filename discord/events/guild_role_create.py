from .._dataclass import dataclass
from ..objects import Role
from ..snowflake import Snowflake


@dataclass
class GuildRoleCreateEvent:
  guild_id: Snowflake
  """ID of the guild."""

  role: Role
  """Role that was created."""