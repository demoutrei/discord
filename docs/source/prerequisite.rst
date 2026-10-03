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

    client = Client()
    client.connect(gateway_cls = Default)

To initially connect to the Gateway API, you must fetch the WSS URL from the :attr:`HTTPClient.get_gateway() <discord.http.HTTPClient.get_gateway>` endpoint and cache it.

.. code:: python

    from discord.gateway import DiscordWebSocket
    from discord.logging import Logger

    class Default(DiscordWebSocket):
      async def setup(self) -> None:
        async with await self.client.http.get_gateway() as response:
          url: str = f"{response["url"]}/v?=10&encoding=json"
        with Logger.debug(f"Cached WSS URL: {url}"):
          self.client.env.WSS_URL: str = url
        await self.connect(self.client.env.WSS_URL)


Hello OpCode
^^^^^^^^^^^^

Upon initiating a connection through the WSS URL, Discord sends an :attr:`OpCode.HELLO <discord.enums.OpCode.HELLO>` event containing a heartbeat interval in milliseconds. You must begin handling heartbeats and send a :attr:`GatewayEvent.IDENTIFY <discord.gateway.GatewayEvent.IDENTIFY>` payload.


Heartbeats
~~~~~~~~~~

Heartbeats are used to maintain an active gateway connection. Upon receiving the :attr:`OpCode.HELLO <discord.enums.OpCode.HELLO>` event, your app should wait ``heartbeat_interval * jitter`` where ``jitter`` is any random value between ``0`` and ``1``, then send its first :attr:`GatewayEvent.HEARTBEAT <discord.gateway.GatewayEvent.HEARTBEAT>` event. From that point until the connection is closed, your app must continually send a heartbeat every ``heartbeat_interval`` milliseconds. If your app fails to send a heartbeat event in time, your connection will be closed and you will be forced to resume.

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

When you send a :attr:`GatewayEvent.HEARTBEAT <discord.gateway.GatewayEvent.HEARTBEAT>` event, Discord will response with a :attr:`OpCode.HEARTBEAT_ACK <discord.enums.OpCode.HEARTBEAT_ACK>` event, which is an acknowledgement that the heartbeat was received.

If the client does not receive a heartbeat ack between its attempts at sending heartbeats, this may be due to a failed or "zombied" connection. The client should immediately terminate the connection with any close code besides ``1000`` or ``1001``, then reconnect and attempt to resume.

In addition to the heartbeat interval, Discord may request additional heartbeats from your app by sending a :attr:`OpCode.HEARTBEAT <discord.enums.OpCode.HEARTBEAT>` event. Upon receiving the event, your app should immediately send back another :attr:`GatewayEvent.HEARTBEAT <discord.gateway.GatewayEvent.HEARTBEAT>` event without waiting the remainder of the current interval.

.. code:: python

    from discord.gateway import DiscordWebSocket, GatewayEvent

    class Default(DiscordWebSocket):
      async def on_heartbeat(self, event: GatewayEvent) -> None:
        await self.send(GatewayEvent.HEARTBEAT(self.last_sequence))


Identifying
~~~~~~~~~~~

After the connection is open and your app is sending heartbeats, you should send a :attr:`GatewayEvent.IDENTIFY <discord.gateway.GatewayEvent.IDENTIFY>` event. The :attr:`OpCode.IDENTIFY <discord.enums.OpCode.IDENTIFY>` event is an initial handshake with the Gateway that's required before your app can begin sending or receiving most Gateway events.

.. code:: python

    from discord.gateway import DiscordWebSocket, GatewayEvent

    class Default(DiscordWebSocket):
      async def on_hello(self, event: GatewayEvent) -> None:
        await self.send(GatewayEvent.IDENTIFY(
          intents = GatewayIntents.default(),
          token = self.client.env.APPLICATION_TOKEN
        ))

After your app sends a valid :attr:`OpCode.IDENTIFY <discord.enums.OpCode.IDENTIFY>` payload, Discord will respond with a ``READY`` :attr:`OpCode.DISPATCH <discord.enums.OpCode.DISPATCH>` event which indicates that your app is in a successfully connected state with the Gateway.


.. _How Do I Create an Application?: https://guides.demoutrei.dev/discord/api/faq#how-do-i-create-an-application
.. _How Do I Get A Bot Token?: https://guides.demoutrei.dev/discord/api/faq#how-do-i-get-a-bot-token