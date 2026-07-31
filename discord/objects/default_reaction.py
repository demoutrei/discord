from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Nullable


@dataclass
class DefaultReaction:
  """An object that specifies the emoji to use as the default way to react to a forum post. Exactly one of :attr:`~.emoji_id` and :attr:`~.emoji_name` must be set"""

  emoji_id: Nullable[Snowflake]
  """The ID of a guild's custom emoji"""

  emoji_name: Nullable[str]
  """The unicode character of the emoji"""