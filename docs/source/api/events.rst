.. _event-reference:


Event Reference
===============

Events are received in listeners using :meth:`~discord.Client.event_listener`.

Event names are case-sensitive and uses underscores (``_``) for spaces.


``APPLICATION_COMMAND_PERMISSIONS_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when an application command's permissions are updated. The inner payload is an :class:`~discord.objects.GuildApplicationCommandPermissions` object.


``AUTO_MODERATION_ACTION_EXECUTION``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a rule is triggered and an action is executed (e.g. when a message is blocked).

.. autoclass:: discord.events.AutoModerationActionExecutionEvent()


``AUTO_MODERATION_RULE_CREATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a rule is created. The inner payload is an :class:`~discord.objects.AutoModerationRule` object.


``AUTO_MODERATION_RULE_DELETE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a rule is deleted. The inner payload is an :class:`~discord.objects.AutoModerationRule` object.


``AUTO_MODERATION_RULE_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a rule is updated. The inner payload is an :class:`~discord.objects.AutoModerationRule` object.


``CHANNEL_CREATE``
~~~~~~~~~~~~~~~~~~

Received when a new guild channel is created, relevant to the current user. The inner payload is a :class:`~discord.objects.Channel` object.


``CHANNEL_DELETE``
~~~~~~~~~~~~~~~~~~

Received when a channel relevant to the current user is deleted. The inner payload is a :class:`~discord.objects.Channel` object.


``CHANNEL_INFO``
~~~~~~~~~~~~~~~~

Includes ephemeral data for channels in a guild. Received in response to :meth:`~discord.gateway.DiscordWebSocket.request_channel_info`.

.. autoclass:: discord.events.ChannelInfoEvent()


``CHANNEL_PINS_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~

Received when a message is pinned or unpinned in a text channel. This is not sent when a pinned message is deleted.

.. autoclass:: discord.events.ChannelPinsUpdateEvent()


``CHANNEL_UPDATE``
~~~~~~~~~~~~~~~~~~

Received when a channel is updated. The inner payload is a :class:`~discord.objects.Channel` object. This is not sent when the :attr:`~discord.objects.Channel.last_message_id` field is altered. To keep track of the :attr:`~discord.objects.Channel.last_message_id` changes, you must listen for ``MESSAGE_CREATE`` events (or ``THREAD_CREATE`` events for :attr:`~discord.enums.ChannelType.GUILD_FORUM` and :attr:`~discord.enums.ChannelType.GUILD_MEDIA` channels).

.. note::
    This event may reference roles or guild members that no longer exist in the guild.


``ENTITLEMENT_CREATE``
~~~~~~~~~~~~~~~~~~~~~~

Received when an entitlement is created. The inner payload is an :class:`~discord.objects.Entitlement` object.


``ENTITLEMENT_DELETE``
~~~~~~~~~~~~~~~~~~~~~~

Received when an entitlement is deleted. The inner payload is an :class:`~discord.objects.Entitlement` object.

Entitlement deletions are infrequent, and occur when:

- Discord issues a refund for a subscription
- Discord removes an entitlement from a user via internal tooling
- Discord deletes an app-managed entitlement they created via the API


``ENTITLEMENT_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~

Received when an entitlement is updated. The inner payload is an :class:`~discord.objects.Entitlement` object.

For subscription entitlements, this event is triggered only when a user's subscription ends, providing an :attr:`~discord.objects.Entitlement.ends_at` timestamp that indicates the end of the entitlement.


``GUILD_AUDIT_LOG_ENTRY_CREATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a guild audit log entry is created. The inner payload is an :class:`~discord.events.GuildAuditLogEntryCreateEvent` object. This event is only sent to bots with the :attr:`~discord.flags.PermissionFlag.VIEW_AUDIT_LOG` permission.

.. autoclass:: discord.events.GuildAuditLogEntryCreateEvent()


``GUILD_BAN_ADD``
~~~~~~~~~~~~~~~~~

Received when a user is banned from a guild. This event is only sent to bots with the :attr:`~discord.flags.PermissionFlag.BAN_MEMBERS` or :attr:`~discord.flags.PermissionFlag.VIEW_AUDIT_LOG` permission.

.. autoclass:: discord.events.GuildBanAddEvent()


``GUILD_BAN_REMOVE``
~~~~~~~~~~~~~~~~~~~~

