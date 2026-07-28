from ..enums import EntitlementType
from ..snowflake import Snowflake
from ..utils import ISO8601Timestamp, Nullable, Optional
from ._base import BaseObject


class Entitlement(BaseObject):
  application_id: Snowflake
  """ID of the parent application."""
  
  consumed: Optional[bool]
  """For consumable items, whether or not the entitlement has been consumed."""
  
  deleted: bool
  """Entitlement was deleted."""
  
  ends_at: Nullable[ISO8601Timestamp]
  """Date at which the entitlement is no longer valid."""

  guild_id: Optional[Snowflake]
  """ID of the guild that is granted access to the entitlement's SKU."""
  
  id: Snowflake
  """ID of the entitlement."""

  sku_id: Snowflake
  """ID of the SKU."""

  starts_at: Nullable[ISO8601Timestamp]
  """Start date at which the entitlement is valid."""

  type: EntitlementType
  """Type of entitlement."""

  user_id: Optional[Snowflake]
  """ID of the user that is granted access to the entitlement's SKU."""