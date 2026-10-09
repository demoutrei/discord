from .._dataclass import dataclass
from ..types import Optional


@dataclass
class ActivityAssets:
  invite_cover_image: Optional[str]
  """See `Activity Asset Image <https://docs.discord.com/developers/events/gateway-events#activity-object-activity-asset-image>`_. Displayed as a banner on a `Game Invite <https://docs.discord.com/developers/discord-social-sdk/development-guides/managing-game-invites>`_."""
  
  large_image: Optional[str]
  """See `Activity Asset Image <https://docs.discord.com/developers/events/gateway-events#activity-object-activity-asset-image>`_."""

  large_text: Optional[str]
  """Text displayed when hovering over the large image of the activity."""

  large_url: Optional[str]
  """URL htat is opened when clicking on the large image."""

  small_image: Optional[str]
  """See `Activity Asset Image <https://docs.discord.com/developers/events/gateway-events#activity-object-activity-asset-image>`_."""

  small_text: Optional[str]
  """Text displayed when hovering over the small image of the activity."""

  small_url: Optional[str]
  """URL that is opened when clicking on the small image."""