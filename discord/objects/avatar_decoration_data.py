from .._dataclass import dataclass
from ..snowflake import Snowflake


@dataclass
class AvatarDecorationData:
  """The data for the user's avatar decoration"""

  asset: str
  """The avatar decoration hash"""

  sku_id: Snowflake
  """ID of the avatar decoration's SKU"""