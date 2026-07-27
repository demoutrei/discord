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
      case "READY":
        from .ready import ReadyEvent
        return ReadyEvent
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
      case _:
        return MISSING