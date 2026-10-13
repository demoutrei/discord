from .._dataclass import dataclass
from ..types import MISSING, Optional


@dataclass
class ActivityParty:

  @property
  def id(self) -> Optional[str]:
    """ID of the party."""
    return self.__dict__.get("id", MISSING)

  @property
  def size(self) -> Optional[list[int]]:
    """(current_size, max_size); used to show the party's current and maximum size."""
    return self.__dict__.get("size", MISSING)