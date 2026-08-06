from ..objects import Integration
from ..snowflake import Snowflake


class IntegrationCreateEvent(Integration):
  guild_id: Snowflake
  """ID of the guild."""