Prerequisite
============

.. attention::

    This assumes you already have the package installed.

First, you must connect to the Discord API. There are two ways that you can connect: through HTTPS, which the library handles for you; and the gateway, which you have to handle yourself.

**Prerequisites**:

- A Discord application. *See also:* `How Do I Create an Application?`_.

- Python of version 3.14 or above installed.

- A ``.env`` file.


Configuring Environment Variables
+++++++++++++++++++++++++++++++++

You don't have to load your dotenv files as the library does it for you. All that there is for you to do is configure it.

**Importantly**, you must have an environment variable named ``APPLICATION_TOKEN`` with a value of your Discord application's bot token.

.. code:: text

    APPLICATION_TOKEN=...

.. tip::

    Environment variables are accessible through the :attr:`Client.env <discord.Client.env>` property.

.. attention::

    Do **NOT** publicly expose your application token or hand it to just anyone---store it in a secured place.

.. seealso::

    `How Do I Get A Bot Token?`_


Connecting to Gateway
+++++++++++++++++++++

First, you must set up your :class:`~discord.Client` class and :class:`~discord.gateway.DiscordWebSocket` subclass.

.. note::

    If you wish to not connect to the Gateway API, then pass ``gateway_cls = None`` as an argument.

.. code:: python

    from discord import Client
    from discord.gateway import DiscordWebSocket, GatewayEvent

    class Default(DiscordWebSocket):
      ...

    client = Client(gateway_cls = Default)
    client.connect()

To initially connect to the Gateway API, you must fetch the WSS URL from the :attr:`HTTPClient.get_gateway() <discord.http.HTTPClient.get_gateway>` endpoint and cache it.

.. code:: python

    from discord.gateway import DiscordWebSocket
    from discord.logging import Logger

    class Default(DiscordWebSocket):
      async def setup(self) -> None:
        async with await self.client.http.get_gateway() as response:
          url: str = response["url"]
          with Logger.debug(f"Cached WSS URL: {url}"):
            self.client.env.WSS_URL: str = url
        await self.connect(f"{self.client.env.WSS_URL}/?v=10&encoding=json")


Hello OpCode
^^^^^^^^^^^^

Upon initiating a connection through the WSS URL, Discord sends an :attr:`OpCode.HELLO <discord.enums.OpCode.HELLO>` event containing a heartbeat interval in milliseconds. You must begin handling heartbeats and send a :meth:`GatewayEvent.IDENTIFY() <discord.gateway.GatewayEvent.IDENTIFY>` payload.


Heartbeats
~~~~~~~~~~

Heartbeats are used to maintain an active gateway connection. Upon receiving the :attr:`OpCode.HELLO <discord.enums.OpCode.HELLO>` event, your app should wait ``heartbeat_interval * jitter`` where ``jitter`` is any random value between ``0`` and ``1``, then send its first :meth:`GatewayEvent.HEARTBEAT() <discord.gateway.GatewayEvent.HEARTBEAT>` event. From that point until the connection is closed, your app must continually send a heartbeat every ``heartbeat_interval`` milliseconds. If your app fails to send a heartbeat event in time, your connection will be closed and you will be forced to resume.

When sending a heartbeat, your app will need to include the last sequence number your app received.

.. code:: python

    from discord.gateway import DiscordWebSocket, GatewayEvent
    import asyncio, random

    class Default(DiscordWebSocket):
      async def on_hello(self, event: GatewayEvent) -> None:
        await asyncio.sleep(event.d["heartbeat_interval"] * random.random())
        await self.send(
          GatewayEvent.HEARTBEAT(self.last_sequence)
        )
        self.keep_alive(interval = event.d["heartbeat_interval"])

When you send a :meth:`GatewayEvent.HEARTBEAT() <discord.gateway.GatewayEvent.HEARTBEAT>` event, Discord will response with a :attr:`OpCode.HEARTBEAT_ACK <discord.enums.OpCode.HEARTBEAT_ACK>` event, which is an acknowledgement that the heartbeat was received.

If the client does not receive a heartbeat ack between its attempts at sending heartbeats, this may be due to a failed or "zombied" connection. The client should immediately terminate the connection with any close code besides ``1000`` or ``1001``, then reconnect and attempt to resume.

In addition to the heartbeat interval, Discord may request additional heartbeats from your app by sending a :attr:`OpCode.HEARTBEAT <discord.enums.OpCode.HEARTBEAT>` event. Upon receiving the event, your app should immediately send back another :meth:`GatewayEvent.HEARTBEAT() <discord.gateway.GatewayEvent.HEARTBEAT>` event without waiting the remainder of the current interval.

.. code:: python

    from discord.gateway import DiscordWebSocket, GatewayEvent

    class Default(DiscordWebSocket):
      async def on_heartbeat(self, event: GatewayEvent) -> None:
        await self.send(GatewayEvent.HEARTBEAT(self.last_sequence))


