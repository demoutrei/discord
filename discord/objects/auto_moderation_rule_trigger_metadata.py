from ..enums import AutoModerationRuleKeywordPresetType
from ._base import BaseObject


class AutoModerationRuleTriggerMetadata(BaseObject):
  """Additional data used to determine whether a rule should be triggered. Different fields are relevant based on the value of ``trigger_type``."""

  allow_list: list[str]
  """Substrings which should not trigger the rule (maximum of 100 or 1000).

  **Associated trigger types**: :attr:`~discord.enums.AutoModerationRuleTriggerType.KEYWORD`, :attr:`~discord.enums.AutoModerationRuleTriggerType.KEYWORD_PRESET`, :attr:`~discord.enums.AutoModerationRuleTriggerType.MEMBER_PROFILE`

  .. note::
      Each ``allow_list`` keyword can be a phrase which contains multiple words. Wildcard symbols can be used to customize how each keyword will be matched. Rules with :attr:`~discord.enums.AutoModerationRuleTriggerType.KEYWORD` trigger type accept a maximum of 100 keywords. Rules with :attr:`~discord.enums.AutoModerationRuleTriggerType.KEYWORD_PRESET` trigger type accept a maximum of 1000 keywords.
  """

  keyword_filter: list[str]
  """Substrings which will be searched for in content (maximum of 1000).

  **Associated trigger types**: :attr:`~discord.enums.AutoModerationRuleTriggerType.KEYWORD`, :attr:`~discord.enums.AutoModerationRuleTriggerType.MEMBER_PROFILE`

  .. note::
      A keyword can be a phrase which contains multiple words. Wildcard symbols can be used to customize how each keyword will be matched. Each keyword must be 60 characters or less.
  """

  mention_raid_protection_enabled: bool
  """Whether to automatically detect mention raids.

  **Associated trigger types**: :attr:`~discord.enums.AutoModerationRuleTriggerType.MENTION_SPAM`
  """

  mention_total_limit: int
  """Total number of unique role and user mentions allowed per message (maximum of 50).

  **Associated trigger types**: :attr:`~discord.enums.AutoModerationRuleTriggerType.MENTION_SPAM`
  """

  presets: list[AutoModerationRuleKeywordPresetType]
  """The internally pre-defined wordsets which will be searched for in content.

  **Associated trigger types**: :attr:`~discord.enums.AutoModerationRuleTriggerType.KEYWORD_PRESET`
  """

  regex_patterns: list[str]
  """Regular expression patterns which will be matched against content (maximum of 10).

  **Associated trigger types**: :attr:`~discord.enums.AutoModerationRuleTriggerType.KEYWORD`, :attr:`~discord.enums.AutoModerationRuleTriggerType.MEMBER_PROFILE`

  .. note::
      Only Rust-flavored regex is currently supported, which can be tested in online editors such as `Rustexp <https://rustexp.lpil.uk/>`_. Each regex pattern must be 260 characters or less.
  """