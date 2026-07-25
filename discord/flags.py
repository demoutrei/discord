from enum import IntFlag, unique


@unique
class ApplicationFlag(IntFlag):
  APPLICATION_AUTO_MODERATION_RULE_CREATE_BADGE: int = 1 << 6
  """Indicates if an app uses the Auto Moderation API"""

  GATEWAY_PRESENCE: int = 1 << 12
  """Intent required for bots in 100 or more servers to receive ``presence_update`` events"""

  GATEWAY_PRESENCE_LIMITED: int = 1 << 13
  """Intent required for bots in under 100 servers to receive ``presence_update`` events, found on the Bot page in your app's settings"""

  GATEWAY_GUILD_MEMBERS: int = 1 << 14
  """Intent requried for bots in 100 or more servers to receive member-related events like ``guild_member_add``"""

  GATEWAY_GUILD_MEMBERS_LIMITED: int = 1 << 15
  """Intent required for bots in under 100 servers to receive member-related events like ``guild_member_add``, found on the Bot page in your app's settings"""

  VERIFICATION_PENDING_GUILD_LIMIT: int = 1 << 16
  """Indicates unusual growth of an app that prevents verification"""

  EMBEDDED: int = 1 << 17
  """Indicates if an app is embedded within the Discord client (currently unavailable publicly)"""

  GATEWAY_MESSAGE_CONTENT: int = 1 << 18
  """Intent required for bots in 100 or more servers to receive message content"""

  GATEWAY_MESSAGE_CONTENT_LIMITED: int = 1 << 19
  """Intent required for bots in under 100 servers to receive message content, found on the Bot page in your app's settings"""

  APPLICATION_COMMAND_BADGE: int = 1 << 23
  """Indicates if an app has registered global application commands"""


@unique
class ChannelFlag(IntFlag):
   PINNED: int = 1 << 1
   """This thread is pinned to the top of its parent :attr:`~discord.enums.ChannelType.GUILD_FORUM` or :attr:`~discord.enums.ChannelType.GUILD_MEDIA` channel"""

   REQUIRE_TAG: int = 1 << 4
   """Whether a tag is required to be specified when creating a thread in a :attr:`~discord.enums.ChannelType.GUILD_FORUM` or a :attr:`~discord.enums.ChannelType.GUILD_MEDIA` channel. Tags are specified in the :attr:`~discord.objects.ChannelType.applied_tags` field"""

   HIDE_MEDIA_DOWNLOAD_OPTIONS: int = 1 << 15
   """When set hides the embedded media download options. Available only for media channels"""

   IS_SPOILER_CHANNEL: int = 1 << 21
   """This channel is a Spoiler Channel i.e. users must opt-in to view its contents. Can be set on all textual guild channels and voice channels (not :attr:`~discord.enums.ChannelType.GUILD_STAGE`). Can only be set if channel's :attr:`~discord.objects.Channel.nsfw` is ``False``"""


