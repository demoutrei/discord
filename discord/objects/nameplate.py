from .._dataclass import dataclass
from ..enums import NameplatePalette
from ..snowflake import Snowflake


@dataclass
class Nameplate:
  """The nameplate the user has."""
  
  asset: str
  """Path to the nameplate asset"""

  label: str
  """The label of this nameplate. Currently unused"""

  palette: NameplatePalette
  """Background color of the nameplate"""
  
  sku_id: Snowflake
  """ID of the nameplate SKU"""