from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..types import MISSING, Optional


@dataclass
class RoleTags:
  """
  .. note::
      Tags with type ``None`` represent booleans. They will be present and set to ``None`` if they are "true", and will be not present if they are "false".
  """

  @property
  def available_for_purchase(self) -> Optional[None]:
    """Whether this role is available for purchase."""
    return self.__dict__.get("available_for_purchase", MISSING)

  @property
  def bot_id(self) -> Optional[Snowflake]:
    """The ID of the bot this role belongs to."""
    if (data := self.__dict__.get("bot_id", MISSING)) is MISSING: return data
    return Snowflake(data)

  @property
  def guild_connections(self) -> Optional[None]:
    """Whether this role is a guild's linked role."""
    return self.__dict__.get("guild_connections", MISSING)

  @property
  def integration_id(self) -> Optional[Snowflake]:
    """The ID of the integration this role belongs to."""
    if (data := self.__dict__.get("integration_id", MISSING)) is MISSING: return data
    return Snowflake(data)

  @property
  def premium_subscriber(self) -> Optional[None]:
    """Whether this is the guild's Booster role."""
    return self.__dict__.get("premium_subscriber", MISSING)

  @property
  def subscription_listing_id(self) -> Optional[Snowflake]:
    """The ID of this role's subscription SKU and listing."""
    if (data := self.__dict__.get("subscription_listing_id", MISSING)) is MISSING: return data
    return Snowflake(data)