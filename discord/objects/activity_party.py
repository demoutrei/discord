from .._dataclass import dataclass
from ..types import Optional


@dataclass
class ActivityParty:
  id: Optional[str]
  """ID of the party."""

  size: Optional[list[int]]
  """(current_size, max_size); used to show the party's current and maximum size."""