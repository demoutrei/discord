from ..enums import ApplicationEventWebhookStatus, ApplicationIntegrationType, WebhookEventType
from ..flags import ApplicationFlag
from ..snowflake import Snowflake
from ..utils import Nullable, Optional
from ._base import BaseObject
from .application_integration_type_configuration import ApplicationIntegrationTypeConfiguration
from .guild import Guild
from .install_params import InstallParams
from .team import Team
from .user import User


class Application(BaseObject):
  approximate_guild_count: Optional[int]
  """Approximate count of guilds the app has been added to"""

  approximate_user_authorization_count: Optional[int]
  """Approximate count of users that have OAuth2 authorization for the app"""

  approximate_user_install_count: Optional[int]
  """Approximate count of users that have installed the app (authorized with ``application.commands`` as a scope)"""
  
  bot: Optional[User]
  """Partial user object for the bot user associated with the app"""
  
  bot_public: bool
  """When ``False``, only the app owner can add the app to the guilds"""

  bot_require_code_grant: bool
  """When ``True``, the app's bot will only join upon completion of the full OAuth2 code grant flow"""
  
  cover_image: Optional[str]
  """App's default rich presence invite cover image hash"""

  custom_install_url: Optional[str]
  """Default custom authorization URL for the app, if enabled"""
  
  description: str
  """Description of the app"""

  event_webhook_status: Optional[ApplicationEventWebhookStatus]
  """If webhook events are enabled for the app. ``1`` (default) means disabled, ``2`` means enabled, ``3`` means disabled by Discord"""

  event_webhooks_types: Optional[list[WebhookEventType]]
  r"""List of :class:`~discord.enums.WebhookEventType`\s the app subscribes to"""

  event_webhooks_url: Optional[Nullable[str]]
  """Event webhooks URL for the app to receive webhook events"""

  flags: Optional[ApplicationFlag]
  """App's public flags"""
  
  guild: Optional[Guild]
  """Partial object of the associated guild"""
  
  guild_id: Optional[Snowflake]
  """Guild associated with the app. For example, a developer support server."""
  
  icon: Nullable[str]
  """Icon hash of the app"""
  
  id: Snowflake
  """ID of the app"""

  install_params: Optional[InstallParams]
  """Settings for the app's default in-app authorization link, if enabled"""

  integration_types_config: Optional[dict[ApplicationIntegrationType, ApplicationIntegrationTypeConfiguration]]
  """Default scopes and permissions for each supported installation context"""

  interactions_endpoint_url: Optional[Nullable[str]]
  """Interactions endpoint URL for the app"""

  name: str
  """Name of the app"""

  owner: Optional[User]
  """Partial user object for the owner of the app"""

  primary_sku_id: Optional[Snowflake]
  """If this app is a game sold on Discord, this field will be the id of the "Game SKU" that is created, if exists"""

  privacy_policy_url: Optional[str]
  """URL of the app's Privacy Policy"""

  redirect_uris: Optional[list[str]]
  """Array of redirect URIs for the app"""

  role_connections_verification_url: Optional[Nullable[str]]
  """Role connections verification URL for the app"""

  rpc_origins: Optional[list[str]]
  """List of RPC origin URLs, if RPC is enabled"""

  slug: Optional[str]
  """If this app is a game sold on Discord, this field will be the URL slug that links to the store page"""

  tags: Optional[list[str]]
  """List of tags describing the content and functionality of the app. Max of 5 tags."""

  team: Nullable[Team]
  """If the app belongs to a team, this will be a list of the members of that team"""

  terms_of_service_url: Optional[str]
  """URL of the app's Terms of Service"""

  verify_key: str
  """Hex encoded key for verification in interactions and the Game SDK's GetTicket"""