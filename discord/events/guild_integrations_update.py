from .._dataclass import dataclass
from ..snowflake import Snowflake


@dataclass
class GuildIntegrationsUpdateEvent:
  guild_id: Snowflake
  """ID of the guild whose integrations where updated."""