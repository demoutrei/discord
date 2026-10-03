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


.. code:: python

    from discord.gateway import DiscordWebSocket, GatewayEvent
    from discord.flags import GatewayIntents

    class Default(DiscordWebSocket):
      async def on_hello(event: GatewayEvent) -> None:
        await self.send(
          GatewayEvent.IDENTIFY(
            intents = GatewayIntents.default(),
            token = self.client.env.APPLICATION_TOKEN
          )
        )


.. _How Do I Create an Application?: https://guides.demoutrei.dev/discord/api/faq#how-do-i-create-an-application
.. _How Do I Get A Bot Token?: https://guides.demoutrei.dev/discord/api/faq#how-do-i-get-a-bot-token