from .._dataclass import dataclass
from ..snowflake import Snowflake


@dataclass
class RoleSubscriptionData:
  is_renewal: bool
  """Whether this notification is for a renewal rather than a new purchase."""
  
  role_subscription_listing_id: Snowflake
  """The ID of the SKU and listing that the user is subscribed to."""

  tier_name: str
  """The name of the tier that the user is subscribed to."""

  total_months_subscribed: int
  """The cumulative number of months that the user has been subscribed for."""