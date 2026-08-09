Discord Objects
===============


.. autoclass:: discord.objects.Activity()


.. autoclass:: discord.objects.ActivityAssets()

**Activity Asset Image**

Activity asset images are arbitrary strings which usually contain snowflake IDs or prefixed image IDs. Treat data within this field carefully, as it is user-specifiable and not sanitized.

To use an external iamge via media proxy, specify the URL as the field's value when sending. You will only receive the ``mp:`` prefix via the gateway.

+-------------------+----------------------------+---------------------------------------------+
| Type              | Format                     | Image URL                                   |
+===================+============================+=============================================+
| Application Asset | ``{application_asset_id}`` | See `Application Asset Image Formatting`_   |
+-------------------+----------------------------+---------------------------------------------+
| Media Proxy Image | ``mp:{image_id}``          | ``https://media.discordapp.net/{image_id}`` |
+-------------------+----------------------------+---------------------------------------------+


.. autoclass:: discord.objects.ActivityButton()


.. autoclass:: discord.objects.ActivityParty()


.. autoclass:: discord.objects.ActivitySecrets()


.. autoclass:: discord.objects.ActivityTimestamps()


.. autoclass:: discord.objects.Application()


.. autoclass:: discord.objects.ApplicationCommandPermissions()


.. autoclass:: discord.objects.ApplicationIntegrationTypeConfiguration()


.. autoclass:: discord.objects.AuditLogEntry()


.. autoclass:: discord.objects.AuditLogChange()

**Audit Log Change Exceptions**

For most objects, the change keys may be any field on the changed object. The following table details the execptions to this pattern.