Identifying
~~~~~~~~~~~

After the connection is open and your app is sending heartbeats, you should send a :meth:`GatewayEvent.IDENTIFY() <discord.gateway.GatewayEvent.IDENTIFY>` event. The :attr:`OpCode.IDENTIFY <discord.enums.OpCode.IDENTIFY>` event is an initial handshake with the Gateway that's required before your app can begin sending or receiving most Gateway events.

.. code:: python

    from discord.gateway import DiscordWebSocket, GatewayEvent

    class Default(DiscordWebSocket):
      async def on_hello(self, event: GatewayEvent) -> None:
        await self.send(GatewayEvent.IDENTIFY(
          intents = GatewayIntents.default(),
          token = self.client.env.APPLICATION_TOKEN
        ))

After your app sends a valid :attr:`OpCode.IDENTIFY <discord.enums.OpCode.IDENTIFY>` payload, Discord will respond with a :class:`~discord.gateway.events.ReadyEvent` which indicates that your app is in a successfully connected state with the Gateway.


Ready Event
^^^^^^^^^^^

The :class:`~discord.gateway.events.ReadyEvent` is sent to your app after it sends a valid :meth:`GatewayEvent.IDENTIFY() <discord.gateway.GatewayEvent.IDENTIFY>` payload.

The :class:`~discord.gateway.events.ReadyEvent` includes fields that you'll need to cache in order to eventually resume your connection after disconnects:

- :attr:`ReadyEvent.resume_gateway_url <discord.gateway.events.ReadyEvent.resume_gateway_url>` is a WebSocket URL that your app should use when it resumes after a disconnect. The :attr:`ReadyEvent.resume_gateway_url <discord.gateway.events.ReadyEvent.resume_gateway_url>` should be used instead of the URL used when connecting.

- :attr:`ReadyEvent.session_id <discord.gateway.events.ReadyEvent.session_id>` is the ID for the Gateway session for the new connection. It's required to know which stream of events were associated with your disconnection.

.. code:: python

    from discord import Client
    from discord.gateway import DiscordWebSocket
    from discord.gateway.events import ReadyEvent
    from discord.logging import Logger

    class Default(DiscordWebSocket): ...

    client: Client = Client(gateway_cls = Default)

    @client.socket.dispatch("READY")
    async def _(client: Client, event: ReadyEvent) -> None:
      client.env.RESUME_GATEWAY_URL: str = event.resume_gateway_url
      client.env.SESSION_ID: str = event.session_id
      Logger.info("App is ready.")

    client.connect()


Disconnecting
+++++++++++++

Gateway disconnects happen for a variety of reasons, and may be initiated by Discord or by your app.


Handling a Disconnect
^^^^^^^^^^^^^^^^^^^^^

When your app encounters a disconnect, it will typically be sent a close code which can be used to determine whether you can reconnect and resume the session, or whether you have to start over and re-identify.

After you determine whether or not your app can reconnect, you will do one of the following:

- If you determine that your app *can* reconnect and resume the previous session, then you should reconnect using the :attr:`ReadyEvent.resume_gateway_url <discord.gateway.events.ReadyEvent.resume_gateway_url>` and :attr:`ReadyEvent.session_id <discord.gateway.events.ReadyEvent.session_id>`.

- If you *cannot* reconnect or the reconnect fails, you should open a new connection using the URL from the initial call to :meth:`HTTPClient.get_gateway() <discord.http.HTTPClient.get_gateway>` or :meth:`HTTPClient.get_gateway_bot() <discord.http.HTTPClient.get_gateway_bot>`. In the case you cannot reconnect, you'll have to re-identify after opening a new connection.


Initiating a Disconnect
^^^^^^^^^^^^^^^^^^^^^^^

When you close the connection to the gateway with close code ``1000`` or ``1001``, your session will be invalidated and your bot will appear offline.

If you simply close the TCP connection or use a different close code, the session will remain active and timeout after a few minutes. This can be useful when you're resuming the previous session.


Resuming
++++++++

When your app is disconnected, Discord has a process for reconnecting and resuming. After resuming, your app will receive the missed events in the same way it would have had the connection had stayed active. Unlike the initial connection, your app does **not** need to re-identify when resuming.

There are a handful of scenarios when your app should attempt to resume:

1. It receives an :attr:`OpCode.RECONNECT <discord.enums.OpCode.RECONNECT>`.

2. It's disconnected with a close code that indicates it can reconnect.

3. It's disconnected but doesn't receive *any* close code.

4. It receives an :attr:`OpCode.INVALID_SESSION <discord.enums.OpCode.INVALID_SESSION>` with the :attr:`GatewayEvent.d <discord.gateway.GatewayEvent.d>` field set to ``True``. This is an unlikely scenario, but it is possible.


Preparing to Resume
^^^^^^^^^^^^^^^^^^^

