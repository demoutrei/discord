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


Responding to Hello OpCode
^^^^^^^^^^^^^^^^^^^^^^^^^^

Upon initiating a connection through the WSS URL, Discord sends an :attr:`OpCode.HELLO` event containing a heartbeat interval in milliseconds. You must begin handling heartbeats and send a :attr:`GatewayEvent.IDENTIFY` payload.


.. code:: python

    class Default(DiscordWebSocket):
      async def on_hello(event: GatewayEvent) -> None:
        identify_payload: GatewayEvent = GatewayEvent.IDENTIFY(
          intents = self.client.intents,
          token = self.client.token
        )
        await self.send(identify_payload)


.. _How Do I Create an Application?: https://guides.demoutrei.dev/discord/api/faq#how-do-i-create-an-application
.. _How Do I Get A Bot Token?: https://guides.demoutrei.dev/discord/api/faq#how-do-i-get-a-bot-token