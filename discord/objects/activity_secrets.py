from .._dataclass import dataclass
from ..types import MISSING, Optional


@dataclass
class ActivitySecrets:
  
  @property
  def join(self) -> Optional[str]:
    """Secret for joining a party."""
    return self.__dict__.get("join", MISSING)

  @property
  def match(self) -> Optional[str]:
    """Secret for a specific instanced match."""
    return self.__dict__.get("match", MISSING)

  @property
  def spectate(self) -> Optional[str]:
    """Secret for spectating a game."""
    return self.__dict__.get("spectate", MISSING)