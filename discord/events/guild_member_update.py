from .._dataclass import dataclass
from ..objects import AvatarDecorationData, Collectible, User
from ..snowflake import Snowflake
from ..utils import ISO8601Timestamp, Nullable, Optional


@dataclass
class GuildMemberUpdateEvent:
  avatar: Nullable[str]
  """Member's guild avatar hash."""

  avatar_decoration_data: Optional[Nullable[AvatarDecorationData]]
  """Data for the member's guild avatar decoration."""

  banner: Nullable[str]
  """Member's guild banner hash."""

  collectibles: Optional[Nullable[Collectible]]
  """Data for the member's collectibles."""
  
  communication_disabled_until: Optional[Nullable[ISO8601Timestamp]]
  """When the user's timeout will expire and the user will be able to communicate in the guild again, null or a time in the past if the user is not timed out."""
  
  deaf: Optional[bool]
  """Whether the user is deafened in voice channels."""
  
  guild_id: Snowflake
  """ID of the guild."""

  joined_at: Nullable[ISO8601Timestamp]
  """When the user joined the guild."""

  mute: Optional[bool]
  """Whether the user is muted in voice channels."""

  nick: Optional[Nullable[str]]
  """Nickname of the user in the guild."""

  pending: Optional[bool]
  """Whether the user has not yet passed the guild's Membership Screening requirements."""

  premium_since: Optional[Nullable[ISO8601Timestamp]]
  """When the user starting boosting the guild."""

  roles: list[Snowflake]
  """User role IDs."""

  user: User
  """User."""