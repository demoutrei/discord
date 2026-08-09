Changelog
=========


v26.1.12-dev
------------

**Added Changes**

- Receive all message-related gateway events.
- Added :class:`~discord.events.MessageReactionRemoveEmojiEvent` event.
- Added :class:`~discord.events.MessageReactionRemoveAllEvent` event.
- Added :class:`~discord.events.MessageReactionRemoveEvent` event.
- Added :class:`~discord.enums.ReactionType` enum.
- Added :class:`~discord.events.MessageReactionAddEvent` event.
- Added :class:`~discord.events.MessageDeleteBulkEvent` event.
- Added :class:`~discord.events.MessageDeleteEvent` event.
- Added :class:`~discord.events.MessageUpdateEvent` event.
- Added :class:`~discord.objects.Message` object.
- Added :class:`~discord.objects.SharedClientTheme` object.
- Added :class:`~discord.objects.BaseThemeType` object.
- Added :class:`~discord.objects.MessageCall` object.
- Added :class:`~discord.objects.Poll` object.
- Added :class:`~discord.objects.PollResults` object.
- Added :class:`~discord.objects.PollAnswerCount` object.
- Added :class:`~discord.enums.PollLayoutType` enum.
- Added :class:`~discord.objects.PollAnswer` object.
- Added :class:`~discord.objects.PollMedia` object.
- Added :class:`~discord.objects.ResolvedData` object.

**Documentation Changes**

- Added missing documentations


v26.1.11
--------

**Added Changes**

- Receive all invite-related gateway events.
- Added :class:`~discord.events.InviteDeleteEvent` event.
- Added :class:`~discord.events.InviteCreateEvent` event.


v26.1.10
--------

**Added Changes**

- Receive all integration-related gateway events.
- :attr:`~discord.objects.Channel.application_id` is now also :attr:`~discord.utils.Nullable`.
- Added :class:`~discord.events.IntegrationDeleteEvent` event.
- Added :class:`~discord.events.IntegrationUpdateEvent` event.
- Added :class:`~discord.events.IntegrationCreateEvent` event.

**Documentation Changes**

- Fixed typos


v26.1.9
-------

**Added Changes**

- Receive all guild-related gateway events.
- Added :class:`~discord.objects.SoundboardSound` object.
- Added :class:`~discord.objects.GuildScheduledEvent` object.
- Added :class:`~discord.objects.GuildScheduledEventRecurrenceRule` object.
- Added :class:`~discord.enums.GuildScheduledEventRecurrenceRuleMonth` enum.
- Added :class:`~discord.objects.GuildScheduledEventRecurrenceRuleNWeekday` object.
- Added :class:`~discord.enums.GuildScheduledEventRecurrenceRuleWeekday` enum.
- Added :class:`~discord.enums.GuildScheduledEventRecurrenceRuleFrequency` enum.
- Added :class:`~discord.objects.GuildScheduledEventEntityMetadata` object.
- Added :class:`~discord.enums.GuildScheduledEventEntityType` enum.
- Added :class:`~discord.enums.GuildScheduledEventStatus` enum.
- Added :class:`~discord.enums.GuildScheduledEventPrivacyLevel` enum.
- Added :class:`~discord.objects.AuditLogEntry` object.
- Added :class:`~discord.objects.OptionalAuditEntryInfo` object.
- Added :class:`~discord.enums.AuditLogEvent` enum.
- Added :class:`~discord.objects.GuildOnboarding` object.
- Added :class:`~discord.enums.OnboardingMode` enum.
- Added :class:`~discord.objects.OnboardingPrompt` object.
- Added :class:`~discord.objects.OnboardingPromptOption` object.
- Added :class:`~discord.enums.OnboardingPromptType` enum.
- Added :class:`~discord.objects.StageInstance` object.
- Added :class:`~discord.enums.StageInstancePrivacyLevel` enum.
- Added :class:`~discord.objects.Integration` object.
- Added :class:`~discord.objects.IntegrationApplication` object.
- Added :class:`~discord.objects.IntegrationAccount` object.
- Added :class:`~discord.enums.IntegrationExpireBehavior` enum.
- Added :class:`~discord.objects.Webhook` object.
- Added :class:`~discord.enums.WebhookType` enum.
- Added :class:`~discord.objects.InviteMetadata` object.
- Added :class:`~discord.objects.Invite` object.
- Added :class:`~discord.flags.GuildInviteFlags` flag.
- Added :class:`~discord.enums.InviteTargetType` enum.
- Added :class:`~discord.enums.InviteType` enum.
- Added :class:`~discord.objects.AuditLogChange` object.
- Added :class:`~discord.events.GuildCreateEvent` event.
- Added :class:`~discord.events.GuildAuditLogEntryCreateEvent` event.
- Added :class:`~discord.events.GuildBanAddEvent` event.
- Added :class:`~discord.events.GuildBanRemoveEvent` event.
- Added :class:`~discord.events.GuildEmojisUpdateEvent` event.
- Added :class:`~discord.events.GuildStickersUpdateEvent` event.
- Added :class:`~discord.events.GuildIntegrationsUpdateEvent` event.
- Added :class:`~discord.events.GuildMemberAddEvent` event.
- Added :class:`~discord.events.GuildMemberRemoveEvent` event.
- Added :class:`~discord.events.GuildMemberUpdateEvent` event.
- Added :class:`~discord.events.GuildMembersChunkEvent` event.
- Added :class:`~discord.events.GuildRoleCreateEvent` event.
- Added :class:`~discord.events.GuildRoleUpdateEvent` event.
- Added :class:`~discord.events.GuildRoleDeleteEvent` event.
- Added :class:`~discord.events.GuildScheduledEventUserAddEvent` event.
- Added :class:`~discord.events.GuildScheduledEventUserRemoveEvent` event.
- Added :class:`~discord.events.GuildSoundboardSoundDeleteEvent` event.
- Added :class:`~discord.events.GuildSoundboardSoundsUpdateEvent` event.
- Added :class:`~discord.events.SoundboardSoundsEvent` event.
- Added :class:`~discord.events.PresenceUpdateEvent` event.
- Added :class:`~discord.objects.ClientStatus` object.
- Added :class:`~discord.objects.Activity` object.
- Added :class:`~discord.objects.ActivityButton` object.
- Added :class:`~discord.flags.ActivityFlags` flag.
- Added :class:`~discord.objects.ActivitySecrets` object.
- Added :class:`~discord.objects.ActivityAssets` object.
- Added :class:`~discord.objects.ActivityParty` object.
- Added :class:`~discord.enums.StatusDisplayType` enum.
- Added :class:`~discord.enums.ActivityType` enum.
- Added :class:`~discord.objects.ActivityTimestamps` object.
- Added :class:`~discord.objects.VoiceState` object.


