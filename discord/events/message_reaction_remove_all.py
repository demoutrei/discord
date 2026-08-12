from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Optional


@dataclass
class MessageReactionRemoveAllEvent:
  channel_id: Snowflake
  """ID of the channel."""

  guild_id: Optional[Snowflake]
  """ID of the guild."""

  message_id: Snowflake
  """ID of the message."""