from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import ISO8601Timestamp, Nullable, Optional


@dataclass
class MessageCall:
  """Information about the call in a private channel."""

  ended_timestamp: Optional[Nullable[ISO8601Timestamp]]
  """Time when call ended."""

  participants: list[Snowflake]
  """Array of user object IDs that participated in the call."""