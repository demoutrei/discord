from .._dataclass import dataclass
from ..enums import InviteTargetType
from ..objects import Application, User
from ..snowflake import Snowflake
from ..utils import ISO8601Timestamp, Nullable, Optional


@dataclass
class InviteCreateEvent:
  channel_id: Snowflake
  """Channel the invite is for."""

  code: str
  """Unique invite code."""

  created_at: ISO8601Timestamp
  """Time at which the invite was created."""

  expires_at: Nullable[ISO8601Timestamp]
  """The expiration date of this invite."""

  guild_id: Optional[Snowflake]
  """Guild of the invite."""

  inviter: Optional[User]
  """User that created the invite."""

  max_age: int
  """How long the invite is valid for (in seconds)."""

  max_uses: int
  """Maximum number of times the invite can be used."""

  role_ids: Optional[list[Snowflake]]
  """The role ID(s) for roles in the guild given to the users that accept this invite."""

  target_application: Optional[Application]
  """Embedded application to open for this voice channel embedded application invite."""

  target_type: Optional[InviteTargetType]
  """Type of target for this voice channel invite."""

  target_user: Optional[User]
  """User whose stream to display for this voice channel stream invite."""

  temporary: bool
  """Whether or not the invite is temporary (invited users will be kicked on disconnect unless they're assigned a role)."""

  uses: int
  """How many times the invite has been used (always will be 0)."""