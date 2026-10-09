from .._dataclass import dataclass
from ..types import Optional


@dataclass
class ActivitySecrets:
  join: Optional[str]
  """Secret for joining a party."""

  match: Optional[str]
  """Secret for a specific instanced match."""

  spectate: Optional[str]
  """Secret for spectating a game."""