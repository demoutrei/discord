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


``READY``
~~~~~~~~~

Dispatched when the client has completed the initial handshake with the gateway (for new sessions).

.. autoclass:: discord.events.ReadyEvent()