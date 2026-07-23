# from ..enums import AutoModerationRuleEventType
from ..enums import AutoModerationRuleTriggerType
from ..snowflake import Snowflake
from ._base import BaseObject
from .auto_moderation_action import AutoModerationAction
from .auto_moderation_rule_trigger_metadata import AutoModerationRuleTriggerMetadata


class AutoModerationRule(BaseObject):
  actions: list[AutoModerationAction]
  """The actions which will execute when the rule is triggered"""
  
  creator_id: Snowflake
  """The user which first created this rule"""

  enabled: bool
  """Whether the rule is enabled"""
  
  event_type: "AutoModerationRuleEventType"
  """The rule event type"""

  exempt_channels: list[Snowflake]
  """The channel IDs that should not be affected by the rule (maximum of 20)"""

  exempt_roles: list[Snowflake]
  """The role IDs that should not be affected by the rule (maximum of 20)"""
  
  guild_id: Snowflake
  """The ID of the guild which this rule belongs to"""
  
  id: Snowflake
  """The ID of this rule"""

  name: str
  """The rule name"""

  trigger_metadata: AutoModerationRuleTriggerMetadata
  """The rule trigger metadata"""

  trigger_type: AutoModerationRuleTriggerType
  """The rule trigger type"""