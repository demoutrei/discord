from .._dataclass import dataclass
from ..enums import WebhookType
from ..snowflake import Snowflake
from ..utils import Nullable, Optional
from .channel import Channel
from .guild import Guild
from .user import User


@dataclass
class Webhook:
  application_id: Nullable[Snowflake]
  """The bot/OAuth2 application that created this webhook."""
  
  avatar: Nullable[str]
  """The default user avatar hash of the webhook."""
  
  channel_id: Nullable[Snowflake]
  """The channel ID this webhook is for, if any."""
  
  guild_id: Optional[Nullable[Snowflake]]
  """The guild ID this webhook is for, if any."""
  
  id: Snowflake
  """The ID of the webhook."""

  name: Nullable[str]
  """The default name of the webhook."""

  source_channel: Optional[Channel]
  """The channel that this webhook is following (returned for :attr:`~discord.enums.WebhookType.CHANNEL_FOLLOWER` webhooks).

  .. note::
      Will be absent if the webhook creator has since lost access to the guild where the followed channel resides.
  """

  source_guild: Optional[Guild]
  """The guild of the channel that this webhook is following (returned for :attr:`~discord.enums.WebhookType.CHANNEL_FOLLOWER` webhooks).

  .. note::
      Will be absent if the webhook creator has since lost access to the guild where the followed channel resides.
  """

  token: Optional[str]
  """The secure token of the webhook (returned for :attr:`~discord.enums.WebhookType.INCOMING` webhooks)."""

  type: WebhookType
  """The type of the webhook."""

  url: Optional[str]
  """The URL used for executing the webhook (returned by the webhooks OAuth2 flow)."""

  user: Optional[User]
  """The user this webhook was created by (not returned when getting a webhook with its token)."""