from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..types import MISSING, Optional


@dataclass
class ActivityEmoji:

  @property
  def animated(self) -> Optional[bool]:
    """Whether the emoji is animated."""
    return self.__dict__.get("animated", MISSING)
  
  @property
  def id(self) -> Optional[Snowflake]:
    """ID of the emoji."""
    return self.__dict__.get("id", MISSING)
  
  @property
  def name(self) -> str:
    """Name of the emoji."""
    return self.__dict__["name"]