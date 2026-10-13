Changelog
=========


v26.0.3
+++++++


Custom Dataclass Rewritten
^^^^^^^^^^^^^^^^^^^^^^^^^^

Object attributes now utilize the ``@property`` factory decorator. Raw data of an object is stored in the ``__dict__`` attribute.


New Partial Type
^^^^^^^^^^^^^^^^

A new ``Partial`` type is implemented. When applied on an object, missing fields will always return :data:`discord.types.MISSING`.

.. code-block:: python

    @dataclass
    class Object:
      @property
      def field(self) -> bool:
        return self.__dict__["field"]

    object_: Partial[Object] = Partial[Object]()
    print(f"{object_.field = }") # MISSING


Added Methods
^^^^^^^^^^^^^

- :meth:`GatewayEvent.REQUEST_GUILD_MEMBERS() <discord.gateway.GatewayEvent.REQUEST_GUILD_MEMBERS>`
- :meth:`GatewayEvent.REQUEST_SOUNDBOARD_SOUNDS() <discord.gateway.GatewayEvent.REQUEST_SOUNDBOARD_SOUNDS>`
- :meth:`GatewayEvent.REQUEST_CHANNEL_INFO() <discord.gateway.GatewayEvent.REQUEST_CHANNEL_INFO>`


v26.0.2
+++++++

- Completed :meth:`GatewayEvent.IDENTIFY() <discord.gateway.GatewayEvent.IDENTIFY>`.
- Added :class:`~discord.flags.GatewayCapabilities`.
- Added :meth:`GatewayEvent.PRESENCE_UPDATE() <discord.gateway.GatewayEvent.PRESENCE_UPDATE>`.
- Added :class:`~discord.enums.StatusType`.
- Added :class:`~discord.objects.Activity`.
- Moved :class:`~discord.enums.ActivityType` documentation.
- Moved :class:`~discord.enums.StatusDisplayType` documentation.
- Added :class:`~discord.objects.ActivityTimestamps`.
- Added :class:`~discord.objects.ActivityEmoji`.
- Added :class:`~discord.objects.ActivityParty`.
- Added :class:`~discord.objects.ActivityAssets`.
- Added :class:`~discord.objects.ActivitySecrets`.
- Moved :class:`~discord.flags.ActivityFlags` documentation.
- Added :class:`~discord.objects.ActivityButton`.
- Moved documentations: :class:`~discord.flags.GatewayCapabilities`, :class:`~discord.flags.GatewayIntents`.


v26.0.1
+++++++

**Documentation Changes**

- Added Changelog.


v26.0.0
+++++++

**Added Changes**

- Modified :class:`~discord.gateway.DiscordWebSocket` and :class:`~discord.http.HTTPClient` functionalities.