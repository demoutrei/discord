from .._dataclass import dataclass
from ..snowflake import Snowflake


@dataclass
class AvatarDecorationData:
  """The data for the user's avatar decoration."""

  @property
  def asset(self) -> str:
    """The avatar decoration hash."""
    return self.__dict__["asset"]

  @property
  def sku_id(self) -> Snowflake:
    """ID of the avatar decoration's SKU."""
    return Snowflake(self.__dict__["sku_id"])