**Documentation Changes**

- Fix unordered list.


v26.1.8
-------

**Added Changes**

- Added :class:`~discord.enums.EntitlementType` enum.
- Added :class:`~discord.objects.Entitlement` object.
- Receive all entitlement-related gateway events.
- Receive ``ENTITLEMENT_CREATE`` gateway event.


v26.1.7
-------


**Added Changes**

- Receive ``CHANNEL_UPDATE`` gateway event.
- Receive ``CHANNEL_DELETE`` gateway event.
- Receive ``CHANNEL_INFO`` gateway event.
- Added :class:`~discord.events.ChannelInfoEvent` event object.
- Added :class:`~discord.objects.ChannelInfoChannel` object.
- Added :class:`~discord.events.VoiceChannelStatusUpdateEvent` event object.
- Added :class:`~discord.events.VoiceChannelStartTimeUpdateEvent` event object.
- Added :class:`~discord.events.ThreadCreateEvent` event object.
- Receive ``THREAD_UPDATE`` gateway event.
- Receive ``THREAD_DELETE`` gateway event.
- Added :class:`~discord.events.ThreadListSyncEvent` event object.
- Added :class:`~discord.events.ThreadMembersUpdateEvent` event object.
- Added :attr:`~discord.objects.ThreadMember.presence` attribute.
- Added :class:`~discord.events.ChannelPinsUpdateEvent` event object.


**Documentation Changes**

- Added documentation for ``CHANNEL_CREATE`` event.


v26.1.6
-------


**Added Changes**

- Added :class:`~discord.events.AutoModerationActionExecutionEvent` event object.
- Added :class:`~discord.objects.Channel` object.
- Added :class:`~discord.enums.ForumLayoutType` enum.
- Added :class:`~discord.enums.DefaultSortOrderType` enum.
- Added :class:`~discord.objects.DefaultReaction` object.
- Added :class:`~discord.objects.ForumTag` object.
- Added :class:`~discord.flags.ChannelFlags` flag.
- Added :class:`~discord.objects.ThreadMember` object.
- Added :class:`~discord.objects.ThreadMetadata` object.
- Added :class:`~discord.enums.VideoQualityMode` enum.
- Added :class:`~discord.objects.PermissionOverwrite` object.
- Added :class:`~discord.enums.ChannelType` enum.
- Added :class:`~discord.objects.GuildMember` object.
- Added :class:`~discord.flags.GuildMemberFlags` flag.


**Documentation Changes**

- Added Changelog.
- Reconstruct documentation (a bit).


v26.1.4
-------


**Added Changes**

- Manage event listeners.
- Handle dispatch event.
- Handle ``APPLICATION_COMMAND_PERMISSIONS_UPDATE`` dispatch event.
- Receive ``AUTO_MODERATION_RULE_*`` events.
- Added :class:`~discord.objects.AutoModerationRule` object.
- Added :class:`~discord.objects.AutoModerationAction` object.
- Added :class:`~discord.objects.AutoModerationActionMetadata` object.
- Added :class:`~discord.enums.AutoModerationActionType` enum.
- Added :class:`~discord.objects.AutoModerationRuleTriggerMetadata` object.
- Added :class:`~discord.enums.AutoModerationRuleTriggerType` enum.
- Added :class:`~discord.enums.AutoModerationRuleKeywordPresetType` enum.
- Added :class:`~discord.enums.AutoModerationRuleEventType` enum.


**Documentation Changes**

- Build documentation.
- Add ``.readthedocs.yaml`` file.


v26.0.7
-------


**Added Changes**

- Added HTTP endpoint hooks: :meth:`~discord._http.HTTP.get_gateway`, :meth:`~discord._http.HTTP.get_gateway_bot`.
- Connect to the gateway. Defaults to ``True``.
- Added context manager-wise logging.
- Handle heartbeats and :attr:`~discord.enums.OpCode.HELLO`.
- Handle identifying.
- Handle disconnect and reconnect.