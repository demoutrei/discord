from ..snowflake import Snowflake
from ..utils import Nullable
from ._base import BaseObject


class WelcomeScreenChannel(BaseObject):
  channel_id: Snowflake
  """The channels' ID"""

  description: str
  """The description shown for the channel"""

  emoji_id: Nullable[Snowflake]
  """The emoji ID, if the emoji is custom"""

  emoji_name: Nullable[str]
  """The emoji name if custom, the unicode character if standard, or ``None`` if no emoji is set"""