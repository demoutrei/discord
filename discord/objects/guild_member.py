from .._dataclass import dataclass
from ..flags import GuildMemberFlags, PermissionFlags
from ..snowflake import Snowflake
from ..utils import ISO8601Timestamp, Nullable, Optional
from .avatar_decoration_data import AvatarDecorationData
from .collectible import Collectible
from .user import User


@dataclass
class GuildMember:
  """
  .. note::
      The field :attr:`~.user` won't be included in the member object attached to ``MESSAGE_CREATE`` and ``MESSAGE_UPDATE`` gateway events.

  .. note::
      In ``GUILD_`` events, :attr:`~.pending` will always be included as ``True`` or ``False``. In non-``GUILD_`` events which can only be triggered by non-:attr:`~.pending` users, :attr:`~.pending` wlil not be included.

  .. note::
      Member objects retrieved from ``VOICE_STATE_UPDATE`` events will have :attr:`~.joined_at` set as ``None`` if the member was invited as a guest.
  """

  avatar: Optional[Nullable[str]]
  """The member's guild avatar hash."""

  avatar_decoration_data: Optional[Nullable[AvatarDecorationData]]
  """Data for the member's guild avatar decoration."""

  banner: Optional[Nullable[str]]
  """The member's guild banner hash."""

  collectibles: Optional[Nullable[Collectible]]
  """Data for the member's collectibles."""

  communication_disabled_until: Optional[Nullable[ISO8601Timestamp]]
  """When the user's timeout will expire and the user will be able to communicate in teh guild again, null or a time in the past if the user is not timed out."""

  deaf: bool
  """Whether the user is deafened in voice channels."""

  flags: GuildMemberFlags
  """Guild member flags represented as a bit set, defaults to ``0``."""

  joined_at: Optional[ISO8601Timestamp]
  """When the user joined the guild."""

  mute: bool
  """Whether the user is muted in voice channels."""

  nick: Optional[Nullable[str]]
  """This user's guild nickname."""

  pending: Optional[bool]
  """Whether the user has not yet passed the guild's Membership Screening requirements."""

  permissions: Optional[PermissionFlags]
  """Total permissions of the member in the channel, including overwrites, returned when in the interaction object."""

  premium_since: Optional[Nullable[ISO8601Timestamp]]
  """When the user started boosting the guild."""

  roles: list[Snowflake]
  """Array of role object IDs."""

  user: Optional[User]
  """The user this guild member represents."""