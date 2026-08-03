from .._dataclass import dataclass
from ..utils import Optional


@dataclass
class ClientStatus:
  desktop: Optional[str]
  """User's status set for an active desktop (Windows, Linux, Mac) application session."""
  
  mobile: Optional[str]
  """User's status set for an active mobile (iOS, Android) application session."""

  web: Optional[str]
  """User's status set for an active web (browser, bot user) application session."""