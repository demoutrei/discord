from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Optional


@dataclass
class InviteDeleteEvent:
  channel_id: Snowflake
  """Channel of the invite."""

  code: str
  """Unique invite code."""

  guild_id: Optional[Snowflake]
  """Guild of the invite."""