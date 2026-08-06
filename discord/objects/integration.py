from .._dataclass import dataclass
from ..enums import IntegrationExpireBehavior
from ..snowflake import Snowflake
from ..utils import ISO8601Timestamp, Optional
from .integration_account import IntegrationAccount
from .integration_application import IntegrationApplication
from .user import User


@dataclass
class Integration:  
  account: IntegrationAccount
  """Integration account information."""
  
  application: Optional[IntegrationApplication]
  """The bot/OAuth2 application for discord integrations."""
  
  enable_emoticons: Optional[Snowflake]
  """Whether emoticons should be synced for this integration (twitch only currently).

  .. note::
      Not provided for discord bot integrations.
  """
  
  enabled: bool
  """Whether the integration is enabled."""

  expire_behavior: Optional[IntegrationExpireBehavior]
  """The behavior of expiring subscribers.

  .. note::
      Not provided for discord bot integrations.
  """

  expire_grace_period: Optional[int]
  """The grace period (in days) before expiring subscribers.

  .. note::
      Not provided for discord bot integrations.
  """
  
  id: Snowflake
  """Integration ID."""

  name: str
  """Integration name."""

  revoked: Optional[bool]
  """Whether the integration has been revoked.

  .. note::
      Not provided for discord bot integrations.
  """

  role_id: Optional[Snowflake]
  """ID that this integration uses for "subscribers".
  
  .. note::
      Not provided for discord bot integrations.
  """

  subscriber_count: Optional[int]
  """How many subscribers this integration has.

  .. note::
      Not provided for discord bot integrations.
  """

  scopes: list[str]
  """The scopes the application has been authorized for."""

  synced_at: Optional[ISO8601Timestamp]
  """When this integration was last synced.

  .. note::
      Not provided for discord bot integrations.
  """

  syncing: Optional[bool]
  """Whether the integration is syncing.

  .. note::
      Not provided for discord bot integrations.
  """

  type: str
  """Integration type (twitch, youtube, discord, or guild_subscription)."""

  user: Optional[User]
  """User for this integration.

  .. attention::
      Some older integrations may not have an attached user.
  """