from ..snowflake import Snowflake
from ..utils import Optional
from ._base import BaseObject


class RoleTags(BaseObject):
  """
  .. note::
      Tags with type ``None`` represent booleans. They will be present and set to ``None`` if they are \"true\", and will be not present if they are \"false\".
  """

  available_for_purchase: Optional[None]
  """Whether this role is available for purchase"""

  bot_id: Optional[Snowflake]
  """The ID of the bot this role belongs to"""

  guild_connections: Optional[None]
  """Whether this role is a guild's linked role"""

  integration_id: Optional[Snowflake]
  """The ID of the integration this role belongs to"""

  premium_subscriber: Optional[None]
  """Whether this is the guild's Booster role"""

  subscription_listing_id: Optional[Snowflake]
  """The ID of this role's subscription sku and listing"""