Received when a user is unbanned from a guild. This event is only sent to bots with the :attr:`~discord.flags.PermissionFlag.BAN_MEMBERS` or :attr:`~discord.flags.PermissionFlag.VIEW_AUDIT_LOG` permission.

.. autoclass:: discord.events.GuildBanRemoveEvent()


``GUILD_CREATE``
~~~~~~~~~~~~~~~~

This event can be received in three different scenarios:

1. When a user is initially connecting, to lazily load and backfill information for all unavailable guilds sent in ``READY`` event. Guilds that are unavailable due to an outage will send a ``GUILD_DELETE`` event.
2. When a Guild becomes available again to the client.
3. When the current user joins a new Guild.

.. note::
    During an outage, the guild object in scenarios 1 and 3 may be marked as unavailable.

.. warning::
    If your bot does not have the :attr:`~discord.flags.GatewayIntent.GUILD_PRESENCES`, or if the guild has over 75k members, members and presences returned in this event will only contain your bot and users in voice channels.

.. autoclass:: discord.events.GuildCreateEvent()


``GUILD_DELETE``
~~~~~~~~~~~~~~~~

Received when a guild becomes or was already unavailable due to an outage, or when the user leaves or is removed from a guild. The inner payload is an :class:`~discord.objects.UnavailableGuild` object. If the :attr:`~discord.objects.UnavailableGuild.unavailable` is not set, the user was removed from the guild.


``GUILD_EMOJIS_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~

Received when a guild's emojis have been updated.

.. autoclass:: discord.events.GuildEmojisUpdateEvent()


``GUILD_INTEGRATIONS_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a guild integration is updated.

.. autoclass:: discord.events.GuildIntegrationsUpdateEvent()


``GUILD_MEMBER_ADD``
~~~~~~~~~~~~~~~~~~~~

Received when a user joins a guild. This event may also be sent for users who are already members of the guild.

.. important::
    If using gateway intents, the :attr:`~discord.flags.GatewayIntent.GUILD_MEMBERS` intent will be required to receive this event.

.. autoclass:: discord.events.GuildMemberAddEvent()


``GUILD_MEMBER_REMOVE``
~~~~~~~~~~~~~~~~~~~~~~~

Received when a user is removed from a guild (leave/kick/ban).

.. important::
    If using gateway intents, the :attr:`~discord.flags.GatewayIntent.GUILD_MEMBERS` intent will be required to receive this event.

.. autoclass:: discord.events.GuildMemberRemoveEvent()


``GUILD_MEMBER_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~

Received when a guild member is updated. This will also fire when the user object of a guild member changes.

.. autoclass:: discord.events.GuildMemberUpdateEvent()


``GUILD_MEMBERS_CHUNK``
~~~~~~~~~~~~~~~~~~~~~~~

Received in response to ``Guild Request Members``. You can use the :attr:`~discord.events.GuildMembersChunkEvent.chunk_index` and :attr:`~discord.events.GuildMembersChunkEvent.chunk_count` to calculate how many chunks are left for your request.

.. autoclass:: discord.events.GuildMembersChunkEvent()


``GUILD_ROLE_CREATE``
~~~~~~~~~~~~~~~~~~~~~

Received when a guild role is created.

.. autoclass:: discord.events.GuildRoleCreateEvent()


``GUILD_ROLE_DELETE``
~~~~~~~~~~~~~~~~~~~~~

Received when a guild role is deleted.

.. autoclass:: discord.events.GuildRoleDeleteEvent()


``GUILD_ROLE_UPDATE``
~~~~~~~~~~~~~~~~~~~~~

Received when a guild role is updated.

.. autoclass:: discord.events.GuildRoleUpdateEvent()


``GUILD_SCHEDULED_EVENT_CREATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a guild scheduled event is created. The inner payload is a :class:`~discord.objects.GuildScheduledEvent` object.


``GUILD_SCHEDULED_EVENT_DELETE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a guild scheduled event is deleted. The inner payload is a :class:`~discord.objects.GuildScheduledEvent` object.


``GUILD_SCHEDULED_EVENT_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a guild scheduled event is updated. The inner payload is a :class:`~discord.objects.GuildScheduledEvent` object.


``GUILD_SCHEDULED_EVENT_USER_ADD``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a user has subscribed to a guild scheduled event.

.. autoclass:: discord.events.GuildScheduledEventUserAddEvent()


``GUILD_SCHEDULED_EVENT_USER_REMOVE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a user has unsubscribed from a guild scheduled event.

