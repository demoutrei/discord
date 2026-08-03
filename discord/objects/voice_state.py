from .._dataclass import dataclass
from ..utils import ISO8601Timestamp, Nullable, Optional
from ..snowflake import Snowflake
from .guild_member import GuildMember


@dataclass
class VoiceState:
  channel_id: Nullable[Snowflake]
  """The channel ID this user is connected to."""
  
  deaf: bool
  """Whether this user is deafened by the server."""
  
  guild_id: Optional[Snowflake]
  """The guild ID this voice state is for."""

  member: Optional[GuildMember]
  """The guild member this voice state is for."""

  mute: bool
  """Whether this user is muted by the server."""

  request_to_speak_timestamp: Optional[ISO8601Timestamp]
  """The time at which the user requested to speak."""

  self_deaf: bool
  """Whether this user is locally deafened."""

  self_mute: bool
  """Whether this user is locally muted."""

  self_stream: Optional[bool]
  """Whether this user is streaming using "Go Live"."""

  self_video: bool
  """Whether this user's camera is enabled."""

  session_id: str
  """The session Id for this voice state."""

  suppress: bool
  """Whether this user's permission to speak is denied."""

  user_id: Snowflake
  """The user ID this voice state is for."""