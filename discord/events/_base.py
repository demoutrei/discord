from ..utils import Optional, MISSING
from .._dataclass import dataclass


@dataclass
class DispatchEvent:
  def __class_getitem__(cls, name: str) -> Optional[type]:
    if not isinstance(name, str):
      raise TypeError(f"name: Must be an instance of {str}; not {name.__class__}")
    name: str = name.strip()
    if not name:
      raise ValueError(f"name: Must not be an empty string")
    match name:
      case "APPLICATION_COMMAND_PERMISSIONS_UPDATE":
        from ..objects import GuildApplicationCommandPermissions
        return GuildApplicationCommandPermissions
      case "AUTO_MODERATION_ACTION_EXECUTION":
        from .auto_moderation_action_execution import AutoModerationActionExecutionEvent
        return AutoModerationActionExecutionEvent
      case "AUTO_MODERATION_RULE_CREATE":
        from ..objects import AutoModerationRule
        return AutoModerationRule
      case "AUTO_MODERATION_RULE_DELETE":
        from ..objects import AutoModerationRule
        return AutoModerationRule
      case "AUTO_MODERATION_RULE_UPDATE":
        from ..objects import AutoModerationRule
        return AutoModerationRule
      case "CHANNEL_CREATE":
        from ..objects import Channel
        return Channel
      case "CHANNEL_DELETE":
        from ..objects import Channel
        return Channel
      case "CHANNEL_INFO":
        from .channel_info import ChannelInfoEvent
        return ChannelInfoEvent
      case "CHANNEL_PINS_UPDATE":
        from .channel_pins_update import ChannelPinsUpdateEvent
        return ChannelPinsUpdateEvent
      case "CHANNEL_UPDATE":
        from ..objects import Channel
        return Channel
      case "ENTITLEMENT_CREATE":
        from ..objects import Entitlement
        return Entitlement
      case "ENTITLEMENT_DELETE":
        from ..objects import Entitlement
        return Entitlement
      case "ENTITLEMENT_UPDATE":
        from ..objects import Entitlement
        return Entitlement
      case "GUILD_AUDIT_LOG_ENTRY_CREATE":
        from .guild_audit_log_entry_create import GuildAuditLogEntryCreateEvent
        return GuildAuditLogEntryCreateEvent
      case "GUILD_BAN_ADD":
        from .guild_ban_add import GuildBanAddEvent
        return GuildBanAddEvent
      case "GUILD_BAN_REMOVE":
        from .guild_ban_remove import GuildBanRemoveEvent
        return GuildBanRemoveEvent
      case "GUILD_CREATE":
        from .guild_create import GuildCreateEvent
        return GuildCreateEvent
      case "GUILD_DELETE":
        from ..objects import UnavailableGuild
        return UnavailableGuild
      case "GUILD_EMOJIS_UPDATE":
        from .guild_emojis_update import GuildEmojisUpdateEvent
        return GuildEmojisUpdateEvent
      case "GUILD_INTEGRATIONS_UPDATE":
        from .guild_integrations_update import GuildIntegrationsUpdateEvent
        return GuildIntegrationsUpdateEvent
      case "GUILD_MEMBER_ADD":
        from .guild_member_add import GuildMemberAddEvent
        return GuildMemberAddEvent
      case "GUILD_MEMBER_REMOVE":
        from .guild_member_remove import GuildMemberRemoveEvent
        return GuildMemberRemoveEvent
      case "GUILD_MEMBER_UPDATE":
        from .guild_member_update import GuildMemberUpdateEvent
        return GuildMemberUpdateEvent
      case "GUILD_MEMBERS_CHUNK":
        from .guild_members_chunk import GuildMembersChunkEvent
        return GuildMembersChunkEvent
      case "GUILD_ROLE_CREATE":
        from .guild_role_create import GuildRoleCreateEvent
        return GuildRoleCreateEvent
      case "GUILD_ROLE_DELETE":
        from .guild_role_delete import GuildRoleDeleteEvent
        return GuildRoleDeleteEvent
      case "GUILD_ROLE_UPDATE":
        from .guild_role_update import GuildRoleUpdateEvent
        return GuildRoleUpdateEvent
      case "GUILD_SCHEDULED_EVENT_CREATE":
        from ..objects import GuildScheduledEvent
        return GuildScheduledEvent
      case "GUILD_SCHEDULED_EVENT_DELETE":
        from ..objects import GuildScheduledEvent
        return GuildScheduledEvent
      case "GUILD_SCHEDULED_EVENT_UPDATE":
        from ..objects import GuildScheduledEvent
        return GuildScheduledEvent
      case "GUILD_SCHEDULED_EVENT_USER_ADD":
        from .guild_scheduled_event_user_add import GuildScheduledEventUserAddEvent
        return GuildScheduledEventUserAddEvent
      case "GUILD_SHCEDULED_EVENT_USER_REMOVE":
        from .guild_scheduled_event_user_remove import GuildScheduledEventUserRemoveEvent
        return GuildScheduledEventUserRemoveEvent
      case "GUILD_SOUNDBOARD_SOUND_CREATE":
        from ..objects import SoundboardSound
        return SoundboardSound
      case "GUILD_SOUNDBOARD_SOUND_DELETE":
        from .guild_soundboard_sound_delete import GuildSoundboardSoundDeleteEvent
        return GuildSoundboardSoundDeleteEvent
      case "GUILD_SOUNDBOARD_SOUND_UPDATE":
        from ..objects import SoundboardSound
        return SoundboardSound
      case "GUILD_SOUNDBOARD_SOUNDS_UPDATE":
        from .guild_soundboard_sounds_update import GuildSoundboardSoundsUpdateEvent
        return GuildSoundboardSoundsUpdateEvent
      case "GUILD_STICKERS_UPDATE":
        from .guild_stickers_update import GuildStickersUpdateEvent
        return GuildStickersUpdateEvent
      case "GUILD_UPDATE":
        from ..objects import Guild
        return Guild
      case "READY":
        from .ready import ReadyEvent
        return ReadyEvent
      case "SOUNDBOARD_SOUNDS":
        from .soundboard_sounds import SoundboardSoundsEvent
        return SoundboardSoundsEvent
      case "THREAD_CREATE":
        from .thread_create import ThreadCreateEvent
        return ThreadCreateEvent
      case "THREAD_DELETE":
        from ..objects import Channel
        return Channel
      case "THREAD_LIST_SYNC":
        from .thread_list_sync import ThreadListSyncEvent
        return ThreadListSyncEvent
      case "THREAD_MEMBERS_UPDATE":
        from .thread_members_update import ThreadMembersUpdateEvent
        return ThreadMembersUpdateEvent
      case "THREAD_UPDATE":
        from ..objects import Channel
        return Channel
      case "VOICE_CHANNEL_START_TIME_UPDATE":
        from .voice_channel_start_time_update import VoiceChannelStartTimeUpdateEvent
        return VoiceChannelStartTimeUpdateEvent
      case "VOICE_CHANNEL_STATUS_UPDATE":
        from .voice_channel_status_update import VoiceChannelStatusUpdateEvent
        return VoiceChannelStatusUpdateEvent
    return MISSING