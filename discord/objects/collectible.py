from .._dataclass import dataclass
from ..types import MISSING, Optional
from .nameplate import Nameplate


@dataclass
class Collectible:
  """The collectibles the user has, excluding Avatar Decorations and Profile Effects."""
  
  @property
  def nameplate(self) -> Optional[Nameplate]:
    """Object mapping of nameplate data."""
    if (data := self.__dict__.get("nameplate", MISSING)) is MISSING: return data
    return Nameplate(**data)