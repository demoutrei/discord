from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..objects import ChannelInfoChannel


@dataclass
class ChannelInfoEvent:
  channels: list[ChannelInfoChannel]
  """Ephemeral data for channels in the guild."""
  
  guild_id: Snowflake
  """The guild ID."""