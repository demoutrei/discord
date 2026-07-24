from enum import auto, IntEnum, StrEnum, unique


@unique
class ApplicationCommandPermissionType(IntEnum):
  ROLE: int = 1
  USER: int = 2
  CHANNEL: int = 3


@unique
class ApplicationEventWebhookStatus(IntEnum):
  """Status indicating whether event webhooks are enabled or disabled for an application"""

  DISABLED: int = 1
  """Webhook events are disabled by developer"""

  ENABLED: int = 2
  """Webhook events are enabled by developer"""

  DISABLED_BY_DISCORD: int = 3
  """Webhook events are disabled by Discord, usually due to inactivity"""


@unique
class ApplicationIntegrationType(StrEnum):
  """Where an app can be installed, also called its supported **installation contexts**."""
  
  GUILD_INSTALL: str = "0"
  """App is installable to servers"""

  USER_INSTALL: str = "1"
  """App is installable to users"""


@unique
class AutoModerationActionType(IntEnum):
  BLOCK_MESSAGE: int = 1
  """Blocks a member's message and prevents it from being posted. A custom explanation can be specified and shown to members whenever their message is blocked."""

  SEND_ALERT_MESSAGE: int = 2
  """Logs user content to a specified channel"""

  TIMEOUT: int = 3
  """Timeout user for a specified duration.

  \\* Can only be set up for :attr:`~discord.enums.AutoModerationRuleTriggerType.KEYWORD` and :attr:`~discord.enums.AutoModerationRuleTriggerType.MENTION_SPAM` rules. The :attr:`~discord.flags.PermissionFlag.MODERATE_MEMBERS` permission is required to use the :attr:`~.TIMEOUT` action type.
  """

  BLOCK_MEMBER_INTERACTION: int = 4
  """Prevents a member from using text, voice, or other interactions"""


@unique
class AutoModerationRuleEventType(IntEnum):
  """Indicates in what event context a rule should be checked."""

  MESSAGE_SEND: int = 1
  """When a member sends or edits a message in the guild"""

  MEMBER_UPDATE: int = 2
  """When a member edits their profile"""


@unique
class AutoModerationRuleKeywordPresetType(IntEnum):
  PROFANITY: int = 1
  """Words that may be considered forms of swearing or cursing"""

  SEXUAL_CONTENT: int = 2
  """Words that refer to sexually explicit behavior or activity"""

  SLURS: int = 3
  """Personal insults or words that may be considered hate speech"""


@unique
class AutoModerationRuleTriggerType(IntEnum):
  """Characterizes the type of content which can trigger the rule."""

  KEYWORD: int = 1
  """Check if content contains words from a user-defined list of keywords.

  **Max per Guild**: 6
  """

  SPAM: int = 3
  """Check if content represents generic spam.

  **Max per Guild**: 1
  """

  KEYWORD_PRESET: int = 4
  """Check if content contains words from internal pre-defined words.

  **Max per Guild**: 1
  """

  MENTION_SPAM: int = 5
  """Check if content contains more unique mentions than allowed.

  **Max per Guild**: 1
  """

  MEMBER_PROFILE: int = 6
  """Check if member profile contains words from a user-defined list of keywords.

  **Max per Guild**: 1
  """


@unique
class DefaultMessageNotificationLevel(IntEnum):
  ALL_MESSAGES: int = 0
  """Members will receive notifications for all messages by default"""

  ONLY_MENTIONS: int = 1
  """Members will receive notifications only for messages that @mention them by default"""


@unique
class DefaultSortOrderType(IntEnum):
  LATEST_ACTIVITY: int = 0
  """Sort forum posts by activity"""

  CREATION_DATE: int = 1
  """Sort forum posts by creation time (from most recent to oldest)"""


@unique
class ExplicitContentFilterLevel(IntEnum):
  DISABLED: int = 0
  """Media content will not be scanned"""

  MEMBERS_WITHOUT_ROLES: int = 1
  """Media content sent by members without roles will be scanned"""

  ALL_MEMBERS: int = 2
  """Media content sent by all members will be scanned"""


