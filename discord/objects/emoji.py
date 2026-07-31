from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Nullable, Optional


@dataclass
class Emoji:
  animated: Optional[bool]
  """Whether this emoji is animated"""

  available: Optional[bool]
  """Whether this emoji can be used, may be ``False`` due to loss of Server Boosts"""
  
  id: Nullable[Snowflake]
  """Emoji ID"""

  managed: Optional[bool]
  """Whether this emoji is managed"""

  name: Nullable[str]
  """Emoji name; can be null only in reaction emoji objects"""

  required_colons: Optional[bool]
  """Whether this emoji must be wrapped in colons"""

  roles: Optional[list[Snowflake]]
  """Roles allowed to use this emoji"""