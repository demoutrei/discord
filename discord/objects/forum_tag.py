from ..snowflake import Snowflake
from ..utils import Nullable
from ._base import BaseObject


class ForumTag(BaseObject):
  """Represents a tag that is able to be applied to a thread in a :attr:`~discord.enums.ChannelType.GUILD_FORUM` or :attr:`~discord.enums.ChannelType.GUILD_MEDIA` channel.

  .. important::
      When updating a :attr:`~discord.enums.ChannelType.GUILD_FORUM` or a :attr:`~discord.enums.ChannelType.GUILD_MEDIA` channel, tag objects in :attr:`~discord.objects.Channel.available_tags` only require the :attr:`~.name` field.
  """

  emoji_id: Nullable[Snowflake]
  """The ID of a guild's custom emoji"""

  emoji_name: Nullable[str]
  """The unicode character of the emoji"""

  id: Snowflake
  "The ID of the tag"

  moderated: bool
  """Whether this tag can only be added to or removed from threads by a member with the :attr:`~discord.flags.PermissionFlag.MANAGE_THREADS` permission"""

  name: str
  """The name of the tag (0-20 characters)"""
