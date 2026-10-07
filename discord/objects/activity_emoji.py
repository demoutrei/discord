from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..types import Optional


@dataclass
class ActivityEmoji:
  animated: Optional[bool]
  """Whether the emoji is animated."""
  
  id: Optional[Snowflake]
  """ID of the emoji."""
  
  name: str
  """Name of the emoji."""