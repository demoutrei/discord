from enum import auto, IntEnum, StrEnum, unique


@unique
class ActivityType(IntEnum):
  PLAYING: int = 0
  STREAMING: int = 1
  LISTENING: int = 2
  WATCHING: int = 3
  CUSTOM: int = 4
  COMPETING: int = 5


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
class AuditLogEvent(IntEnum):
  """The **Object Changed** notes which object's values may be included in the entry. Though there are exceptions, possible keys in the :attr:`~discord.objects.AuditLogEntry.changes` array typically correspond to the object's fields. The descriptions and types for those fields can be found in the linked documentation for the object.

  If no object is noted, there won't be a :attr:`~discord.objects.AuditLogEntry.changes` array in the entry, though other fields like the :attr:`~discord.objects.AuditLogEntry.target_id` still exist and many have fields in the :attr:`~discord.objects.AuditLogEntry.options` object.

  .. hint::
      You should assume that your app may run into any field for the changed object, though none are guaranteed to be present. In most cases only a subset of the object's fields will be in the :attr:`~discord.objects.AuditLogEntry.changes` array.
  """

  GUILD_UPDATE: int = 1
  """Server settings were updated.

  **Object Changed**: :class:`~discord.objects.Guild`
  """

  CHANNEL_CREATE: int = 10
  """Channel was created.

  **Object Changed**: :class:`~discord.objects.Channel`
  """

  CHANNEL_UPDATE: int = 11
  """Channel settings were updated.

  **Object Changed**: :class:`~discord.objects.Channel`
  """

  CHANNEL_DELETE: int = 12
  """Channel was deleted.

  **Object Changed**: :class:`~discord.objects.Channel`
  """

  CHANNEL_OVERWRITE_CREATE: int = 13
  """Permission overwrite was added to a channel.

  **Object Changed**: :class:`~discord.objects.PermissionOverwrite`
  """

  CHANNEL_OVERWRITE_UPDATE: int = 14
  """Permission overwrite was updated for a channel.

  **Object Changed**: :class:`~discord.objects.PermissionOverwrite`
  """

  CHANNEL_OVERWRITE_DELETE: int = 15
  """Permission overwrite was deleted from a channel.

  **Object Changed**: :class:`~discord.objects.PermissionOverwrite`
  """

  MEMBER_KICK: int = 20
  """Member was removed from server."""

  MEMBER_PRUNE: int = 21
  """Members was pruned from server."""

  MEMBER_BAN_ADD: int = 22
  """Member was banned from server."""

  MEMBER_BAN_REMOVE: int = 23
  """Server ban was lifted for a member."""

  MEMBER_UPDATE: int = 24
  """Member was updated in a server.

  **Object Changed**: :class:`~discord.objects.GuildMember`
  """

  MEMBER_ROLE_UPDATE: int = 25
  """Member was added or removed from a role.

  **Object Changed**: :class:`~discord.objects.Role`
  """

  MEMBER_MOVE: int = 26
  """Member was moved to a different voice channel."""

  MEMBER_DISCONNECT: int = 27
  """Member was disconnected from a voice channel."""

  BOT_ADD: int = 28
  """Bot user was added to server."""

  ROLE_CREATE: int = 30
  """Role was created.

  **Object Changed**: :class:`~discord.objects.Role`
  """

  ROLE_UPDATE: int = 31
  """Role was edited.

  **Object Changed**: :class:`~discord.objects.Role`
  """

  ROLE_DELETE: int = 32
  """Role was deleted.

  **Object Changed**: :class:`~discord.objects.Role`
  """

  INVITE_CREATE: int = 40
  """Server invite was created.

  **Object Changed**: :class:`~discord.objects.Invite` and :class:`~discord.objects.InviteMetadata`
  """

  INVITE_UPDATE: int = 41
  """Server invite was updated.

  **Object Changed**: :class:`~discord.objects.Invite` and :class:`~discord.objects.InviteMetadata`
  """

  INVITE_DELETE: int = 42
  """Server invite was deleted.

  **Object Changed**: :class:`~discord.objects.Invite` and :class:`~discord.objects.InviteMetadata`
  """

  WEBHOOK_CREATE: int = 50
  """Webhook was created.

  **Object Changed**: :class:`~discord.objects.Webhook`
  """

  WEBHOOK_UPDATE: int = 51
  """Webhook properties or channel were updated.

  **Object Changed**: :class:`~discord.objects.Webhook`
  """

  WEBHOOK_DELETE: int = 52
  """Webhook was deleted.

  **Object Changed**: :class:`~discord.objects.Webhook`
  """

  EMOJI_CREATE: int = 60
  """Emoji was created.

  **Object Changed**: :class:`~discord.objects.Emoji`
  """

  EMOJI_UPDATE: int = 61
  """Emoji name was updated.

  **Object Changed**: :class:`~discord.objects.Emoji`
  """

  EMOJI_DELETE: int = 62
  """Emoji was deleted.

  **Object Changed**: :class:`~discord.objects.Emoji`
  """

  MESSAGE_DELETE: int = 72
  """Single message was deleted."""

  MESSAGE_BULK_DELETE: int = 73
  """Multiple messages were deleted."""

  MESSAGE_PIN: int = 74
  """Message was pinned to a channel."""

  MESSAGE_UNPIN: int = 75
  """Message was unpinned to a channel."""

  INTEGRATION_CREATE: int = 80
  """App was added to server.

  **Object Changed**: :class:`~discord.objects.Integration`
  """

  INTEGRATION_UPDATE: int = 81
  """App was updated (as an example, its scopes were updated).

  **Object Changed**: :class:`~discord.objects.Integration`
  """

  INTEGRATION_DELETE: int = 82
  """App was removed from server.

  **Object Changed**: :class:`~discord.objects.Integration`
  """

  STAGE_INSTANCE_CREATE: int = 83
  """Stage instance was created (stage channel becomes live).

  **Object Changed**: :class:`~discord.objects.StageInstance`
  """

  STAGE_INSTANCE_UPDATE: int = 84
  """Stage instance details were updated.

  **Object Changed**: :class:`~discord.objects.StageInstance`
  """

  STAGE_INSTANCE_DELETE: int = 85
  """Stage instance was deleted (stage channel no longer live).

  **Object Changed**: :class:`~discord.objects.StageInstance`
  """

  STICKER_CREATE: int = 90
  """Sticker was created.

  **Object Changed**: :class:`~discord.objects.Sticker`
  """

  STICKER_UPDATE: int = 91
  """STicker details were updated.

  **Object Changed**: :class:`~discord.objects.Sticker`
  """

  STICKER_DELETE: int = 92
  """Sticker was deleted.
  
  **Object Changed**: :class:`~discord.objects.Sticker`
  """

  GUILD_SCHEDULED_EVENT_CREATE: int = 100
  """Event was created.

  **Object Changed**: :class:`~discord.objects.GuildScheduledEvent`
  """

  GUILD_SCHEDULED_EVENT_UPDATE: int = 101
  """Event was updated.

  **Object Changed**: :class:`~discord.objects.GuildScheduledEvent`
  """

  GUILD_SCHEDULED_EVENT_DELETE: int = 102
  """Event was cancelled.

  **Object Changed**: :class:`~discord.objects.GuildScheduledEvent`
  """

  THREAD_CREATE: int = 110
  """Thread was created in a channel.

  **Object Changed**: :class:`~discord.objects.ThreadMetadata`
  """

  THREAD_UPDATE: int = 111
  """Thread was updated.

  **Object Changed**: :class:`~discord.objects.ThreadMetadata`
  """

  THREAD_DELETE: int = 112
  """Thread was deleted.

  **Object Changed**: :class:`~discord.objects.ThreadMetadata`
  """

  APPLICATION_COMMAND_PERMISSION_UPDATE: int = 121
  """Permissions were updated for a command.

  **Object Changed**: :class:`~discord.objects.ApplicationCommandPermissions`
  """

  SOUNDBOARD_SOUND_CREATE: int = 130
  """Soundboard sound was created.

  **Object Changed**: :class:`~discord.objects.SoundboardSound`
  """

  SOUNDBOARD_SOUND_UPDATE: int = 131
  """Soundboard sound was updated.

  **Object Changed**: :class:`~discord.objects.SoundboardSound`
  """

  SOUNDBOARD_SOUND_DELETE: int = 132
  """Soundboard sound was deleted.

  **Object Changed**: :class:`~discord.objects.SoundboardSound`
  """

  AUTO_MODERATION_RULE_CREATE: int = 140
  """Auto Moderation rule was created.

  **Object Changed**: :class:`~discord.objects.AutoModerationRule`
  """

  AUTO_MODERATION_RULE_UPDATE: int = 141
  """Auto Moderation rule was updated.

  **Object Changed**: :class:`~discord.objects.AutoModerationRule`
  """

  AUTO_MODERATION_RULE_DELETE: int = 142
  """Auto Moderation rule was deleted.

  **Object Changed**: :class:`~discord.objects.AutoModerationRule`
  """

  AUTO_MODERATION_BLOCK_MESSAGE: int = 143
  """Message was blocked by Auto Moderation."""

  AUTO_MODERATION_FLAG_TO_CHANNEL: int = 144
  """Message was flagged by Auto Moderation."""

  AUTO_MODERATION_USER_COMMUNICATION_DISABLED: int = 145
  """Member was timed out by Auto Moderation."""

  AUTO_MODERATION_QUARANTINE_USER: int = 146
  """Member was quarantined by Auto Moderation."""

  CREATOR_MONETIZATION_REQUEST_CREATED: int = 150
  """Creator monetization request was created."""

  CREATOR_MONETIZATION_TERMS_ACCEPTED: int = 151
  """Creator monetization terms were accepted."""

  ONBOARDING_PROMPT_CREATE: int = 163
  """Guild Onboarding Question was created.

  **Object Changed**: :class:`~discord.objects.OnboardingPrompt`
  """

  ONBOARDING_PROMPT_UPDATE: int = 164
  """Guild Onboarding Question was updated.

  **Object Changed**: :class:`~discord.objects.OnboardingPrompt`
  """

  ONBOARDING_PROMPT_DELETE: int = 165
  """Guild Onboarding Question was deleted.

  **Object Changed**: :class:`~discord.objects.OnboardingPrompt`
  """

  ONBOARDING_CREATE: int = 166
  """Guild Onboarding was created.

  **Object Changed**: :class:`~discord.objects.GuildOnboarding`
  """

  ONBOARDING_UPDATE: int = 167
  """Guild Onboarding was updated.

  **Object Changed**: :class:`~discord.objects.GuildOnboarding`
  """

  HOME_SETTINGS_CREATE: int = 190
  """Guild Server Guide was created."""

  HOME_SETTINGS_UPDATE: int = 191
  """Guild Server Guide was updated."""

  VOICE_CHANNEL_STATUS_CREATE: int = 192
  """A voice channel status was set by a user."""

  VOICE_CHANNEL_STATUS_DELETE: int = 193
  """A voice channel status was deleted by a user."""


