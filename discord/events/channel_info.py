from ..snowflake import Snowflake
from ..objects import ChannelInfoChannel
from ._base import DispatchEvent


class ChannelInfoEvent(DispatchEvent):
  channels: list[ChannelInfoChannel]
  """Ephemeral data for channels in the guild."""
  
  guild_id: Snowflake
  """The guild ID."""