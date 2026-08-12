from .._dataclass import dataclass
from ..enums import ReactionType
from ..objects import Emoji
from ..snowflake import Snowflake
from ..utils import Optional


@dataclass
class MessageReactionRemoveEvent:
  burst: bool
  """``True`` if this was a super-reaction."""
  
  channel_id: Snowflake
  """ID of the channel."""

  emoji: Emoji
  """Emoji used to react."""

  guild_id: Optional[Snowflake]
  """ID of the guild."""

  message_id: Snowflake
  """ID of the message."""

  type: ReactionType
  """The type of reaction."""
  
  user_id: Snowflake
  """ID of the user."""