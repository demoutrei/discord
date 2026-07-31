Discord Objects
===============


.. autoclass:: discord.objects.Application()


.. autoclass:: discord.objects.ApplicationCommandPermissions()


.. autoclass:: discord.objects.ApplicationIntegrationTypeConfiguration()


.. autoclass:: discord.objects.AutoModerationAction()

  .. note::
    :attr:`~discord.objects.AutoModerationAction.metadata` can be omitted based on :attr:`~discord.objects.AutoModerationAction.type`.


.. autoclass:: discord.objects.AutoModerationActionMetadata()


.. autoclass:: discord.objects.AutoModerationRule()
  

.. autoclass:: discord.objects.AutoModerationRuleTriggerMetadata()
  

.. autoclass:: discord.objects.AvatarDecorationData()


.. autoclass:: discord.objects.Channel()


.. autoclass:: discord.objects.ChannelInfoChannel()


.. autoclass:: discord.objects.Collectible()


.. autoclass:: discord.objects.DefaultReaction()


.. autoclass:: discord.objects.Emoji()


.. autoclass:: discord.objects.Entitlement()


.. autoclass:: discord.objects.ForumTag()

  .. note::
    At most one of :attr:`~discord.objects.ForumTag.emoji_id` and :attr:`~discord.objects.ForumTag.emoji_name` may be set to a non-null value.


.. autoclass:: discord.objects.Guild()


.. autoclass:: discord.objects.GuildApplicationCommandPermissions()


.. autoclass:: discord.objects.GuildMember()


.. autoclass:: discord.objects.GuildScheduledEvent()

Field Requirements By Entity Type
---------------------------------

The following table shows field requirements based on current entity type.

``value``: This field is required to be a non-null value.

``null``: This field is required to be null.

``-``: No strict requirements.

+-------------------------------------------------------------+------------+-----------------+--------------------+
| Entity Type                                                 | channel_id | entity_metadata | scheduled_end_time |
+=============================================================+============+=================+====================+
| ~discord.enums.GuildScheduledEventEntityType.STAGE_INSTANCE | value      | null            | -                  |
+-------------------------------------------------------------+------------+-----------------+--------------------+
| ~discord.enums.GuildScheduledEventEntityType.VOICE          | value      | null            | -                  |
+-------------------------------------------------------------+------------+-----------------+--------------------+
| ~discord.enums.GuildScheduledEventEntityType.EXTERNAL       | null       | value \*        | value              |
+-------------------------------------------------------------+------------+-----------------+--------------------+

\* :attr:`discord.objects.GuildScheduledEvent.entity_metadata` with a non-null :attr:`~discord.objects.GuildScheduledEventEntityMetadata.location` must be provided.


.. autoclass:: discord.objects.IncidentsData()


.. autoclass:: discord.objects.InstallParams()


.. autoclass:: discord.objects.Nameplate()


.. autoclass:: discord.objects.PermissionOverwrite()


.. autoclass:: discord.objects.Role()


.. autoclass:: discord.objects.SessionStartLimit()
  

.. autoclass:: discord.Snowflake()


.. autoclass:: discord.objects.SoundboardSound()


.. autoclass:: discord.objects.Sticker()


.. autoclass:: discord.objects.Team()


.. autoclass:: discord.objects.TeamMember()


.. autoclass:: discord.objects.ThreadMember()


.. autoclass:: discord.objects.ThreadMetadata()


.. autoclass:: discord.objects.UnavailableGuild()


.. autoclass:: discord.objects.User()


.. autoclass:: discord.objects.UserPrimaryGuild()


.. autoclass:: discord.objects.WelcomeScreen()


.. autoclass:: discord.objects.WelcomeScreenChannel()