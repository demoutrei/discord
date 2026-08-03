from .._dataclass import dataclass
from ..utils import Optional


@dataclass
class ActivityParty:
  id: Optional[str]
  """ID of the party."""

  size: Optional[list[int]]
  """Used to show the party's current and maximum size."""