+---------------------------------------------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Object Changed                                          | Change Key Exceptions                                                                    | Change Object Exceptions                                                                                                     |
+=========================================================+==========================================================================================+==============================================================================================================================+
| :class:`~discord.objects.ApplicationCommandPermissions` | Snowflake as key                                                                         | The :attr:`~discord.objects.AuditLogEntry.changes` array contains objects with a ``key`` field representing the entity whose |
|                                                         |                                                                                          | command was affected (role, channel, or user ID), a previous permissions object (with an ``old_value`` key), and an updated  |
|                                                         |                                                                                          | permissions object (with a ``new_value`` key).                                                                               |
+---------------------------------------------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :class:`~discord.objects.Invite` and                    | Additional ``channel_id`` key (instead of object's :class:`~discord.objects.Channel.id`) |                                                                                                                              |
| :class:`~discord.objects.InviteMetadata`                |                                                                                          |                                                                                                                              |
+---------------------------------------------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :class:`~discord.objects.Role`                          | ``$add`` and ``$remove`` as keys                                                         | ``new_value`` is an array of objects that contain the role ``id`` and ``name``                                               |
+---------------------------------------------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :class:`~discord.objects.Webhook`                       | ``avatar_hash`` key (instead of ``avatar``)                                              |                                                                                                                              |
+---------------------------------------------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+


.. autoclass:: discord.objects.AutoModerationAction()

  .. note::
    :attr:`~discord.objects.AutoModerationAction.metadata` can be omitted based on :attr:`~discord.objects.AutoModerationAction.type`.


.. autoclass:: discord.objects.AutoModerationActionMetadata()


.. autoclass:: discord.objects.AutoModerationRule()
  

.. autoclass:: discord.objects.AutoModerationRuleTriggerMetadata()
  

.. autoclass:: discord.objects.AvatarDecorationData()


.. autoclass:: discord.objects.Channel()


.. autoclass:: discord.objects.ChannelInfoChannel()


.. autoclass:: discord.objects.ClientStatus()


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


.. autoclass:: discord.objects.GuildOnboarding()


.. autoclass:: discord.objects.GuildScheduledEvent()

**Field Requirements By Entity Type**

The following table shows field requirements based on current entity type.

``value``: This field is required to be a non-null value.

``null``: This field is required to be null.

``-``: No strict requirements.

+----------------+------------+-----------------+--------------------+
| Entity Type    | channel_id | entity_metadata | scheduled_end_time |
+================+============+=================+====================+
| STAGE_INSTANCE | value      | null            | -                  |
+----------------+------------+-----------------+--------------------+
| VOICE          | value      | null            | -                  |
+----------------+------------+-----------------+--------------------+
| EXTERNAL       | null       | value \*        | value              |
+----------------+------------+-----------------+--------------------+

\* :attr:`~discord.objects.GuildScheduledEvent.entity_metadata` with a non-null :attr:`~discord.objects.GuildScheduledEventEntityMetadata.location` must be provided.


.. autoclass:: discord.objects.GuildScheduledEventRecurrenceRule()

.. admonition:: System limitations
    :collapsible:

    The current system limitations are present due to how reoccuring event data needs to be displayed in the client. In the future, Discord would like to open the system up to have fewer/none of these restrictions.

    The following fields cannot be set by the client/application:

    - :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.count`
    - :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.end`
    - :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_year_day`

    The following combinations are mutually exclusive:

    - :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_weekday`
    - :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_n_weekday`
    - :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_month` + :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_month_day`

    :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_weekday`

    - Only valid for daily and weekly events (:attr:`~discord.objects.GuildScheduledEventRecurrenceRule.frequency` of :attr:`~discord.enums.GuildScheduledEventRecurrenceRuleFrequency.DAILY` or :attr:`~discord.enums.GuildScheduledEventRecurrenceRuleFrequency.WEEKLY`)
    - When used in a daily event (:attr:`~discord.objects.GuildScheduledEventRecurrenceRule.frequency` is :attr:`~discord.enums.GuildScheduledEventRecurrenceRuleFrequency.DAILY`)

      - The values present in the :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_weekday` event must be a "known set" of weekdays.
      - The following are current allowed "sets":

        - Monday - Friday (``[0, 1, 2, 3, 4]``)
        - Tuesday - Saturday (``[1, 2, 3, 4, 5]``)
        - Sunday - Thursday (``[6, 0, 1, 2, 3]``)
        - Friday & Saturday (``[4, 5]``)
        - Saturday & Sunday (``[5, 6]``)
        - Sunday & Monday (``[6, 0]``)

    - When used in a weekly event (:attr:`~discord.objects.GuildScheduledEventRecurrenceRule.frequency` is :attr:`~discord.enums.GuildScheduledEventRecurrenceRuleFrequency.WEEKLY`)

      - :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_weekday` array currently can only be a length of ``1``.

        - I.e.: You can only select a single day within a weeky to have a recurring event on.
        - If you wish to have multiple days within a week have a recurring event, use a :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.frequency` of :attr:`~discord.enums.GuildScheduledEventRecurrenceRuleFrequency.DAILY`.

      - Also, see ``interval`` bellow for "every-other" week information.

    :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_n_weekday`

    - Only valid for monthly events (:attr:`~discord.objects.GuildScheduledEventRecurrenceRule.frequency` is :attr:`~discord.enums.GuildScheduledEventRecurrenceRuleFrequency.MONTHLY`)
    - :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_n_weekday` array can only be a length of ``1``.

      - I.e.: You can only select a single day within a month to have a recurring event on.

    :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_month` and :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_month_day`

    - Only valid for annual event (:attr:`~discord.objects.GuildScheduledEventRecurrenceRule.frequency` is :attr:`~discord.enums.GuildScheduledEventRecurrenceRuleFrequency.YEARLY`)
    - Both :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_month` and :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_month_day` must be provided.
    - Both :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_month` and :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_month_day` arrays must have a length of ``1``.

      - I.e.: You can only set a single date for annual events.

    :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.interval` can only be set to a value other than ``1`` when :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.frequency` is set to :attr:`~discord.enums.GuildScheduledEventRecurrenceRuleFrequency.WEEKLY`

    - In this situation, interval can be set to ``2``.
    - This allowance enables "every-other week" events.
    - Due to the limitations placed on :attr:`~discord.objects.GuildScheduledEventRecurrenceRule.by_weekday`, this means that if you wish to use "every-other week" functionality you can only do so for a single day.


.. autoclass:: discord.objects.GuildScheduledEventEntityMetadata()


.. autoclass:: discord.objects.GuildScheduledEventRecurrenceRuleNWeekday()


.. autoclass:: discord.objects.IncidentsData()


.. autoclass:: discord.objects.InstallParams()


.. autoclass:: discord.objects.Integration()


.. autoclass:: discord.objects.IntegrationAccount()


.. autoclass:: discord.objects.IntegrationApplication()


.. autoclass:: discord.objects.Invite()


.. autoclass:: discord.objects.InviteMetadata()


.. autoclass:: discord.objects.Message()


.. autoclass:: discord.objects.Nameplate()


.. autoclass:: discord.objects.OnboardingPrompt()


.. autoclass:: discord.objects.OnboardingPromptOption()


.. autoclass:: discord.objects.OptionalAuditEntryInfo()


.. autoclass:: discord.objects.PermissionOverwrite()


.. autoclass:: discord.objects.Role()


.. autoclass:: discord.objects.SessionStartLimit()
  

.. autoclass:: discord.objects.SharedClientTheme()


.. autoclass:: discord.Snowflake()


.. autoclass:: discord.objects.SoundboardSound()


.. autoclass:: discord.objects.StageInstance()


.. autoclass:: discord.objects.Sticker()


.. autoclass:: discord.objects.Team()


.. autoclass:: discord.objects.TeamMember()


.. autoclass:: discord.objects.ThreadMember()


.. autoclass:: discord.objects.ThreadMetadata()


.. autoclass:: discord.objects.UnavailableGuild()


.. autoclass:: discord.objects.User()


.. autoclass:: discord.objects.UserPrimaryGuild()


.. autoclass:: discord.objects.VoiceState()


.. autoclass:: discord.objects.Webhook()


.. autoclass:: discord.objects.WelcomeScreen()


.. autoclass:: discord.objects.WelcomeScreenChannel()


.. _Application Asset Image Formatting: https://docs.discord.com/developers/reference#image-formatting