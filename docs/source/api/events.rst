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


``CHANNEL_UPDATE``
~~~~~~~~~~~~~~~~~~

Received when a channel is updated. The inner payload is a :class:`~discord.objects.Channel` object. This is not sent when the :attr:`~discord.objects.Channel.last_message_id` field is altered. To keep track of the :attr:`~discord.objects.Channel.last_message_id` changes, you must listen for ``MESSAGE_CREATE`` events (or ``THREAD_CREATE`` events for :attr:`~discord.enums.ChannelType.GUILD_FORUM` and :attr:`~discord.enums.ChannelType.GUILD_MEDIA` channels).

.. note::
    This event may reference roles or guild members that no longer exist in the guild.


``READY``
~~~~~~~~~

Dispatched when the client has completed the initial handshake with the gateway (for new sessions).

.. autoclass:: discord.events.ReadyEvent()


``VOICE_CHANNEL_START_TIME_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when the voice channel start time changes.

.. autoclass:: discord.events.VoiceChannelStartTimeUpdateEvent()


``VOICE_CHANNEL_STATUS_UPDATE``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Received when the voice channel status changes.

.. autoclass:: discord.events.VoiceChannelStatusUpdateEvent()