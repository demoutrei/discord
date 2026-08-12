from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Optional
from .attachment import Attachment
from .channel import Channel
from .member import Member
from .message import Message
from .role import Role
from .user import User


@dataclass
class ResolvedData:
  """.. tip::
      If data for a Member is included, data for its corresponding User will also be included.
  """

  attachments: Optional[dict[Snowflake, Attachment]]
  """IDs and attachment objects."""

  channels: Optional[dict[Snowflake, Channel]]
  """IDs and partial Channel objects.

  .. note::
      Partial :class:`~discord.objects.Channel` objects only have :attr:`~discord.objects.Channel.id`, :attr:`~discord.objects.Channel.name`, :attr:`~discord.objects.Channel.type`, :attr:`~discord.objects.Channel.permissions`, :attr:`~discord.objects.Channel.app_permissions`, :attr:`~discord.objects.Channel.last_message_id`, :attr:`~discord.objects.Channel.last_pin_timestamp`, :attr:`~discord.objects.Channel.nsfw`, :attr:`~discord.objects.Channel.parent_id`, :attr:`~discord.objects.Channel.guild_id`, :attr:`~discord.objects.Channel.flags`, :attr:`~discord.objects.Channel.rate_limit_per_user`, :attr:`~discord.objects.Channel.topic`, and :attr:`~discord.objects.Channel.position` fields. Threads will also have the :attr:`~discord.objects.Channel.thread_metadata` field.
  """

  members: Optional[dict[Snowflake, Member]]
  """IDs and partial Member objects.

  .. note::
      Partial :class:`~discord.objects.Member` objects are missing :attr:`~discord.objects.Member.user`, :attr:`~discord.objects.Member.dead`, and :attr:`~discord.objects.Member.mute` fields.
  """

  messages: Optional[dict[Snowflake, Message]]
  """IDs and partial Message objects."""

  roles: Optional[dict[Snowflake, Role]]
  """IDs and Role objects."""

  users: Optional[dict[Snowflake, User]]
  """IDs and User objects."""