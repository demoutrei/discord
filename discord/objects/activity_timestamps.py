from .._dataclass import dataclass
from ..types import MISSING, Optional


@dataclass
class ActivityTimestamps:

  @property
  def end(self) -> Optional[int]:
    """Unix time (in milliseconds) of when the activity ends."""
    return self.__dict__.get("end", MISSING)
  
  @property
  def start(self) -> Optional[int]:
    """Unix time (in milliseconds) of when the activity started."""
    return self.__dict__.get("start", MISSING)