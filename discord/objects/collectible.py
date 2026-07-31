from .._dataclass import dataclass
from ..utils import Optional
from .nameplate import Nameplate


@dataclass
class Collectible:
  """The collectibles the user has, excluding Avatar Decorations and Profile Effects."""
  
  nameplate: Optional[Nameplate]
  """Object mapping of nameplate data"""