@unique
class GatewayIntent(IntFlag):
  """Represents a set of Gateway intents"""

  GUILDS: int = 1 << 0
  """- GUILD_CREATE
  - GUILD_UPDATE
  - GUILD_DELETE
  - GUILD_ROLE_CREATE
  - GUILD_ROLE_UPDATE
  - GUILD_ROLE_DELETE
  - CHANNEL_CREATE
  - CHANNEL_UPDATE
  - CHANNEL_DELETE
  - CHANNEL_PINS_UPDATE
  - THREAD_CREATE
  - THREAD_UPDATE
  - THREAD_DELETE
  - THREAD_LIST_SYNC
  - THREAD_MEMBER_UPDATE
  - THREAD_MEMBERS_UPDATE
  - STAGE_INSTANCE_CREATE
  - STAGE_INSTANCE_UPDATE
  - STAGE_INSTANCE_DELETE
  - VOICE_CHANNEL_STATUS_UPDATE
  - VOICE_CHANNEL_START_TIME_UPDATE
  """

  GUILD_MEMBERS: int = 1 << 1
  """- GUILD_MEMBER_ADD
  - GUILD_MEMBER_UPDATE
  - GUILD_MEMBER_REMOVE
  - THREAD_MEMBERS_UPDATE
  """

  GUILD_MODERATION: int = 1 << 2
  """- GUILD_AUDIT_LOG_ENTRY_CREATE
  - GUILD_BAN_ADD
  - GUILD_BAN_REMOVE
  """

  GUILD_EXPRESSIONS: int = 1 << 3
  """- GUILD_EMOJIS_UPDATE
  - GUILD_STICKERS_UPDATE
  - GUILD_SOUNDBOARD_SOUND_CREATE
  - GUILD_SOUNDBOARD_SOUND_UPDATE
  - GUILD_SOUNDBOARD_SOUND_DELETE
  - GUILD_SOUNDBOARD_SOUNDS_UPDATE
  """

  GUILD_INTEGRATIONS: int = 1 << 4
  """- GUILD_INTEGRATIONS_UPDATE
  - INTEGRATION_CREATE
  - INTEGRATION_UPDATE
  - INTEGRATION_DELETE
  """

  GUILD_WEBHOOKS: int = 1 << 5
  """- WEBHOOKS_UPDATE"""

  GUILD_INVITES: int = 1 << 6
  """- INVITE_CREATE
  - INVITE_DELETE
  """

  GUILD_VOICE_STATES: int = 1 << 7
  """- VOICE_CHANNEL_EFFECT_SEND
  - VOICE_STATE_UPDATE
  """

  GUILD_PRESENCES: int = 1 << 8
  """- PRESENCE_UPDATE"""

  GUILD_MESSAGES: int = 1 << 9
  """- MESSAGE_CREATE
  - MESSAGE_UPDATE
  - MESSAGE_DELETE
  - MESSAGE_DELETE_BULK
  """

  GUILD_MESSAGE_REACTIONS: int = 1 << 10
  """- MESSAGE_REACTION_ADD
  - MESSAGE_REACTION_REMOVE
  - MESSAGE_REACTION_REMOVE_ALL
  - MESSAGE_REACTION_REMOVE_EMOJI
  """

  GUILD_MESSAGE_TYPING: int = 1 << 11
  """- TYPING_START"""

  DIRECT_MESSAGES: int = 1 << 12
  """- MESSAGE_CREATE
  - MESSAGE_UPDATE
  - MESSAGE_DELETE
  - CHANNEL_PINS_UPDATE
  """

  DIRECT_MESSAGE_REACTIONS: int = 1 << 13
  """- MESSAGE_REACTION_ADD
  - MESSAGE_REACTION_REMOVE
  - MESSAGE_REACTION_REMOVE_ALL
  - MESSAGE_REACTION_REMOVE_EMOJI
  """

  DIRECT_MESSAGE_TYPING: int = 1 << 14
  """- TYPING_START"""

  MESSAGE_CONTENT: int = 1 << 15

  GUILD_SCHEDULED_EVENTS: int = 1 << 16
  """- GUILD_SCHEDULED_EVENT_CREATE
  - GUILD_SCHEDULED_EVENT_UPDATE
  - GUILD_SCHEDULED_EVENT_DELETE
  - GUILD_SCHEDULED_EVENT_USER_ADD
  - GUILD_SCHEDULED_EVENT_USER_REMOVE
  """

  AUTO_MODERATION_CONFIGURATION: int = 1 << 20
  """- AUTO_MODERATION_RULE_CREATE
  - AUTO_MODERATION_RULE_UPDATE
  - AUTO_MODERATION_RULE_DELETE
  """

  AUTO_MODERATION_EXECUTION: int = 1 << 21
  """- AUTO_MODERATION_ACTION_EXECUTION"""

  GUILD_MESSAGE_POLLS: int = 1 << 24
  """- MESSAGE_POLL_VOTE_ADD
  - MESSAGE_POLL_VOTE_REMOVE
  """

  DIRECT_MESSAGE_POLLS: int = 1 << 25
  """- MESSAGE_POLL_VOTE_ADD
  - MESSAGE_POLL_VOTE_REMOVE
  """

  @classmethod
  def default(cls) -> Self:
    """Returns a set of gateway intents containing but the privileged intents."""
    value: Self = cls.none()
    for member in cls:
      if member in [cls.GUILD_PRESENCES, cls.GUILD_MEMBERS, cls.MESSAGE_CONTENT]: continue
      value |= member
    return value

  @classmethod
  def none(cls) -> Self:
    """Returns an instance with no gateway intent enabled"""
    return cls(0)


