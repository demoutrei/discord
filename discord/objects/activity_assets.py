from .._dataclass import dataclass
from ..types import MISSING, Optional


@dataclass
class ActivityAssets:
  
  @property
  def invite_cover_image(self) -> Optional[str]:
    """See `Activity Asset Image <https://docs.discord.com/developers/events/gateway-events#activity-object-activity-asset-image>`_. Displayed as a banner on a `Game Invite <https://docs.discord.com/developers/discord-social-sdk/development-guides/managing-game-invites>`_."""
    return self.__dict__.get("invite_cover_image", MISSING)

  @property
  def large_image(self) -> Optional[str]:
    """See `Activity Asset Image <https://docs.discord.com/developers/events/gateway-events#activity-object-activity-asset-image>`_."""
    return self.__dict__.get("large_image", MISSING)

  @property
  def large_text(self) -> Optional[str]:
    """Text displayed when hovering over the large image of the activity."""
    return self.__dict__.get("large_text", MISSING)

  @property
  def large_url(self) -> Optional[str]:
    """URL that is opened when clicking on the large image."""
    return self.__dict__.get("large_url", MISSING)

  @property
  def small_image(self) -> Optional[str]:
    """See `Activity Asset Image <https://docs.discord.com/developers/events/gateway-events#activity-object-activity-asset-image>`_."""
    return self.__dict__.get("small_image", MISSING)

  @property
  def small_text(self) -> Optional[str]:
    """Text displayed when hovering over the small image of the activity."""
    return self.__dict__.get("small_text", MISSING)

  @property
  def small_url(self) -> Optional[str]:
    """URL that is opened when clicking on the small image."""
    return self.__dict__.get("small_url", MISSING)