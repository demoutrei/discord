Activity
========


.. autoclass:: discord.objects.Activity()


.. autoclass:: discord.objects.ActivityTimestamps()


Enumerations
++++++++++++


.. autoclass:: discord.enums.ActivityType()

.. important::
    If the presence author's Profile Privacy Setting is set to ``Friends Only``, or to ``Friends & Small Servers Only`` in a guild with more than 200 members, their :attr:`custom status <discord.enums.ActivityType.CUSTOM>` is omitted from ``activities`` in :attr:`OpCode.PRESENCE_UPDATE` events dispatched to that guild. This applies to any subscription to the guild's presence, including bots and apps. Other activity types are not affected by this setting.

.. note::
    :attr:`ActivityType.STREAMING <discord.enums.ActivityType.STREAMING>` currently only supports Twitch and YouTube. Only ``https://twitch.tv/`` and ``https://youtube.com/`` urls will work.


.. autoclass:: discord.enums.StatusDisplayType()

.. note::
    This applies to all activity types. "Listening" was used to serve as a consistent example of what different fields might be used for.