@unique
class ForumLayoutType(IntEnum):
  NOT_SET: int = 0
  """No default has been set for forum channel"""

  LIST_VIEW: int = 1
  """Display posts as a list"""

  GALLERY_VIEW: int = 2
  """Display posts as a collection of tiles"""


@unique
class GuildAgeRestrictionLevel(IntEnum):
  DEFAULT: int = 0
  EXPLICIT: int = 1
  SAFE: int = 2
  AGE_RESTRICTED: int = 3


@unique
class GuildFeature(StrEnum):
  ANIMATED_BANNER: str = "ANIMATED_BANNER"
  """Guild has access to set an animated guild banner image"""

  ANIMATED_ICON: str = "ANIMATED_ICON"
  """Guild has access to set an animated guild icon"""

  APPLICATION_COMMAND_PERMISSIONS_V2: str = "APPLICATION_COMMAND_PERMISSIONS_V2"
  """Guild is using the old permissions configuration behavior"""

  AUTO_MODERATION: str = "AUTO_MODERATION"
  """Guild has set up auto moderation rules"""

  BANNER: str = "BANNER"
  """Guild has access to set a guild banner image"""

  COMMUNITY: str = "COMMUNITY"
  """Guild can enable welcome screen, Membership Screening, stage channels and discovery, and receives community updates"""

  CREATOR_MONETIZABLE_PROVISIONAL: str = "CREATOR_MONETIZABLE_PROVISIONAL"
  """Guild has enabled monetization"""

  CREATOR_STORE_PAGE: str = "CREATOR_STORE_PAGE"
  """Guild has enabled the role subscription promo page"""

  DEVELOPER_SUPPORT_SERVER: str = "DEVELOPER_SUPPORT_SERVER"
  """Guild has been set as a support server on the App Directory"""

  DISCOVERABLE: str = "DISCOVERABLE"
  """Guild is able to be discovered in the directory"""

  ENHANCED_ROLE_COLORS: str = "ENHANCED_ROLE_COLORS"
  """Guild is able to set gradient colors to roles"""

  FEATURABLE: str = "FEATURABLE"
  """Guild is able to be featured in the directory"""

  GUESTS_ENABLED: str = "GUESTS_ENABLED"
  """Guild has access to guest invites"""

  GUILD_TAGS: str = "GUILD_TAGS"
  """Guild has access to set guild tags"""

  INVITES_DISABLED: str = "INVITES_DISABLED"
  """Guild has paused invites, preventing new users from joining"""

  INVITE_SPLASH: str = "INVITE_SPLASH"
  """Guild has access to set an invite splash background"""

  MEMBER_VERIFICATION_GATE_ENABLED: str = "MEMBER_VERIFICATION_GATE_ENABLED"
  """Guild has enabled Membership Screening"""

  MORE_SOUNDBOARD: str = "MORE_SOUNDBOARD"
  """Guild has increased custom soundboard sound slots"""

  MORE_STICKERS: str = "MORE_STICKERS"
  """Guild has increased custom sticker slots"""

  NEWS: str = "NEWS"
  """Guild has access to create announcement channels"""

  PARTNERED: str = "PARTNERED"
  """Guild is partnered"""

  PREVIEW_ENABLED: str = "PREVIEW_ENABLED"
  """Guild can be previewed before joining via Membership Screening or the directory"""

  RAID_ALERTS_DISABLED: str = "RAID_ALERTS_DISABLED"
  """Guild has disabled alerts for join raids in the configured safety alerts channel"""

  ROLE_ICONS: str = "ROLE_ICONS"
  """Guild is able to set role icons"""

  ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE: str = "ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE"
  """Guild has role subscriptions that can be purchased"""

  ROLE_SUBSCRIPTIONS_ENABLED: str = "ROLE_SUBSCRIPTIONS_ENABLED"
  """Guild has enabled role subscriptions"""

  SOUNDBOARD: str = "SOUNDBOARD"
  """Guild has created soundboard sounds"""

  TICKETED_EVENTS_ENABLED: str = "TICKETED_EVENTS_ENABLED"
  """Guild has enabled ticketed events"""

  VANITY_URL: str = "VANITY_URL"
  """Guild has access to set a vanity URL"""

  VERIFIED: str = "VERIFIED"
  """Guild is verified"""

  VIP_REGIONS: str = "VIP_REGIONS"
  """Guild has access to set 384kbps bitrate in voice (previously VIP voice servers)"""

  WELCOME_SCREEN_ENABLED: str = "WELCOME_SCREEN_ENABLED"
  """Guild has enabld the welcome screen"""


