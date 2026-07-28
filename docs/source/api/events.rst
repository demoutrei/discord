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


``READY``
~~~~~~~~~

Dispatched when the client has completed the initial handshake with the gateway (for new sessions).

.. autoclass:: discord.events.ReadyEvent()


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