from .._dataclass import dataclass
from ..snowflake import Snowflake


@dataclass
class GuildSoundboardSoundDeleteEvent:
  guild_id: Snowflake
  """ID of the guild the sound was in."""
  
  sound_id: Snowflake
  """ID of the sound that was deleted."""