Before your app can send a :meth:`GatewayEvent.RESUME() <discord.gateway.GatewayEvent.RESUME>`, it will need three values: the :attr:`ReadyEvent.session_id <discord.gateway.events.ReadyEvent.session_id>` and the :attr:`ReadyEvent.resume_gateway_url <discord.gateway.events.ReadyEvent.resume_gateway_url>`, and the sequence number (:attr:`GatewayEvent.s <discord.gateway.GatewayEvent.s>`) from the last :attr:`OpCode.DISPATCH <discord.enums.OpCode.DISPATCH>` event it received before the disconnect.

.. code:: python

    from discord import Client
    from discord.gateway.events import ReadyEvent

    @client.socket.dispatch("READY")
    async def _(client: Client, event: ReadyEvent) -> None:
      client.env.RESUME_GATEWAY_URL: str = event.resume_gateway_url
      client.env.SESSION_ID: str = event.session_id

After the connection is closed, your app should open a new connection using :attr:`ReadyEvent.resume_gateway_url <discord.gateway.events.ReadyEvent.resume_gateway_url>` rather than the URL used to initially connect. If your app doesn't use the :attr:`ReadyEvent.resume_gateway_url <discord.gateway.events.ReadyEvent.resume_gateway_url>` when reconnecting, it will experience disconnects at a higher rate than normal.

.. code:: python

    from discord.gateway import DiscordWebSocket, GatewayEvent

    class Default(DiscordWebSocket):
      async def on_reconnect(self, event: GatewayEvent, /) -> None:
        await self.disconnect()
        await self.connect(f"{self.client.env.RESUME_GATEWAY_URL}/?v=10&encoding=json")

Once the new connection is opened, your app should send a :meth:`GatewayEvent.RESUME() <discord.gateway.GatewayEvent.RESUME>` using the :attr:`ReadyEvent.session_id <discord.gateway.events.ReadyEvent.session_id>` and sequence number mentioned above.

.. code:: python

    from discord.gateway import DiscordWebSocket, GatewayEvent

    class Default(DiscordWebSocket):
      async def on_reconnect(self, event: GatewayEvent, /) -> None:
        # ...
        await self.send(GatewayEvent.RESUME(
          token = self.client.env.APPLICATION_TOKEN,
          session_id = self.client.env.SESSION_ID,
          sequence = self.last_sequence
        ))

When resuming, you do not need to send a :meth:`GatewayEvent.IDENTIFY() <discord.gateway.GatewayEvent.IDENTIFY>` after opening the connection.

If successful, the Gateway will send the missed events in order, finishing with a ``RESUMED`` event to signal event replay has finished and that all subsequent events will be new.

.. important::

    When resuming with the :attr:`ReadyEvent.resume_gateway_url <discord.gateway.events.ReadyEvent.resume_gateway_url>`, you need to provide the same version and encoding as the initial connection.

It's possible your app won't reconnect in time to resume, in which case it will receive an :attr:`OpCode.INVALID_SESSION <discord.enums.OpCode.INVALID_SESSION>`. If the :attr:`GatewayEvent.d <discord.gateway.GatewayEvent.d>` field is set to ``False``, your app should disconnect. After disconnect, your app should create a new connection with your cached URL from the :meth:`HTTPClient.get_gateway() <discord.http.HTTPClient.get_gateway>` or the :meth:`HTTPClient.get_gateway_bot() <discord.http.HTTPClient.get_gateway_bot>` endpoint, then send a :meth:`GatewayEvent.IDENTIFY() <discord.gateway.GatewayEvent.IDENTIFY>`.

.. code:: python

    from discord.flags import GatewayIntents
    from discord.gateway import DiscordWebSocket, GatewayEvent

    class Default(DiscordWebSocket):
      async def on_invalid_session(self, event: GatewayEvent, /) -> None:
        await self.disconnect()
        if not event.d:
          await self.connect(f"{self.client.env.RESUME_GATEWAY_URL}/?v=10&encoding=json")
          await self.send(GatewayEvent.IDENTIFY(
            intents = GatewayIntents.default(),
            token = self.client.env.APPLICATION_TOKEN
          ))
        else:
          await self.connect(f"{self.client.env.RESUME_GATEWAY_URL}/?v=10&encoding=json")
          await self.send(GatewayEvent.RESUME(
            token = self.client.env.APPLICATION_TOKEN,
            session_id = self.client.env.SESSION_ID,
            sequence = self.last_sequence
          ))


.. admonition:: Source
    :class: seealso

    `Gateway - Documentation - Discord`_


.. _Gateway - Documentation - Discord: https://docs.discord.com/developers/events/gateway
.. _How Do I Create an Application?: https://guides.demoutrei.dev/discord/api/faq#how-do-i-create-an-application
.. _How Do I Get A Bot Token?: https://guides.demoutrei.dev/discord/api/faq#how-do-i-get-a-bot-token