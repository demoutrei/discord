from ..objects import Integration
from ..snowflake import Snowflake


class IntegrationUpdateEvent(Integration):
  guild_id: Snowflake
  """ID of the guild."""