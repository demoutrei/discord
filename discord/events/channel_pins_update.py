from ..snowflake import Snowflake
from ..utils import ISO8601Timestamp, Nullable, Optional
from ._base import DispatchEvent


class ChannelPinsUpdateEvent(DispatchEvent):
  channel_id: Snowflake
  """ID of the channel."""
  
  guild_id: Optional[Snowflake]
  """ID of the guild."""

  last_pin_timestamp: Optional[Nullable[ISO8601Timestamp]]
  """Time at which the most recent pinned message was pinned."""