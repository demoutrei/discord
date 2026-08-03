from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Nullable, Optional


@dataclass
class ChannelInfoChannel:
  id: Snowflake
  """The channel ID."""

  status: Optional[Nullable[str]]
  """The voice channel status."""

  voice_start_time: Optional[Nullable[int]]
  """Unix timestamp (in seconds) of when the voice session started."""