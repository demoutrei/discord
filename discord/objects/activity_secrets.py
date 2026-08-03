from .._dataclass import dataclass
from ..utils import Optional


@dataclass
class ActivitySecrets:
  join: Optional[str]
  """Secret for joining a party."""

  match: Optional[str]
  """Secret for a specific instanced match."""

  spectate: Optional[str]
  """Secret for spectating a game."""