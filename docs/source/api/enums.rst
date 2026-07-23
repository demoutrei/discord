Enumerations
============


.. autoclass:: discord.enums.ApplicationCommandPermissionType()

.. autoclass:: discord.enums.ApplicationEventWebhookStatus()

.. autoclass:: discord.flags.ApplicationFlag()

.. autoclass:: discord.enums.ApplicationIntegrationType()

.. autoclass:: discord.enums.AutoModerationActionType()

.. autoclass:: discord.enums.DefaultMessageNotificationLevel()

.. autoclass:: discord.enums.ExplicitContentFilterLevel()

.. autoclass:: discord.flags.GatewayIntent()

\* **Thread Members Update** contains different data depending on which intents are used.

\*\* Events under the :attr:`~.GUILD_PRESENCES` and :attr:`~.GUILD_MEMBERS` intents are **turned off by default on all API versions**. If you are using **API v6**, you will receive those events if you are authorized to receive them and have enabled the intents in the `Developer Portal`_. You do not need to use intents on API v6 to receive these events; you just need to enable the flags. If you are using **API v8 or above**, intents are mandatory and must be specified when identifying.

\*\*\* :attr:`~.MESSAGE_CONTENT` does not represent individual events, but rather affects what data is present for events that could contain message content fields.

.. _Developer Portal: https://discord.com/developers/applications

.. autoclass:: discord.enums.GuildAgeRestrictionLevel()

.. autoclass:: discord.enums.GuildFeature()

.. autoclass:: discord.enums.Locale()

.. autoclass:: discord.enums.MembershipState()

.. autoclass:: discord.enums.MFALevel()

.. autoclass:: discord.enums.NameplatePalette()

.. autoclass:: discord.enums.OpCode()

.. autoclass:: discord.flags.PermissionFlag

.. autoclass:: discord.enums.PremiumTier()

.. autoclass:: discord.enums.PremiumType()

.. autoclass:: discord.flags.RoleFlag()

.. autoclass:: discord.enums.StickerFormatType()

.. autoclass:: discord.enums.StickerType()

.. autoclass:: discord.flags.SystemChannelFlag()

.. autoclass:: discord.enums.TeamMemberRole()

.. autoclass:: discord.flags.UserFlag()

.. autoclass:: discord.enums.VerificationLevel()

.. autoclass:: discord.enums.WebhookEventType()