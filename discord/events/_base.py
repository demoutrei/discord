from ..utils import Optional, MISSING
from .._dataclass import dataclass


@dataclass
class DispatchEvent:
  def __class_getitem__(cls, name: str) -> Optional[type]:
    if not isinstance(name, str):
      raise TypeError(f"name: Must be an instance of {str}; not {name.__class__}")
    name: str = name.strip().upper()
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
      case "READY":
        from .ready import ReadyEvent
        return ReadyEvent
      case _:
        return MISSING