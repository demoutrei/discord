from .._dataclass import dataclass
from ..objects import Emoji
from ..snowflake import Snowflake


@dataclass
class GuildEmojisUpdateEvent:
  emojis: list[Emoji]
  """Array of emojis."""
  
  guild_id: Snowflake
  """ID of the guild."""