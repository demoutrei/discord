from .._dataclass import dataclass
from ..enums import AutoModerationRuleTriggerType
from ..objects import AutoModerationAction
from ..snowflake import Snowflake
from ..utils import Nullable, Optional


@dataclass
class AutoModerationActionExecutionEvent:
  """Received when a rule is triggered and an action is executed (e.g. when a message is blocked)."""

  action: AutoModerationAction
  """Action which was executed"""

  alert_system_message_id: Optional[Snowflake]
  """ID of any system auto moderation messages posted as a result of this action.

  .. note::
      :attr:`~.alert_system_message_id` will not exist if this event does not correspond to an action with type :attr:`~discord.enums.AutoModerationActionType`.
  """

  channel_id: Optional[Snowflake]
  """ID of the channel in which user content was posted"""

  content: str
  """User-generated text content

  .. note::
      :attr:`~discord.flags.GatewayIntent.MESSAGE_CONTENT` gateway intent is required to receive the :attr:`~.content` and :attr:`~.matched_content` fields.
  """

  guild_id: Snowflake
  """ID of the guild in which action was executed"""

  matched_content: Nullable[str]
  """Substring in content that triggered the rule.

  .. note::
      :attr:`~discord.flags.GatewayIntent.MESSAGE_CONTENT` gateway intent is required to receive the :attr:`~.content` and :attr:`~.matched_content` fields.
  """

  matched_keyword: Nullable[str]
  """Word or phrase configured in the rule that triggered the rule"""

  message_id: Optional[Snowflake]
  """ID of any user message which content belongs to.

  .. note::
      :attr:`~.message_id` will not exist if message was blocked by Auto Moderation or content was not part of any message.
  """

  rule_id: Snowflake
  """ID of the rule which action belongs to"""

  rule_trigger_type: AutoModerationRuleTriggerType
  """Trigger type of rule which was triggered"""

  user_id: Snowflake
  """ID of the user which generated the content which triggered the rule"""