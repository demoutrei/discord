from ..enums import NameplatePalette
from ..snowflake import Snowflake
from ._base import BaseObject


class Nameplate(BaseObject):
  """The nameplate the user has."""
  
  asset: str
  """Path to the nameplate asset"""

  label: str
  """The label of this nameplate. Currently unused"""

  palette: NameplatePalette
  """Background color of the nameplate"""
  
  sku_id: Snowflake
  """ID of the nameplate SKU"""