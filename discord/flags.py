from enum import IntFlag, unique


@unique
class GatewayIntent(IntFlag):
  """Represents a set of Gateway intents.

  .. note::
     \* **Thread Members Update** contains different data depending on which intents are used.
     \*\* Events under the :attr:```~.GUILD_PRESENCES``` and :attr:```~.GUILD_MEMBERS``` intents are **turned off by default on all API versions**. If you are using **API v6**, you will receive those events if you are authorized to receive them and have enabled the intents in the `Developer Portal`_. You do not need to use intents on API v6 to receive these events; you just need to enable the flags. If you are using **API v8 or above**, intents are mandatory and must be specified when identifying.
     \*\*\* :attr:```~.MESSAGE_CONTENT``` does not represent individual events, but rather affects what data is present for events that could contain message content fields.

  .. _Developer Portal: https://discord.com/developers/applications
  """

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