@unique
class GuildMemberFlag(IntFlag):
  DID_REJOIN: int = 1 << 0
  """Member has left and rejoined the guild.

  **Editable**: ``False``
  """

  COMPLETED_ONBOARDING: int = 1 << 1
  """Member has completed onboarding.

  **Editable**: ``False``
  """

  BYPASSES_VERIFICATION: int = 1 << 2
  """Member is exempt from guild verification requirements.

  **Editable**: ``True``

  .. hint::
      Allows a member who does not meet verification requirements to participate in a server.
  """

  STARTED_ONBOARDING: int = 1 << 3
  """Member has started onboarding.

  **Editable**: ``False``
  """

  IS_GUEST: int = 1 << 4
  """Member is a guest and can only access the voice channel they were invited to.

  **Editable**: ``False``
  """

  STARTED_HOME_ACTIONS: int = 1 << 5
  """Member has started Server Guide new member actions.

  **Editable**: ``False``
  """

  COMPLETED_HOME_ACTIONS: int = 1 << 6
  """Member has completed Server Guide new member actions.

  **Editable**: ``False``
  """

  AUTOMOD_QUARANTINED_USERNAME: str = 1 << 7
  """Member's username, display name, or nickname is blocked by AutoMod.

  **Editable**: ``False``
  """

  DM_SETTINGS_UPSELL_ACKNOWLEDGED: int = 1 << 9
  """Member has dismissed the DM settings upsell.

  **Editable**: ``False``
  """

  AUTOMOD_QUARANTINED_GUILD_TAG: int = 1 << 10
  """Member's guild tag is blocked by AutoMod.

  **Editable**: ``False``
  """


