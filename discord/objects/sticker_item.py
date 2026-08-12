from .._dataclass import dataclass
from ..enums import StickerFormatType
from ..snowflake import Snowflake


@dataclass
class StickerItem:
  format_type: StickerFormatType
  """Type of sticker format."""
  
  id: Snowflake
  """ID of the sticker."""

  name: str
  """Name of the sticker."""