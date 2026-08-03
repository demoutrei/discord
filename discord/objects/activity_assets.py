from .._dataclass import dataclass
from ..utils import Optional


@dataclass
class ActivityAssets:
  invite_cover_image: Optional[str]
  """See **Activity Asset Image**. Displayed as a banner on a **Game Invite**."""
  
  large_image: Optional[str]
  """See **Activity Asset Image**."""

  large_url: Optional[str]
  """URL that is opened when clicking on the large image."""

  large_text: Optional[str]
  """Text displayed when hovering over the large image of the activity."""

  small_image: Optional[str]
  """See **Activity Asset Image**."""

  small_url: Optional[str]
  """URL that is opened when clicking on the small image."""

  small_text: Optional[str]
  """Text displayed when hovering over the small image of the activity."""