@unique
class Locale(StrEnum):
  BULGARIAN: str = "bg"
  CHINESE_CHINA: str = "zh-CN"
  CHINESE_TAIWAN: str = "zh-Tw"
  CROATIAN: str = "hr"
  CZECH: str = "cs"
  DANISH: str = "da"
  DUTCH: str = "nl"
  ENGLISH_UK: str = "en-GB"
  ENGLISH_US: str = "en-US"
  FINNISH: str = "fi"
  FRENCH: str = "fr"
  GERMAN: str = "de"
  GREEK: str = "el"
  HINDI: str = "hi"
  HUNGARIAN: str = "hu"
  INDONESIAN: str = "id"
  ITALIAN: str = "it"
  JAPANESE: str = "ja"
  KOREAN: str = "ko"
  LITHUANIAN: str = "lt"
  NORWEGIAN: str = "no"
  POLISH: str = "pl"
  PORTUGUESE_BRAZILIAN: str = "pt-BR"
  ROMANIAN_ROMANIA: str = "ro"
  RUSSIAN: str = "ru"
  SPANISH: str = "es-ES"
  SPANISH_LATAM: str = "es-419"
  SWEDISH: str = "sv-SE"
  THAI: str = "th"
  TURKISH: str = "tr"
  UKRANIAN: str = "uk"
  VIETNAMESE: str = "vi"


@unique
class MembershipState(IntEnum):
  INVITED: int = 1
  ACCEPTED: int = 2


@unique
class MFALevel(IntEnum):
  NONE: int = 0
  """Guild has no MFA/2FA requirements for moderation actions"""
  
  ELEVATED: int = 1
  """Guild has 2FA requirements for moderation actions"""


@unique
class NameplatePalette(StrEnum):
  BERRY: str = auto()
  BUBBLE_GUM: str = auto()
  CLOVER: str = auto()
  COBALT: str = auto()
  CRIMSON: str = auto()
  FOREST: str = auto()
  LEMON: str = auto()
  SKY: str = auto()
  TEAL: str = auto()
  VIOLET: str = auto()
  WHITE: str = auto()


@unique
class OpCode(IntEnum):
  DISPATCH: int = 0
  """An event was dispatched."""

  HEARTBEAT: int = 1
  """Fired periodically by the client to keep the connection alive."""

  IDENTIFY: int = 2
  """Starts a new session during the initial handshake."""

  PRESENCE_UPDATE: int = 3
  """Update the client's presence."""

  VOICE_STATE_UPDATE: int = 4
  """Used to join/leave or move between voice channels."""

  RESUME: int = 6
  """Resume a previous session that was disconnected."""

  RECONNECT: int = 7
  """You should attempt to reconnect and resume immediately."""

  REQUEST_GUILD_MEMBERS: int = 8
  """Request information about offline guild members in a large guild."""

  INVALID_SESSION: int = 9
  """The session has been invalidated. You should reconnect and identify/resume accordingly."""

  HELLO: int = 10
  """Sent immediately after connecting, contains the ``heartbeat_interval`` to use."""

  HEARTBEAT_ACK: int = 11
  """Sent in response to receiving a heartbeat to acknowledge that it has been received."""

  REQUEST_SOUNDBOARD_SOUNDS: int = 31
  """Request information about soundboard sounds in a set of guilds."""

  REQUEST_CHANNEL_INFO: int = 43
  """Request ephemeral channel data for channels in a guild."""