@unique
class AutoModerationActionType(IntEnum):
  BLOCK_MESSAGE: int = 1
  """Blocks a member's message and prevents it from being posted. A custom explanation can be specified and shown to members whenever their message is blocked."""

  SEND_ALERT_MESSAGE: int = 2
  """Logs user content to a specified channel"""

  TIMEOUT: int = 3
  """Timeout user for a specified duration.

  .. important::
  
      Can only be set up for :attr:`~discord.enums.AutoModerationRuleTriggerType.KEYWORD` and :attr:`~discord.enums.AutoModerationRuleTriggerType.MENTION_SPAM` rules. The :attr:`~discord.flags.PermissionFlag.MODERATE_MEMBERS` permission is required to use the :attr:`~.TIMEOUT` action type.
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
class ChannelType(IntEnum):
  GUILD_TEXT: int = 0
  """A text channel within a server."""

  DM: int = 1
  """A direct message between users."""

  GUILD_VOICE: int = 2
  """A voice channel within a server."""

  GROUP_DM: int = 3
  """A direct message between multiple users."""

  GUILD_CATEGORY: int = 4
  """An organizational category that contains up to 50 channels."""

  GUILD_ANNOUNCEMENT: int = 5
  """A channel that users can follow and crosspost into their own server (formerly news channels)."""

  ANNOUNCEMENT_THREAD: int = 10
  """A temporary sub-channel within a :attr:`~.GUILD_ANNOUNCEMENT` channel."""

  PUBLIC_THREAD: int = 11
  """A temporary sub-channel within a :attr:`~.GUILD_TEXT` or :attr:`~.GUILD_FORUM` channel."""

  PRIVATE_THREAD: int = 12
  """A temporary sub-channel within a :attr:`~.GUILD_TEXT` channel that is only viewable by those invited and those with the :attr:`~discord.flags.PermissionFlag.MANAGE_THREADS` permission."""

  GUILD_STAGE_VOICE: int = 13
  """A voice channel for hosting events with an audience."""

  GUILD_DIRECTORY: int = 14
  """The channel in a hub containing the listed servers."""

  GUILD_FORUM: int = 15
  """Channel that can only contain threads."""

  GUILD_MEDIA: int = 16
  """Channel that can only contain threads, similar to :attr:`~.GUILD_FORUM` channels."""


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
class EntitlementType(IntEnum):
  PURCHASE: int = 1
  """Entitlement was purchased by user."""

  PREMIUM_SUBSCRIPTION: int = 2
  """Entitlement for Discord Nitro subscription."""

  DEVELOPER_GIFT: int = 3
  """Entitlement was gifted by developer."""

  TEST_MODE_PURCHASE: int = 4
  """Entitlement was purchased by a dev in application test mode."""

  FREE_PURCHASE: int = 5
  """Entitlement was granted when the SKU was free."""

  USER_GIFT: int = 6
  """Entitlement was gifted by another user."""

  PREMIUM_PURCHASE: int = 7
  """Entitlement was claimed by user for free as a Nitro Subscriber."""

  APPLICATION_SUBSCRIPTION: int = 8
  """Entitlement was purchased as an app subscription."""


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
class GuildScheduledEventEntityType(IntEnum):
  STAGE_INSTANCE: int = 1
  VOICE: int = 2
  EXTERNAL: int = 3


@unique
class GuildScheduledEventPrivacyLevel(IntEnum):
  GUILD_ONLY: int = 2
  """The scheduled event is only accessible to guild members."""


@unique
class GuildScheduledEventRecurrenceRuleFrequency(IntEnum):
  YEARLY: int = 0
  MONTHLY: int = 1
  WEEKLY: int = 2
  DAILY: int = 3


@unique
class GuildScheduledEventRecurrenceRuleMonth(IntEnum):
  JANUARY: int = 1
  FEBRUARY: int = 2
  MARCH: int = 3
  APRIL: int = 4
  MAY: int = 5
  JUNE: int = 6
  JULY: int = 7
  AUGUST: int = 8
  SEPTEMBER: int = 9
  OCTOBER: int = 10
  NOVEMBER: int = 11
  DECEMBER: int = 12


@unique
class GuildScheduledEventRecurrenceRuleWeekday(IntEnum):
  MONDAY: int = 0
  TUESDAY: int = 1
  WEDNESDAY: int = 2
  THURSDAY: int = 3
  FRIDAY: int = 4
  SATURDAY: int = 5
  SUNDAY: int = 6


@unique
class GuildScheduledEventStatus(IntEnum):
  SCHEDULED: int = 1
  ACTIVE: int = 2
  COMPLETED: int = 3
  CANCELED: int = 4


@unique
class IntegrationExpireBehavior(IntEnum):
  REMOVE_ROLE: int = 0
  KICK: int = 1


@unique
class InviteTargetType(IntEnum):
  STREAM: int = 1
  EMBEDDED_APPLICATION: int = 2


@unique
class InviteType(IntEnum):
  GUILD: int = 0
  GROUP_DM: int = 1
  FRIEND: int = 2


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
class OnboardingMode(IntEnum):
  """Defines the criteria used to satisfy Onboarding constraints that are required for enabled."""

  ONBOARDING_DEFAULT: int = 0
  """Counts only Default Channels towards constraints."""

  ONBOARDING_ADVANCED: int = 1
  """Counts Default Channels and Questions towards constraints."""


@unique
class OnboardingPromptType(IntEnum):
  MULTIPLE_CHOICE: int = 0
  DROPDOWN: int = 1


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
class StageInstancePrivacyLevel(IntEnum):
  PUBLIC: int = 1
  """The Stage instance is visible publicly (deprecated)."""


  GUILD_ONLY: int = 2
  """The Stage isntance is visible to only guild members."""


@unique
class StatusDisplayType(IntEnum):
  NAME: int = 0
  """\"Listening to Spotify\"."""

  STATE: int = 1
  """\"Listening to Rick Astley\""""

  DETAILS: int = 2
  """\"Listening to Never Gonna Give You Up\""""


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
class VideoQualityMode(IntEnum):
  AUTO: int = 1
  """Discord chooses the quality for optimal performances"""

  FULL: int = 2
  """720p"""


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


@unique
class WebhookType(IntEnum):
  """
  .. tip::
      These types don't include webhook events, which are outgoing webhooks sent to your app by Discord.
  """

  INCOMING: int = 1
  """Incoming Webhooks can post messages to channels with a generated token."""

  CHANNEL_FOLLOWER: int = 2
  """Channel Follower Webhooks are internal webhooks used with Channel Following to post new messages into channels."""

  APPLICATION: int = 3
  """Application webhooks are webhooks used with Interactions."""