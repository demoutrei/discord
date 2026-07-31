from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Nullable


@dataclass
class WelcomeScreenChannel:
  channel_id: Snowflake
  """The channels' ID"""

  description: str
  """The description shown for the channel"""

  emoji_id: Nullable[Snowflake]
  """The emoji ID, if the emoji is custom"""

  emoji_name: Nullable[str]
  """The emoji name if custom, the unicode character if standard, or ``None`` if no emoji is set"""