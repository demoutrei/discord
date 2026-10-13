from .._dataclass import dataclass
from ..snowflake import Snowflake


@dataclass
class UnavailableGuild:
  """Represents an Offline Guild, or a Guild whose information has not been provided through Guild Create events during the Gateway connect."""

  @property
  def id(self) -> Snowflake:
    return Snowflake(self.__dict__["id"])
  
  @property
  def unavailable(self) -> bool:
    return self.__dict__["unavailable"]