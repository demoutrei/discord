from ..snowflake import Snowflake
from ..utils import Nullable, Optional
from ._base import DispatchEvent


class VoiceChannelStartTimeUpdateEvent(DispatchEvent):
  guild_id: Snowflake
  """The guild ID."""
  
  id: Snowflake
  """The channel ID."""

  voice_start_time: Optional[Nullable[int]]
  """Unix timestamp (in seconds) of when the voice session started."""