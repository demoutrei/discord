from ..snowflake import Snowflake
from ..utils import Nullable
from ._base import DispatchEvent


class VoiceChannelStatusUpdateEvent(DispatchEvent):
  guild_id: Snowflake
  """The guild ID."""
  
  id: Snowflake
  """The channel ID."""

  status: Nullable[str]
  """The new voice channel status."""