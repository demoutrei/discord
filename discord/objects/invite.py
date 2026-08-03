from .._dataclass import dataclass
from ..enums import InviteTargetType, InviteType
from ..flags import GuildInviteFlags
from ..utils import ISO8601Timestamp, Nullable, Optional
from .application import Application
from .channel import Channel
from .guild import Guild
from .guild_scheduled_event import GuildScheduledEvent
from .role import Role
from .user import User


@dataclass
class Invite:
  """Represents a code that when used, adds a user to a guild or group DM channel."""

  approximate_member_count: Optional[int]
  """Approximate count of total members, returned from the ``GET /invites/<code>`` endpoint when ``with_counts`` is ``True``."""

  approximate_presence_count: Optional[int]
  """Approximate count of online members, returned from the ``GET /invites/<code>`` endpoint when ``with_counts`` is ``True``."""

  channel: Nullable[Channel]
  """The channel this invite is for."""

  code: str
  """The invite code (unique ID)."""

  expires_at: Nullable[ISO8601Timestamp]
  """The expiration date of this invite."""

  flags: Optional[GuildInviteFlags]
  """Guild invite flags for guild invites."""

  guild: Optional[Guild]
  """The guild this invite is for."""

  guild_scheduled_event: Optional[GuildScheduledEvent]
  """Guild scheduled event data, only included if ``guild_scheduled_event_id`` contains a valid guild scheduled event ID."""

  inviter: Optional[User]
  """The user who created the invite."""

  roles: list[Role]
  """The roles assigned to the user upon accepting the invite.

  .. important::
      This is a partial role object that only contains :attr:`~discord.objects.Role.id`, :attr:`~discord.objects.Role.name`, :attr:`~discord.objects.Role.position`, :attr:`~discord.objects.Role.color`, :attr:`~discord.objects.Role.colors`, :attr:`~discord.objects.Role.icon`, and :attr:`~discord.objects.Role.unicode_emoji`.
  """

  target_application: Optional[Application]
  """The embedded application to open for this voice channel embedded application invite."""

  target_type: Optional[InviteTargetType]
  """The type of target for this voice channel invite."""

  target_user: Optional[User]
  """The user whose stream to display for this voice channel stream invite."""

  type: InviteType
  """The type of invite."""