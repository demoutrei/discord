from ..enums import AutoModerationActionType
from ..utils import Optional
from ._base import BaseObject
from .auto_moderation_action_metadata import AutoModerationActionMetadata


class AutoModerationAction(BaseObject):
  """An action which will execute whenever a rule is triggered."""

  metadata: Optional[AutoModerationActionMetadata]
  """Additional metadata needed during execution for this specific action type"""

  type: AutoModerationActionType
  """The type of action"""