from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Optional


@dataclass
class MessageDeleteBulk:
  channel_id: Snowflake
  """ID of the channel."""

  guild_id: Optional[Snowflake]
  """ID of the guild."""
  
  ids: list[Snowflake]
  """ID of the messages."""