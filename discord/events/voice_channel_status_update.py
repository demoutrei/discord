from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Nullable


@dataclass
class VoiceChannelStatusUpdateEvent:
  guild_id: Snowflake
  """The guild ID."""
  
  id: Snowflake
  """The channel ID."""

  status: Nullable[str]
  """The new voice channel status."""