@unique
class PermissionFlag(IntFlag):
  """Represents a set of permission flags"""

  CREATE_INSTANT_INVITE: int = 1 << 0
  """Allows creation of instant invites"""

  KICK_MEMBERS: int = 1 << 1
  """Allows kicking members.
  
  .. attention::
     This permission requires the owner account to use two-factor authentication when used on a guild that has server-wide 2FA enabled.
  """

  BAN_MEMBERS: int = 1 << 2
  """Allows banning members.

  .. attention::
     This permission requires the owner account to use two-factor authentication when used on a guild that has server-wide 2FA enabled.
  """

  ADMINISTRATOR: int = 1 << 3
  """Allows all permission and bypasses channel permission overwrites.

  .. attention::
     This permission requires the owner account to use two-factor authentication when used on a guild that has server-wide 2FA enabled.
  """

  MANAGE_CHANNELS: int = 1 << 4
  """Allows management and editing of channels.

  .. attention::
     This permission requires the owner account to use two-factor authentication when used on a guild that has server-wide 2FA enabled.
  """

  MANAGE_GUILD: int = 1 << 5
  """Allows management and editing of the guild.

  .. attention::
     This permission requires the owner account to use two-factor authentication when used on a guild that has server-wide 2FA enabled.
  """

  ADD_REACTIONS: int = 1 << 6
  """Allows for adding new reactions to messages. This permission does not apply to reacting with an existing reaction on a message."""

  VIEW_AUDIT_LOG: int = 1 << 7
  """Allows for viewing of audit logs"""

  PRIORITY_SPEAKER: int = 1 << 8
  """Allows for using priority speaker in a voice channel"""

  STREAM: int = 1 << 9
  """Allows the user to go live"""

  VIEW_CHANNEL: int = 1 << 10
  """Allows guild members to view a channel, which includes reading messages in text channels and joining voice channels"""

  SEND_MESSAGES: int = 1 << 11
  """Allows for sending messages in a channel and creating threads in a forum (does not allow sending messages in threads)"""

  SEND_TTS_MESSAGES: int = 1 << 12
  """Allows for sending of ``/tts`` messages"""

  MANAGE_MESSAGES: int = 1 << 13
  """Allows for deletion of other users messages.

  .. attention::
     This permission requires the owner account to use two-factor authentication when used on a guild that has server-wide 2FA enabled.
  """

  EMBED_LINKS: int = 1 << 14
  """Links sent by users with this permission will be auto-embedded"""

  ATTACH_FILES: int = 1 << 15
  """Allows for uploading images and files"""

  READ_MESSAGE_HISTORY: int = 1 << 16
  """Allows for reading of message history"""

  MENTION_EVERYONE: int = 1 << 17
  """Allows for using the ``@everyone`` tag to notify all users in a channel, and the ``@here`` tag to notify all online users in a channel"""

  USE_EXTERNAL_EMOJIS: int = 1 << 18
  """Allows the usage of custom emojis from other servers"""

  VIEW_GUILD_INSIGHTS: int = 1 << 19
  """Allows for viewing guild insights"""

  CONNECT: int = 1 << 20
  """Allows for joining of a voice channel"""

  SPEAK: int = 1 << 21
  """Allows for speaking in a voice channel"""

  MUTE_MEMBERS: int = 1 << 22
  """Allows for muting members in a voice channel"""

  DEAFEN_MEMBERS: int = 1 << 23
  """Allows for deafening of members in a voice channel"""

  MOVE_MEMBERS: int = 1 << 24
  """Allows for moving of members between voice channels"""

  USE_VAD: int = 1 << 25
  """Allows for using voice-activity-detection in a voice channel"""

  CHANGE_NICKNAME: int = 1 << 26
  """Allows for modification of own nickname"""

  MANAGE_NICKNAMES: int = 1 << 27
  """Allows for modification of other users nicknames"""

  MANAGE_ROLES: int = 1 << 28
  """Allows management and editing of roles.

  .. attention::
     This permission requires the owner account to use two-factor authentication when used on a guild that has server-wide 2FA enabled.
  """

  MANAGE_WEBHOOKS: int = 1 << 29
  """Allows management and editing of webhooks.

  .. attention::
     This permission requires the owner account to use two-factor authentication when used on a guild that has server-wide 2FA enabled.
  """

  MANAGE_GUILD_EXPRESSIONS: int = 1 << 30
  """Allows for editing and deleting emojis, stickers, and soundboard sounds created by all users.
  
  .. attention::
     This permission requires the owner account to use two-factor authentication when used on a guild that has server-wide 2FA enabled.
  """

  USE_APPLICATION_COMMANDS: int = 1 << 31
  """Allows members to use application commands, including slash commands and context menu commands"""

  REQUEST_TO_SPEAK: int = 1 << 32
  """Allows for requesting to speak in stage channels"""

  MANAGE_EVENTS: int = 1 << 33
  """Allows for editing and deleting scheduled events created by all users"""

  MANAGE_THREADS: int = 1 << 34
  """Allows for deleting and archiving threads, and viewing all private threads.

  .. attention::
     This permission requires the owner account to use two-factor authentication when used on a guild that has server-wide 2FA enabled.
  """

  CREATE_PUBLIC_THREADS: int = 1 << 35
  """Allows for creating public and announcement threads"""

  CREATE_PRIVATE_THREADS: int = 1 << 36
  """Allows for creating private threads"""

  USE_EXTERNAL_STICKERS: int = 1 << 37
  """Allows the usage of custom stickers from other servers"""

  SEND_MESSAGES_IN_THREADS: int = 1 << 38
  """Allows for sending messages in threads"""

  USE_EMBEDDED_ACTIVITIES: int = 1 << 39
  """Allows for using Activities (applications with the ``EMBEDDED`` flag)"""

  MODERATE_MEMBERS: int = 1 << 40
  """Allows for timing out users to prevent them from sending or reacting to messages in chat and threads, and speaking in voice and stage channels"""

  VIEW_CREATOR_MONETIZATION_ANALYTICS: int = 1 << 41
  """Allows for viewing role subscription insights.
  
  .. attention::
     This permission requires the owner account to use two-factor authentication when used on a guild that has server-wide 2FA enabled.
  """

  USE_SOUNDBOARD: int = 1 << 42
  """Allows for using sondboard in a voice channel"""

  CREATE_GUILD_EXPRESSIONS: int = 1 << 43
  """Allows for creating emojis, stickers, and soundboard sounds, and editing and deleting those created by the current users"""

  CREATE_EVENTS: int = 1 << 44
  """Allows for creating scheduled events, and editing and deleting those created by the current user"""

  USE_EXTERNAL_SOUNDS: int = 1 << 45
  """Allows the usage of custom soundboard sounds from other servers"""

  SEND_VOICE_MESSAGES: int = 1 << 46
  """Allows sending voice messages"""

  SET_VOICE_CHANNEL_STATUS: int = 1 << 48
  """Allows setting voice channel status"""

  SEND_POLLS: int = 1 << 49
  """Allows sending polls"""

  USE_EXTERNAL_APPS: int = 1 << 50
  """Allows user-installed apps to send public responses. When disabled, users will still be allowed to use their apps but the responses will be ephemeral. This only applies to apps not also installed to the server"""

  PIN_MESSAGES: int = 1 << 51
  """Allows pinning and unpinning messages"""

  BYPASS_SLOWMODE: int = 1 << 52
  """Allows bypassing slowmode restrictions"""


