from .._dataclass import dataclass
from ..utils import Optional


@dataclass
class ActivityTimestamps:
  end: Optional[int]
  """Unix time (in milliseconds) of when the activity ends."""
  
  start: Optional[int]
  """Unix time (in milliseconds) of when the activity started."""