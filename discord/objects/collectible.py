from ..utils import Optional
from ._base import BaseObject
from .nameplate import Nameplate


class Collectible(BaseObject):
  """The collectibles the user has, excluding Avatar Decorations and Profile Effects."""
  
  nameplate: Optional[Nameplate]
  """Object mapping of nameplate data"""