@unique
class RoleFlag(IntFlag):
   IN_PROMPT: int = 1 << 0
   """Role can be selected by members in an onboarding prompt"""


@unique
class SystemChannelFlag(IntFlag):
   SUPPRESS_JOIN_NOTIFICATIONS: int = 1 << 0
   """Suppress member join notifications"""

   SUPPRESS_PREMIUM_SUBSCRIPTIONS: int = 1 << 1
   """Suppress server boost notifications"""

   SUPPRESS_GUILD_REMINDER_NOTIFICATIONS: int = 1 << 2
   """Suppress server setup tips"""

   SUPPRESS_JOIN_NOTIFICATION_REPLIES: int = 1 << 3
   """Hide member join sticker reply buttons"""

   SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATIONS: int = 1 << 4
   """Suppress role subscription purchase and renewal notifications"""

   SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATION_REPLIES: int = 1 << 5
   """Hide role subscription sticker reply buttons"""


@unique
class UserFlag(IntFlag):
   STAFF: int = 1 << 0
   """Discord Employee"""

   PARTNER: int = 1 << 1
   """Partnered Server Owner"""

   HYPESQUAD: int = 1 << 2
   """HypeSquad Events Member"""

   BUG_HUNTER_LEVEL_1: int = 1 << 3
   """Bug Hunter Level 1"""

   HYPESQUAD_ONLINE_HOUSE_1: int = 1 << 6
   """House Bravery Member"""

   HYPESQUAD_ONLINE_HOUSE_2: int = 1 << 7
   """House Brilliance Member"""

   HYPESQUAD_ONLINE_HOUSE_3: int = 1 << 8
   """House Balance Member"""

   PREMIUM_EARLY_SUPPORTER: int = 1 << 9
   """Early Nitro Supporter"""

   TEAM_PSEUDO_USER: int = 1 << 10
   """User is a team"""

   BUG_HUNTER_LEVEL_2: int = 1 << 14
   """Bug Hunter Level 2"""

   VERIFIED_BOT: int = 1 << 16
   """Verified Bot"""

   VERIFIED_DEVELOPER: int = 1 << 17
   """Early Verified Bot Developer"""

   CERTIFIED_MODERATOR: int = 1 << 18
   """Moderator Programs Alumni"""

   BOT_HTTP_INTERACTIONS: int = 1 << 19
   """Bot uses only HTTP interactions and is shown in the online member list"""