.. autoclass:: discord.events.GuildScheduledEventUserRemoveEvent()


``GUILD_SOUNDBOARD_SOUND_CREATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a guild soundboard sound is created. The inner payload is a :class:`~discord.objects.SoundboardSound` object.


``GUILD_SOUNDBOARD_SOUND_DELETE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a guild soundboard sound is deleted.

.. autoclass:: discord.events.GuildSoundboardSoundDeleteEvent()


``GUILD_SOUNDBOARD_SOUND_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a guild soundboard sound is updated. The inner payload is a :class:`~discord.objects.SoundboardSound` object.


``GUILD_SOUNDBOARD_SOUNDS_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when multiple guild soundboard sounds are updated.

.. autoclass:: discord.events.GuildSoundboardSoundsUpdateEvent()


``GUILD_STICKERS_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~~~

Received when a guild's stickers have been updated.

.. autoclass:: discord.events.GuildStickersUpdateEvent()


``GUILD_UPDATE``
~~~~~~~~~~~~~~~~

Received when a guild is updated. The inner payload is a :class:`~discord.objects.Guild` object.


``PRESENCE_UPDATE``
~~~~~~~~~~~~~~~~~~~

A user's presence is their current state on a guild. This event is sent when a user's presence or info, such as name or avatar, is updated.

.. important::
    If you are using Gateway Intents, you *must* specify the :attr:`~discord.flags.GatewayIntent.GUILD_PRESENCES` intent in order to receive the Presence Update events.

.. important::
    The user object within this event can be partial, the only field which must be sent is the :attr:`~.discord.objects.User.id`, everything else is optional. Along with this limitation, no fields are required, and the types of the fields are not validated. Your client should expect any combination of fields and types within this event.

.. autoclass:: discord.events.PresenceUpdateEvent()


``READY``
~~~~~~~~~

Dispatched when the client has completed the initial handshake with the gateway (for new sessions).

.. autoclass:: discord.events.ReadyEvent()


``SOUNDBOARD_SOUNDS``
~~~~~~~~~~~~~~~~~~~~~

Includes a guild's list of soundboard sounds. Received in response to ``Request Soundboard Sounds``.

.. autoclass:: discord.events.SoundboardSoundsEvent()


``THREAD_CREATE``
~~~~~~~~~~~~~~~~~

Received when a thread is created, relevant to the current user, or when the current user is added to a thread. The inner payload is a :class:`~discord.objects.Channel` object.

- When a thread is created, includes an additional :attr:`~discord.events.ThreadCreateEvent.newly_created` boolean field.
- When being added to an existing private thread, includes a :attr:`~discord.objects.Channel.member` object.

.. py:class:: discord.events.ThreadCreateEvent()

  .. py:attribute:: newly_created
    :type: ~discord.utils.Optional[bool]


``THREAD_DELETE``
~~~~~~~~~~~~~~~~~

Received when a thread relevant to the current user is deleted. The inner payload is a subset of the :class:`~discord.objects.Channel` object, containing just the :attr:`~discord.objects.Channel.id`, :attr:`~discord.objects.Channel.guild_id`, :attr:`~discord.objects.Channel.parent_id`, and :attr:`~discord.objects.Channel.type` fields.


``THREAD_LIST_SYNC``
~~~~~~~~~~~~~~~~~~~~

Received when the current user *gains* access to a channel.

.. autoclass:: discord.events.ThreadListSyncEvent()


``THREAD_MEMBERS_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~~~

Received when anyone is added to or removed from a thread. If the current user does not have the :attr:`~discord.flags.GatewayIntent.GUILD_MEMBERS` gateway intent, then this event will only be sent if the current user was added to or removed from the thread.

.. autoclass:: discord.events.ThreadMembersUpdateEvent()


``THREAD_UPDATE``
~~~~~~~~~~~~~~~~~

Received when a thread is updated. The inner payload is a :class:`~discord.objects.Channel` object. This is not sent when the :attr:`~discord.objects.Channel.last_message_id` is altered. To keep track of the :attr:`~discord.objects.Channel.last_message_id` changes, you must listen for ``MESSAGE_CREATE`` events.


``VOICE_CHANNEL_START_TIME_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when the voice channel start time changes.

.. autoclass:: discord.events.VoiceChannelStartTimeUpdateEvent()


``VOICE_CHANNEL_STATUS_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when the voice channel status changes.

.. autoclass:: discord.events.VoiceChannelStatusUpdateEvent()