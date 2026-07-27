from ..snowflake import Snowflake
from ..utils import Nullable, Optional
from ._base import BaseObject


class ChannelInfoChannel(BaseObject):
  id: Snowflake
  """The channel ID."""

  status: Optional[Nullable[str]]
  """The voice channel status."""

  voice_start_time: Optional[Nullable[int]]
  """Unix timestamp (in seconds) of when the voice session started."""