@unique
class PremiumTier(IntEnum):
  NONE: int = 0
  """Guild has not unlocked any Server Boost perks"""

  TIER_1: int = 1
  """Guild has unlocked Server Boost level 1 perks"""

  TIER_2: int = 2
  """Guild has unlocked Server Boost level 2 perks"""

  TIER_3: int = 3
  """Guild has unlocked Server Boost level 3 perks"""


@unique
class PremiumType(IntEnum):
  """Premium types denote the level of premium a user has."""

  NONE: int = 0
  NITRO_CLASSIC: int = 1
  NITRO: int = 2
  NITRO_BASIC: int = 3


@unique
class StickerFormatType(IntEnum):
  PNG: int = 1
  APNG: int = 2
  LOTTIE: int = 3
  GIF: int = 4


@unique
class StickerType(IntEnum):
  STANDARD: int = 1
  """An official sticker in a pack"""

  GUILD: int = 2
  """A sticker uplaoded to a guild for the guild's members"""


@unique
class TeamMemberRole(StrEnum):
  OWNER: str = ""
  """Owners are the most permissible role, and can take destructive, irreversible actions like deleting team-owned apps or the team itself. Teams are limited to 1 owner."""

  ADMIN: str = auto()
  """Admins have similar access as owners, except they cannot take destructive actions on the team or team-owned apps."""

  DEVELOPER: str = auto()
  """Developers can access information about team-owned apps, like the client secret or public key. They can also take limited actions on team-owned apps, like configuring interaction endpoints or resetting the bot token. Members with the :attr:`~.DEVELOPER` role *cannot* manage the team or its members, or take destructive actions on team-owned apps."""

  READ_ONLY: str = auto()
  """Read-only members can access information about a team and any team-owned apps. Some examples including getting the IDs of applications and exporting payout records. Members can also invite bots associated with team-owned apps that are marked private."""


@unique
class VerificationLevel(IntEnum):
  NONE: int = 0
  """Unrestricted"""

  LOW: int = 1
  """Must have verified email on account"""

  MEDIUM: int = 2
  """Must be registered on Discord for longer than 5 minutes"""

  HIGH: int = 3
  """Must be a member of the server for longer than 10 minutes"""

  VERY_HIGH: int = 4
  """Must have a verified phone number"""


@unique
class WebhookEventType(StrEnum):
  APPLICATION_AUTHORIZED: str = "APPLICATION_AUTHORIZED"
  """Sent when an app was authorized by a user to a server or their account"""

  APPLICATION_DEAUTHORIZED: str = "APPLICATION_DEAUTHORIZED"
  """Sent when an app was deauthorized by a user"""

  ENTITLEMENT_CREATE: str = "ENTITLEMENT_CREATE"
  """Entitlement was created"""

  ENTITLEMENT_UPDATE: str = "ENTITLEMENT_UPDATE"
  """Entitlement was updated"""

  ENTITLEMENT_DELETE: str = "ENTITLEMENT_DELETE"
  """Entitlement was deleted"""

  QUEST_USER_ENROLLMENT: str = "QUEST_USER_ENROLLMENT"
  """User was added to a Quest (currently unavailable)"""

  LOBBY_MESSAGE_CREATE: str = "LOBBY_MESSAGE_CREATE"
  """Sent when a message is created in a lobby"""
  
  LOBBY_MESSAGE_UPDATE: str = "LOBBY_MESSAGE_UPDATE"
  """Sent when a message is updated in a lobby"""

  LOBBY_MESSAGE_DELETE: str = "LOBBY_MESSAGE_DELETE"
  """Sent when a message is deleted in a lobby"""

  GAME_DIRECT_MESSAGE_CREATE: str = "GAME_DIRECT_MESSAGE_CREATE"
  """Sent when a direct message is created during an active Social SDK session"""

  GAME_DIRECT_MESSAGE_UPDATE: str = "GAME_DIRECT_MESSAGE_UPDATE"
  """Sent when a direct message is updated during an active Social SDK session"""

  GAME_DIRECT_MESSAGE_DELETE: str = "GAME_DIRECT_MESSAGE_DELETE"
  """Sent when a direct message is deleted during an active Social SDK session"""