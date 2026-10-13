from .._dataclass import dataclass
from ..enums import NameplatePalette
from ..snowflake import Snowflake


@dataclass
class Nameplate:
  """The nameplate the user has."""
  
  @property
  def asset(self) -> str:
    """Path to the nameplate asset."""
    return self.__dict__["asset"]

  @property
  def label(self) -> str:
    """The label of this nameplate. Currently unused."""
    return self.__dict__["label"]

  @property
  def palette(self) -> NameplatePalette:
    """Background color of the nameplate."""
    return NameplatePalette(**self.__dict__["palette"])
  
  @property
  def sku_id(self) -> Snowflake:
    """ID of the nameplate SKU."""
    return Snowflake(self.__dict__["sku_id"])