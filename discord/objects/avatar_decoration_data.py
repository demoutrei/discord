from ..snowflake import Snowflake
from ._base import BaseObject


class AvatarDecorationData(BaseObject):
  """The data for the user's avatar decoration"""

  asset: str
  """The avatar decoration hash"""

  sku_id: Snowflake
  """ID of the avatar decoration's SKU"""