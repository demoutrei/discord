from .._dataclass import dataclass
from ..objects import Emoji
from ..snowflake import Snowflake
from ..utils import Optional


@dataclass
class MessageReactionRemoveEmojiEvent:
  channel_id: Snowflake
  """ID of the channel."""

  emoji: Emoji
  """Emoji that was removed."""

  guild_id: Optional[Snowflake]
  """ID of the guild."""

  message_id: Snowflake
  """ID of the message."""