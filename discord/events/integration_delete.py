from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Optional


@dataclass
class IntegrationDeleteEvent:
  application_id: Snowflake
  """ID of the bot/OAuth2 application for this integration."""
  
  guild_id: Snowflake
  """ID of the guild."""
  
  id: Snowflake
  """Integration ID."""