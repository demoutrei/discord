from ..enums import ChannelType
from ..objects import GuildMember, Message, User
from ..snowflake import Snowflake
from ..utils import Optional


class MessageUpdateEvent(Message):
  channel_type: Optional[ChannelType]
  """The type of channel the message was sent in."""
  
  guild_id: Optional[Snowflake]
  """ID of the guild the message was sent in--unless it is an ephemeral message."""

  member: Optional[GuildMember]
  """Member properties for this emssage's author. Missing for ephemeral messages and messages from webhooks."""

  mentions: list[User]
  """Users specifically mentioned in the message."""