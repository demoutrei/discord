from ..enums import DefaultMessageNotificationLevel, ExplicitContentFilterLevel, GuildAgeRestrictionLevel, GuildFeature, Locale, MFALevel, PremiumTier, VerificationLevel
from ..flags import PermissionFlag, SystemChannelFlag
from ..snowflake import Snowflake
from ..utils import Nullable, Optional
from ._base import BaseObject
from .emoji import Emoji
from .incidents_data import IncidentsData
from .role import Role
from .sticker import Sticker
from .welcome_screen import WelcomeScreen


class Guild(BaseObject):
  """Represents an isolated collection of users and channels, and are often referred to as "servers" in the UI."""

  afk_channel_id: Nullable[Snowflake]
  """ID of AFK channel"""

  afk_timeout: int
  """AFK timeout in seconds"""

  application_id: Nullable[Snowflake]
  """Application ID of the guild creator if it is bot-created"""

  approximate_member_count: Optional[int]
  """Approximate number of members in this guild, retunred from the ``GET /guilds/<id>`` and ``/users/@me/guilds`` endpoints when ``with_counts`` is ``True``"""

  approximate_presence_count: Optional[int]
  """Approximate number of non-offline members in this guild, returned from the ``GET /guilds/<id>`` and ``/users/@me/guilds`` endpoints when ``with_counts`` is ``True``"""

  banner: Nullable[str]
  """Banner hash"""

  default_message_notifications: DefaultMessageNotificationLevel
  """Default message notifications level"""

  description: Nullable[str]
  """The description of a guild"""

  discovery_splash: Nullable[str]
  """Discovery splash hash; only present for guilds with the "DISCOVERABLE" feature"""

  emojis: list[Emoji]
  """Custom guild emojis"""

  explicit_content_filter: ExplicitContentFilterLevel
  """Explicit content filter level"""

  features: list[GuildFeature]
  """Enabled guild feature"""

  icon: Nullable[str]
  """Icon hash"""

  icon_hash: Optional[Nullable[str]]
  """Icon hash, returned when in the template object"""

  id: Snowflake
  """Guild ID"""

  incidents_data: Nullable[IncidentsData]
  """The incidents data for this guild"""

  max_members: Optional[int]
  """The maximum number of members for the guild"""

  max_presences: Optional[Nullable[int]]
  """The maximum number of presences for the guild (``None`` is always returned, arapt from the largest of guilds)"""

  max_stage_video_channel_users: Optional[int]
  """The maximum amount of users in a stage video channel"""

  max_video_channel_users: Optional[int]
  """The maximum amount of users in a video channel"""

  mfa_level: MFALevel
  """Required MFA level for the guild"""

  name: str
  """Guild name (2-100 characters, excluding trailing and leading whitespace)"""

  nsfw_level: GuildAgeRestrictionLevel
  """Guild age-restriction level"""

  owner: Optional[bool]
  """``True`` if the user is the owner of the guild"""

  owner_id: Snowflake
  """ID of the owner.

  .. note::
     This field is only sent when using the :meth:`~discord._http.HTTP.get_current_user_guilds` endpoint and are relative to the requested user.
  """

  permissions: Optional[PermissionFlag]
  """Total permissiosn for the user in the guild (excludes overwrites and implicit permissions).

  .. note::
     This field is only sent when using the :meth:`~discord._http.HTTP.get_current_user_guilds` endpoint and are relative to the requested user.
  """

  preferred_locale: Locale
  """The preferred locale of a Community guild; used in server discovery and notices from Discord, and sent in interactions; defaults to :attr:`~discord.enums.Locale.ENGLISH_US`"""

  premium_progress_bar_enabled: bool
  """Whether the guild has the boost progress bar enabled"""

  premium_subscription_count: Optional[int]
  """The number of boosts this guild currently has"""

  premium_tier: PremiumTier
  """Premium tier (Server Boost level)"""

  public_updates_channel_id: Nullable[Snowflake]
  """The ID of the channel where admins and moderators of Community guilds receive notices from Discord"""

  region: Optional[Nullable[str]]
  """Voice region Id of the guild (deprecated).

  .. note::
      This field is deprecated and is replaced by :attr:`discord.objects.Channel.rtc_region`.
  """

  roles: list[Role]
  """Roles in the guild"""

  rules_channels_id: Nullable[Snowflake]
  """The ID of the channel where Community guilds can display rules and/or guidelines"""

  safety_alerts_channel_id: Nullable[Snowflake]
  """The ID of the channel where admins and moderators of Community guilds receive safety alerts from Discord"""

  splash: Nullable[str]
  """Splash hash"""

  stickers: Optional[list[Sticker]]
  """Custom guild stickers"""

  system_channel_flags: SystemChannelFlag
  """System channel flags"""

  system_channel_id: Nullable[Snowflake]
  """The ID of the channel where guild notices such as welcome messages and boost events are posted"""

  vanity_url_code: Nullable[str]
  """The vanity URL code for the guild"""

  verification_level: VerificationLevel
  """Verification level required for the guild"""

  welcome_screen: Optional[WelcomeScreen]
  """The welcome screen of a Community guild, shown to new members, returned in an :class:`~discord.objects.Invite`'s guild object"""

  widget_channel_id: Optional[Nullable[Snowflake]]
  """The channel ID that the widget will generate an invite to, or ``None`` if set to no invite"""

  widget_enabled: Optional[bool]
  """``True`` if the server widget is enabled"""