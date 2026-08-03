from .._dataclass import dataclass
from ..objects import SoundboardSound
from ..snowflake import Snowflake


@dataclass
class SoundboardSoundsEvent:
  guild_id: Snowflake
  """ID of the guild."""
  
  soundboard_sounds: list[SoundboardSound]
  """The guild's soundboard sounds."""