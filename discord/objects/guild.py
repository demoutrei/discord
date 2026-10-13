from .._dataclass import dataclass
from ..enums import DefaultMessageNotificationLevel, ExplicitContentFilterLevel, GuildAgeRestrictionLevel, GuildFeature, Locale, MFALevel, PremiumTier, VerificationLevel
from ..flags import PermissionFlags, SystemChannelFlags
from ..snowflake import Snowflake
from ..types import MISSING, Nullable, Optional
from .emoji import Emoji
from .incidents_data import IncidentsData
from .role import Role
from .sticker import Sticker
from .welcome_screen import WelcomeScreen


@dataclass
class Guild:
  """Represents an isolated collection of users and channels, and are often referred to as "servers" in the UI."""

  @property
  def afk_channel_id(self) -> Nullable[Snowflake]:
    """ID of AFK channel."""
    if (data := self.__dict__["afk_channel_id"]) is None: return data
    return Snowflake(data)

  @property
  def afk_timeout(self) -> int:
    """AFK timeout in seconds."""
    return self.__dict__["afk_timeout"]

  @property
  def application_id(self) -> Nullable[Snowflake]:
    """Application ID of the guild creator if it is bot-created."""
    if (data := self.__dict__["application_id"]) is None: return data
    return Snowflake(data)

  @property
  def approximate_member_count(self) -> Optional[int]:
    """Approximate number of members in this guild, retunred from the ``GET /guilds/<id>`` and ``/users/@me/guilds`` endpoints when ``with_counts`` is ``True``."""
    return self.__dict__.get("approximate_member_count", MISSING)

  @property
  def approximate_presence_count(self) -> Optional[int]:
    """Approximate number of non-offline members in this guild, returned from the ``GET /guilds/<id>`` and ``/users/@me/guilds`` endpoints when ``with_counts`` is ``True``."""
    return self.__dict__.get("approximate_presence_count", MISSING)

  @property
  def banner(self) -> Nullable[str]:
    """Banner hash."""
    return self.__dict__["banner"]

  @property
  def default_message_notifications(self) -> DefaultMessageNotificationLevel:
    """Default message notifications level."""
    return DefaultMessageNotificationLevel(self.__dict__["default_message_notifications"])

  @property
  def description(self) -> Nullable[str]:
    """The description of a guild."""
    return self.__dict__["description"]

  @property
  def discovery_splash(self) -> Nullable[str]:
    """Discovery splash hash; only present for guilds with the "DISCOVERABLE" feature."""
    return self.__dict__["discovery_splash"]

  @property
  def emojis(self) -> list[Emoji]:
    """Custom guild emojis."""
    return [Emoji(**data) for data in self.__dict__["emojis"]]

  @property
  def explicit_content_filter(self) -> ExplicitContentFilterLevel:
    """Explicit content filter level."""
    return ExplicitContentFilterLevel(self.__dict__["explicit_content_filter"])

  @property
  def features(self) -> list[GuildFeature]:
    """Enabled guild feature."""
    return [GuildFeature(data) for data in self.__dict__["features"]]

  @property
  def icon(self) -> Nullable[str]:
    """Icon hash."""
    return self.__dict__["icon"]

  @property
  def icon_hash(self) -> Optional[Nullable[str]]:
    """Icon hash, returned when in the template object"""
    return self.__dict__.get("icon_hash", MISSING)

  @property
  def id(self) -> Snowflake:
    """Guild ID."""
    return Snowflake(self.__dict__["id"])

  @property
  def incidents_data(self) -> Nullable[IncidentsData]:
    """The incidents data for this guild."""
    if (data := self.__dict__["incidents_data"]) is None: return data
    return IncidentsData(**data)

  @property
  def max_members(self) -> Optional[int]:
    """The maximum number of members for the guild."""
    return self.__dict__.get("max_members", MISSING)

  @property
  def max_presences(self) -> Optional[Nullable[int]]:
    """The maximum number of presences for the guild (``None`` is always returned, arapt from the largest of guilds)."""
    return self.__dict__.get("max_presences", MISSING)

  @property
  def max_stage_video_channel_users(self) -> Optional[int]:
    """The maximum amount of users in a stage video channel."""
    return self.__dict__.get("max_stage_video_channel_users", MISSING)

  @property
  def max_video_channel_users(self) -> Optional[int]:
    """The maximum amount of users in a video channel."""
    return self.__dict__.get("max_video_channel_users", MISSING)

  @property
  def mfa_level(self) -> MFALevel:
    """Required MFA level for the guild."""
    return MFALevel(self.__dict__["mfa_level"])

  @property
  def name(self) -> str:
    """Guild name (2-100 characters, excluding trailing and leading whitespace)."""
    return self.__dict__["name"]

  @property
  def nsfw_level(self) -> GuildAgeRestrictionLevel:
    """Guild age-restriction level."""
    return GuildAgeRestrictionLevel(self.__dict__["nsfw_level"])

  @property
  def owner(self) -> Optional[bool]:
    """``True`` if the user is the owner of the guild."""
    return self.__dict__.get("owner", MISSING)

  @property
  def owner_id(self) -> Snowflake:
    """ID of the owner.

    .. note::
      This field is only sent when using the :meth:`HTTPClient.get_current_user_guilds <discord.http.HTTPClient.get_current_user_guilds>` endpoint and are relative to the requested user.
    """
    return Snowflake(self.__dict__["owner_id"])

  @property
  def permissions(self) -> Optional[PermissionFlags]:
    """Total permissions for the user in the guild (excludes overwrites and implicit permissions).

    .. note::
      This field is only sent when using the :meth:`~discord._http.HTTP.get_current_user_guilds` endpoint and are relative to the requested user.
    """
    if (data := self.__dict__.get("permissions", MISSING)) is MISSING: return data
    return PermissionFlags(int(data))

  @property
  def preferred_locale(self) -> Locale:
    """The preferred locale of a Community guild; used in server discovery and notices from Discord, and sent in interactions; defaults to :attr:`~discord.enums.Locale.ENGLISH_US`."""
    return Locale(self.__dict__["preferred_locale"])

  @property
  def premium_progress_bar_enabled(self) -> bool:
    """Whether the guild has the boost progress bar enabled."""
    return self.__dict__["premium_progress_bar_enabled"]

  @property
  def premium_subscription_count(self) -> Optional[int]:
    """The number of boosts this guild currently has."""
    return self.__dict__.get("premium_subscription_count", MISSING)

  @property
  def premium_tier(self) -> PremiumTier:
    """Premium tier (Server Boost level)."""
    return PremiumTier(self.__dict__["premium_tier"])

  @property
  def public_updates_channel_id(self) -> Nullable[Snowflake]:
    """The ID of the channel where admins and moderators of Community guilds receive notices from Discord."""
    if (data := self.__dict__["public_updates_channel_id"]) is None: return data
    return Snowflake(data)

  @property
  def region(self) -> Optional[Nullable[str]]:
    """Voice region Id of the guild (deprecated).

    .. attention::
        This field is deprecated and is replaced by :attr:`Channel.rtc_region <discord.objects.Channel.rtc_region>`.
    """
    return self.__dict__.get("region", MISSING)

  @property
  def roles(self) -> list[Role]:
    """Roles in the guild."""
    return [Role(**data) for data in self.__dict__["roles"]]

  @property
  def rules_channel_id(self) -> Nullable[Snowflake]:
    """The ID of the channel where Community guilds can display rules and/or guidelines."""
    if (data := self.__dict__["rules_channel_id"]) is None: return data
    return Snowflake(data)

  @property
  def safety_alerts_channel_id(self) -> Nullable[Snowflake]:
    """The ID of the channel where admins and moderators of Community guilds receive safety alerts from Discord."""
    if (data := self.__dict__["safety_alerts_channel_id"]) is None: return data
    return Snowflake(data)

  @property
  def splash(self) -> Nullable[str]:
    """Splash hash."""
    return self.__dict__["splash"]

  @property
  def stickers(self) -> Optional[list[Sticker]]:
    """Custom guild stickers."""
    if (data := self.__dict__.get("stickers", MISSING)) is MISSING: return data
    return [Sticker(**_) for _ in data]

  @property
  def system_channel_flags(self) -> SystemChannelFlags:
    """System channel flags."""
    return SystemChannelFlags(self.__dict__["system_channel_flags"])

  @property
  def system_channel_id(self) -> Nullable[Snowflake]:
    """The ID of the channel where guild notices such as welcome messages and boost events are posted."""
    if (data := self.__dict__["system_channel_id"]) is None: return data
    return Snowflake(data)

  @property
  def vanity_url_code(self) -> Nullable[str]:
    """The vanity URL code for the guild."""
    return self.__dict__["vanity_url_code"]

  @property
  def verification_level(self) -> VerificationLevel:
    """Verification level required for the guild."""
    return VerificationLevel(self.__dict__["verification_level"])

  @property
  def welcome_screen(self) -> Optional[WelcomeScreen]:
    """The welcome screen of a Community guild, shown to new members, returned in an :class:`~discord.objects.Invite`'s guild object."""
    if (data := self.__dict__.get("welcome_screen", MISSING)) is MISSING: return data
    return WelcomeScreen(**data)

  @property
  def widget_channel_id(self) -> Optional[Nullable[Snowflake]]:
    """The channel ID that the widget will generate an invite to, or ``None`` if set to no invite."""
    if (data := self.__dict__.get("widget_channel_id", MISSING)) in (MISSING, None): return data
    return Snowflake(data)

  @property
  def widget_enabled(self) -> Optional[bool]:
    """``True`` if the server widget is enabled."""
    return self.__dict__.get("widget_enabled", MISSING)