from .._dataclass import dataclass
from ..enums import ReactionType
from ..objects import Emoji, GuildMember
from ..snowflake import Snowflake
from ..utils import Optional


@dataclass
class MessageReactionAddEvent:
  burst: bool
  """``True`` if this is a super-reaction."""

  burst_colors: Optional[list[str]]
  """Colors used for super-reaction animation in "#rrggbb" format."""
  
  channel_id: Snowflake
  """ID of the channel."""

  emoji: Emoji
  """Emoji used to react."""

  guild_id: Optional[Snowflake]
  """ID of the guild."""

  member: Optional[GuildMember]
  """Member who reacted if this happened in a guild."""

  message_author_id: Optional[Snowflake]
  """ID of the user who authored the message which was reacted to."""

  message_id: Snowflake
  """ID of the message."""

  type: ReactionType
  """The type of reaction."""
  
  user_id: Snowflake
  """ID of the user."""