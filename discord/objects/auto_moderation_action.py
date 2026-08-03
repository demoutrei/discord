from .._dataclass import dataclass
from ..enums import AutoModerationActionType
from ..utils import Optional
from .auto_moderation_action_metadata import AutoModerationActionMetadata


@dataclass
class AutoModerationAction:
  """An action which will execute whenever a rule is triggered."""

  metadata: Optional[AutoModerationActionMetadata]
  """Additional metadata needed during execution for this specific action type"""

  type: AutoModerationActionType
  """The type of action"""