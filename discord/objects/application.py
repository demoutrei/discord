from .._dataclass import dataclass
from ..enums import ApplicationEventWebhookStatus, ApplicationIntegrationType, WebhookEventType
from ..flags import ApplicationFlags
from ..snowflake import Snowflake
from ..types import MISSING, Nullable, Optional
from .application_integration_type_configuration import ApplicationIntegrationTypeConfiguration
from .guild import Guild
from .install_params import InstallParams
from .team import Team
from .user import User


@dataclass
class Application:
  @property
  def approximate_guild_count(self) -> Optional[int]:
    """Approximate count of guilds the app has been added to."""
    return self.__dict__.get("approximate_guild_count", MISSING)

  @property
  def approximate_user_authorization_count(self) -> Optional[int]:
    """Approximate count of users that have OAuth2 authorization for the app."""
    return self.__dict__.get("approximate_user_authorization_count", MISSING)

  @property
  def approximate_user_install_count(self) -> Optional[int]:
    """Approximate count of users that have installed the app (authorized with ``application.commands`` as a scope)."""
    return self.__dict__.get("approximate_user_install_count", MISSING)
  
  @property
  def bot(self) -> Optional[User]:
    """Partial user object for the bot user associated with the app."""
    if (data := self.__dict__.get("bot", MISSING)) is MISSING: return data
    return User(**data)
  
  @property
  def bot_public(self) -> bool:
    """When ``False``, only the app owner can add the app to the guilds."""
    return self.__dict__["bot_public"]

  @property
  def bot_require_code_grant(self) -> bool:
    """When ``True``, the app's bot will only join upon completion of the full OAuth2 code grant flow."""
    return self.__dict__["bot_require_code_grant"]
  
  @property
  def cover_image(self) -> Optional[str]:
    """App's default rich presence invite cover image hash."""
    return self.__dict__.get("cover_image", MISSING)

  @property
  def custom_install_url(self) -> Optional[str]:
    """Default custom authorization URL for the app, if enabled."""
    return self.__dict__.get("custom_install_url", MISSING)
  
  @property
  def description(self) -> str:
    """Description of the app."""
    return self.__dict__["description"]

  @property
  def event_webhook_status(self) -> Optional[ApplicationEventWebhookStatus]:
    """If webhook events are enabled for the app. ``1`` (default) means disabled, ``2`` means enabled, ``3`` means disabled by Discord."""
    if (data := self.__dict__.get("event_webhook_status", MISSING)) is MISSING: return data
    return ApplicationEventWebhookStatus(data)

  @property
  def event_webhooks_types(self) -> Optional[list[WebhookEventType]]:
    r"""List of :class:`~discord.enums.WebhookEventType`\s the app subscribes to."""
    if (data := self.__dict__.get("event_webhooks_types", MISSING)) in (MISSING, None): return data
    return WebhookEventType(data)

  @property
  def event_webhooks_url(self) -> Optional[Nullable[str]]:
    """Event webhooks URL for the app to receive webhook events."""
    return self.__dict__.get("event_webhooks_url", MISSING)

  @property
  def flags(self) -> Optional[ApplicationFlags]:
    """App's public flags."""
    if (data := self.__dict__.get("flags", MISSING)) is MISSING: return data
    return ApplicationFlags(data)
  
  @property
  def guild(self) -> Optional[Guild]:
    """Partial object of the associated guild."""
    if (data := self.__dict__.get("guild", MISSING)) is MISSING: return data
    return Guild(**data)
  
  @property
  def guild_id(self) -> Optional[Snowflake]:
    """Guild associated with the app. For example, a developer support server."""
    if (data := self.__dict__.get("guild_id", MISSING)) is MISSING: return data
    return Snowflake(data)
  
  @property
  def icon(self) -> Nullable[str]:
    """Icon hash of the app."""
    return self.__dict__["icon"]
  
  @property
  def id(self) -> Snowflake:
    """ID of the app."""
    return Snowflake(self.__dict__["id"])

  @property
  def install_params(self) -> Optional[InstallParams]:
    """Settings for the app's default in-app authorization link, if enabled."""
    if (data := self.__dict__.get("install_params", MISSING)) is MISSING: return data
    return InstallParams(**data)

  @property
  def integration_types_config(self) -> Optional[dict[ApplicationIntegrationType, ApplicationIntegrationTypeConfiguration]]:
    """Default scopes and permissions for each supported installation context."""
    if (data := self.__dict__.get("integration_types_config", MISSING)) is MISSING: return data
    return {ApplicationIntegrationType(key): ApplicationIntegrationTypeConfiguration(**value) for key, value in data.items()}

  @property
  def interactions_endpoint_url(self) -> Optional[Nullable[str]]:
    """Interactions endpoint URL for the app."""
    return self.__dict__.get("interactions_endpoint_url", MISSING)

  @property
  def name(self) -> str:
    """Name of the app."""
    return self.__dict__["name"]

  @property
  def owner(self) -> Optional[User]:
    """Partial user object for the owner of the app."""
    if (data := self.__dict__.get("owner", MISSING)) is MISSING: return data
    return User(**data)

  @property
  def primary_sku_id(self) -> Optional[Snowflake]:
    """If this app is a game sold on Discord, this field will be the id of the "Game SKU" that is created, if exists."""
    if (data := self.__dict__.get("primary_sku_id", MISSING)) is MISSING: return data
    return Snowflake(data)

  @property
  def privacy_policy_url(self) -> Optional[str]:
    """URL of the app's Privacy Policy."""
    return self.__dict__.get("privacy_policy_url", MISSING)

  @property
  def redirect_uris(self) -> Optional[list[str]]:
    """Array of redirect URIs for the app."""
    return self.__dict__.get("redirect_uris", MISSING)

  @property
  def role_connections_verification_url(self) -> Optional[Nullable[str]]:
    """Role connections verification URL for the app."""
    return self.__dict__.get("role_connections_verification_url", MISSING)

  @property
  def rpc_origins(self) -> Optional[list[str]]:
    """List of RPC origin URLs, if RPC is enabled."""
    return self.__dict__.get("rpc_origins", MISSING)

  @property
  def slug(self) -> Optional[str]:
    """If this app is a game sold on Discord, this field will be the URL slug that links to the store page."""
    return self.__dict__.get("slug", MISSING)

  @property
  def tags(self) -> Optional[list[str]]:
    """List of tags describing the content and functionality of the app. Max of 5 tags."""
    return self.__dict__.get("tags", MISSING)

  @property
  def team(self) -> Nullable[Team]:
    """If the app belongs to a team, this will be a list of the members of that team."""
    if (data := self.__dict__["team"]) is None: return data
    return Team(**data)

  @property
  def terms_of_service_url(self) -> Optional[str]:
    """URL of the app's Terms of Service."""
    return self.__dict__.get("terms_of_service_url", MISSING)

  @property
  def verify_key(self) -> str:
    """Hex encoded key for verification in interactions and the Game SDK's GetTicket."""
    return self.__dict__["verify_key"]