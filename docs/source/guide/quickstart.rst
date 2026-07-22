Quickstart
==========


.. important::
  This guide expects you already have the :ref:`installed <installation>` in your environment.


Prerequisites
=============


1. Create your ``.env`` file

Your ``.env`` file should contain the following keys:

- ``APPLICATION_TOKEN``: The bot token of your application. You can get this in the **Bot** tab of your application's `Developer Portal <https://discord.com/developers/applications>`_.


Steps
=====


1. **Import modules**

.. code:: python

  from discord import Client
  from discord.flags import GatewayIntent


2. **Configure client**

.. code:: python

  intents = GatewayIntents.default()
  client = Client(intents = intents)


3. **Register event listeners**

.. code:: python

  @client.event_listener("READY")
  async def _(event: ReadyEvent) -> None:
    print("Client is ready!")


.. seealso::
  :ref:`event-reference`


4. **Connect to Discord API**

.. code:: python

  client.connect()