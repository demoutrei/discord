from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Optional


@dataclass
class AutoModerationActionMetadata:
  """Additional data used when an action is executed. Different fields are relevant based on the value of :attr:`action type <discord.objects.AutoModerationAction.type>`."""

  channel_id: Snowflake
  """Channel to which user content should be logged.

  **Associated action type**: :attr:`~discord.enums.AutoModerationActionType.SEND_ALERT_MESSAGE`
  
  **Constraints**: Existing channel
  """

  custom_message: Optional[str]
  """Additional explanation that will be shown to members whenever their message is blocked.

  **Associated action type**: :attr:`~discord.enums.AutoModerationActionType.BLOCK_MESSAGE`

  **Constraints**: Maximum of ``150`` characters
  """

  duration_seconds: int
  """Timeout duration in seconds.

  **Associated action type**: :attr:`~discord.enums.AutoModerationActionType.TIMEOUT`

  **Constraints**: Maximum of ``2419200`` seconds (4 weeks)
  """